---
rating: ⭐⭐⭐
title: ask-search
url: https://skills.sh/ythx-101/ask-search/ask-search
---

# ask-search

skills/ythx-101/ask-search/ask-search
ask-search
Installation
$ npx skills add https://github.com/ythx-101/ask-search --skill ask-search
SKILL.md
ask-search

Web search powered by SearxNG. Aggregates multiple search engines, zero API key, full privacy.

Usage
ask-search "your query"                    # top 10 results
ask-search "query" --num 5                 # limit results
ask-search "AI news" --categories news     # news only
ask-search "query" --lang zh-CN            # Chinese results
ask-search "query" --urls-only             # URL list (pipe to web_fetch)
ask-search "query" --json                  # raw JSON

Agent Workflow
Run ask-search "topic" to get candidates
Check snippet — if enough, answer directly
If snippet truncated, use web_fetch on the URL for full content
Parameters
Flag	Short	Description
--num N	-n	Max results (default 10)
--engines	-e	google,bing,duckduckgo,brave
--lang	-l	zh-CN, en, ja, ko
--categories	-c	general,news,images,science
--json	-j	Raw JSON output
--urls-only	-u	URLs only
Setup

Requires SearxNG running locally. Set SEARXNG_URL if not on default port 8080.

Weekly Installs
45
Repository
ythx-101/ask-search
GitHub Stars
352
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn