---
rating: ⭐⭐⭐
title: ai-music-generation
url: https://skills.sh/inference-sh/skills/ai-music-generation
---

# ai-music-generation

skills/inference-sh/skills/ai-music-generation
ai-music-generation
Installation
$ npx skills add https://github.com/inference-sh/skills --skill ai-music-generation
SKILL.md
AI Music Generation

Generate music and songs via inference.sh CLI.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

# Generate a song
belt app run infsh/diffrythm --input '{"prompt": "upbeat electronic dance track"}'

Available Models
Model	App ID	Best For
ElevenLabs Music	elevenlabs/music	Up to 10 min, commercial license
Diffrythm	infsh/diffrythm	Fast song generation
Tencent Song	infsh/tencent-song-generation	Full songs with vocals
Browse Audio Apps
belt app list --category audio

Examples
Instrumental Track
belt app run infsh/diffrythm --input '{
  "prompt": "cinematic orchestral soundtrack, epic and dramatic"
}'

Song with Vocals
belt app sample infsh/tencent-song-generation --save input.json

# Edit input.json:
# {
#   "prompt": "pop song about summer love",
#   "lyrics": "Walking on the beach with you..."
# }

belt app run infsh/tencent-song-generation --input input.json

Background Music for Video
belt app run infsh/diffrythm --input '{
  "prompt": "calm lo-fi hip hop beat, study music, relaxing"
}'

Podcast Intro
belt app run infsh/diffrythm --input '{
  "prompt": "short podcast intro jingle, professional, tech themed, 10 seconds"
}'

Game Soundtrack
belt app run infsh/diffrythm --input '{
  "prompt": "retro 8-bit video game music, adventure theme, chiptune"
}'

Prompt Tips

Genre keywords: pop, rock, electronic, jazz, classical, hip-hop, lo-fi, ambient, orchestral

Mood keywords: happy, sad, energetic, calm, dramatic, epic, mysterious, uplifting

Instrument keywords: piano, guitar, synth, drums, strings, brass, choir

Structure keywords: intro, verse, chorus, bridge, outro, loop

Use Cases
Social Media: Background music for videos
Podcasts: Intro/outro jingles
Games: Soundtracks and effects
Videos: Background scores
Ads: Commercial jingles
Content Creation: Royalty-free music
Related Skills
# ElevenLabs music (up to 10 min, commercial license)
npx skills add inference-sh/skills@elevenlabs-music

# ElevenLabs sound effects (combine with music)
npx skills add inference-sh/skills@elevenlabs-sound-effects

# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# Text-to-speech
npx skills add inference-sh/skills@text-to-speech

# Video generation (add music to videos)
npx skills add inference-sh/skills@ai-video-generation

# Speech-to-text
npx skills add inference-sh/skills@speech-to-text


Browse all apps: belt app list

Documentation
Running Apps - How to run apps via CLI
Content Pipeline Example - Building media workflows
Apps Overview - Understanding the app ecosystem
Weekly Installs
299
Repository
inference-sh/skills
GitHub Stars
395
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn