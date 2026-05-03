---
rating: ⭐⭐⭐
title: ocr
url: https://skills.sh/mr-shaper/opencode-skills-paddle-ocr/ocr
---

# ocr

skills/mr-shaper/opencode-skills-paddle-ocr/ocr
ocr
Installation
$ npx skills add https://github.com/mr-shaper/opencode-skills-paddle-ocr --skill ocr
SKILL.md
OCR Skill
Usage

To extract text from an image or PDF, run:

python3 "/Users/mrshaper/Library/Application Support/com.differentai.openwork/workspaces/starter/.opencode/skills/paddle-ocr/scripts/ocr.py" "/path/to/image.png"

Options
Option	Description
--prompt "text"	Custom prompt (e.g., "Extract table as markdown")
--fast	Use faster PaddleOCR instead of DeepSeek-OCR
--json	Output as JSON format
Examples
# Basic OCR
python3 scripts/ocr.py image.png

# Extract table as markdown
python3 scripts/ocr.py table.png --prompt "Extract this table as markdown"

# Fast mode
python3 scripts/ocr.py image.png --fast

# PDF OCR
python3 scripts/ocr.py document.pdf

Supported Formats

Images: PNG, JPG, JPEG, BMP, GIF, WEBP, TIFF Documents: PDF

Weekly Installs
339
Repository
mr-shaper/openc…ddle-ocr
GitHub Stars
1
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass