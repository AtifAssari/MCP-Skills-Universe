---
rating: ⭐⭐
title: context7-2
url: https://skills.sh/sundial-org/awesome-openclaw-skills/context7-2
---

# context7-2

skills/sundial-org/awesome-openclaw-skills/context7-2
context7-2
Installation
$ npx skills add https://github.com/sundial-org/awesome-openclaw-skills --skill context7-2
SKILL.md
Context7 Documentation Fetcher

Retrieve current library documentation via Context7 API.

Workflow
1. Search for the library
python3 ~/.claude/skills/context7/scripts/context7.py search "<library-name>"


Example:

python3 ~/.claude/skills/context7/scripts/context7.py search "next.js"


Returns library metadata including the id field needed for step 2.

2. Fetch documentation context
python3 ~/.claude/skills/context7/scripts/context7.py context "<library-id>" "<query>"


Example:

python3 ~/.claude/skills/context7/scripts/context7.py context "/vercel/next.js" "app router middleware"


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
8
Repository
sundial-org/awe…w-skills
GitHub Stars
589
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn