---
title: firecrawl
url: https://skills.sh/vm0-ai/vm0-skills/firecrawl
---

# firecrawl

skills/vm0-ai/vm0-skills/firecrawl
firecrawl
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill firecrawl
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name FIRECRAWL_TOKEN or zero doctor check-connector --url https://api.firecrawl.dev/v1/scrape --method POST

How to Use

All examples below assume you have FIRECRAWL_TOKEN set.

Base URL: https://api.firecrawl.dev/v1

1. Scrape - Single Page

Extract content from a single webpage.

Basic Scrape

Write to /tmp/firecrawl_request.json:

{
  "url": "https://example.com",
  "formats": ["markdown"]
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/scrape" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json

Scrape with Options

Write to /tmp/firecrawl_request.json:

{
  "url": "https://docs.example.com/api",
  "formats": ["markdown"],
  "onlyMainContent": true,
  "timeout": 30000
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/scrape" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq '.data.markdown'

Get HTML Instead

Write to /tmp/firecrawl_request.json:

{
  "url": "https://example.com",
  "formats": ["html"]
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/scrape" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq '.data.html'

Get Screenshot

Write to /tmp/firecrawl_request.json:

{
  "url": "https://example.com",
  "formats": ["screenshot"]
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/scrape" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq '.data.screenshot'


Scrape Parameters:

Parameter	Type	Description
url	string	URL to scrape (required)
formats	array	markdown, html, rawHtml, screenshot, links
onlyMainContent	boolean	Skip headers/footers
timeout	number	Timeout in milliseconds
2. Crawl - Entire Website

Crawl all pages of a website (async operation).

Start a Crawl

Write to /tmp/firecrawl_request.json:

{
  "url": "https://example.com",
  "limit": 50,
  "maxDepth": 2
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/crawl" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json


Response:

{
  "success": true,
  "id": "crawl-job-id-here"
}

Check Crawl Status

Replace <job-id> with the actual job ID returned from the crawl request:

curl -s "https://api.firecrawl.dev/v1/crawl/<job-id>" -H "Authorization: Bearer $FIRECRAWL_TOKEN" | jq '{status, completed, total}'

Get Crawl Results

Replace <job-id> with the actual job ID:

curl -s "https://api.firecrawl.dev/v1/crawl/<job-id>" -H "Authorization: Bearer $FIRECRAWL_TOKEN" | jq '.data[] | {url: .metadata.url, title: .metadata.title}'

Crawl with Path Filters

Write to /tmp/firecrawl_request.json:

{
  "url": "https://blog.example.com",
  "limit": 20,
  "maxDepth": 3,
  "includePaths": ["/posts/*"],
  "excludePaths": ["/admin/*", "/login"]
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/crawl" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json


Crawl Parameters:

Parameter	Type	Description
url	string	Starting URL (required)
limit	number	Max pages to crawl (default: 100)
maxDepth	number	Max crawl depth (default: 3)
includePaths	array	Paths to include (e.g., /blog/*)
excludePaths	array	Paths to exclude
3. Map - URL Discovery

Get all URLs from a website quickly.

Basic Map

Write to /tmp/firecrawl_request.json:

{
  "url": "https://example.com"
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/map" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq '.links[:10]'

Map with Search Filter

Write to /tmp/firecrawl_request.json:

{
  "url": "https://shop.example.com",
  "search": "product",
  "limit": 500
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/map" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq '.links'


Map Parameters:

Parameter	Type	Description
url	string	Website URL (required)
search	string	Filter URLs containing keyword
limit	number	Max URLs to return (default: 1000)
4. Search - Web Search

Search the web and get full page content.

Basic Search

Write to /tmp/firecrawl_request.json:

{
  "query": "AI news 2024",
  "limit": 5
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/search" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq '.data[] | {title: .metadata.title, url: .url}'

Search with Full Content

Write to /tmp/firecrawl_request.json:

{
  "query": "machine learning tutorials",
  "limit": 3,
  "scrapeOptions": {
    "formats": ["markdown"]
  }
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/search" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq '.data[] | {title: .metadata.title, content: .markdown[:500]}'


Search Parameters:

Parameter	Type	Description
query	string	Search query (required)
limit	number	Number of results (default: 10)
scrapeOptions	object	Options for scraping results
5. Extract - AI Data Extraction

Extract structured data from pages using AI.

Basic Extract

Write to /tmp/firecrawl_request.json:

{
  "urls": ["https://example.com/product/123"],
  "prompt": "Extract the product name, price, and description"
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/extract" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq '.data'

Extract with Schema

Write to /tmp/firecrawl_request.json:

{
  "urls": ["https://example.com/product/123"],
  "prompt": "Extract product information",
  "schema": {
    "type": "object",
    "properties": {
      "name": {"type": "string"},
      "price": {"type": "number"},
      "currency": {"type": "string"},
      "inStock": {"type": "boolean"}
    }
  }
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/extract" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq '.data'

Extract from Multiple URLs

Write to /tmp/firecrawl_request.json:

{
  "urls": [
    "https://example.com/product/1",
    "https://example.com/product/2"
  ],
  "prompt": "Extract product name and price"
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/extract" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq '.data'


Extract Parameters:

Parameter	Type	Description
urls	array	URLs to extract from (required)
prompt	string	Description of data to extract (required)
schema	object	JSON schema for structured output
Practical Examples
Scrape Documentation

Write to /tmp/firecrawl_request.json:

{
  "url": "https://docs.python.org/3/tutorial/",
  "formats": ["markdown"],
  "onlyMainContent": true
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/scrape" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq -r '.data.markdown' > python-tutorial.md

Find All Blog Posts

Write to /tmp/firecrawl_request.json:

{
  "url": "https://blog.example.com",
  "search": "post"
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/map" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq -r '.links[]'

Research a Topic

Write to /tmp/firecrawl_request.json:

{
  "query": "best practices REST API design 2024",
  "limit": 5,
  "scrapeOptions": {"formats": ["markdown"]}
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/search" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq '.data[] | {title: .metadata.title, url: .url}'

Extract Pricing Data

Write to /tmp/firecrawl_request.json:

{
  "urls": ["https://example.com/pricing"],
  "prompt": "Extract all pricing tiers with name, price, and features"
}


Then run:

curl -s -X POST "https://api.firecrawl.dev/v1/extract" -H "Authorization: Bearer $FIRECRAWL_TOKEN" -H "Content-Type: application/json" -d @/tmp/firecrawl_request.json | jq '.data'

Poll Crawl Until Complete

Replace <job-id> with the actual job ID:

while true; do
  STATUS="$(curl -s "https://api.firecrawl.dev/v1/crawl/<job-id>" -H "Authorization: Bearer $FIRECRAWL_TOKEN" | jq -r '.status')"
  echo "Status: $STATUS"
  [ "$STATUS" = "completed" ] && break
  sleep 5
done

Response Format
Scrape Response
{
  "success": true,
  "data": {
  "markdown": "# Page Title\n\nContent...",
  "metadata": {
  "title": "Page Title",
  "description": "...",
  "url": "https://..."
  }
  }
}

Crawl Status Response
{
  "success": true,
  "status": "completed",
  "completed": 50,
  "total": 50,
  "data": [...]
}

Guidelines
Rate limits: Add delays between requests to avoid 429 errors
Crawl limits: Set reasonable limit values to control API usage
Main content: Use onlyMainContent: true for cleaner output
Async crawls: Large crawls are async; poll /crawl/{id} for status
Extract prompts: Be specific for better AI extraction results
Check success: Always check success field in responses
Weekly Installs
247
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn