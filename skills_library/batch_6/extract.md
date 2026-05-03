---
title: extract
url: https://skills.sh/tavily-ai/skills/extract
---

# extract

skills/tavily-ai/skills/extract
extract
Installation
$ npx skills add https://github.com/tavily-ai/skills --skill extract
Summary

Extract clean content from specific URLs using Tavily's extraction API.

Supports up to 20 URLs per request with optional query-based reranking to focus on relevant content chunks
Two extraction modes: basic for fast text extraction, advanced for JavaScript-rendered pages and structured data
Automatic OAuth authentication via browser on first run, or manual API key configuration in settings
Returns markdown or plain text format with optional image URLs and configurable timeout up to 60 seconds
SKILL.md
Extract Skill

Extract clean content from specific URLs. Ideal when you know which pages you want content from.

Authentication

The script uses OAuth via the Tavily MCP server. No manual setup required - on first run, it will:

Check for existing tokens in ~/.mcp-auth/
If none found, automatically open your browser for OAuth authentication

Note: You must have an existing Tavily account. The OAuth flow only supports login — account creation is not available through this flow. Sign up at tavily.com first if you don't have an account.

Alternative: API Key

If you prefer using an API key, get one at https://tavily.com and add to ~/.claude/settings.json:

{
  "env": {
    "TAVILY_API_KEY": "tvly-your-api-key-here"
  }
}

Quick Start
Using the Script
./scripts/extract.sh '<json>'


Examples:

# Single URL
./scripts/extract.sh '{"urls": ["https://example.com/article"]}'

# Multiple URLs
./scripts/extract.sh '{"urls": ["https://example.com/page1", "https://example.com/page2"]}'

# With query focus and chunks
./scripts/extract.sh '{"urls": ["https://example.com/docs"], "query": "authentication API", "chunks_per_source": 3}'

# Advanced extraction for JS pages
./scripts/extract.sh '{"urls": ["https://app.example.com"], "extract_depth": "advanced", "timeout": 60}'

Basic Extraction
curl --request POST \
  --url https://api.tavily.com/extract \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "urls": ["https://example.com/article"]
  }'

Multiple URLs with Query Focus
curl --request POST \
  --url https://api.tavily.com/extract \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "urls": [
      "https://example.com/ml-healthcare",
      "https://example.com/ai-diagnostics"
    ],
    "query": "AI diagnostic tools accuracy",
    "chunks_per_source": 3
  }'

API Reference
Endpoint
POST https://api.tavily.com/extract

Headers
Header	Value
Authorization	Bearer <TAVILY_API_KEY>
Content-Type	application/json
Request Body
Field	Type	Default	Description
urls	array	Required	URLs to extract (max 20)
query	string	null	Reranks chunks by relevance
chunks_per_source	integer	3	Chunks per URL (1-5, requires query)
extract_depth	string	"basic"	basic or advanced (for JS pages)
format	string	"markdown"	markdown or text
include_images	boolean	false	Include image URLs
timeout	float	varies	Max wait (1-60 seconds)
Response Format
{
  "results": [
    {
      "url": "https://example.com/article",
      "raw_content": "# Article Title\n\nContent..."
    }
  ],
  "failed_results": [],
  "response_time": 2.3
}

Extract Depth
Depth	When to Use
basic	Simple text extraction, faster
advanced	Dynamic/JS-rendered pages, tables, structured data
Examples
Single URL Extraction
curl --request POST \
  --url https://api.tavily.com/extract \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "urls": ["https://docs.python.org/3/tutorial/classes.html"],
    "extract_depth": "basic"
  }'

Targeted Extraction with Query
curl --request POST \
  --url https://api.tavily.com/extract \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "urls": [
      "https://example.com/react-hooks",
      "https://example.com/react-state"
    ],
    "query": "useState and useEffect patterns",
    "chunks_per_source": 2
  }'

JavaScript-Heavy Pages
curl --request POST \
  --url https://api.tavily.com/extract \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "urls": ["https://app.example.com/dashboard"],
    "extract_depth": "advanced",
    "timeout": 60
  }'

Batch Extraction
curl --request POST \
  --url https://api.tavily.com/extract \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "urls": [
      "https://example.com/page1",
      "https://example.com/page2",
      "https://example.com/page3",
      "https://example.com/page4",
      "https://example.com/page5"
    ],
    "extract_depth": "basic"
  }'

Tips
Max 20 URLs per request - batch larger lists
Use query + chunks_per_source to get only relevant content
Try basic first, fall back to advanced if content is missing
Set longer timeout for slow pages (up to 60s)
Check failed_results for URLs that couldn't be extracted
Weekly Installs
4.9K
Repository
tavily-ai/skills
GitHub Stars
259
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn