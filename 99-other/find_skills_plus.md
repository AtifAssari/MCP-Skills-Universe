---
title: find-skills-plus
url: https://skills.sh/yinhui1984/find_skills_plus/find-skills-plus
---

# find-skills-plus

skills/yinhui1984/find_skills_plus/find-skills-plus
find-skills-plus
Installation
$ npx skills add https://github.com/yinhui1984/find_skills_plus --skill find-skills-plus
SKILL.md
Find Skills Plus

This skill searches the skills registry and enriches each result with a description.

When to Use

Use this skill when the user asks to discover skills and wants more than just a list (e.g., asks for descriptions, comparisons, or short summaries).

How It Works
Runs npx skills find <query> to get matching skills.
For each result, fetches the skills.sh page and extracts a description (first non-empty paragraph).
Prints results in an easy-to-scan format.
Command
node scripts/enrich_find.js "<query>"

Options
--max N Limit number of results to enrich (default: 10)
--timeout SECONDS Per-request timeout (default: 10)
--concurrency N Concurrent fetches (default: 5)
--no-fetch Show list only (skip description fetch)
Output Format
owner/repo@skill
└ https://skills.sh/owner/repo/skill
[description]

Notes
Descriptions are pulled from the skills.sh page when available.
If the skills.sh page is missing a description, the script falls back to agent-skills.md.
If a description cannot be found, the output will say "[no description found]".
Weekly Installs
60
Repository
yinhui1984/find…lls_plus
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn