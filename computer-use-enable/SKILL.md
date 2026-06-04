---
name: computer-use-enable
description: Enable or repair Codex Computer Use setup on macOS. Use when Computer Use is missing, disabled, not callable, needs config.toml/plugin setup, plugin cache installation, or a Codex desktop/plugin configuration change is needed.
---

# Computer Use Enable

Use this skill when the user asks to enable, fix, restore, or verify Computer Use in Codex.

## Goal

Make the bundled `computer-use@openai-bundled` plugin available to Codex without disturbing unrelated Codex configuration.

## Evidence First

Check current state before editing:

- Codex config: `$CODEX_HOME/config.toml` or `~/.codex/config.toml`
- Recent config backups: `$CODEX_HOME/config.toml.backup-*` or `~/.codex/config.toml.backup-*`
- Bundled plugin cache/marketplace paths under `$CODEX_HOME/plugins` or `~/.codex/plugins`, and the Codex.app resources when present
- Plugin installation status from `codex plugin list`
- Available tools in the current session, especially `mcp__computer_use__`

Use `rg` or small `sed` reads. Do not print secrets.

## Expected Config

The minimal config entry is:

```toml
[plugins."computer-use@openai-bundled"]
enabled = true
```

Add this only if it is missing. If the plugin block exists, preserve existing keys and only set `enabled = true` when needed.

The bundled marketplace should also be registered:

```toml
[marketplaces.openai-bundled]
source_type = "local"
source = "/Applications/Codex.app/Contents/Resources/plugins/openai-bundled"
```

`last_updated = "..."` may also appear and should be preserved.

The plugin should be installed into the local plugin cache, typically under:

```text
~/.codex/plugins/cache/openai-bundled/computer-use/<version>
```

## Workflow

1. Inspect `~/.codex/config.toml`.
2. Make a timestamped backup before editing if no fresh backup exists for this repair.
3. Inspect plugin status:
   - Run `codex plugin list` or `'/Applications/Codex.app/Contents/Resources/codex' plugin list`.
   - If `computer-use@openai-bundled` is `installed, enabled`, do not reinstall.
   - If it is `not installed`, install it with `codex plugin add computer-use@openai-bundled`.
4. Patch the config narrowly when the install command cannot do it or when config is inconsistent:
   - preserve unrelated plugin settings
   - preserve marketplace/source settings
   - do not rewrite formatting unnecessarily
5. Verify:
   - config contains the enabled plugin block
   - `codex plugin list` reports `computer-use@openai-bundled` as `installed, enabled`
   - the local cache contains `openai-bundled/computer-use/<version>` with `.codex-plugin/`, `.mcp.json`, and the Computer Use app bundle
   - Codex session exposes Computer Use tools after restart/reload, when that can be checked
6. If a restart is required, say so clearly and stop after the config, plugin status, and cache are correct.

## Validation Commands

Useful read-only checks:

```bash
rg -n 'computer-use|openai-bundled|plugins' ~/.codex/config.toml
codex plugin list
find ~/.codex/plugins/cache/openai-bundled/computer-use -maxdepth 2 -print 2>/dev/null
find /Applications/Codex.app/Contents/Resources/plugins/openai-bundled -maxdepth 2 -print 2>/dev/null
```

If `codex` on `PATH` is unavailable or resolves to a different installation, use the bundled CLI:

```bash
'/Applications/Codex.app/Contents/Resources/codex' plugin list
'/Applications/Codex.app/Contents/Resources/codex' plugin add computer-use@openai-bundled
```

Use Computer Use itself only after confirming the tool is available in the active session.

## Guardrails

- Do not reset the whole Codex config.
- Do not delete plugin caches unless the user explicitly asks.
- Do not install unrelated plugins.
- Editing `~/.codex/config.toml` may require permission outside the workspace; request escalation normally.
- Installing the bundled plugin writes outside the workspace; request escalation normally.
- If the session still lacks Computer Use after config, plugin status, and cache are correct, the likely stopping condition is a full Codex restart or plugin reload, not more config churn.
