---
title: ai-image-generation
url: https://skills.sh/inference-sh/skills/ai-image-generation
---

# ai-image-generation

skills/inference-sh/skills/ai-image-generation
ai-image-generation
Originally frominfsh-skills/skills
Installation
$ npx skills add https://github.com/inference-sh/skills --skill ai-image-generation
Summary

Generate images with 50+ AI models including FLUX, Gemini, Grok, and Seedream via inference.sh CLI.

Supports text-to-image, image-to-image, inpainting, LoRA fine-tuning, image editing, upscaling, and text rendering across multiple model families
Models range from ultra-fast budget options (FLUX Klein at $0.0001/image) to high-fidelity 4K outputs (ImagineArt, Seedream 4.5)
Includes Google Gemini, xAI Grok, ByteDance Seedream, and Pruna P-Image variants optimized for speed, quality, or cost
Requires inference.sh CLI (infsh) installation and authentication; browse available models with infsh app list --category image
SKILL.md
AI Image Generation

Generate images with 50+ AI models via inference.sh CLI.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

# Generate an image with FLUX
belt app run falai/flux-dev-lora --input '{"prompt": "a cat astronaut in space"}'

Available Models
Model	App ID	Best For
GPT-Image-2	openai/gpt-image-2	Text-to-image, editing, inpainting
FLUX Dev LoRA	falai/flux-dev-lora	High quality with custom styles
FLUX.2 Klein LoRA	falai/flux-2-klein-lora	Fast with LoRA support (4B/9B)
P-Image	pruna/p-image	Fast, economical, multiple aspects
P-Image-LoRA	pruna/p-image-lora	Fast with preset LoRA styles
P-Image-Edit	pruna/p-image-edit	Fast image editing
Gemini 3 Pro	google/gemini-3-pro-image-preview	Google's latest
Gemini 2.5 Flash	google/gemini-2-5-flash-image	Fast Google model
Grok Imagine	xai/grok-imagine-image	xAI's model, multiple aspects
Seedream 4.5	bytedance/seedream-4-5	2K-4K cinematic quality
Seedream 4.0	bytedance/seedream-4-0	High quality 2K-4K
Seedream 3.0	bytedance/seedream-3-0-t2i	Accurate text rendering
Reve	falai/reve	Natural language editing, text rendering
ImagineArt 1.5 Pro	falai/imagine-art-1-5-pro-preview	Ultra-high-fidelity 4K
FLUX Klein 4B	pruna/flux-klein-4b	Ultra-cheap ($0.0001/image)
Topaz Upscaler	falai/topaz-image-upscaler	Professional upscaling
Browse All Image Apps
belt app list --category image

Examples
GPT-Image-2
belt app run openai/gpt-image-2 --input '{
  "prompt": "professional product photo of sneakers, studio lighting",
  "quality": "high"
}'

GPT-Image-2 Editing
belt app run openai/gpt-image-2 --input '{
  "prompt": "change the background to a beach at sunset",
  "images": ["https://your-image.jpg"]
}'

Text-to-Image with FLUX
belt app run falai/flux-dev-lora --input '{
  "prompt": "professional product photo of a coffee mug, studio lighting"
}'

Fast Generation with FLUX Klein
belt app run falai/flux-2-klein-lora --input '{"prompt": "sunset over mountains"}'

Google Gemini 3 Pro
belt app run google/gemini-3-pro-image-preview --input '{
  "prompt": "photorealistic landscape with mountains and lake"
}'

Grok Imagine
belt app run xai/grok-imagine-image --input '{
  "prompt": "cyberpunk city at night",
  "aspect_ratio": "16:9"
}'

Reve (with Text Rendering)
belt app run falai/reve --input '{
  "prompt": "A poster that says HELLO WORLD in bold letters"
}'

Seedream 4.5 (4K Quality)
belt app run bytedance/seedream-4-5 --input '{
  "prompt": "cinematic portrait of a woman, golden hour lighting"
}'

Image Upscaling
belt app run falai/topaz-image-upscaler --input '{"image_url": "https://..."}'

Stitch Multiple Images
belt app run infsh/stitch-images --input '{
  "images": ["https://img1.jpg", "https://img2.jpg"],
  "direction": "horizontal"
}'

Related Skills
# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# Pruna P-Image (fast & economical)
npx skills add inference-sh/skills@p-image

# GPT-Image-2 (OpenAI)
npx skills add inference-sh/skills@gpt-image

# FLUX-specific skill
npx skills add inference-sh/skills@flux-image

# Upscaling & enhancement
npx skills add inference-sh/skills@image-upscaling

# Background removal
npx skills add inference-sh/skills@background-removal

# Video generation
npx skills add inference-sh/skills@ai-video-generation

# AI avatars from images
npx skills add inference-sh/skills@ai-avatar-video


Browse all apps: belt app list

Documentation
Running Apps - How to run apps via CLI
Image Generation Example - Complete image generation guide
Apps Overview - Understanding the app ecosystem
Weekly Installs
758
Repository
inference-sh/skills
GitHub Stars
395
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn