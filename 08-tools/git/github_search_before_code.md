---
title: github-search-before-code
url: https://skills.sh/ruiwarn/skills/github-search-before-code
---

# github-search-before-code

skills/ruiwarn/skills/github-search-before-code
github-search-before-code
Installation
$ npx skills add https://github.com/ruiwarn/skills --skill github-search-before-code
SKILL.md
GitHub Search Before Code
Trigger Conditions

Scenario 1 - New functionality: New algorithms, protocols, drivers, or complex features not in codebase Scenario 2 - Repeated failures: User says "still not working", "tried many times", "改了很多次了", "还是有问题"

Workflow
1. Infer Domain

Analyze conversation context to extract 1-2 domain keywords:

Without first identifying the industry background, keyword extraction may lead to results that are completely off-topic.
Current discussion topic
Recent code files/functions
User's project description

If unclear, see industry-background.md for domain keyword reference.

2. Construct Keywords

Pattern: "<function> <domain> <tech>"

Examples:

C: "harmonic analysis" + "power" → "harmonic analysis power metering" C
Python: "web scraping" → "web scraping beautifulsoup" Python
Shell: "backup automation" → "incremental backup script" Shell

Domain matters: "Goertzel" → audio ❌, "Goertzel power" → power analysis ✅

3. Search GitHub
python3 scripts/github_search.py repo "<keywords>" [language]


Features:

see search-strategies.md for search flow reference.
Auto-fallback: tries 4 strategies if no results (language → no-lang → simplified → core-word)
Token support: set GITHUB_TOKEN env var for 5000/h quota (vs 60/h)
Desc truncated to 200 chars to save tokens
4. Analyze & Use

Screen: Stars > 20, language matches project, updated < 2yr Read: WebFetch README for key info Use: Extract logic, adapt style, add // Reference: [URL] (or # Reference: for Python/Shell)

No results: Try broader keywords or WebSearch

Commands

Output: ⭐stars | lang | year | desc (sorted by stars)

Weekly Installs
12
Repository
ruiwarn/skills
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn