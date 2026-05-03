---
title: nano-banana-pro
url: https://skills.sh/intellectronica/agent-skills/nano-banana-pro
---

# nano-banana-pro

skills/intellectronica/agent-skills/nano-banana-pro
nano-banana-pro
Installation
$ npx skills add https://github.com/intellectronica/agent-skills --skill nano-banana-pro
Summary

Text-to-image generation and image-to-image editing via Google's Gemini 3 Pro Image API.

Supports both new image generation from text prompts and editing of existing images with instruction-based modifications
Configurable output resolution: 1K (default), 2K, or 4K for high-resolution results
Automatically detects API key from --api-key argument or GEMINI_API_KEY environment variable
Saves PNG output to the user's current working directory with timestamped filenames
SKILL.md
Nano Banana Pro Image Generation & Editing

Generate new images or edit existing ones using Google's Nano Banana Pro API (Gemini 3 Pro Image).

Usage

Run the script using absolute path (do NOT cd to skill directory first):

Generate new image:

uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py --prompt "your image description" --filename "output-name.png" [--resolution 1K|2K|4K] [--api-key KEY]


Edit existing image:

uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py --prompt "editing instructions" --filename "output-name.png" --input-image "path/to/input.png" [--resolution 1K|2K|4K] [--api-key KEY]


Important: Always run from the user's current working directory so images are saved where the user is working, not in the skill directory.

Resolution Options

The Gemini 3 Pro Image API supports three resolutions (uppercase K required):

1K (default) - ~1024px resolution
2K - ~2048px resolution
4K - ~4096px resolution

Map user requests to API parameters:

No mention of resolution → 1K
"low resolution", "1080", "1080p", "1K" → 1K
"2K", "2048", "normal", "medium resolution" → 2K
"high resolution", "high-res", "hi-res", "4K", "ultra" → 4K
API Key

The script checks for API key in this order:

--api-key argument (use if user provided key in chat)
GEMINI_API_KEY environment variable

If neither is available, the script exits with an error message.

Filename Generation

Generate filenames with the pattern: yyyy-mm-dd-hh-mm-ss-name.png

Format: {timestamp}-{descriptive-name}.png

Timestamp: Current date/time in format yyyy-mm-dd-hh-mm-ss (24-hour format)
Name: Descriptive lowercase text with hyphens
Keep the descriptive part concise (1-5 words typically)
Use context from user's prompt or conversation
If unclear, use random identifier (e.g., x9k2, a7b3)

Examples:

Prompt "A serene Japanese garden" → 2025-11-23-14-23-05-japanese-garden.png
Prompt "sunset over mountains" → 2025-11-23-15-30-12-sunset-mountains.png
Prompt "create an image of a robot" → 2025-11-23-16-45-33-robot.png
Unclear context → 2025-11-23-17-12-48-x9k2.png
Image Editing

When the user wants to modify an existing image:

Check if they provide an image path or reference an image in the current directory
Use --input-image parameter with the path to the image
The prompt should contain editing instructions (e.g., "make the sky more dramatic", "remove the person", "change to cartoon style")
Common editing tasks: add/remove elements, change style, adjust colors, blur background, etc.
Prompt Handling

For generation: Pass user's image description as-is to --prompt. Only rework if clearly insufficient.

For editing: Pass editing instructions in --prompt (e.g., "add a rainbow in the sky", "make it look like a watercolor painting")

Preserve user's creative intent in both cases.

Output
Saves PNG to current directory (or specified path if filename includes directory)
Script outputs the full path to the generated image
Do not read the image back - just inform the user of the saved path
Examples

Generate new image:

uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py --prompt "A serene Japanese garden with cherry blossoms" --filename "2025-11-23-14-23-05-japanese-garden.png" --resolution 4K


Edit existing image:

uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py --prompt "make the sky more dramatic with storm clouds" --filename "2025-11-23-14-25-30-dramatic-sky.png" --input-image "original-photo.jpg" --resolution 2K

Weekly Installs
2.2K
Repository
intellectronica…t-skills
GitHub Stars
254
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail