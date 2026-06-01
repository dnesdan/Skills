---
name: computer-use-enable
description: Enable or repair Dan's Codex Computer Use setup on this Mac. Use when Computer Use is missing, disabled, not callable, needs config.toml/plugin setup, or a Codex desktop/plugin configuration change is needed.
---

# Computer Use Enable

Use this skill when Dan asks to enable, fix, restore, or verify Computer Use in Codex.

## Goal

Make the bundled `computer-use@openai-bundled` plugin available to Codex without disturbing unrelated Codex configuration.

## Evidence First

Check current state before editing:

- Codex config: `/Users/dan/.codex/config.toml`
- Recent config backups: `/Users/dan/.codex/config.toml.backup-*`
- Bundled plugin cache/marketplace paths under `/Users/dan/.codex/plugins` and the Codex.app resources when present
- Available tools in the current session, especially `mcp__computer_use__`

Use `rg` or small `sed` reads. Do not print secrets.

## Expected Config

The minimal config entry Dan has used successfully is:

```toml
[plugins."computer-use@openai-bundled"]
enabled = true
```

Add this only if it is missing. If the plugin block exists, preserve existing keys and only set `enabled = true` when needed.

## Workflow

1. Inspect `/Users/dan/.codex/config.toml`.
2. Make a timestamped backup before editing if no fresh backup exists for this repair.
3. Patch the config narrowly:
   - preserve unrelated plugin settings
   - preserve marketplace/source settings
   - do not rewrite formatting unnecessarily
4. Verify:
   - config contains the enabled plugin block
   - Codex session exposes Computer Use tools after restart/reload, when that can be checked
5. If a restart is required, say so clearly and stop after the config is correct.

## Validation Commands

Useful read-only checks:

```bash
rg -n 'computer-use|openai-bundled|plugins' /Users/dan/.codex/config.toml
ls -la /Users/dan/.codex/plugins /Applications/Codex.app/Contents/Resources/plugins 2>/dev/null
```

Use Computer Use itself only after confirming the tool is available in the active session.

## Guardrails

- Do not reset the whole Codex config.
- Do not delete plugin caches unless Dan explicitly asks.
- Do not install unrelated plugins.
- Editing `/Users/dan/.codex/config.toml` may require permission outside the workspace; request escalation normally.
- If the session still lacks Computer Use after config is fixed, the likely stopping condition is a Codex restart or plugin reload, not more config churn.
