---
title: tavily-cli
url: https://skills.sh/tavily-ai/skills/tavily-cli
---

# tavily-cli

skills/tavily-ai/skills/tavily-cli
tavily-cli
Installation
$ npx skills add https://github.com/tavily-ai/skills --skill tavily-cli
Summary

Web search, content extraction, site crawling, and deep research via Tavily CLI.

Five command modes covering search, extraction, URL discovery, bulk crawling, and multi-source research with citations
All commands support JSON output and file saving for structured, agentic workflows
Escalation pattern guides you from simple search through extraction, mapping, crawling, to comprehensive research based on your needs
Requires tavily-cli installation and API key authentication via tvly login
SKILL.md
Tavily CLI

Web search, content extraction, site crawling, URL discovery, and deep research. Returns JSON optimized for LLM consumption.

Run tvly --help or tvly <command> --help for full option details.

Prerequisites

Must be installed and authenticated. Check with tvly --status.

tavily v0.1.0

> Authenticated via OAuth (tvly login)


If not ready:

curl -fsSL https://cli.tavily.com/install.sh | bash


Or manually: uv tool install tavily-cli / pip install tavily-cli

Then authenticate:

tvly login --api-key tvly-YOUR_KEY
# or: export TAVILY_API_KEY=tvly-YOUR_KEY
# or: tvly login  (opens browser for OAuth)

Workflow

Follow this escalation pattern — start simple, escalate when needed:

Search — No specific URL. Find pages, answer questions, discover sources.
Extract — Have a URL. Pull its content directly.
Map — Large site, need to find the right page. Discover URLs first.
Crawl — Need bulk content from an entire site section.
Research — Need comprehensive, multi-source analysis with citations.
Need	Command	When
Find pages on a topic	tvly search	No specific URL yet
Get a page's content	tvly extract	Have a URL
Find URLs within a site	tvly map	Need to locate a specific subpage
Bulk extract a site section	tvly crawl	Need many pages (e.g., all /docs/)
Deep research with citations	tvly research	Need multi-source synthesis

For detailed command reference, use the individual skill for each command (e.g., tavily-search, tavily-crawl) or run tvly <command> --help.

Output

All commands support --json for structured, machine-readable output and -o to save to a file.

tvly search "react hooks" --json -o results.json
tvly extract "https://example.com/docs" -o docs.md
tvly crawl "https://docs.example.com" --output-dir ./docs/

Tips
Always quote URLs — shell interprets ? and & as special characters.
Use --json for agentic workflows — every command supports it.
Read from stdin with - — echo "query" | tvly search -
Exit codes: 0 = success, 2 = bad input, 3 = auth error, 4 = API error.
Weekly Installs
5.5K
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