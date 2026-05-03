---
rating: ⭐⭐⭐
title: firecrawl-browser
url: https://skills.sh/firecrawl/cli/firecrawl-browser
---

# firecrawl-browser

skills/firecrawl/cli/firecrawl-browser
firecrawl-browser
Installation
$ npx skills add https://github.com/firecrawl/cli --skill firecrawl-browser
Summary

Cloud browser automation for pages requiring clicks, forms, login, and pagination.

Supports interactive workflows: click elements, fill forms, navigate multi-step flows, handle pagination and infinite scroll
Persistent profiles survive session close, enabling login-then-work patterns where authentication state is retained across reconnects
Core commands include open, snapshot -i (element discovery with @ref IDs), click, fill, type, scrape, scroll, wait, and eval for JavaScript execution
Session management with configurable TTL, inactivity timeout, and read-only reconnect mode for parallel or sequential browser work
SKILL.md
firecrawl interact (formerly browser)

The browser command is deprecated. Use scrape + interact instead. Interact lets you scrape a page and then click, fill forms, and navigate without managing sessions manually.

Interact with scraped pages in a live browser session. Scrape a page first, then use natural language prompts or code to click, fill forms, navigate, and extract data.

When to use
Content requires interaction: clicks, form fills, pagination, login
scrape failed because content is behind JavaScript interaction
You need to navigate a multi-step flow
Last resort in the workflow escalation pattern: search → scrape → map → crawl → interact
Never use interact for web searches — use search instead
Quick start
# 1. Scrape a page (scrape ID is saved automatically)
firecrawl scrape "<url>"

# 2. Interact with the page using natural language
firecrawl interact --prompt "Click the login button"
firecrawl interact --prompt "Fill in the email field with test@example.com"
firecrawl interact --prompt "Extract the pricing table"

# 3. Or use code for precise control
firecrawl interact --code "agent-browser click @e5" --language bash
firecrawl interact --code "agent-browser snapshot -i" --language bash

# 4. Stop the session when done
firecrawl interact stop

Options
Option	Description
--prompt <text>	Natural language instruction (use this OR --code)
--code <code>	Code to execute in the browser session
--language <lang>	Language for code: bash, python, node
--timeout <seconds>	Execution timeout (default: 30, max: 300)
--scrape-id <id>	Target a specific scrape (default: last scrape)
-o, --output <path>	Output file path
Profiles

Use --profile on the scrape to persist browser state (cookies, localStorage) across scrapes:

# Session 1: Login and save state
firecrawl scrape "https://app.example.com/login" --profile my-app
firecrawl interact --prompt "Fill in email with user@example.com and click login"

# Session 2: Come back authenticated
firecrawl scrape "https://app.example.com/dashboard" --profile my-app
firecrawl interact --prompt "Extract the dashboard data"


Read-only reconnect (no writes to profile state):

firecrawl scrape "https://app.example.com" --profile my-app --no-save-changes

Tips
Always scrape first — interact requires a scrape ID from a previous firecrawl scrape call
The scrape ID is saved automatically, so you don't need --scrape-id for subsequent interact calls
Use firecrawl interact stop to free resources when done
For parallel work, scrape multiple pages and interact with each using --scrape-id
See also
firecrawl-scrape — try scrape first, escalate to interact only when needed
firecrawl-search — for web searches (never use interact for searching)
firecrawl-agent — AI-powered extraction (less manual control)
Weekly Installs
11.3K
Repository
firecrawl/cli
GitHub Stars
362
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail