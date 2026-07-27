# Native iOS Visual Audit Rubric

Use this rubric to keep a redesign audit evidence-based and consistent. It is not a numeric scorecard. A screen can look polished and still fail if hierarchy, behavior, accessibility, or state handling is weak.

## Contents

1. Capture matrix
2. Screen craft rubric
3. AI-slop pattern tests
4. Motion and interaction rubric
5. Evidence manifest
6. Acceptance-criteria patterns

## 1. Capture matrix

Audit applicable combinations rather than every theoretical permutation.

| Dimension | Baseline | Risk-driven additions |
| --- | --- | --- |
| Device | Primary supported iPhone | Smallest width, largest phone, iPad, resizable window |
| Appearance | Light | Dark, tinted preference, inactive presentation |
| Type | Default | Accessibility size, long localized copy |
| Motion | Default | Reduce Motion |
| Material | Default | Reduce Transparency, Increase Contrast |
| Content | Typical | Empty, dense, long, malformed, unavailable |
| Network | Healthy | Loading, slow, offline, recoverable failure |
| Account | Signed-in default | Signed-out, expired, restricted, premium/free |
| Input | Touch | Keyboard, pointer, VoiceOver, Switch Control where relevant |
| Lifecycle | Fresh launch | Background/foreground, restoration, interruption |

For each captured state record:

```text
Capture ID:
Screen and state:
Flow step:
Simulator/device:
OS/build/configuration:
Appearance:
Accessibility settings:
Locale/content fixture:
Screenshot path:
Video path and timestamp:
Source file:line or symbol:
Notes:
```

## 2. Screen craft rubric

### Purpose and hierarchy

- Can a person identify the screen’s job and next action immediately?
- Does the strongest visual emphasis match the most important task?
- Are secondary and destructive actions appropriately separated?
- Does repeated chrome overpower changing content?
- Is every heading needed?

### Structure and layout

- Does grouping follow meaning rather than a repeated card template?
- Are content margins, safe areas, and alignment lines consistent?
- Does the composition adapt rather than merely scale?
- Are lists, grids, panes, sheets, and toolbars the correct structural components?
- Does content remain stable when loading, updating, or rotating?

### Spacing

- Is spacing governed by a small rhythm or by local guesses?
- Do related items sit closer than unrelated groups?
- Are vertical gaps consistent at equivalent hierarchy levels?
- Do icon/text baselines align?
- Are tap targets and edge distances comfortable?

### Typography

- Do styles express semantic roles rather than one-off sizes?
- Is body measure readable?
- Are weight and color being used redundantly to create weak hierarchy?
- Does wrapping preserve meaning?
- Do truncation and minimum-scale behavior hide essential content?
- Does large Dynamic Type reorganize instead of clipping?

### Color, imagery, and symbols

- Are colors semantic and accessible in both appearances?
- Is the accent reserved for action, selection, or meaningful data?
- Are symbols from one coherent family and weight?
- Is imagery content, brand, instruction, or merely filler?
- Does generated or stock imagery make the product feel generic?

### Shape, material, and depth

- Are corner radii tied to component roles?
- Does every container need a visible outline or background?
- Is Liquid Glass limited to functional controls over content?
- Are shadows and blur consistent with actual layering?
- Does depth explain interaction order or merely decorate?
- Do transparency and contrast settings preserve hierarchy?

### Controls and input

- Are system controls used where their behavior is expected?
- Are labels precise and action-oriented?
- Are custom controls discoverable and accessible?
- Is destructive behavior confirmed or reversible?
- Does keyboard appearance preserve the active field and primary action?
- Are gestures optional enhancements rather than the only route?

### State quality

- Does loading preserve layout and avoid flashing placeholders?
- Does empty state explain what happened and what to do?
- Does error state preserve user work and offer recovery?
- Does offline behavior distinguish stale data from no data?
- Do success states avoid unnecessary ceremony?

## 3. AI-slop pattern tests

Flag a pattern only when it fails one or more tests.

### Generic gradient test

- Is the gradient connected to brand, data, state, lighting, or depth?
- Would replacing it with neutral material improve clarity?
- Does it create contrast or readability problems?
- Does it resemble an undifferentiated AI product landing page?

### Card-soup test

- Does the card establish a real interaction or grouping boundary?
- Could spacing, a section header, divider, list row, or pane express the structure better?
- Are nested cards creating arbitrary depth?
- Are corner radii inconsistent or excessive?

### Glass test

- Is the surface a functional control layer over changing content?
- Would the system component already provide the correct glass?
- Does custom glass survive Reduce Transparency and Increase Contrast?
- Does it remain legible over every underlying state?

### Decorative AI test

- Do sparkles, brains, magic wands, orbit lines, glows, or generated blobs communicate a real function?
- Is “AI” being shown instead of the user benefit?
- Does decoration create false affordance or compete with content?

### Generic copy test

- Does the text say something specific to the user’s state?
- Can redundant title/subtitle/body layers be collapsed?
- Does it sound like filler, encouragement, or model-generated explanation?
- Is an error or limitation described honestly?

### Trend test

- Would the design still make sense after the current visual trend fades?
- Does it follow platform behavior or mimic a screenshot aesthetic?
- Does it improve repeated daily use?

## 4. Motion and interaction rubric

### Purpose

Motion must provide feedback, continuity, state explanation, or an intentionally rare moment. Remove it when stillness communicates equally well.

### Continuity

- Does movement originate from the acted-on element?
- Do source and destination share conceptual identity?
- Are geometry, mask, material, shadow, and content synchronized?
- Does navigation preserve spatial orientation?

### Direct manipulation

- Does the object track the finger?
- Is velocity preserved on release?
- Can the gesture reverse and cancel?
- Does it coexist with scroll, back, sheet, and accessibility gestures?

### Timing and state

- Does the model state commit at the correct event?
- Can rapid repetition produce stale completions?
- Does loading finish without a one-frame intermediate state?
- Can an animation retarget from its currently visible state?

### Rendering quality

- Are there dropped frames, long frames, or input latency?
- Are blur, shadow, shader, and mask bounds stable?
- Does text rasterization remain crisp?
- Do effects pause offscreen and outside the active lifecycle?
- Is energy cost proportionate to value?

### Haptics and sound

- Is feedback tied to selection, threshold crossing, success, warning, or failure?
- Does it occur once at the committed event?
- Does it duplicate system feedback?
- Is the experience understandable without it?

### Accessibility

- Does Reduce Motion preserve meaning and state?
- Does VoiceOver focus land on the expected element?
- Does Reduce Transparency preserve layering?
- Can keyboard and Switch Control users perform the same action?

## 5. Evidence manifest

Use stable IDs:

- `SCR-###` for screenshots
- `VID-###@mm:ss.mmm` for video timestamps
- `SRC-path:line` for source evidence
- `AX-###` for accessibility snapshots or observations

Every P0/P1 finding should contain:

```text
Finding ID:
Priority:
Screen/state:
Observed behavior:
User impact:
Visual evidence:
Source evidence:
Principle:
Redesign direction:
Acceptance criteria:
Verification capture:
Confidence:
Residual unknown:
```

## 6. Acceptance-criteria patterns

Write observable outcomes, not implementation instructions.

Weak:

```text
Improve the animation and spacing.
```

Strong:

```text
Opening Detail from a selected row preserves the row’s visual identity, shows
no intermediate blank frame, remains interruptible during back navigation, and
has a reduced-motion dissolve. Verify in VID-Detail-Open at normal speed and
frame-by-frame around presentation and dismissal.
```

Weak:

```text
Use better typography.
```

Strong:

```text
The screen has one primary heading, body copy remains readable at accessibility
sizes without horizontal clipping, metadata stays visually secondary in light
and dark appearance, and equivalent semantic roles use the same text style
across all detail screens.
```

Weak:

```text
Add premium glass and shadows.
```

Strong:

```text
Remove decorative card backgrounds from content groups. Keep system-provided
glass only on the floating control layer, with legible Reduce Transparency and
Increase Contrast outcomes. Depth must correspond to presentation order.
```
