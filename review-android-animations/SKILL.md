---
name: review-android-animations
description: Review Compose motion, Material 3 Expressive behavior, Navigation 3 and shared transitions, adaptive pane continuity, state-based Styles, AGSL RuntimeShader graphics, gestures, and haptics against the current Google I/O 2026 baseline. Use for Android 17-era diffs or explicit file scopes when asked to audit or approve motion, graphics, predictive back, accessibility, lifecycle, or runtime performance. Treat new XML/View animation and older navigation patterns as modernization findings unless a documented migration constraint requires them. Read-only by default.
---

# Review Android Animations

Review current Compose motion and graphics as product behavior, not decoration. Approval requires dependency-aware API use, adaptive correctness, accessibility, and measured release performance.

Read [references/standards.md](references/standards.md) before issuing findings.

## Currency Gate

Use the Google I/O 2026 baseline. Inspect the Compose BOM, Material version, Android target and minimum, Navigation version, and experimental opt-ins. Never present an alpha API as stable or approve a deprecated access path because it still compiles.

## Scope

- Remain read-only unless fixes are separately requested.
- Prefer the current diff; otherwise use the explicit files or components.
- Include Compose state, Material motion, Navigation 3, shared transitions, adaptive scaffolds, gestures, graphics, shaders, semantics, lifecycle, and performance coupled to motion.
- Ignore unrelated code unless it directly causes the issue.
- Use `find-android-animation-opportunities` for missing motion.

## Review Process

1. Record dependency versions, API stability, min SDK, architecture, and form factors.
2. Map each effect to trigger, conceptual identity, frequency, source, destination, and Material or system alternative.
3. Check `MaterialTheme.motionScheme`, expressive versus standard character, component defaults, and experimental opt-ins.
4. Check Navigation 3, shared keys, modifier order, overlays, predictive back, adaptive pane changes, interruption, and cancellation.
5. For graphics, verify drawing API, AGSL or RenderEffect availability, caching, uniforms, fallback, overdraw, and offscreen layers.
6. Check Remove animations, TalkBack focus and semantics, alternate input, and configuration continuity.
7. Run the smallest relevant release build, Macrobenchmark, Perfetto trace, or device exercise when source cannot prove behavior.
8. Report only actionable findings caused or exposed by the reviewed scope.

## Non-Negotiable Standards

Raise a finding when the change:

1. Uses motion, expressive styling, or a shader without a user-facing purpose.
2. Applies expressive motion to recurring utilitarian interactions instead of standard Material behavior.
3. Uses a deprecated motion access path, scatters hardcoded specs, or mislabels an experimental API as stable.
4. Breaks Navigation 3 state, predictive back, shared identity, modifier order, overlay, or semantics.
5. Restarts, jumps, loses velocity, ignores anchors, or delays input during an interruptible gesture.
6. Breaks pane continuity, resizing, insets, fold posture, focus, or non-touch input.
7. Introduces new XML/View animation, Navigation 2, or phone-only assumptions without a documented migration constraint.
8. Recreates shaders, brushes, paths, or effects per frame; uses an unavailable API without fallback; or creates unbounded offscreen work.
9. Leaves invisible content focusable or has no usable animation-disabled outcome.
10. Risks measurable jank, memory growth, thermal load, or input latency.

## Severity

- **Blocker:** broken navigation or state, inaccessible essential information, crash, invalid API availability, trapped input, or runaway work.
- **High:** visible jump, broken predictive back, hidden focusable content, no animation-disabled outcome, severe frame/GPU risk, or new legacy-first architecture.
- **Medium:** unjustified expressiveness, wrong API family, adaptive defect, unstable identity, avoidable energy cost, or weak Material fit.
- **Low:** localized polish issue with concrete user impact.

## Required Output

### Findings

| Severity | Location | Current-platform evidence | User impact | Compose-native recommendation |
| --- | --- | --- | --- | --- |

Cite `file:line`, dependency and API stability, and the smallest correction direction. Do not write a patch unless asked.

If there are no findings, write `No animation findings.` and state unverified devices, refresh rates, GPU effects, or experimental behavior.

### Verdict

Choose exactly one:

- **Block**
- **Request changes**
- **Approve**

Close with scope, dependency baseline, checks performed, and residual risk.
