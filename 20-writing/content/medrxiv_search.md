---
title: medrxiv-search
url: https://skills.sh/yorkeccak/scientific-skills/medrxiv-search
---

# medrxiv-search

skills/yorkeccak/scientific-skills/medrxiv-search
medrxiv-search
Installation
$ npx skills add https://github.com/yorkeccak/scientific-skills --skill medrxiv-search
SKILL.md
medRxiv Search

Search the complete medRxiv database of medical and health sciences preprints using natural language queries powered by Valyu's semantic search API.

Why This Skill is Powerful
No API Parameter Parsing: Just pass natural language queries directly - no need to construct complex search parameters
Semantic Search: Understands the meaning of your query, not just keyword matching
Full-Text Access: Returns complete article content, not just abstracts
Image Links: Includes figures and images from papers
Comprehensive Coverage: Access to all medRxiv preprints in medical and health sciences
Requirements
Node.js 18+ (uses built-in fetch)
Valyu API key from https://platform.valyu.ai ($10 free credits)
CRITICAL: Script Path Resolution

The scripts/search commands in this documentation are relative to this skill's installation directory.

Before running any command, locate the script using:

MEDRXIV_SCRIPT=$(find ~/.claude/plugins/cache -name "search" -path "*/medrxiv-search/*/scripts/*" -type f 2>/dev/null | head -1)


Then use the full path for all commands:

$MEDRXIV_SCRIPT "COVID-19 vaccine efficacy" 15

API Key Setup Flow

When you run a search and receive "setup_required": true, follow this flow:

Ask the user for their API key: "To search medRxiv, I need your Valyu API key. Get one free ($10 credits) at https://platform.valyu.ai"

Once the user provides the key, run:

scripts/search setup <api-key>


Retry the original search.

When to Use This Skill
Accessing latest medical research before journal publication
Clinical trial results and outcomes
Epidemiological studies and public health data
Medical device and therapy research
Health policy and healthcare system studies
Rapid response research on emerging health topics
Output Format
{
  "success": true,
  "type": "medrxiv_search",
  "query": "COVID-19 vaccine efficacy",
  "result_count": 10,
  "results": [
    {
      "title": "Article Title",
      "url": "https://medrxiv.org/content/...",
      "content": "Full article text with figures...",
      "source": "medrxiv",
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
Clinical Medicine
# Find clinical research
scripts/search "heart failure treatment outcomes" 50

Public Health
# Search for epidemiology research
scripts/search "vaccine hesitancy determinants" 20

Medical Imaging
# Find imaging studies
scripts/search "AI in radiology diagnosis" 15

Infectious Disease
# Search for infectious disease papers
scripts/search "antibiotic resistance mechanisms" 25

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

If you're building an AI project and want to integrate medRxiv Search directly into your application, use the Valyu SDK:

Python Integration
from valyu import Valyu

client = Valyu(api_key="your-api-key")

response = client.search(
    query="your search query here",
    included_sources=["valyu/valyu-medrxiv"],
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
  includedSources: ["valyu/valyu-medrxiv"],
  maxResults: 20
});

response.results.forEach((result) => {
  console.log(`Title: ${result.title}`);
  console.log(`URL: ${result.url}`);
  console.log(`Content: ${result.content.substring(0, 500)}...`);
});


See the Valyu docs for full integration examples and SDK reference.

Weekly Installs
116
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