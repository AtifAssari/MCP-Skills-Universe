---
rating: ⭐⭐⭐
title: x-search
url: https://skills.sh/syjcnss/skills/x-search
---

# x-search

skills/syjcnss/skills/x-search
x-search
Installation
$ npx skills add https://github.com/syjcnss/skills --skill x-search
SKILL.md
X Search

Search X (Twitter) posts using xAI's Grok API with keyword search, semantic search, user filtering, and date range capabilities.

Instructions for Agents

When invoking this skill:

Execute the script using the Bash tool with appropriate parameters based on the user's request
Parse the output which contains both the analysis and citations sections
CRITICAL: Always include the citations in your response to the user. The script output contains a "Citations:" section with numbered X post URLs that MUST be presented to the user
Format your response to include:
The analysis/findings from Grok
The complete citations list with all referenced post URLs

The script will return formatted output with citations. You MUST include these citations in your response to the user.

Quick Start

Basic X search:

scripts/x_search.sh "What are people saying about AI?"

Environment Setup

Required environment variables:

XAI_API_KEY: Your xAI API key (required)
XAI_API_HOST: API host URL (optional, defaults to https://api.x.ai)
Search Options
Date Range Filtering

Restrict search to specific time period:

scripts/x_search.sh "AI developments" --from-date 2025-01-01 --to-date 2025-02-06

User Handle Filtering

Search only specific users (max 10):

scripts/x_search.sh "latest updates" --allowed-handles elonmusk,gdb


Exclude specific users (max 10):

scripts/x_search.sh "tech news" --excluded-handles spamaccount,bot123


Note: Cannot use both --allowed-handles and --excluded-handles in the same request.

Media Understanding

Enable image analysis in posts:

scripts/x_search.sh "AI art trends" --enable-images


Enable video analysis in posts:

scripts/x_search.sh "product demos" --enable-videos

Combined Options

All options can be combined:

scripts/x_search.sh "climate change discussion" \
  --from-date 2025-01-01 \
  --excluded-handles climateskeptic \
  --enable-images

Enable Reasoning Model

Use --thinking flag to switch to the reasoning model for deeper analysis:

scripts/x_search.sh "complex topic requiring deep analysis" --thinking


This uses grok-4-1-fast-reasoning instead of the default grok-4-1-fast-non-reasoning.

Output Format

The script automatically parses the JSON response and outputs:

Text content: Grok's formatted analysis and findings
Citations: List of X post URLs with reference numbers

Example output:

## Response:

[Analysis text with inline citation markers]

## Citations:
[1] https://x.com/i/status/...
[2] https://x.com/i/status/...

Usage Notes
Default model: grok-4-1-fast-non-reasoning for fast search responses
With --thinking flag: grok-4-1-fast-reasoning for deeper reasoning
The script uses curl to query the xAI Responses API endpoint
Output is automatically parsed with jq for readability
Date format: ISO8601 (YYYY-MM-DD)
Handle limits: 10 maximum for allowed/excluded lists
Weekly Installs
37
Repository
syjcnss/skills
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn