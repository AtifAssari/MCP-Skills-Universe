---
rating: ⭐⭐⭐
title: sci-ppt
url: https://skills.sh/shzhao27208/aut_sci_write/sci-ppt
---

# sci-ppt

skills/shzhao27208/aut_sci_write/sci-ppt
sci-ppt
Installation
$ npx skills add https://github.com/shzhao27208/aut_sci_write --skill sci-ppt
SKILL.md
Sci-PPT — Academic Auto-PPT Agent

A specialized tool for generating professional academic presentations directly from paper content or structured outlines.

Core Behavioral Rules (The 12 Laws)
Format: Use 1. Title for chapters and - Point for bullets.
Markdown: 🚫 DO NOT use ## for slide titles; it is not recognized by the parser.
Innovation: Identify the core innovation of the paper and highlight it in Red.
Imagery: Use HD extraction (600 DPI) for figures; minimum width >= 300px.
No Scrapping: 🚫 PROHIBITED to scrap low-quality bitmaps from PDF streams.
Formulas: Render LaTeX formulas as high-quality transparent PNGs.
Transparency: All generated formula/media assets must have transparent backgrounds.
Feedback: Inform the user if an operation (like PDF parsing) will take >10 seconds.
Final Output: 🚫 DO NOT output intermediate Markdown; generate and provide the .pptx directly.
Colors: Use #1E3A5F (Primary Blue) and #EE0000 (Highlight Red).
Layout: Ensure zero text-overflow or figure-text overlap.
Professionalism: Keep communication brief and technical; skip AI pleasantries.
Usage
Simple Text Input
from aut_sci_ppt import create_ppt

create_ppt("""
主题：[Title]
申请人：[Name]
1. [Section Title]
- [Content]
""", "output.pptx")

PDF to PPT (Academic Workflow)
from aut_sci_ppt import auto_generate_ppt

output = auto_generate_ppt("paper.pdf", author="张三", advisor="李教授")

Environment Variables
MOONSHOT_API_KEY (optional): Used for Chinese translation in PDF-to-PPT workflow. If not set, content is kept in original language.
Network access required for LaTeX formula rendering (via codecogs.com).
© License & Copyright

Aut_Sci_Write — Autonomous Scientific Writer

Author: Shuo Zhao
License: MIT License
Copyright: © 2026 Shuo Zhao. All rights reserved.
Original Work: This is an original work created by the author. No reproduction, redistribution, or commercial use without explicit permission. Permission is hereby granted, free of charge, to any person obtaining a copy of this software... (See the LICENSE file in the root directory for the full MIT terms.)
This skill is part of the Aut_Sci_Write suite. For full license terms, see the LICENSE file in the project root.
Weekly Installs
33
Repository
shzhao27208/aut…ci_write
GitHub Stars
37
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn