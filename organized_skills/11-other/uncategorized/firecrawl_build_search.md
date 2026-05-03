---
rating: ⭐⭐
title: firecrawl-build-search
url: https://skills.sh/firecrawl/skills/firecrawl-build-search
---

# firecrawl-build-search

skills/firecrawl/skills/firecrawl-build-search
firecrawl-build-search
Installation
$ npx skills add https://github.com/firecrawl/skills --skill firecrawl-build-search
SKILL.md
Firecrawl Build Search

Use this when the application starts with a query, not a URL.

Use This When
the user asks a question and the product must discover sources first
the feature needs current web results
you want to turn a search query into a shortlist of pages for later scraping
Default Recommendations
Use /search first when URL discovery is part of the product behavior.
Keep search and extraction conceptually separate unless scraping search results is clearly required.
Prefer selective follow-up extraction over broad hydration when cost or latency matters.
Common Product Patterns
answer generation with cited sources
company, competitor, or topic discovery
research workflows that produce a shortlist before deeper extraction
query-to-URL pipelines for later /scrape or /interact
Escalation Rules
If you already have the URL, use firecrawl-build-scrape.
If the result page then requires clicks or form interaction, escalate to firecrawl-build-interact.
Implementation Notes
Treat /search as discovery, ranking, and source selection.
Be explicit about whether the product needs snippets, URLs, or full result content.
Keep the query contract stable so downstream scraping logic stays predictable.
Docs (Source of Truth)

Read the source-of-truth page for your project language before writing integration code:

Node / TypeScript: docs.firecrawl.dev/agent-source-of-truth/node
Python: docs.firecrawl.dev/agent-source-of-truth/python
Rust: docs.firecrawl.dev/agent-source-of-truth/rust
Java: docs.firecrawl.dev/agent-source-of-truth/java
Elixir: docs.firecrawl.dev/agent-source-of-truth/elixir
cURL / REST: docs.firecrawl.dev/agent-source-of-truth/curl
See Also
firecrawl-build
firecrawl-build-scrape
firecrawl-build-interact
Weekly Installs
16.5K
Repository
firecrawl/skills
GitHub Stars
4
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn