# Imagegen Framing Prompts

Use this reference when turning raw screenshots into framed store assets with internal imagegen.

## Imagegen Mode

Use the internal imagegen skill/tool path by default.

For existing raw screenshots:

- Treat each raw screenshot as an edit target.
- Inspect/load each local raw image first so it is visible in context.
- Preserve the raw app UI exactly.
- Change only the wrapper: store canvas, device frame, background, headline, and approved accents.

For a new visual direction:

- Generate one style frame first.
- Confirm headline text, layout lock, raw UI preservation, and output dimensions.
- Apply the same prompt structure to the remaining frames.

Use one generation per distinct final frame. Never ask imagegen to generate a complete 10-frame set as one combined image.

## Campaign Bible Prompt Block

For multi-frame sets, write this block once and reuse it in every prompt:

```text
Campaign bible:
- Platform mode: <iOS / Android / tablet / mixed>
- Device presentation: <hardware style>, physically correct aspect ratio, consistent frame, consistent scale, controlled shadow.
- Visual system: <palette>, <background material>, <accent language>, <typography mood>, <headline treatment>.
- Composition rules: same canvas, same headline zone, same device anchor, same safe margins, same overall hierarchy.
- Content rules: preserve the raw app UI exactly, keep the device screen readable, use only the approved headline, add no extra store badges or claims.
```

Do not let later frames drift into a different visual system. Variation is allowed only in the raw screenshot, headline text, and subtle approved accents.

## Strict Layout-Lock Prompt Template

```text
Use case: store marketing screenshot
Asset type: framed app screenshot
Platform/device: <App Store iPhone 6.9 / App Store iPad 13 / Google Play Android phone / Google Play Android tablet>
Final canvas: <width>x<height> px, <portrait/landscape>. Generate at this exact final size if possible.

Input image:
- Image 1 is the raw app screenshot.
- Preserve Image 1 pixel-faithfully inside the device screen.
- Do not alter in-app text, icons, colors, board state, data, status bar, or navigation.

Layout lock:
- Campaign bible: <paste the approved campaign bible for this set>.
- Use the same device placement as the rest of the set.
- Device frame: <realistic iPhone/iPad/Android phone/tablet frame>.
- Device aspect ratio: keep the hardware and visible screen geometry faithful to <device class>. Do not stretch, squash, widen, narrow, or cosmetically distort the phone/tablet; preserve Image 1's aspect ratio inside the device screen.
- Device position: <centered/lower anchored; relative top and height>.
- Device scale: <screen fills about N% of canvas height/width>.
- Headline zone: <top band, centered/left aligned, max lines>.
- Background system: <brand background and accent style>.
- Only decorative accents may vary subtly between frames.

Text outside device:
- Exact headline: "<headline>"
- No subtitle unless explicitly specified.
- Do not add any extra words.

Style:
- Premium app store marketing image, clean raster mockup, high-resolution.
- Strong first-glance hierarchy, safe margins, readable UI.

Avoid:
- Fake UI, fake ratings, badges, awards, prices, promotional claims, calls to action, watermarks, wrong hardware, warped devices, clutter, tiny text, cropped headline, changing device placement.
```

## Creative Variation Template

Use only when the user requests a more creative campaign:

```text
Use the approved visual system, but use layout template <A/B/C>:
- Template A: <device anchor, headline zone>
- Template B: <device anchor, headline zone>
- Template C: <device anchor, headline zone>
Keep all templates within the same typography, background, device-frame, and safe-margin system.
```

## Existing Framed Screenshot Restyle

When an existing framed set is the style reference:

```text
Use case: style-transfer
Asset type: regenerated framed store screenshot
Primary request: Recreate the approved screenshot style using the new raw screenshot and updated headline.
Input images: Image 1 is the new raw screenshot and edit target. Image 2 is the style reference only.
Layout: Preserve the same device placement, scale, headline zone, background system, and typography mood as Image 2.
Constraints: Preserve Image 1's UI exactly. Borrow only layout, background style, device framing, typography mood, and visual polish from Image 2. Do not copy old text or old app UI.
Text outside device: "<new headline>"
```

## Localization Prompt

```text
Use case: localized framed store screenshot
Primary request: Generate the <locale> version of the approved English framed screenshot.
Input images: Image 1 is the localized raw app screenshot and must remain pixel-faithful. Image 2 is the approved English framed screenshot style reference.
Layout: Keep the approved layout lock unless the localized headline would be truncated; if adjusted, keep device placement unchanged and rebalance only headline line breaks/size.
Text outside device: "<localized headline>"
Constraints: Preserve Image 1's app UI exactly. Replace only the marketing headline outside the device screen. Ensure localized text is readable and not truncated.
```

## Visual Direction Presets

Minimal premium:

- White or light neutral background.
- Subtle depth and clean shadow.
- One strong headline.
- Few decorative elements.

Bold colorful:

- Brand-color background with high contrast.
- Large headline and energetic geometry.
- Keep the device screen dominant.

Playful game-like:

- App/game-inspired background texture or soft shapes.
- Brighter palette.
- Optional thematic props that do not compete with the UI.

Dark high-contrast:

- Deep background with controlled highlights.
- Bright headline.
- Strong screen glow without obscuring UI.

Editorial:

- Soft real-world desk or hand-held context only when truthful and compatible with store guidelines.
- Avoid making the actual UI too small.

## Device Framing Rules

Aspect ratio discipline:

- Keep the visible hardware and screen proportions faithful to the selected device class.
- Preserve the raw screenshot aspect ratio inside the device screen; do not crop, stretch, squash, or pad it in a way that makes the UI look like a different phone/tablet shape.
- If the raw screenshot ratio does not match the requested device frame, pause and flag the mismatch before generating or use a matching device slot/frame.
- Reject outputs where the phone looks too narrow, too wide, too tall, stubby, warped, or inconsistent with the set.

iOS:

- Use iPhone frames for iPhone outputs and iPad frames for iPad outputs.
- Use realistic bezels, rounded corners, camera cutouts, and screen curvature.
- Do not place Android navigation controls on iOS screenshots.

Android:

- Use Android phone or tablet frames.
- Avoid iPhone notches, Dynamic Island, Apple-only hardware cues, or Apple-style home indicators.
- Keep the app UI within the Android screen area.

Tablet:

- Use a tablet frame and tablet-appropriate composition.
- Do not scale a phone mockup into an iPad/tablet canvas.

## Text Reliability

Imagegen may make mistakes in rendered text. Improve reliability by:

- Keeping headline copy short.
- Quoting exact text.
- Avoiding tiny micro-copy.
- Asking for one headline region with generous padding.
- Validating every generated output visually.

If exact text still fails after targeted iteration, keep the imagegen background/device art and add text with a deterministic editor or project screenshot tooling when available.

## Regeneration Rules

Regenerate or choose a different frame path when:

- The raw app UI is edited, redrawn, translated, blurred, or cropped incorrectly.
- The phone/tablet aspect ratio is visibly wrong or inconsistent with the set.
- The device frame uses the wrong platform cues.
- The output adds unapproved text, fake badges, ratings, prices, CTAs, or watermarks.
- The layout lock drifts: device anchor, device scale, headline zone, typography, or background system changes unexpectedly.
- The image looks generic, cluttered, or imagegen-made in a way that weakens store conversion.

## Validation Checklist

Check every final image:

- Correct platform frame.
- Correct raw screenshot and locale.
- Raw UI has not changed.
- Headline text is exact.
- Text is readable at store thumbnail scale.
- No hallucinated badges, prices, ratings, claims, CTAs, or UI.
- No device-screen cropping mistakes.
- Device and screen aspect ratio look physically correct for the selected device class.
- Device placement and scale match the set's layout lock.
- First three screenshots form a clear conversion story.
- Output file is saved in the requested workspace location.
- Pixel dimensions match the selected store slot.
