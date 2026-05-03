---
title: local-whisper
url: https://skills.sh/thinkfleetai/thinkfleet-engine/local-whisper
---

# local-whisper

skills/thinkfleetai/thinkfleet-engine/local-whisper
local-whisper
Installation
$ npx skills add https://github.com/thinkfleetai/thinkfleet-engine --skill local-whisper
SKILL.md
Local Whisper STT

Local speech-to-text using OpenAI's Whisper. Fully offline after initial model download.

Usage
# Basic
~/.thinkfleetbot/skills/local-whisper/scripts/local-whisper audio.wav

# Better model
~/.thinkfleetbot/skills/local-whisper/scripts/local-whisper audio.wav --model turbo

# With timestamps
~/.thinkfleetbot/skills/local-whisper/scripts/local-whisper audio.wav --timestamps --json

Models
Model	Size	Notes
tiny	39M	Fastest
base	74M	Default
small	244M	Good balance
turbo	809M	Best speed/quality
large-v3	1.5GB	Maximum accuracy
Options
--model/-m — Model size (default: base)
--language/-l — Language code (auto-detect if omitted)
--timestamps/-t — Include word timestamps
--json/-j — JSON output
--quiet/-q — Suppress progress
Setup

Uses uv-managed venv at .venv/. To reinstall:

cd ~/.thinkfleetbot/skills/local-whisper
uv venv .venv --python 3.12
uv pip install --python .venv/bin/python click openai-whisper torch --index-url https://download.pytorch.org/whl/cpu

Weekly Installs
146
Repository
thinkfleetai/th…t-engine
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass