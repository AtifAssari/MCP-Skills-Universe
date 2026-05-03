---
title: daily-news
url: https://skills.sh/6551team/daily-news/daily-news
---

# daily-news

skills/6551team/daily-news/daily-news
daily-news
Installation
$ npx skills add https://github.com/6551team/daily-news --skill daily-news
SKILL.md
Daily News Skill

Query daily news and hot topics from the 6551 platform REST API. No authentication required.

Base URL: https://ai.6551.io

News Operations
1. Get News Categories

Get all available news categories and subcategories.

curl -s -X GET "https://ai.6551.io/open/free_categories"

2. Get Hot News

Get hot news articles and trending tweets by category.

curl -s -X GET "https://ai.6551.io/open/free_hot?category=macro"

Parameter	Type	Required	Description
category	string	Yes	Category key from free_categories
subcategory	string	No	Subcategory key

Response:

{
  "success": true,
  "category": "crypto",
  "subcategory": "defi",
  "news": {
    "success": true,
    "count": 10,
    "items": [
      {
        "id": 123,
        "title": "...",
        "source": "...",
        "link": "https://...",
        "score": 85,
        "grade": "A",
        "signal": "bullish",
        "summary_zh": "...",
        "summary_en": "...",
        "coins": ["BTC", "ETH"],
        "published_at": "2026-03-17T10:00:00Z"
      }
    ]
  },
  "tweets": {
    "success": true,
    "count": 5,
    "items": [
      {
        "author": "Vitalik Buterin",
        "handle": "VitalikButerin",
        "content": "...",
        "url": "https://...",
        "metrics": { "likes": 1000, "retweets": 200, "replies": 50 },
        "posted_at": "2026-03-17T09:00:00Z",
        "relevance": "high"
      }
    ]
  }
}

Common Workflows
Get All Categories
curl -s -X GET "https://ai.6551.io/open/free_categories"

Get Hot Crypto News
curl -s -X GET "https://ai.6551.io/open/free_hot?category=macro"

Get DeFi Subcategory News
curl -s -X GET "https://ai.6551.io/open/free_hot?category=macro&subcategory=defi"

Notes
No authentication required
Data is cached and updated periodically
If data is still being generated, a 503 response will be returned
Weekly Installs
449
Repository
6551team/daily-news
GitHub Stars
311
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn