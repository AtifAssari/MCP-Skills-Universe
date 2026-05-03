---
rating: ⭐⭐⭐
title: firecrawl-search
url: https://skills.sh/firecrawl/cli/firecrawl-search
---

# firecrawl-search

skills/firecrawl/cli/firecrawl-search
firecrawl-search
Installation
$ npx skills add https://github.com/firecrawl/cli --skill firecrawl-search
Summary

Web search with optional full-page content extraction from results.

Returns real search results as JSON with optional --scrape flag to fetch complete page markdown for each result, avoiding redundant fetches
Supports filtering by source type (web, images, news), category (GitHub, research, PDF), time range (past hour/day/week/month/year), location, and country
Use --limit to control result count and --scrape-formats to customize output formats when extracting full content
Part of a workflow escalation pattern: search first to discover URLs, then use dedicated scrape/map/crawl skills for deeper extraction
SKILL.md
firecrawl search

Web search with optional content scraping. Returns search results as JSON, optionally with full page content.

When to use
You don't have a specific URL yet
You need to find pages, answer questions, or discover sources
First step in the workflow escalation pattern: search → scrape → map → crawl → interact
Quick start
# Basic search
firecrawl search "your query" -o .firecrawl/result.json --json

# Search and scrape full page content from results
firecrawl search "your query" --scrape -o .firecrawl/scraped.json --json

# News from the past day
firecrawl search "your query" --sources news --tbs qdr:d -o .firecrawl/news.json --json

Options
Option	Description
--limit <n>	Max number of results
--sources <web,images,news>	Source types to search
--categories <github,research,pdf>	Filter by category
--tbs <qdr:h|d|w|m|y>	Time-based search filter
--location	Location for search results
--country <code>	Country code for search
--scrape	Also scrape full page content for each result
--scrape-formats	Formats when scraping (default: markdown)
-o, --output <path>	Output file path
--json	Output as JSON
Tips
--scrape fetches full content — don't re-scrape URLs from search results. This saves credits and avoids redundant fetches.
Always write results to .firecrawl/ with -o to avoid context window bloat.
Use jq to extract URLs or titles: jq -r '.data.web[].url' .firecrawl/search.json
Naming convention: .firecrawl/search-{query}.json or .firecrawl/search-{query}-scraped.json
See also
firecrawl-scrape — scrape a specific URL
firecrawl-map — discover URLs within a site
firecrawl-crawl — bulk extract from a site
Weekly Installs
32.9K
Repository
firecrawl/cli
GitHub Stars
362
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn