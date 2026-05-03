---
title: nano-banana
url: https://skills.sh/kingbootoshi/nano-banana-2-skill/nano-banana
---

# nano-banana

skills/kingbootoshi/nano-banana-2-skill/nano-banana
nano-banana
Installation
$ npx skills add https://github.com/kingbootoshi/nano-banana-2-skill --skill nano-banana
SKILL.md
nano-banana

AI image generation CLI. Default model: Gemini 3.1 Flash Image Preview (Nano Banana 2).

/init - First-Time Setup

When the user says "init", "setup nano-banana", or "install nano-banana", run these commands to get the CLI tool on their machine. No sudo required.

Prerequisites: Bun must be installed. If not: curl -fsSL https://bun.sh/install | bash

# 1. Clone the repo
git clone https://github.com/kingbootoshi/nano-banana-2-skill.git ~/tools/nano-banana-2

# 2. Install dependencies
cd ~/tools/nano-banana-2 && bun install

# 3. Link globally (creates `nano-banana` command via Bun - no sudo)
cd ~/tools/nano-banana-2 && bun link

# 4. Set up API key
mkdir -p ~/.nano-banana
echo "GEMINI_API_KEY=<ask user for their key>" > ~/.nano-banana/.env


After init, the user can type nano-banana "prompt" from anywhere.

If bun link fails or the command is not found after linking, fall back to:

mkdir -p ~/.local/bin
ln -sf ~/tools/nano-banana-2/src/cli.ts ~/.local/bin/nano-banana
# Then ensure ~/.local/bin is on PATH:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc


Get a Gemini API key at: https://aistudio.google.com/apikey

Quick Reference
Command: nano-banana "prompt" [options]
Default: 1K resolution, Flash model, current directory
Core Options
Option	Default	Description
-o, --output	nano-gen-{timestamp}	Output filename (no extension)
-s, --size	1K	Image size: 512, 1K, 2K, or 4K
-a, --aspect	model default	Aspect ratio: 1:1, 16:9, 9:16, 4:3, 3:4, etc.
-m, --model	flash	Model: flash/nb2, pro/nb-pro, or any model ID
-d, --dir	current directory	Output directory
-r, --ref	-	Reference image (can use multiple times)
-t, --transparent	-	Generate on green screen, remove background (FFmpeg)
--api-key	-	Gemini API key (overrides env/file)
--costs	-	Show cost summary
Models
Alias	Model	Use When
flash, nb2	Gemini 3.1 Flash	Default. Fast, cheap (~$0.067/1K image)
pro, nb-pro	Gemini 3 Pro	Highest quality needed (~$0.134/1K image)
Sizes
Size	Cost (Flash)	Cost (Pro)
512	~$0.045	Flash only
1K	~$0.067	~$0.134
2K	~$0.101	~$0.201
4K	~$0.151	~$0.302
Aspect Ratios

Supported: 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 4:5, 5:4, 21:9

Use -a flag: nano-banana "cinematic scene" -a 16:9

Key Workflows
Basic Generation
nano-banana "minimal dashboard UI with dark theme"
nano-banana "cinematic landscape" -s 2K -a 16:9
nano-banana "quick concept sketch" -s 512

Model Selection
# Default (Flash - fast, cheap)
nano-banana "your prompt"

# Pro (highest quality)
nano-banana "detailed portrait" --model pro -s 2K

Reference Images (Style Transfer / Editing)
# Edit existing image
nano-banana "change the background to pure white" -r dark-ui.png -o light-ui

# Style transfer - multiple references
nano-banana "combine these two styles" -r style1.png -r style2.png -o combined

Transparent Assets
nano-banana "robot mascot character" -t -o mascot
nano-banana "pixel art treasure chest" -t -o chest


The -t flag automatically prompts the AI to generate on a green screen, then uses FFmpeg colorkey + despill to key out the background and remove green spill from edge pixels. Pixel-perfect transparency with no manual prompting needed.

Requires: brew install ffmpeg imagemagick

Exact Dimensions

To get a specific output dimension:

First -r flag: your reference/style image
Last -r flag: blank image in target dimensions
Include dimensions in prompt
nano-banana "pixel art character in style of first image, 256x256" -r style.png -r blank-256x256.png -o sprite

Reference Order Matters
First reference: primary style/content source
Additional references: secondary influences
Last reference: controls output dimensions (if using blank image trick)
Cost Tracking

Every generation is logged to ~/.nano-banana/costs.json. View summary:

nano-banana --costs

Use Cases
Landing page assets - product mockups, UI previews
Image editing - transform existing images with prompts
Style transfer - combine multiple reference images
Marketing materials - hero images, feature illustrations
UI iterations - quickly generate variations of designs
Transparent assets - icons, logos, mascots with no background
Game assets - sprites, backgrounds, characters
Video production - visual elements for video compositions
Prompt Examples
# UI mockups
nano-banana "clean SaaS dashboard with analytics charts, white background"

# Widescreen cinematic
nano-banana "cyberpunk cityscape at sunset" -a 16:9 -s 2K

# Product shots with Pro quality
nano-banana "premium software product hero image" --model pro

# Quick low-res concept
nano-banana "rough sketch of a robot" -s 512

# Dark mode UI
nano-banana "Premium SaaS chat interface, dark mode, minimal, Linear-style aesthetic"

# Game assets with transparency (green screen auto-prompted)
nano-banana "pixel art treasure chest" -t -o chest

# Portrait aspect ratio
nano-banana "mobile app onboarding screen" -a 9:16

API Key Setup

The CLI resolves the Gemini API key in this order:

--api-key flag
GEMINI_API_KEY environment variable
.env file in current directory
.env file next to the CLI script
~/.nano-banana/.env

Get a key at: https://aistudio.google.com/apikey

Weekly Installs
394
Repository
kingbootoshi/na…-2-skill
GitHub Stars
363
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykFail