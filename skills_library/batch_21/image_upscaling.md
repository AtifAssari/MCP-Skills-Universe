---
title: image-upscaling
url: https://skills.sh/inference-sh/skills/image-upscaling
---

# image-upscaling

skills/inference-sh/skills/image-upscaling
image-upscaling
Installation
$ npx skills add https://github.com/inference-sh/skills --skill image-upscaling
SKILL.md
Image Upscaling

Upscale and enhance images via inference.sh CLI.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

belt app run infsh/real-esrgan --input '{"image_url": "https://your-image.jpg"}'

Available Upscalers
Model	App ID	Best For
Topaz Image Upscaler	falai/topaz-image-upscaler	Professional quality, any image
Examples
Upscale Any Image
belt app run falai/topaz-image-upscaler --input '{"image_url": "https://low-res-image.jpg"}'

Workflow: Generate and Upscale
# 1. Generate image with FLUX Klein (fast)
belt app run falai/flux-2-klein-lora --input '{"prompt": "landscape painting"}' > image.json

# 2. Upscale the result
belt app run falai/topaz-image-upscaler --input '{"image_url": "<url-from-step-1>"}'

Use Cases
AI Art: Upscale generated images for print
Old Photos: Restore and enhance resolution
Web Images: Prepare for high-DPI displays
Print: Increase resolution for large prints
Thumbnails: Create high-res versions
Related Skills
# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# Image generation (generate then upscale)
npx skills add inference-sh/skills@ai-image-generation

# FLUX models
npx skills add inference-sh/skills@flux-image

# Background removal
npx skills add inference-sh/skills@background-removal


Browse all image apps: belt app list --category image

Documentation
Running Apps - How to run apps via CLI
Image Generation Example - Complete image workflow guide
Apps Overview - Understanding the app ecosystem
Weekly Installs
298
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