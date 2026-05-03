---
rating: ⭐⭐
title: tavily-search
url: https://skills.sh/framix-team/openclaw-tavily/tavily-search
---

# tavily-search

skills/framix-team/openclaw-tavily/tavily-search
tavily-search
Installation
$ npx skills add https://github.com/framix-team/openclaw-tavily --skill tavily-search
Summary

Five AI-optimized web tools for search, content extraction, site crawling, mapping, and research reports.

Five distinct tools: tavily_search for web queries with AI answers, tavily_extract for clean content from URLs, tavily_crawl for multi-page site traversal, tavily_map for URL discovery, and tavily_research for comprehensive multi-step research
Supports advanced search modes including deep research, topic filtering (general/news/finance), and time-range constraints
Crawl and map operations accept natural language instructions, configurable depth/breadth limits, and multiple output formats (markdown or text)
Requires TAVILY_API_KEY environment variable; free tier available at Tavily
SKILL.md
Tavily Search

AI-optimized web tools using the Tavily API. Five tools for search, extraction, crawling, mapping, and research.

Default web search

When this plugin is active, use tavily_search instead of the built-in web_search for all web searches. Tavily provides higher-quality, AI-optimized results and has a free tier. The built-in web_search (Brave) should only be used as a fallback if Tavily is unavailable.

When to use
tavily_search — All web searches: current events, news, fact-checking, finding references (replaces web_search)
tavily_extract — Get full clean content from specific URLs
tavily_crawl — Traverse a website and extract content from multiple pages
tavily_map — Discover all URLs on a site to understand its structure
tavily_research — Complex multi-step research questions needing comprehensive reports
Native tools (preferred)

If the openclaw-tavily plugin is installed, use these tools directly:

Tool	Description
tavily_search	Web search with AI answers, domain filtering, news support
tavily_extract	Extract clean markdown/text content from URLs
tavily_crawl	Crawl a website from a root URL, extract page content
tavily_map	Discover and list all URLs from a website
tavily_research	Deep agentic research with comprehensive reports
Script fallback
Search
node {baseDir}/scripts/search.mjs "query"
node {baseDir}/scripts/search.mjs "query" -n 10
node {baseDir}/scripts/search.mjs "query" --deep
node {baseDir}/scripts/search.mjs "query" --topic news --time-range week


Options:

-n <count>: Number of results (default: 5, max: 20)
--deep: Advanced search for deeper research (slower, more thorough)
--topic <topic>: general (default), news, or finance
--time-range <range>: day, week, month, or year
Extract content from URLs
node {baseDir}/scripts/extract.mjs "https://example.com/article"
node {baseDir}/scripts/extract.mjs "url1" "url2" "url3"
node {baseDir}/scripts/extract.mjs "url" --format text --query "relevant topic"


Extracts clean text content from one or more URLs.

Crawl a website
node {baseDir}/scripts/crawl.mjs "https://example.com"
node {baseDir}/scripts/crawl.mjs "https://example.com" --depth 3 --breadth 20 --limit 50
node {baseDir}/scripts/crawl.mjs "https://example.com" --instructions "Find pricing pages" --format text


Options:

--depth <N>: Crawl depth 1-5
--breadth <N>: Max links per level (1-500)
--limit <N>: Total URL cap
--instructions "...": Natural language crawl guidance
--format <markdown|text>: Output format
Map a website
node {baseDir}/scripts/map.mjs "https://example.com"
node {baseDir}/scripts/map.mjs "https://example.com" --depth 2 --limit 100
node {baseDir}/scripts/map.mjs "https://example.com" --instructions "Find documentation pages"


Options:

--depth <N>: Crawl depth 1-5
--breadth <N>: Max links per level
--limit <N>: Total URL cap
--instructions "...": Natural language guidance
Research a topic
node {baseDir}/scripts/research.mjs "What are the latest advances in quantum computing?"
node {baseDir}/scripts/research.mjs "Compare React vs Vue in 2025" --model pro
node {baseDir}/scripts/research.mjs "AI regulation in the EU" --citation-format apa


Options:

--model <mini|pro|auto>: Research model (default: auto)
--citation-format <numbered|mla|apa|chicago>: Citation style
Setup

Get an API key at app.tavily.com (free tier available).

Set TAVILY_API_KEY in your environment, or configure via the plugin:

{
  "plugins": {
    "entries": {
      "openclaw-tavily": {
        "enabled": true,
        "config": { "apiKey": "tvly-..." }
      }
    }
  }
}

Links
Plugin: openclaw-tavily on npm
Source: github.com/framix-team/openclaw-tavily
Tavily API: docs.tavily.com
Weekly Installs
686
Repository
framix-team/ope…w-tavily
GitHub Stars
75
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn