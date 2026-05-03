---
rating: ⭐⭐⭐
title: clawcard
url: https://skills.sh/latchagent/skill/clawcard
---

# clawcard

skills/latchagent/skill/clawcard
clawcard
Installation
$ npx skills add https://github.com/latchagent/skill --skill clawcard
SKILL.md

You have access to ClawCard via the clawcard CLI. All commands support --json for machine-readable output. Always pass --json when calling these commands.

Quick Start
clawcard agent info --json                             # Your identity, email, phone, balance
clawcard agent pay <slug> '<json>' --json              # Pay for any capability
clawcard agent catalog --json                          # Browse all capabilities
clawcard agent catalog-search "flights" --json         # Search capabilities
clawcard agent files list --json                       # Your files
clawcard agent creds --json                            # Your credentials


ALWAYS check existing resources before creating new ones. List cards before every purchase. Reuse open merchant_locked cards for the same merchant.

Core Capabilities
Capability	Command Reference
Email (send, receive, read)	reference/email.md
SMS (send, receive)	reference/sms.md
Virtual Cards (create, pay, manage)	reference/cards.md
File Storage (upload, list, download)	reference/files.md
Credentials (store, retrieve secrets)	reference/credentials.md
Browser Checkout (navigate, fill forms, pay)	reference/checkout.md
Catalog — ~300 Paid API Capabilities

Your agent has access to ~300 paid capabilities via the catalog. All calls deduct from your account balance.

How to pay for any capability:

clawcard agent pay <slug> '<json body>' --json


Browse full catalog: clawcard agent catalog --json Search by keyword: clawcard agent catalog-search "web scraping" --json

Category	Examples	Price Range	Reference
Search	web-search, news-search, image-search	$0.01-0.09	reference/catalog-search.md
Scrape & Extract	scrape-url, crawl-site, extract-data	$0.01-0.05	reference/catalog-scrape.md
People & Companies	enrich-person, enrich-company, find-contacts, find-email	$0.01-0.06	reference/catalog-enrich.md
Social Media	tiktok-profile, instagram-posts, reddit-search	$0.06	reference/catalog-social.md
Media Generation	image-gen, music-gen, transcribe, text-to-speech	$0.03-0.11	reference/catalog-media.md
Finance & Markets	stock-quote, sec-filings, exchange rates	$0.01-0.06	reference/catalog-finance.md
Travel	flight-search, hotel-search	$0.01-0.06	reference/catalog-travel.md
Maps & Weather	geocode, directions, weather	$0.01	reference/catalog-maps.md
Compute	run-code, screenshot	$0.01-0.06	reference/catalog-compute.md
Reference	wolfram, translate	$0.01-0.06	reference/catalog-reference.md
Marketing & SEO	seo-keywords	$0.01-0.03	reference/catalog-marketing.md
Niche Data	sneaker-prices, property-value	$0.01-0.04	reference/catalog-data.md
Important: Async Capabilities

Some capabilities (video generation, music generation, deep research, website crawling) take time to complete. They return a job/task ID instead of immediate results. You MUST poll the corresponding status slug to get results.

Every poll costs money. Wait 10-15 seconds between polls to avoid wasting balance.

Example flow for music generation:

# 1. Start generation ($0.11)
clawcard agent pay music-gen '{"prompt":"upbeat lo-fi beat","customMode":false,"instrumental":true,"model":"V4"}' --json
# → returns { data: { data: { taskId: "abc123" } } }

# 2. Wait 15 seconds, then poll ($0.01 per poll)
clawcard agent pay music-status '{"taskId":"abc123"}' --json
# → returns status: "PENDING" or "TEXT_SUCCESS" or "FIRST_SUCCESS" with audioUrl


Status slugs for async capabilities:

music-gen → poll with music-status
lyrics-gen → poll with lyrics-status
image-gen-gpt, image-gen-nano, video-gen-* (StableStudio) → poll with stablestudio-status
stability-3d, stability-audio → poll with stability-status
replicate-run → poll with replicate-status
clado-deep-research → poll with clado-research-status
allium-sql → poll with allium-sql-status, then allium-sql-results
dune-sql → poll with dune-results
tako-deep-search → poll with tako-deep-status
crawl-site → poll with crawl-status
deep-research → poll with parallel-task-status
Browser Checkout (MCP)

For purchasing things on websites (domains, subscriptions, SaaS signups), use the clawcard-browser MCP server. It launches a browser with the ClawCard Pay extension.

Setup: If the browser MCP tools aren't available, help the user configure it:

Claude Code: clawcard mcp or claude mcp add clawcard-browser -e CLAWCARD_API_KEY=<key> -- npx @clawcard/browser
mcporter (OpenClaw, etc.): Add to ~/.mcporter/mcporter.json:
"clawcard-browser": {
  "command": "npx",
  "args": ["@clawcard/browser"],
  "env": { "CLAWCARD_API_KEY": "<key>" }
}

Cursor / VS Code: Add to .cursor/mcp.json or MCP config with same shape as above

Flow:

Create a card: clawcard agent cards create --amount <cents> --type merchant_locked --memo "description" --json
Launch browser: launch_browser tool with the checkout URL
Navigate and fill non-payment fields using snapshot, click, fill
Fill payment: fill_checkout tool with your card ID + billing details
The extension fills card number, expiry, CVC directly — you never see the card number
Review the page and submit

MCP Tools:

Tool	What it does
launch_browser	Open browser with ClawCard Pay extension
navigate	Go to a URL
snapshot	Get page accessibility tree with @e1 refs
click	Click element by ref
fill	Type into field by ref
detect_checkout	Check if page is a checkout (returns confidence + amount)
fill_checkout	Fill card + billing fields securely (card details never reach the LLM)
screenshot	Capture the page
close_browser	Close session

Security: Card details (PAN, CVV) go directly from the server to the browser extension. The LLM never sees or handles card numbers. Only the last four digits are returned.

Tips
For API capabilities, use clawcard agent pay — it handles payment automatically from your balance.
For purchasing on websites, use the clawcard-browser MCP tools with a virtual card.
Default to merchant_locked cards. Only use single_use for one-time purchases.
NEVER silently pay for a subscription. Always warn the user first.
If you need a capability, search the catalog: clawcard agent catalog-search "<what you need>" --json
To add balance: clawcard billing topup
Weekly Installs
51
Repository
latchagent/skill
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn