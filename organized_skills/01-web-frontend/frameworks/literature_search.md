---
rating: ⭐⭐⭐
title: literature-search
url: https://skills.sh/yorkeccak/scientific-skills/literature-search
---

# literature-search

skills/yorkeccak/scientific-skills/literature-search
literature-search
Installation
$ npx skills add https://github.com/yorkeccak/scientific-skills --skill literature-search
SKILL.md
Literature Search

Search across all major scientific literature databases (PubMed, arXiv, bioRxiv, medRxiv) simultaneously using natural language queries powered by Valyu's semantic search API.

Why This Skill is Powerful
No API Parameter Parsing: Just pass natural language queries directly - no need to construct complex search parameters
Semantic Search: Understands the meaning of your query, not just keyword matching
Full-Text Access: Returns complete article content, not just abstracts
Image Links: Includes figures and images from papers
Comprehensive Coverage: Search across PubMed, arXiv, bioRxiv, and medRxiv simultaneously
Unified Results: Get results from all sources in a single query
Requirements
Node.js 18+ (uses built-in fetch)
Valyu API key from https://platform.valyu.ai ($10 free credits)
CRITICAL: Script Path Resolution

The scripts/search commands in this documentation are relative to this skill's installation directory.

Before running any command, locate the script using:

LITERATURE_SCRIPT=$(find ~/.claude/plugins/cache -name "search" -path "*/literature-search/*/scripts/*" -type f 2>/dev/null | head -1)


Then use the full path for all commands:

$LITERATURE_SCRIPT "CRISPR gene editing advances" 15

API Key Setup Flow

When you run a search and receive "setup_required": true, follow this flow:

Ask the user for their API key: "To search scientific literature, I need your Valyu API key. Get one free ($10 credits) at https://platform.valyu.ai"

Once the user provides the key, run:

scripts/search setup <api-key>


Retry the original search.

When to Use This Skill
Comprehensive literature reviews across all domains
Finding all relevant research on a topic
Cross-domain scientific discovery
Combining biomedical, physics, and preprint literature
Emerging research across disciplines
Output Format
{
  "success": true,
  "type": "literature_search",
  "query": "CRISPR gene editing advances",
  "result_count": 15,
  "results": [
    {
      "title": "Article Title",
      "url": "https://...",
      "content": "Full article text with figures...",
      "source": "pubmed|arxiv|biorxiv|medrxiv",
      "relevance_score": 0.95,
      "images": ["https://example.com/figure1.jpg"]
    }
  ],
  "cost": 0.025
}

Processing Results
With jq
# Get article titles
scripts/search "query" 20 | jq -r '.results[].title'

# Get URLs
scripts/search "query" 20 | jq -r '.results[].url'

# Extract full content
scripts/search "query" 20 | jq -r '.results[].content'

# Filter by source
scripts/search "query" 20 | jq -r '.results[] | select(.source == "arxiv") | .title'

Common Use Cases
Comprehensive Literature Review
# Search across all sources for thorough review
scripts/search "mechanisms of cellular senescence" 100

Cross-Disciplinary Research
# Find papers spanning multiple fields
scripts/search "quantum computing applications in drug discovery" 50

Recent Developments
# Get latest preprints and publications
scripts/search "foundation models for protein folding" 30

Medical Research
# Search biomedical literature comprehensively
scripts/search "immunotherapy checkpoint inhibitors resistance" 40

Error Handling

All commands return JSON with success field:

{
  "success": false,
  "error": "Error message"
}


Exit codes:

0 - Success
1 - Error (check JSON for details)
API Endpoint
Base URL: https://api.valyu.ai/v1
Endpoint: /search
Authentication: X-API-Key header
Architecture
scripts/
├── search          # Bash wrapper
└── search.mjs      # Node.js CLI


Direct API calls using Node.js built-in fetch(), zero external dependencies.

Adding to Your Project

If you're building an AI project and want to integrate Literature Search directly into your application, use the Valyu SDK:

Python Integration
from valyu import Valyu

client = Valyu(api_key="your-api-key")

response = client.search(
    query="your search query here",
    included_sources=["valyu/valyu-pubmed", "valyu/valyu-arxiv", "valyu/valyu-biorxiv", "valyu/valyu-medrxiv"],
    max_results=20
)

for result in response["results"]:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Content: {result['content'][:500]}...")

TypeScript Integration
import { Valyu } from "valyu-js";

const client = new Valyu("your-api-key");

const response = await client.search({
  query: "your search query here",
  includedSources: ["valyu/valyu-pubmed", "valyu/valyu-arxiv", "valyu/valyu-biorxiv", "valyu/valyu-medrxiv"],
  maxResults: 20
});

response.results.forEach((result) => {
  console.log(`Title: ${result.title}`);
  console.log(`URL: ${result.url}`);
  console.log(`Content: ${result.content.substring(0, 500)}...`);
});


See the Valyu docs for full integration examples and SDK reference.

Weekly Installs
340
Repository
yorkeccak/scien…c-skills
GitHub Stars
35
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail