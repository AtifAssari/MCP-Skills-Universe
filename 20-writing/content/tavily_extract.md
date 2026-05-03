---
rating: ⭐⭐⭐
title: tavily-extract
url: https://skills.sh/tavily-ai/skills/tavily-extract
---

# tavily-extract

skills/tavily-ai/skills/tavily-extract
tavily-extract
Installation
$ npx skills add https://github.com/tavily-ai/skills --skill tavily-extract
Summary

Extract clean markdown or text from up to 20 URLs, with JavaScript rendering and query-focused chunking support.

Handles JavaScript-rendered pages with configurable extraction depth (basic for simple pages, advanced for dynamic SPAs and tables)
Supports query-focused extraction to return only relevant content chunks instead of full pages
Returns LLM-optimized markdown by default, with options for plain text format and structured JSON output
Processes up to 20 URLs in a single call; integrates into the Tavily workflow as the extraction step following search results
SKILL.md
tavily extract

Extract clean markdown or text content from one or more URLs.

Before running any command

If tvly is not found on PATH, install it first:

curl -fsSL https://cli.tavily.com/install.sh | bash && tvly login


Do not skip this step or fall back to other tools.

See tavily-cli for alternative install methods and auth options.

When to use
You have a specific URL and want its content
You need text from JavaScript-rendered pages
Step 2 in the workflow: search → extract → map → crawl → research
Quick start
# Single URL
tvly extract "https://example.com/article" --json

# Multiple URLs
tvly extract "https://example.com/page1" "https://example.com/page2" --json

# Query-focused extraction (returns relevant chunks only)
tvly extract "https://example.com/docs" --query "authentication API" --chunks-per-source 3 --json

# JS-heavy pages
tvly extract "https://app.example.com" --extract-depth advanced --json

# Save to file
tvly extract "https://example.com/article" -o article.md

Options
Option	Description
--query	Rerank chunks by relevance to this query
--chunks-per-source	Chunks per URL (1-5, requires --query)
--extract-depth	basic (default) or advanced (for JS pages)
--format	markdown (default) or text
--include-images	Include image URLs
--timeout	Max wait time (1-60 seconds)
-o, --output	Save output to file
--json	Structured JSON output
Extract depth
Depth	When to use
basic	Simple pages, fast — try this first
advanced	JS-rendered SPAs, dynamic content, tables
Tips
Max 20 URLs per request — batch larger lists into multiple calls.
Use --query + --chunks-per-source to get only relevant content instead of full pages.
Try basic first, fall back to advanced if content is missing.
Set --timeout for slow pages (up to 60s).
If search results already contain the content you need (via --include-raw-content), skip the extract step.
See also
tavily-search — find pages when you don't have a URL
tavily-crawl — extract content from many pages on a site
Weekly Installs
5.6K
Repository
tavily-ai/skills
GitHub Stars
259
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail