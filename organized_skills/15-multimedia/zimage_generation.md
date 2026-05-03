---
rating: ⭐⭐⭐
title: zimage-generation
url: https://skills.sh/toolsai/free-zimage-skills/zimage-generation
---

# zimage-generation

skills/toolsai/free-zimage-skills/zimage-generation
zimage-generation
Installation
$ npx skills add https://github.com/toolsai/free-zimage-skills --skill zimage-generation
Summary

Generate images using ModelScope's Z-Image API with simple command-line prompts.

Supports three API key configuration methods: hardcoded in script, command-line argument, or .env file in the scripts folder
Accepts optional parameters for custom output filename and alternative model IDs
Requires Python 3 with requests library and a ModelScope account with Alibaba Cloud binding for API access
Returns 401 errors if the account lacks proper Alibaba Cloud setup; users must bind their account via ModelScope dashboard
SKILL.md
Z-Image Generation Skill

This skill allows you to generate images using the Z-Image model via the ModelScope Inference API.

When to Use

Use this skill when:

The user requests to generate an image using "Zimage", "zimage:", or "ModelScope".
The user inputs a command like zimage: <prompt> or zimage <prompt>.
The user wants to use their configured ModelScope API key for image generation.
Usage

The skill provides a Python script scripts/generate_zimage.py to handle the API interaction.

Prerequisites
Python 3 with requests installed.
API Key Setup (Choose one):
Method A (Easiest for beginners): Open scripts/generate_zimage.py and paste your key into the DEFAULT_API_KEY variable at the top.
Method B (Temporary): Pass via command line: --api-key your_token
Method C (Recommended Project Setup): Create a new text file named .env in the same folder as the script (scripts/).
Content of the file should be: MODELSCOPE_API_TOKEN="your_key_here"
Commands

To generate an image:

# If you used Method A (pasted key in file):
python3 /Users/promptcase/.gemini/antigravity/skills/zimage-generation/scripts/generate_zimage.py "Your descriptive prompt here"

# If you prefer command line (Method B):
python3 /Users/promptcase/.gemini/antigravity/skills/zimage-generation/scripts/generate_zimage.py "Your prompt" --api-key "your_key"


Arguments:

prompt: The text description of the image (required).
--output, -o: Specify output filename (optional).
--model: Specify a different model ID (optional).
--api-key: API key (if not set in file or environment).
API Verification Note

If the script returns a 401 error mentioning "bind your Alibaba Cloud account", notify the user that they must log in to ModelScope (https://modelscope.cn/my/account) and bind their Alibaba Cloud account to enable API access. This is a one-time setup required by the platform.

Example
# To generate a cyberpunk city
python3 /Users/mattchan/.gemini/antigravity/skills/zimage-generation/scripts/generate_zimage.py "cyberpunk city, neon lights, rainy street, high detail"

Weekly Installs
637
Repository
toolsai/free-zi…e-skills
GitHub Stars
12
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail