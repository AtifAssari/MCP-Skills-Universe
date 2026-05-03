---
title: oxfmt-oxlint
url: https://skills.sh/upamune/radicaster/oxfmt-oxlint
---

# oxfmt-oxlint

skills/upamune/radicaster/oxfmt-oxlint
oxfmt-oxlint
Installation
$ npx skills add https://github.com/upamune/radicaster --skill oxfmt-oxlint
SKILL.md
OXFMT-OXLINT Skill

This skill provides access to OXFMT-OXLINT documentation.

Documentation

All documentation files are in the docs/ directory as Markdown files.

Search Tool
python scripts/search_docs.py "<query>"


Options:

--json - Output as JSON
--max-results N - Limit results (default: 10)
Usage
Search or read files in docs/ for relevant information
Each file has frontmatter with source_url and fetched_at
Always cite the source URL in responses
Note the fetch date - documentation may have changed
Response Format
[Answer based on documentation]

**Source:** [source_url]
**Fetched:** [fetched_at]

Weekly Installs
59
Repository
upamune/radicaster
GitHub Stars
2
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn