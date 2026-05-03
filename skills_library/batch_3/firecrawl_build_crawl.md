---
title: firecrawl-build-crawl
url: https://skills.sh/firecrawl/skills/firecrawl-build-crawl
---

# firecrawl-build-crawl

skills/firecrawl/skills/firecrawl-build-crawl
firecrawl-build-crawl
Installation
$ npx skills add https://github.com/firecrawl/skills --skill firecrawl-build-crawl
SKILL.md
Firecrawl Build Crawl

Use this when the product needs many pages from the same site, not just one.

Use This When
the feature targets a docs section, blog, or help center
you need bulk extraction with path or depth boundaries
the product should ingest or refresh a site section at once
Guidance
Keep crawl scope narrow with path, depth, or page-count constraints.
Prefer /crawl over many manual /scrape calls when the site structure is stable.
Treat this as secondary to /scrape, /search, and /interact unless the feature is clearly site-wide.
When Not To Use It
If you only need one known URL, use firecrawl-build-scrape.
If you first need to discover URLs on a single site, start with firecrawl-build-map.
Docs (Source of Truth)

Read the docs for request/response schemas, parameters, and SDK examples before writing integration code:

docs.firecrawl.dev/features/crawl
See Also
firecrawl-build
firecrawl-build-map
firecrawl-build-scrape
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