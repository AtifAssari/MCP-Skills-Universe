---
rating: ⭐⭐⭐
title: groq-stt
url: https://skills.sh/958877748/skills/groq-stt
---

# groq-stt

skills/958877748/skills/groq-stt
groq-stt
Installation
$ npx skills add https://github.com/958877748/skills --skill groq-stt
SKILL.md
Groq STT Skill

This skill uploads an audio file to the Groq Speech-to-Text API and saves the transcription.

Usage
# set your API key (or use .env in the repo root)
export GROQ_API_KEY=your_api_key_here

# run the script with a path to an audio file
node scripts/transcribe.mjs /path/to/audio.mp4

Output
Writes a {filename}_transcript.txt next to the input file.
Notes
Uses the whisper-large-v3-turbo model by default.
Supported file types: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, webm
Weekly Installs
59
Repository
958877748/skills
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass