---
title: people-research
url: https://skills.sh/exa-labs/exa-mcp-server/people-research
---

# people-research

skills/exa-labs/exa-mcp-server/people-research
people-research
Installation
$ npx skills add https://github.com/exa-labs/exa-mcp-server --skill people-research
SKILL.md
People Research
Tool Restriction (Critical)

ONLY use web_search_advanced_exa. Do NOT use web_search_exa or any other Exa tools.

Token Isolation (Critical)

Never run Exa searches in main context. Always spawn Task agents:

Agent runs Exa search internally
Agent processes results using LLM intelligence
Agent returns only distilled output (compact JSON or brief markdown)
Main context stays clean regardless of search volume
Dynamic Tuning

No hardcoded numResults. Tune to user intent:

User says "a few" → 10-20
User says "comprehensive" → 50-100
User specifies number → match it
Ambiguous? Ask: "How many profiles would you like?"
Query Variation

Exa returns different results for different phrasings. For coverage:

Generate 2-3 query variations
Run in parallel
Merge and deduplicate
Categories

Use appropriate Exa category depending on what you need:

people → LinkedIn profiles, public bios (primary for discovery)
personal site → personal blogs, portfolio sites, about pages
news → press mentions, interviews, speaker bios
No category (type: "auto") → general web results, broader context

Start with category: "people" for profile discovery, then use other categories or no category for deeper research on specific individuals.

Category-Specific Filter Restrictions

When using category: "people", these parameters cause errors:

startPublishedDate / endPublishedDate
startCrawlDate / endCrawlDate
includeText / excludeText
excludeDomains
includeDomains — LinkedIn domains only (e.g., "linkedin.com")

When searching without a category, all parameters are available (but includeText/excludeText still only support single-item arrays).

LinkedIn

Public LinkedIn via Exa: category: "people", no other filters. Auth-required LinkedIn → use Claude in Chrome browser fallback.

Browser Fallback

Auto-fallback to Claude in Chrome when:

Exa returns insufficient results
Content is auth-gated
Dynamic pages need JavaScript
Examples
Discovery: find people by role
web_search_advanced_exa {
  "query": "VP Engineering AI infrastructure",
  "category": "people",
  "numResults": 20,
  "type": "auto"
}

With query variations
web_search_advanced_exa {
  "query": "machine learning engineer San Francisco",
  "category": "people",
  "additionalQueries": ["ML engineer SF", "AI engineer Bay Area"],
  "numResults": 25,
  "type": "deep"
}

Deep dive: research a specific person
web_search_advanced_exa {
  "query": "Dario Amodei Anthropic CEO background",
  "type": "auto",
  "numResults": 15
}

News mentions
web_search_advanced_exa {
  "query": "Dario Amodei interview",
  "category": "news",
  "numResults": 10,
  "startPublishedDate": "2024-01-01"
}

Output Format

Return:

Results (name, title, company, location if available)
Sources (Profile URLs)
Notes (profile completeness, verification status)
Weekly Installs
61
Repository
exa-labs/exa-mcp-server
GitHub Stars
4.4K
First Seen
Feb 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn