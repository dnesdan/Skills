# Native Component Gate

Create this map before prompting and verify it again after generation.

## Resolution order

Map every visible structural or interactive element in this order:

1. **Existing project component** — reuse its behavior, identity, states, and
   tokens.
2. **Current semantic platform component** — use the installed SDK and the
   applicable `apple-design` or `android-design` skill.
3. **Custom native primitive** — allow only when the first two cannot express a
   named product or interaction need.

Never use image generation to visually replace a component whose behavior and
identity already exist in code.

## Component map

Record one row for every visible region:

| Region | Current source/component | Proposed native component | Preserve/change | Custom justification |
| --- | --- | --- | --- | --- |
| App shell | `<source symbol>` | same project component | Preserve | — |
| Primary action | `<source symbol>` | `<platform control>` | Preserve behavior | — |
| Content visualization | `<source symbol>` | `<platform API or custom>` | Allowed to change | `<why native APIs do not fit>` |

Include navigation, tabs or navigation suite, toolbars/top app bar, sheets,
lists, buttons, menus, progress, charts, search, input, symbols/icons,
materials, and custom drawing when visible.

## Preserve by default

Unless the user explicitly names them as redesign targets, preserve:

- navigation destinations, back behavior, tab destinations, labels, ordering,
  and selected state
- the current system navigation/tab/toolbar presentation
- existing project components and their interaction semantics
- brand and semantic colors, typography roles, symbols, assets, and materials
- all visible real content modules, actions, states, and monetization surfaces

Changing layout hierarchy does not authorize changing the app shell or removing
content.

## Custom-native budget

A custom primitive must include:

- the product or interaction need that system/project components cannot meet
- semantic and accessibility behavior
- adaptive and localization behavior
- reduced-motion or animation-disabled behavior when animated
- availability and performance fallback

Custom navigation, tabs, standard buttons, toggles, fields, menus, or
presentations are a hard failure unless the user explicitly requires behavior
the platform component cannot provide.

## Post-generation gate

Inspect the raster rather than trusting the prompt. Fail a literal direction
when it:

- replaces current platform chrome with a flat, generic, fabricated, or
  obsolete-looking imitation
- changes project symbols, tab icons, labels, ordering, accent, type roles, or
  materials without permission
- drops or invents a visible content module or control
- cannot be mapped to the declared native components
- makes a custom visualization carry navigation or core control behavior

A structurally promising failed direction may be riffed after restoring the
preserved shell and component identity. It cannot win as rendered.
