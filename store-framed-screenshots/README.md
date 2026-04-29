# Store Framed Screenshots

Create polished App Store and Google Play screenshot sets from real app captures using internal image generation.

This skill is built for teams that want store-ready screenshots without maintaining a separate web export toolchain. It keeps the app UI truthful, wraps it in consistent device framing, and produces a focused marketing story for each platform, locale, and device class.

## What It Does

- Plans App Store and Google Play screenshot sets.
- Turns real raw screenshots into framed marketing screenshots.
- Keeps device placement, aspect ratio, typography, and background treatment consistent across a set.
- Preserves the app UI instead of inventing fake screens.
- Supports iPhone, iPad, Android phone, and Android tablet outputs.
- Helps localize headline overlays while keeping raw app UI localization separate.
- Validates final dimensions, platform framing, text accuracy, raw UI preservation, and store-policy risks.

## Good Use Cases

- You have raw simulator or device screenshots and want polished store assets.
- You need a consistent screenshot campaign for multiple locales.
- You want the first 3 screenshots to tell a sharper conversion story.
- You need iPhone, iPad, Android phone, or Android tablet framing without hand-building a generator.
- You want a contact sheet review before selecting final submission assets.

## Example Prompts

```text
Use $store-framed-screenshots to create an English App Store iPhone screenshot set from the raw screenshots in ./local_screenshots/raw. Keep a premium minimal style, use strict consistent placement, and output framed PNGs to ./app_store_assets/screenshots/en/iphone.
```

```text
Use $store-framed-screenshots to plan a 10-frame App Store screenshot story for this app. I have iPhone and iPad raw screenshots already. Return the frame plan, headline copy, raw capture list, and layout lock before generating.
```

```text
Use $store-framed-screenshots to regenerate these Google Play phone screenshots with the same visual system as ./references/approved-contact-sheet.png. Preserve the raw UI exactly, keep the Android frame physically correct, and avoid promotional claims or CTAs.
```

```text
Use $store-framed-screenshots to localize the approved English set into German, Spanish, and Japanese. Keep the same layout lock, use localized raw screenshots when available, and flag any headline that needs shorter wording.
```

## Workflow

1. Gather app context, target stores, device classes, locales, raw screenshot sources, visual direction, and output path.
2. Pick exact output slots from `references/store-dimensions.md`.
3. Build the screenshot story with one short benefit-led headline per frame.
4. Capture or collect truthful raw screenshots.
5. Define the campaign bible and layout lock.
6. Generate one approved style frame first, then the remaining frames.
7. Validate every final image visually and by file dimensions.
8. Save raw and framed outputs separately with predictable names.

## Campaign Quality Bar

Every set should have a compact campaign bible:

- Platform mode: iOS, Android, tablet, or mixed.
- Device presentation: frame style, aspect ratio, scale, anchor, and shadow.
- Visual system: palette, background material, accent language, typography mood, and headline treatment.
- Content rules: real raw UI only, one benefit per frame, readable thumbnail hierarchy, and no unsupported claims.
- Consistency rules: keep the same visual system across every frame, locale, and variant unless a documented store or device constraint forces a change.

The skill should reject warped phones, stretched screenshots, generic imagegen backgrounds, invented app UI, fake badges, unsupported claims, inconsistent hardware, and tiny unreadable screens.

## Subagent Support

When the Codex environment supports subagents, this skill can split planning and QA work:

- Raw-shot auditor: checks screenshot folders for weak, blank, duplicated, debug, mismatched, or policy-risk shots.
- Copy planner: drafts frame sequencing and headline options.
- Prompt planner: prepares the campaign bible, layout lock, and per-frame imagegen prompts.
- Platform verifier: checks final dimensions, naming, locales, device proportions, text accuracy, and visual consistency.

Generation usually stays in the main thread unless separate agents own separate output folders.

## Showcase Contact Sheets

We will add 2-3 contact sheets here using finished screenshot sets from our own apps. These should work as examples and as quiet product promotion.

Suggested structure:

```text
assets/showcase/
  app-one-contact-sheet.png
  app-two-contact-sheet.png
  app-three-contact-sheet.png
```

Suggested Markdown once the images exist:

```markdown
![App One framed screenshot contact sheet](assets/showcase/app-one-contact-sheet.png)
![App Two framed screenshot contact sheet](assets/showcase/app-two-contact-sheet.png)
![App Three framed screenshot contact sheet](assets/showcase/app-three-contact-sheet.png)
```

Each contact sheet should show the final framed outputs, not raw screenshots, and should include enough variety to demonstrate iPhone, iPad, Android phone, Android tablet, localization, or visual direction when available.

## Files

- `SKILL.md` - trigger metadata and core workflow.
- `references/store-frame-planning.md` - screenshot story, headlines, layout lock, and localization planning.
- `references/store-dimensions.md` - App Store and Google Play slot guidance.
- `references/capture-integration.md` - repeatable raw screenshot capture options.
- `references/imagegen-framing-prompts.md` - prompt templates, device framing rules, and validation checklist.
