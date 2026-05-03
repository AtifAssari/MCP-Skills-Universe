---
title: dot
url: https://skills.sh/snowboard-software/getdot/dot
---

# dot

skills/snowboard-software/getdot/dot
dot
Installation
$ npx skills add https://github.com/snowboard-software/getdot --skill dot
SKILL.md
dot — AI Data Analyst CLI

dot lets you query your company's databases through Dot, an AI data analyst. Dot writes SQL, runs queries, generates charts, and explains results.

Setup

If dot is not installed or not found in PATH:

macOS/Linux: curl -fsSL https://app.getdot.ai/install.sh | sh
Windows: irm https://app.getdot.ai/install.ps1 | iex

After installing, authenticate with dot login (opens browser).

When to use

Use dot when the user asks about:

Data questions: "What were sales last month?", "Show me top customers"
Metrics and KPIs: "What's our churn rate?", "Revenue by region"
SQL queries: "Write a query to find...", "Check the database for..."
Reports: "Generate a summary of...", "Break down..."
Any time they say "ask dot", "check the numbers", or "query the data"
Decision: catalog vs ask
If the user asks WHAT data is available, run dot catalog
If the question is vague (no specific metric, table, or time period), run dot catalog first to understand what's available, then ask a targeted question
If the user asks a specific data question, go straight to dot "..."
How to use
Discover available data first

Before asking questions, run dot catalog to see what data is available:

dot catalog


This returns instantly (no LLM call) and shows:

Available capabilities (SQL, visualizations, scheduled reports, text analysis)
Custom skills configured for the org
Data source connections with table counts
Top 50 tables sorted by usage, with descriptions and column/row counts
External assets (Looker dashboards, etc.)
Ask questions

Run dot via Bash with the question in quotes. Set a generous timeout — Dot runs a full AI analysis pipeline (SQL generation, execution, visualization) which takes 15-60 seconds, sometimes up to 2 minutes for complex queries:

dot "What were total sales last month?"

Follow-up questions

Every response includes a chat ID. Use --chat to continue the conversation:

dot "Now break down by region" --chat cli-m1abc2d-x4y5z6

When to bypass cache

Responses are cached permanently. Use --no-cache when:

The question involves "today", "right now", "latest", or "current"
The user says "refresh", "update", or "re-run"
The user seems unsatisfied with a previous answer
dot "What are today's sales numbers?" --no-cache

After receiving a response
Parse the output text and present the explanation to the user
If a chart PNG path is shown ("Chart saved to: /tmp/dot/...png"), READ the PNG file — you have multimodal capabilities and can describe what the chart shows
If a CSV path is shown and the user needs detailed analysis, read and analyze the CSV data
Present suggested follow-ups if they seem relevant to the user's goal
If the user wants to continue, use --chat with the chat ID from the output
Output format

The output includes:

Text explanation — natural language answer to the question
SQL query — the exact SQL that was executed
Data preview — first rows as CSV-like text with column stats
Chart — saved as PNG to /tmp/dot/<chat-id>/ (read it — you're multimodal)
CSV data — saved locally for further analysis
Dot URL — link to the full interactive analysis in the browser
Suggested follow-ups — use these proactively if relevant
Multi-step analysis

You can orchestrate multi-step data analysis:

Run dot catalog to understand available data
Ask an initial question with dot "..."
Read the CSV output for deeper analysis or custom calculations
Ask follow-up questions using --chat to refine results
Compare results across multiple queries
Caching
dot "question" — cached forever until --clear-cache
Follow-ups with --chat are never cached (always fresh)
dot catalog is never cached (already fast, no LLM)

Use --no-cache to force a fresh request, or --clear-cache to wipe all cached data.

Tips for good questions
Start with dot catalog to understand what tables and data are available
Be specific: include metric names, time periods, filters
One question at a time works best
Use follow-ups (--chat) to refine rather than asking compound questions
If you need a chart, say "show me a chart of..." or "visualize..."
Error: command not found

If dot is not found, tell the user to install it:

curl -fsSL https://app.getdot.ai/install.sh | sh
dot login

Error: Not authenticated

If you get "Not authenticated", the user needs to log in:

dot login


If dot login doesn't work (e.g., no browser available, SSO issues), the user can create an API token manually:

Open the Dot dashboard in a browser (e.g., https://app.getdot.ai or your company's Dot URL)
Go to Settings > Users > API Tokens
Create a new token scoped to their user
Use it with: dot login --token <TOKEN> --server <SERVER_URL>
Error: Authentication failed

If you get "Authentication failed", the token may have expired. The user needs to re-login:

dot login

Error: Connection failed

If dot can't reach the server, tell the user to check their internet connection. If using a custom server, verify the URL with dot status.

Debugging

Run dot status to check who is logged in, which server is configured, and whether the token is expired.

Examples
# See what data is available
dot catalog

# Simple question
dot "What were total sales last month?"

# With follow-up
dot "Compare to the same period last year" --chat cli-m1abc2d-x4y5z6

# Chart request
dot "Show me a chart of monthly revenue trend for the past 12 months"

# Specific filters
dot "Top 10 customers by order count in Q4 2025, US only"

# Force fresh answer (bypass cache)
dot "What were total sales last month?" --no-cache

Weekly Installs
81
Repository
snowboard-softw…e/getdot
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail