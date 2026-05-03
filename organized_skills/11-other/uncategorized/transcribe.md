---
rating: ⭐⭐
title: transcribe
url: https://skills.sh/aviz85/claude-skills-library/transcribe
---

# transcribe

skills/aviz85/claude-skills-library/transcribe
transcribe
Installation
$ npx skills add https://github.com/aviz85/claude-skills-library --skill transcribe
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
25
Repository
aviz85/claude-s…-library
GitHub Stars
27
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail