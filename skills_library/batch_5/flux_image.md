---
title: flux-image
url: https://skills.sh/inference-sh/skills/flux-image
---

# flux-image

skills/inference-sh/skills/flux-image
flux-image
Installation
$ npx skills add https://github.com/inference-sh/skills --skill flux-image
SKILL.md
FLUX Image Generation

Generate images with FLUX models via inference.sh CLI.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

belt app run falai/flux-dev-lora --input '{"prompt": "a futuristic city at night"}'

FLUX Models
Model	App ID	Speed	Quality	Use Case
FLUX Dev LoRA	falai/flux-dev-lora	Medium	Highest	Production, custom styles
FLUX.2 Klein LoRA	falai/flux-2-klein-lora	Fastest	Good	Fast iteration, 4B/9B sizes
FLUX Dev (Pruna)	pruna/flux-dev	Fast	High	Optimized, speed modes
FLUX Dev LoRA (Pruna)	pruna/flux-dev-lora	Fast	High	LoRA with optimization
FLUX Klein 4B (Pruna)	pruna/flux-klein-4b	Fastest	Good	Ultra-cheap ($0.0001/img)
Examples
High-Quality Generation
belt app run falai/flux-dev-lora --input '{
  "prompt": "professional product photo of headphones, studio lighting, white background"
}'

Fast Generation (Klein)
belt app run falai/flux-2-klein-lora --input '{"prompt": "abstract art, colorful"}'

With LoRA Custom Styles
belt app sample falai/flux-dev-lora --save input.json

# Edit to add lora_url for custom style
belt app run falai/flux-dev-lora --input input.json

Image-to-Image
belt app run falai/flux-dev-lora --input '{
  "prompt": "transform to watercolor style",
  "image_url": "https://your-image.jpg"
}'

For Other Image Tasks
# Image editing with natural language
belt app run falai/reve --input '{"prompt": "change background to beach"}'

# Upscaling
belt app run falai/topaz-image-upscaler --input '{"image_url": "https://..."}'

Related Skills
# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# Pruna P-Image (fast & economical)
npx skills add inference-sh/skills@p-image

# All image generation models
npx skills add inference-sh/skills@ai-image-generation

# Upscaling
npx skills add inference-sh/skills@image-upscaling


Browse all apps: belt app list

Documentation
Running Apps - How to run apps via CLI
Image Generation Example - Complete image generation guide
Streaming Results - Real-time progress updates
Weekly Installs
302
Repository
inference-sh/skills
GitHub Stars
395
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass