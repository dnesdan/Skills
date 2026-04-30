---
name: ios-app-preview-videos
description: Capture, regenerate, export, and validate iOS App Store preview videos from Simulator, especially 15-second gameplay or product marketing captures with release builds, normal navigation, staged in-progress states, touch overlays, and app sound effects. Use when asked to make App Store videos, preview videos, gameplay recordings, simulator marketing captures, or regenerate iOS app preview videos.
---

# iOS App Preview Videos

## Overview

Produce truthful 15-second iOS preview videos from real Simulator captures. The usual output is a pair of
App Store-ready MP4s: a clean version and a touch-overlay version.

Default output location:

```text
local_screenshots/app-preview/<app>/<app>-release-fresh-win-clean-appstore-1080x1920.mp4
local_screenshots/app-preview/<app>/<app>-release-fresh-win-touch-appstore-1080x1920.mp4
```

## Non-Negotiables

- Use a Release build unless the user explicitly asks for Debug. Debug-only UI can leak into dialogs.
- Start from normal app navigation, not a raw board-only view. Include the welcome/menu and the in-game navigation bar.
- Keep welcome/menu time short, usually under 2 seconds, unless the user asks otherwise.
- Stage a fresh or freshly in-progress puzzle. Avoid stale timers, old progress, or already-solved states.
- Prefer 3-4 remaining actions before the win, then hold the win dialog for about 2 seconds.
- Final App Store preview files should be 15.0 seconds, 1080x1920 portrait, H.264, 30 fps, AAC audio.
- Keep generated captures under `local_screenshots/` or another local output folder. Do not commit raw videos.
- Validate every final video with `ffprobe` and contact sheets before reporting success.
- Keep this skill generic. Use placeholders such as `<app>`, `<Scheme>`, and `<bundle id>` in examples and
  instructions; do not bake project-specific game names, bundle IDs, puzzle moves, or marketing copy into the skill.

## Workflow

1. Gather capture settings:
   - App/scheme name, bundle ID, simulator UDID/device, locale, and output directory.
   - Whether the user wants clean, touch overlay, or both.
   - Desired scene: fresh game, in-progress game, number of moves, win dialog, and pacing.

2. Build and install a Release app:

   ```bash
   xcodebuild build \
     -workspace Games.xcworkspace \
     -scheme <Scheme> \
     -configuration Release \
     -destination 'platform=iOS Simulator,name=<Device>'
   xcrun simctl install <UDID> <path-to-built-app.app>
   ```

   If a Build iOS Apps tool profile is available, use it, but still verify the configuration is Release.

3. Stage the scene:
   - Terminate the app before editing app data.
   - Reset database rows, user defaults, saved state, or app-specific capture flags.
   - If the app restores directly into a game and the user wants normal navigation, tap back to the menu before recording.
   - Wait 1-2 seconds after opening the game screen before the first game action; early taps can land during transitions.

4. Record raw video and event timing:
   - Prefer `axe record-video --fps 30` for fixed-frame Simulator captures.
   - Use `xcrun simctl io ... recordVideo` only when static holds are not important; it can behave like variable-frame capture.
   - Start recording only when the intended first frame is visible.
   - Use `axe tap` for interactions and write an event log as JSON:

   ```json
   [
     {"t": 0.95, "x": 201.0, "y": 411.0, "label": "Easy menu"},
     {"t": 3.52, "x": 200.2, "y": 428.8, "label": "game action 2,2"}
   ]
   ```

5. Export final videos:
   - Use `scripts/export_app_preview.py` for simple raw-to-App-Store exports, optional touch overlays, and audio mixing.
   - For app sounds, prefer the app's bundled effects over fake system beeps.
   - If live system audio capture is unavailable, mix sounds from the app assets at event times.
   - Verify the exported file has an audio stream, and inspect the contact sheet with sound-event timing in mind
     so taps, gameplay actions, and final celebration sounds land on the visible moments.

6. Validate:

   ```bash
   ffprobe -v error \
     -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,duration,sample_rate,channels \
     -of compact=p=0:nk=1 <video.mp4>

   ffmpeg -y -v error -i <video.mp4> \
     -vf "fps=1/3,scale=216:-2,format=yuvj420p,tile=5x1" \
     -frames:v 1 /tmp/<app>-preview-sheet.jpg
   ```

   Inspect the first frame, middle gameplay, final dialog, touch visibility, audio stream, and lack of debug UI.

## Export Helper

Use the bundled script for the common case where one raw native capture should become clean and touch App Store
exports:

```bash
python3 <skill>/scripts/export_app_preview.py \
  --input local_screenshots/app-preview/<app>/<app>-release-fresh-win-raw-native.mp4 \
  --events local_screenshots/app-preview/<app>/<app>-release-fresh-win-events.json \
  --output local_screenshots/app-preview/<app>/<app>-release-fresh-win-clean-appstore-1080x1920.mp4 \
  --touch-output local_screenshots/app-preview/<app>/<app>-release-fresh-win-touch-appstore-1080x1920.mp4 \
  --sound-dir <path-to-app-sounds> \
  --derive-audio alternating
```

When automatic sound derivation is too rough, pass an explicit audio plan:

```json
[
  {"t": 0.95, "sound": "tap", "volume": 0.32},
  {"t": 3.52, "sound": "line", "volume": 0.68},
  {"t": 10.24, "sound": "victory", "volume": 0.86}
]
```

Then run with `--audio-events audio-plan.json --sound-dir <Sounds>`.

Generic `--derive-audio` modes:

- `tap`: every recorded event uses `tap.mp3`, then a final `victory.mp3`.
- `action`: the first event uses `tap.mp3`; later events use the configurable action sound, then `victory.mp3`.
- `alternating`: the first event uses `tap.mp3`; later events alternate action and tap sounds, then `victory.mp3`.
- `palette`: event labels containing `palette`, `theme`, `color`, or `colour` use the configurable palette sound; other events use `tap.mp3`, then `victory.mp3`.

Use `--tap-sound`, `--action-sound`, `--palette-sound`, and `--victory-sound` when the app's bundled sound filenames differ.

## Response Shape

For planning, return the capture scene, build target, simulator, staging approach, output names, and validation plan.

For completed work, return the final video paths, whether they are clean or touch-overlay variants, and the validation
facts: duration, resolution, fps, audio presence, and any known caveats.
