---
title: firecrawl
url: https://skills.sh/tumf/skills/firecrawl
---

# firecrawl

skills/tumf/skills/firecrawl
firecrawl
Installation
$ npx skills add https://github.com/tumf/skills --skill firecrawl
SKILL.md
Firecrawl Web Scraping & Data Extraction
Installation
pip install firecrawl-py

Environment Setup

Set your Firecrawl API key:

export FIRECRAWL_API_KEY="your-api-key-here"

Scripts

Note: Set SKILL_ROOT to this skill's base directory. Reference bundled scripts as python3 "$SKILL_ROOT/scripts/<script>.py" ... (not relative paths from the current working directory).

scrape.py - Single Page Scraping

The most powerful and reliable scraper. Use when you know exactly which page contains the information.

# Basic scrape (returns markdown)
python3 "$SKILL_ROOT/scripts/scrape.py" "https://example.com"

# Get HTML format
python3 "$SKILL_ROOT/scripts/scrape.py" "https://example.com" --format html

# Extract only main content (removes headers, footers, etc.)
python3 "$SKILL_ROOT/scripts/scrape.py" "https://example.com" --only-main

# Combine options
python3 "$SKILL_ROOT/scripts/scrape.py" "https://docs.example.com/api" --format markdown --only-main

search.py - Web Search

Search the web when you don't know which website has the information.

# Basic search
python3 "$SKILL_ROOT/scripts/search.py" "latest AI research papers 2024"

# Limit results
python3 "$SKILL_ROOT/scripts/search.py" "Python web scraping tutorials" --limit 5

# Search with scraping (get full content)
python3 "$SKILL_ROOT/scripts/search.py" "firecrawl documentation" --limit 3

map.py - URL Discovery

Discover all URLs on a website. Use before deciding what to scrape.

# Map a website
python3 "$SKILL_ROOT/scripts/map.py" "https://docs.example.com"

# Limit number of URLs
python3 "$SKILL_ROOT/scripts/map.py" "https://example.com" --limit 100

# Search within mapped URLs
python3 "$SKILL_ROOT/scripts/map.py" "https://docs.example.com" --search "authentication"

crawl.py - Multi-Page Crawling

Extract content from multiple related pages. Warning: can be slow and return large results.

# Basic crawl
python3 "$SKILL_ROOT/scripts/crawl.py" "https://docs.example.com"

# Limit pages
python3 "$SKILL_ROOT/scripts/crawl.py" "https://docs.example.com" --limit 20

# Control crawl depth
python3 "$SKILL_ROOT/scripts/crawl.py" "https://docs.example.com" --limit 10 --depth 2

extract.py - Structured Data Extraction

Extract specific structured data using LLM capabilities.

# Extract with prompt
python3 "$SKILL_ROOT/scripts/extract.py" "https://example.com/pricing" \
  --prompt "Extract all pricing tiers with their features and prices"

# Extract with JSON schema
python3 "$SKILL_ROOT/scripts/extract.py" "https://example.com/team" \
  --prompt "Extract team member information" \
  --schema '{"type":"object","properties":{"members":{"type":"array","items":{"type":"object","properties":{"name":{"type":"string"},"role":{"type":"string"},"bio":{"type":"string"}}}}}}'

# Extract from multiple URLs
python3 "$SKILL_ROOT/scripts/extract.py" "https://example.com/page1" "https://example.com/page2" \
  --prompt "Extract product information"

agent.py - Autonomous Data Gathering

Autonomous agent that searches, navigates, and extracts data from anywhere on the web.

# Simple research task
python3 "$SKILL_ROOT/scripts/agent.py" --prompt "Find the founders of Firecrawl and their backgrounds"

# Complex data gathering
python3 "$SKILL_ROOT/scripts/agent.py" --prompt "Find the top 5 AI startups founded in 2024 and their funding amounts"

# Focus on specific URLs
python3 "$SKILL_ROOT/scripts/agent.py" \
  --prompt "Compare the features and pricing" \
  --urls "https://example1.com,https://example2.com"

# With output schema
python3 "$SKILL_ROOT/scripts/agent.py" \
  --prompt "Find recent tech layoffs" \
  --schema '{"type":"object","properties":{"layoffs":{"type":"array","items":{"type":"object","properties":{"company":{"type":"string"},"count":{"type":"number"},"date":{"type":"string"}}}}}}'

Output Format

All scripts output JSON to stdout. Errors are written to stderr.

Success Response
{
  "success": true,
  "data": { ... }
}

Error Response
{
  "success": false,
  "error": "Error message"
}

Tips
Performance: Use scrape for single pages - it's 500% faster with caching
Discovery: Use map first to find URLs, then scrape specific pages
Large sites: Prefer map + scrape over crawl for better control
Structured data: Use extract with a JSON schema for consistent output
Research: Use agent when you don't know where to find the data
Weekly Installs
53
Repository
tumf/skills
GitHub Stars
3
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn