---
title: cctv-news-fetcher
url: https://skills.sh/kirkluokun/awesome-a-stock-openclawskills/cctv-news-fetcher
---

# cctv-news-fetcher

skills/kirkluokun/awesome-a-stock-openclawskills/cctv-news-fetcher
cctv-news-fetcher
Installation
$ npx skills add https://github.com/kirkluokun/awesome-a-stock-openclawskills --skill cctv-news-fetcher
SKILL.md
CCTV News Fetcher

This skill allows you to fetch summary titles and content from the CCTV News Broadcast for any specific date.

Usage

You can ask the agent to:

"Fetch CCTV news for 20250210"
"Give me the news highlights for yesterday"
Instructions

When the user asks for news from a specific date:

Format the date as YYYYMMDD. If the user says "yesterday" or "today", calculate the date relative to the current local time.
Execute the script at {baseDir}/scripts/news_crawler.js using bun or node.
Command: bun {baseDir}/scripts/news_crawler.js <YYYYMMDD>
Parse the JSON output and summarize it for the user. Group news by "Domestic" and "International" if possible based on titles, or just list the highlights.
Configuration

The skill depends on node-html-parser. Ensure bun is installed in the environment.

Weekly Installs
57
Repository
kirkluokun/awes…awskills
GitHub Stars
41
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn