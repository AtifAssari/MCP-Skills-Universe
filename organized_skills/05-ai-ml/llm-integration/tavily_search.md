---
rating: ⭐⭐⭐
title: tavily-search
url: https://skills.sh/tavily-ai/skills/tavily-search
---

# tavily-search

skills/tavily-ai/skills/tavily-search
tavily-search
Installation
$ npx skills add https://github.com/tavily-ai/skills --skill tavily-search
Summary

Web search with LLM-optimized results, content snippets, and relevance scores.

Supports four search depths (ultra-fast, fast, basic, advanced) with configurable result counts up to 20, plus domain filtering and time-range constraints
Returns structured JSON output with content snippets, relevance scores, and metadata optimized for LLM consumption
Includes specialized search modes for news and finance topics, with optional AI-generated answers and full page content extraction
Integrates into multi-step research workflows: search → extract → map → crawl → research
SKILL.md
tavily search

Web search returning LLM-optimized results with content snippets and relevance scores.

Before running any command

If tvly is not found on PATH, install it first:

curl -fsSL https://cli.tavily.com/install.sh | bash && tvly login


Do not skip this step or fall back to other tools.

See tavily-cli for alternative install methods and auth options.

When to use
You need to find information on any topic
You don't have a specific URL yet
First step in the workflow: search → extract → map → crawl → research
Quick start
# Basic search
tvly search "your query" --json

# Advanced search with more results
tvly search "quantum computing" --depth advanced --max-results 10 --json

# Recent news
tvly search "AI news" --time-range week --topic news --json

# Domain-filtered
tvly search "SEC filings" --include-domains sec.gov,reuters.com --json

# Include full page content in results
tvly search "react hooks tutorial" --include-raw-content --max-results 3 --json

Options
Option	Description
--depth	ultra-fast, fast, basic (default), advanced
--max-results	Max results, 0-20 (default: 5)
--topic	general (default), news, finance
--time-range	day, week, month, year
--start-date	Results after date (YYYY-MM-DD)
--end-date	Results before date (YYYY-MM-DD)
--include-domains	Comma-separated domains to include
--exclude-domains	Comma-separated domains to exclude
--country	Boost results from country
--include-answer	Include AI answer (basic or advanced)
--include-raw-content	Include full page content (markdown or text)
--include-images	Include image results
--include-image-descriptions	Include AI image descriptions
--chunks-per-source	Chunks per source (advanced/fast depth only)
-o, --output	Save output to file
--json	Structured JSON output
Search depth
Depth	Speed	Relevance	Best for
ultra-fast	Fastest	Lower	Real-time chat, autocomplete
fast	Fast	Good	Need chunks, latency matters
basic	Medium	High	General-purpose (default)
advanced	Slower	Highest	Precision, specific facts
Tips
Keep queries under 400 characters — think search query, not prompt.
Break complex queries into sub-queries for better results.
Use --include-raw-content when you need full page text (saves a separate extract call).
Use --include-domains to focus on trusted sources.
Use --time-range for recent information.
Read from stdin: echo "query" | tvly search - --json
See also
tavily-extract — extract content from specific URLs
tavily-research — comprehensive multi-source research
Weekly Installs
15.0K
Repository
tavily-ai/skills
GitHub Stars
259
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail