---
title: image-creation
url: https://skills.sh/cklxx/elephant.ai/image-creation
---

# image-creation

skills/cklxx/elephant.ai/image-creation
image-creation
Installation
$ npx skills add https://github.com/cklxx/elephant.ai --skill image-creation
SKILL.md
image-creation

Generate images via Seedream.

Required Env
ARK_API_KEY (required)
SEEDREAM_TEXT_ENDPOINT_ID (optional; fallback: SEEDREAM_TEXT_MODEL -> built-in default model)
SEEDREAM_I2I_ENDPOINT_ID (required for refine)
Constraints
Backend minimum pixels: 1920*1920. Smaller inputs (for example 1024x1024) are auto-upscaled.
success=true only when the output file is actually written and non-empty.
Backend response must contain b64_json or url; otherwise the call fails.
Default output path is /tmp unless output is provided.
watermark defaults to false (no "AI generated" watermark). Set to true only when you explicitly need watermark.
Usage
# Text to image
python3 skills/image-creation/run.py generate --prompt 'white cat in moonlight' --style realistic --watermark false

# Image to image
python3 skills/image-creation/run.py refine --image_path /tmp/cat.png --prompt 'add starry sky background' --watermark false

Parameters
generate
name	type	required	notes
prompt	string	yes	image description
style	string	no	style tag (default: realistic)
size	string	no	WIDTHxHEIGHT, default 1920x1920
watermark	bool	no	default false; whether to enable API watermark
output	string	no	output file path (default /tmp/seedream_<ts>.png)
refine
name	type	required	notes
image_path	string	yes	input image path
prompt	string	yes	refinement instruction
watermark	bool	no	default false; whether to enable API watermark
output	string	no	output path (default /tmp/seedream_refined_<ts>.png)
Weekly Installs
31
Repository
cklxx/elephant.ai
GitHub Stars
10
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass