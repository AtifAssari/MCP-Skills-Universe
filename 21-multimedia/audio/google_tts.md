---
title: google-tts
url: https://skills.sh/sanjay3290/ai-skills/google-tts
---

# google-tts

skills/sanjay3290/ai-skills/google-tts
google-tts
Installation
$ npx skills add https://github.com/sanjay3290/ai-skills --skill google-tts
SKILL.md
Google Cloud Text-to-Speech

Converts text and documents into audio using Google Cloud TTS API. Supports Neural2, WaveNet, Studio, and Standard voices across 40+ languages.

Setup

API key via GOOGLE_TTS_API_KEY env var or skills/google-tts/config.json with {"api_key": "..."}. Requires ffmpeg for multi-chunk documents. Optional: pip install PyPDF2 python-docx for PDF/DOCX.

Commands
List Voices
python skills/google-tts/scripts/google_tts.py voices --language en-US --type Neural2
python skills/google-tts/scripts/google_tts.py voices --json

Text-to-Speech
# From text or document (PDF, DOCX, MD, TXT)
python skills/google-tts/scripts/google_tts.py tts --text "Hello world" --output ~/Downloads/hello.mp3
python skills/google-tts/scripts/google_tts.py tts --file /path/to/doc.pdf --output ~/Downloads/narration.mp3

# With voice, rate, pitch, encoding options
python skills/google-tts/scripts/google_tts.py tts --file doc.md --voice en-US-Neural2-F --rate 0.9 --encoding MP3 --output ~/Downloads/out.mp3

Podcast Generation

Takes a JSON script with alternating speakers, synthesizes each with a different voice.

[
  {"speaker": "host1", "text": "Welcome to our podcast!"},
  {"speaker": "host2", "text": "Thanks for having me..."}
]

python skills/google-tts/scripts/google_tts.py podcast --script /tmp/script.json --output ~/Downloads/podcast.mp3
python skills/google-tts/scripts/google_tts.py podcast --script /tmp/script.json --voice1 en-US-Neural2-J --voice2 en-US-Neural2-H --rate 0.9 --output ~/Downloads/podcast.mp3

Workflow
Single-Voice Narration
If user provides a file path, use --file. For generated content, write clean prose to /tmp/tts_input.md first.
Default voice: en-US-Neural2-D (male) or en-US-Neural2-F (female). Use Neural2 for best quality/cost balance.
Generate: python skills/google-tts/scripts/google_tts.py tts --file /tmp/tts_input.md --output ~/Downloads/recording.mp3
Report file location and size. Default output to ~/Downloads/.
Podcast from Document
Extract text: python skills/google-tts/scripts/extract.py /path/to/document.pdf
Generate a two-host conversation script as JSON:
Natural discussion, not verbatim reading. Host 1 leads, Host 2 reacts/analyzes.
Include intro and outro. Vary turn lengths. Keep turns under 4000 chars.
Write script to /tmp/podcast_script.json
Generate: python skills/google-tts/scripts/google_tts.py podcast --script /tmp/podcast_script.json --output ~/Downloads/podcast.mp3
Clean up temp files.
Reference
Recommended voice type: Neural2 (~$4/1M chars, high quality)
Speaking rate: 0.25-4.0 (0.85-0.95 good for technical content)
Pitch: -20.0 to 20.0 semitones
Encodings: MP3 (default), LINEAR16 (.wav), OGG_OPUS (.ogg)
API limit: 5000 bytes/request. Script auto-chunks at sentence boundaries.
Weekly Installs
119
Repository
sanjay3290/ai-skills
GitHub Stars
246
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass