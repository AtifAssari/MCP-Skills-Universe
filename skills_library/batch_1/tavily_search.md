---
title: tavily-search
url: https://skills.sh/veithly/tavily-search/tavily-search
---

# tavily-search

skills/veithly/tavily-search/tavily-search
tavily-search
Installation
$ npx skills add https://github.com/veithly/tavily-search --skill tavily-search
Summary

Web search optimized for AI agents with real-time data retrieval.

Single command interface (scripts/search) for querying the web with results tailored for agent consumption
Supports JSON output formatting for structured data integration into agent workflows
Requires Tavily API key for authentication; free API key available from tavily.com
SKILL.md
Tavily Search

Web search optimized for AI agents using Tavily API.

Usage
./scripts/search "your search query"

Scripts
Script	Usage
scripts/search <query>	Search the web
scripts/search "latest AI news" --format json	JSON output
Environment
export TAVILY_API_KEY="your-api-key"


Get API key: https://tavily.com/

Example
./scripts/search "Claude AI latest features"
# Returns: Search results optimized for AI context

Weekly Installs
3.6K
Repository
veithly/tavily-search
GitHub Stars
4
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn