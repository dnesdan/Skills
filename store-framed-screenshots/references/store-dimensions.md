# Store Dimensions

Use this reference to pick output slots before prompting imagegen. Store specs change; for final submission, verify the current official App Store Connect or Play Console requirements when exact compliance matters.

## App Store Screenshot Slots

Apple accepts 1-10 screenshots per localization and device display. Current common portrait slots:

| Device slot | Portrait sizes |
|-------------|----------------|
| iPhone 6.9" | 1260x2736, 1290x2796, 1320x2868 |
| iPhone 6.5" | 1242x2688, 1284x2778 |
| iPhone 6.3" | 1179x2556, 1206x2622 |
| iPhone 6.1" | 1080x2340, 1125x2436, 1170x2532 |
| iPad 13" | 2048x2732, 2064x2752 |
| iPad 12.9" | 2048x2732 |
| iPad 11" | 1488x2266, 1640x2360, 1668x2388, 1668x2420 |

Landscape sizes are the same pairs reversed.

Practical defaults:

- Use the raw simulator screenshot size when it is an accepted App Store size.
- For iPhone 6.9, prefer the exact size captured from the simulator/device in use: `1290x2796` for iPhone 15 Pro Max/Plus-class captures, `1320x2868` for iPhone 16/17 Pro Max-class captures, or `1260x2736` for iPhone Air-class captures.
- For iPad, prefer `2064x2752` or `2048x2732` portrait depending on the simulator raw output.
- Do not upscale a small image unless imagegen or another deterministic export path cannot produce final dimensions directly; disclose any upscaling.

## Google Play Screenshot Slots

Google Play accepts screenshots per supported device type within flexible constraints:

- JPEG or 24-bit PNG with no alpha.
- Minimum dimension: 320 px.
- Maximum dimension: 3840 px.
- Maximum side cannot be more than twice the minimum side.
- Up to 8 screenshots per supported device type.
- Phones and tablets should use real app/game experience.

Practical defaults:

| Device type | Recommended portrait | Recommended landscape |
|-------------|----------------------|-----------------------|
| Android phone | 1080x1920 | 1920x1080 |
| 7" tablet | 1200x1920 | 1920x1200 |
| 10" tablet | 1600x2560 | 2560x1600 |
| Feature graphic | 1024x500 | n/a |

Large-screen Play guidance:

- Tablet/Chromebook screenshots should be between 1080 and 7680 px and use 9:16 portrait or 16:9 landscape.
- For app recommendation eligibility, provide at least four screenshots at minimum 1080 px resolution.
- For games, provide at least three 16:9 landscape or three 9:16 portrait screenshots, minimum 1080 px resolution, showing actual gameplay.

Google Play text guidance:

- Use taglines only when needed; keep them visually small enough that the app experience remains primary.
- Avoid ranking, awards, price, promotion, testimonials, and CTAs.
- Avoid extra device imagery on surfaces where Google forbids it, such as Wear OS screenshots.
