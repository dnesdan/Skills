# Native Android Animation Standards

Use this reference for precise Compose and View-system review. Reuse app motion tokens and Material defaults unless evidence justifies a custom spec.

## Contents

1. Purpose and frequency
2. API ownership
3. Gestures and navigation
4. Adaptive behavior
5. Accessibility and semantics
6. Performance
7. Validation
8. Escalation checks

## Purpose and Frequency

Accept motion that gives feedback, preserves spatial context, clarifies a state transition, or prevents an abrupt change. Reserve ornamental or celebratory motion for rare, product-appropriate moments.

Do not add custom spectacle to standard controls, routine navigation, back, frequent list work, or keyboard-driven actions.

## API Ownership

### Jetpack Compose

- Use `animate*AsState` for one state-derived value.
- Use `updateTransition` when multiple properties belong to one state transition.
- Use `AnimatedVisibility` when hidden content must leave composition and semantics.
- Use `AnimatedContent` only when content identity and direction are clear.
- Use `Animatable` for cancellation, retargeting, velocity, or gesture coordination.
- Use `anchoredDraggable`, scroll, swipe, and Material components before raw `pointerInput`.
- Add stable keys to animated lazy items.
- Avoid two animation APIs writing the same property.
- Ensure coroutines are scoped to the owning state and cancel cleanly.
- Give animation APIs meaningful labels for tooling.

### Android Views

- Use platform or Material transitions when they match the component.
- Use property animation for predetermined changes and spring or fling behavior for physical motion.
- Use `MotionLayout` for coordinated state transitions only when its ownership is clearer than imperative animators.
- Avoid multiple animators competing over one property.
- Cancel or retarget animations when a view detaches or state changes.

## Gestures and Navigation

- Keep pointer movement and content movement synchronized.
- Respect touch slop, direction locking, nested scroll, resistance, anchors, and velocity thresholds.
- Preserve velocity across drag release and retargeting.
- Keep gestures cancelable and provide an alternate action.
- Do not delay state commitment merely to finish decoration.
- Integrate custom navigation motion with system back and predictive back.
- Test both gesture and three-button navigation.

## Adaptive Behavior

- Keep motion valid while the window resizes or a fold posture changes.
- Animate pane continuity only when it helps orientation; do not drag phone-only geometry across expanded layouts.
- Respect edge-to-edge insets, display cutouts, system bars, and the IME throughout the transition.
- Avoid hardcoded distances derived from one device size.
- Preserve item and pane identity when presentation changes.

## Accessibility and Semantics

- Provide a coherent final state when system animations are removed or animator duration scale is zero.
- Ensure hidden content leaves semantics when it is no longer available.
- Keep TalkBack focus stable through visibility and content changes.
- Do not require a swipe or drag without an accessibility action or visible alternative.
- Keep essential state independent of motion, color, sound, and haptics.
- Test large font and display size so animated bounds do not clip content.

## Performance

- Prefer draw-phase work where equivalent behavior does not require recomposition or layout.
- Use modifier lambdas and `graphicsLayer` appropriately to defer reads and bound invalidation.
- Treat layout animation as legitimate when layout is the purpose, but profile it in large or nested hierarchies.
- Avoid per-frame allocation, state publication, image work, unbounded blur, and broad recomposition.
- Keep lazy-list item identity stable.
- Use Macrobenchmark, system tracing, Compose animation tooling, and frame timing when risk is material.
- Validate on a representative lower-performance device, not only a desktop emulator.

## Validation

- Exercise initial entry, exit, interruption, reversal, rapid repetition, cancellation, process or lifecycle changes, and navigation back.
- Test compact and expanded widths, orientation, fold or resize, edge-to-edge, and IME appearance.
- Test Remove animations, TalkBack, Switch Access, keyboard, mouse, large fonts, dark theme, and dynamic color.
- Inspect slow motion or frame by frame for origin, coordinated properties, dropped frames, and gesture handoff.

## Escalation Checks

Raise a finding when any answer is yes:

- Can back or predictive back disagree with the visual state?
- Can cancellation leave the model and screen in different states?
- Can a coroutine or animator outlive its owner?
- Can rapid targets make motion restart or jump?
- Can invisible content remain focusable?
- Can a lazy item animate with the wrong identity?
- Can window resizing or insets invalidate the path?
- Does the animation perform expensive composition, layout, or drawing each frame?
- Is custom motion replacing correct Material behavior without a user benefit?
