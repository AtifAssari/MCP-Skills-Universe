---
rating: ⭐⭐⭐
title: seo-geo
url: https://skills.sh/agricidaniel/claude-seo/seo-geo
---

# seo-geo

skills/agricidaniel/claude-seo/seo-geo
seo-geo
Installation
$ npx skills add https://github.com/agricidaniel/claude-seo --skill seo-geo
SKILL.md
AI Search / GEO Optimization (February 2026)
Key Statistics
Metric	Value	Source
AI Overviews reach	1.5 billion users/month across 200+ countries	Google
AI Overviews query coverage	50%+ of all queries	Industry data
AI-referred sessions growth	527% (Jan-May 2025)	SparkToro
ChatGPT weekly active users	900 million	OpenAI
Perplexity monthly queries	500+ million	Perplexity
Critical Insight: Brand Mentions > Backlinks

Brand mentions correlate 3x more strongly with AI visibility than backlinks. (Ahrefs December 2025 study of 75,000 brands)

Signal	Correlation with AI Citations
YouTube mentions	~0.737 (strongest)
Reddit mentions	High
Wikipedia presence	High
LinkedIn presence	Moderate
Domain Rating (backlinks)	~0.266 (weak)

Only 11% of domains are cited by both ChatGPT and Google AI Overviews for the same query, so platform-specific optimization is essential.

GEO Analysis Criteria (Updated)
1. Citability Score (25%)

Optimal passage length: 134-167 words for AI citation.

Strong signals:

Clear, quotable sentences with specific facts/statistics
Self-contained answer blocks (can be extracted without context)
Direct answer in first 40-60 words of section
Claims attributed with specific sources
Definitions following "X is..." or "X refers to..." patterns
Unique data points not found elsewhere

Weak signals:

Vague, general statements
Opinion without evidence
Buried conclusions
No specific data points
2. Structural Readability (20%)

92% of AI Overview citations come from top-10 ranking pages, but 47% come from pages ranking below position 5, demonstrating different selection logic.

Strong signals:

Clean H1->H2->H3 heading hierarchy
Question-based headings (matches query patterns)
Short paragraphs (2-4 sentences)
Tables for comparative data
Ordered/unordered lists for step-by-step or multi-item content
FAQ sections with clear Q&A format

Weak signals:

Wall of text with no structure
Inconsistent heading hierarchy
No lists or tables
Information buried in paragraphs
3. Multi-Modal Content (15%)

Content with multi-modal elements sees 156% higher selection rates.

Check for:

Text + relevant images
Video content (embedded or linked)
Infographics and charts
Interactive elements (calculators, tools)
Structured data supporting media
4. Authority & Brand Signals (20%)

Strong signals:

Author byline with credentials
Publication date and last-updated date
Citations to primary sources (studies, official docs, data)
Organization credentials and affiliations
Expert quotes with attribution
Entity presence in Wikipedia, Wikidata
Mentions on Reddit, YouTube, LinkedIn

Weak signals:

Anonymous authorship
No dates
No sources cited
No brand presence across platforms
5. Technical Accessibility (20%)

AI crawlers do NOT execute JavaScript. Server-side rendering is critical.

Check for:

Server-side rendering (SSR) vs client-only content
AI crawler access in robots.txt
llms.txt file presence and configuration
RSL 1.0 licensing terms
AI Crawler Detection

Check robots.txt for these AI crawlers:

Crawler	Owner	Purpose
GPTBot	OpenAI	ChatGPT web search
OAI-SearchBot	OpenAI	OpenAI search features
ChatGPT-User	OpenAI	ChatGPT browsing
ClaudeBot	Anthropic	Claude web features
PerplexityBot	Perplexity	Perplexity AI search
CCBot	Common Crawl	Training data (often blocked)
anthropic-ai	Anthropic	Claude training
Bytespider	ByteDance	TikTok/Douyin AI
cohere-ai	Cohere	Cohere models

Recommendation: Allow GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot for AI search visibility. Block CCBot and training crawlers if desired.

llms.txt Standard

The emerging llms.txt standard provides AI crawlers with structured content guidance.

Location: /llms.txt (root of domain)

Format:

# Title of site
> Brief description

## Main sections
- [Page title](url): Description
- [Another page](url): Description

## Optional: Key facts
- Fact 1
- Fact 2


Check for:

Presence of /llms.txt
Structured content guidance
Key page highlights
Contact/authority information
RSL 1.0 (Really Simple Licensing)

New standard (December 2025) for machine-readable AI licensing terms.

Backed by: Reddit, Yahoo, Medium, Quora, Cloudflare, Akamai, Creative Commons

Check for: RSL implementation and appropriate licensing terms.

Platform-Specific Optimization
Platform	Key Citation Sources	Optimization Focus
Google AI Overviews	Top-10 ranking pages (92%)	Traditional SEO + passage optimization
ChatGPT	Wikipedia (47.9%), Reddit (11.3%)	Entity presence, authoritative sources
Perplexity	Reddit (46.7%), Wikipedia	Community validation, discussions
Bing Copilot	Bing index, authoritative sites	Bing SEO, IndexNow
Output

Generate GEO-ANALYSIS.md with:

GEO Readiness Score: XX/100
Platform breakdown (Google AIO, ChatGPT, Perplexity scores)
AI Crawler Access Status (which crawlers allowed/blocked)
llms.txt Status (present, missing, recommendations)
Brand Mention Analysis (presence on Wikipedia, Reddit, YouTube, LinkedIn)
Passage-Level Citability (optimal 134-167 word blocks identified)
Server-Side Rendering Check (JavaScript dependency analysis)
Top 5 Highest-Impact Changes
Schema Recommendations (for AI discoverability)
Content Reformatting Suggestions (specific passages to rewrite)
Quick Wins
Add "What is [topic]?" definition in first 60 words
Create 134-167 word self-contained answer blocks
Add question-based H2/H3 headings
Include specific statistics with sources
Add publication/update dates
Implement Person schema for authors
Allow key AI crawlers in robots.txt
Medium Effort
Create /llms.txt file
Add author bio with credentials + Wikipedia/LinkedIn links
Ensure server-side rendering for key content
Build entity presence on Reddit, YouTube
Add comparison tables with data
Implement FAQ sections (structured, not schema for commercial sites)
High Impact
Create original research/surveys (unique citability)
Build Wikipedia presence for brand/key people
Establish YouTube channel with content mentions
Implement comprehensive entity linking (sameAs across platforms)
Develop unique tools or calculators
DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, use ai_optimization_chat_gpt_scraper to check what ChatGPT web search returns for target queries (real GEO visibility check) and ai_opt_llm_ment_search with ai_opt_llm_ment_top_domains for LLM mention tracking across AI platforms.

Error Handling
Scenario	Action
URL unreachable (DNS failure, connection refused)	Report the error clearly. Do not guess site content. Suggest the user verify the URL and try again.
AI crawlers blocked by robots.txt	Report exactly which crawlers are blocked and which are allowed. Provide specific robots.txt directives to add for enabling AI search visibility.
No llms.txt found	Note the absence and provide a ready-to-use llms.txt template based on the site's content structure.
No structured data detected	Report the gap and provide specific schema recommendations (Article, Organization, Person) for improving AI discoverability.
FLOW Framework Integration

For prompt-guided AI content optimization, use /seo flow optimize <url> — FLOW's 21 optimize-stage prompts complement GEO's citability and structure analysis with evidence-led AI prompts.

Weekly Installs
1.3K
Repository
agricidaniel/claude-seo
GitHub Stars
5.9K
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn