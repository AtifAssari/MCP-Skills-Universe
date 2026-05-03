---
title: image-enhancement-suite
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/image-enhancement-suite
---

# image-enhancement-suite

skills/dkyazzentwatwa/chatgpt-skills/image-enhancement-suite
image-enhancement-suite
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill image-enhancement-suite
SKILL.md
Image Enhancement Suite

Use this as the primary image toolkit. It now includes the repo's background removal, metadata, comparison, filter, palette, icon, collage, and sprite helpers.

Use This For
Resize, crop, watermark, compress, and format conversion
Background removal and quick cleanup
Image comparisons and metadata inspection
Palette extraction, icon generation, collages, and sprite sheet assembly
Workflow
Start with scripts/image_enhancer.py for general-purpose image work.
Use focused helpers when the task is narrow:
background_remover.py
image_comparison.py
image_metadata.py
image_filter.py
color_palette_extractor.py
icon_generator.py
collage_maker.py
sprite_sheet_generator.py
Prefer batch operations only when the same transforms should be applied consistently.
Guardrails
Preserve originals when quality tradeoffs are uncertain.
Say when a background removal or smart crop is heuristic, not exact.
Use vector output or SVG-oriented tooling when the request is really illustration, not raster editing.
Weekly Installs
135
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass