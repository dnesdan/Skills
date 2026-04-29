# Store Frame Planning

Use this reference when creating the screenshot story, headline sequence, capture requirements, or localization plan before image generation.

## Inputs To Gather

Collect or infer:

- App name and one-sentence value proposition.
- Target store: App Store, Google Play, or both.
- Target country and primary locale.
- Platforms: iPhone, iPad, Android phone, Android tablet.
- Screenshot count per platform.
- Existing metadata, target keywords, competitor notes, and product positioning when provided by the user.
- Raw screenshot paths, device classes, locales, orientation, and appearance.
- Visual preferences, brand colors, app icon, existing framed screenshots, and no-go styles.
- Layout policy: strict consistent placement by default, creative variation only when requested.

Ask at most three blocking questions before drafting. Good first questions:

1. Which platforms and device classes should be produced?
2. Should I use existing raw screenshots, capture new ones, or first create a plan?
3. What visual direction and layout consistency should the framed screenshots follow?

If the user asks for speed, use these defaults:

- English master set first.
- Strict consistent placement within each platform/device/locale set.
- 10 App Store frames when possible; up to 8 Google Play screenshots.
- Benefit-led headlines.
- One device per frame unless comparing states or platforms.
- Bright but brand-compatible background.

## Sequencing

Make the first three screenshots carry the conversion story:

- Frame 1: strongest outcome, category promise, or clearest gameplay/app hook.
- Frame 2: core loop or main differentiator.
- Frame 3: retention hook, personalization, daily habit, progress, social proof, or premium value if truthful.

Frames 4-10 can cover:

- Secondary modes or tools.
- Personalization.
- Progress, history, stats, streaks, levels, or achievements.
- Ease of use.
- Offline/privacy/accessibility benefits.
- Widgets, watch, tablet, or cross-device features.
- Premium value only when visible in UI or supported by metadata.

Avoid:

- Repeating the same promise with different words.
- Leading with settings screens unless customization is the product hook.
- Explaining gestures instead of benefits.
- Keyword stuffing.
- Claims that are not visible or supportable.
- Tiny UI in a huge decorative wrapper.

## Headline Rules

Write overlay text as store-facing marketing copy:

- Keep headlines short: ideally 2-6 words.
- Make one promise per frame.
- Prefer benefits over feature labels.
- Use target keywords naturally only when they improve clarity.
- Keep punctuation simple.
- Avoid unverifiable claims like "best", "#1", or "guaranteed" unless substantiated.
- Avoid call-to-action copy such as "Download now", "Install now", or "Play now".
- Avoid price or promotion language unless the user explicitly confirms it is allowed for the target store.
- Avoid platform names in visible copy unless the screenshot is specifically about platform support.

Good patterns:

- "Solve One Puzzle Daily"
- "Track Every Win"
- "Choose Your Challenge"
- "Play Without Distraction"
- "Built For Bigger Screens"

Weaker patterns:

- "Settings"
- "Daily Screen"
- "Our App Is The Best"
- "Tap To Start"
- "Amazing Features"

## Frame Plan Template

Use this table before generation:

```markdown
| # | Store role | Headline | Raw screen needed | Platform variants | Layout notes |
|---|------------|----------|-------------------|-------------------|--------------|
| 1 | Primary promise | ... | Home/gameplay/result | iPhone, Android | Same layout lock as set |
| 2 | Core loop | ... | Active use state | iPhone, Android | Same device anchor |
| 3 | Retention hook | ... | Daily/progress/streak | iPhone, Android, iPad | Localize headline |
```

For each row, include:

- Exact headline text.
- Optional micro-caption only if the visual direction allows it and store policy allows it.
- Raw screenshot filename or capture instructions.
- Device class and orientation.
- Platform-specific copy differences.
- Any exception to the layout lock.

## Raw Capture List Template

```markdown
| Frame | Locale | Platform | Device class | App state | Required UI/data | Capture notes |
|-------|--------|----------|--------------|-----------|------------------|---------------|
| 01 | en-US | iOS | iPhone 6.9 portrait | Main gameplay | Clean in-progress puzzle | No debug overlays |
```

Raw screenshot requirements:

- Use the real app.
- Use realistic seeded data.
- Hide debug panels, simulator chrome, local-only controls, notifications, and unstable timestamps where possible.
- Capture each locale natively when possible.
- Keep the UI readable after device framing.
- Use tablet-specific UI for iPad/tablet screenshots when the app has it.

## Layout Lock Template

Define this once per set:

```markdown
| Property | Value |
|----------|-------|
| Canvas | 1290x2796 portrait |
| Device | realistic iPhone frame with Dynamic Island |
| Device placement | centered, x=50%, top begins near 28% of canvas |
| Device scale | screen fills about 72-78% of canvas height |
| Headline zone | top 14-24%, centered, max two lines |
| Background | warm off-white with subtle brand-color accents |
| Variation allowed | accent colors only; device position locked |
```

If imagegen cannot honor exact pixel coordinates, describe the layout lock in relative terms and verify visually after every frame.

## Campaign Bible Template

Use this when planning more than one framed screenshot:

```markdown
| Property | Value |
|----------|-------|
| Platform mode | iOS iPhone / iPad / Android phone / Android tablet / mixed |
| Device presentation | Frame style, aspect ratio, shadow, scale, and anchor |
| Visual system | Palette, background material, accent language, and texture level |
| Typography mood | Headline weight, alignment, line count, and text-safe region |
| Composition rhythm | Strictly consistent / 2-template campaign / creative variation |
| No-go patterns | Warped hardware, unreadable UI, generic gradients, clutter, fake claims |
```

Keep the campaign bible short enough to paste into every imagegen prompt. It should make the set feel like one campaign, not a folder of unrelated mockups.

## Localization Workflow

Default to English first:

1. Draft English frame plan.
2. Generate or approve English framed screenshots.
3. Translate headlines and micro-copy.
4. Check text expansion and cultural fit.
5. Capture localized raw screenshots.
6. Regenerate localized framed outputs using the same layout lock.

Do not edit localized text inside raw screenshots with imagegen unless the user explicitly requests a rough concept. Final localized store assets should use localized app UI captures.
