---
rating: ⭐⭐
title: alphaear-news
url: https://skills.sh/rkiding/awesome-finance-skills/alphaear-news
---

# alphaear-news

skills/rkiding/awesome-finance-skills/alphaear-news
alphaear-news
Installation
$ npx skills add https://github.com/rkiding/awesome-finance-skills --skill alphaear-news
SKILL.md
AlphaEar News Skill
Overview

Fetch real-time hot news, generate unified trend reports, and retrieve Polymarket prediction data.

Capabilities
1. Fetch Hot News & Trends

Use scripts/news_tools.py via NewsNowTools.

Fetch News: fetch_hot_news(source_id, count)
See sources.md for valid source_ids (e.g., cls, weibo).
Unified Report: get_unified_trends(sources)
Aggregates top news from multiple sources.
2. Fetch Prediction Markets

Use scripts/news_tools.py via PolymarketTools.

Market Summary: get_market_summary(limit)
Returns a formatted report of active prediction markets.
Dependencies
requests, loguru
scripts/database_manager.py (Local DB)
Weekly Installs
813
Repository
rkiding/awesome…e-skills
GitHub Stars
2.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn