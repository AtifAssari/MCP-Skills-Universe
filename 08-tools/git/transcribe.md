---
title: transcribe
url: https://skills.sh/badlogic/pi-skills/transcribe
---

# transcribe

skills/badlogic/pi-skills/transcribe
transcribe
Installation
$ npx skills add https://github.com/badlogic/pi-skills --skill transcribe
SKILL.md
Transcribe

Speech-to-text using Groq Whisper API.

Setup

The script needs GROQ_API_KEY environment variable. Check if already set:

echo $GROQ_API_KEY


If not set, guide the user through setup:

Ask if they have a Groq API key
If not, have them sign up at https://console.groq.com/ and create an API key
Have them add to their shell profile (~/.zshrc or ~/.bashrc):
export GROQ_API_KEY="<their-api-key>"

Then run source ~/.zshrc (or restart terminal)
Usage
{baseDir}/transcribe.sh <audio-file>

Supported Formats
m4a, mp3, wav, ogg, flac, webm
Max file size: 25MB
Output

Returns plain text transcription with punctuation and proper capitalization to stdout.

Weekly Installs
88
Repository
badlogic/pi-skills
GitHub Stars
1.5K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass