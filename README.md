# Skills

A focused collection of reusable Codex skills for product planning, delivery orchestration, store screenshot production, redesign evaluation, and release readiness.

## Included Skills

| Skill | Folder | Type | Description |
| --- | --- | --- | --- |
| Feature Planning Swarm | `feature-planning-swarm` | Advisory swarm | Turns a feature idea into multiple concrete implementation plans with one recommended path. |
| Feature Extension Swarm | `feature-extension-swarm` | Advisory swarm | Scans the current repo and app surface to propose the most valuable next feature extensions for competitiveness. |
| Redesign Swarm | `redesign-swarm` | Advisory swarm | Analyzes an existing surface and proposes redesign directions with tradeoffs and a recommendation. |
| Release Readiness Swarm | `release-readiness-swarm` | Advisory swarm | Assesses whether an app, feature, or build is ready to ship and returns one clear release verdict. |
| Implementation Orchestrator | `implementation-orchestrator` | Execution orchestrator | Converts an approved plan into dependency-aware work packets, parallel execution waves, and validation gates. |
| Store Framed Screenshots | `store-framed-screenshots` | Marketing asset workflow | Creates consistent App Store and Google Play framed screenshots from truthful raw app captures using internal imagegen. |
| Cross-Store Ratings Report | `cross-store-ratings-report` | Store operations report | Produces private portfolio ratings/reviews reports from `asc` and the Google Play developer client, without public scraping. |
| Computer Use Enable | `computer-use-enable` | Local tooling repair | Enables or repairs Dan's bundled Codex Computer Use plugin setup. |
| Reddit Promo Writing | `reddit-promo-writing` | Marketing writing workflow | Drafts honest, subreddit-aware promo and feedback posts for Dan's apps from local source context. |

## Suggested Flow

1. Use `feature-planning-swarm` when a feature idea needs shaping before coding.
2. Use `feature-extension-swarm` when you want the repo analyzed for product gaps and the strongest next features to add.
3. Use `redesign-swarm` when a current flow or screen needs a stronger UX or visual direction.
4. Use `release-readiness-swarm` before shipping a build, major feature, or redesign.
5. Use `implementation-orchestrator` after a plan has been chosen and the work should actually be executed.
6. Use `store-framed-screenshots` when raw app screenshots need polished store-ready frames, exact dimensions, localization, and validation.
7. Use `cross-store-ratings-report` when ratings/reviews need to be pulled from App Store Connect and Google Play developer tooling across the portfolio.
8. Use `computer-use-enable` when Codex Computer Use is disabled or missing on Dan's Mac.
9. Use `reddit-promo-writing` when an app needs a Reddit post, feedback request, or launch/update copy.

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
