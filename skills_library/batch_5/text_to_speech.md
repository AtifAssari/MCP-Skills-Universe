---
title: text-to-speech
url: https://skills.sh/inference-sh/skills/text-to-speech
---

# text-to-speech

skills/inference-sh/skills/text-to-speech
text-to-speech
Installation
$ npx skills add https://github.com/inference-sh/skills --skill text-to-speech
SKILL.md
Text-to-Speech

Convert text to natural speech via inference.sh CLI.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

# Generate speech
belt app run infsh/kokoro-tts --input '{"text": "Hello, welcome to our product demo."}'

Available Models
Model	App ID	Best For
ElevenLabs TTS	elevenlabs/tts	Premium quality, 22+ voices, 32 languages
DIA TTS	infsh/dia-tts	Conversational, expressive
Kokoro TTS	infsh/kokoro-tts	Fast, natural
Chatterbox	infsh/chatterbox	General purpose
Higgs Audio	infsh/higgs-audio	Emotional control
VibeVoice	infsh/vibevoice	Podcasts, long-form
Browse All Audio Apps
belt app list --category audio

Examples
Basic Text-to-Speech
belt app run infsh/kokoro-tts --input '{"text": "Welcome to our tutorial."}'

Conversational TTS with DIA
belt app sample infsh/dia-tts --save input.json

# Edit input.json:
# {
#   "text": "Hey! How are you doing today? I'm really excited to share this with you.",
#   "voice": "conversational"
# }

belt app run infsh/dia-tts --input input.json

Long-form Audio (Podcasts)
belt app sample infsh/vibevoice --save input.json

# Edit input.json with your podcast script
belt app run infsh/vibevoice --input input.json

Expressive Speech with Higgs
belt app sample infsh/higgs-audio --save input.json

# {
#   "text": "This is absolutely incredible!",
#   "emotion": "excited"
# }

belt app run infsh/higgs-audio --input input.json

Use Cases
Voiceovers: Product demos, explainer videos
Audiobooks: Convert text to spoken word
Podcasts: Generate podcast episodes
Accessibility: Make content accessible
IVR: Phone system voice prompts
Video Narration: Add narration to videos
Combine with Video

Generate speech, then create a talking head video:

# 1. Generate speech
belt app run infsh/kokoro-tts --input '{"text": "Your script here"}' > speech.json

# 2. Use the audio URL with OmniHuman for avatar video
belt app run bytedance/omnihuman-1-5 --input '{
  "image_url": "https://portrait.jpg",
  "audio_url": "<audio-url-from-step-1>"
}'

Related Skills
# ElevenLabs TTS (premium, 22+ voices)
npx skills add inference-sh/skills@elevenlabs-tts

# ElevenLabs dialogue (multi-speaker)
npx skills add inference-sh/skills@elevenlabs-dialogue

# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# AI avatars (combine TTS with talking heads)
npx skills add inference-sh/skills@ai-avatar-video

# AI music generation
npx skills add inference-sh/skills@ai-music-generation

# Speech-to-text (transcription)
npx skills add inference-sh/skills@speech-to-text

# Video generation
npx skills add inference-sh/skills@ai-video-generation


Browse all apps: belt app list

Documentation
Running Apps - How to run apps via CLI
Audio Transcription Example - Audio processing workflows
Apps Overview - Understanding the app ecosystem
Weekly Installs
302
Repository
inference-sh/skills
GitHub Stars
395
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass