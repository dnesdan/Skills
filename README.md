# Skills

A focused collection of multi-agent planning and delivery skills for shaping features, evaluating redesigns, checking release readiness, and coordinating implementation safely.

## Included Skills

| Skill | Folder | Type | Description |
| --- | --- | --- | --- |
| Feature Planning Swarm | `feature-planning-swarm` | Advisory swarm | Turns a feature idea into multiple concrete implementation plans with one recommended path. |
| Redesign Swarm | `redesign-swarm` | Advisory swarm | Analyzes an existing surface and proposes redesign directions with tradeoffs and a recommendation. |
| Release Readiness Swarm | `release-readiness-swarm` | Advisory swarm | Assesses whether an app, feature, or build is ready to ship and returns one clear release verdict. |
| Implementation Orchestrator | `implementation-orchestrator` | Execution orchestrator | Converts an approved plan into dependency-aware work packets, parallel execution waves, and validation gates. |

## Suggested Flow

1. Use `feature-planning-swarm` when a feature idea needs shaping before coding.
2. Use `redesign-swarm` when a current flow or screen needs a stronger UX or visual direction.
3. Use `release-readiness-swarm` before shipping a build, major feature, or redesign.
4. Use `implementation-orchestrator` after a plan has been chosen and the work should actually be executed.

## Install

Place these skill folders under `$CODEX_HOME/skills` or `~/.codex/skills` so Codex can discover them automatically.

## Structure

Each skill is self-contained:

- `SKILL.md` defines when to use the skill and how the workflow should run.
- `agents/openai.yaml` provides UI-facing metadata for the skill picker and prompt chips.

## Design Principles

- Advisory swarms stay read-only and converge on one synthesized recommendation.
- The orchestrator separates planning from execution and enforces explicit file ownership.
- Skills are intentionally narrow so the main agent can compose them without mixing incompatible goals.
