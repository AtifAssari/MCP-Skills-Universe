---
title: xiaohongshu-cover-generator
url: https://skills.sh/freestylefly/xiaohongshu-skills/xiaohongshu-cover-generator
---

# xiaohongshu-cover-generator

skills/freestylefly/xiaohongshu-skills/xiaohongshu-cover-generator
xiaohongshu-cover-generator
Installation
$ npx skills add https://github.com/freestylefly/xiaohongshu-skills --skill xiaohongshu-cover-generator
Summary

Generate Xiaohongshu-style cover images from user topics with automatic formatting.

Accepts a topic as input and produces vertically-oriented 3:4 cover images optimized for mobile viewing
Requires API key from https://api.canghe.ai/ (via CANGHE_API_KEY environment variable or direct argument)
Saves generated images to the current working directory with timestamped filenames (xiaohongshu-cover-{timestamp}.png)
Applies clean, youthful aesthetic with automatic watermark removal and readable text sizing
SKILL.md
Xiaohongshu Cover Generator

This skill generates Xiaohongshu-style cover images based on user-provided topics.

Usage

When a user requests a Xiaohongshu cover image:

Confirm the topic with the user if not clear
Check for API key (CANGHE_API_KEY environment variable or ask user to provide it)
Run the generation script with the topic
The image will be saved to the current working directory with filename format: xiaohongshu-cover-{timestamp}.png
Running the Script

The script is located at scripts/handler.ts and requires:

Topic (required): The subject for the cover image
API Key (required): Either via environment variable CANGHE_API_KEY or passed as argument

Execute with:

cd ~/.codebuddy/skills/xiaohongshu-cover-generator
npx tsx scripts/handler.ts "<topic>" "<api-key-optional>"


Or with environment variable:

cd ~/.codebuddy/skills/xiaohongshu-cover-generator
CANGHE_API_KEY="your-api-key" npx tsx scripts/handler.ts "<topic>"

API Key

Users need a valid API key from https://api.canghe.ai/

If the API key is missing or invalid, provide the user with clear instructions to obtain one.

Output

The generated image will be saved to the directory where the skill was invoked (current working directory), not the skill's directory. The filename format is xiaohongshu-cover-{timestamp}.png where timestamp is in milliseconds.

Style Specifications

The generated images follow these specifications:

Aspect ratio: 3:4 (vertical, mobile-friendly)
Style: Clean, refined, youthful aesthetic
Automatic removal of watermarks and logos
High-quality output suitable for mobile viewing
Text should be clear and readable with appropriate sizing
Weekly Installs
1.3K
Repository
freestylefly/xi…u-skills
GitHub Stars
82
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail