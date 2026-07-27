---
name: android-design
description: Design, implement, or review native Android interfaces using Material guidance, adaptive layouts, accessibility, platform conventions, touch and input behavior, and purposeful motion. Use for Jetpack Compose or Android View work involving navigation, components, typography, edge-to-edge, window size classes, foldables, gestures, transitions, springs, haptics, animation performance, or an Android-native design critique. Do not use for web interfaces.
---

# Android Design

Create Android interfaces that feel at home across phones, tablets, foldables, desktop windows, and varied OEM hardware. Favor platform semantics, adaptability, and useful feedback over ornamental motion.

## Source Order

Use this order when guidance conflicts:

1. Current Android Developers and Material guidance
2. Existing app behavior, design-system tokens, and project instructions
3. Standard Material and Compose or View components
4. Custom behavior justified by a concrete user need

This skill adapts the restraint and physical-motion ideas in Emil Kowalski's design skills to native Android APIs and platform conventions.

## Design Principles

- **Purpose:** Make the main task and primary action obvious.
- **User control:** Keep actions reversible and avoid unnecessary confirmation.
- **Platform familiarity:** Preserve Android navigation, back behavior, system surfaces, and component semantics.
- **Adaptability:** Design for changing window size, posture, orientation, input, density, language, and font scale.
- **Clarity:** Use hierarchy, containment, alignment, and plain labels to reduce cognitive load.
- **Accessibility:** Treat semantics, target size, contrast, and alternate input as core design.
- **Restraint:** Add motion only when it improves understanding or feedback.

## Platform Fit

- Identify the actual target set: compact phone, tablet, foldable, desktop windowing, TV, Wear OS, or multiple classes.
- Design with window size classes and panes. Reflow, reveal, or change presentation instead of stretching a phone layout.
- Support edge-to-edge correctly with system bar, display cutout, and IME insets.
- Keep important actions reachable without assuming one device size or grip.
- Preserve Android system back and predictive back behavior.
- Prefer Material components and navigation patterns before inventing custom controls.
- Use scalable text units, test nonlinear font scaling, and avoid fixed containers that clip enlarged text.
- Keep touch targets at least 48 dp and provide focus, keyboard, mouse, stylus, and accessibility semantics where relevant.

## Interaction

- Prefer the highest-level component or modifier that fits. `Button`, `clickable`, `toggleable`, scrolling containers, and Material swipe components include behavior and semantics that raw pointer handling does not.
- Give immediate press feedback through the component's indication and interaction state.
- Keep dragged content synchronized with the pointer and preserve nested-scroll contracts.
- Use touch slop, velocity, resistance, and anchors rather than brittle distance-only gesture rules.
- Provide a visible or semantic alternative for swipe-only and drag-only actions.
- Keep haptics causal and sparse. Trigger them at the committed state change, not as decoration.

## Motion

Use motion for feedback, spatial continuity, state explanation, or to bridge a change that would otherwise feel abrupt.

- Keep frequently repeated flows fast and subtle.
- Prefer system and Material motion already provided by components.
- Use springs for physical or interruptible changes and duration-based specs for deliberate, predetermined choreography.
- Preserve current value and velocity when a target changes.
- Keep enter and exit paths spatially coherent.
- Do not delay navigation, back, or input until a decorative transition finishes.
- Treat no animation as a valid and often preferable result.

### Jetpack Compose

- Drive animations from explicit state and use the narrowest API that fits.
- Use `animate*AsState` for one value, `updateTransition` for coordinated values, `AnimatedVisibility` for lifecycle-correct appearance, and `AnimatedContent` for meaningful content swaps.
- Use `Animatable` when motion needs cancellation, retargeting, velocity, or gesture coordination.
- Use `anchoredDraggable`, scroll, or other high-level gesture APIs before raw `pointerInput`.
- Prefer modifier lambda and `graphicsLayer` paths when they avoid recomposition or relayout during every frame.
- Use `animateContentSize` only when the layout change is itself the intended motion and performance has been checked.
- Add labels to animation APIs so tooling and traces remain understandable.

### Android Views

- Prefer platform and Material transitions or `MotionLayout` when they match the interaction.
- Use `ViewPropertyAnimator`, `ValueAnimator`, `ObjectAnimator`, or spring and fling animations according to whether the motion is predetermined or physical.
- Make interactive transitions cancelable and continue from their visible state.
- Avoid repeatedly forcing measure and layout during gesture-driven animation.

## Visual System

- Use Material color roles, type scale, shapes, elevation, and state layers consistently.
- Treat dynamic color as an input to the system, not a reason to discard brand hierarchy.
- Use containment to group related content and actions.
- Keep content width bounded on large windows. Change panes and component presentation rather than scaling everything up.
- Maintain contrast across light, dark, dynamic, high-contrast, and disabled states.
- Use icons with clear semantics and content descriptions only when they convey meaning not already expressed by nearby text.

## Accessibility

- Keep every essential state understandable with animation disabled.
- Test the system's Remove animations setting and animator duration scale at zero.
- Preserve TalkBack focus and semantics during animated visibility and content replacement.
- Avoid leaving invisible content in the semantics tree; choose lifecycle-aware visibility when content should disappear.
- Do not communicate only through motion, color, sound, or haptics.
- Test TalkBack, Switch Access, keyboard navigation, large font scale, display size, and high contrast where relevant.

## Workflow

1. Identify framework, target form factors, Android versions, navigation model, and primary user task.
2. Read project instructions and inspect theme, component system, insets, adaptive layout, existing motion, and accessibility.
3. Describe the current hierarchy and interaction before proposing changes.
4. Choose a standard component or platform behavior when it already solves the problem.
5. For custom motion, state purpose, frequency, trigger, path, interruption behavior, disabled-animation behavior, and performance risk.
6. Implement only when asked; otherwise return a critique or implementation-ready recommendation.
7. Validate with Compose Preview or layout inspection, emulator coverage, and representative real hardware.
8. Test compact and expanded widths, fold or resize transitions, gesture and three-button navigation, font scale, TalkBack, dark theme, and animation-disabled mode.

## Output

Lead with the strongest design decision or highest-impact issue. Cite concrete composables, views, and `file:line` evidence when reviewing code. Separate Android convention issues, adaptive-layout risks, accessibility, motion quality, and optional polish. Prefer deleting weak custom behavior over adding more motion.
