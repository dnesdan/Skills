# Light-Up Game Capture Notes

Use these notes when capturing preview videos in `/Users/dan/AI_Stuff/light-up-game` or another app that shares the
same puzzle shell patterns.

## Release Builds

- Build Release for MiniHue, Hue, Slant, Hashi, Akari Glow, and similar preview captures unless the user asks for Debug.
- Debug builds can show share/debug-only controls in completion dialogs.
- Reconfirm the installed bundle is the Release artifact when the visual output looks different from App Store UI.

## Output Layout

Prefer:

```text
local_screenshots/app-preview/<app>/<app>-release-fresh-win-raw-native.mp4
local_screenshots/app-preview/<app>/<app>-release-fresh-win-events.json
local_screenshots/app-preview/<app>/<app>-release-fresh-win-clean-appstore-1080x1920.mp4
local_screenshots/app-preview/<app>/<app>-release-fresh-win-touch-appstore-1080x1920.mp4
```

## Staging CoreData Puzzle State

- Terminate the app before touching SQLite.
- Check and clear locks with `lsof <PuzzleDatabase.sqlite>` if writes fail.
- Reset stale completion data:

```sql
UPDATE ZPUZZLE
SET ZHINTSUSED = 0,
    ZTIMESPENT = 0,
    ZCOMPLETEDAT = NULL,
    ZREDOHISTORYJSON = '[]',
    ZLASTPLAYEDAT = <apple-reference-date>
WHERE Z_PK = <target-row>;
```

- Set `ZSTATE = 'inProgress'` when the staged board already includes progress that must survive loading.
- Set `ZSTATEHISTORYJSON` to a JSON array containing the staged serialized state when the view model restores history.
- Use `notPlayed` only for truly fresh boards.

Hashi-specific: Hashi strips bridges from `puzzleString` when `ZSTATE` is `notPlayed`. Use `inProgress` for staged
boards with prefilled bridges, otherwise the first visible board may be reset and later taps will not solve the puzzle.

## Navigation and Timing

- Start recording with the welcome/menu visible if the user asks for normal navigation.
- If the app restores straight into a game, tap the back button before starting the final recording.
- Keep the welcome/menu under about 2 seconds, then enter the game.
- Wait about 2 seconds after opening a game board before the first game tap if transitions or lazy layout are involved.
- Keep moves slower than normal automation. Marketing captures should be understandable, not just fast.
- Leave about 2 seconds for the win dialog at the end.

## Recording Tool Choice

Prefer:

```bash
axe record-video --udid <UDID> --fps 30 --output <raw-native.mp4>
```

Use `axe tap` for actions and record event times with `time.monotonic()`.

Avoid relying on `xcrun simctl io <UDID> recordVideo` for final pacing. It has no audio capture and can produce
surprising timing around static holds, which may make end dialogs too short or include unintended app transitions.

## Sound Mixing

`simctl io recordVideo` does not capture app audio, and many local Macs have no loopback input. When live audio is not
available, mix the app's bundled effects from:

```text
SharedGameUI/Sources/SharedGameUI/Resources/Sounds/
```

Useful mappings:

- Hue: menu/cell taps use `tap.mp3`, palette placements use `place.mp3`, finish uses `victory.mp3`.
- Slant: moves use `line.mp3`, finish uses `victory.mp3`.
- Hashi: island selection uses `tap.mp3`, bridge placement uses `bridge.mp3`, finish uses `victory.mp3`.

Use `scripts/export_app_preview.py --derive-audio hue|slant|hashi` for these default mappings.

## Review Checklist

- First frame shows the intended app, not the previous app, Home screen, or a blank launch frame.
- Welcome/menu is short and normal navigation into the game is visible.
- The navigation bar remains visible in the game.
- First tap reacts.
- Timer is fresh, usually under 20 seconds by completion.
- Touch overlay is visible but not obstructive.
- The win dialog is visible and readable for the final hold.
- `ffprobe` reports H.264 video, 1080x1920, 30 fps, 15.0 seconds, AAC audio.
