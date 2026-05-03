---
title: sprite-sheet-generator
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/sprite-sheet-generator
---

# sprite-sheet-generator

skills/dkyazzentwatwa/chatgpt-skills/sprite-sheet-generator
sprite-sheet-generator
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill sprite-sheet-generator
SKILL.md
Sprite Sheet Generator

Combine multiple images into optimized sprite sheets with CSS generation.

Features
Grid Layouts: Auto or custom grid arrangements
Smart Packing: Optimize sprite placement
CSS Generation: Auto-generate sprite CSS classes
Transparent Backgrounds: Preserve alpha channels
Padding/Margins: Control spacing between sprites
Batch Processing: Process multiple sprite sets
Quick Start
from sprite_sheet_generator import SpriteSheetGenerator

gen = SpriteSheetGenerator()
gen.add_images_from_dir('icons/')
gen.generate(output='sprites.png', grid=(4, 4))
gen.generate_css('sprites.css', class_prefix='icon')

CLI Usage
python sprite_sheet_generator.py --input icons/ --output sprites.png --grid 4x4 --css sprites.css

Dependencies
pillow>=10.0.0
Weekly Installs
81
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass