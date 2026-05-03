---
rating: ⭐⭐
title: news-sentiment
url: https://skills.sh/staskh/trading_skills/news-sentiment
---

# news-sentiment

skills/staskh/trading_skills/news-sentiment
news-sentiment
Installation
$ npx skills add https://github.com/staskh/trading_skills --skill news-sentiment
SKILL.md
News Sentiment

Fetch recent news from Yahoo Finance.

Instructions

Note: If uv is not installed or pyproject.toml is not found, replace uv run python with python in all commands below.

uv run python scripts/news.py SYMBOL [--limit LIMIT]

Arguments
SYMBOL - Ticker symbol
--limit - Number of articles (default: 10)
Output

Returns JSON with:

articles - Array of recent news with title, publisher, date, link
summary - Brief summary of overall sentiment

Present key headlines and note any significant news that could impact the stock.

Dependencies
yfinance
Timezone

All timestamps and time-based calculations must use the America/New_York timezone. All JSON output must include generated_at (NY time string) and data_delay fields.

Weekly Installs
95
Repository
staskh/trading_skills
GitHub Stars
139
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn