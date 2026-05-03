---
title: video-understand
url: https://skills.sh/heygen-com/skills/video-understand
---

# video-understand

skills/heygen-com/skills/video-understand
video-understand
Installation
$ npx skills add https://github.com/heygen-com/skills --skill video-understand
SKILL.md
video-understand

Understand video content locally using ffmpeg for frame extraction and Whisper for transcription. Fully offline, no API keys required.

Prerequisites
ffmpeg + ffprobe (required): brew install ffmpeg
openai-whisper (optional, for transcription): pip install openai-whisper
Commands
# Scene detection + transcribe (default)
python3 skills/video-understand/scripts/understand_video.py video.mp4

# Keyframe extraction
python3 skills/video-understand/scripts/understand_video.py video.mp4 -m keyframe

# Regular interval extraction
python3 skills/video-understand/scripts/understand_video.py video.mp4 -m interval

# Limit frames extracted
python3 skills/video-understand/scripts/understand_video.py video.mp4 --max-frames 10

# Use a larger Whisper model
python3 skills/video-understand/scripts/understand_video.py video.mp4 --whisper-model small

# Frames only, skip transcription
python3 skills/video-understand/scripts/understand_video.py video.mp4 --no-transcribe

# Quiet mode (JSON only, no progress)
python3 skills/video-understand/scripts/understand_video.py video.mp4 -q

# Output to file
python3 skills/video-understand/scripts/understand_video.py video.mp4 -o result.json

CLI Options
Flag	Description
video	Input video file (positional, required)
-m, --mode	Extraction mode: scene (default), keyframe, interval
--max-frames	Maximum frames to keep (default: 20)
--whisper-model	Whisper model size: tiny, base, small, medium, large (default: base)
--no-transcribe	Skip audio transcription, extract frames only
-o, --output	Write result JSON to file instead of stdout
-q, --quiet	Suppress progress messages, output only JSON
Extraction Modes
Mode	How it works	Best for
scene	Detects scene changes via ffmpeg select='gt(scene,0.3)'	Most videos, varied content
keyframe	Extracts I-frames (codec keyframes)	Encoded video with natural keyframe placement
interval	Evenly spaced frames based on duration and max-frames	Fixed sampling, predictable output

If scene mode detects no scene changes, it automatically falls back to interval mode.

Output

The script outputs JSON to stdout (or file with -o). See references/output-format.md for the full schema.

{
  "video": "video.mp4",
  "duration": 18.076,
  "resolution": {"width": 1224, "height": 1080},
  "mode": "scene",
  "frames": [
    {"path": "/abs/path/frame_0001.jpg", "timestamp": 0.0, "timestamp_formatted": "00:00"}
  ],
  "frame_count": 12,
  "transcript": [
    {"start": 0.0, "end": 2.5, "text": "Hello and welcome..."}
  ],
  "text": "Full transcript...",
  "note": "Use the Read tool to view frame images for visual understanding."
}


Use the Read tool on frame image paths to visually inspect extracted frames.

References
references/output-format.md -- Full JSON output schema documentation
Weekly Installs
1.1K
Repository
heygen-com/skills
GitHub Stars
202
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass