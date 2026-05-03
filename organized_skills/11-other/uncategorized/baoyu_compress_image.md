---
rating: ⭐⭐⭐
title: baoyu-compress-image
url: https://skills.sh/questnova502/claude-skills-sync/baoyu-compress-image
---

# baoyu-compress-image

skills/questnova502/claude-skills-sync/baoyu-compress-image
baoyu-compress-image
Installation
$ npx skills add https://github.com/questnova502/claude-skills-sync --skill baoyu-compress-image
SKILL.md
Image Compressor

Cross-platform image compression with WebP default output, PNG-to-PNG support, preferring system tools with Sharp fallback.

Script Directory

Important: All scripts are located in the scripts/ subdirectory of this skill.

Agent Execution Instructions:

Determine this SKILL.md file's directory path as SKILL_DIR
Script path = ${SKILL_DIR}/scripts/<script-name>.ts
Replace all ${SKILL_DIR} in this document with the actual path

Script Reference:

Script	Purpose
scripts/main.ts	CLI entry point for image compression
Quick Start
# Compress to WebP (default)
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png

# Keep original format (PNG → PNG)
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png --format png

# Custom quality
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png -q 75

# Process directory
npx -y bun ${SKILL_DIR}/scripts/main.ts ./images/ -r

Commands
Single File Compression
# Basic (converts to WebP, replaces original)
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png

# Custom output path
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png -o compressed.webp

# Keep original file
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png --keep

# Custom quality (0-100, default: 80)
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png -q 75

# Keep original format
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png -f png

Directory Processing
# Process all images in directory
npx -y bun ${SKILL_DIR}/scripts/main.ts ./images/

# Recursive processing
npx -y bun ${SKILL_DIR}/scripts/main.ts ./images/ -r

# With custom quality
npx -y bun ${SKILL_DIR}/scripts/main.ts ./images/ -r -q 75

Output Formats
# Plain text (default)
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png

# JSON output
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png --json

Options
Option	Short	Description	Default
<input>		Input file or directory	Required
--output <path>	-o	Output path	Same path, new extension
--format <fmt>	-f	webp, png, jpeg	webp
--quality <n>	-q	Quality 0-100	80
--keep	-k	Keep original file	false
--recursive	-r	Process directories recursively	false
--json		JSON output	false
--help	-h	Show help	
Compressor Selection

Priority order (auto-detected):

sips (macOS built-in, WebP support since macOS 11)
cwebp (Google's official WebP tool)
ImageMagick (convert command)
Sharp (npm package, auto-installed by Bun)

The skill automatically selects the best available compressor.

Output Format
Text Mode (default)
image.png → image.webp (245KB → 89KB, 64% reduction)

JSON Mode
{
  "input": "image.png",
  "output": "image.webp",
  "inputSize": 250880,
  "outputSize": 91136,
  "ratio": 0.36,
  "compressor": "sips"
}

Directory JSON Mode
{
  "files": [...],
  "summary": {
    "totalFiles": 10,
    "totalInputSize": 2508800,
    "totalOutputSize": 911360,
    "ratio": 0.36,
    "compressor": "sips"
  }
}

Examples
Compress single image
npx -y bun ${SKILL_DIR}/scripts/main.ts photo.png
# photo.png → photo.webp (1.2MB → 340KB, 72% reduction)

Compress with custom quality
npx -y bun ${SKILL_DIR}/scripts/main.ts photo.png -q 60
# photo.png → photo.webp (1.2MB → 280KB, 77% reduction)

Keep original format
npx -y bun ${SKILL_DIR}/scripts/main.ts screenshot.png -f png --keep
# screenshot.png → screenshot-compressed.png (500KB → 380KB, 24% reduction)

Process entire directory
npx -y bun ${SKILL_DIR}/scripts/main.ts ./screenshots/ -r
# Processed 15 files: 12.5MB → 4.2MB (66% reduction)

Get JSON for scripting
npx -y bun ${SKILL_DIR}/scripts/main.ts image.png --json | jq '.ratio'

Extension Support

Custom configurations via EXTEND.md.

Check paths (priority order):

.baoyu-skills/baoyu-compress-image/EXTEND.md (project)
~/.baoyu-skills/baoyu-compress-image/EXTEND.md (user)

If found, load before workflow. Extension content overrides defaults.

Weekly Installs
9
Repository
questnova502/cl…lls-sync
GitHub Stars
3
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass