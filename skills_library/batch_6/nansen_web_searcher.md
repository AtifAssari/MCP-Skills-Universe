---
title: nansen-web-searcher
url: https://skills.sh/nansen-ai/nansen-cli/nansen-web-searcher
---

# nansen-web-searcher

skills/nansen-ai/nansen-cli/nansen-web-searcher
nansen-web-searcher
Installation
$ npx skills add https://github.com/nansen-ai/nansen-cli --skill nansen-web-searcher
SKILL.md
Web Search

Search the web for one or more queries in parallel via the Serper API.

nansen web search "bitcoin price"
nansen web search "solana ecosystem news" --num-results 5
nansen web search --query "ethereum ETF" --query "bitcoin ETF" --num-results 3


Positional args and --query flags can be combined — all become queries.

Flag	Values	Default	Purpose
--query	string	—	Query string (repeatable for multiple queries)
--num-results	1–20	10	Results per query
--pretty	flag	off	Human-readable JSON

Returns results[] — one entry per query, each with organic[] (title, link, snippet, date) and optional knowledge_graph.

Note: Some domains are excluded from results (paywalled/unfetchable sites like bloomberg.com, twitter.com). Use nansen web fetch to retrieve content from specific URLs.

Weekly Installs
262
Repository
nansen-ai/nansen-cli
GitHub Stars
121
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn