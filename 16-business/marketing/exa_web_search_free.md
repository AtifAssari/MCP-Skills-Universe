---
rating: ⭐⭐
title: exa-web-search-free
url: https://skills.sh/sundial-org/awesome-openclaw-skills/exa-web-search-free
---

# exa-web-search-free

skills/sundial-org/awesome-openclaw-skills/exa-web-search-free
exa-web-search-free
Installation
$ npx skills add https://github.com/sundial-org/awesome-openclaw-skills --skill exa-web-search-free
Summary

Neural search across web, code, and company research without API keys.

Three core tools: web search for news and facts, code search for GitHub and Stack Overflow examples, and company research for business intelligence
Configurable search depth with type parameter ("fast" or "deep") for web queries and adjustable token ranges (1000–50000) for code context
Optional advanced tools available via config update, including domain/date filtering, query expansion, full page crawling, people search, and an AI research agent
Integrates via mcporter MCP server with simple command-line setup and no authentication required
SKILL.md
Exa Web Search (Free)

Neural search for web, code, and company research. No API key required.

Setup

Verify mcporter is configured:

mcporter list exa


If not listed:

mcporter config add exa https://mcp.exa.ai/mcp

Core Tools
web_search_exa

Search web for current info, news, or facts.

mcporter call 'exa.web_search_exa(query: "latest AI news 2026", numResults: 5)'


Parameters:

query - Search query
numResults (optional, default: 8)
type (optional) - "auto", "fast", or "deep"
get_code_context_exa

Find code examples and docs from GitHub, Stack Overflow.

mcporter call 'exa.get_code_context_exa(query: "React hooks examples", tokensNum: 3000)'


Parameters:

query - Code/API search query
tokensNum (optional, default: 5000) - Range: 1000-50000
company_research_exa

Research companies for business info and news.

mcporter call 'exa.company_research_exa(companyName: "Anthropic", numResults: 3)'


Parameters:

companyName - Company name
numResults (optional, default: 5)
Advanced Tools (Optional)

Six additional tools available by updating config URL:

web_search_advanced_exa - Domain/date filters
deep_search_exa - Query expansion
crawling_exa - Full page extraction
people_search_exa - Professional profiles
deep_researcher_start/check - AI research agent

Enable all tools:

mcporter config add exa-full "https://mcp.exa.ai/mcp?tools=web_search_exa,web_search_advanced_exa,get_code_context_exa,deep_search_exa,crawling_exa,company_research_exa,people_search_exa,deep_researcher_start,deep_researcher_check"

# Then use:
mcporter call 'exa-full.deep_search_exa(query: "AI safety research")'

Tips
Web: Use type: "fast" for quick lookup, "deep" for thorough research
Code: Lower tokensNum (1000-2000) for focused, higher (5000+) for comprehensive
See examples.md for more patterns
Resources
GitHub
npm
Docs
Weekly Installs
2.4K
Repository
sundial-org/awe…w-skills
GitHub Stars
589
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn