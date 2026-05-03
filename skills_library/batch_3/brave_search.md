---
title: brave-search
url: https://skills.sh/steipete/agent-scripts/brave-search
---

# brave-search

skills/steipete/agent-scripts/brave-search
brave-search
Installation
$ npx skills add https://github.com/steipete/agent-scripts --skill brave-search
Summary

Lightweight web search and content extraction via Brave Search API, no browser required.

Two core commands: search.js for querying the web with configurable result counts, and content.js for extracting readable markdown from specific URLs
Search results include title, link, and snippet by default; add --content flag to include full page content as markdown
Ideal for documentation lookup, fact-checking, and fetching web content without the overhead of browser automation
Requires BRAVE_API_KEY environment variable and one-time npm setup
SKILL.md
Brave Search

Headless web search and content extraction using Brave Search. No browser required.

Setup

Run once before first use:

cd ~/Projects/agent-scripts/skills/brave-search
npm ci


Needs env: BRAVE_API_KEY.

Search
./search.js "query"                    # Basic search (5 results)
./search.js "query" -n 10              # More results
./search.js "query" --content          # Include page content as markdown
./search.js "query" -n 3 --content     # Combined

Extract Page Content
./content.js https://example.com/article


Fetches a URL and extracts readable content as markdown.

Output Format
--- Result 1 ---
Title: Page Title
Link: https://example.com/page
Snippet: Description from search results
Content: (if --content flag used)
  Markdown content extracted from the page...

--- Result 2 ---
...

When to Use
Searching for documentation or API references
Looking up facts or current information
Fetching content from specific URLs
Any task requiring web search without interactive browsing
Weekly Installs
824
Repository
steipete/agent-scripts
GitHub Stars
2.5K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn