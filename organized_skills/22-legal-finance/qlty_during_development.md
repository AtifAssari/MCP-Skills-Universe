---
rating: ⭐⭐⭐
title: qlty-during-development
url: https://skills.sh/parcadei/continuous-claude-v3/qlty-during-development
---

# qlty-during-development

skills/parcadei/continuous-claude-v3/qlty-during-development
qlty-during-development
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill qlty-during-development
SKILL.md
QLTY During Development

Run QLTY checks during code writing to catch issues early.

When to Run

Run QLTY after significant code changes:

After completing a new file
After substantial edits to existing files
Before committing changes
Commands
# Quick lint check
qlty check

# Format code
qlty fmt

# Check specific files
qlty check src/sdk/providers.ts

# Auto-fix issues
qlty check --fix

Integration Pattern

After writing code:

Run qlty check on changed files
If errors, fix them before proceeding
Run qlty fmt to ensure formatting
Don't Run When
Just reading/exploring code
Making single-line typo fixes
In the middle of multi-file refactoring (run at end)
Weekly Installs
299
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass