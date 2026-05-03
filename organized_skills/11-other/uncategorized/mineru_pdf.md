---
rating: ⭐⭐
title: mineru-pdf
url: https://skills.sh/kesslerio/mineru-pdf-parser-clawdbot-skill/mineru-pdf
---

# mineru-pdf

skills/kesslerio/mineru-pdf-parser-clawdbot-skill/mineru-pdf
mineru-pdf
Installation
$ npx skills add https://github.com/kesslerio/mineru-pdf-parser-clawdbot-skill --skill mineru-pdf
SKILL.md
MinerU PDF
Overview

Parse a PDF locally with MinerU (CPU). Default output is Markdown + JSON. Use tables/images only when requested.

Quick start (single PDF)
# Run from the skill directory
./scripts/mineru_parse.sh /path/to/file.pdf


Optional examples:

./scripts/mineru_parse.sh /path/to/file.pdf --format json
./scripts/mineru_parse.sh /path/to/file.pdf --tables --images

When to read references

If flags differ from your wrapper or you need advanced defaults (backend/method/device/threads/format mapping), read:

references/mineru-cli.md
Output conventions
Output root defaults to ./mineru-output/.
MinerU creates the per-document subfolder under the output root (e.g., ./mineru-output/<basename>/...).
Batching

Default is single-PDF parsing. Only implement batch folder parsing if explicitly requested.

Weekly Installs
87
Repository
kesslerio/miner…ot-skill
GitHub Stars
7
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass