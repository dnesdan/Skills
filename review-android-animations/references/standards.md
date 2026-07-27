# Google I/O 2026 Android Motion and Graphics Standards

Use this reference for Compose-first review on the Android 17 adaptive baseline.

## Contents

1. Source and dependency baseline
2. Material 3 Expressive
3. Compose motion ownership
4. Navigation 3 and shared transitions
5. Adaptive behavior and input
6. Compose graphics and AGSL
7. Accessibility and lifecycle
8. Performance and modernization

## Source and Dependency Baseline

Verify volatile claims against:

- [Compose First](https://android-developers.googleblog.com/2026/05/android-ui-development-is-compose-first.html)
- [Adaptive development — Google I/O 2026](https://android-developers.googleblog.com/2026/05/android-adaptive-development-ecosystem.html)
- [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3)
- [Navigation 3](https://developer.android.com/guide/navigation/navigation-3)
- [Shared element transitions](https://developer.android.com/develop/ui/compose/animation/shared-elements)
- [Compose graphics](https://developer.android.com/develop/ui/compose/graphics/draw/overview)

Read the Compose BOM and library versions from the project. Compose 1.11 is the April 2026 stable baseline, but Material expressive motion and Styles APIs remain version-dependent. Isolate experimental opt-ins and never infer availability from memory.

## Material 3 Expressive

- Start with Material 3 components and theme roles.
- Keep recurring utilitarian interaction on standard motion.
- Reserve expressive motion for prominent elements and hero interactions.
- Use component defaults before custom specs.
- Read motion from `MaterialTheme.motionScheme` when the selected Material version exposes it.
- Reject deprecated `LocalMotionScheme`.
- Verify the current `ExperimentalMaterial3ExpressiveApi` requirement.
- Use spatial specs for bounds or shape and effects specs for color or alpha.
- Keep dynamic color, expressive shapes, and variable typography legible and semantic.
- Avoid assigning expressive behavior to an entire app without a frequency and product-character review.

## Compose Motion Ownership

- Use `animate*AsState` for one state-derived value.
- Use `updateTransition` for coordinated values owned by one state machine.
- Use `AnimatedVisibility` when hidden content must leave composition and semantics.
- Use `AnimatedContent` for a meaningful content identity change.
- Use `Animatable` for cancellation, retargeting, velocity, and gesture coordination.
- Use `anchoredDraggable` and high-level gestures before raw pointer handling.
- Keep one owner per animated property.
- Keep stable keys for lazy content, reordering, and shared transitions.
- Use theme or component specs instead of scattered hardcoded timing.
- Ensure coroutine work cancels when its owner leaves composition.

## Navigation 3 and Shared Transitions

- Prefer Navigation 3 for new compatible Compose architecture.
- Keep back-stack entries uniquely keyed and state-restorable.
- Synchronize predictive back with visual progress.
- Use `SharedTransitionLayout` at a hierarchy level containing both endpoints.
- Use `sharedElement` only for the same conceptual content.
- Use `sharedBounds` for a container whose internal content changes.
- Use typed unique keys and consistent modifier ordering.
- Account for overlay, clipping, and z-order.
- Choose `ScaleToBounds` for text where reflow would distract; remeasure only when geometry requires it.
- Respect current interoperability limitations.
- Remove caller-managed invisible shared elements after transition completion so they do not remain active or focusable.

## Adaptive Behavior and Input

- Use `NavigationSuiteScaffold`, `ListDetailPaneScaffold`, and `SupportingPaneScaffold` when their canonical behavior fits.
- Preserve selected item, navigation state, focus, and scroll position as pane count changes.
- Handle Large and Extra-large classes when supported by the selected adaptive library.
- Keep animation endpoints valid during live resize, fold posture changes, external displays, and density or font changes.
- Respect edge-to-edge, system bars, display cutouts, and IME insets throughout motion.
- Support keyboard, mouse, trackpad, stylus, focus rings, and accessibility input.
- Treat MediaQuery, Grid, FlexBox, and Styles as experimental until the project's dependencies say otherwise.

## Compose Graphics and AGSL

- Use `Canvas`, `DrawScope`, `drawBehind`, and `drawWithContent` for custom drawing.
- Use `drawWithCache` only when caching actual objects.
- Keep brushes, paths, shaders, textures, and immutable inputs stable.
- Use `ShaderBrush(RuntimeShader)` with AGSL only on Android 13 and later.
- Use `RenderEffect` only on Android 12 and later.
- Provide a lower-API Compose fallback.
- Update uniforms instead of reconstructing the shader every frame.
- Bound sampling, overdraw, blur, shadows, and offscreen compositing.
- Remember that alpha, RenderEffect, and some compositing modes create offscreen layers.
- Stop or simplify continuous graphics when offscreen, animation-disabled, or power-sensitive.
- Keep information-dense content and controls legible.

## Accessibility and Lifecycle

- Keep the final state correct when Remove animations or animator duration scale disables motion.
- Ensure invisible content leaves semantics.
- Preserve TalkBack focus through content swaps, navigation, pane changes, and shared transitions.
- Provide accessibility actions and visible alternatives for gestures.
- Test large text, display scaling, high contrast, Switch Access, keyboard, and trackpad.
- Never rely only on motion, color, shape, shader output, sound, or haptics.
- Cancel animation and graphics work when composition or lifecycle ownership ends.

## Performance and Modernization

- Avoid per-frame allocation, broad recomposition, repeated measure/layout, and unnecessary offscreen buffers.
- Prefer draw- or layout-phase APIs when they safely avoid composition work.
- Measure release builds with Perfetto, Macrobenchmark, JankStats, and devices covering low and high refresh rates.
- Test rapid retargeting, cancellation, predictive back, resize, fold, background, foreground, and process recreation.
- Raise modernization findings for newly touched XML/View UI, new `RecyclerView`, Navigation 2 in a new architecture, fixed device checks, orientation locks, or manual transitions replaced by current Compose APIs.
- Do not require a risky big-bang migration; define the smallest Compose boundary that prevents new legacy code.
