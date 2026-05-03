---
rating: ⭐⭐⭐
title: firecrawl-agent
url: https://skills.sh/firecrawl/cli/firecrawl-agent
---

# firecrawl-agent

skills/firecrawl/cli/firecrawl-agent
firecrawl-agent
Installation
$ npx skills add https://github.com/firecrawl/cli --skill firecrawl-agent
Summary

AI-powered autonomous extraction of structured data from complex multi-page websites.

Navigates sites intelligently to locate and extract data, returning results as JSON with optional schema validation
Supports custom JSON schemas for predictable structured output, or freeform extraction when schema is not provided
Offers two model tiers (spark-1-mini and spark-1-pro) with credit limits and optional waiting for inline results
Best suited for multi-page extraction tasks; use simpler scrape or crawl skills for single-page or bulk extraction without AI reasoning
SKILL.md
firecrawl agent

AI-powered autonomous extraction. The agent navigates sites and extracts structured data (takes 2-5 minutes).

When to use
You need structured data from complex multi-page sites
Manual scraping would require navigating many pages
You want the AI to figure out where the data lives
Quick start
# Extract structured data
firecrawl agent "extract all pricing tiers" --wait -o .firecrawl/pricing.json

# With a JSON schema for structured output
firecrawl agent "extract products" --schema '{"type":"object","properties":{"name":{"type":"string"},"price":{"type":"number"}}}' --wait -o .firecrawl/products.json

# Focus on specific pages
firecrawl agent "get feature list" --urls "<url>" --wait -o .firecrawl/features.json

Options
Option	Description
--urls <urls>	Starting URLs for the agent
--model <model>	Model to use: spark-1-mini or spark-1-pro
--schema <json>	JSON schema for structured output
--schema-file <path>	Path to JSON schema file
--max-credits <n>	Credit limit for this agent run
--wait	Wait for agent to complete
--pretty	Pretty print JSON output
-o, --output <path>	Output file path
Tips
Always use --wait to get results inline. Without it, returns a job ID.
Use --schema for predictable, structured output — otherwise the agent returns freeform data.
Agent runs consume more credits than simple scrapes. Use --max-credits to cap spending.
For simple single-page extraction, prefer scrape — it's faster and cheaper.
See also
firecrawl-scrape — simpler single-page extraction
firecrawl-interact — scrape + interact for manual page interaction (more control)
firecrawl-crawl — bulk extraction without AI
Weekly Installs
32.6K
Repository
firecrawl/cli
GitHub Stars
364
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn