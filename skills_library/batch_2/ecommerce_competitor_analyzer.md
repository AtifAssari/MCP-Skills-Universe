---
title: ecommerce-competitor-analyzer
url: https://skills.sh/buluslan/ecommerce-competitor-analyzer/ecommerce-competitor-analyzer
---

# ecommerce-competitor-analyzer

skills/buluslan/ecommerce-competitor-analyzer/ecommerce-competitor-analyzer
ecommerce-competitor-analyzer
Installation
$ npx skills add https://github.com/buluslan/ecommerce-competitor-analyzer --skill ecommerce-competitor-analyzer
Summary

Automated scraping and AI-powered analysis of e-commerce products across Amazon, Temu, and Shopee.

Extracts product data (title, price, rating, reviews) from multiple platforms via batch scraping with error isolation, ensuring single failures don't halt processing
Analyzes each product across four dimensions: copywriting strategy and keyword frequency, visual design methodology, customer review sentiment, and market positioning gaps
Outputs results in dual formats: structured Google Sheets table and detailed markdown report with strategic insights
Supports bulk processing of product identifiers (ASINs or URLs) in parallel, with typical analysis completing in 1–2 minutes per product using Gemini AI and Olostep scraping APIs
SKILL.md
E-commerce Competitor Analyzer Skill
Quick Start (For AI)

When to use this skill: When user asks to analyze, research, or extract insights from e-commerce products (Amazon, Temu, Shopee).

What you should do:

Extract product identifiers (ASINs or URLs) from user input
Call the scraper script to get product data
Call the AI analysis with the analysis prompt template
Output results in BOTH formats: Google Sheets + Markdown

Input examples:

"Analyze B0C4YT8S6H"
"Analyze these products: B0C4YT8S6H, B08N5WRQ1Y, B0CLFH7CCV"
"Research this competitor: https://amazon.com/dp/B0C4YT8S6H"

Output requirements:

Google Sheets table with: ASIN, Title, Price, Rating, 4 analysis summaries
Markdown report with detailed 4-dimensional analysis
How AI Should Process Requests
Step 1: Extract Product Identifiers

From user input, extract all ASINs and/or URLs:

Example inputs:

"Analyze these Amazon products:
B0C4YT8S6H
B08N5WRQ1Y
B0CLFH7CCV"


Extract: ['B0C4YT8S6H', 'B08N5WRQ1Y', 'B0CLFH7CCV']

Mixed input handling:

"Analyze B0C4YT8S6H and https://amazon.com/dp/B08N5WRQ1Y"


Extract: ['B0C4YT8S6H', 'B08N5WRQ1Y'] (extract ASIN from URL)

Step 2: Batch Scrape Product Data

For each product identifier:

Detect platform (use scripts/detect-platform.js if available)
Call appropriate scraper (Amazon: scripts/scrape-amazon.js)
Use Olostep API with configured API key from .env

Batch processing pattern:

// Process all products in parallel
const products = ['B0C4YT8S6H', 'B08N5WRQ1Y', 'B0CLFH7CCV'];
const results = await Promise.allSettled(
  products.map(asin => scrapeAmazon(asin))
);

// Handle failures gracefully
const successful = results.filter(r => r.status === 'fulfilled');
const failed = results.filter(r => r.status === 'rejected');

Step 3: Batch AI Analysis

For each successfully scraped product:

Read the analysis prompt from prompts/analysis-prompt-base.md
Replace product data placeholders in the prompt
Call Gemini API (model: gemini-3-flash-preview)
Extract structured analysis results

Analysis framework (4 dimensions):

文案构建逻辑与词频分析 (The Brain) - Copywriting strategy & keywords
视觉资产设计思路 (The Face) - Visual design methodology
评论定量与定性分析 (The Voice) - Review sentiment analysis
市场维态与盲区扫描 (The Pulse) - Market positioning & blind spots
Step 4: Generate Dual Format Output

Format 1: Google Sheets (Structured Data)

Write to Google Sheets with columns: | ASIN | 产品标题 | 价格 | 评分 | 文案分析摘要 | 视觉分析摘要 | 评论分析摘要 | 市场分析摘要 |

Sheet selection priority:

User explicitly specified Sheet ID/Name/URL
Default from .env (GOOGLE_SHEETS_ID)
Ask user to provide Sheet ID

Format 2: Markdown Report (Detailed Analysis)

Generate file: 竞品分析-YYYY-MM-DD.md

Structure:

# Amazon Competitor Analysis Report

## Analysis Overview
- Products analyzed: 3
- Analysis date: 2026-01-29
- Total time: ~5 minutes

---

## Product 1: B0C4YT8S6H

### Basic Information
- Title: [Product title]
- Price: [Price]
- Rating: [Rating]

### Copywriting Strategy & Keyword Analysis
[Full analysis...]

### Visual Asset Design Methodology
[Full analysis...]

### Customer Review Analysis
[Full analysis...]

### Market Positioning & Competitive Intelligence
[Full analysis...]

---

File Structure
ecommerce-competitor-analyzer.skill/
├── SKILL.md                                # This file (AI instructions)
├── platforms.yaml                          # Platform configurations (URL patterns, regex)
├── .env.example                            # Configuration template (API keys)
├── prompts/                                # AI prompt templates
│   └── analysis-prompt-base.md            # Base analysis framework (from n8n)
├── scripts/                                # Processing scripts
│   ├── detect-platform.js                 # Platform detection utility
│   ├── scrape-amazon.js                   # Amazon scraper (Olostep API)
│   └── batch-processor.js                 # Batch processing engine
└── references/                             # Documentation
    └── n8n-workflow-analysis.md           # n8n workflow insights

Configuration Files
platforms.yaml

Contains platform-specific configurations:

URL patterns for platform detection
ASIN extraction regex patterns
Scraper API endpoints
Data extraction patterns

Key sections:

platforms:
  amazon:
    url_patterns: ["amazon.com", "amazon.co.uk", ...]
    asin_regex:
      standard: "/dp/([A-Z0-9]{10})"
    scraper:
      provider: "olostep"
      api_endpoint: "https://api.olostep.com/v2/agent/web-agent"

.env.example

Template for required API keys:

OLOSTEP_API_KEY=your_olostep_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_SHEETS_ID=YOUR_GOOGLE_SHEETS_ID_HERE


Critical: Always check if .env file exists and contains required keys before processing.

Analysis Prompt Template

The AI analysis uses a proven 4-dimensional framework. The exact prompt is stored in: prompts/analysis-prompt-base.md

Key sections:

Role: 10-year experienced Amazon Operations Director & Brand Strategist
Goal: Deep scan of product listing to extract strategic insights
Output Structure:
Part 1: 文案构建逻辑与词频分析
Part 2: 视觉资产设计思路
Part 3: 评论定量与定性分析
Part 4: 市场维态与盲区扫描

Important: Use the prompt EXACTLY as provided in the template without modifications.

API Services
Olostep API (Web Scraping)
Purpose: Scrape Amazon product pages with rendered JavaScript
Endpoint: https://api.olostep.com/v2/agent/web-agent
Cost: 1000 free requests/month, then $0.002/request
Key param: comments_to_scrape: 100 (matching n8n config)
Google Gemini API (AI Analysis)
Purpose: Generate comprehensive product analysis
Model: gemini-3-flash-preview (cost-effective)
Cost: ~$0.001/product
Alternative: gemini-2-flash-thinking (for complex analysis)
Google Sheets API (Data Storage)
Purpose: Export structured results
Authentication: OAuth2 service account
Cost: Free tier
Error Handling
Batch Processing with Error Isolation

Critical pattern from n8n workflow:

const items = productIdentifiers;
const results = await Promise.allSettled(
  items.map(async (item, index) => {
    try {
      const data = await scrapeProduct(item);
      const analysis = await analyzeWithAI(data);
      return { success: true, index, data: analysis };
    } catch (error) {
      // Single failure doesn't stop batch
      return { success: false, index, error: error.message };
    }
  })
);

// Report results
const successful = results.filter(r => r.status === 'fulfilled' && r.value.success);
const failed = results.filter(r => r.status === 'rejected' || !r.value.success);

console.log(`Processed: ${successful.length} succeeded, ${failed.length} failed`);

Common Errors & Solutions
Error	Cause	Solution
OLOSTEP_API_KEY not found	Missing .env file	Check .env exists and contains key
Invalid ASIN format	Malformed ASIN	Validate ASIN: 10 alphanumeric chars
Scraping timeout	Slow page load	Increase timeout or retry
Gemini rate limit	Too many requests	Add delay between batches
Platform Detection Logic
function detectPlatform(urlOrId) {
  // Direct ASIN
  if (/^[A-Z0-9]{10}$/.test(urlOrId)) {
    return { platform: 'amazon', id: urlOrId };
  }

  // Amazon URL patterns
  if (/amazon\.(com|co\.uk|de|es|fr|it|ca|co\.jp)/i.test(urlOrId)) {
    const asinMatch = urlOrId.match(/\/dp\/([A-Z0-9]{10})/i);
    if (asinMatch) {
      return { platform: 'amazon', id: asinMatch[1] };
    }
  }

  // Other platforms (future)
  // if (/temu\.com/i.test(urlOrId)) return { platform: 'temu', id: extractId(urlOrId) };

  return null;
}

Implementation Notes
Current Version: Phase 1 MVP

Supported Platforms: Amazon (US only) Input Method: Dialog-based (ASINs or URLs) Output Format: Google Sheets table + Markdown report

Roadmap
✅ Phase 1: Amazon MVP (current)
🔄 Phase 2: Add Temu & Shopee platforms
🔄 Phase 3: Cross-platform comparison
🔄 Phase 4: Historical tracking & price alerts
Design Philosophy

This skill follows the error isolation pattern from the n8n workflow:

Single product failure NEVER stops the entire batch
Always report both successes and failures
Provide detailed error messages for debugging
Performance Benchmarks
Operation	Time	Cost
Single product scrape	~30 seconds	$0.002 (Olostep)
Single product analysis	~45 seconds	$0.001 (Gemini)
Total per product	~1-2 minutes	~$0.003
Batch of 10 products	~10-15 minutes (parallel)	~$0.03
References
n8n Workflow: Based on v81 workflow logic
Platform Config: See platforms.yaml for URL patterns and extraction rules
Analysis Prompt: See prompts/analysis-prompt-base.md for exact prompt template
Important Reminders for AI
ALWAYS extract ALL product identifiers from user input before processing
ALWAYS use batch processing with Promise.allSettled for error isolation
ALWAYS generate BOTH output formats: Google Sheets + Markdown
NEVER modify the analysis prompt - use it exactly as provided
ALWAYS validate .env exists before starting processing
ALWAYS report processing summary: X succeeded, Y failed
If Google Sheets ID is missing, ask user to provide it
Use the exact prompt from prompts/analysis-prompt-base.md without any modifications
Weekly Installs
983
Repository
buluslan/ecomme…analyzer
GitHub Stars
40
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn