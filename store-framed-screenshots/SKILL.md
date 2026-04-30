---
name: store-framed-screenshots
description: Create polished App Store and Google Play framed screenshot sets with internal imagegen from real raw app screenshots. Use when planning, capturing, framing, contact-sheet reviewing, localizing, resizing, validating, or regenerating store screenshots for iPhone, iPad, Android phone, or Android tablet, especially when consistent device placement, exact store dimensions, truthful app UI preservation, and correct device proportions matter.
---

# Store Framed Screenshots

## Overview

Create conversion-ready store screenshots from real app captures. The skill is a two-stage workflow:

1. Capture or collect truthful raw screenshots for each platform, locale, appearance, and device class.
2. Use internal imagegen to produce the marketing wrapper: device frame, background, headline, and polish.

Default to an English master set first. Generate localized sets only after the English layout and message order are approved.

## Non-Negotiables

- Use the internal imagegen skill/tool path for framed art. Do not scaffold web generators or require npm, bun, Next.js, Playwright exports, or browser-based renderers.
- Preserve truthful app UI. Final store assets should use real raw screenshots unless the user explicitly asks for concepts.
- Keep raw screenshots and framed outputs separate.
- Do not let imagegen invent or alter in-app UI, ratings, claims, prices, subscription terms, badges, awards, store logos, or platform chrome.
- Use iPhone/iPad frames for iOS outputs and Android phone/tablet frames for Android outputs.
- Use real, recognizable device hardware for the selected platform. For modern iPhone shots, include believable
  hardware cues such as Dynamic Island/camera cutout, bezels, side buttons, screen curvature, and shadow.
- Keep device and visible screen aspect ratios physically faithful to the selected device class; never stretch, squash, or cosmetically distort the raw screenshot inside a frame.
- Respect Google Play restrictions: no misleading ranking, price, promo, testimonial, or call-to-action text; keep taglines minimal.
- Localize overlays and raw app UI separately. Do not translate in-app UI inside a screenshot unless the user asks for a rough concept.
- Validate every final image visually and with file dimensions before handoff.

## Default Layout Policy

By default, keep device placement consistent across every screenshot in the same platform/device/locale set. Consistency beats novelty unless the user explicitly asks for a creative or highly varied campaign.

Use a **layout lock** per set:

- Same canvas size, orientation, device frame style, device scale, device anchor, headline zone, typography mood, safe margins, shadow style, and background system.
- Headlines may change line breaks, but should occupy the same reserved text area.
- Lock headline typography after the first approved frame: same font family, weight, cap height, line height, text box,
  alignment, and color. Fit long copy with shorter wording or line breaks before changing font size.
- Background accents may vary subtly by frame, but never move the device or change the visual system.
- Keep the phone/tablet large enough that the raw UI is readable at store thumbnail size.
- Use multi-device, angled, cropped, or alternating layouts only when the user asks for creativity or when a specific frame truly needs comparison.

When the user asks for creative variation, define 2-3 approved layout templates first and apply them intentionally instead of improvising per frame.

## Campaign Quality Bar

Before batch generation, define a compact campaign bible for the set:

- Platform mode: iOS, Android, tablet, or mixed platform.
- Device presentation: hardware style, aspect ratio, scale, shadow, and anchor.
- Visual system: palette, background material, accent language, typography mood, headline treatment, and safe margins.
- Content rules: real raw UI only, one benefit per frame, readable thumbnail hierarchy, and no unsupported claims.
- Consistency rules: keep the campaign bible stable across every frame, locale, and variant unless a documented store/device constraint forces an adjustment.

Avoid default imagegen slop: warped phones, inconsistent mockups, generic purple-blue gradients, noisy decorative clutter, tiny unreadable UI, extra invented text, fake store badges, and repeated layouts that do not advance the screenshot story.

## Workflow

1. Gather context:
   - App name, one-sentence value proposition, platforms, stores, locales, target country, screenshot count, orientation, and output folder.
   - Raw screenshot source: existing files, simulator/emulator capture, or a capture plan.
   - Visual preference: minimal premium, bold colorful, playful game-like, editorial, dark high-contrast, or existing brand style.
   - Whether the set should use strict consistent placement or creative variation.

2. Select output slots:
   - For App Store, use exact accepted screenshot dimensions for the requested display class. See `references/store-dimensions.md`.
   - For Google Play, use Play-safe 9:16 portrait or 16:9 landscape assets within current constraints. See `references/store-dimensions.md`.
   - Prefer generating at final size directly. If imagegen returns a smaller file, resize only after inspecting quality and disclose the risk.

3. Build a frame plan:
   - Default to up to 10 App Store frames or up to 8 Google Play screenshots when enough meaningful raw screens exist.
   - Make frames 1-3 carry the conversion story: primary promise, core loop, retention/proof/personalization.
   - Use one short benefit-led headline per frame.
   - Include the exact raw screenshot file or capture requirement for every frame.
   - See `references/store-frame-planning.md`.

4. Capture or collect raw screenshots:
   - Prefer real app screenshots captured at the requested device class and locale.
   - For iOS SwiftUI apps, a deterministic in-app capture mode can be used when the project supports it. See `references/capture-integration.md`.
   - For Android, use emulator/device screenshots, seeded app state, and locale/appearance relaunches when possible.
   - Exclude blank, debug, unstable, duplicated, or visually weak raw shots from final framing.

5. Define the layout lock:
   - Choose canvas size, headline zone, device scale, device anchor, aspect-ratio constraints, and background system before batch generation.
   - Write a compact campaign bible when the set has more than one frame or locale.
   - If the user approves a first frame, reuse it as the style/layout reference for the set and explicitly lock headline typography and device placement to it.
   - Write these values into every imagegen prompt.
   - Generate one style frame first for new visual directions. After approval, reuse the same layout lock for the remaining frames.

6. Generate with imagegen:
   - Inspect each raw screenshot before generation.
   - Use one imagegen call per final frame or variant.
   - Save final selected outputs into the requested project/workspace folder; never leave final assets only under the generated-images cache.
   - Use prompt templates in `references/imagegen-framing-prompts.md`.

7. Localize after English approval:
   - Translate overlay headlines from the approved English plan.
   - Use localized raw app screenshots whenever possible.
   - Keep the same layout lock across locales unless text expansion forces a documented adjustment.
   - For RTL languages, mirror only when the composition benefits from native RTL flow.

8. Validate:
   - Correct store slot and dimensions.
   - Correct platform frame and hardware cues.
   - Realistic named-device hardware, not a generic rounded rectangle.
   - Physically believable phone/tablet and screen aspect ratio.
   - Exact headline text and no extra text.
   - Headline font size, line height, placement, and color match the approved set lock.
   - Raw UI preserved and readable.
   - Layout placement consistent across the set unless creative variation was requested.
   - No policy-risk claims, badges, rankings, CTAs, or fake UI.
   - Predictable filenames and clear raw/framed folder separation.

## Subagent Use

Use subagents only when the current Codex environment supports them and the task benefits from parallelism:

- Raw-shot auditor: inspect screenshot folders and flag weak, blank, duplicated, debug, aspect-ratio-mismatched, or policy-risk shots.
- Copy planner: draft a frame plan and headline alternatives from product context, metadata, or target keywords.
- Prompt planner: prepare the campaign bible, layout lock, and per-frame imagegen prompts.
- Platform verifier: check final dimensions, naming, locale coverage, device proportions, text accuracy, and visual consistency.

Keep generation itself in the main thread unless workers have disjoint output folders. Never let multiple agents overwrite the same screenshot set. When subagents are used, consolidate their findings into one plan before prompting imagegen.

## Output Conventions

Use the user's requested destination when provided. Otherwise prefer:

```text
local_screenshots/store-framed/<app>/<locale>/<platform>/<device-class>/raw/
local_screenshots/store-framed/<app>/<locale>/<platform>/<device-class>/framed/
```

For intentionally curated submission bundles:

```text
app_store_assets/screenshots/<app>/<locale>/<platform>/<device-class>/
```

Use lowercase, sortable filenames:

```text
01-primary-promise-iphone-en.png
02-core-loop-android-en.png
03-daily-habit-ipad-cs.png
```

## Response Shape

When planning, return:

- `Screenshot Brief`
- `Output Slots`
- `Frame Plan`
- `Raw Capture List`
- `Layout Lock`
- `Imagegen Prompt Set`
- `Localization Notes`

When generating, return:

- Final saved paths
- Platform/device/locale coverage
- Validation notes
- Missing raw screenshots or residual risks

## Reference Map

- `references/store-frame-planning.md`: frame sequencing, headline rules, capture table, and localization planning.
- `references/store-dimensions.md`: current App Store and Google Play screenshot slot guidance.
- `references/capture-integration.md`: deterministic raw capture guidance, including iOS in-app marketing capture.
- `references/imagegen-framing-prompts.md`: imagegen prompt templates, layout-lock wording, platform framing rules, and validation checklist.
