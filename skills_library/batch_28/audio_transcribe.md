---
title: audio-transcribe
url: https://skills.sh/maxgent-ai/maxgent-plugin/audio-transcribe
---

# audio-transcribe

skills/maxgent-ai/maxgent-plugin/audio-transcribe
audio-transcribe
Installation
$ npx skills add https://github.com/maxgent-ai/maxgent-plugin --skill audio-transcribe
SKILL.md
Audio Transcriber

Speech recognition using WhisperX with multi-language support and word-level timestamp alignment.

Prerequisites

Requires Python 3.12 (uv manages this automatically).

Usage

When the user wants to transcribe audio/video: $ARGUMENTS

Instructions
Step 1: Get input file

If the user has not provided an input file path, ask them to provide one.

Supported formats:

Audio: MP3, WAV, FLAC, M4A, OGG, etc.
Video: MP4, MKV, MOV, AVI, etc. (audio is extracted automatically)

Verify the file exists:

ls -la "$INPUT_FILE"

Step 2: Ask user for configuration

Warning: You MUST use AskUserQuestion to collect user preferences. Do not skip this step.

Use AskUserQuestion to collect the following:

Model size: Choose the recognition model

Options:
"base - Balanced speed and accuracy (Recommended)"
"tiny - Fastest, lower accuracy"
"small - Faster, moderate accuracy"
"medium - Slower, higher accuracy"
"large-v2 - Slowest, highest accuracy"

Language: What language is the audio?

Options:
"Auto-detect (Recommended)"
"Chinese (zh)"
"English (en)"
"Japanese (ja)"
"Other"

Word-level alignment: Do you need word-level timestamps?

Options:
"Yes - Precise timing for each word (Recommended)"
"No - Sentence-level timing only (faster)"

Output format: What format to output?

Options:
"TXT - Plain text with timestamps (Recommended)"
"SRT - Subtitle format"
"VTT - Web subtitle format"
"JSON - Structured data (with word-level info)"

Output path: Where to save?

Default: same directory as input file, named <original_name>.txt (or matching format)
Step 3: Run transcription script

Use the transcribe.py script in the skill directory:

uv run /path/to/skills/audio-transcribe/transcribe.py "INPUT_FILE" [OPTIONS]


Parameters:

--model, -m: Model size (tiny/base/small/medium/large-v2)
--language, -l: Language code (en/zh/ja/...), auto-detect if not specified
--no-align: Skip word-level alignment
--no-vad: Disable VAD filtering (use if transcription has time jumps or missing segments)
--output, -o: Output file path
--format, -f: Output format (srt/vtt/txt/json)

Examples:

# Basic transcription (auto-detect language)
uv run skills/audio-transcribe/transcribe.py "video.mp4" -o "video.txt"

# Chinese transcription, output SRT subtitles
uv run skills/audio-transcribe/transcribe.py "audio.mp3" -l zh -f srt -o "subtitles.srt"

# Fast transcription, skip word alignment
uv run skills/audio-transcribe/transcribe.py "audio.wav" --no-align -o "transcript.txt"

# Use a larger model, output JSON (with word-level timestamps)
uv run skills/audio-transcribe/transcribe.py "speech.mp3" -m medium -f json -o "result.json"

# Disable VAD filtering (fix time jumps / missing segments)
uv run skills/audio-transcribe/transcribe.py "audio.mp3" --no-vad -o "transcript.txt"

Step 4: Present results

After transcription completes:

Show the full output file path
Display a preview of the transcription content
Report total duration and segment count
Output format reference
TXT format
[00:00:00.000 - 00:00:03.500] This is the first sentence
[00:00:03.500 - 00:00:07.200] This is the second sentence

SRT format
1
00:00:00,000 --> 00:00:03,500
This is the first sentence

2
00:00:03,500 --> 00:00:07,200
This is the second sentence

JSON format (with word-level)
[
  {
    "start": 0.0,
    "end": 3.5,
    "text": "This is the first sentence",
    "words": [
      {"word": "This", "start": 0.0, "end": 0.5, "score": 0.95},
      ...
    ]
  }
]

Troubleshooting

Slow on first run:

WhisperX needs to download model files; first run will be slower
Subsequent runs use the cached model

Out of memory:

Use a smaller model (tiny or base)
Ensure the system has enough memory

Low recognition accuracy:

Try a larger model (medium or large-v2)
Explicitly specify the language instead of auto-detect
Weekly Installs
50
Repository
maxgent-ai/maxg…t-plugin
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass