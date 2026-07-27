---
name: apple-design
description: Design, implement, modernize, or review native Apple interfaces against the current WWDC 2026 and 2027-platform baseline. Use for SwiftUI-first work involving Liquid Glass, modern navigation and toolbars, resizable layouts, Observation, gestures, spring and navigation transitions, Metal-backed SwiftUI shaders, custom graphics, SF Symbols, haptics, accessibility, or Apple-platform design critique. Prefer Xcode 27 and current SwiftUI APIs for new code; treat UIKit, AppKit, storyboards, and older patterns as migration or interoperability concerns rather than the default. Do not use for web interfaces.
---

# Apple Design

Build current Apple-platform interfaces with SwiftUI first. Use the system's design and behavior before creating a custom imitation.

## Currency Gate

Treat July 2026 as the knowledge baseline:

- WWDC26 and Xcode 27
- the 2027 Apple platform releases
- refreshed Liquid Glass
- the June 2026 Human Interface Guidelines and SwiftUI updates

Before using a beta or availability-gated API, verify its current declaration in Apple Developer documentation and the SDK installed in the project. Beta signatures can change. If a project supports older systems, keep the modern architecture and add the narrowest availability fallback; do not make the fallback the primary design.

Use only official Apple sources for volatile platform guidance:

- [Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles)
- [Materials](https://developer.apple.com/design/human-interface-guidelines/materials)
- [Motion](https://developer.apple.com/design/human-interface-guidelines/motion)
- [SwiftUI updates](https://developer.apple.com/documentation/updates/swiftui)
- [What's new in SwiftUI — WWDC26](https://developer.apple.com/videos/play/wwdc2026/269/)
- [Compose advanced graphics effects with SwiftUI — WWDC26](https://developer.apple.com/videos/play/wwdc2026/322/)

## Current Baseline

- Build new interface work in SwiftUI.
- Use Observation (`@Observable`, `@State`, `@Environment`, `@Bindable`) for new models and data flow.
- Use `NavigationStack` and `NavigationSplitView`.
- Design for arbitrary window sizes. Use size classes, adaptive containers, and content-driven layout rather than device checks or screen bounds.
- Exercise layouts with Xcode 27 resizable previews and on every supported platform.
- Use semantic system controls, toolbars, tabs, presentations, symbols, text styles, and gestures before custom replacements.
- Keep UIKit or AppKit only for a framework capability SwiftUI does not expose, a deliberate interoperability boundary, or incremental modernization.

## Design Principles

Apply Apple's current principles:

- **Purpose:** Make something meaningful and focus the experience on what matters.
- **Agency:** Keep people in control and make actions reversible.
- **Responsibility:** Protect privacy, safety, attention, and trust.
- **Familiarity:** Use conventions people already understand.
- **Flexibility:** Support different people, contexts, inputs, platforms, and window sizes.
- **Simplicity:** Include what is necessary; simplicity is not visual emptiness.
- **Craft:** Make every visual, interaction, motion, sound, and word intentional.
- **Delight:** Let delight emerge from the other principles instead of attaching spectacle.

## Liquid Glass

Treat Liquid Glass as a functional control layer over content.

- Let standard SwiftUI navigation, toolbar, tab, search, menu, and control surfaces adopt Liquid Glass automatically.
- Do not add glass to the content layer merely for decoration. Content cards and static content usually remain flat.
- Use custom glass sparingly for important floating controls that need separation from content.
- Use `.buttonStyle(.glass)` or `.buttonStyle(.glassProminent)` for buttons. Do not place a raw `glassEffect` behind a button.
- Use `buttonBorderShape(_:)` to shape glass buttons.
- Apply `.glassEffect(...)` after layout and appearance modifiers.
- Use `.interactive()` only for a surface that actually responds to direct interaction.
- Use `.regular` by default. Use `.clear` only over visually rich content where legibility remains strong.
- Group related effects in `GlassEffectContainer`; use `glassEffectID` and a namespace only for a real hierarchy-changing morph.
- Keep toolbar glass supplied by the system. Use `sharedBackgroundVisibility(_:)` or `contentMarginsRemoved(_:)` only when the item semantics justify separating it from the shared group.
- Honor the system Liquid Glass tint preference, inactive-window appearance, Reduce Transparency, and Increase Contrast.
- Rebuild with Xcode 27 before customizing: the refreshed 2027 appearance is adopted automatically.

## Resizable Structure and Toolbars

- Assume iPhone, iPad, and Mac windows can resize continuously.
- Use horizontal and vertical size classes and adaptive containers instead of idiom branches.
- Keep primary actions visible as space shrinks with `visibilityPriority(_:)`.
- Move secondary actions into `ToolbarOverflowMenu`.
- Use `topBarPinnedTrailing` only for an action that must remain anchored.
- Use `toolbarMinimizeBehavior(_:for:)` when more content space during scrolling improves the task.
- Use the prominent tab role only for a genuinely distinct, important destination or action.
- Preserve state and focus while a one-pane presentation becomes multi-pane.
- Avoid fixed frames, fixed orientation assumptions, and custom toolbar backgrounds.

## Motion and Interaction

Add motion only for feedback, spatial continuity, state explanation, or a transition that would otherwise disorient.

- Keep direct manipulation attached to the gesture and preserve velocity at release.
- Let gesture-driven motion interrupt, reverse, and retarget from the visible state.
- Prefer modern SwiftUI animation presets such as `.smooth`, `.snappy`, `.bouncy`, and `spring(duration:bounce:)`; choose by behavior, not novelty.
- Use `withAnimation` for a bounded mutation and `.animation(_:value:)` for an explicit dependency.
- Use `PhaseAnimator` or `KeyframeAnimator` only for noninteractive choreography.
- Use `matchedGeometryEffect` for shared identity within a hierarchy.
- Use system navigation transitions and `matchedTransitionSource` where available; do not implement a custom `NavigationTransition` conformance when the SDK exposes only framework-provided transitions.
- Use `Transaction` to prevent inherited animation from moving unrelated state.
- Never block input solely to finish an animation.
- Pair visual, haptic, and audio feedback at the committed event.

## SwiftUI Graphics, Metal, and Shaders

Use custom graphics when they serve content or interaction and system effects cannot express the result.

- Decompose the design into a pipeline of data, layout, drawing, shader, and time stages.
- Use SwiftUI drawing and layout first: `Canvas`, `Shape`, `visualEffect`, alignment guides, and drawing modifiers.
- Use `ShaderLibrary` with stitchable Metal functions for GPU effects.
- Choose the narrowest shader:
  - `colorEffect` for per-pixel color transformation
  - `distortionEffect` for position remapping
  - `layerEffect` only when sampling neighboring pixels or the rendered layer
- Declare an accurate `maxSampleOffset`; an incorrect bound can clip output or waste work.
- Treat shaders as stateless. Drive intentional animation with `TimelineView(.animation)` or explicit state and pass only the needed uniforms.
- Keep shader creation, textures, and immutable inputs stable; do not rebuild expensive resources every frame.
- Pause or simplify continuous effects when offscreen, inactive, Low Power Mode is relevant, or Reduce Motion is enabled.
- Provide a nonshader or static fallback when availability, accessibility, energy, or performance requires it.
- Use direct Metal only when SwiftUI shader effects, Canvas, and system frameworks cannot meet the rendering requirement. Check Metal feature support instead of assuming one GPU family.
- Profile with Instruments and Metal tools on representative hardware.

## Modern SwiftUI State and Performance

- Keep view identity stable and prefer concrete view types or `@ContentBuilder` over `AnyView` on update-heavy paths.
- Preserve simple show/hide identity when insertion and removal are unnecessary.
- Use stable identifiers for lists, reordering, shared transitions, and drag-and-drop.
- Prefer the new reorderable container APIs and swipe actions on arbitrary container content where their availability matches the project.
- Use lazy containers for large collections and measure before adding custom caching.
- Keep expensive work out of `body`, drawing callbacks, gesture updates, and per-frame timelines.
- Use the Xcode SwiftUI performance instruments and validate release builds.

## Accessibility

- Read `accessibilityReduceMotion` for custom movement and shader animation.
- Preserve meaning with a static state, restrained dissolve, text, symbol, or control state.
- Honor Reduce Transparency, Increase Contrast, Differentiate Without Color, Dynamic Type, VoiceOver, Switch Control, and Full Keyboard Access.
- Keep VoiceOver focus stable during transitions and glass morphs.
- Provide alternatives to gesture-only actions.
- Do not make motion, glass, shaders, color, sound, or haptics the only carrier of essential information.

## Reject Legacy-First Solutions

Do not introduce these as the preferred solution for new UI:

- storyboards or XIB-authored screens
- `NavigationView`
- broad implicit `.animation` without a value dependency
- device-idiom or `UIScreen`-bounds layout
- manual blur stacks that imitate Liquid Glass
- custom toolbar chrome that replaces current SwiftUI toolbars
- `ObservableObject` architecture when Observation fits
- display-link plumbing when `TimelineView`, SwiftUI animation, or a framework timeline fits
- new View Controller or AppKit view hierarchies without a documented SwiftUI gap

## Workflow

1. Inspect the project SDK, deployment targets, Swift language mode, framework mix, and existing design system.
2. Verify volatile APIs against the installed Xcode 27 SDK and current Apple documentation.
3. Build the semantic SwiftUI hierarchy and adaptive behavior before styling.
4. Let system controls adopt Liquid Glass before adding custom glass.
5. Add motion or shaders only with a named purpose and a reduced-motion outcome.
6. Implement only when requested; otherwise return a critique or implementation-ready plan.
7. Build and test in resizable previews, Simulator, and representative hardware.
8. Validate accessibility, performance, energy, interruption, resizing, inactive windows, and older-system fallbacks.

## Output

Lead with the current-platform decision. Cite `file:line` evidence when reviewing code. Label beta or experimental API explicitly. Separate required modernization, Liquid Glass correctness, adaptive layout, motion and shader quality, accessibility, and optional polish.
