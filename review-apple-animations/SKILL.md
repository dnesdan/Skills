---
name: review-apple-animations
description: Review native Apple-platform animation and gesture code against a strict bar for purpose, platform fit, physical continuity, interruptibility, accessibility, and runtime performance. Use for SwiftUI, UIKit, AppKit, watchOS, tvOS, or visionOS diffs and explicit file scopes when asked to review, audit, or approve existing motion. Read-only by default; do not use to find missing animation opportunities or review unrelated code.
---

# Review Apple Animations

Review only motion and the code directly required to make that motion correct. Approval is earned through evidence.

Read [references/standards.md](references/standards.md) before issuing findings that depend on API choice, physical behavior, accessibility, or validation.

## Scope

- Remain read-only unless the user separately asks for fixes.
- Prefer the current diff. If no diff exists, use the explicit files or components named by the user.
- Include gestures, transitions, haptics, animation state, and accessibility behavior coupled to the motion.
- Ignore unrelated style and architecture unless they directly cause a motion defect.
- Use `find-apple-animation-opportunities` for places that currently have no motion.

## Review Process

1. Read project instructions and identify platform, framework, deployment target, design tokens, and expected device classes.
2. Map every changed animation to its trigger, source state, target state, conceptual object, and expected frequency.
3. Inspect gesture ownership, interruption, cancellation, rapid retargeting, and navigation or dismissal behavior.
4. Inspect Reduce Motion and other accessibility adaptations.
5. Check per-frame work, invalidation scope, identity, and state lifetime.
6. Run the smallest useful build, preview, simulator, or UI exercise when code does not prove behavior.
7. Report only actionable findings caused by the reviewed change.

## Non-Negotiable Standards

Flag a finding when motion:

1. Has no user-facing purpose.
2. Adds delay or spectacle to a frequent or system-standard action.
3. breaks the spatial relationship between source and destination.
4. Restarts, jumps, or drops velocity during an interruptible interaction.
5. Locks input or prevents reversal solely while animation runs.
6. Uses unstable identity or implicit animation scope that animates unrelated state.
7. Conflicts with platform navigation, interactive dismissal, focus, or gesture conventions.
8. Communicates essential state only through motion, haptics, sound, or color.
9. Ignores Reduce Motion for large movement, parallax, repeated oscillation, or decorative spring behavior.
10. Performs avoidable layout, allocation, rendering, or state work every frame and risks visible jank.

Do not flag a difference from a personal timing preference when platform defaults, project tokens, and runtime behavior are sound.

## Severity

- **Blocker:** motion can trap input, break navigation or gesture completion, make essential state inaccessible, or cause a severe runtime failure.
- **High:** visible jump, wrong destination, lost velocity, unstable identity, repeated jank, or missing reduced-motion handling for substantial movement.
- **Medium:** unjustified motion, weak platform fit, excessive frequency, misleading origin, or avoidable performance risk.
- **Low:** localized polish issue with a clear user-visible effect.

## Required Output

### Findings

List findings in severity order. Use one row per issue:

| Severity | Location | Evidence | User impact | Native recommendation |
| --- | --- | --- | --- | --- |

Cite `file:line`. Explain the failure mode and the smallest direction for correction. Do not produce a patch unless asked.

If there are no findings, write `No animation findings.` and name any runtime behavior that remains unverified.

### Verdict

Choose exactly one:

- **Block** — at least one blocker or high-severity motion regression
- **Request changes** — actionable medium or low issues remain
- **Approve** — no actionable findings in the reviewed scope

Close with scope, tests performed, and residual risk in one short paragraph.
