---
rating: ⭐⭐
title: uv-environment
url: https://skills.sh/gemini960114/skills/uv-environment
---

# uv-environment

skills/gemini960114/skills/uv-environment
uv-environment
Installation
$ npx skills add https://github.com/gemini960114/skills --skill uv-environment
SKILL.md

You are helping with uv and Python environments.

Core Principle

Assume uv is already installed. Never suggest reinstalling uv or Python unless explicitly requested or clearly broken.

Step 1 — Detect OS

Detect the operating system from:

Path style (C:\ vs /home/)
Shell prompt (PS vs $)
Commands used (where vs which)
Explicit OS mention
Step 2 — Use OS-appropriate commands
If Windows:
Activate venv: .\.venv\Scripts\Activate.ps1
Check python: where python
Check uv: uv --version
If macOS/Linux:
Activate venv: source .venv/bin/activate
Check python: which python
Check uv: uv --version
Always Prefer uv Workflow

Use:

uv init
uv venv
uv sync
uv run
uv pip

Avoid switching to pip/venv unless requested.

Troubleshooting (Only If Needed)

If venv missing:

uv venv

If dependencies missing:

uv sync

If PowerShell policy blocks activation:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Output Style
Command-first
Minimal steps
Provide copy-paste ready blocks
Use OS-correct syntax
Weekly Installs
11
Repository
gemini960114/skills
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn