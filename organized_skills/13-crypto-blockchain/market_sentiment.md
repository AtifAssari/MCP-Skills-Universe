---
rating: ⭐⭐
title: market-sentiment
url: https://skills.sh/kukapay/crypto-skills/market-sentiment
---

# market-sentiment

skills/kukapay/crypto-skills/market-sentiment
market-sentiment
Installation
$ npx skills add https://github.com/kukapay/crypto-skills --skill market-sentiment
SKILL.md
Crypto Market Sentiment
Overview

This skill enables aggregation of news from popular cryptocurrency RSS feeds, performs sentiment analysis on the articles, and computes a market sentiment score ranging from -1 (highly negative) to +1 (highly positive), along with evidence-based explanations.

Workflow

Follow these steps to analyze crypto market sentiment:

Select RSS Feeds: Choose popular crypto RSS feeds (see references/rss_feeds.md for a curated list).
Fetch News: Retrieve recent articles from the selected feeds.
Analyze Sentiment: Classify each article's sentiment as positive (+1), negative (-1), or neutral (0) based on content keywords and context.
Calculate Score: Compute the average sentiment score across all articles.
Generate Explanation: Provide evidence from the news items supporting the score.
Sentiment Classification Guidelines
Positive (+1): News about adoption, launches, partnerships, ETF approvals, price rallies, regulatory wins, or technological breakthroughs.
Negative (-1): News about hacks, crashes, regulatory crackdowns, liquidations, delays, or criticisms.
Neutral (0): Factual updates, mixed outcomes, or speculative content without clear bias.
Output Format

The skill outputs:

Sentiment Score: Numerical value between -1 and 1.
Explanation: Breakdown by feed/source, key positive/negative drivers, and overall market implications.
Resources
scripts/
sentiment_analyzer.py: Python script to fetch RSS feeds, parse articles, and compute sentiment score. Run with python sentiment_analyzer.py to get automated results.
references/
rss_feeds.md: List of popular crypto RSS feeds with URLs and descriptions.
sentiment_examples.md: Examples of sentiment classification for common news types.
Weekly Installs
360
Repository
kukapay/crypto-skills
GitHub Stars
17
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn