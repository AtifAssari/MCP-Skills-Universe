---
title: techguide
url: https://skills.sh/ggprompts/htmlstyleguides/techguide
---

# techguide

skills/ggprompts/htmlstyleguides/techguide
techguide
Installation
$ npx skills add https://github.com/ggprompts/htmlstyleguides --skill techguide
SKILL.md
Build a Tech Guide

Create a comprehensive tech guide for $ARGUMENTS.

Follow the full conventions in techguides/CLAUDE.md. The guide must be self-contained HTML with inline CSS, Google Fonts only, 1500-4000+ lines, 8-12 numbered sections, sticky jump nav, and responsive design.

Phase 0 — Plan (interactive)
Parse the argument: the first word is the topic (e.g., "xterm.js"), optional second word is the style name (e.g., "celtic").
If no style was specified:
Read the Style Guide Catalog table in README.md to see which styles are available (empty Tech Guide column) vs already used
Suggest 3-4 unused styles that thematically fit the topic
Ask the user to pick one
Read the chosen style's HTML file from styles/{name}.html to extract the design system (CSS variables, fonts, color palette, component patterns).
Read techguides/CLAUDE.md for the template and conventions.
Read 1-2 existing tech guides (like python.html or docker.html) to match structure and depth — just skim the first ~100 lines for structure reference.
Propose a section outline (8-12 sections) and discuss with the user before proceeding.
Phase 1 — Research (parallel Sonnet subagents)

Launch 3-4 sonnet subagents in parallel to research different topic areas:

Each subagent should use context7 MCP (mcp-cli call context7/resolve-library-id then mcp-cli call context7/query-docs) to find the latest documentation
Each subagent should also use WebSearch for current best practices
Subagents should cover distinct non-overlapping areas (e.g., for a language: fundamentals, advanced features, ecosystem/frameworks, tooling/testing)
Each subagent returns a structured summary of key concepts, code examples, and current best practices
Phase 2 — Build (sequential Opus subagents)

Use 4-5 sequential opus subagents, each writing a portion of the guide:

First agent: Create the full HTML skeleton with the chosen style's CSS adapted for tech guide components (jump nav, section headers, code blocks, tables, alerts, command grids). Write sections 01-03. Include all Google Font links, all CSS, the complete <head>, back link, header, jump nav with ALL section links, and the opening sections.
Second agent: Read the file so far, then append sections 04-06. Must read the existing file first to continue seamlessly.
Third agent: Read the file so far, then append sections 07-09.
Fourth agent: Read the file so far, then append sections 10-12 (or however many remain) plus the footer. Close all HTML tags.
Fifth agent (polish): Read the complete file. Verify all jump nav anchor links match section IDs. Check for consistency in class names, spacing, and code example formatting. Fix any issues.

Critical rules for build agents:

Each agent MUST read the current file before writing
Use the Edit tool to append content (find the closing </body> or last </section> and insert before it)
Never rewrite the entire file — only append or edit specific sections
All code examples must use <pre><code> blocks
Every section needs an id attribute matching the jump nav anchors
Include the back link: <a href="index.html" class="back-link">Tech Guides</a>
Phase 3 — Index & Ship
Read techguides/index.html to understand the card format and tiers.
Add a card for the new guide in the appropriate tier:
Tier 1 — Core Tools: Essential developer tools (git, docker, vim, bash)
Tier 2 — Essential Toolkit: Common languages/utilities (python, rust, go)
Tier 3 — Infrastructure & Ops: Server/deployment/architecture
Add matching .card-{style-name} CSS with colors from the style's palette.
Update the guide count in the index header if present.
Update the Style Guide Catalog table in README.md — add the tech guide name in the Tech Guide column for the chosen style.
Commit with message: Add {Topic} tech guide ({style-name} style)
Push using: git config --global credential.helper store && echo "https://GGPrompts:$(gh auth token --user GGPrompts)@github.com" > ~/.git-credentials && git push origin main
Weekly Installs
22
Repository
ggprompts/htmls…leguides
GitHub Stars
15
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail