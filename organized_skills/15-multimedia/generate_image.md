---
rating: ⭐⭐⭐
title: generate-image
url: https://skills.sh/wxul/openrouter-generate-image-skill/generate-image
---

# generate-image

skills/wxul/openrouter-generate-image-skill/generate-image
generate-image
Installation
$ npx skills add https://github.com/wxul/openrouter-generate-image-skill --skill generate-image
SKILL.md
Generate Image via OpenRouter

Generate images using OpenRouter's image models from the command line. Default model: google/gemini-3.1-flash-image-preview.

Prerequisites
OPENROUTER_API_KEY environment variable must be set
tsx available via npx
Usage

Run the script via npx tsx:

npx tsx generate-image.ts \
  --prompt "description of the image" \
  --model "google/gemini-3.1-flash-image-preview" \
  --width 1024 --height 1024 \
  --output "filename.png" \
  --dir "./generated-images" \
  --proxy "http://127.0.0.1:7890"

Parameters
Param	Required	Default	Description
--prompt	Yes	-	Image description
--model	No	google/gemini-3.1-flash-image-preview	OpenRouter model ID
--width	No	1024	Image width
--height	No	1024	Image height
--output	No	auto (timestamp-slug.png)	Output filename
--dir	No	./generated-images	Output directory
--proxy	No	-	HTTP proxy URL
Supported Models
google/gemini-3.1-flash-image-preview (default, recommended)
black-forest-labs/flux-1.1-pro
black-forest-labs/flux-schnell
Any OpenRouter model that supports image generation
How to Use as an Agent

When the user asks you to generate an image:

Compose a detailed English prompt describing the desired image
Choose appropriate model and size for the use case
Run the script using Bash tool
The script outputs the saved file path to stdout — use this path to reference the image in code or tell the user
Quick Examples
# Simple generation with defaults
npx tsx generate-image.ts \
  --prompt "a minimalist logo of a mountain with a sun, flat design, blue and orange"

# With specific model and output
npx tsx generate-image.ts \
  --prompt "abstract gradient background, purple to blue" \
  --model "black-forest-labs/flux-1.1-pro" \
  --output "bg-gradient.png" \
  --dir "./public/images"

# With proxy
npx tsx generate-image.ts \
  --prompt "pixel art cat sitting on a desk" \
  --proxy "http://127.0.0.1:7890"

Troubleshooting
No API key: Set OPENROUTER_API_KEY env var. Get key at https://openrouter.ai/keys
Proxy issues: Ensure proxy URL is correct and proxy is running
Model not found: Check available models at https://openrouter.ai/models
Weekly Installs
9
Repository
wxul/openrouter…ge-skill
GitHub Stars
1
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass