# Native Apple Animation Standards

Use this reference to make review findings precise. Prefer current project tokens and platform defaults over arbitrary constants.

## Contents

1. Purpose and frequency
2. Spatial and physical behavior
3. SwiftUI
4. UIKit and AppKit
5. Accessibility
6. Performance
7. Validation
8. Escalation checks

## Purpose and Frequency

Accept motion that provides feedback, preserves context, explains a state change, or prevents a disorienting jump. Permit extra delight only for rare moments where it matches the product.

Routine navigation, keyboard actions, repeated row selection, and standard controls usually need no custom motion. System motion is already part of the interaction.

## Spatial and Physical Behavior

- Keep touch and content synchronized during direct manipulation.
- Preserve the point where the object was grabbed.
- Use velocity and projected intent when choosing a landing target.
- Continue from the visible value when retargeting.
- Keep interactive motion cancelable and reversible.
- Use resistance past a boundary rather than an unexplained hard stop.
- Keep source and destination connected when they represent one conceptual object.
- Use coherent entry and exit paths.
- Align visual, haptic, and audio feedback with the committed event.

## SwiftUI

- Keep one clear source of truth for the state transition.
- Scope `.animation(_:value:)` to the value intended to animate.
- Watch for broad implicit animation that moves unrelated descendants.
- Use `withAnimation` for bounded state mutations.
- Use a spring for retargetable or gesture-driven movement.
- Use `Animatable` conformance only when interpolation genuinely requires a custom value.
- Verify asymmetric transitions during both insertion and removal.
- Use stable identity for lists and `matchedGeometryEffect`.
- Do not use matched geometry between views that are not conceptually the same object.
- Use `Transaction` to suppress inherited motion when state must update immediately.
- Cancel tasks and timelines when the owning view disappears.
- Verify `PhaseAnimator` and `KeyframeAnimator` sequences do not block input or replay unexpectedly.

## UIKit and AppKit

- Prefer interruptible property animators for custom interactive movement.
- Keep gesture progress and transition progress synchronized.
- Use current presentation state when replacing an in-flight animation.
- Pass meaningful velocity into spring or completion behavior.
- Verify custom transition controllers handle cancellation and completion symmetrically.
- Coordinate collection updates with stable data identity.
- Avoid nested animators fighting over the same property.

## Accessibility

- Provide a Reduce Motion branch for large translations, zoom, parallax, repeated oscillation, and decorative springs.
- Preserve essential feedback through a static state change, restrained dissolve, text, symbol, or control state.
- Honor Reduce Transparency and Increase Contrast when materials animate.
- Keep VoiceOver focus and reading order stable across transitions.
- Provide alternatives to gesture-only actions.
- Verify Dynamic Type does not change animation geometry into clipping or overlap.

## Performance

- Avoid expensive layout measurement, geometry discovery, allocation, image decoding, and state publication every frame.
- Keep drawing and visual effects bounded to the smallest useful area.
- Avoid stacking blur, shadow, masking, and translucency over large moving surfaces without profiling.
- Ensure animation state changes occur on the correct actor.
- Look for view identity churn that recreates animation state.
- Measure on representative hardware when custom drawing, materials, large lists, or gesture tracking are involved.

## Validation

- Test the initial run, interruption, reversal, rapid repeated trigger, cancellation, background and foreground, and view removal.
- Test Reduce Motion, VoiceOver, light and dark appearance, large accessibility text, rotation, resizing, and relevant input devices.
- Inspect slow motion or frame by frame when origin, velocity handoff, or coordinated properties are uncertain.
- Use previews for iteration, but validate gestures, haptics, performance, and system transitions on a simulator or device.

## Escalation Checks

Raise a finding when any answer is yes:

- Can input become disabled or trapped while motion runs?
- Can a state change restart from the wrong value?
- Can rapid interaction create a jump or stale completion?
- Can two animation owners write the same property?
- Does conceptual identity change during a matched transition?
- Does Reduce Motion still contain substantial decorative movement?
- Can hidden content retain accessibility focus?
- Does the animation require heavy per-frame work on a common device?
- Does it replace a familiar system transition without measurable benefit?
