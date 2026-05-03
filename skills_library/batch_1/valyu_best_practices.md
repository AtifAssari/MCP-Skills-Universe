---
title: valyu-best-practices
url: https://skills.sh/valyuai/skills/valyu-best-practices
---

# valyu-best-practices

skills/valyuai/skills/valyu-best-practices
valyu-best-practices
Installation
$ npx skills add https://github.com/valyuai/skills --skill valyu-best-practices
Summary

Real-time search, content extraction, AI-powered answers, and deep research across 25+ specialized data sources.

Four core APIs: Search (web, academic, financial, news), Contents (URL extraction with summarization), Answer (cited synthesis), and DeepResearch (comprehensive reports in fast/standard/heavy modes)
Supports domain-specific queries across academic papers, SEC filings, clinical trials, stock data, prediction markets, and transportation sources with source filtering
Official SDK libraries required for JavaScript/TypeScript (valyu-js) and Python (valyu) with built-in type safety, retries, and streaming support
Query best practices emphasize specificity, conciseness, and constraint-based filtering; complex requests should be split into focused queries
SKILL.md
Valyu Best Practices

This skill provides instructions for using the Valyu API to perform search, content extraction, AI-powered answers, and deep research tasks.

Quick Reference: Choosing the Right API

Use this decision tree to select the appropriate Valyu API:

What do you need?

├─ Find information across multiple sources
│  └─ Use Search API
│
├─ Extract content from specific URLs
│  └─ Use Contents API
│
├─ Get an AI-synthesized answer with citations
│  └─ Use Answer API
│
├─ Generate a comprehensive research report
│  └─ Use DeepResearch API
│
└─ Discover available data sources
   └─ Use Datasources API

⚠️ MANDATORY: Use Official Valyu SDK Libraries

CRITICAL: When writing code that uses the Valyu API, you MUST use the official SDK libraries. NEVER make raw HTTP/fetch calls to the Valyu API endpoints.

JavaScript/TypeScript: valyu-js
npm install valyu-js
# or
pnpm add valyu-js

import { Valyu } from 'valyu-js';

const valyu = new Valyu(process.env.VALYU_API_KEY);

// Now use valyu.search(), valyu.contents(), valyu.answer(), valyu.deepResearch

Python: valyu
pip install valyu
# or
uv add valyu

from valyu import Valyu

valyu = Valyu(api_key=os.environ.get("VALYU_API_KEY"))

# Now use valyu.search(), valyu.contents(), valyu.answer(), valyu.deep_research

Why SDK Over Raw API Calls?
Type safety - Full TypeScript/Python type hints for all parameters and responses
Automatic retries - Built-in retry logic for transient failures
Streaming support - Proper async iterator support for streaming responses
Error handling - Structured error types with helpful messages
Future compatibility - SDK updates handle API changes automatically
❌ NEVER Do This
// DON'T make raw fetch calls
const response = await fetch('https://api.valyu.ai/v1/search', {
  method: 'POST',
  headers: {
    'x-api-key': apiKey,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ query: '...' })
});

✅ Always Do This
// DO use the SDK
import { Valyu } from 'valyu-js';

const valyu = new Valyu(process.env.VALYU_API_KEY);
const response = await valyu.search({ query: '...' });

1. Search API

Purpose: Find information across web, academic, medical, transportation, financial, news, and proprietary sources.

When to Use
Finding recent information on any topic
Academic research (arXiv, PubMed, bioRxiv, medRxiv)
Financial data (SEC filings, earnings reports, stock data)
News monitoring and current events
Healthcare data (clinical trials, drug labels)
Prediction markets (Polymarket, Kalshi)
Transportation (UK National Rail, Global Shipping)
Basic Usage
const response = await valyu.search({
  query: "transformer architecture attention mechanism 2024",
  searchType: "all",
  maxNumResults: 10
});

Search Types
Type	Use For
all	Everything - web, academic, financial, proprietary
web	General internet content only
proprietary	Licensed academic papers and research
news	News articles and current events
Key Parameters
Parameter (TS/JS)	Parameter (Python)	Purpose	Example
query	query	Search query (under 400 chars)	"CRISPR gene editing 2024"
searchType	search_type	Source scope	"all", "web", "proprietary", "news"
maxNumResults	max_num_results	Number of results (1-20)	10
includedSources	included_sources	Limit to specific sources	["valyu/valyu-arxiv", "valyu/valyu-pubmed"]
startDate / endDate	start_date / end_date	Date filtering	"2024-01-01"
relevanceThreshold	relevance_threshold	Minimum relevance (0-1)	0.7
Domain-Specific Search Patterns

Academic Research:

await valyu.search({
  query: "CRISPR therapeutic applications clinical trials",
  searchType: "proprietary",
  includedSources: ["valyu/valyu-arxiv", "valyu/valyu-pubmed", "valyu/valyu-biorxiv"],
  startDate: "2024-01-01"
});


Financial Analysis:

await valyu.search({
  query: "Apple revenue Q4 2024 earnings",
  searchType: "all",
  includedSources: ["valyu/valyu-sec-filings", "valyu/valyu-earnings-US"]
});


News Monitoring:

await valyu.search({
  query: "AI regulation EU",
  searchType: "news",
  startDate: "2024-06-01",
  countryCode: "EU"
});

Search Recipes

For detailed patterns, see:

Basic Search Patterns
Academic Search
Finance Search
News Search
Healthcare Search
2. Contents API

Purpose: Extract clean, structured content from web pages optimized for LLM processing.

When to Use
Converting web pages to clean markdown
Extracting article text for summarization
Parsing documentation for RAG systems
Structured data extraction from product pages
Processing academic papers
Basic Usage
const response = await valyu.contents({
  urls: ["https://example.com/article"]
});

With Summarization
const response = await valyu.contents({
  urls: ["https://arxiv.org/abs/2401.12345"],
  summary: "Extract key findings in 3 bullet points"
});

Structured Extraction (JSON Schema)
const response = await valyu.contents({
  urls: ["https://example.com/product"],
  summary: {
    type: "object",
    properties: {
      product_name: { type: "string" },
      price: { type: "number" },
      features: { type: "array", items: { type: "string" } }
    },
    required: ["product_name", "price"]
  }
});

Key Parameters
Parameter (TS/JS)	Parameter (Python)	Purpose	Example
urls	urls	URLs to process (1-10)	["https://example.com"]
responseLength	response_length	Content length	"short", "medium", "large", "max"
extractEffort	extract_effort	Extraction quality	"normal", "high", "auto"
summary	summary	AI summarization	true, "instructions", or JSON schema
screenshot	screenshot	Capture screenshots	true
Content Recipes

For detailed patterns, see:

Basic Content Extraction
Extraction with Summary
Structured Extraction
Research Paper Extraction
3. Answer API

Purpose: Get AI-powered answers grounded in real-time search results with citations.

When to Use
Questions requiring current information synthesis
Multi-source fact verification
Technical documentation questions
Research requiring cited sources
Structured data extraction from search results
Basic Usage
const response = await valyu.answer({
  query: "What are the latest developments in quantum computing?"
});

With Fast Mode (Lower Latency)
const response = await valyu.answer({
  query: "Current Bitcoin price and 24h change",
  fastMode: true
});

With Custom Instructions
const response = await valyu.answer({
  query: "Compare React and Vue for enterprise applications",
  systemInstructions: "Provide a balanced comparison with pros and cons. Format as a comparison table."
});

With Streaming
const stream = await valyu.answer({
  query: "Explain transformer architecture",
  streaming: true
});

for await (const chunk of stream) {
  // Handle: search_results, content, metadata, done, error
  console.log(chunk);
}

Structured Output
const response = await valyu.answer({
  query: "Apple Q4 2024 financial highlights",
  structuredOutput: {
    type: "object",
    properties: {
      revenue: { type: "string" },
      growthRate: { type: "string" },
      keyHighlights: { type: "array", items: { type: "string" } }
    }
  }
});

Key Parameters
Parameter (TS/JS)	Parameter (Python)	Purpose	Example
query	query	Question to answer	"What is quantum computing?"
fastMode	fast_mode	Lower latency	true
systemInstructions	system_instructions	AI directives	"Be concise"
structuredOutput	structured_output	JSON schema	{type: "object", ...}
streaming	streaming	Enable SSE streaming	true
dataMaxPrice	data_max_price	Dollar limit	1.0
Answer Recipes

For detailed patterns, see:

Basic Answer
Fast Mode
Streaming
Custom Instructions
4. DeepResearch API

Purpose: Generate comprehensive research reports with detailed analysis and citations.

When to Use
Comprehensive market analysis
Literature reviews
Competitive intelligence
Technical deep dives
Topics requiring multi-source synthesis
Research Modes
Mode	Duration	Best For
fast	~5 minutes	Quick lookups, simple questions
standard	~10-20 minutes	Balanced research (most common)
heavy	~90 minutes	Comprehensive analysis, complex topics
Create Research Task
const task = await valyu.deepResearch.create({
  query: "AI chip market competitive landscape 2024",
  model: "standard"
});
// Returns: { deepresearch_id: "abc123", status: "queued" }

Poll for Completion
const status = await valyu.deepResearch.getStatus(task.deepresearch_id);
// status: "queued" | "running" | "completed" | "failed" | "cancelled"

if (status.status === "completed") {
  console.log(status.output);  // Markdown report
  console.log(status.sources); // Cited sources
  console.log(status.pdf_url); // PDF download link
}

Key Parameters
Parameter (TS/JS)	Parameter (Python)	Purpose	Example
query	query	Research question	"AI market trends 2024"
model	model	Research depth	"fast", "standard", "heavy"
outputFormat	output_format	Report format	"markdown", "pdf"
includedSources	included_sources	Source filtering	["valyu/valyu-arxiv", "techcrunch.com"]
startDate / endDate	start_date / end_date	Date range	"2024-01-01"
DeepResearch Recipes

For detailed patterns, see:

Fast Research
Standard Research
Heavy Research
5. Query Writing Best Practices
Core Principles
Be specific - Use domain terminology
Be concise - Keep queries under 400 characters
Be focused - One topic per query
Add constraints - Include timeframes, source types
Query Anatomy
Element	Description	Example
Intent	What you need	"latest advancements" vs "overview"
Domain	Topic terminology	"transformer architecture"
Constraints	Filters	"2024", "peer-reviewed"
Source type	Where to look	academic papers, SEC filings
Good vs Bad Queries
BAD:  "I want to know about AI"
GOOD: "transformer attention mechanism survey 2024"

BAD:  "Apple financial information"
GOOD: "Apple revenue growth Q4 2024 earnings SEC filing"

BAD:  "gene editing research"
GOOD: "CRISPR off-target effects therapeutic applications 2024"

Split Complex Requests
# Don't do this
"Tesla stock performance, new products, and Elon Musk statements"

# Do this instead
Query 1: "Tesla stock performance Q4 2024"
Query 2: "Tesla Cybertruck production updates 2024"
Query 3: "Tesla FSD autonomous driving progress"

Source Filtering

Use includedSources for domain authority:​Financial Research Collection. Some sources to include:

valyu/valyu-sec-filings - SEC regulatory filings
valyu/valyu-stocks - Stock market data
valyu/valyu-earnings-US - Earnings reports
reuters.com - Financial news
bloomberg.com - Market analysis​Medical Research Collection. Some sources to include:
valyu/valyu-pubmed - Medical literature
valyu/valyu-clinical-trials - Clinical trial data
valyu/valyu-drug-labels - FDA drug information
nejm.org - New England Journal of Medicine
thelancet.com - The Lancet​Tech Documentation Collection. Some sources to include:
docs.aws.amazon.com - AWS documentation
cloud.google.com/docs - Google Cloud docs
learn.microsoft.com - Microsoft docs
kubernetes.io/docs - Kubernetes docs
developer.mozilla.org - MDN Web Docs
// Academic
includedSources: ["valyu/valyu-arxiv", "valyu/valyu-pubmed", "nature"]

// Financial
includedSources: ["valyu/valyu-sec-filings", "bloomberg.com", "reuters.com"]

// Tech news
includedSources: ["techcrunch.com", "theverge.com", "arstechnica.com"]


For complete prompting guide, see references/prompting.md.

6. Common Workflows
Research Workflow
// 1. Quick search to find sources
const searchResults = await valyu.search({
  query: "CRISPR therapeutic applications",
  searchType: "proprietary",
  maxNumResults: 20
});

// 2. Extract key content from top results
const contents = await valyu.contents({
  urls: searchResults.results.slice(0, 3).map(r => r.url),
  summary: "Extract key findings"
});

// 3. Deep analysis for comprehensive report
const research = await valyu.deepResearch.create({
  query: "CRISPR therapeutic applications comprehensive review",
  model: "heavy"
});

Financial Analysis Workflow
// 1. Get SEC filings
const filings = await valyu.search({
  query: "Apple 10-K 2024",
  includedSources: ["valyu/valyu-sec-filings"]
});

// 2. Quick synthesis
const summary = await valyu.answer({
  query: "Apple Q4 2024 financial highlights",
  fastMode: true
});

// 3. Structured extraction
const metrics = await valyu.answer({
  query: "Apple financial metrics 2024",
  structuredOutput: {
    type: "object",
    properties: {
      revenue: { type: "string" },
      netIncome: { type: "string" },
      growthRate: { type: "string" }
    }
  }
});

7. Available Data Sources

Valyu provides access to 25+ specialized datasets:

Category	Examples
Academic	arXiv (2.5M+ papers), PubMed (37M+), bioRxiv, medRxiv
Financial	SEC filings, earnings transcripts, stock data, crypto
Healthcare	Clinical trials, DailyMed, PubChem, drug labels, ChEMBL, DrugBank, Open Target, WHO ICD
Economic	FRED, BLS, World Bank, US Treasury, Destatis
Predictions	Polymarket, Kalshi
Patents	US patent database
Transportation	UK Rail, Ship Tracking

For complete datasource reference, see references/datasources.md.

8. API Reference

For complete API documentation including all parameters, response structures, and error codes, see references/api-guide.md.

9. Integration Guides

Platform-specific integration documentation:

Anthropic Claude
OpenAI
Vercel AI SDK
LangChain
LlamaIndex
MCP Server
Additional Resources
All Recipes Index
Design Philosophy
Prompting Guide
Full API Reference
Weekly Installs
2.0K
Repository
valyuai/skills
GitHub Stars
17
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn