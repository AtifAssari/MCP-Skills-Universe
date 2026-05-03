---
rating: ⭐⭐⭐
title: ai-voice-cloning
url: https://skills.sh/inference-sh/skills/ai-voice-cloning
---

# ai-voice-cloning

skills/inference-sh/skills/ai-voice-cloning
ai-voice-cloning
Installation
$ npx skills add https://github.com/inference-sh/skills --skill ai-voice-cloning
SKILL.md
AI Voice Generation

Generate natural AI voices via inference.sh CLI.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

# Generate speech
belt app run infsh/kokoro-tts --input '{
  "prompt": "Hello! This is an AI-generated voice that sounds natural and engaging.",
  "voice": "af_sarah"
}'

Available Models
Model	App ID	Best For
ElevenLabs TTS	elevenlabs/tts	Premium quality, 22+ voices, 32 languages
ElevenLabs Voice Changer	elevenlabs/voice-changer	Transform existing voice recordings
Kokoro TTS	infsh/kokoro-tts	Natural, multiple voices
DIA	infsh/dia-tts	Conversational, expressive
Chatterbox	infsh/chatterbox	Casual, entertainment
Higgs	infsh/higgs-tts	Professional narration
VibeVoice	infsh/vibevoice	Emotional range
Kokoro Voice Library
American English
Voice ID	Gender	Style
af_sarah	Female	Warm, friendly
af_nicole	Female	Professional
af_sky	Female	Youthful
am_michael	Male	Authoritative
am_adam	Male	Conversational
am_echo	Male	Clear, neutral
British English
Voice ID	Gender	Style
bf_emma	Female	Refined
bf_isabella	Female	Warm
bm_george	Male	Classic
bm_lewis	Male	Modern
Voice Generation Examples
Professional Narration
belt app run infsh/kokoro-tts --input '{
  "prompt": "Welcome to our quarterly earnings call. Today we will discuss the financial performance and strategic initiatives for the past quarter.",
  "voice": "am_michael",
  "speed": 1.0
}'

Conversational Style
belt app run infsh/dia-tts --input '{
  "text": "Hey, so I was thinking about that project we discussed. What if we tried a different approach?",
  "voice": "conversational"
}'

Audiobook Narration
belt app run infsh/kokoro-tts --input '{
  "prompt": "Chapter One. The morning mist hung low over the valley as Sarah made her way down the winding path. She had been walking for hours.",
  "voice": "bf_emma",
  "speed": 0.9
}'

Video Voiceover
belt app run infsh/kokoro-tts --input '{
  "prompt": "Introducing the next generation of productivity. Work smarter, not harder.",
  "voice": "af_nicole",
  "speed": 1.1
}'

Podcast Host
belt app run infsh/kokoro-tts --input '{
  "prompt": "Welcome back to Tech Talk! Im your host, and today we are diving deep into the world of artificial intelligence.",
  "voice": "am_adam"
}'

Multi-Voice Conversation
# Generate dialogue between two speakers
# Speaker 1
belt app run infsh/kokoro-tts --input '{
  "prompt": "Have you seen the latest AI developments? Its incredible how fast things are moving.",
  "voice": "am_michael"
}' > speaker1.json

# Speaker 2
belt app run infsh/kokoro-tts --input '{
  "prompt": "I know, right? Just last week I tried that new image generator and was blown away.",
  "voice": "af_sarah"
}' > speaker2.json

# Merge conversation
belt app run infsh/media-merger --input '{
  "audio_files": ["<speaker1-url>", "<speaker2-url>"],
  "crossfade_ms": 300
}'

Long-Form Content
Chunked Processing

For content over 5000 characters, split into chunks:

# Process long text in chunks
TEXT="Your very long text here..."

# Split and generate
# Chunk 1
belt app run infsh/kokoro-tts --input '{
  "prompt": "<chunk-1>",
  "voice": "bf_emma"
}' > chunk1.json

# Chunk 2
belt app run infsh/kokoro-tts --input '{
  "prompt": "<chunk-2>",
  "voice": "bf_emma"
}' > chunk2.json

# Merge chunks
belt app run infsh/media-merger --input '{
  "audio_files": ["<chunk1-url>", "<chunk2-url>"],
  "crossfade_ms": 100
}'

Voice + Video Workflow
Add Voiceover to Video
# 1. Generate voiceover
belt app run infsh/kokoro-tts --input '{
  "prompt": "This stunning footage shows the beauty of nature in its purest form.",
  "voice": "am_michael"
}' > voiceover.json

# 2. Merge with video
belt app run infsh/media-merger --input '{
  "video_url": "https://your-video.mp4",
  "audio_url": "<voiceover-url>"
}'

Create Talking Head
# 1. Generate speech
belt app run infsh/kokoro-tts --input '{
  "prompt": "Hi, Im excited to share some updates with you today.",
  "voice": "af_sarah"
}' > speech.json

# 2. Animate with avatar
belt app run bytedance/omnihuman-1-5 --input '{
  "image_url": "https://portrait.jpg",
  "audio_url": "<speech-url>"
}'

Speed and Pacing
Speed	Effect	Use For
0.8	Slow, deliberate	Audiobooks, meditation
0.9	Slightly slow	Education, tutorials
1.0	Normal	General purpose
1.1	Slightly fast	Commercials, energy
1.2	Fast	Quick announcements
# Slow narration
belt app run infsh/kokoro-tts --input '{
  "prompt": "Take a deep breath. Let yourself relax.",
  "voice": "bf_emma",
  "speed": 0.8
}'

Punctuation for Pacing

Use punctuation to control speech rhythm:

Punctuation	Effect
Period .	Full pause
Comma ,	Brief pause
...	Extended pause
!	Emphasis
?	Question intonation
-	Quick break
belt app run infsh/kokoro-tts --input '{
  "prompt": "Wait... Did you hear that? Something is coming. Something big!",
  "voice": "am_adam"
}'

Best Practices
Match voice to content - Professional voice for business, casual for social
Use punctuation - Control pacing with periods and commas
Keep sentences short - Easier to generate and sounds more natural
Test different voices - Same text sounds different across voices
Adjust speed - Slightly slower often sounds more natural
Break long content - Process in chunks for consistency
Use Cases
Voiceovers - Video narration, commercials
Audiobooks - Full book narration
Podcasts - AI hosts and guests
E-learning - Course narration
Accessibility - Screen reader content
IVR - Phone system messages
Content localization - Translate and voice
Related Skills
# ElevenLabs TTS (premium, 22+ voices)
npx skills add inference-sh/skills@elevenlabs-tts

# ElevenLabs voice changer (transform recordings)
npx skills add inference-sh/skills@elevenlabs-voice-changer

# All TTS models
npx skills add inference-sh/skills@text-to-speech

# Podcast creation
npx skills add inference-sh/skills@ai-podcast-creation

# AI avatars
npx skills add inference-sh/skills@ai-avatar-video

# Video generation
npx skills add inference-sh/skills@ai-video-generation

# Full platform skill
npx skills add inference-sh/skills@infsh-cli


Browse audio apps: belt app list --category audio

Weekly Installs
288
Repository
inference-sh/skills
GitHub Stars
395
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail