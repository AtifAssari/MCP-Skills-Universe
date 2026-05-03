---
title: context-doctor
url: https://skills.sh/jzocb/context-doctor/context-doctor
---

# context-doctor

skills/jzocb/context-doctor/context-doctor
context-doctor
Installation
$ npx skills add https://github.com/jzocb/context-doctor --skill context-doctor
SKILL.md
Context Doctor

Diagnose and visualize how the context window budget is allocated.

Quick Start

Run the visualization script:

python3 scripts/context-doctor.py


The script auto-detects:

Workspace path (~/.openclaw/workspace or OPENCLAW_WORKSPACE env)
OpenClaw version (via openclaw --version)
Installed skills (system + workspace)
Bootstrap file sizes and status
Output Sections
1. Workspace Files

Shows each bootstrap file with:

Status: ✓ OK / ✗ MISSING / ⚠ TRUNCATED (symlink target missing = MISSING)
Characters & Tokens: Raw size and estimated token count (chars/4)
Visual bar: Proportional to file size
2. Installed Skills

Lists all discovered SKILL.md files from system and workspace skill directories. Skills are loaded on-demand, not in bootstrap — shown for awareness only.

3. Token Budget

Breaks down bootstrap overhead:

System Prompt (framework)
Workspace Files (from scan)
Skills List (metadata descriptions)
Tool Schemas + Summaries

Shows total bootstrap % vs free conversation space.

Diagnostic Signals
Signal	Meaning	Action
🔴 TRUNCATED	File exceeded max chars, silently cut	Reduce file size or split content
🟡 MISSING	File not found or broken symlink	Check path, fix symlink target
🟢 Bootstrap <10%	Healthy	No action needed
🟠 Bootstrap >15%	Heavy	Review workspace files for bloat
Image Output (for chat / sharing)

Generate a PNG image directly — no terminal screenshot needed:

python3 scripts/context-doctor.py --png /tmp/context-doctor.png


The script renders a colored terminal-style image via Rich SVG export. Requires: rich (pip3 install rich) + one of: rsvg-convert (brew install librsvg) or cairosvg (pip3 install cairosvg).

Agent workflow: When a user asks about context health in chat, run with --png and send the image directly. The output path is printed to stdout on success.

Weekly Installs
61
Repository
jzocb/context-doctor
GitHub Stars
118
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass