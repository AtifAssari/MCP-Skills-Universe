---
title: tavily-best-practices
url: https://skills.sh/tavily-ai/skills/tavily-best-practices
---

# tavily-best-practices

skills/tavily-ai/skills/tavily-best-practices
tavily-best-practices
Installation
$ npx skills add https://github.com/tavily-ai/skills --skill tavily-best-practices
Summary

Web search API for LLMs with real-time data access, content extraction, site crawling, and AI-powered research.

Five core methods: search() for web results, extract() for URL content, crawl() for site-wide extraction, map() for URL discovery, and research() for end-to-end AI synthesis
Supports Python and JavaScript SDKs with async clients for parallel queries and configurable search depth (ultra-fast/fast/basic/advanced)
Crawl method accepts semantic instructions to focus extraction on specific content types; Map-then-Extract pattern available for targeted workflows
Research method offers three model tiers (mini/pro/auto) with polling-based async execution, streaming support, and structured output schemas
Integrates with LangChain, LlamaIndex, CrewAI, Vercel AI SDK, and other frameworks; supports Hybrid RAG patterns and project-level usage tracking
SKILL.md
Tavily

Tavily is a search API designed for LLMs, enabling AI applications to access real-time web data.

Installation

Python:

pip install tavily-python


JavaScript:

npm install @tavily/core


See references/sdk.md for complete SDK reference.

Client Initialization
from tavily import TavilyClient

# Uses TAVILY_API_KEY env var (recommended)
client = TavilyClient()

#With project tracking (for usage organization)
client = TavilyClient(project_id="your-project-id")

# Async client for parallel queries
from tavily import AsyncTavilyClient
async_client = AsyncTavilyClient()

Choosing the Right Method

For custom agents/workflows:

Need	Method
Web search results	search()
Content from specific URLs	extract()
Content from entire site	crawl()
URL discovery from site	map()

For out-of-the-box research:

Need	Method
End-to-end research with AI synthesis	research()
Quick Reference
search() - Web Search
response = client.search(
    query="quantum computing breakthroughs",  # Keep under 400 chars
    max_results=10,
    search_depth="advanced"
)
print(response)


Key parameters: query, max_results, search_depth (ultra-fast/fast/basic/advanced), include_domains, exclude_domains, time_range

See references/search.md for complete search reference.

extract() - URL Content Extraction
# Simple one-step extraction
response = client.extract(
    urls=["https://docs.example.com"],
    extract_depth="advanced"
)
print(response)


Key parameters: urls (max 20), extract_depth, query, chunks_per_source (1-5)

See references/extract.md for complete extract reference.

crawl() - Site-Wide Extraction
response = client.crawl(
    url="https://docs.example.com",
    instructions="Find API documentation pages",  # Semantic focus
    extract_depth="advanced"
)
print(response)


Key parameters: url, max_depth, max_breadth, limit, instructions, chunks_per_source, select_paths, exclude_paths

See references/crawl.md for complete crawl reference.

map() - URL Discovery
response = client.map(
    url="https://docs.example.com"
)
print(response)

research() - AI-Powered Research
import time

# For comprehensive multi-topic research
result = client.research(
    input="Analyze competitive landscape for X in SMB market",
    model="pro"  # or "mini" for focused queries, "auto" when unsure
)
request_id = result["request_id"]

# Poll until completed
response = client.get_research(request_id)
while response["status"] not in ["completed", "failed"]:
    time.sleep(10)
    response = client.get_research(request_id)

print(response["content"])  # The research report


Key parameters: input, model ("mini"/"pro"/"auto"), stream, output_schema, citation_format

See references/research.md for complete research reference.

Detailed Guides

For complete parameters, response fields, patterns, and examples:

references/sdk.md - Python & JavaScript SDK reference, async patterns, Hybrid RAG
references/search.md - Query optimization, search depth selection, domain filtering, async patterns, post-filtering
references/extract.md - One-step vs two-step extraction, query/chunks for targeting, advanced mode
references/crawl.md - Crawl vs Map, instructions for semantic focus, use cases, Map-then-Extract pattern
references/research.md - Prompting best practices, model selection, streaming, structured output schemas
references/integrations.md - LangChain, LlamaIndex, CrewAI, Vercel AI SDK, and framework integrations
Weekly Installs
8.8K
Repository
tavily-ai/skills
GitHub Stars
259
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn