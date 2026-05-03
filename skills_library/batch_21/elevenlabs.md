---
title: elevenlabs
url: https://skills.sh/sanjay3290/ai-skills/elevenlabs
---

# elevenlabs

skills/sanjay3290/ai-skills/elevenlabs
elevenlabs
Installation
$ npx skills add https://github.com/sanjay3290/ai-skills --skill elevenlabs
SKILL.md
ElevenLabs - Text-to-Speech & Podcast Skill
Overview

This skill converts text and documents into high-quality audio using ElevenLabs TTS API. It supports two modes: single-voice narration and two-host conversational podcast generation.

When to Use This Skill

Activate when the user mentions:

"create podcast", "generate podcast", "podcast from document"
"narrate document", "narrate this file", "read aloud"
"text to speech", "TTS", "convert to audio"
"audio from document", "audio version of"
Setup

Config at skills/elevenlabs/config.json:

{
  "api_key": "your-elevenlabs-api-key",
  "default_voice": "JBFqnCBsd6RMkjVDRZzb",
  "default_model": "eleven_multilingual_v2",
  "podcast_voice1": "JBFqnCBsd6RMkjVDRZzb",
  "podcast_voice2": "EXAVITQu4vr4xnSDxMaL"
}


Only api_key is required. Or set ELEVENLABS_API_KEY env var.

Dependencies: pip install PyPDF2 python-docx (only needed for PDF/DOCX files).

Requires ffmpeg for multi-chunk narration and podcasts.

Commands
List Voices
python skills/elevenlabs/scripts/elevenlabs.py voices
python skills/elevenlabs/scripts/elevenlabs.py voices --json


Use this to find voice IDs for the user.

Single-Voice TTS
# From text
python skills/elevenlabs/scripts/elevenlabs.py tts --text "Hello world" --output ~/Downloads/hello.mp3

# From document
python skills/elevenlabs/scripts/elevenlabs.py tts --file /path/to/doc.pdf --output ~/Downloads/narration.mp3

# With specific voice
python skills/elevenlabs/scripts/elevenlabs.py tts --file doc.md --voice VOICE_ID --output out.mp3


The script handles text extraction, chunking at sentence boundaries (~4000 chars), TTS per chunk with voice continuity, and ffmpeg concatenation automatically.

Podcast Generation

Podcast mode requires a JSON script file with conversation segments:

[
  {"speaker": "host1", "text": "Welcome to our podcast! Today we're diving into..."},
  {"speaker": "host2", "text": "That's right! I found the section on..."},
  {"speaker": "host1", "text": "Let's break that down..."}
]

python skills/elevenlabs/scripts/elevenlabs.py podcast --script /tmp/script.json --voice1 ID1 --voice2 ID2 --output ~/Downloads/podcast.mp3

Podcast Workflow (for Claude)

When the user asks to create a podcast from a document:

Extract the document text:

python skills/elevenlabs/scripts/extract.py /path/to/document.pdf


Generate a two-host conversation script from the extracted text. Follow these guidelines:

Write as a natural, engaging discussion between two hosts
Host 1 typically leads/introduces topics, Host 2 adds analysis and reactions
Start with a brief intro welcoming listeners and stating the topic
End with a summary/outro
Keep each turn under 3000 characters
Vary turn lengths - mix short reactions with longer explanations
Use conversational language: "That's a great point", "What I found interesting was..."
Reference specific details from the source document
Avoid reading the document verbatim - discuss and interpret it

Write the script as a JSON array to a temp file:

# Write to /tmp/podcast_script.json
[
  {"speaker": "host1", "text": "Welcome to today's episode..."},
  {"speaker": "host2", "text": "Thanks for having me..."},
  ...
]


Generate the podcast:

python skills/elevenlabs/scripts/elevenlabs.py podcast --script /tmp/podcast_script.json --output ~/Downloads/podcast.mp3


Clean up the temp script file.

Tips
Run voices first to let the user pick voices they like
For podcasts, suggest voice pairs with contrasting qualities (e.g., one deep, one bright)
Default output to ~/Downloads/ unless the user specifies otherwise
For large documents, warn the user about character usage on their ElevenLabs plan
Weekly Installs
135
Repository
sanjay3290/ai-skills
GitHub Stars
246
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass