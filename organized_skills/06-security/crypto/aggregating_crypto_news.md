---
rating: ⭐⭐⭐
title: aggregating-crypto-news
url: https://skills.sh/jeremylongshore/claude-code-plugins-plus-skills/aggregating-crypto-news
---

# aggregating-crypto-news

skills/jeremylongshore/claude-code-plugins-plus-skills/aggregating-crypto-news
aggregating-crypto-news
Installation
$ npx skills add https://github.com/jeremylongshore/claude-code-plugins-plus-skills --skill aggregating-crypto-news
SKILL.md
Aggregating Crypto News
Overview

Aggregate cryptocurrency news from 50+ authoritative sources via RSS feeds with real-time scanning, coin/category filtering, and relevance scoring.

Prerequisites
Python 3.8+ installed
Dependencies: pip install feedparser requests
Internet connectivity for RSS feed access
Instructions

Assess user intent - determine filters needed:

General news: no filters, use defaults
Coin-specific: extract symbol (BTC, ETH, etc.)
Category-specific: extract category (defi, nft, regulatory, etc.)
Time-specific: extract window (1h, 4h, 24h, 7d)

Run the aggregator with appropriate filters:

# Default scan (top 20, past 24h, relevance sorted)
python ${CLAUDE_SKILL_DIR}/scripts/news_aggregator.py

# Coin-specific scan
python ${CLAUDE_SKILL_DIR}/scripts/news_aggregator.py --coin BTC --period 4h

# Category filter
python ${CLAUDE_SKILL_DIR}/scripts/news_aggregator.py --category defi --top 30

# Multiple filters
python ${CLAUDE_SKILL_DIR}/scripts/news_aggregator.py --coin ETH --category defi --period 24h --top 15


Export results for downstream processing:

python ${CLAUDE_SKILL_DIR}/scripts/news_aggregator.py --format json --output news.json


Present results to the user:

Show source, title, age, and relevance score
Highlight market-moving keywords if present
Provide links for full articles
Summarize meta information (sources checked, articles found)
Output

Table showing articles ranked by relevance score (0-100) based on market-moving keyword detection, source authority, and recency:

==============================================================================
  CRYPTO NEWS AGGREGATOR                            Updated: 2026-01-14 15:30  # 2026 - current year timestamp
==============================================================================

  TOP CRYPTO NEWS (24h)
------------------------------------------------------------------------------
  Rank  Source          Title                           Age     Score
------------------------------------------------------------------------------
    1   CoinDesk        Bitcoin Breaks $100K ATH        2h      95.0
    2   The Block       SEC Approves ETH ETF            4h      92.5
    3   Decrypt         Solana DeFi TVL Surges          6h      78.3
------------------------------------------------------------------------------

  Summary: 20 articles shown | Scanned: 50 sources | Matched: 187
==============================================================================

Error Handling
Error	Cause	Solution
Network timeout	RSS feed unreachable	Uses cached data; skips unavailable sources
Parse error	Malformed RSS	Skips entry; continues with valid articles
No results	Filters too strict	Suggest relaxing filters
Invalid coin	Unknown symbol	List similar valid symbols

See ${CLAUDE_SKILL_DIR}/references/errors.md for comprehensive error handling.

Examples

Filtering patterns for common news monitoring scenarios:

# Latest crypto news (defaults)
python ${CLAUDE_SKILL_DIR}/scripts/news_aggregator.py

# Bitcoin news from past 4 hours
python ${CLAUDE_SKILL_DIR}/scripts/news_aggregator.py --coin BTC --period 4h

# DeFi category news
python ${CLAUDE_SKILL_DIR}/scripts/news_aggregator.py --category defi

# High-relevance news only
python ${CLAUDE_SKILL_DIR}/scripts/news_aggregator.py --min-score 70 --top 10

# Multiple coins
python ${CLAUDE_SKILL_DIR}/scripts/news_aggregator.py --coins BTC,ETH,SOL

Resources
${CLAUDE_SKILL_DIR}/references/implementation.md - CLI options, categories, JSON format, advanced filtering
${CLAUDE_SKILL_DIR}/references/errors.md - Comprehensive error handling
${CLAUDE_SKILL_DIR}/references/examples.md - Detailed usage examples
${CLAUDE_SKILL_DIR}/config/sources.yaml - Full source registry
CoinDesk RSS: https://www.coindesk.com/arc/outboundfeeds/rss/
feedparser docs: https://feedparser.readthedocs.io/
Weekly Installs
216
Repository
jeremylongshore…s-skills
GitHub Stars
2.1K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn