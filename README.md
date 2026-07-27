# Skills

A focused collection of reusable Codex skills for product planning, delivery orchestration, current WWDC 2026 Apple and Google I/O 2026 Android design, animation review, store screenshot production, redesign evaluation, and release readiness.

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
| Apple Design | `apple-design` | Current native design guidance | Applies the WWDC 2026 baseline with Xcode 27, current SwiftUI, Liquid Glass, adaptive layout, Metal shaders, and accessibility. |
| Android Design | `android-design` | Current native design guidance | Applies the Google I/O 2026 Compose-first baseline with Android 17 adaptive UI, Material 3 Expressive, Navigation 3, AGSL, and accessibility. |
| Find Apple Animation Opportunities | `find-apple-animation-opportunities` | Read-only motion discovery | Finds restrained SwiftUI, Liquid Glass, transition, and shader opportunities using the WWDC 2026 baseline. |
| Find Android Animation Opportunities | `find-android-animation-opportunities` | Read-only motion discovery | Finds restrained Compose, Material, adaptive, shared-transition, and shader opportunities using the I/O 2026 baseline. |
| Review Apple Animations | `review-apple-animations` | Read-only motion review | Reviews SwiftUI motion, Liquid Glass, Metal shaders, accessibility, energy, and performance against WWDC 2026. |
| Review Android Animations | `review-android-animations` | Read-only motion review | Reviews Compose motion, Material 3 Expressive, Navigation 3, AGSL, accessibility, and performance against I/O 2026. |

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
10. Use `apple-design` or `android-design` when designing, implementing, or critiquing a native interface.
11. Use the platform-specific `find-*-animation-opportunities` skill to find missing motion without changing code.
12. Use the platform-specific `review-*-animations` skill to review motion that already exists.

## Install

Place these skill folders under `$CODEX_HOME/skills` or `~/.codex/skills` so Codex can discover them automatically.

## Structure

Each skill is self-contained:

- `SKILL.md` defines when to use the skill and how the workflow should run.
- `agents/openai.yaml` provides UI-facing metadata for the skill picker and prompt chips.

## Design Principles

- Advisory swarms stay read-only and converge on one synthesized recommendation.
- The orchestrator separates planning from execution and enforces explicit file ownership.
- Apple UI guidance is SwiftUI-first and current to WWDC 2026; Android UI guidance is Compose-first and current to Google I/O 2026.
- Legacy UIKit/AppKit and Android View technologies are treated as migration or narrow interoperability concerns, not defaults for new UI.
- Motion discovery and review stay platform-native and do not prescribe browser styling or animation APIs.
- Skills are intentionally narrow so the main agent can compose them without mixing incompatible goals.
