---
title: openai-whisper
url: https://skills.sh/steipete/clawdis/openai-whisper
---

# openai-whisper

skills/steipete/clawdis/openai-whisper
openai-whisper
Installation
$ npx skills add https://github.com/steipete/clawdis --skill openai-whisper
Summary

Local speech-to-text transcription using OpenAI's Whisper CLI without API keys.

Transcribes audio files (MP3, M4A, and other formats) directly on your machine with no external API calls required
Supports multiple model sizes (tiny, base, small, medium, large, turbo) with automatic caching to ~/.cache/whisper on first run
Offers transcription and translation tasks with configurable output formats (TXT, SRT, JSON, VTT)
Requires only the whisper CLI binary, installable via Homebrew or pip
SKILL.md
Whisper (CLI)

Use whisper to transcribe audio locally.

Quick start

whisper /path/audio.mp3 --model medium --output_format txt --output_dir .
whisper /path/audio.m4a --task translate --output_format srt

Notes

Models download to ~/.cache/whisper on first run.
--model defaults to turbo on this install.
Use smaller models for speed, larger for accuracy.
Weekly Installs
2.2K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass