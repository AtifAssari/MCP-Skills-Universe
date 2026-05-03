---
title: firecrawl
url: https://skills.sh/ljt-520/openclaw-backup/firecrawl
---

# firecrawl

skills/ljt-520/openclaw-backup/firecrawl
firecrawl
Installation
$ npx skills add https://github.com/ljt-520/openclaw-backup --skill firecrawl
SKILL.md
Firecrawl

Web search and scraping via Firecrawl API.

Prerequisites

Set FIRECRAWL_API_KEY in your environment or .env file:

export FIRECRAWL_API_KEY=fc-xxxxxxxxxx

Quick Start
Search the web
firecrawl_search "your search query" --limit 10

Scrape a single page
firecrawl_scrape "https://example.com"

Crawl an entire site
firecrawl_crawl "https://example.com" --max-pages 50

API Reference

See references/api.md for detailed API documentation and advanced options.

Scripts
scripts/search.py - Search the web with Firecrawl
scripts/scrape.py - Scrape a single URL
scripts/crawl.py - Crawl an entire website
Weekly Installs
9
Repository
ljt-520/openclaw-backup
GitHub Stars
1
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn