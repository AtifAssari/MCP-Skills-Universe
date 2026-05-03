---
title: tavily
url: https://skills.sh/vm0-ai/vm0-skills/tavily
---

# tavily

skills/vm0-ai/vm0-skills/tavily
tavily
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill tavily
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name TAVILY_TOKEN or zero doctor check-connector --url https://api.tavily.com/search --method POST

How to Use

All examples below assume you have TAVILY_TOKEN set in your environment. The base endpoint for the Tavily search API is a POST request to:

https://api.tavily.com/search

with a JSON body.

1. Basic Search

Write to /tmp/tavily_request.json:

{
  "query": "2025 AI Trending",
  "search_depth": "basic",
  "max_results": 5
}


Then run:

curl -s -X POST "https://api.tavily.com/search" --header "Content-Type: application/json" --header "Authorization: Bearer $TAVILY_TOKEN" -d @/tmp/tavily_request.json


Key parameters:

query: Search query or natural language question
search_depth:
"basic" – faster, good for most use cases
"advanced" – deeper search and higher recall
max_results: Maximum number of results to return (e.g. 3 / 5 / 10)
2. Advanced Search

Write to /tmp/tavily_request.json:

{
  "query": "serverless SaaS pricing best practices",
  "search_depth": "advanced",
  "max_results": 8,
  "include_answer": true,
  "include_domains": ["docs.aws.amazon.com", "cloud.google.com"],
  "exclude_domains": ["reddit.com", "twitter.com"],
  "include_raw_content": false
}


Then run:

curl -s -X POST "https://api.tavily.com/search" --header "Content-Type: application/json" --header "Authorization: Bearer $TAVILY_TOKEN" -d @/tmp/tavily_request.json


Common advanced parameters:

include_answer: When true, Tavily returns a summarized answer field
include_domains: Whitelist of domains to include
exclude_domains: Blacklist of domains to exclude
include_raw_content: Whether to include raw page content (HTML / raw text). Default is false.
3. Typical Response Structure (Example)

Tavily returns a JSON object similar to:

{
  "answer": "Brief summary...",
  "results": [
  {
  "title": "Article title",
  "url": "https://example.com/article",
  "content": "Snippet or extracted content...",
  "score": 0.89
  }
  ]
}


In agents or automation flows you typically:

Use answer as a concise, ready-to-use summary
Iterate over results to extract title + url as references / citations
4. Using Tavily in n8n (HTTP Request Node)

To integrate Tavily in n8n with the HTTP Request node:

Method: POST
URL: https://api.tavily.com/search
Headers:
Content-Type: application/json
Authorization: Bearer {{ $env.TAVILY_TOKEN }}
Body: JSON, for example:
{
  "query": "n8n self-hosted best practices",
  "search_depth": "basic",
  "max_results": 5
}


This lets you pipe Tavily search results into downstream nodes such as LLMs, Notion, Slack notifications, etc.

Guidelines
Use advanced only when necessary: it consumes more resources and is best for deep research / high-value questions.
Mind quotas and cost: Tavily typically offers free tiers plus paid usage; in automation flows, add guards (filters, rate limits).
Post-process results with an LLM: use Tavily for retrieval, then let your LLM summarize, extract tables, or generate reports.
Handle sensitive data carefully: avoid sending raw secrets or PII directly in query; anonymize or mask when possible.
Weekly Installs
69
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn