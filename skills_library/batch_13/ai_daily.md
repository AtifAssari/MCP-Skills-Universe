---
title: ai-daily
url: https://skills.sh/geekjourneyx/mind-skills/ai-daily
---

# ai-daily

skills/geekjourneyx/mind-skills/ai-daily
ai-daily
Installation
$ npx skills add https://github.com/geekjourneyx/mind-skills --skill ai-daily
SKILL.md
AI Daily News

Fetch AI industry news from smol.ai RSS feed.

Quick Start
# Basic queries
昨天AI资讯
今天的AI新闻
2026-01-13的资讯

Query Types
Type	Examples	Description
Relative date	昨天AI资讯 今天的新闻 前天	Yesterday, today, day before
Absolute date	2026-01-13的新闻	YYYY-MM-DD format
Date range	有哪些日期的新闻	Show available dates
Workflow
- [ ] Step 1: Parse date from user request
- [ ] Step 2: Fetch RSS data
- [ ] Step 3: Check content availability
- [ ] Step 4: Format and display results

Step 1: Parse Date
User Input	Target Date	Calculation
昨天	Yesterday	today - 1 day
前天	Day before	today - 2 days
今天	Today	Current date
2026-01-13	2026-01-13	Direct parse

Format: Always use YYYY-MM-DD

Step 2: Fetch RSS
python skills/ai-daily/scripts/fetch_news.py --date YYYY-MM-DD


Available commands:

# Get specific date
python skills/ai-daily/scripts/fetch_news.py --date 2026-01-13

# Get date range
python skills/ai-daily/scripts/fetch_news.py --date-range

# Relative dates
python skills/ai-daily/scripts/fetch_news.py --relative yesterday


Requirements: pip install feedparser requests

Step 3: Check Content
When NOT Found
Sorry, no news available for 2026-01-14

Available date range: 2026-01-10 ~ 2026-01-13

Suggestions:
- View 2026-01-13 news
- View 2026-01-12 news

Step 4: Format Results

Example Output:

# AI Daily · 2026年1月13日

> not much happened today

## Content

[News content from smol.ai RSS...]

---
Source: smol.ai

Configuration
Variable	Description	Default
RSS_URL	RSS feed URL	https://news.smol.ai/rss.xml

No API keys required.

Troubleshooting
Issue	Solution
RSS fetch fails	Check network connectivity
Invalid date	Use YYYY-MM-DD format
No content	Check available date range
References
Output Format - Markdown template
HTML Themes - Webpage theme specifications
Weekly Installs
208
Repository
geekjourneyx/mind-skills
GitHub Stars
25
First Seen
Feb 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn