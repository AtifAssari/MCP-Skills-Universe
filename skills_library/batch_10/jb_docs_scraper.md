---
title: jb-docs-scraper
url: https://skills.sh/bjesuiter/skills/jb-docs-scraper
---

# jb-docs-scraper

skills/bjesuiter/skills/jb-docs-scraper
jb-docs-scraper
Installation
$ npx skills add https://github.com/bjesuiter/skills --skill jb-docs-scraper
SKILL.md
Documentation Scraper

Scrape any documentation website into local markdown files. Uses crawl4ai for async web crawling.

Quick Start
# Scrape any documentation URL
uv run --with crawl4ai python ./references/scrape_docs.py <URL>

# Examples
uv run --with crawl4ai python ./references/scrape_docs.py https://mediasoup.org/documentation/v3/
uv run --with crawl4ai python ./references/scrape_docs.py https://docs.rombo.co/tailwind


Output goes to ./docs/<auto-detected-name>/ by default.

Prerequisites (First Time Only)
uv run --with crawl4ai playwright install

Usage
uv run --with crawl4ai python ./references/scrape_docs.py <URL> [OPTIONS]

Options
Option	Description	Default
-o, --output PATH	Output directory	./docs/<auto-detected-name>
--max-depth N	Maximum link depth	6
--max-pages N	Maximum pages to scrape	500
--url-pattern PATTERN	URL filter (glob)	Auto-detected
-q, --quiet	Suppress verbose output	False
Examples
# Basic - scrape to ./docs/documentation_v3/
uv run --with crawl4ai python ./references/scrape_docs.py \
  https://mediasoup.org/documentation/v3/

# Custom output directory
uv run --with crawl4ai python ./references/scrape_docs.py \
  https://docs.rombo.co/tailwind \
  --output ./my-tailwind-docs

# Limit crawl scope
uv run --with crawl4ai python ./references/scrape_docs.py \
  https://tanstack.com/start/latest/docs/framework/react/overview \
  --max-pages 50 \
  --max-depth 3

# Custom URL pattern filter
uv run --with crawl4ai python ./references/scrape_docs.py \
  https://example.com/docs/api/v2/ \
  --url-pattern "*api/v2/*"

How It Works
Auto-detects domain and URL pattern from the input URL
Crawls using BFS (breadth-first search) strategy
Filters to stay within the documentation section
Converts pages to clean markdown
Saves with directory structure mirroring the URL paths
Output Structure
docs/<name>/
  index.md           # Root page
  getting-started.md
  api/
    overview.md
    client.md
  guides/
    installation.md

Troubleshooting
Issue	Solution
Playwright browser binaries are missing	Run uv run --with crawl4ai playwright install
Empty output	Check if URL pattern matches actual doc URLs. Try --url-pattern
Missing pages	Increase --max-depth or --max-pages
Wrong pages scraped	Use stricter --url-pattern
Tips
Test first - Use --max-pages 10 to verify config before full crawl
Check output name - Script auto-detects from URL path segments
Rerun safe - Files are overwritten, duplicates skipped
Weekly Installs
13
Repository
bjesuiter/skills
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn