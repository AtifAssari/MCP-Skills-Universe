---
title: tavily-search
url: https://skills.sh/jacky1n7/openclaw-skill-tavily-search/tavily-search
---

# tavily-search

skills/jacky1n7/openclaw-skill-tavily-search/tavily-search
tavily-search
Installation
$ npx skills add https://github.com/jacky1n7/openclaw-skill-tavily-search --skill tavily-search
SKILL.md
Tavily Search

Use the bundled script to search the web with Tavily.

Requirements
Provide API key via either:
environment variable: TAVILY_API_KEY, or
~/.openclaw/.env line: TAVILY_API_KEY=...
Commands

Run from the OpenClaw workspace:

# raw JSON (default)
python3 {baseDir}/scripts/tavily_search.py --query "..." --max-results 5

# include short answer (if available)
python3 {baseDir}/scripts/tavily_search.py --query "..." --max-results 5 --include-answer

# stable schema (closer to web_search): {query, results:[{title,url,snippet}], answer?}
python3 {baseDir}/scripts/tavily_search.py --query "..." --max-results 5 --format brave

# human-readable Markdown list
python3 {baseDir}/scripts/tavily_search.py --query "..." --max-results 5 --format md

Output
raw (default)
JSON: query, optional answer, results: [{title,url,content}]
brave
JSON: query, optional answer, results: [{title,url,snippet}]
md
A compact Markdown list with title/url/snippet.
Notes
Keep max-results small by default (3–5) to reduce token/reading load.
Prefer returning URLs + snippets; fetch full pages only when needed.
Weekly Installs
126
Repository
jacky1n7/opencl…y-search
GitHub Stars
4
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn