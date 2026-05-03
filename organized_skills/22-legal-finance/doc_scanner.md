---
rating: ⭐⭐
title: doc-scanner
url: https://skills.sh/0xdarkmatter/claude-mods/doc-scanner
---

# doc-scanner

skills/0xdarkmatter/claude-mods/doc-scanner
doc-scanner
Installation
$ npx skills add https://github.com/0xdarkmatter/claude-mods --skill doc-scanner
SKILL.md
Documentation Scanner

Scan for and synthesize project documentation.

When to Activate
User asks to review, understand, or explore a codebase
Starting work in a new/unfamiliar project
User asks about project conventions or workflows
Before making significant architectural decisions
Instructions
Step 1: Scan for Documentation

Use Glob to search project root:

AGENTS.md, CLAUDE.md, AI.md, ASSISTANT.md,
GEMINI.md, COPILOT.md, CHATGPT.md, CODEIUM.md,
CURSOR.md, WINDSURF.md, VSCODE.md, JETBRAINS.md,
WARP.md, FIG.md, DEVCONTAINER.md, GITPOD.md

Step 2: Read All Found Files

Read complete contents of every documentation file found.

Step 3: Synthesize

Combine information into unified summary:

PROJECT DOCUMENTATION

Sources: [list files found]

RECOMMENDED AGENTS
  Primary: [agents for core work]
  Secondary: [agents for specific tasks]

KEY WORKFLOWS
  [consolidated workflows]

CONVENTIONS
  [code style, patterns]

QUICK COMMANDS
  [common commands]

Step 4: Offer Consolidation

If 2+ documentation files exist, offer to consolidate:

Create .doc-archive/ directory
Archive originals with date suffix
Generate unified AGENTS.md
Report what was consolidated
Step 5: No Documentation Found

If none found, offer to generate AGENTS.md based on:

Project structure and tech stack
Patterns observed in codebase
Priority Order
AGENTS.md (platform-agnostic)
CLAUDE.md (Claude-specific)
Other AI docs
IDE docs
Terminal docs
Additional Resources

For detailed patterns, load:

./references/file-patterns.md - Complete list of files to scan
./references/templates.md - AGENTS.md generation templates
Weekly Installs
38
Repository
0xdarkmatter/claude-mods
GitHub Stars
17
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail