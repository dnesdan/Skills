---
name: review-apple-animations
description: Review SwiftUI motion, Liquid Glass, navigation transitions, Metal-backed shader effects, custom graphics, gestures, and haptics against the current WWDC 2026 and 2027-platform baseline. Use for Xcode 27-era diffs or explicit file scopes when asked to audit or approve Apple UI motion, graphics, interruption, adaptive behavior, accessibility, energy, or runtime performance. Treat new UIKit/AppKit animation and older SwiftUI patterns as modernization findings unless a documented interoperability gap requires them. Read-only by default.
---

# Review Apple Animations

Review current SwiftUI motion and graphics as release-critical behavior. Approval requires platform fit, correct lifecycle, accessibility, and measured performance.

Read [references/standards.md](references/standards.md) before issuing findings.

## Currency Gate

Use the WWDC26, Xcode 27, and 2027-platform baseline. Inspect the project SDK and verify beta API declarations in official Apple documentation. Do not approve an older pattern merely because it still compiles when a current direct replacement fits.

## Scope

- Remain read-only unless the user separately requests fixes.
- Prefer the current diff; otherwise use the explicit files or components.
- Include animation state, Liquid Glass, shaders, drawing, gestures, haptics, navigation, resizing, accessibility, energy, and performance coupled to the motion.
- Ignore unrelated code unless it directly causes the motion failure.
- Use `find-apple-animation-opportunities` for missing motion.

## Review Process

1. Identify Xcode, SDK, deployment targets, SwiftUI/UIKit boundaries, and availability strategy.
2. Map every changed effect to its trigger, conceptual identity, frequency, source, destination, and system alternative.
3. Check whether Liquid Glass is automatic, custom, grouped, interactive, and placed on the control layer.
4. Check modern SwiftUI state, animation scope, navigation transition, interruption, cancellation, rapid retargeting, and resizing.
5. For shaders, verify API choice, Metal function inputs, sample bounds, time source, lifecycle, fallback, and GPU cost.
6. Check Reduce Motion, Reduce Transparency, Increase Contrast, VoiceOver, Dynamic Type, and nonvisual feedback.
7. Build and exercise the smallest relevant release configuration when source cannot prove behavior.
8. Report only actionable findings caused or exposed by the reviewed scope.

## Non-Negotiable Standards

Raise a finding when the change:

1. Uses motion, glass, or a shader without a user-facing purpose.
2. Adds custom glass where a system control already supplies it or places glass in the content layer.
3. Applies raw glass behind a button instead of a glass button style.
4. Breaks conceptual identity, spatial origin, interactive dismissal, or framework navigation behavior.
5. Restarts, jumps, drops velocity, or disables input during an interruptible action.
6. Uses broad implicit animation, unstable identity, or multiple owners for one animated value.
7. Introduces legacy-first UIKit/AppKit, display-link, screen-bounds, or manual-blur behavior without a documented current-framework gap.
8. Runs a shader or timeline unnecessarily, rebuilds resources per frame, declares the wrong sample bound, or lacks an availability fallback.
9. Ignores resizing, inactive-window appearance, accessibility settings, lifecycle, energy, or older-system behavior.
10. Risks measurable frame drops, memory growth, thermal load, or input latency.

## Severity

- **Blocker:** trapped input, broken navigation or state, inaccessible essential information, crash, runaway work, or invalid availability.
- **High:** visible jump, lost gesture continuity, wrong glass usage across a primary surface, no reduced-motion outcome, severe GPU/frame risk, or new legacy-first architecture.
- **Medium:** unjustified effect, wrong API family, unstable identity, resizing defect, avoidable energy cost, or weak platform fit.
- **Low:** localized polish issue with concrete user impact.

## Required Output

### Findings

| Severity | Location | Current-platform evidence | User impact | SwiftUI-native recommendation |
| --- | --- | --- | --- | --- |

Cite `file:line`, name stable or beta status, and give the smallest correction direction. Do not write a patch unless asked.

If no findings remain, write `No animation findings.` and state which runtime, GPU, device, or beta behavior remains unverified.

### Verdict

Choose exactly one:

- **Block**
- **Request changes**
- **Approve**

Close with the reviewed scope, SDK baseline, checks performed, and residual risk.
