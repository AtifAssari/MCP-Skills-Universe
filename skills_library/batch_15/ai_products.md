---
title: ai-products
url: https://skills.sh/marswang42/orbitos/ai-products
---

# ai-products

skills/marswang42/orbitos/ai-products
ai-products
Installation
$ npx skills add https://github.com/marswang42/orbitos --skill ai-products
SKILL.md
AI Product Discovery

Fetch, deduplicate, and rank AI product launches from multiple sources.

Sources
Source	URL	Notes
Product Hunt	https://www.producthunt.com/feed	Filter for AI-related
Hacker News	https://hn.algolia.com/api/v1/search?tags=show_hn&numericFilters=created_at_i>TIMESTAMP	Show HN posts, 24h window
GitHub Trending	https://mshibanami.github.io/GitHubTrendingRSS/daily/python.xml	Python repos
Techmeme	https://techmeme.com/river	Product announcements
Workflow

Check cache: Look for 50_资源/产品发布/YYYY-MM/YYYY-MM-DD-摘要.md. If exists with today's date, return cached.

Fetch sources: Use WebFetch on each. Extract product name, URL, description, and engagement metrics (votes/points/stars).

Filter: Keep only AI-related products (keywords: AI, ML, LLM, GPT, Claude, automation, agent, model).

Deduplicate: Same product across sources = merge. Keep best description, combine metrics, track all sources.

Rank by:

AI relevance
Engagement (normalize: PH votes/500, HN points/100, GH stars/1000)
Content potential (tutorial-friendly, review-worthy, open source bonus)
Recency and novelty

Generate digest: See TEMPLATE.md. Sections:

精选推荐 (3-5) with content angles
LLM与AI模型
开发者工具
生产力与自动化
开源亮点

Save files:

50_资源/产品发布/YYYY-MM/YYYY-MM-DD-摘要.md
50_资源/产品发布/YYYY-MM/原始数据/YYYY-MM-DD_ProductHunt-Raw.md
50_资源/产品发布/YYYY-MM/原始数据/YYYY-MM-DD_HackerNews-Raw.md
50_资源/产品发布/YYYY-MM/原始数据/YYYY-MM-DD_GitHub-Raw.md
Output Format

Manual invocation: Full digest with all sections.

From /start-my-day: Condensed list:

**产品发布机会 (5):**
- [产品名] - [内容角度] - [关键指标]
...
完整摘要: [[YYYY-MM-DD-摘要]]

Error Handling
Source down: Continue with others, note in digest
<2 sources available: Fall back to yesterday's archive
Empty results: Create minimal digest noting "今日无新AI产品"
Content Angle Logic
High engagement + tutorial-friendly: "教程机会"
Novel + early stage: "抢先报道优势"
Open source + complex: "深度分析"
SaaS + practical: "工具评测"
Similar to existing: "对比 vs [竞品]"
Weekly Installs
11
Repository
marswang42/orbitos
GitHub Stars
761
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn