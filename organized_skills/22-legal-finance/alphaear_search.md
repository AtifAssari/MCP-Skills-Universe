---
rating: ⭐⭐
title: alphaear-search
url: https://skills.sh/rkiding/awesome-finance-skills/alphaear-search
---

# alphaear-search

skills/rkiding/awesome-finance-skills/alphaear-search
alphaear-search
Installation
$ npx skills add https://github.com/rkiding/awesome-finance-skills --skill alphaear-search
SKILL.md
AlphaEar Search Skill
Overview

Unified search capabilities: web search (Jina/DDG/Baidu) and local RAG search.

Capabilities
1. Web Search

Use scripts/search_tools.py via SearchTools.

Search: search(query, engine, max_results)
Engines: jina, ddg, baidu, local.
Returns: JSON string (summary) or List[Dict] (via search_list).
Smart Cache (Agentic): If you want to avoid redundant searches, use the Search Cache Relevance Prompt in references/PROMPTS.md. Read the cache first and decide if it's usable.
Aggregate: aggregate_search(query)
Combines results from multiple engines.
2. Local RAG

Use scripts/hybrid_search.py or SearchTools with engine='local'.

Search: Searches local daily_news database.
Dependencies
duckduckgo-search, requests
scripts/database_manager.py (search cache & local news)
Weekly Installs
256
Repository
rkiding/awesome…e-skills
GitHub Stars
2.0K
First Seen
Feb 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn