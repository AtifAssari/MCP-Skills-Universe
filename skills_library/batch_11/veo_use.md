---
title: veo-use
url: https://skills.sh/cnemri/google-genai-skills/veo-use
---

# veo-use

skills/cnemri/google-genai-skills/veo-use
veo-use
Installation
$ npx skills add https://github.com/cnemri/google-genai-skills --skill veo-use
SKILL.md
Veo Use

Use this skill to generate and edit videos using Google's Veo models (veo-3.1 and veo-2.0).

This skill uses portable Python scripts managed by uv.

Prerequisites

Ensure you have one of the following authentication methods configured in your environment:

API Key:

GOOGLE_API_KEY or GEMINI_API_KEY

Vertex AI:

GOOGLE_CLOUD_PROJECT
GOOGLE_CLOUD_LOCATION
GOOGLE_GENAI_USE_VERTEXAI=1
Usage
1. Text to Video

Generate a video purely from a text description.

uv run skills/veo-use/scripts/text_to_video.py "A cinematic drone shot of a futuristic city" --output city.mp4

2. Image to Video

Generate a video starting from a static image context.

uv run skills/veo-use/scripts/image_to_video.py "Zoom out from the flower" --image start.png --output flower.mp4

3. Reference to Video

Use specific asset images (subjects, products) to guide generation.

uv run skills/veo-use/scripts/reference_to_video.py "A man walking on the moon" --reference-image man.png --output moon_walk.mp4

4. Edit Video (Inpainting)

Modify existing videos using masks.

Modes:

REMOVE: Remove dynamic object.
REMOVE_STATIC: Remove static object (watermark).
INSERT: Insert new object (requires --prompt).
uv run skills/veo-use/scripts/edit_video.py --video input.mp4 --mask mask.png --mode INSERT --prompt "A flying car" --output edited.mp4

5. Extend Video

Extend the duration of an existing video clip.

uv run skills/veo-use/scripts/extend_video.py --video clip.mp4 --prompt "The car flies away into the sunset" --duration 6 --output extended.mp4

Common Options
--model: Default veo-3.1-generate-001.
--resolution: 1080p (default), 720p, 4k.
--aspect-ratio: 16:9 (default), 9:16.
--duration: 6 (default), 4, 8.
References

Before running scripts, review the reference guides for prompting tips and best practices.

Prompting Guide - Camera angles, movements, lens effects, and visual styles
Weekly Installs
120
Repository
cnemri/google-g…i-skills
GitHub Stars
119
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass