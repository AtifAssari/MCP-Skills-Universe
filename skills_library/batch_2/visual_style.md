---
title: visual-style
url: https://skills.sh/heygen-com/skills/visual-style
---

# visual-style

skills/heygen-com/skills/visual-style
visual-style
Installation
$ npx skills add https://github.com/heygen-com/skills --skill visual-style
SKILL.md
Visual Style

Create, extract, and apply portable visual design systems. A visual-style.md file defines colors, typography, layout, motion, and mood in one file that any AI tool can consume.

Quick Reference
Mode	Trigger	What it does
Create	"Create a visual-style.md for..."	Build a style from scratch via guided prompts
Extract	"Extract a visual-style.md from [URL/image/video]"	Analyze a source and generate a style file
Apply	"Apply this visual-style.md to [tool]"	Use a style with a specific connector
Gallery	"Show me available visual styles"	Browse and use example styles
Default Workflow
Create
Gather vibe — Ask about mood, era, references, inspiration
Define colors — Primary (2+), accent, neutrals with hex values and roles
Set typography — Display, body, caption families + weight/style rules
Layout & motion — Grid system, transitions, pacing
Generate — Output complete visual-style.md using references/templates/minimal.visual-style.md or references/templates/full.visual-style.md
Preview — Show a small HTML swatch or describe the visual result
Optionally apply — Ask if user wants to use it with a connector

Questions to batch:

What's the vibe? (mood keywords, era, references)
Any specific colors? (or derive from the vibe?)
Typography preference? (clean, editorial, technical, playful?)
What tool will you use this with? (HeyGen, slides, paper.design, Figma?)
Extract
Receive source — URL, image, video, or PDF
Load extractor — Read the appropriate extractor reference file
Analyze — Identify colors, typography, layout, motion, mood
Generate — Output complete visual-style.md with source_url set
Validate — Ensure all required fields are present
Apply
Read the style — Load the visual-style.md file
Ask which connector — Or detect from context
Load connector — Read the appropriate connector reference file
Transform — Map style fields to tool-specific format
Generate output — Produce tool-ready instructions or code
Gallery
List styles — Show available styles from references/gallery/
Preview — Describe the selected style's visual character
Load — Read the full visual-style.md
Apply — Use with a connector
Format Quick Reference
Required fields
name: "Style Name"
version: "1.0"
style_prompt_short: "1-2 sentence elevator pitch"
style_prompt_full: "Detailed generation prompt — THE most important field"
colors:
  primary:
    - name: "Color Name"
      hex: "#000000"
      role: "how this color is used"


style_prompt_full is king. If a tool can only read one field, it reads this one. Everything else is structured data for tools that want finer control.

Full spec: references/spec.md

Reference Files
Connectors (Apply mode)
Connector	Use case	File
HeyGen Video Agent	AI video generation	references/connectors/heygen-video-agent.md
HTML Slides	Web presentations	references/connectors/html-slides.md
paper.design	Design documents	references/connectors/paper-design.md
Figma	Design tool styles	references/connectors/figma.md
Extractors (Extract mode)
Source	File
Website URL	references/extractors/from-website.md
Video keyframes	references/extractors/from-video.md
PDF / Brand guide	references/extractors/from-pdf.md
Gallery (pre-built styles)
Style	Era	File
Müller-Brockmann Swiss	1950s–70s	references/gallery/mueller-brockmann-swiss.visual-style.md
Neville Brody Industrial	Late 1980s–90s	references/gallery/neville-brody-industrial.visual-style.md
Saul Bass Cinematic	1950s–60s	references/gallery/saul-bass-cinematic.visual-style.md
Game Boy Color	1998–2003	references/gallery/game-boy-color.visual-style.md
HeyGen AI Video	2020s	references/gallery/heygen-ai-video.visual-style.md
Templates & Spec
references/templates/minimal.visual-style.md — Bare minimum template
references/templates/full.visual-style.md — Complete template with all fields
references/spec.md — Full format specification
Best Practices
style_prompt_full is king — Always usable as a standalone generation prompt
One style, one file — No multi-style bundling
Assets are URLs — Never embed binary data
Show, don't tell — Generate previews when creating styles
Opinionated defaults, flexible extensions — Core schema is fixed; x_* for tool-specific config
Weekly Installs
921
Repository
heygen-com/skills
GitHub Stars
202
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn