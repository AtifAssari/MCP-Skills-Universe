---
title: firecrawl-build-map
url: https://skills.sh/firecrawl/skills/firecrawl-build-map
---

# firecrawl-build-map

skills/firecrawl/skills/firecrawl-build-map
firecrawl-build-map
Installation
$ npx skills add https://github.com/firecrawl/skills --skill firecrawl-build-map
SKILL.md
Firecrawl Build Map

Use this when the product knows the site but not the exact URLs.

Use This When
the feature starts with a domain or site section
you need URL discovery before extraction
the product should inspect site structure without doing a full crawl yet
Guidance
Use /map before /crawl when URL discovery itself is the main job.
Combine /map with /scrape when you only need a filtered subset of pages.
Keep this as lighter coverage than /scrape, /search, and /interact unless the feature is navigation-heavy.
When Not To Use It
If you already have the exact URL, use firecrawl-build-scrape.
If the feature begins with a general query across the web, use firecrawl-build-search.
Docs (Source of Truth)

Read the docs for request/response schemas, parameters, and SDK examples before writing integration code:

docs.firecrawl.dev/features/map
See Also
firecrawl-build
firecrawl-build-search
firecrawl-build-crawl
Weekly Installs
554
Repository
firecrawl/skills
GitHub Stars
4
First Seen
Apr 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn