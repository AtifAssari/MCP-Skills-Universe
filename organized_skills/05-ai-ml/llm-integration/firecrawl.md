---
rating: ⭐⭐⭐
title: firecrawl
url: https://skills.sh/firecrawl/cli/firecrawl
---

# firecrawl

skills/firecrawl/cli/firecrawl
firecrawl
Installation
$ npx skills add https://github.com/firecrawl/cli --skill firecrawl
Summary

Web scraping, search, crawling, and browser automation with LLM-optimized markdown output.

Supports six command modes: search for discovery, scrape for single URLs, map to locate subpages, crawl for bulk site sections, browser for interactive content, and download for offline archives
Returns clean markdown formatted for LLM context windows; write results to .firecrawl/ directory to avoid redundant fetches and manage large outputs
Includes escalation workflow: start with search or scrape, use map to find specific URLs within sites, switch to browser when content requires clicks, form fills, or login interactions
Parallel job execution up to concurrency limit; check firecrawl --status for remaining credits and active job slots before running bulk operations
SKILL.md
Firecrawl CLI

Search, scrape, and interact with the web. Returns clean markdown optimized for LLM context windows.

Run firecrawl --help or firecrawl <command> --help for full option details.

If the task is to integrate Firecrawl into an application, add FIRECRAWL_API_KEY to a project, or choose endpoint usage in product code, use the firecrawl-build skills. They are already installed alongside this CLI skill when you run firecrawl init.

Prerequisites

Must be installed and authenticated. Check with firecrawl --status.

  🔥 firecrawl cli v1.8.0

  ● Authenticated via FIRECRAWL_API_KEY
  Concurrency: 0/100 jobs (parallel scrape limit)
  Credits: 500,000 remaining

Concurrency: Max parallel jobs. Run parallel operations up to this limit.
Credits: Remaining API credits. Each operation consumes credits.

If not ready, see rules/install.md. For output handling guidelines, see rules/security.md.

Before doing real work, verify the setup with one small request:

mkdir -p .firecrawl
firecrawl scrape "https://firecrawl.dev" -o .firecrawl/install-check.md

firecrawl search "query" --scrape --limit 3

Workflow

Follow this escalation pattern:

Search - No specific URL yet. Find pages, answer questions, discover sources.
Scrape - Have a URL. Extract its content directly.
Map + Scrape - Large site or need a specific subpage. Use map --search to find the right URL, then scrape it.
Crawl - Need bulk content from an entire site section (e.g., all /docs/).
Interact - Scrape first, then interact with the page (pagination, modals, form submissions, multi-step navigation).
Need	Command	When
Find pages on a topic	search	No specific URL yet
Get a page's content	scrape	Have a URL, page is static or JS-rendered
Find URLs within a site	map	Need to locate a specific subpage
Bulk extract a site section	crawl	Need many pages (e.g., all /docs/)
AI-powered data extraction	agent	Need structured data from complex sites
Interact with a page	scrape + interact	Content requires clicks, form fills, pagination, or login
Download a site to files	download	Save an entire site as local files
Parse a local file	parse	File on disk (PDF, DOCX, XLSX, etc.) — not a URL

For detailed command reference, run firecrawl <command> --help.

Scrape vs interact:

Use scrape first. It handles static pages and JS-rendered SPAs.
Use scrape + interact when you need to interact with a page, such as clicking buttons, filling out forms, navigating through a complex site, infinite scroll, or when scrape fails to grab all the content you need.
Never use interact for web searches - use search instead.

Avoid redundant fetches:

search --scrape already fetches full page content. Don't re-scrape those URLs.
Check .firecrawl/ for existing data before fetching again.
When to Load References
Searching the web or finding sources first -> firecrawl-search
Scraping a known URL -> firecrawl-scrape
Finding URLs on a known site -> firecrawl-map
Bulk extraction from a docs section or site -> firecrawl-crawl
AI-powered structured extraction from complex sites -> firecrawl-agent
Clicks, forms, login, pagination, or post-scrape browser actions -> firecrawl-interact
Downloading a site to local files -> firecrawl-download
Parsing a local file (PDF, DOCX, XLSX, HTML, etc.) -> firecrawl-parse
Install, auth, or setup problems -> rules/install.md
Output handling and safe file-reading patterns -> rules/security.md
Integrating Firecrawl into an app, adding FIRECRAWL_API_KEY to .env, or choosing endpoint usage in product code -> use the firecrawl-build skills (already installed alongside this CLI skill)
Output & Organization

Unless the user specifies to return in context, write results to .firecrawl/ with -o. Add .firecrawl/ to .gitignore. Always quote URLs - shell interprets ? and & as special characters.

firecrawl search "react hooks" -o .firecrawl/search-react-hooks.json --json
firecrawl scrape "<url>" -o .firecrawl/page.md


Naming conventions:

.firecrawl/search-{query}.json
.firecrawl/search-{query}-scraped.json
.firecrawl/{site}-{path}.md


Never read entire output files at once. Use grep, head, or incremental reads:

wc -l .firecrawl/file.md && head -50 .firecrawl/file.md
grep -n "keyword" .firecrawl/file.md


Single format outputs raw content. Multiple formats (e.g., --format markdown,links) output JSON.

Working with Results

These patterns are useful when working with file-based output (-o flag) for complex tasks:

# Extract URLs from search
jq -r '.data.web[].url' .firecrawl/search.json

# Get titles and URLs
jq -r '.data.web[] | "\(.title): \(.url)"' .firecrawl/search.json

Parallelization

Run independent operations in parallel. Check firecrawl --status for concurrency limit:

firecrawl scrape "<url-1>" -o .firecrawl/1.md &
firecrawl scrape "<url-2>" -o .firecrawl/2.md &
firecrawl scrape "<url-3>" -o .firecrawl/3.md &
wait


For interact, scrape multiple pages and interact with each independently using their scrape IDs.

Credit Usage
firecrawl credit-usage
firecrawl credit-usage --json --pretty -o .firecrawl/credits.json

Weekly Installs
46.5K
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