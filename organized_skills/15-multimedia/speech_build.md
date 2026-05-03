---
rating: ⭐⭐⭐
title: speech-build
url: https://skills.sh/cnemri/google-genai-skills/speech-build
---

# speech-build

skills/cnemri/google-genai-skills/speech-build
speech-build
Installation
$ npx skills add https://github.com/cnemri/google-genai-skills --skill speech-build
SKILL.md
Speech Skill (TTS & STT)

Use this skill to implement audio generation and transcription workflows using the google-genai and google-cloud-speech SDKs.

Quick Start Setup
from google import genai
from google.genai import types
# For STT: from google.cloud import speech_v2

client = genai.Client()

Reference Materials
Text-to-Speech (TTS): Gemini-TTS, Chirp 3 HD, Instant Custom Voice.
Speech-to-Text (STT): Chirp 3 Transcription, Diarization, Streaming.
Voices & Locales: Available voices (Aoede, Puck...) and languages.
Prompting Guide: How to control style, accent, and pacing in Gemini-TTS.
Source Code: Deep inspection of SDK internals.
Common Workflows
1. Generate Speech (Gemini-TTS)
response = client.models.generate_content(
    model="gemini-2.5-flash-preview-tts",
    contents="Hello, world!",
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name='Kore')
            )
        )
    )
)

2. Transcribe Audio (Chirp 3)
# Requires google-cloud-speech
from google.cloud import speech_v2
# ... (See stt.md for full setup)
response = speech_client.recognize(...)

Weekly Installs
39
Repository
cnemri/google-g…i-skills
GitHub Stars
119
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn