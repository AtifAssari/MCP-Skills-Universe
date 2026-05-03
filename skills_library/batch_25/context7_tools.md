---
title: context7-tools
url: https://skills.sh/bsamiee/parametric_forge/context7-tools
---

# context7-tools

skills/bsamiee/parametric_forge/context7-tools
context7-tools
Installation
$ npx skills add https://github.com/bsamiee/parametric_forge --skill context7-tools
SKILL.md
[H1][CONTEXT7-TOOLS]

Dictum: Two-step resolution ensures accurate documentation retrieval.

Query Context7 library documentation via unified Python CLI.

[IMPORTANT] Commands require arguments. First resolve, then docs.

# Resolve library name → ID
uv run .claude/skills/context7-tools/scripts/context7.py resolve --library "react"

# Fetch documentation by resolved ID
uv run .claude/skills/context7-tools/scripts/context7.py docs --library-id "/facebook/react"

# Apply topic filter
uv run .claude/skills/context7-tools/scripts/context7.py docs --library-id "/facebook/react" --topic "hooks"

# Set custom token limit
uv run .claude/skills/context7-tools/scripts/context7.py docs --library-id "/vercel/next.js" --tokens 10000

[1][OUTPUT]

Commands return: {"status": "success|error", ...}.

[INDEX]	[CMD]	[RESPONSE]
[1]	resolve	{library: string, matches: object[]}
[2]	docs	{library_id: string, docs: object}
Weekly Installs
8
Repository
bsamiee/parametric_forge
GitHub Stars
2
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass