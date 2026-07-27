# Promote a Selected Apple Direction

Load the installed `apple-design` skill before implementation. Its current
platform baseline and freshness checks take precedence over this concise
handoff. Verify prerelease declarations against Apple documentation and the
project's installed Xcode SDK.

## Convert image decisions into SwiftUI

Extract:

- semantic content hierarchy and reading order
- adaptive container and navigation choice
- system text styles and scalable spacing relationships
- semantic colors, materials, control prominence, and depth layers
- reusable component boundaries and explicit UI states
- intended transition relationships, not imagined timing from a still

Implement new interface work in SwiftUI with the project's existing
architecture. Prefer semantic system navigation, toolbars, tabs, search,
presentations, controls, symbols, text styles, and gestures.

Use Liquid Glass on a functional control layer when current system APIs and the
design purpose support it. Do not reproduce glass by stacking arbitrary blur,
gradients, borders, and shadows. Use custom rendering, SwiftUI shaders, Canvas,
or Metal only for a named content or interaction purpose, with bounded work,
availability handling, and a legible fallback.

## Required checks

- safe areas, keyboard avoidance, rotation, resizing, iPhone and iPad where
  supported
- Dynamic Type, VoiceOver reading and focus order, Increase Contrast, Reduce
  Transparency, and Reduce Motion
- semantic actions and alternatives for gesture-only behavior
- dark and light appearances, localization, long content, loading, empty,
  error, disabled, and interrupted states as relevant
- transition interruption, reversal, rapid repeat, and state preservation
- release-like runtime behavior for custom drawing, blur, shaders, or motion

Do not add UIKit, AppKit, storyboards, CSS, HTML, or WebViews to reproduce the
mockup. Keep an existing interoperability boundary only when the project needs
it.
