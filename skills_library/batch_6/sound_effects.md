---
title: sound-effects
url: https://skills.sh/elevenlabs/skills/sound-effects
---

# sound-effects

skills/elevenlabs/skills/sound-effects
sound-effects
Installation
$ npx skills add https://github.com/elevenlabs/skills --skill sound-effects
Summary

Text-to-sound effect generation with looping, duration control, and prompt adherence tuning.

Converts natural language descriptions into sound effects via ElevenLabs API; supports ambient sounds, UI effects, cinematic impacts, and audio textures
Configurable duration (0.5–30 seconds), prompt influence (0–1 scale for adherence strictness), and seamless looping for v2 model
20+ output formats including MP3, PCM, Opus, and μ-law across various sample rates and bitrates
Requires ELEVENLABS_API_KEY environment variable; available in Python, JavaScript, and cURL
SKILL.md
ElevenLabs Sound Effects

Generate sound effects from text descriptions — supports looping, custom duration, and prompt adherence control.

Setup: See Installation Guide. For JavaScript, use @elevenlabs/* packages only.

Quick Start
Python
from elevenlabs import ElevenLabs

client = ElevenLabs()

audio = client.text_to_sound_effects.convert(
    text="Thunder rumbling in the distance with light rain",
)

with open("thunder.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)

JavaScript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import { createWriteStream } from "fs";

const client = new ElevenLabsClient();
const audio = await client.textToSoundEffects.convert({
  text: "Thunder rumbling in the distance with light rain",
});
audio.pipe(createWriteStream("thunder.mp3"));

cURL
curl -X POST "https://api.elevenlabs.io/v1/sound-generation" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" \
  -d '{"text": "Thunder rumbling in the distance with light rain"}' \
  --output thunder.mp3

Parameters
Parameter	Type	Default	Description
text	string (required)	—	Description of the desired sound effect
model_id	string	eleven_text_to_sound_v2	Model to use
duration_seconds	number | null	null (auto)	Duration 0.5–30s; auto-calculated if null
prompt_influence	number | null	0.3	How closely to follow the prompt (0–1)
loop	boolean	false	Generate a seamlessly looping sound (v2 model only)
Examples with Parameters
# Looping ambient sound, 10 seconds
audio = client.text_to_sound_effects.convert(
    text="Gentle forest ambiance with birds chirping",
    duration_seconds=10.0,
    prompt_influence=0.5,
    loop=True,
)

# Short UI sound, high prompt adherence
audio = client.text_to_sound_effects.convert(
    text="Soft notification chime",
    duration_seconds=1.0,
    prompt_influence=0.8,
)

Output Formats

Pass output_format as a query parameter (cURL) or SDK parameter:

Format	Description
mp3_44100_128	MP3 44.1kHz 128kbps (default)
pcm_44100	Raw uncompressed CD quality
opus_48000_128	Opus 48kHz 128kbps — efficient compressed
ulaw_8000	μ-law 8kHz — telephony

Full list: mp3_22050_32, mp3_24000_48, mp3_44100_32, mp3_44100_64, mp3_44100_96, mp3_44100_128, mp3_44100_192, pcm_8000, pcm_16000, pcm_22050, pcm_24000, pcm_32000, pcm_44100, pcm_48000, ulaw_8000, alaw_8000, opus_48000_32, opus_48000_64, opus_48000_96, opus_48000_128, opus_48000_192.

Prompt Tips
Be specific: "Heavy rain on a tin roof" > "Rain"
Combine elements: "Footsteps on gravel with distant traffic"
Specify style: "Cinematic braam, horror" or "8-bit retro jump sound"
Mention mood/context: "Eerie wind howling through an abandoned building"
Error Handling
try:
    audio = client.text_to_sound_effects.convert(text="Explosion")
except Exception as e:
    print(f"API error: {e}")


Common errors:

401: Invalid API key
422: Invalid parameters (check duration range, prompt_influence range)
429: Rate limit exceeded
References
Installation Guide
Weekly Installs
2.2K
Repository
elevenlabs/skills
GitHub Stars
208
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass