---
rating: ⭐⭐⭐
title: firecrawl-map
url: https://skills.sh/firecrawl/cli/firecrawl-map
---

# firecrawl-map

skills/firecrawl/cli/firecrawl-map
firecrawl-map
Installation
$ npx skills add https://github.com/firecrawl/cli --skill firecrawl-map
Summary

Discover and filter URLs on a website, with optional search to locate specific pages.

Supports filtering by search query to find pages matching keywords within large sites
Includes sitemap handling strategies (include, skip, or use only) and optional subdomain inclusion
Outputs results as plain text or JSON with configurable URL limits
Commonly paired with firecrawl-scrape: use map with search to find the target URL, then scrape it
SKILL.md
firecrawl map

Discover URLs on a site. Use --search to find a specific page within a large site.

When to use
You need to find a specific subpage on a large site
You want a list of all URLs on a site before scraping or crawling
Step 3 in the workflow escalation pattern: search → scrape → map → crawl → interact
Quick start
# Find a specific page on a large site
firecrawl map "<url>" --search "authentication" -o .firecrawl/filtered.txt

# Get all URLs
firecrawl map "<url>" --limit 500 --json -o .firecrawl/urls.json

Options
Option	Description
--limit <n>	Max number of URLs to return
--search <query>	Filter URLs by search query
--sitemap <include|skip|only>	Sitemap handling strategy
--include-subdomains	Include subdomain URLs
--json	Output as JSON
-o, --output <path>	Output file path
Tips
Map + scrape is a common pattern: use map --search to find the right URL, then scrape it.
Example: map https://docs.example.com --search "auth" → found /docs/api/authentication → scrape that URL.
See also
firecrawl-scrape — scrape the URLs you discover
firecrawl-crawl — bulk extract instead of map + scrape
firecrawl-download — download entire site (uses map internally)
Weekly Installs
32.3K
Repository
firecrawl/cli
GitHub Stars
364
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn