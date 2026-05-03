---
rating: ⭐⭐
title: ai-newsletters
url: https://skills.sh/marswang42/orbitos/ai-newsletters
---

# ai-newsletters

skills/marswang42/orbitos/ai-newsletters
ai-newsletters
Installation
$ npx skills add https://github.com/marswang42/orbitos --skill ai-newsletters
SKILL.md
AI Newsletter Curation

Fetch, deduplicate, and rank AI newsletter content into a daily digest.

RSS Sources
TLDR AI: https://bullrich.dev/tldr-rss/ai.rss
The Rundown AI: https://rss.beehiiv.com/feeds/2R3C6Bt5wj.xml
Workflow

Check cache: Look for 50_资源/Newsletters/YYYY-MM/YYYY-MM-DD-摘要.md. If exists with today's date, return cached content.

Fetch feeds: Use WebFetch on both RSS URLs. Extract title, link, pubDate, description for each item.

Deduplicate: Merge items with similar titles (80%+ word overlap). Keep longer description, track both sources.

Rank items by:

AI relevance (LLM, GPT, Claude, agents, ML keywords)
Productivity relevance (workflow, automation, tools, PKM)
Recency (newer = higher)
Novelty (check recent archives, penalize repeats)

Generate digest: See TEMPLATE.md for format. Include:

精选推荐 (3-5 highest scoring) with content creation angles
AI动态 section
生产力工具 section
Stats footer

Save files:

50_资源/Newsletters/YYYY-MM/YYYY-MM-DD-摘要.md (curated)
50_资源/Newsletters/YYYY-MM/原始数据/YYYY-MM-DD_TLDR-AI-Raw.md
50_资源/Newsletters/YYYY-MM/原始数据/YYYY-MM-DD_Rundown-AI-Raw.md
Output Format

Manual invocation: Display full digest with all sections.

From /start-my-day: Return condensed list:

**内容机会 (5):**
- [标题] - [角度]
...
完整摘要: [[YYYY-MM-DD-摘要]]

Error Handling
One feed down: Continue with other, note in digest
Both down: Use yesterday's archive with warning
Empty feeds: Create minimal digest noting "今日无新内容"
Weekly Installs
13
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