---
title: music
url: https://skills.sh/elevenlabs/skills/music
---

# music

skills/elevenlabs/skills/music
music
Installation
$ npx skills add https://github.com/elevenlabs/skills --skill music
Summary

AI-generated music composition from text prompts with optional fine-grained control via composition plans.

Supports prompt-based generation for instrumental tracks, songs with lyrics, background music, and jingles with configurable length in milliseconds
Composition plans enable structured control over styles and sections; generate a plan, modify it, then compose for granular customization
Includes compose_detailed method for retrieving audio alongside composition plan and metadata in a single call
Content restrictions prevent referencing specific artists or copyrighted lyrics; API returns suggestions for rejected prompts
Requires ElevenLabs API key and internet access; available in Python, JavaScript, and via cURL
SKILL.md
ElevenLabs Music Generation

Generate music from text prompts - supports instrumental tracks, songs with lyrics, and fine-grained control via composition plans.

Setup: See Installation Guide. For JavaScript, use @elevenlabs/* packages only.

Quick Start
Python
from elevenlabs import ElevenLabs

client = ElevenLabs()

audio = client.music.compose(
    prompt="A chill lo-fi hip hop beat with jazzy piano chords",
    music_length_ms=30000
)

with open("output.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)

JavaScript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import { createWriteStream } from "fs";

const client = new ElevenLabsClient();
const audio = await client.music.compose({
  prompt: "A chill lo-fi hip hop beat with jazzy piano chords",
  musicLengthMs: 30000,
});
audio.pipe(createWriteStream("output.mp3"));

cURL
curl -X POST "https://api.elevenlabs.io/v1/music" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" \
  -d '{"prompt": "A chill lo-fi beat", "music_length_ms": 30000}' --output output.mp3

Methods
Method	Description
music.compose	Generate audio from a prompt or composition plan
music.composition_plan.create	Generate a structured plan for fine-grained control
music.compose_detailed	Generate audio + composition plan + metadata
music.video_to_music	Generate background music from one or more uploaded video files
music.upload	Upload an audio file for later inpainting workflows and optionally extract its composition plan

See API Reference for full parameter details.

music.upload is available to enterprise clients with access to the inpainting feature.

Video to Music

Generate background music that follows one or more uploaded video clips. The API combines videos in order, accepts an optional natural-language description, and lets you steer style with up to 10 tags such as upbeat or cinematic.

Python
from elevenlabs import ElevenLabs

client = ElevenLabs()

audio = client.music.video_to_music(
    videos=["trailer.mp4"],
    description="Build suspense, then resolve with a warm cinematic finish.",
    tags=["cinematic", "suspenseful", "uplifting"],
)

with open("video-score.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)

cURL
curl -X POST "https://api.elevenlabs.io/v1/music/video-to-music" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -F "videos=@trailer.mp4" \
  -F "description=Build suspense, then resolve with a warm cinematic finish." \
  -F "tags=cinematic" \
  -F "tags=suspenseful" \
  -F "tags=uplifting" \
  --output video-score.mp3


Constraints from the current API schema:

Upload 1-10 video files per request
Keep total combined upload size at or below 200 MB
Keep total combined video duration at or below 600 seconds
Use description for high-level musical direction and tags for concise style cues
Composition Plans

For granular control, generate a composition plan first, modify it, then compose:

plan = client.music.composition_plan.create(
    prompt="An epic orchestral piece building to a climax",
    music_length_ms=60000
)

# Inspect/modify styles and sections
print(plan.positiveGlobalStyles)  # e.g. ["orchestral", "epic", "cinematic"]

audio = client.music.compose(
    composition_plan=plan,
    music_length_ms=60000
)

Content Restrictions
Cannot reference specific artists, bands, or copyrighted lyrics
bad_prompt errors include a prompt_suggestion with alternative phrasing
bad_composition_plan errors include a composition_plan_suggestion
Error Handling
try:
    audio = client.music.compose(prompt="...", music_length_ms=30000)
except Exception as e:
    print(f"API error: {e}")


Common errors: 401 (invalid key), 422 (invalid params), 429 (rate limit).

References
Installation Guide
API Reference
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