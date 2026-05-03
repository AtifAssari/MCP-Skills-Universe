---
title: carousel-generator
url: https://skills.sh/drshailesh88/integrated_content_os/carousel-generator
---

# carousel-generator

skills/drshailesh88/integrated_content_os/carousel-generator
carousel-generator
Installation
$ npx skills add https://github.com/drshailesh88/integrated_content_os --skill carousel-generator
SKILL.md
Carousel Generator

Generate branded Instagram carousels (1080x1080px) from text content.

Quick Start
cd "/Users/shaileshsingh/integrated cowriting system/skills/cardiology/carousel-generator"
python tools/generate-carousel.py <input_file> <account> [options]

# Examples:
python tools/generate-carousel.py content.txt 1           # Account 1: @heartdocshailesh
python tools/generate-carousel.py content.txt 2           # Account 2: @dr.shailesh.singh
python tools/generate-carousel.py content.txt 1 -m 8      # Max 8 slides
python tools/generate-carousel.py content.txt 1 -o ~/out  # Custom output dir

Features
1080x1080px Instagram carousel slides
Brand colors (Deep Teal, Mist Aqua, Warm Coral)
Consistent footer with name and handle
Automatic text wrapping
Bullet point rendering
Title slides (teal background) + content slides (light background)
Input Formats
1. Plain Text with Markdown
# Main Title
Subtitle or intro

---

## Slide 2 Title
• Bullet point 1
• Bullet point 2

---

## Slide 3
Body text with automatic wrapping.

2. JSON Format
[
  {"title": "Title Slide", "body": "Subtitle", "type": "title"},
  {"title": "Content Slide", "body": "Body text", "type": "content"}
]

Output

PNG files in output/carousels/<name>/account-<n>/

Brand Specifications
Colors
COLORS = {
    'primary': '#207178',      # Deep Teal - titles, CTAs
    'secondary': '#E4F1EF',    # Mist Aqua - backgrounds
    'accent': '#F28C81',       # Warm Coral - bullets, highlights
    'neutral_light': '#F8F9FA', # Off-White - alt backgrounds
    'neutral_dark': '#333333',  # Charcoal - body text
    'alert': '#E63946'         # Heart Red - emphasis
}

Accounts
Account 1: @heartdocshailesh
Account 2: @dr.shailesh.singh
Typography
Font: Inter (Bold, SemiBold, Regular, Medium)
Fallback: Helvetica (macOS) -> System default
Dependencies
Python 3.11+
Pillow (PIL) for image generation
No API keys required (runs locally)
pip install pillow

Note

This skill is called by the content-os orchestrator for carousel generation. You can also use it standalone for quick carousel creation.

Weekly Installs
26
Repository
drshailesh88/in…ntent_os
GitHub Stars
3
First Seen
8 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass