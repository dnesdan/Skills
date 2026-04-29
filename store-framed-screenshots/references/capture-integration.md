# Capture Integration

Use this reference when raw screenshots do not already exist or when the user wants repeatable capture across locales, appearances, and device classes.

## Capture Principles

- Raw captures are source truth. Framed screenshots should wrap real app UI, not invent it.
- Capture raw screenshots before imagegen framing.
- Seed deterministic demo data when screens would otherwise look empty, random, or personally identifiable.
- Capture one raw screenshot per final frame and platform variant unless multiple frames intentionally share a raw screen.
- Store raw files beside framed outputs for traceability.

## iOS Raw Capture Options

Simple simulator capture:

1. Build and install the app on the requested simulator.
2. Seed premium/demo state using existing debug flags, launch arguments, StoreKit config, or app-specific test hooks.
3. Navigate manually or with simulator/UI automation.
4. Capture with `xcrun simctl io <device> screenshot <path>`.
5. Repeat for locale and appearance.

Deterministic in-app capture mode:

- Add DEBUG-only capture hooks when the project can safely support them.
- Build once, then relaunch per locale/appearance with launch arguments such as `-AppleLanguages (en)` and app-specific capture flags.
- Use a step coordinator where each step navigates, waits for animations, screenshots, and cleans up.
- Write PNGs to the app container or a known local folder, then copy them into the raw screenshot directory.
- Prefer this when generating many locales or many app states.

Useful iOS capture patterns:

- In-app capture mode instead of UI tests when the app needs direct access to ViewModels, seeded data, SwiftData, widgets, or `ImageRenderer`.
- Step-based captures named `01-home`, `02-gameplay`, `03-settings`.
- Isolated element renders for widgets/cards when those assets will be composited later, but keep final store screenshots truthful.
- Explicit light/dark relaunches rather than toggling appearance mid-capture.

## Android Raw Capture Options

- Build/install the requested app variant on an emulator or real device.
- Seed premium/demo state with existing debug flags, SharedPreferences, database seeders, test billing setup, or app-specific launch flags.
- Set locale and night mode before launch when capturing localized or dark screenshots.
- Capture with `adb exec-out screencap -p > <path>` or an existing project screenshot script.
- Use Android phone frames for phone screenshots and tablet frames for tablet screenshots.

## Raw QA

Reject or recapture raw screenshots when:

- The app is blank, loading, logged out unintentionally, or on the wrong screen.
- Debug banners, test controls, personal data, notification banners, or simulator overlays are visible.
- The same screen repeats without adding a new store message.
- The screenshot is too dense to remain readable inside a device frame.
- A tablet capture is just a stretched phone UI when the app has a better tablet layout.

## Folder Convention

```text
local_screenshots/store-framed/<app>/<locale>/<platform>/<device-class>/raw/
local_screenshots/store-framed/<app>/<locale>/<platform>/<device-class>/framed/
```

Keep capture scripts and temporary simulator artifacts out of committed app code unless the user explicitly asks for a reusable capture system.
