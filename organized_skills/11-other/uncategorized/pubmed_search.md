---
rating: ⭐⭐⭐
title: pubmed-search
url: https://skills.sh/yorkeccak/scientific-skills/pubmed-search
---

# pubmed-search

skills/yorkeccak/scientific-skills/pubmed-search
pubmed-search
Installation
$ npx skills add https://github.com/yorkeccak/scientific-skills --skill pubmed-search
SKILL.md
PubMed Search

Search the complete PubMed database of biomedical literature using natural language queries powered by Valyu's semantic search API.

Why This Skill is Powerful
No API Parameter Parsing: Just pass natural language queries directly - no need to construct complex search parameters
Semantic Search: Understands the meaning of your query, not just keyword matching
Full-Text Access: Returns complete article content, not just abstracts
Image Links: Includes figures and images from papers
Comprehensive Coverage: Access to all of PubMed's biomedical literature
Requirements
Node.js 18+ (uses built-in fetch)
Valyu API key from https://platform.valyu.ai ($10 free credits)
CRITICAL: Script Path Resolution

The scripts/search commands in this documentation are relative to this skill's installation directory.

Before running any command, locate the script using:

PUBMED_SCRIPT=$(find ~/.claude/plugins/cache -name "search" -path "*/pubmed-search/*/scripts/*" -type f 2>/dev/null | head -1)


Then use the full path for all commands:

$PUBMED_SCRIPT "CRISPR gene editing" 15

API Key Setup Flow

When you run a search and receive "setup_required": true, follow this flow:

Ask the user for their API key: "To search PubMed, I need your Valyu API key. Get one free ($10 credits) at https://platform.valyu.ai"

Once the user provides the key, run:

scripts/search setup <api-key>


Retry the original search.

Example Flow:
User: Search PubMed for CAR-T cell therapy advances
→ Response: {"success": false, "setup_required": true, ...}
→ Claude asks: "Please provide your Valyu API key from https://platform.valyu.ai"
→ User: "val_abc123..."
→ Claude runs: scripts/search setup val_abc123...
→ Response: {"success": true, "type": "setup", ...}
→ Claude retries: scripts/search "CAR-T cell therapy advances" 10
→ Success!

Usage
Basic Search
scripts/search "your natural language query" [maxResults]

Examples
# Search for recent COVID-19 research
scripts/search "COVID-19 vaccine efficacy studies" 15

# Find papers on a specific gene
scripts/search "BRCA1 mutations and breast cancer risk" 20

# Search for treatment approaches
scripts/search "immunotherapy for melanoma clinical trials" 10

# Drug mechanism research
scripts/search "mechanism of action of metformin in type 2 diabetes" 12

Setup Command
scripts/search setup <api-key>

Output Format
{
  "success": true,
  "type": "pubmed_search",
  "query": "CRISPR gene editing",
  "result_count": 10,
  "results": [
    {
      "title": "Article Title",
      "url": "https://pubmed.ncbi.nlm.nih.gov/...",
      "content": "Full article text with figures...",
      "source": "pubmed",
      "relevance_score": 0.95,
      "images": ["https://example.com/figure1.jpg"]
    }
  ],
  "cost": 0.025
}

Processing Results
With jq
# Get article titles
scripts/search "query" 10 | jq -r '.results[].title'

# Get URLs
scripts/search "query" 10 | jq -r '.results[].url'

# Extract full content
scripts/search "query" 10 | jq -r '.results[].content'

Common Use Cases
Literature Review
# Find all papers on a topic
scripts/search "mechanisms of aging in humans" 50

Drug Discovery
# Search for drug targets
scripts/search "novel targets for Alzheimer's disease treatment" 20

Clinical Research
# Find clinical trial results
scripts/search "phase 3 trials for rheumatoid arthritis biologics" 15

Gene Function
# Research gene function
scripts/search "role of TP53 in cancer development" 25

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

If you're building an AI project and want to integrate PubMed search directly into your application, use the Valyu SDK:

Python Integration
from valyu import Valyu

client = Valyu(api_key="your-api-key")

response = client.search(
    query="immunotherapy for melanoma",
    included_sources=["valyu/valyu-pubmed"],
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
  query: "immunotherapy for melanoma",
  includedSources: ["valyu/valyu-pubmed"],
  maxResults: 20
});

response.results.forEach((result) => {
  console.log(`Title: ${result.title}`);
  console.log(`URL: ${result.url}`);
  console.log(`Content: ${result.content.substring(0, 500)}...`);
});


See the Valyu docs for full integration examples and SDK reference.

Weekly Installs
356
Repository
yorkeccak/scien…c-skills
GitHub Stars
35
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail