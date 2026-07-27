# Skills

A focused collection of reusable Codex skills for product planning, delivery orchestration, private store reporting, current WWDC 2026 Apple and Google I/O 2026 Android opportunity audits, simulator-backed redesign assessment, native design, and animation review.

## Included Skills

| Skill | Folder | Type | Description |
| --- | --- | --- | --- |
| Feature Planning Swarm | `feature-planning-swarm` | Advisory swarm | Turns a feature idea into multiple concrete implementation plans with one recommended path. |
| Feature Extension Swarm | `feature-extension-swarm` | Advisory swarm | Scans the current repo and app surface to propose the most valuable next feature extensions for competitiveness. |
| Implementation Orchestrator | `implementation-orchestrator` | Execution orchestrator | Converts an approved plan into dependency-aware work packets, parallel execution waves, and validation gates. |
| Cross-Store Ratings Report | `cross-store-ratings-report` | Read-only store intelligence | Produces source-transparent portfolio ratings/review reports with correct windows, coverage, app mapping, themes, and comparable deltas from `asc` and Google Play developer tooling. |
| WWDC26 App Opportunity Audit | `wwdc26-app-opportunity-audit` | Read-only platform opportunity audit | Audits an Apple app against current iOS 27-era APIs and ranks repo-grounded Apple Intelligence, Siri, system-surface, device, and native-platform opportunities. |
| Google I/O 26 App Opportunity Audit | `google-io26-app-opportunity-audit` | Read-only platform opportunity audit | Audits an Android app against Android 17 and I/O 2026 APIs and ranks repo-grounded Gemini, AppFunctions, adaptive-surface, device, and native-platform opportunities. |
| iOS Redesign Audit | `audit-ios-app-redesign` | Simulator-backed redesign audit | Inspects every reachable screen, state, transition, and interaction for AI slop and native craft problems, then returns an evidence-backed redesign brief without changing code. |
| Imagegen UI Prototypes | `prototype-ui-with-imagegen` | Native visual divergence and promotion | Uses Codex's built-in image generation to compare System-native, Hybrid-native, and Custom-native Apple or Android UI directions, then optionally rebuilds an explicitly selected direction in SwiftUI or Compose and validates it at runtime. |
| Apple Design | `apple-design` | Current native design guidance | Applies the WWDC 2026 baseline with Xcode 27, current SwiftUI, Liquid Glass, adaptive layout, Metal shaders, and accessibility. |
| Android Design | `android-design` | Current native design guidance | Applies the Google I/O 2026 Compose-first baseline with Android 17 adaptive UI, Material 3 Expressive, Navigation 3, AGSL, and accessibility. |
| Find Apple Animation Opportunities | `find-apple-animation-opportunities` | Read-only motion discovery | Finds restrained SwiftUI, Liquid Glass, transition, and shader opportunities using the WWDC 2026 baseline. |
| Find Android Animation Opportunities | `find-android-animation-opportunities` | Read-only motion discovery | Finds restrained Compose, Material, adaptive, shared-transition, and shader opportunities using the I/O 2026 baseline. |
| Review Apple Animations | `review-apple-animations` | Read-only motion review | Reviews SwiftUI motion, Liquid Glass, Metal shaders, accessibility, energy, and performance against WWDC 2026. |
| Review Android Animations | `review-android-animations` | Read-only motion review | Reviews Compose motion, Material 3 Expressive, Navigation 3, AGSL, accessibility, and performance against I/O 2026. |

## Suggested Flow

1. Use `feature-planning-swarm` when a feature idea needs shaping before coding.
2. Use `feature-extension-swarm` when you want the repo analyzed for product gaps and the strongest next features to add.
3. Use `implementation-orchestrator` after a plan has been chosen and the work should actually be executed.
4. Use `cross-store-ratings-report` when ratings/reviews need to be pulled from App Store Connect and Google Play developer tooling across the portfolio.
5. Use `wwdc26-app-opportunity-audit` or `google-io26-app-opportunity-audit` when an existing app needs current, evidence-backed AI and platform opportunities ranked for adoption.
6. Use `audit-ios-app-redesign` when an existing iOS app needs a full Simulator-backed visual and interaction audit before any redesign code is written.
7. Use `prototype-ui-with-imagegen` when one native surface needs divergent visual concepts before code; select `keep <variant>` only when a direction should be rebuilt and runtime-validated.
8. Use `apple-design` or `android-design` when designing, implementing, or critiquing a native interface.
9. Use the platform-specific `find-*-animation-opportunities` skill to find missing motion without changing code.
10. Use the platform-specific `review-*-animations` skill to review motion that already exists.

## Install

Place these skill folders under `$CODEX_HOME/skills` or `~/.codex/skills` so Codex can discover them automatically.

## Structure

Each skill is self-contained:

- `SKILL.md` defines when to use the skill and how the workflow should run.
- `agents/openai.yaml` provides UI-facing metadata for the skill picker and prompt chips.
- `references/` contains supporting standards or dated research maps; a dated catalog is never a substitute for live freshness checks.

## Design Principles

- Advisory swarms stay read-only and converge on one synthesized recommendation.
- The orchestrator separates planning from execution and enforces explicit file ownership.
- Apple UI guidance is SwiftUI-first and current to WWDC 2026; Android UI guidance is Compose-first and current to Google I/O 2026.
- Cross-store reporting keeps developer reviews, public Apple storefront aggregates, Google statistics reports, partial coverage, and unavailable metrics explicitly separate.
- Redesign audits verify runtime behavior screen by screen, distinguish evidence from taste, and stop at a design brief and implementation handoff.
- Image-generated UI concepts stay outside production during exploration, span system, hybrid, and custom-native strategies, are judged against native behavior and accessibility constraints, and become real UI only through a selected SwiftUI or Compose rebuild.
- Platform opportunity audits require current first-party sources, repository evidence, explicit availability and maturity labels, privacy and cost analysis, and graceful fallbacks.
- Consumer AI subscriptions, developer APIs, system-only features, public frameworks, previews, MCP, and cloud trust boundaries are never treated as interchangeable.
- Legacy UIKit/AppKit and Android View technologies are treated as migration or narrow interoperability concerns, not defaults for new UI.
- Motion discovery and review stay platform-native and do not prescribe browser styling or animation APIs.
- Skills are intentionally narrow so the main agent can compose them without mixing incompatible goals.
