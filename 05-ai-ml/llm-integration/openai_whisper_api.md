---
rating: ⭐⭐
title: openai-whisper-api
url: https://skills.sh/steipete/clawdis/openai-whisper-api
---

# openai-whisper-api

skills/steipete/clawdis/openai-whisper-api
openai-whisper-api
Installation
$ npx skills add https://github.com/steipete/clawdis --skill openai-whisper-api
SKILL.md
OpenAI Whisper API (curl)

Transcribe an audio file via OpenAI’s /v1/audio/transcriptions endpoint. Set OPENAI_BASE_URL to use an OpenAI-compatible proxy or local gateway.

Quick start
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a


Defaults:

Model: whisper-1
Output: <input>.txt
Useful flags
{baseDir}/scripts/transcribe.sh /path/to/audio.ogg --model whisper-1 --out /tmp/transcript.txt
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a --language en
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a --prompt "Speaker names: Peter, Daniel"
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a --json --out /tmp/transcript.json

API key

Set OPENAI_API_KEY, or configure it in the active OpenClaw config file ($OPENCLAW_CONFIG_PATH, default ~/.openclaw/openclaw.json). Optionally set OPENAI_BASE_URL (for example http://127.0.0.1:51805/v1) to use an OpenAI-compatible proxy or local gateway:

{
  skills: {
    "openai-whisper-api": {
      apiKey: "OPENAI_KEY_HERE",
    },
  },
}

Weekly Installs
1.1K
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