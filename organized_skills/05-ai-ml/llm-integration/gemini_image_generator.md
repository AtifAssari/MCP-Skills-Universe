---
rating: ⭐⭐
title: gemini-image-generator
url: https://skills.sh/mkdev-me/claude-skills/gemini-image-generator
---

# gemini-image-generator

skills/mkdev-me/claude-skills/gemini-image-generator
gemini-image-generator
Installation
$ npx skills add https://github.com/mkdev-me/claude-skills --skill gemini-image-generator
SKILL.md
gemini-image-generator
Instructions

Use this skill to generate images using Google Gemini's image generation model. The skill supports:

Text-to-image generation from prompts
Image-to-image generation with a reference image
Multiple output sizes (1K, 2K, 4K)
Custom output paths

The API key must be set via the GEMINI_API_KEY environment variable.

Parameters
--prompt (required): The text prompt describing the image to generate
--output (required): Output file path for the generated image
--reference: Optional reference image for style/content guidance
--size: Image size - "1K", "2K", or "4K" (default: 4K)
Examples
Basic text-to-image generation
./scripts/generate.py --prompt "A serene mountain landscape at sunset" --output images/landscape.png

With reference image for style guidance
./scripts/generate.py --prompt "Same character but wearing a party hat" --reference images/character.png --output images/party.png

Different output size
./scripts/generate.py --prompt "Abstract art" --output art.png --size 2K

Setup

Before first use, set up the virtual environment:

cd scripts && python3 -m venv venv && ./venv/bin/pip install -r requirements.txt


Set your API key:

export GEMINI_API_KEY="your-api-key-here"

Weekly Installs
25
Repository
mkdev-me/claude-skills
GitHub Stars
34
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass