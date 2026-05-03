---
title: video-understand
url: https://skills.sh/jrusso1020/video-understand-skills/video-understand
---

# video-understand

skills/jrusso1020/video-understand-skills/video-understand
video-understand
Installation
$ npx skills add https://github.com/jrusso1020/video-understand-skills --skill video-understand
SKILL.md
Video Understanding

Multi-provider video understanding with automatic fallback and model selection.

Quick Start
# Check available providers
python3 scripts/check_providers.py

# Process a video (auto-selects best provider)
python3 scripts/process_video.py "https://youtube.com/watch?v=..."
python3 scripts/process_video.py /path/to/video.mp4

# Custom prompt
python3 scripts/process_video.py video.mp4 -p "List all products shown with timestamps"

# Use specific provider/model
python3 scripts/process_video.py video.mp4 --provider openrouter -m google/gemini-3-pro-preview

# List available models
python3 scripts/process_video.py --list-models

Provider Hierarchy

Automatically selects the best available provider:

Priority	Provider	Capability	Env Var	Default Model
1	Gemini	Full video	GEMINI_API_KEY	gemini-3-flash-preview
2	Vertex AI	Full video	GOOGLE_APPLICATION_CREDENTIALS	gemini-3-flash-preview
3	OpenRouter	Full video	OPENROUTER_API_KEY	google/gemini-3-flash-preview
4	FFMPEG	Frames + ASR	None (requires ffmpeg + whisper)	scene
5	OpenAI	ASR only	OPENAI_API_KEY	whisper-1
6	AssemblyAI	ASR + analysis	ASSEMBLYAI_API_KEY	best
7	Deepgram	ASR	DEEPGRAM_API_KEY	nova-2
8	Groq	ASR (fast)	GROQ_API_KEY	whisper-large-v3-turbo
9	Local Whisper	ASR (offline)	None	base

Full video = visual + audio analysis. Frames + ASR = extracted screenshots + audio transcription (free, offline). ASR = audio transcription only.

CLI Options
python3 scripts/process_video.py [OPTIONS] SOURCE

Arguments:
  SOURCE              YouTube URL, video URL, or local file path

Options:
  -p, --prompt TEXT   Custom prompt for video understanding
  --provider NAME     Force specific provider
  -m, --model NAME    Force specific model
  --asr-only          Force ASR-only mode (skip visual analysis)
  -o, --output FILE   Write JSON to file instead of stdout
  -q, --quiet         Suppress progress messages
  --list-models       Show available models per provider
  --list-providers    Show available providers as JSON

Model Selection

Each provider supports multiple models. Use --list-models to see options:

python3 scripts/process_video.py --list-models


OpenRouter models:

google/gemini-3-flash-preview (default) - Fast, free tier
google/gemini-3-pro-preview - Higher quality

Gemini models:

gemini-3-flash-preview (default) - Latest, fast
gemini-3-pro-preview - Highest quality
gemini-2.5-flash - Stable production fallback

Local Whisper models:

tiny, base (default), small, medium, large, large-v3

FFMPEG modes (frame extraction strategy):

scene (default) - Extract frames when scene changes (smart, efficient)
keyframe - Extract I-frames only (fastest)
interval - Extract frames at regular intervals (predictable)
Quick Reference
Task	Reference
Setup & API keys	setup-guide.md
Use Gemini for video	gemini.md
Use OpenRouter	openrouter.md
FFMPEG frames (free)	ffmpeg-frames.md
ASR providers	asr-providers.md
Output JSON schema	output-format.md
Video sources & downloading	video-sources.md
Verify Setup
python3 scripts/setup.py  # Check dependencies and API keys

Output Format

All providers return consistent JSON:

{
  "source": {
    "type": "youtube|url|local",
    "path": "...",
    "duration_seconds": 120.5,
    "size_mb": 15.2
  },
  "provider": "openrouter",
  "model": "google/gemini-3-flash-preview",
  "capability": "full_video",
  "response": "...",
  "transcript": [{"start": 0.0, "end": 2.5, "text": "..."}],
  "text": "Full transcript..."
}

Features
Automatic provider selection based on available API keys
Model selection per provider with sensible defaults
Robust path handling for macOS special characters and unicode
Progress output (use -q for quiet mode)
File size warnings for API limits
Auto-conversion of video formats when needed
YouTube URL support (direct or via download)
Requirements

For full video understanding:

pip install google-generativeai  # Gemini
pip install openai               # OpenRouter


For ASR fallback:

brew install yt-dlp ffmpeg       # Video tools
pip install openai               # OpenAI Whisper
pip install groq                 # Groq Whisper
pip install assemblyai           # AssemblyAI
pip install deepgram-sdk         # Deepgram
pip install openai-whisper       # Local Whisper

Weekly Installs
115
Repository
jrusso1020/vide…d-skills
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn