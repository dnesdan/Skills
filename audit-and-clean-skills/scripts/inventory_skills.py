#!/usr/bin/env python3
"""Create a secret-minimizing, read-only inventory of agent skill directories."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", re.DOTALL)
IGNORED_PARTS = {".git", "__pycache__", ".DS_Store"}


def owner_class(path: Path) -> str:
    text = str(path)
    if "/plugins/cache/" in text or "/plugins/" in text:
        return "plugin-managed"
    if "/.codex/skills/.system/" in text:
        return "system"
    if "/.codex/skills/" in text:
        return "codex-user"
    if "/.agents/skills/" in text:
        return "cross-client-user"
    if "/.claude/skills/" in text:
        return "claude-user"
    if "/.codex/skills" in text or "/.agents/skills" in text or "/.claude/skills" in text:
        return "project"
    return "user-specified"


def parse_frontmatter(skill_md: Path) -> tuple[str | None, str | None, bool]:
    try:
        text = skill_md.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return None, None, False
    match = FRONTMATTER_RE.search(text)
    if not match:
        return None, None, False
    frontmatter = match.group(1)
    try:
        import yaml  # type: ignore
    except ImportError:
        return parse_simple_frontmatter(frontmatter)
    try:
        fields = yaml.safe_load(frontmatter)
        if not isinstance(fields, dict):
            return None, None, False
        name = fields.get("name")
        description = fields.get("description")
        return (
            str(name).strip() if name is not None else None,
            str(description).strip() if description is not None else None,
            True,
        )
    except (yaml.YAMLError, ValueError, TypeError):
        return parse_simple_frontmatter(frontmatter)


def parse_simple_frontmatter(frontmatter: str) -> tuple[str | None, str | None, bool]:
    fields: dict[str, str] = {}
    lines = frontmatter.splitlines()
    index = 0
    while index < len(lines):
        match = re.match(r"^(name|description):\s*(.*)$", lines[index])
        if not match:
            index += 1
            continue
        key, value = match.groups()
        if value in {"|", ">", "|-", ">-", "|+", ">+"}:
            index += 1
            block = []
            while index < len(lines) and (not lines[index].strip() or lines[index][0].isspace()):
                block.append(lines[index].strip())
                index += 1
            value = "\n".join(block) if value.startswith("|") else " ".join(block)
            fields[key] = value.strip()
            continue
        fields[key] = value.strip().strip("\"'")
        index += 1
    return fields.get("name"), fields.get("description"), bool(fields)


def symlink_ancestors(path: Path) -> list[str]:
    ancestors = []
    current = path.absolute()
    for candidate in [current, *current.parents]:
        try:
            if candidate.is_symlink():
                ancestors.append(str(candidate))
        except OSError:
            continue
    return sorted(ancestors)


def git_metadata(directory: Path) -> dict:
    def run(*args: str) -> str | None:
        try:
            result = subprocess.run(
                ["git", "-C", str(directory), *args],
                capture_output=True,
                check=False,
                text=True,
                timeout=3,
            )
        except (OSError, subprocess.TimeoutExpired):
            return None
        return result.stdout.strip() if result.returncode == 0 else None

    root = run("rev-parse", "--show-toplevel")
    if not root:
        return {"repository": None, "git_tracked": None, "git_dirty": None}
    try:
        relative = str(directory.resolve().relative_to(Path(root).resolve()))
    except ValueError:
        relative = "."
    tracked = run("ls-files", "--error-unmatch", f"{relative}/SKILL.md") is not None
    status = run("status", "--porcelain", "--untracked-files=normal", "--", relative)
    return {
        "repository": root,
        "git_tracked": tracked,
        "git_dirty": bool(status) if status is not None else None,
    }


def directory_hash(directory: Path) -> str | None:
    digest = hashlib.sha256()
    try:
        files = sorted(
            path
            for path in directory.rglob("*")
            if path.is_file() and not any(part in IGNORED_PARTS for part in path.parts)
        )
        for path in files:
            relative = path.relative_to(directory).as_posix().encode()
            digest.update(len(relative).to_bytes(8, "big"))
            digest.update(relative)
            data = path.read_bytes()
            digest.update(len(data).to_bytes(8, "big"))
            digest.update(data)
    except OSError:
        return None
    return digest.hexdigest()


def discover(root: Path) -> list[Path]:
    if not root.exists() and not root.is_symlink():
        return []
    if root.name == "SKILL.md":
        return [root.parent]
    if (root / "SKILL.md").exists() or (root / "SKILL.md").is_symlink():
        return [root]
    found: list[Path] = []
    for current, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(name for name in dirs if name not in IGNORED_PARTS)
        if "SKILL.md" in files:
            found.append(Path(current))
            dirs[:] = []
    return found


def count_kind(directory: Path, kind: str) -> int:
    target = directory / kind
    if not target.is_dir():
        return 0
    try:
        return sum(1 for path in target.rglob("*") if path.is_file())
    except OSError:
        return 0


def record(display_path: Path) -> dict:
    is_link = display_path.is_symlink()
    link_target = None
    broken = False
    if is_link:
        try:
            link_target = os.readlink(display_path)
            broken = not display_path.exists()
        except OSError:
            broken = True
    canonical = display_path.resolve(strict=False)
    skill_md = canonical / "SKILL.md"
    name, description, frontmatter_valid = parse_frontmatter(skill_md)
    try:
        stat = skill_md.stat()
        line_count = len(skill_md.read_bytes().splitlines())
        byte_count = stat.st_size
    except OSError:
        line_count = 0
        byte_count = 0
    result = {
        "path": str(display_path.absolute()),
        "canonical_path": str(canonical),
        "owner_class": owner_class(display_path.absolute()),
        "is_symlink": is_link,
        "symlink_ancestors": symlink_ancestors(display_path),
        "symlink_target": link_target,
        "broken_symlink": broken,
        "name": name,
        "description": description,
        "description_chars": len(description or ""),
        "frontmatter_valid": frontmatter_valid,
        "skill_md_bytes": byte_count,
        "skill_md_lines": line_count,
        "directory_sha256": None if broken else directory_hash(canonical),
        "scripts": count_kind(canonical, "scripts"),
        "references": count_kind(canonical, "references"),
        "assets": count_kind(canonical, "assets"),
        "agent_metadata": count_kind(canonical, "agents"),
    }
    result.update(git_metadata(canonical))
    return result


def grouped(records: list[dict], field: str, minimum: int = 2) -> list[dict]:
    values: dict[str, list[str]] = defaultdict(list)
    for item in records:
        value = item.get(field)
        if value:
            values[str(value)].append(item["path"])
    return [
        {field: value, "paths": sorted(paths)}
        for value, paths in sorted(values.items())
        if len(paths) >= minimum
    ]


def markdown_report(payload: dict) -> str:
    summary = payload["summary"]
    lines = [
        "# Skill inventory",
        "",
        f"Generated: {payload['generated_at']}",
        "",
        f"- Roots requested: {summary['roots_requested']}",
        f"- Roots found: {summary['roots_found']}",
        f"- Skill paths: {summary['skill_paths']}",
        f"- Canonical skill directories: {summary['canonical_skills']}",
        f"- Symlinks: {summary['symlinks']}",
        f"- Paths below a symlinked ancestor: {summary['paths_below_symlink_ancestor']}",
        f"- Broken symlinks: {summary['broken_symlinks']}",
        f"- Description characters: {summary['description_chars']}",
        "",
        "## Groups requiring review",
        "",
        f"- Alias groups: {len(payload['alias_groups'])}",
        f"- Exact-copy groups: {len(payload['exact_copy_groups'])}",
        f"- Name collisions: {len(payload['name_collisions'])}",
        "",
        "Exact copies and name collisions are candidates only; they are not automatic merge or deletion decisions.",
        "",
        "## Skills",
        "",
        "| Name | Owner | Path | Link | Hash | Valid |",
        "|---|---|---|---:|---|---:|",
    ]
    for item in payload["skills"]:
        lines.append(
            f"| {item['name'] or '—'} | {item['owner_class']} | `{item['path']}` | "
            f"{'yes' if item['is_symlink'] else 'no'} | "
            f"{(item['directory_sha256'] or '—')[:12]} | "
            f"{'yes' if item['frontmatter_valid'] else 'no'} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", action="append", required=True, help="Skill root to scan; repeatable")
    parser.add_argument("--output-dir", required=True, help="Directory for inventory.json and inventory.md")
    args = parser.parse_args()

    roots = [Path(value).expanduser().absolute() for value in args.root]
    found_roots = [root for root in roots if root.exists() or root.is_symlink()]
    paths = sorted({path.absolute() for root in found_roots for path in discover(root)}, key=str)
    records = [record(path) for path in paths]

    canonical_groups = grouped(records, "canonical_path")
    exact_copy_groups = []
    hashes: dict[str, list[dict]] = defaultdict(list)
    for item in records:
        if item["directory_sha256"]:
            hashes[item["directory_sha256"]].append(item)
    for digest, items in sorted(hashes.items()):
        canonical = sorted({item["canonical_path"] for item in items})
        if len(canonical) > 1:
            exact_copy_groups.append({"directory_sha256": digest, "canonical_paths": canonical})

    payload = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "roots": [{"path": str(root), "exists": root in found_roots} for root in roots],
        "summary": {
            "roots_requested": len(roots),
            "roots_found": len(found_roots),
            "skill_paths": len(records),
            "canonical_skills": len({item["canonical_path"] for item in records}),
            "symlinks": sum(bool(item["is_symlink"]) for item in records),
            "paths_below_symlink_ancestor": sum(bool(item["symlink_ancestors"]) for item in records),
            "broken_symlinks": sum(bool(item["broken_symlink"]) for item in records),
            "description_chars": sum(item["description_chars"] for item in records),
        },
        "skills": records,
        "alias_groups": canonical_groups,
        "exact_copy_groups": exact_copy_groups,
        "name_collisions": grouped(records, "name"),
    }

    output = Path(args.output_dir).expanduser().absolute()
    output.mkdir(parents=True, exist_ok=True)
    (output / "inventory.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    (output / "inventory.md").write_text(markdown_report(payload), encoding="utf-8")
    print(output / "inventory.json")
    print(output / "inventory.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
