---
title: sag
url: https://skills.sh/steipete/clawdis/sag
---

# sag

skills/steipete/clawdis/sag
sag
Installation
$ npx skills add https://github.com/steipete/clawdis --skill sag
SKILL.md
sag

Use sag for ElevenLabs TTS with local playback.

API key (required)

ELEVENLABS_API_KEY (preferred)
SAG_API_KEY also supported by the CLI

Quick start

sag "Hello there"
sag speak -v "Roger" "Hello"
sag voices
sag prompting (model-specific tips)

Model notes

Default: eleven_v3 (expressive)
Stable: eleven_multilingual_v2
Fast: eleven_flash_v2_5

Pronunciation + delivery rules

First fix: respell (e.g. "key-note"), add hyphens, adjust casing.
Numbers/units/URLs: --normalize auto (or off if it harms names).
Language bias: --lang en|de|fr|... to guide normalization.
v3: SSML <break> not supported; use [pause], [short pause], [long pause].
v2/v2.5: SSML <break time="1.5s" /> supported; <phoneme> not exposed in sag.

v3 audio tags (put at the entrance of a line)

[whispers], [shouts], [sings]
[laughs], [starts laughing], [sighs], [exhales]
[sarcastic], [curious], [excited], [crying], [mischievously]
Example: sag "[whispers] keep this quiet. [short pause] ok?"

Voice defaults

ELEVENLABS_VOICE_ID or SAG_VOICE_ID

Confirm voice + speaker before long output.

Chat voice responses

When the user asks for a "voice" reply (e.g., "crazy scientist voice", "explain in voice"), generate audio and send it:

# Generate audio file
sag -v Clawd -o /tmp/voice-reply.mp3 "Your message here"

# Then include in reply:
# MEDIA:/tmp/voice-reply.mp3


Voice character tips:

Crazy scientist: Use [excited] tags, dramatic pauses [short pause], vary intensity
Calm: Use [whispers] or slower pacing
Dramatic: Use [sings] or [shouts] sparingly

Default voice for Clawd: lj2rcrvANS3gaWWnczSX (or just -v Clawd)

Weekly Installs
1.0K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass