---
name: apple-design
description: Design, implement, or review native Apple-platform interfaces with Apple Human Interface Guidelines, platform conventions, accessibility, adaptive layout, direct manipulation, and fluid motion. Use for SwiftUI, UIKit, AppKit, watchOS, tvOS, or visionOS work involving navigation, controls, typography, materials, gestures, transitions, springs, haptics, reduced motion, or an Apple-native design critique. Do not use for web interfaces.
---

# Apple Design

Create interfaces that feel native to the Apple platform they run on. Favor clarity, directness, continuity, and system behavior over decorative imitation.

## Source Order

Use this order when guidance conflicts:

1. The current platform's Human Interface Guidelines and SDK documentation
2. Existing app behavior, design-system tokens, and project instructions
3. Standard SwiftUI, UIKit, AppKit, or other platform components
4. Custom behavior justified by a concrete user need

Treat upstream design-engineering advice as a lens, not a substitute for current Apple guidance. This skill is informed by Apple's Human Interface Guidelines, *Designing Fluid Interfaces* (WWDC18), and Emil Kowalski's `apple-design` skill, adapted for native Apple development.

## Design Principles

Use these principles to make tradeoffs:

- **Purpose:** Make the primary task and next action obvious. Remove elements that do not help.
- **Agency:** Keep people in control. Make actions reversible and reserve confirmation for genuinely destructive consequences.
- **Familiarity:** Use platform conventions and standard components unless a tested alternative is better.
- **Flexibility:** Support different devices, window sizes, orientations, input methods, languages, and abilities.
- **Simplicity:** Show the common path first without hiding information people need to decide.
- **Craft:** Treat typography, alignment, motion, sound, haptics, and wording as one system.
- **Delight:** Earn delight through responsiveness and care; do not attach spectacle to routine work.

## Platform Fit

- Identify the exact target: iOS, iPadOS, macOS, watchOS, tvOS, or visionOS. Do not flatten their conventions into a generic Apple look.
- Prefer standard navigation, presentation, controls, symbols, materials, menus, focus behavior, and gestures.
- Preserve content hierarchy across size changes, but change presentation when the platform calls for it. A sheet on iPhone may become a persistent inspector or secondary column on iPad or macOS.
- Respect safe areas, keyboard avoidance, pointer and keyboard input, multitasking, rotation, and window resizing.
- Use system fonts and text styles by default. Support Dynamic Type and test the largest accessibility sizes.
- Use SF Symbols semantically and keep symbol rendering, weight, and animation consistent with nearby text and controls.

## Interaction

- Give immediate feedback when contact begins and commit an action when the interaction completes.
- Keep dragged content attached to the gesture in the same coordinate space. Preserve the grab offset.
- Allow cancellation where the system convention allows it; do not trap people in a transition.
- Prefer system gesture recognizers and components before custom recognizers.
- Keep alternate access available for gesture-only actions, including VoiceOver actions, keyboard commands, menus, or visible controls.
- Use haptics and sound only for meaningful events. Align them with the visual state change and never make them the only feedback.

## Motion

Add motion only when it provides feedback, preserves spatial context, explains a state change, or prevents a disorienting jump.

- Keep routine interactions brief and restrained.
- Let people interrupt and reverse gesture-driven motion.
- Continue from the visible state and current velocity when retargeting.
- Use a spring for physical, interactive movement. Avoid bounce unless the gesture or product character earns it.
- Enter and exit along a coherent path. Anchor a transition to its source when that relationship helps understanding.
- Keep navigation and system component motion familiar. Do not replace a platform transition merely to make the app look distinctive.
- Never block input solely because an animation is running.

### SwiftUI

- Drive motion from explicit state.
- Use `withAnimation` for a bounded state change and `.animation(_:value:)` only when the dependency is clear.
- Use `spring` or `interactiveSpring` for retargetable physical motion.
- Use `PhaseAnimator` or `KeyframeAnimator` only for noninteractive sequences that genuinely need choreography.
- Use `matchedGeometryEffect` only when two views represent the same conceptual object and the identity remains understandable.
- Pair insertion and removal transitions deliberately; verify interrupted and rapidly repeated state changes.
- Use `Transaction` to disable or replace inherited animation where motion would be misleading.

### UIKit and AppKit

- Prefer interruptible property animators for interactive transitions.
- Connect transition progress to the gesture continuously.
- Seed continuation with current progress and velocity instead of restarting from a model target.
- Read the presentation state when necessary to prevent jumps during interruption.
- Keep custom transition controllers cancelable and test both completion and reversal.

## Materials, Depth, and Typography

- Use system materials to express layering and focus, not as decoration.
- Avoid stacking translucent surfaces until text and controls lose contrast.
- Pair elevation, dimming, scale, and material changes with a clear hierarchy.
- Keep text legible over changing content and honor Increase Contrast and Reduce Transparency.
- Build hierarchy with semantic text styles, weight, spacing, and placement. Do not encode hierarchy with size alone.
- Let text expansion reflow the layout. Do not truncate essential actions or values at accessibility sizes.

## Accessibility

- Read `accessibilityReduceMotion` in SwiftUI or the equivalent platform setting for custom motion.
- Under reduced motion, preserve meaning with a restrained dissolve, highlight, or direct state change; remove large movement, parallax, and unnecessary spring effects.
- Honor Reduce Transparency, Increase Contrast, Differentiate Without Color, VoiceOver, Switch Control, Full Keyboard Access, and Dynamic Type where applicable.
- Keep interactive targets at least as large as the current platform guidance requires.
- Never use motion, color, sound, or haptics as the only carrier of essential information.

## Workflow

1. Identify platform, framework, device classes, input methods, and the user's primary task.
2. Read project instructions and inspect the existing design system, navigation, components, motion, and accessibility support.
3. Describe the current hierarchy and interaction before proposing changes.
4. Prefer a standard platform component or transition when it satisfies the need.
5. For custom motion, state its purpose, trigger, path, interruption behavior, reduced-motion behavior, and performance risk.
6. Implement only when the user asked for changes; otherwise return a critique or implementation-ready recommendation.
7. Validate in previews or a simulator, then on representative hardware for gestures, haptics, performance, and platform feel.
8. Test light and dark appearance, text scaling, reduced motion, rotation or resizing, and rapid repeated interaction.

## Output

Lead with the strongest design decision or highest-impact issue. Cite concrete views and `file:line` evidence when reviewing code. Separate platform violations, usability risks, motion polish, and optional refinements. Avoid prescribing a custom animation when the system behavior is already the better design.
