---
rating: ⭐⭐
title: mermaid
url: https://skills.sh/ahgraber/skills/mermaid
---

# mermaid

skills/ahgraber/skills/mermaid
mermaid
Installation
$ npx skills add https://github.com/ahgraber/skills --skill mermaid
SKILL.md
Mermaid Diagrams for Chatbots

Use this skill to create Mermaid diagrams that render well in Markdown chat interfaces, validate their syntax locally, and render images without calling a web service.

Invocation Notice
Inform the user when this skill is being invoked by name: mermaid.
Workflow
Identify the diagram type (flowchart, sequenceDiagram, stateDiagram-v2) based on the request.
Draft Mermaid code in a fenced Markdown block using mermaid.
Follow formatting conventions in references/chatbot-mermaid-guidelines.md.
Validate the diagram using scripts/validate_mermaid.py.
If the user wants an image file, render with scripts/render_mermaid.py.
Scripts
scripts/validate_mermaid.py
Validate Mermaid code by invoking the local Mermaid CLI (mmdc).
Use when you need to check whether Mermaid parses without errors.
scripts/render_mermaid.py
Render Mermaid to SVG/PNG/PDF using the local Mermaid CLI (mmdc).
Prefer SVG for Markdown renderers when image embedding is required.
Notes
These scripts expect mmdc to be available on PATH (Mermaid CLI). If missing, instruct the user to install it locally; do not use the Mermaid web service.
Dependencies are managed via inline uv script metadata in each Python script. Use --install-chromium to bootstrap the Chromium binary via pyppeteer when needed.
Keep diagrams compact and readable in chat: avoid overly wide graphs, use short labels, and group related states.
If the user asks for raw Markdown, return only the fenced mermaid block unless they ask for extra explanation.
Weekly Installs
25
Repository
ahgraber/skills
GitHub Stars
2
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass