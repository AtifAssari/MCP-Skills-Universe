---
rating: ⭐⭐
title: mcp-duckgo
url: https://skills.sh/aahl/skills/mcp-duckgo
---

# mcp-duckgo

skills/aahl/skills/mcp-duckgo
mcp-duckgo
Installation
$ npx skills add https://github.com/aahl/skills --skill mcp-duckgo
Summary

Web search and content scraping via DuckDuckGo with configurable result limits.

Provides two core commands: search for querying the web with customizable result counts, and fetch_content for scraping full page content from URLs
Integrates with the DuckDuckGo MCP Server for real-time search results and webpage extraction
Useful for agents that need to gather current information, verify facts, or extract text from live web pages
SKILL.md
DuckDuckGo Search

Executing Shell commands.

Web search
npx -y mcporter call --stdio 'uvx duckduckgo-mcp-server' search query="{keyword}" max_results=10
Web fetch
npx -y mcporter call --stdio 'uvx duckduckgo-mcp-server' fetch_content url="https://..."
Weekly Installs
1.3K
Repository
aahl/skills
GitHub Stars
120
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn