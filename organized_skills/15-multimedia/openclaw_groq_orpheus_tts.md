---
rating: ⭐⭐⭐
title: openclaw-groq-orpheus-tts
url: https://skills.sh/ahmedeid5/openclaw-groq-orpheus-tts/openclaw-groq-orpheus-tts
---

# openclaw-groq-orpheus-tts

skills/ahmedeid5/openclaw-groq-orpheus-tts/openclaw-groq-orpheus-tts
openclaw-groq-orpheus-tts
Installation
$ npx skills add https://github.com/ahmedeid5/openclaw-groq-orpheus-tts --skill openclaw-groq-orpheus-tts
SKILL.md
Groq Orpheus TTS

A powerful and fast text-to-speech skill that leverages Groq's Orpheus models.

Key Features:

100% Free Tier Friendly: Uses the Groq Free API key (100 requests per day).
Ultra-Fast: Near-instant audio generation.
High Quality: Professional generative AI voices.

Supported Languages:

Arabic: Authentic Saudi dialect synthesis (Voices: fahad, sultan, noura, lulwa, aisha).
English: Expressive, high-quality speech (Voices: autumn, diana, hannah, austin, daniel, troy).
Requirements
API Key: A GROQ_API_KEY from the Groq Console. This is FREE.
Terms: You must accept the model terms for orpheus-v1-english on the Groq Playground before using the English model.
Tools: ffmpeg must be installed on your system for audio conversion.
Requirements
API Key: GROQ_API_KEY from Groq Console.
Terms: You must accept the model terms for orpheus-v1-english on the Groq Playground before using the English model.
Tools: ffmpeg must be installed on your system for audio conversion.
Usage

You can ask the assistant to say something or generate an audio file.

Voices Available
Arabic (ar): fahad (Male), sultan (Male), noura (Female), lulwa (Female), aisha (Female).
English (en): autumn, diana, hannah, austin, daniel, troy.
Commands
# General usage
python3 groq-tts.py "Text" output.mp3 [voice] [lang]

# Examples
python3 groq-tts.py "أهلا بك" welcome.mp3 fahad ar
python3 groq-tts.py "Hello world" hello.mp3 troy en

Chat Responses

When you want the assistant to reply in voice, use:

python3 groq-tts.py "Your message" /tmp/reply.mp3 fahad ar
# Then include MEDIA:/tmp/reply.mp3 in the response.

Weekly Installs
14
Repository
ahmedeid5/openc…heus-tts
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass