---
title: context7
url: https://skills.sh/am-will/codex-skills/context7
---

# context7

skills/am-will/codex-skills/context7
context7
Installation
$ npx skills add https://github.com/am-will/codex-skills --skill context7
Summary

Fetch current library documentation via Context7 API for any external package.

Search for libraries by name, then retrieve documentation context using the library ID and a specific query
Supports two output formats (txt and markdown) with configurable token limits for response size
Use proactively when working with external libraries, installing dependencies, debugging library-specific issues, or verifying APIs beyond your training data cutoff
API key stored in .env file within the skill installation directory; requires Python 3 to run the CLI scripts
SKILL.md
Context7 Documentation Fetcher

Retrieve current library documentation via Context7 API.

IMPORTANT: CONTEXT7_API_KEY IS STORED IN THE .env FILE IN THE SKILL FOLDER THAT THE CONTEXT7 SKILL IS INSTALLED IN. SEARCH FOR IT THERE. .env FILES ARE HIDDEN FILES.

Example: ~/.agents/skills/context7/.env ~/.claude/skills/context7/.env

Workflow
1. Search for the library
python3 ~/.codex/skills/context7/scripts/context7.py search "<library-name>"


Example:

python3 ~/.codex/skills/context7/scripts/context7.py search "next.js"


Returns library metadata including the id field needed for step 2.

2. Fetch documentation context
python3 ~/.codex/skills/context7/scripts/context7.py context "<library-id>" "<query>"


Example:

python3 ~/.codex/skills/context7/scripts/context7.py context "/vercel/next.js" "app router middleware"


Options:

--type txt|md - Output format (default: txt)
--tokens N - Limit response tokens
Quick Reference
Task	Command
Find React docs	search "react"
Get React hooks info	context "/facebook/react" "useEffect cleanup"
Find Supabase	search "supabase"
Get Supabase auth	context "/supabase/supabase" "authentication row level security"
When to Use
Before implementing any library-dependent feature
When unsure about current API signatures
For library version-specific behavior
To verify best practices and patterns
Weekly Installs
1.2K
Repository
am-will/codex-skills
GitHub Stars
907
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn