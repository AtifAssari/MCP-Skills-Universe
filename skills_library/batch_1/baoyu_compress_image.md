---
title: baoyu-compress-image
url: https://skills.sh/jimliu/baoyu-skills/baoyu-compress-image
---

# baoyu-compress-image

skills/jimliu/baoyu-skills/baoyu-compress-image
baoyu-compress-image
Installation
$ npx skills add https://github.com/jimliu/baoyu-skills --skill baoyu-compress-image
Summary

Compresses images to WebP or PNG with automatic tool selection based on system availability.

Supports WebP (default), PNG, and JPEG output formats with configurable quality (0–100, default 80)
Automatically selects best available compression tool: sips, cwebp, ImageMagick, or Sharp
Processes single files or directories recursively with options to keep originals or replace in-place
Customizable via EXTEND.md configuration files at project, user home, or XDG config locations
SKILL.md
Image Compressor

Compresses images using best available tool (sips → cwebp → ImageMagick → Sharp).

Script Directory

Scripts in scripts/ subdirectory. {baseDir} = this SKILL.md's directory path. Resolve ${BUN_X} runtime: if bun installed → bun; if npx available → npx -y bun; else suggest installing bun. Replace {baseDir} and ${BUN_X} with actual values.

Script	Purpose
scripts/main.ts	Image compression CLI
Preferences (EXTEND.md)

Check EXTEND.md in priority order — the first one found wins:

Priority	Path	Scope
1	.baoyu-skills/baoyu-compress-image/EXTEND.md	Project
2	${XDG_CONFIG_HOME:-$HOME/.config}/baoyu-skills/baoyu-compress-image/EXTEND.md	XDG
3	$HOME/.baoyu-skills/baoyu-compress-image/EXTEND.md	User home

If none found, use defaults.

EXTEND.md supports: Default format, default quality, keep-original preference.

Usage
${BUN_X} {baseDir}/scripts/main.ts <input> [options]

Options
Option	Short	Description	Default
<input>		File or directory	Required
--output	-o	Output path	Same path, new ext
--format	-f	webp, png, jpeg	webp
--quality	-q	Quality 0-100	80
--keep	-k	Keep original	false
--recursive	-r	Process subdirs	false
--json		JSON output	false
Examples
# Single file → WebP (replaces original)
${BUN_X} {baseDir}/scripts/main.ts image.png

# Keep PNG format
${BUN_X} {baseDir}/scripts/main.ts image.png -f png --keep

# Directory recursive
${BUN_X} {baseDir}/scripts/main.ts ./images/ -r -q 75

# JSON output
${BUN_X} {baseDir}/scripts/main.ts image.png --json


Output:

image.png → image.webp (245KB → 89KB, 64% reduction)

Extension Support

Custom configurations via EXTEND.md. See Preferences section for paths and supported options.

Weekly Installs
16.7K
Repository
jimliu/baoyu-skills
GitHub Stars
16.9K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass