#!/usr/bin/env python3
"""Export iOS Simulator recordings to App Store preview MP4s.

The script converts a native portrait Simulator recording to 1080x1920 H.264,
optionally overlays tap indicators from an event log, and optionally mixes
bundled app sound effects into an AAC track.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


def run(cmd: list[str | Path]) -> None:
    printable = " ".join(str(part) for part in cmd)
    print(f"$ {printable}", file=sys.stderr)
    subprocess.run([str(part) for part in cmd], check=True)


def ffprobe_dimensions(path: Path) -> tuple[int, int]:
    output = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width,height",
            "-of",
            "csv=p=0:s=x",
            str(path),
        ],
        text=True,
    ).strip()
    width, height = output.split("x")
    return int(width), int(height)


def load_json(path: Path | None) -> list[dict[str, Any]]:
    if path is None:
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a JSON list")
    return data


def event_float(event: dict[str, Any], key: str) -> float:
    value = event.get(key)
    if not isinstance(value, (int, float)):
        raise ValueError(f"event is missing numeric {key}: {event}")
    return float(value)


def output_xy(
    event: dict[str, Any],
    source_width: int,
    source_height: int,
    output_width: int,
    output_height: int,
    point_scale: float,
) -> tuple[float, float]:
    scale = output_width / source_width
    crop_y = ((source_height * scale) - output_height) / 2
    return event_float(event, "x") * point_scale * scale, event_float(event, "y") * point_scale * scale - crop_y


def touch_filters(
    events: list[dict[str, Any]],
    source_width: int,
    source_height: int,
    output_width: int,
    output_height: int,
    point_scale: float,
) -> list[str]:
    filters: list[str] = []
    for index, event in enumerate(events):
        t = event_float(event, "t")
        x, y = output_xy(event, source_width, source_height, output_width, output_height, point_scale)
        size = 50 if index == 0 else 58
        x0 = max(0, x - size / 2)
        y0 = max(0, y - size / 2)
        enable = f"between(t,{max(0, t - 0.05):.3f},{t + 0.45:.3f})"
        filters.append(
            f"drawbox=x={x0:.1f}:y={y0:.1f}:w={size}:h={size}:"
            f"color=white@0.22:t=fill:enable='{enable}'"
        )
        filters.append(
            f"drawbox=x={x0:.1f}:y={y0:.1f}:w={size}:h={size}:"
            f"color=0x7C3AED@0.88:t=5:enable='{enable}'"
        )
    return filters


def render_video(
    input_path: Path,
    output_path: Path,
    events: list[dict[str, Any]],
    args: argparse.Namespace,
    touch_overlay: bool,
) -> None:
    source_width, source_height = ffprobe_dimensions(input_path)
    filters = [
        f"fps={args.fps}",
        f"scale={args.width}:-2",
        f"crop={args.width}:{args.height}:(iw-{args.width})/2:(ih-{args.height})/2",
        "setsar=1",
    ]
    if touch_overlay:
        filters.extend(
            touch_filters(
                events,
                source_width,
                source_height,
                args.width,
                args.height,
                args.point_scale,
            )
        )

    run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "warning",
            "-i",
            input_path,
            "-t",
            f"{args.duration:.3f}",
            "-vf",
            ",".join(filters),
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            args.preset,
            "-crf",
            str(args.crf),
            "-pix_fmt",
            "yuv420p",
            "-movflags",
            "+faststart",
            output_path,
        ]
    )


def derive_audio_events(
    mode: str,
    events: list[dict[str, Any]],
    victory_delay: float,
    tap_sound: str,
    action_sound: str,
    palette_sound: str,
    victory_sound: str,
) -> list[dict[str, Any]]:
    if mode == "none" or not events:
        return []

    audio: list[dict[str, Any]] = []
    for index, event in enumerate(events):
        if mode == "tap":
            sound = tap_sound
            volume = 0.32
        elif mode == "action":
            sound = tap_sound if index == 0 else action_sound
            volume = 0.32 if index == 0 else 0.68
        elif mode == "alternating":
            sound = tap_sound if index == 0 or index % 2 == 0 else action_sound
            volume = 0.32 if sound == tap_sound else 0.68
        elif mode == "palette":
            label = str(event.get("label", "")).lower()
            is_palette_event = any(token in label for token in ("palette", "theme", "color", "colour"))
            sound = palette_sound if is_palette_event else tap_sound
            volume = 0.62 if is_palette_event else 0.32
        else:
            raise ValueError(f"unsupported --derive-audio value: {mode}")

        audio.append({"t": event_float(event, "t"), "sound": sound, "volume": volume})

    audio.append(
        {
            "t": min(14.0, event_float(events[-1], "t") + victory_delay),
            "sound": victory_sound,
            "volume": 0.86,
        }
    )
    return audio


def add_audio(
    video_path: Path,
    output_path: Path,
    audio_events: list[dict[str, Any]],
    sound_dir: Path | None,
    duration: float,
) -> None:
    if not audio_events:
        shutil.copy2(video_path, output_path)
        return
    if sound_dir is None:
        raise ValueError("--sound-dir is required when audio events are provided")

    cmd: list[str | Path] = [
        "ffmpeg",
        "-y",
        "-v",
        "warning",
        "-i",
        video_path,
        "-f",
        "lavfi",
        "-t",
        f"{duration:.3f}",
        "-i",
        "anullsrc=channel_layout=stereo:sample_rate=48000",
    ]

    for event in audio_events:
        sound = event.get("sound")
        if not isinstance(sound, str):
            raise ValueError(f"audio event is missing sound name: {event}")
        sound_path = sound_dir / f"{sound}.mp3"
        if not sound_path.exists():
            raise FileNotFoundError(sound_path)
        cmd.extend(["-i", sound_path])

    filters = [f"[1:a]atrim=0:{duration:.3f},asetpts=N/SR/TB[sil]"]
    labels = ["[sil]"]
    for input_index, event in enumerate(audio_events, start=2):
        t = event_float(event, "t")
        volume = float(event.get("volume", 1.0))
        delay_ms = max(0, int(round(t * 1000)))
        filters.append(
            f"[{input_index}:a]aresample=48000,aformat=channel_layouts=stereo,"
            f"adelay={delay_ms}:all=1,volume={volume}[a{input_index}]"
        )
        labels.append(f"[a{input_index}]")
    filters.append(
        f"{''.join(labels)}amix=inputs={len(labels)}:duration=longest:"
        f"dropout_transition=0,atrim=0:{duration:.3f},asetpts=N/SR/TB[a]"
    )

    cmd.extend(
        [
            "-filter_complex",
            ";".join(filters),
            "-map",
            "0:v:0",
            "-map",
            "[a]",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-t",
            f"{duration:.3f}",
            "-movflags",
            "+faststart",
            output_path,
        ]
    )
    run(cmd)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Raw native Simulator recording")
    parser.add_argument("--output", required=True, type=Path, help="Clean exported App Store MP4")
    parser.add_argument("--touch-output", type=Path, help="Optional touch-overlay exported MP4")
    parser.add_argument("--events", type=Path, help="JSON event log with t, x, y, label")
    parser.add_argument("--audio-events", type=Path, help="JSON list with t, sound, volume")
    parser.add_argument("--sound-dir", type=Path, help="Directory containing sound-name.mp3 files")
    parser.add_argument("--derive-audio", choices=["none", "tap", "action", "alternating", "palette"], default="none")
    parser.add_argument("--tap-sound", default="tap", help="Sound filename stem for ordinary taps")
    parser.add_argument("--action-sound", default="place", help="Sound filename stem for generic game actions")
    parser.add_argument("--palette-sound", default="place", help="Sound filename stem for palette/theme/color events")
    parser.add_argument("--victory-sound", default="victory", help="Sound filename stem for the final success sound")
    parser.add_argument("--victory-delay", type=float, default=0.75)
    parser.add_argument("--duration", type=float, default=15.0)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1920)
    parser.add_argument("--point-scale", type=float, default=3.0, help="Simulator pixels per event-log point")
    parser.add_argument("--crf", type=int, default=18)
    parser.add_argument("--preset", default="veryfast")
    parser.add_argument("--keep-temp", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    events = load_json(args.events)
    audio_events = load_json(args.audio_events)
    if not audio_events:
        audio_events = derive_audio_events(
            args.derive_audio,
            events,
            args.victory_delay,
            args.tap_sound,
            args.action_sound,
            args.palette_sound,
            args.victory_sound,
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.touch_output is not None:
        args.touch_output.parent.mkdir(parents=True, exist_ok=True)

    temp_context = tempfile.TemporaryDirectory(prefix="ios-app-preview-")
    temp_dir = Path(temp_context.name)
    try:
        clean_silent = temp_dir / "clean-silent.mp4"
        render_video(args.input, clean_silent, events, args, touch_overlay=False)
        add_audio(clean_silent, args.output, audio_events, args.sound_dir, args.duration)

        if args.touch_output is not None:
            touch_silent = temp_dir / "touch-silent.mp4"
            render_video(args.input, touch_silent, events, args, touch_overlay=True)
            add_audio(touch_silent, args.touch_output, audio_events, args.sound_dir, args.duration)
    finally:
        if args.keep_temp:
            print(f"kept temporary files at {temp_dir}", file=sys.stderr)
        else:
            temp_context.cleanup()


if __name__ == "__main__":
    main()
