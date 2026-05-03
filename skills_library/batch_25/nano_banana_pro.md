---
title: nano-banana-pro
url: https://skills.sh/insight68/skills/nano-banana-pro
---

# nano-banana-pro

skills/insight68/skills/nano-banana-pro
nano-banana-pro
Installation
$ npx skills add https://github.com/insight68/skills --skill nano-banana-pro
SKILL.md
Nano Banana Pro (Gemini 3 Pro Image)

Use the bundled script to generate or edit images.

Generate

uv run {baseDir}/scripts/generate_image.py --prompt "your image description" --filename "output.png" --resolution 1K


Edit (single image)

uv run {baseDir}/scripts/generate_image.py --prompt "edit instructions" --filename "output.png" -i "/path/in.png" --resolution 2K


Multi-image composition (up to 14 images)

uv run {baseDir}/scripts/generate_image.py --prompt "combine these into one scene" --filename "output.png" -i img1.png -i img2.png -i img3.png


API key

GEMINI_API_KEY env var
Or set skills."nano-banana-pro".apiKey / skills."nano-banana-pro".env.GEMINI_API_KEY in ~/.openclaw/openclaw.json

Notes

Resolutions: 1K (default), 2K, 4K.
Use timestamps in filenames: yyyy-mm-dd-hh-mm-ss-name.png.
The script prints a MEDIA: line for OpenClaw to auto-attach on supported chat providers.
Do not read the image back; report the saved path only.
Weekly Installs
9
Repository
insight68/skills
GitHub Stars
4
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass