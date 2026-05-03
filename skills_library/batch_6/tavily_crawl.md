---
title: tavily-crawl
url: https://skills.sh/tavily-ai/skills/tavily-crawl
---

# tavily-crawl

skills/tavily-ai/skills/tavily-crawl
tavily-crawl
Installation
$ npx skills add https://github.com/tavily-ai/skills --skill tavily-crawl
Summary

Multi-page website crawler with semantic filtering and markdown export.

Crawl entire site sections with depth and breadth control; filter by path regex, domain, or natural language instructions to focus results
Save each page as local markdown files via --output-dir, or return structured JSON for agentic processing
Use semantic instructions with chunk extraction to prevent context bloat when feeding results to LLMs; use full-page extraction for offline documentation downloads
Supports external link following, image inclusion, timeout configuration, and regex-based path/domain filtering for precise scope control
SKILL.md
tavily crawl

Crawl a website and extract content from multiple pages. Supports saving each page as a local markdown file.

Before running any command

If tvly is not found on PATH, install it first:

curl -fsSL https://cli.tavily.com/install.sh | bash && tvly login


Do not skip this step or fall back to other tools.

See tavily-cli for alternative install methods and auth options.

When to use
You need content from many pages on a site (e.g., all /docs/)
You want to download documentation for offline use
Step 4 in the workflow: search → extract → map → crawl → research
Quick start
# Basic crawl
tvly crawl "https://docs.example.com" --json

# Save each page as a markdown file
tvly crawl "https://docs.example.com" --output-dir ./docs/

# Deeper crawl with limits
tvly crawl "https://docs.example.com" --max-depth 2 --limit 50 --json

# Filter to specific paths
tvly crawl "https://example.com" --select-paths "/api/.*,/guides/.*" --exclude-paths "/blog/.*" --json

# Semantic focus (returns relevant chunks, not full pages)
tvly crawl "https://docs.example.com" --instructions "Find authentication docs" --chunks-per-source 3 --json

Options
Option	Description
--max-depth	Levels deep (1-5, default: 1)
--max-breadth	Links per page (default: 20)
--limit	Total pages cap (default: 50)
--instructions	Natural language guidance for semantic focus
--chunks-per-source	Chunks per page (1-5, requires --instructions)
--extract-depth	basic (default) or advanced
--format	markdown (default) or text
--select-paths	Comma-separated regex patterns to include
--exclude-paths	Comma-separated regex patterns to exclude
--select-domains	Comma-separated regex for domains to include
--exclude-domains	Comma-separated regex for domains to exclude
--allow-external / --no-external	Include external links (default: allow)
--include-images	Include images
--timeout	Max wait (10-150 seconds)
-o, --output	Save JSON output to file
--output-dir	Save each page as a .md file in directory
--json	Structured JSON output
Crawl for context vs. data collection

For agentic use (feeding results to an LLM):

Always use --instructions + --chunks-per-source. Returns only relevant chunks instead of full pages — prevents context explosion.

tvly crawl "https://docs.example.com" --instructions "API authentication" --chunks-per-source 3 --json


For data collection (saving to files):

Use --output-dir without --chunks-per-source to get full pages as markdown files.

tvly crawl "https://docs.example.com" --max-depth 2 --output-dir ./docs/

Tips
Start conservative — --max-depth 1, --limit 20 — and scale up.
Use --select-paths to focus on the section you need.
Use map first to understand site structure before a full crawl.
Always set --limit to prevent runaway crawls.
See also
tavily-map — discover URLs before deciding to crawl
tavily-extract — extract individual pages
tavily-search — find pages when you don't have a URL
Weekly Installs
5.4K
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