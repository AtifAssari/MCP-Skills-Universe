---
rating: ⭐⭐⭐
title: speech-to-text
url: https://skills.sh/inference-sh/skills/speech-to-text
---

# speech-to-text

skills/inference-sh/skills/speech-to-text
speech-to-text
Installation
$ npx skills add https://github.com/inference-sh/skills --skill speech-to-text
SKILL.md
Speech-to-Text

Transcribe audio to text via inference.sh CLI.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

belt app run infsh/fast-whisper-large-v3 --input '{"audio_url": "https://audio.mp3"}'

Available Models
Model	App ID	Best For
ElevenLabs Scribe v2	elevenlabs/stt	98%+ accuracy, diarization, 90+ languages
Fast Whisper V3	infsh/fast-whisper-large-v3	Fast transcription
Whisper V3 Large	infsh/whisper-v3-large	Highest accuracy
Examples
Basic Transcription
belt app run infsh/fast-whisper-large-v3 --input '{"audio_url": "https://meeting.mp3"}'

With Timestamps
belt app sample infsh/fast-whisper-large-v3 --save input.json

# {
#   "audio_url": "https://podcast.mp3",
#   "timestamps": true
# }

belt app run infsh/fast-whisper-large-v3 --input input.json

Translation (to English)
belt app run infsh/whisper-v3-large --input '{
  "audio_url": "https://french-audio.mp3",
  "task": "translate"
}'

From Video
# Extract audio from video first
belt app run infsh/video-audio-extractor --input '{"video_url": "https://video.mp4"}' > audio.json

# Transcribe the extracted audio
belt app run infsh/fast-whisper-large-v3 --input '{"audio_url": "<audio-url>"}'

Workflow: Video Subtitles
# 1. Transcribe video audio
belt app run infsh/fast-whisper-large-v3 --input '{
  "audio_url": "https://video.mp4",
  "timestamps": true
}' > transcript.json

# 2. Use transcript for captions
belt app run infsh/caption-videos --input '{
  "video_url": "https://video.mp4",
  "captions": "<transcript-from-step-1>"
}'

Supported Languages

Whisper supports 99+ languages including: English, Spanish, French, German, Italian, Portuguese, Chinese, Japanese, Korean, Arabic, Hindi, Russian, and many more.

Use Cases
Meetings: Transcribe recordings
Podcasts: Generate transcripts
Subtitles: Create captions for videos
Voice Notes: Convert to searchable text
Interviews: Transcription for research
Accessibility: Make audio content accessible
Output Format

Returns JSON with:

text: Full transcription
segments: Timestamped segments (if requested)
language: Detected language
Related Skills
# ElevenLabs STT (98%+ accuracy, diarization)
npx skills add inference-sh/skills@elevenlabs-stt

# ElevenLabs TTS (reverse direction)
npx skills add inference-sh/skills@elevenlabs-tts

# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# Text-to-speech (reverse direction)
npx skills add inference-sh/skills@text-to-speech

# Video generation (add captions)
npx skills add inference-sh/skills@ai-video-generation

# AI avatars (lipsync with transcripts)
npx skills add inference-sh/skills@ai-avatar-video


Browse all audio apps: belt app list --category audio

Documentation
Running Apps - How to run apps via CLI
Audio Transcription Example - Complete transcription guide
Apps Overview - Understanding the app ecosystem
Weekly Installs
308
Repository
inference-sh/skills
GitHub Stars
395
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass