---
title: tavily
url: https://skills.sh/site/skills.volces.com/tavily
---

# tavily

skills/skills.volces.com/tavily
tavily
$ npx skills add https://skills.volces.com/skills/clawhub/yi307520559-droid
SKILL.md
Tavily Search

AI-optimized web search using Tavily API. Designed for AI agents - returns clean, relevant content.

Search
node {baseDir}/scripts/search.mjs "query"
node {baseDir}/scripts/search.mjs "query" -n 10
node {baseDir}/scripts/search.mjs "query" --deep
node {baseDir}/scripts/search.mjs "query" --topic news

Options
-n <count>: Number of results (default: 5, max: 20)
--deep: Use advanced search for deeper research (slower, more comprehensive)
--topic <topic>: Search topic - general (default) or news
--days <n>: For news topic, limit to last n days
Extract content from URL
node {baseDir}/scripts/extract.mjs "https://example.com/article"


Notes:

Needs TAVILY_API_KEY from https://tavily.com
Tavily is optimized for AI - returns clean, relevant snippets
Use --deep for complex research questions
Use --topic news for current events
Weekly Installs
311
Source
skills.volces.c…59-droid
First Seen
Mar 11, 2026
Security Audits
SocketPass