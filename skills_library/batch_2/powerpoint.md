---
title: powerpoint
url: https://skills.sh/igorwarzocha/opencode-workflows/powerpoint
---

# powerpoint

skills/igorwarzocha/opencode-workflows/powerpoint
powerpoint
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill powerpoint
Summary

Create, design, and audit PowerPoint presentations with precise layout control and design principles.

Supports high-fidelity slide creation via HTML-to-PPTX conversion with exact 720pt × 405pt positioning and rasterized visuals
Includes template-based workflows: audit decks with thumbnail grids, inject content via JSON mapping, and rearrange slides programmatically
Enforces design quality standards: web-safe fonts only, proper hex color formatting, two-column layouts, and final verification thumbnails to catch text cutoff or overlap
Built for pitch decks, status updates, and visual storytelling with proactive design intervention when layout precision matters
SKILL.md

<high_fidelity_creation> The preferred method for precise layout positioning:

HTML: Create slides (720pt x 405pt). Text MUST be in <p>, <h1>-<h6>, or <ul>.
Visuals: You MUST rasterize gradients/icons as PNGs using Sharp FIRST. Reference: references/html2pptx.md.
Execution: Run html2pptx.js to generate the presentation. </high_fidelity_creation>

<template_structure> For deck editing or template mapping:

Audit: Generate thumbnail grid (scripts/thumbnail.py) to analyze layout.
Duplication: Use scripts/rearrange.py to duplicate and reorder slides.
Text Injection: Use scripts/replace.py with the JSON inventory to populate content. </template_structure>

<design_quality>

Fonts: You MUST use web-safe fonts ONLY (Arial, Helvetica, Georgia).
Colors: You MUST NOT use the # prefix in PptxGenJS hex codes (causes corruption).
Layout: You SHOULD prefer two-column or full-slide layouts. You MUST NOT stack charts below text.
Verification: You MUST generate a final thumbnail grid with --cols 4 to inspect for text cutoff or overlap issues. </design_quality>

</powerpoint_professional_suite>

Weekly Installs
1.4K
Repository
igorwarzocha/op…orkflows
GitHub Stars
111
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass