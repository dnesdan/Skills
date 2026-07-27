---
name: prototype-ui-with-imagegen
description: >-
  Explore genuinely different visual directions for one native Apple or Android
  UI surface with Codex's built-in image generation, compare the generated
  concepts against product and platform constraints, and optionally rebuild a
  user-selected direction in SwiftUI or Jetpack Compose. Use when the user asks
  for UI concepts, image-generated redesign variants, a native component or
  screen prototype, more options around a chosen concept, or implementation of
  a selected generated direction. Keep exploration read-only and stop before
  production changes unless the user explicitly selects a variant to keep. Do
  not use for web, HTML, CSS, or generated production UI assets.
---

# Prototype Native UI with Image Generation

Use image generation as a divergence tool, not as the implementation. Generate
visual hypotheses, judge them against the real product, then rebuild only an
explicitly selected direction with native code.

## Interpret the invocation

Support these modes:

- **Explore** — default; generate three directions, compare them, recommend one,
  and stop without changing the project.
- **Explore x5** — generate at most five directions when the user explicitly
  requests five or uses `x5`.
- **Riff `<variant>`** — generate three new directions around a named result
  while preserving its successful principles. Do not edit the project.
- **Keep `<variant>`** — implement the selected result in the real app, validate
  it at runtime, and report the changes.

Treat one component, screen, state, or short coherent flow as one run. If the
request spans many surfaces, select the highest-value representative surface
when that is safe; otherwise ask the user to narrow the target.

## Enforce hard boundaries

- Use Codex's built-in `image_gen` path by default. Do not require Claude,
  Fable, Codex MCP, another model host, or an API key.
- Do not create an HTML, CSS, JavaScript, or browser-based variant picker.
  Present images directly in Codex.
- In Explore and Riff, do not edit source, assets, documentation, project
  settings, or Git state. Keep preview artifacts outside the repository.
- Never ship a generated screenshot as the interface, a sliced mockup, a
  background that contains controls, or a substitute for native code.
- Do not invent product capabilities, data, navigation destinations, or copy to
  make a concept look complete.
- Do not claim that a still image validates motion, gestures, haptics, focus,
  accessibility, dynamic content, localization, or runtime performance.
- Preserve unrelated user changes. Commit only when the user asked for a
  commit.

If built-in image generation is unavailable, state that the default path cannot
run. Offer the imagegen CLI fallback only as an explicit opt-in because it
requires an API key; never switch silently.

## 1. Reconstruct the real product

Before prompting:

1. Read repository instructions and inspect Git status without changing it.
2. Identify Apple versus Android, the real UI stack, deployment targets,
   supported devices, design tokens, reusable components, and current state
   management.
3. Load the applicable installed `apple-design` or `android-design` skill when
   available. Treat its current platform baseline as authoritative; verify
   volatile or prerelease APIs against first-party documentation and the
   installed SDK.
4. Inspect the target source and adjacent states: loading, empty, populated,
   error, disabled, permission, keyboard, large text, dark appearance, and
   adaptive layouts as relevant.
5. Capture or reuse a representative runtime screenshot when possible. For a
   local screenshot, call `view_image` before passing it to built-in image
   generation.

Label every input image:

- **Edit target** when structure, content, and identity must remain and only
  specified visual properties may change.
- **Reference** when it communicates product context, composition, or style but
  genuine structural divergence is allowed.

If runtime capture is blocked, continue from source evidence and label the
concepts source-informed rather than runtime-verified.

## 2. Freeze the brief

Write a compact brief before generation:

- platform, device or window class, appearance, and exact UI state
- primary user job and primary action
- source-backed content and verbatim copy
- an allowlist of visible controls and interactive affordances confirmed by
  source or the user
- invariants that every direction must preserve
- freedoms the concepts may explore
- forbidden additions and known accessibility or localization constraints
- implementation constraints from the actual project

Do not use generated text as the source of truth. Repository copy and product
requirements win even when the image renders different text.

Treat every back arrow, hamburger, overflow menu, chevron, tab, filter, badge,
row action, and floating button as product behavior rather than harmless visual
decoration. Do not allow one unless source evidence or the user confirms it.
Do not infer calendar weekdays, progress values, destinations, or other facts
from incomplete inputs.

## 3. Generate real alternatives

Read [variant-prompting.md](references/variant-prompting.md) before generating.
Classify each request as `ui-mockup`.

Issue one built-in `image_gen` call per direction with a separate prompt. Do not
use one multi-output request as a substitute for intentionally different
prompts. Generate three directions by default and no more than five.

Give every direction:

- a memorable neutral name
- one primary design thesis
- at least one meaningful axis of divergence such as layout, density,
  hierarchy, navigation model, disclosure, spatial organization, or
  interaction model
- the shared brief and invariants
- platform, viewport, state, and output framing identical to the other
  directions so comparison remains fair

Do not count palette, gradient, corner-radius, glass, shadow, illustration, or
copy changes alone as a distinct direction.

Inspect every result at readable size. Reject or retry once with a single
targeted correction when a result breaks an invariant, invents functionality,
adds an unapproved interactive affordance, has impossible geometry, clips
essential content, or becomes unusable because of malformed text. Keep the
original direction thesis during a correction.

## 4. Evaluate before recommending

Read [evaluation-rubric.md](references/evaluation-rubric.md). Evaluate each
direction as `Pass`, `Concern`, or `Fail`; do not manufacture numeric precision.
A hard failure cannot win.

Present each image inline at a useful size rather than only in a contact sheet.
For each direction, state:

- what it tests
- what improves over the current surface
- its product and accessibility tradeoffs
- native implementation feasibility
- likely implementation cost or risk

Recommend one result only when it clearly fits the brief. Otherwise say that
there is no winner and identify the smallest useful next generation pass.

Return exactly:

1. **Prototype brief**
2. **Current evidence**
3. **Generated directions**
4. **Constraint comparison**
5. **Recommendation**
6. **What image generation did not verify**
7. **Choose next step** — `keep <name>`, `riff <name>`, or stop

Then stop. Explore and Riff must not proceed into implementation.

## 5. Riff on a direction

Resolve the selected image from the current conversation or ask the user to
reattach it. Preserve the chosen direction's successful hierarchy, product
job, content, and platform conventions.

Generate three fresh alternatives, each changing one or two named aspects.
Avoid cosmetic mutations. Re-run the same evaluation and output contract, then
stop again.

## 6. Keep and rebuild natively

Enter this phase only after an explicit `keep`, unambiguous selection, or direct
request to implement a named generated result.

Read:

- [apple-promotion.md](references/apple-promotion.md) for Apple projects, or
- [android-promotion.md](references/android-promotion.md) for Android projects,
- plus [visual-validation.md](references/visual-validation.md) in both cases.

Translate the chosen image into explicit rules for hierarchy, layout, spacing,
type roles, color roles, materials, component boundaries, states, and motion
intent. Treat the image as a design reference, not a pixel contract. Resolve
ambiguous or generated details using the product model, native conventions,
accessibility, and source copy.

Implement with the project's existing architecture and reusable primitives.
Add a custom control, shader, blur, glass treatment, or transition only when it
has a named functional purpose and a graceful accessibility and availability
fallback.

Build and run the actual app. Capture the same state and viewport as the
reference, compare structure at full screen and in focused crops, and make
targeted corrections. Test real interaction, alternate states, large text,
dark appearance, reduced motion, and adaptive sizing as applicable. Record
motion when judging motion.

Finish with:

- selected direction and extracted design rules
- files changed
- build, test, and runtime validation performed
- visual differences intentionally retained and why
- unverified devices, states, or risks
- commit hash only when a commit was requested and succeeded

Do not call the result complete when the app was not run, unless the environment
made runtime validation impossible; state that limitation directly.
