---
title: agent-tools
url: https://skills.sh/inference-sh/skills/agent-tools
---

# agent-tools

skills/inference-sh/skills/agent-tools
agent-tools
Originally frominfsh-skills/skills
Installation
$ npx skills add https://github.com/inference-sh/skills --skill agent-tools
Summary

Access 150+ cloud-based AI apps via CLI—image generation, video creation, LLMs, search, 3D modeling, and Twitter automation.

Supports major models including FLUX, Veo, Claude, Gemini, Grok, Seedance, OmniHuman, Tavily, and Exa with no local GPU required
Automatic local file upload for images, audio, and video inputs; run apps synchronously or asynchronously with task status tracking
Covers six capability categories: image generation, video generation, LLM inference, web search, 3D modeling, and Twitter/X automation
CLI commands for app discovery, filtering by category, generating sample inputs, and running tasks with optional output waiting
SKILL.md
inference.sh

Run 250+ AI apps in the cloud with a simple CLI. No GPU required.

Install CLI
curl -fsSL https://cli.inference.sh | sh
belt login


What does the installer do? The install script detects your OS and architecture, downloads the correct binary from dist.inference.sh, verifies its SHA-256 checksum, and places it in your PATH. That's it — no elevated permissions, no background processes, no telemetry. If you have cosign installed, the installer also verifies the Sigstore signature automatically.

Manual install (if you prefer not to pipe to sh):

# Download the binary and checksums
curl -LO https://dist.inference.sh/cli/checksums.txt
curl -LO $(curl -fsSL https://dist.inference.sh/cli/manifest.json | grep -o '"url":"[^"]*"' | grep $(uname -s | tr A-Z a-z)-$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/') | head -1 | cut -d'"' -f4)
# Verify checksum
sha256sum -c checksums.txt --ignore-missing
# Extract and install
tar -xzf inferencesh-cli-*.tar.gz
mv inferencesh-cli-* ~/.local/bin/inferencesh

Quick Examples
# Generate an image
belt app run falai/flux-dev-lora --input '{"prompt": "a cat astronaut"}'

# Generate a video
belt app run google/veo-3-1-fast --input '{"prompt": "drone over mountains"}'

# Call Claude
belt app run openrouter/claude-sonnet-45 --input '{"prompt": "Explain quantum computing"}'

# Web search
belt app run tavily/search-assistant --input '{"query": "latest AI news"}'

# Post to Twitter
belt app run x/post-tweet --input '{"text": "Hello from AI!"}'

# Generate 3D model
belt app run infsh/rodin-3d-generator --input '{"prompt": "a wooden chair"}'

Local File Uploads

The CLI automatically uploads local files when you provide a path instead of a URL:

# Upscale a local image
belt app run falai/topaz-image-upscaler --input '{"image": "/path/to/photo.jpg", "upscale_factor": 2}'

# Image-to-video from local file
belt app run falai/wan-2-5-i2v --input '{"image": "./my-image.png", "prompt": "make it move"}'

# Avatar with local audio and image
belt app run bytedance/omnihuman-1-5 --input '{"audio": "/path/to/speech.mp3", "image": "/path/to/face.jpg"}'

# Post tweet with local media
belt app run x/post-create --input '{"text": "Check this out!", "media": "./screenshot.png"}'

Commands
Task	Command
List all apps	belt app list
Search apps	belt app list --search "flux"
Filter by category	belt app list --category image
Get app details	belt app get google/veo-3-1-fast
Generate sample input	belt app sample google/veo-3-1-fast --save input.json
Run app	belt app run google/veo-3-1-fast --input input.json
Run without waiting	belt app run <app> --input input.json --no-wait
Check task status	belt task get <task-id>
What's Available
Category	Examples
Image	FLUX, Gemini 3 Pro, Grok Imagine, Seedream 4.5, Reve, Topaz Upscaler
Video	Veo 3.1, Seedance 1.5, Wan 2.5, OmniHuman, Fabric, HunyuanVideo Foley
LLMs	Claude Opus/Sonnet/Haiku, Gemini 3 Pro, Kimi K2, GLM-4, any OpenRouter model
Search	Tavily Search, Tavily Extract, Exa Search, Exa Answer, Exa Extract
3D	Rodin 3D Generator
Twitter/X	post-tweet, post-create, dm-send, user-follow, post-like, post-retweet
Utilities	Media merger, caption videos, image stitching, audio extraction
Related Skills
# Image generation (FLUX, Gemini, Grok, Seedream)
npx skills add inference-sh/skills@ai-image-generation

# Video generation (Veo, Seedance, Wan, OmniHuman)
npx skills add inference-sh/skills@ai-video-generation

# LLMs (Claude, Gemini, Kimi, GLM via OpenRouter)
npx skills add inference-sh/skills@llm-models

# Web search (Tavily, Exa)
npx skills add inference-sh/skills@web-search

# AI avatars & lipsync (OmniHuman, Fabric, PixVerse)
npx skills add inference-sh/skills@ai-avatar-video

# Twitter/X automation
npx skills add inference-sh/skills@twitter-automation

# Model-specific
npx skills add inference-sh/skills@flux-image
npx skills add inference-sh/skills@google-veo

# Utilities
npx skills add inference-sh/skills@image-upscaling
npx skills add inference-sh/skills@background-removal

Reference Files
Authentication & Setup
Discovering Apps
Running Apps
CLI Reference
Documentation
Agent Skills Overview - The open standard for AI capabilities
Getting Started - Introduction to inference.sh
What is inference.sh? - Platform overview
Apps Overview - Understanding the app ecosystem
CLI Setup - Installing the CLI
Workflows vs Agents - When to use each
Why Agent Runtimes Matter - Runtime benefits
Weekly Installs
694
Repository
inference-sh/skills
GitHub Stars
395
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn