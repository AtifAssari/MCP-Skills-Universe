---
title: web-research
url: https://skills.sh/merit-systems/x402scan-skills/web-research
---

# web-research

skills/merit-systems/x402scan-skills/web-research
web-research
Installation
$ npx skills add https://github.com/merit-systems/x402scan-skills --skill web-research
SKILL.md
Web Research with x402 APIs

STOP — Read before making any API call. enrichx402.com endpoints are not the same as each provider's native API. All paths use the format https://enrichx402.com/api/{provider}/{action}. You MUST either:

Copy exact URLs from the Quick Reference table below, OR
Run x402.discover_api_endpoints(url="https://enrichx402.com") to get the correct paths

Guessing paths will fail with 405 errors (wrong path) or 404 errors (missing /api/ prefix).

Access Exa (neural search) and Firecrawl (web scraping) through x402-protected endpoints.

Setup

See rules/getting-started.md for installation and wallet setup.

Quick Reference
Task	Endpoint	Price	Best For
Neural search	https://enrichx402.com/api/exa/search	$0.01	Semantic web search
Find similar	https://enrichx402.com/api/exa/find-similar	$0.01	Pages similar to a URL
Extract text	https://enrichx402.com/api/exa/contents	$0.002	Clean text from URLs
Direct answers	https://enrichx402.com/api/exa/answer	$0.01	Factual Q&A
Scrape page	https://enrichx402.com/api/firecrawl/scrape	$0.0126	Single page to markdown
Web search	https://enrichx402.com/api/firecrawl/search	$0.0252	Search with scraping
When to Use What
Scenario	Tool
General web search	WebSearch (free) or Exa ($0.01)
Semantic/conceptual search	Exa search
Find pages like X	Exa find-similar
Get clean text from URL	Exa contents
Scrape blocked/JS-heavy site	Firecrawl scrape
Search + scrape results	Firecrawl search
Quick fact lookup	Exa answer

See rules/when-to-use.md for detailed guidance.

Exa Neural Search

Semantic search that understands meaning, not just keywords:

x402.fetch(
  url="https://enrichx402.com/api/exa/search",
  method="POST",
  body={
    "query": "startups building AI agents for customer support",
    "numResults": 10,
    "type": "neural"
  }
)


Options:

query - Search query (required)
numResults - Number of results (default: 10, max: 25)
type - "neural" (semantic) or "keyword" (traditional)
includeDomains - Only search these domains
excludeDomains - Skip these domains
startPublishedDate / endPublishedDate - Date range filter

Returns: List of URLs with titles, snippets, and relevance scores.

Find Similar Pages

Find pages semantically similar to a reference URL:

x402.fetch(
  url="https://enrichx402.com/api/exa/find-similar",
  method="POST",
  body={
    "url": "https://example.com/article-i-like",
    "numResults": 10
  }
)


Great for:

Finding competitor products
Discovering related content
Expanding research sources
Extract Text Content

Get clean, structured text from URLs:

x402.fetch(
  url="https://enrichx402.com/api/exa/contents",
  method="POST",
  body={
    "urls": [
      "https://example.com/article1",
      "https://example.com/article2"
    ]
  }
)


Options:

urls - Array of URLs to extract
text - Include full text (default: true)
highlights - Include key highlights

Cheapest option ($0.002) when you already have URLs and just need the content.

Direct Answers

Get factual answers to questions:

x402.fetch(
  url="https://enrichx402.com/api/exa/answer",
  method="POST",
  body={
    "query": "What is the population of Tokyo?"
  }
)


Returns a direct answer with source citations. Best for:

Factual questions
Quick lookups
Verification of claims
Firecrawl Scrape

Scrape a single page to clean markdown:

x402.fetch(
  url="https://enrichx402.com/api/firecrawl/scrape",
  method="POST",
  body={
    "url": "https://example.com/page-to-scrape"
  }
)


Options:

url - Page to scrape (required)
formats - Output formats: ["markdown", "html", "links"]
onlyMainContent - Skip nav/footer/ads (default: true)
waitFor - Wait ms for JS to render

Advantages over WebFetch:

Handles JavaScript-rendered content
Bypasses common blocking
Extracts main content only
LLM-optimized markdown output
Firecrawl Search

Web search with automatic scraping of results:

x402.fetch(
  url="https://enrichx402.com/api/firecrawl/search",
  method="POST",
  body={
    "query": "best practices for react server components",
    "limit": 5
  }
)


Options:

query - Search query (required)
limit - Number of results (default: 5)
scrapeOptions - Options passed to scraper

Returns search results with full scraped content for each.

Workflows
Deep Research
(Optional) Check balance: x402.get_wallet_info
Discover endpoints (required before first fetch): x402.discover_api_endpoints(url="https://enrichx402.com")
Search broadly with Exa
Find related sources with find-similar
Extract content from top sources
Synthesize findings
x402.fetch(
  url="https://enrichx402.com/api/exa/search",
  method="POST",
  body={"query": "AI agents in healthcare 2024", "numResults": 15}
)

x402.fetch(
  url="https://enrichx402.com/api/exa/find-similar",
  method="POST",
  body={"url": "https://best-article-found.com"}
)

x402.fetch(
  url="https://enrichx402.com/api/exa/contents",
  method="POST",
  body={"urls": ["url1", "url2", "url3"]}
)

Blocked Site Scraping
 Try WebFetch first (free)
 If blocked/empty, use Firecrawl with waitFor for JS-heavy sites
x402.fetch(
  url="https://enrichx402.com/api/firecrawl/scrape",
  method="POST",
  body={"url": "https://blocked-site.com/article", "waitFor": 3000}
)

Cost Optimization
Use Exa contents ($0.002) when you already have URLs
Use WebSearch/WebFetch first (free) and fall back to x402 endpoints
Batch URL extraction - pass multiple URLs to Exa contents
Limit results - request only as many as needed
Parallel Calls

Independent searches can run in parallel:

# These don't depend on each other
x402.fetch(url=".../exa/search", body={"query": "topic A"})
x402.fetch(url=".../exa/search", body={"query": "topic B"})

Weekly Installs
51
Repository
merit-systems/x…n-skills
GitHub Stars
3
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn