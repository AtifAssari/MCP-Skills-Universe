---
title: tavily-map
url: https://skills.sh/tavily-ai/skills/tavily-map
---

# tavily-map

skills/tavily-ai/skills/tavily-map
tavily-map
Installation
$ npx skills add https://github.com/tavily-ai/skills --skill tavily-map
Summary

Fast URL discovery on websites without extracting content, ideal for finding specific pages on large sites.

Returns structured lists of all URLs on a domain with configurable depth and breadth, regex path filtering, and natural language instructions for semantic filtering
Supports depth control (1–5 levels), breadth limits per page, external link inclusion/exclusion, and domain filtering via regex patterns
Designed as step 1 in a workflow: map to find the right page, then use extract or crawl for content retrieval
Requires Tavily CLI (tvly) installed and authenticated; faster alternative to full-site crawling when you know the domain but not the exact page
SKILL.md
tavily map

Discover URLs on a website without extracting content. Faster than crawling.

Before running any command

If tvly is not found on PATH, install it first:

curl -fsSL https://cli.tavily.com/install.sh | bash && tvly login


Do not skip this step or fall back to other tools.

See tavily-cli for alternative install methods and auth options.

When to use
You need to find a specific subpage on a large site
You want a list of all URLs before deciding what to extract or crawl
Step 3 in the workflow: search → extract → map → crawl → research
Quick start
# Discover all URLs
tvly map "https://docs.example.com" --json

# With natural language filtering
tvly map "https://docs.example.com" --instructions "Find API docs and guides" --json

# Filter by path
tvly map "https://example.com" --select-paths "/blog/.*" --limit 500 --json

# Deep map
tvly map "https://example.com" --max-depth 3 --limit 200 --json

Options
Option	Description
--max-depth	Levels deep (1-5, default: 1)
--max-breadth	Links per page (default: 20)
--limit	Max URLs to discover (default: 50)
--instructions	Natural language guidance for URL filtering
--select-paths	Comma-separated regex patterns to include
--exclude-paths	Comma-separated regex patterns to exclude
--select-domains	Comma-separated regex for domains to include
--exclude-domains	Comma-separated regex for domains to exclude
--allow-external / --no-external	Include external links
--timeout	Max wait (10-150 seconds)
-o, --output	Save output to file
--json	Structured JSON output
Map + Extract pattern

Use map to find the right page, then extract it. This is often more efficient than crawling an entire site:

# Step 1: Find the authentication docs
tvly map "https://docs.example.com" --instructions "authentication" --json

# Step 2: Extract the specific page you found
tvly extract "https://docs.example.com/api/authentication" --json

Tips
Map is URL discovery only — no content extraction. Use extract or crawl for content.
Map + extract beats crawl when you only need a few specific pages from a large site.
Use --instructions for semantic filtering when path patterns aren't enough.
See also
tavily-extract — extract content from URLs you discover
tavily-crawl — bulk extract when you need many pages
Weekly Installs
5.2K
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