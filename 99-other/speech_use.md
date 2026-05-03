---
title: speech-use
url: https://skills.sh/cnemri/google-genai-skills/speech-use
---

# speech-use

skills/cnemri/google-genai-skills/speech-use
speech-use
Installation
$ npx skills add https://github.com/cnemri/google-genai-skills --skill speech-use
SKILL.md
Speech Use

Use this skill to perform Text-to-Speech (TTS), Speech-to-Text (STT), and Voice Cloning operations.

This skill uses portable Python scripts managed by uv.

Prerequisites

Environment Variables:

GOOGLE_API_KEY (for TTS via Gemini)
GOOGLE_CLOUD_PROJECT (Required for STT and Voice Cloning)
GOOGLE_APPLICATION_CREDENTIALS (Recommended for STT/Voice Cloning)

APIs Enabled:

Text-to-Speech API (texttospeech.googleapis.com)
Speech-to-Text API (speech.googleapis.com)
Usage
1. Generate Speech (TTS)

Generate audio from text using Gemini-TTS.

Standard Voice:

uv run skills/speech-use/scripts/generate_speech.py "Hello world, this is a test." --voice Puck --output hello.wav


Custom Voice (Cloned):

uv run skills/speech-use/scripts/generate_speech.py "This is my custom voice speaking." --voice-cloning-key "YOUR_KEY_HERE" --output custom.wav

2. Create Custom Voice (Voice Cloning)

Generate a voiceCloningKey from a reference audio file and a consent file.

Requirements:

reference.wav: 10-30s of clear speech (the voice to clone).
consent.wav: The speaker saying: "I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model."
uv run skills/speech-use/scripts/create_custom_voice.py --reference-audio reference.wav --consent-audio consent.wav


Save the output key to use with generate_speech.py.

3. Transcribe Audio (STT)

Transcribe audio files using Chirp 3.

uv run skills/speech-use/scripts/transcribe_audio.py audio.wav --language en-US --output transcript.txt

Options

generate_speech.py

--voice: Prebuilt voice (e.g., Kore, Puck, Fenrir, Aoede).
--voice-cloning-key: Key from create_custom_voice.py.
--model: Default gemini-2.5-flash-preview-tts.

transcribe_audio.py

--model: Default chirp_3.
--language: Default auto.
--location: Cloud region (default us).
References

Before running scripts, review the reference guides for available voices and options.

Voices Guide - 30+ voice options with styles (Puck, Kore, Fenrir, Aoede, etc.)
Weekly Installs
48
Repository
cnemri/google-g…i-skills
GitHub Stars
119
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail