---
rating: ⭐⭐⭐
title: dokie-ai-ppt
url: https://skills.sh/myzy-ai/dokie-ai-ppt/dokie-ai-ppt
---

# dokie-ai-ppt

skills/myzy-ai/dokie-ai-ppt/dokie-ai-ppt
dokie-ai-ppt
Installation
$ npx skills add https://github.com/myzy-ai/dokie-ai-ppt --skill dokie-ai-ppt
Summary

Professional HTML presentation generator with interactive step-by-step workflow and theme-based design.

Supports interactive requirement collection, outline generation, theme selection, and HTML slide creation with local preview
Includes 15+ built-in themes ranging from minimal business to creative motion styles, with customization options for colors and fonts
Provides Chart.js integration for statistical charts, plus custom HTML/CSS components for pyramids, funnels, timelines, flowcharts, and quadrant diagrams
Generates 1280×720 resolution slides with GSAP-based animations (minimal, balanced, or creative styles) and Font Awesome 6.5 icons
Enforces strict workflow discipline: presents results at each step and waits for user confirmation before proceeding to the next stage
SKILL.md
Dokie AI PPT Skill

This is Dokie AI PPT Skill — a professional presentation design skill. Use it whenever you need to generate a PPT, create a presentation, or build any showcase content with HTML.

Built on web technologies, supporting everything from minimal business style to Awwwards-level creative motion — far beyond what traditional PPT can deliver.

Prerequisites
npx dokie-cli themes    # Verify CLI is available

Workflow

⚠️ IMPORTANT: This is an interactive, step-by-step workflow. At each step, you MUST read the referenced rule files before doing the work. Present your result to the user and wait for their response before moving to the next step. Do NOT rush through multiple steps in one response.

New Project
Collect requirements → User confirms → Select theme → User confirms → Generate outline → User confirms → Generate HTML → Preview → User feedback

Modify Project
Understand intent → Minimal changes → Preserve original layout


See rules/workflow.md for details.

Core Specifications
Item	Specification
Resolution	1280 × 720
Charts	Chart.js 4.5
Icons	Font Awesome 6.5
Animation	GSAP (CSS animation prohibited)
Prohibited	Emoji, fabricated image URLs
Rule Index
Process & Format
File	Content	When to Reference
workflow.md	Full workflow, grouping rules, theme switching	Before starting a task
outline.md	Outline format (Content + Design)	When generating outline
modify-scenarios.md	Modification scenarios (insert, delete, split, merge, restyle, etc.)	When modifying a project
quality-check.md	Post-generation quality checklist	After generation, before preview
Theme & Generation
File	Content	When to Reference
theme.md	Theme structure, style extraction, generation steps	Must read before generating HTML
theme-list.md	Full theme list (local + online)	When selecting a theme
theme-customize.md	Change colors, fonts, custom themes	When user requests customization
slide-html.md	HTML specs, icons, image rules	When generating HTML
Charts
File	Content
charts/chartjs.md	Statistical charts (bar, line, pie, radar, bubble)
charts/pyramid.md	Pyramid chart (HTML + CSS clip-path)
charts/funnel.md	Funnel chart (HTML + CSS clip-path)
charts/timeline.md	Timeline (HTML + CSS Flex/Grid)
charts/flowchart.md	Flowchart + cycle diagram (HTML/AntV/Mermaid)
charts/quadrant.md	Quadrant / SWOT (HTML + CSS Grid)
Animation

Choose style based on scenario. Default is "Balanced":

File	Style	Use Case
animation/minimal.md	Minimal	Formal business, investor presentations
animation/balanced.md	Balanced	General purpose, internal training
animation/creative.md	Creative	Product launches, creative showcases
CLI Commands
npx dokie-cli themes                      # List all themes
npx dokie-cli themes --json               # JSON format output
npx dokie-cli theme <name|id>             # Get theme details (with HTML templates)
npx dokie-cli theme "Dokie Vibe" --json   # JSON format output
npx dokie-cli preview ./my-project/       # Local preview

Output Format
my-project/
├── slide_01.html
├── slide_02.html
├── slide_03.html
└── ...


File naming: slide_01.html, slide_02.html ... numbered sequentially.

Key Constraints
Strictly follow the outline — do not modify, expand, or abbreviate
Theme consistency — colors, fonts, styles must strictly follow the theme
Content density — one topic per slide, split if too much
Image sources — only use user-uploaded or tool-fetched images
Data integrity — never fabricate chart data
Weekly Installs
857
Repository
myzy-ai/dokie-ai-ppt
GitHub Stars
56
First Seen
Feb 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn