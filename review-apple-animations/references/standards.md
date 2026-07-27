# WWDC 2026 Apple Motion and Graphics Standards

Use this reference for SwiftUI-first review with Xcode 27 and the 2027 platform releases.

## Contents

1. Source and availability
2. Liquid Glass
3. SwiftUI motion and navigation
4. Metal-backed SwiftUI shaders
5. Resizing and identity
6. Accessibility and lifecycle
7. Performance and validation
8. Modernization triggers

## Source and Availability

Verify volatile claims against:

- [SwiftUI updates](https://developer.apple.com/documentation/updates/swiftui)
- [What's new in SwiftUI — WWDC26](https://developer.apple.com/videos/play/wwdc2026/269/)
- [Compose advanced graphics effects with SwiftUI — WWDC26](https://developer.apple.com/videos/play/wwdc2026/322/)
- [Materials](https://developer.apple.com/design/human-interface-guidelines/materials)
- [Motion](https://developer.apple.com/design/human-interface-guidelines/motion)

Treat beta signatures as provisional. Check the installed SDK, wrap platform-specific APIs in the narrowest availability gate, and provide a current architectural fallback.

## Liquid Glass

- System navigation, toolbar, tab, search, menu, and standard control surfaces receive current Liquid Glass automatically.
- Custom glass belongs on important functional controls floating over content, not on the content layer.
- Use `.buttonStyle(.glass)` or `.buttonStyle(.glassProminent)` for glass buttons and shape them with `buttonBorderShape(_:)`.
- Apply `glassEffect` after layout and appearance modifiers.
- Mark only interactive surfaces with `.interactive()`.
- Prefer regular glass; clear glass requires visually rich backing content and verified legibility.
- Group multiple effects in `GlassEffectContainer`.
- Use `glassEffectID` only for real hierarchy-changing morphs with stable identity.
- Keep system toolbar glass unless `sharedBackgroundVisibility(_:)` or `contentMarginsRemoved(_:)` has a semantic reason.
- Verify automatic 2027 tint response, inactive-window appearance, Reduce Transparency, Increase Contrast, and availability fallback.
- Reject manual blur and translucency stacks that imitate Liquid Glass.

## SwiftUI Motion and Navigation

- Drive animation from explicit state.
- Use `withAnimation` for a bounded mutation and `.animation(_:value:)` for one named dependency.
- Prefer `.smooth`, `.snappy`, `.bouncy`, or `spring(duration:bounce:)` by intended behavior.
- Use springs for retargetable physical movement and preserve velocity at gesture release.
- Use `PhaseAnimator` and `KeyframeAnimator` for deliberate noninteractive sequences.
- Keep direct manipulation interruptible and reversible from the visible value.
- Use stable identity for lists, reordering, matched geometry, and transitions.
- Use `matchedGeometryEffect` for the same conceptual object within a hierarchy.
- Use `matchedTransitionSource` and framework-provided navigation transitions where available.
- Do not invent a custom `NavigationTransition` conformance when the SDK exposes only framework-provided implementations.
- Use `Transaction` to suppress inherited motion that would animate unrelated state.
- Never lock input only because an animation is running.

## Metal-Backed SwiftUI Shaders

- Use `ShaderLibrary` and stitchable Metal functions with the narrowest SwiftUI modifier:
  - `colorEffect` for color transformation
  - `distortionEffect` for remapping positions
  - `layerEffect` only when sampling the rendered layer or neighboring pixels
- Verify Metal function signature and SwiftUI argument order.
- Declare `maxSampleOffset` large enough for every sample and no larger than needed.
- Keep textures, shader functions, and immutable inputs stable.
- Treat shaders as stateless. Pass time or state explicitly.
- Use `TimelineView(.animation)` only while visible and meaningful.
- Stop, reduce, or replace continuous motion for Reduce Motion, inactive scenes, and power-sensitive contexts.
- Provide a static or nonshader fallback for availability and accessibility.
- Avoid shaders on text, controls, and information-dense content when they reduce legibility.
- Use direct Metal only when SwiftUI graphics and shader effects cannot meet the rendering requirement; check feature support.

## Resizing and Identity

- Assume continuous resizing on iPhone, iPad, and Mac.
- Use size classes and adaptive structure, not device idiom or screen bounds.
- Keep toolbars functional as width shrinks with visibility priorities and overflow.
- Preserve selected content, focus, navigation state, and transition identity when pane count changes.
- Avoid fixed frames that make animated endpoints wrong at another size.
- Prefer concrete view types or `@ContentBuilder` over `AnyView` in frequently updating hierarchies.
- Avoid unnecessary structural insertion/removal when visibility can preserve identity.

## Accessibility and Lifecycle

- Read `accessibilityReduceMotion` for custom movement and shader timelines.
- Preserve meaning through a static state, restrained dissolve, label, symbol, or control state.
- Verify Reduce Transparency, Increase Contrast, Differentiate Without Color, VoiceOver, Switch Control, keyboard input, and Dynamic Type.
- Keep VoiceOver focus and reading order stable across transitions and morphs.
- Pair haptics and audio with the committed event; never use them as the only signal.
- Cancel tasks and timelines when their view or scene is no longer active.

## Performance and Validation

- Keep expensive work out of `body`, gesture callbacks, drawing callbacks, and per-frame timelines.
- Avoid per-frame texture creation, allocation, geometry discovery, and state publication.
- Bound blur, translucency, masks, shadows, offscreen layers, and sample regions.
- Validate release builds with Instruments, SwiftUI performance tools, Metal tools, Energy Log, and representative hardware.
- Exercise entry, exit, interruption, reversal, rapid repeat, cancellation, resize, background, foreground, and older-system fallback.
- Inspect slow motion or frame-by-frame for origin, velocity handoff, clipping, and coordinated state.

## Modernization Triggers

Raise a finding when new or touched code relies on:

- storyboards, XIBs, or new controller-owned screens without a SwiftUI gap
- `NavigationView`
- broad implicit animation
- `UIScreen` bounds or device idiom for layout
- manual Liquid Glass imitation
- `ObservableObject` architecture where Observation fits
- display-link plumbing where SwiftUI animation or `TimelineView` fits
- custom toolbar backgrounds or navigation transitions replacing correct system behavior
- beta APIs without an availability and fallback plan
