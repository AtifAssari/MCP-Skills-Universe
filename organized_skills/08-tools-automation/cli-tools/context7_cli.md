---
rating: ⭐⭐⭐
title: context7-cli
url: https://skills.sh/upstash/context7/context7-cli
---

# context7-cli

skills/upstash/context7/context7-cli
context7-cli
Installation
$ npx skills add https://github.com/upstash/context7 --skill context7-cli
SKILL.md
ctx7 CLI

The Context7 CLI does three things: fetches up-to-date library documentation, manages AI coding skills, and sets up Context7 MCP for your editor.

Make sure the CLI is up to date before running commands:

npm install -g ctx7@latest


Or run directly without installing:

npx ctx7@latest <command>

What this skill covers
Documentation — Fetch current docs for any library. Use when writing code, verifying API signatures, or when training data may be outdated.
Skills management — Install, search, suggest, list, remove, and generate AI coding skills.
Setup — Configure Context7 MCP for Claude Code / Cursor / OpenCode.
Quick Reference
# Documentation
ctx7 library <name> <query>           # Step 1: resolve library ID
ctx7 docs <libraryId> <query>         # Step 2: fetch docs
ctx7 docs <libraryId> <query> --research  # Retry with deep research if the default answer didn't satisfy

# Skills
ctx7 skills install /owner/repo       # Install from a repo (interactive)
ctx7 skills install /owner/repo name  # Install a specific skill
ctx7 skills search <keywords>         # Search the registry
ctx7 skills suggest                   # Auto-suggest based on project deps
ctx7 skills list                      # List installed skills
ctx7 skills remove <name>             # Uninstall a skill
ctx7 skills generate                  # Generate a custom skill with AI (requires login)

# Setup
ctx7 setup                            # Configure Context7 MCP (interactive)
ctx7 login                            # Log in for higher rate limits + skill generation
ctx7 whoami                           # Check current login status

Authentication
ctx7 login               # Opens browser for OAuth
ctx7 login --no-browser  # Prints URL instead of opening browser
ctx7 logout              # Clear stored tokens
ctx7 whoami              # Show current login status (name + email)


Most commands work without login. Exceptions: skills generate always requires it; ctx7 setup requires it unless --api-key or --oauth is passed. Login also unlocks higher rate limits on docs commands.

Set an API key via environment variable to skip interactive login entirely:

export CONTEXT7_API_KEY=your_key

Common Mistakes
Library IDs require a / prefix — /facebook/react not facebook/react
Always run ctx7 library first — ctx7 docs react "hooks" will fail without a valid ID
Repository format for skills is /owner/repo — e.g., ctx7 skills install /anthropics/skills
skills generate requires login — run ctx7 login first
Weekly Installs
1.7K
Repository
upstash/context7
GitHub Stars
54.3K
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn