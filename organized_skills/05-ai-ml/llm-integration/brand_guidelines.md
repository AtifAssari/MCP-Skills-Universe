---
rating: ⭐⭐⭐
title: brand-guidelines
url: https://skills.sh/composiohq/awesome-claude-skills/brand-guidelines
---

# brand-guidelines

skills/composiohq/awesome-claude-skills/brand-guidelines
brand-guidelines
Originally fromanthropics/skills
Installation
$ npx skills add https://github.com/composiohq/awesome-claude-skills --skill brand-guidelines
Summary

Apply Anthropic's official brand colors, typography, and visual identity to artifacts.

Includes six brand colors (dark, light, mid/light gray, orange, blue, green) with RGB values for precise matching across platforms
Automatically applies Poppins font to headings (24pt+) and Lora font to body text, with fallback to Arial and Georgia if custom fonts unavailable
Smart color selection adapts text and accent colors based on background for readability and visual hierarchy
Works with system-installed fonts; no additional installation required for basic functionality
SKILL.md
Anthropic Brand Styling
Overview

To access Anthropic's official brand identity and style resources, use this skill.

Keywords: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Anthropic brand, visual formatting, visual design

Brand Guidelines
Colors

Main Colors:

Dark: #141413 - Primary text and dark backgrounds
Light: #faf9f5 - Light backgrounds and text on dark
Mid Gray: #b0aea5 - Secondary elements
Light Gray: #e8e6dc - Subtle backgrounds

Accent Colors:

Orange: #d97757 - Primary accent
Blue: #6a9bcc - Secondary accent
Green: #788c5d - Tertiary accent
Typography
Headings: Poppins (with Arial fallback)
Body Text: Lora (with Georgia fallback)
Note: Fonts should be pre-installed in your environment for best results
Features
Smart Font Application
Applies Poppins font to headings (24pt and larger)
Applies Lora font to body text
Automatically falls back to Arial/Georgia if custom fonts unavailable
Preserves readability across all systems
Text Styling
Headings (24pt+): Poppins font
Body text: Lora font
Smart color selection based on background
Preserves text hierarchy and formatting
Shape and Accent Colors
Non-text shapes use accent colors
Cycles through orange, blue, and green accents
Maintains visual interest while staying on-brand
Technical Details
Font Management
Uses system-installed Poppins and Lora fonts when available
Provides automatic fallback to Arial (headings) and Georgia (body)
No font installation required - works with existing system fonts
For best results, pre-install Poppins and Lora fonts in your environment
Color Application
Uses RGB color values for precise brand matching
Applied via python-pptx's RGBColor class
Maintains color fidelity across different systems
Weekly Installs
1.6K
Repository
composiohq/awes…e-skills
GitHub Stars
57.5K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass