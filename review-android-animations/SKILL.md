---
name: review-android-animations
description: Review native Android animation and gesture code against a strict bar for purpose, Material and platform fit, physical continuity, interruption, adaptive behavior, accessibility, and runtime performance. Use for Jetpack Compose or Android View diffs and explicit file scopes when asked to review, audit, or approve existing motion. Read-only by default; do not use to find missing animation opportunities or review unrelated code.
---

# Review Android Animations

Review motion and only the code directly required for its correctness. Treat platform behavior, accessibility, and runtime feel as release criteria.

Read [references/standards.md](references/standards.md) before issuing findings that depend on API selection, gesture behavior, adaptive layout, semantics, or performance.

## Scope

- Remain read-only unless the user separately requests fixes.
- Prefer the current diff; otherwise use the explicit files or components in scope.
- Include animation state, navigation, gestures, haptics, semantics, and adaptive behavior coupled to the motion.
- Ignore unrelated style or architecture unless it directly causes a motion issue.
- Use `find-android-animation-opportunities` for missing motion.

## Review Process

1. Read project instructions and identify Compose or View system, Android versions, design tokens, form factors, and navigation mode.
2. Map each changed animation to its trigger, state transition, item identity, frequency, and user purpose.
3. Inspect interruption, coroutine cancellation, rapid retargeting, gesture ownership, nested scroll, back, and predictive back.
4. Inspect Remove animations behavior, TalkBack semantics, focus, and alternate input.
5. Check recomposition, layout, draw work, allocations, and invalidation on every frame.
6. Exercise compact and expanded layouts or run focused tests when source does not prove behavior.
7. Report only actionable findings introduced or exposed by the reviewed scope.

## Non-Negotiable Standards

Flag a finding when motion:

1. Has no clear user-facing purpose.
2. Slows a frequent action, navigation, or back behavior.
3. Fights Material or Android component behavior without a user need.
4. Jumps, restarts, loses velocity, or ignores anchors during an interruptible gesture.
5. Delays input, cancellation, or state commitment until decorative motion finishes.
6. Uses unstable Lazy item identity, mismatched transition state, or competing animation owners.
7. Breaks predictive back, window resizing, fold transitions, insets, or pane continuity.
8. Leaves hidden content in semantics, moves TalkBack focus unexpectedly, or communicates essential state only through motion.
9. Has no valid animation-disabled outcome.
10. Performs avoidable recomposition, measure, layout, allocation, or rendering work every frame and risks jank.

Do not demand custom timings or easing when Material defaults, app tokens, and runtime behavior are already correct.

## Severity

- **Blocker:** broken navigation or gesture completion, inaccessible essential state, crash, or unrecoverable input state.
- **High:** visible jump, lost velocity, broken back behavior, hidden focusable content, repeated jank, or no usable animation-disabled state.
- **Medium:** unjustified motion, poor Android fit, excessive frequency, wrong API ownership, adaptive-layout risk, or avoidable performance cost.
- **Low:** localized polish issue with a concrete user-visible effect.

## Required Output

### Findings

List findings from highest severity to lowest:

| Severity | Location | Evidence | User impact | Native recommendation |
| --- | --- | --- | --- | --- |

Cite `file:line`, state the failure mode, and give the smallest correction direction. Do not write a patch unless requested.

If no findings remain, write `No animation findings.` and state what runtime behavior was not verified.

### Verdict

Choose exactly one:

- **Block** — at least one blocker or high-severity motion regression
- **Request changes** — actionable medium or low issues remain
- **Approve** — no actionable findings in scope

End with the reviewed scope, checks performed, and residual risk in one short paragraph.
