---
title: firecrawl-scrape
url: https://skills.sh/parcadei/continuous-claude-v3/firecrawl-scrape
---

# firecrawl-scrape

skills/parcadei/continuous-claude-v3/firecrawl-scrape
firecrawl-scrape
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill firecrawl-scrape
SKILL.md
Firecrawl Scrape Skill
When to Use
Scrape content from any URL
Extract structured data from web pages
Search the web and get content
Instructions
uv run python -m runtime.harness scripts/mcp/firecrawl_scrape.py \
    --url "https://example.com" \
    --format "markdown"

Parameters
--url: URL to scrape
--format: Output format - markdown, html, text (default: markdown)
--search: (alternative) Search query instead of direct URL
Examples
# Scrape a page
uv run python -m runtime.harness scripts/mcp/firecrawl_scrape.py \
    --url "https://docs.python.org/3/library/asyncio.html"

# Search and scrape
uv run python -m runtime.harness scripts/mcp/firecrawl_scrape.py \
    --search "Python asyncio best practices 2024"

MCP Server Required

Requires firecrawl server in mcp_config.json with FIRECRAWL_API_KEY.

Weekly Installs
306
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn