---
title: slides-grab-export
url: https://skills.sh/vkehfdl1/slides-grab/slides-grab-export
---

# slides-grab-export

skills/vkehfdl1/slides-grab/slides-grab-export
slides-grab-export
Installation
$ npx skills add https://github.com/vkehfdl1/slides-grab --skill slides-grab-export
SKILL.md
slides-grab Export Skill (Codex)

Use this only after the user approves design output.

Goal

Convert reviewed slide HTML into PDF or per-slide PNG reliably, and into experimental / unstable PPTX/Figma outputs on a best-effort basis.

Inputs
Approved <slides-dir>/slide-*.html
Optional output path settings
Outputs
Presentation artifact (.pdf, .png per slide, or .pptx)
Workflow
Confirm user approval for conversion.
Pick the right primary target:
Card-news / Instagram-style decks → slides-grab png --slides-dir <path> --slide-mode card-news --resolution 2160p (see slides-grab-card-news).
Widescreen slide decks → slides-grab pdf --slides-dir <path> --output <name>.pdf.
When per-slide raster output is needed (card news, social posts, thumbnails):
slides-grab png --slides-dir <path> --output-dir <path>/out-png --resolution 2160p
Add --slide-mode card-news for 1:1 cards.
If the user also wants a PDF deck:
slides-grab pdf --slides-dir <path> --output <name>.pdf
Add --slide-mode card-news when the deck is square.
If the user wants PPTX (experimental / unstable):
slides-grab convert --slides-dir <path> --output <name>.pptx
If the user wants Figma-importable PPTX (experimental / unstable):
slides-grab figma --slides-dir <path> --output <name>-figma.pptx
Report success/failure with actionable errors.
Rules
Do not modify slide content during conversion stage unless explicitly requested.
If conversion fails, diagnose and fix root causes in source HTML/CSS.
Always tell the user that PPTX and Figma export are experimental / unstable and may require manual cleanup.
Use the packaged CLI and bundled references only; do not depend on unpublished agent-specific files.
Reference

For detailed conversion behavior and tools, use:

references/export-rules.md
references/pptx-skill-reference.md — archived full PPTX workflow guidance
references/html2pptx.md — archived converter usage guide
references/ooxml.md — archived OOXML reference
Weekly Installs
10
Repository
vkehfdl1/slides-grab
GitHub Stars
641
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass