---
rating: ⭐⭐
title: image-remove-background
url: https://skills.sh/agntswrm/agent-media/image-remove-background
---

# image-remove-background

skills/agntswrm/agent-media/image-remove-background
image-remove-background
Installation
$ npx skills add https://github.com/agntswrm/agent-media --skill image-remove-background
SKILL.md
Image Remove Background

Removes the background from an image, leaving only the foreground subject with transparency.

Command
npx agent-media@latest image remove-background --in <path> [options]

Inputs
Option	Required	Description
--in	Yes	Input file path or URL
--out	No	Output path, filename or directory (default: ./)
--provider	No	Provider to use (local, fal, replicate)
--resolution	No	Output resolution (e.g., "2048x2048"). Supported by fal Dynamic model.
Output

Returns a JSON object with the processed image path:

{
  "ok": true,
  "media_type": "image",
  "action": "remove-background",
  "provider": "fal",
  "output_path": "nobg_123_abc.png",
  "mime": "image/png",
  "bytes": 34567
}

Examples

Remove background from local file:

npx agent-media@latest image remove-background --in portrait.jpg


Remove background using specific provider:

npx agent-media@latest image remove-background --in portrait.jpg --provider replicate


Remove background at full resolution (fal Dynamic model):

npx agent-media@latest image remove-background --in portrait.jpg --provider fal --resolution 2048x2048

Providers
local

Runs locally on CPU using Transformers.js, no API key required.

Uses Xenova/modnet model
Models downloaded on first use (~25MB)
You may see a mutex lock failed error — ignore it, the output is correct if "ok": true
npx agent-media@latest image remove-background --in portrait.jpg --provider local

fal
Requires FAL_API_KEY
Uses birefnet/v2 model with General Use (Dynamic) variant
Supports --resolution option (e.g., "2048x2048") for processing at full input resolution
replicate
Requires REPLICATE_API_TOKEN
Uses birefnet model
Weekly Installs
126
Repository
agntswrm/agent-media
GitHub Stars
4
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass