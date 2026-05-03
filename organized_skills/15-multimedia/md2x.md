---
rating: ⭐⭐⭐
title: md2x
url: https://skills.sh/site/skills.netease.im/md2x
---

# md2x

skills/skills.netease.im/md2x
md2x
$ npx skills add https://skills.netease.im/api/install/c982fcd2828cb549d387d824bbcae87b
SKILL.md
md2x - Markdown Converter

Quick Start: Run npx md2x input.md for PDF, add -f docx for Word, -f html for web, or -f png for a full-page screenshot image. Customize with --theme (academic, minimal, etc.). Supports front matter config in markdown files.

Critical Usage Rules
Rule 1: Basic Conversion
# PDF (default)
npx md2x input.md

# DOCX
npx md2x input.md -f docx

# HTML
npx md2x input.md -f html

# Image (full-page screenshot via Puppeteer)
npx md2x input.md -f png
npx md2x input.md -f jpg
npx md2x input.md -f webp


For very tall documents, md2x will automatically split the output into multiple files: output.part-001.png, output.part-002.png, ...

Rule 2: Output Control
# Specify output path
npx md2x input.md -o output.pdf

# Auto-named output (input name + format extension)
npx md2x README.md -f docx  # → README.docx

# Format can be inferred from output extension (no -f needed)
npx md2x README.md README.png
npx md2x README.md README.webp

Rule 3: Theme Selection
# List available themes
npx md2x --list-themes

# Use specific theme
npx md2x input.md --theme academic
npx md2x input.md -t minimal

Rule 4: Page Break Control
# Horizontal rules as page breaks (default for PDF/DOCX)
npx md2x input.md --hr-page-break true

# Keep horizontal rules as visual dividers (default for HTML)
npx md2x input.md --hr-page-break false

Rule 5: HTML Diagram Modes
# Live rendering with CDN (default, requires internet)
npx md2x input.md -f html --diagram-mode live

# Pre-rendered images (offline-ready)
npx md2x input.md -f html --diagram-mode img

# Source code only (no rendering)
npx md2x input.md -f html --diagram-mode none

Rule 6: Front Matter Configuration
---
format: pdf
theme: academic
hrAsPageBreak: true
title: My Document
---

# Document Content

CLI Options Reference
Option	Alias	Description	Default	Values
--help	-h	Show help message	-	-
--version	-v	Show version number	-	-
--output	-o	Output file path	Input name with format extension	File path
--format	-f	Output format	pdf	pdf, docx, html, png, jpg/jpeg, webp
--theme	-t	Theme name	default	See --list-themes
--diagram-mode	-	HTML diagram rendering mode	live	img, live, none
--hr-page-break	-	Convert horizontal rules to page breaks	true for PDF/DOCX, false for HTML	true, false
--list-themes	-	List all available themes	-	-
Common Pitfalls
Issue	Solution
Input file not found	Use absolute path or verify file exists
Theme not found	Run --list-themes to see available options
Diagrams not rendering in HTML	Check --diagram-mode setting and internet connection
Page breaks not working	Verify --hr-page-break true for PDF/DOCX
Output directory doesn't exist	Tool creates directories automatically
Supported Features
Diagrams
Mermaid: Flowcharts, sequence diagrams, state machines, Gantt charts
Graphviz: DOT language graphs
Vega/Vega-Lite: Data visualizations and charts
Infographic: Quick KPI and metric displays
HTML/SVG: Embedded graphics
Content
Math: LaTeX formulas via KaTeX
Code: Syntax highlighting for 100+ languages
Tables: Full markdown table support
Images: Local and remote image embedding
Links: Internal and external hyperlinks
Priority Order (CLI vs Front Matter)

CLI arguments explicitly set take precedence over front matter:

CLI explicit (highest priority)
Front matter in markdown file
Default values (lowest priority)

Example:

# Front matter has theme: minimal
# CLI overrides with theme: academic
npx md2x input.md --theme academic  # Uses academic

Output Format
# Command
npx md2x input.md -f pdf --theme academic

# Console output
Converting: input.md
Format: PDF
Theme: academic
HR as page break: true
Output: /path/to/input.pdf
Done!

Related Files

For detailed examples and advanced usage patterns, refer to references below:

examples.md — Common use cases, front matter examples, batch conversion patterns, and troubleshooting
Resources
GitHub Repository
npm Package
Markdown Viewer Extension
Weekly Installs
10
Source
skills.netease.…bbcae87b
First Seen
11 days ago