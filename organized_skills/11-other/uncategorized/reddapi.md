---
rating: ⭐⭐⭐
title: reddapi
url: https://skills.sh/lignertys/reddit-research-skill/reddapi
---

# reddapi

skills/lignertys/reddit-research-skill/reddapi
reddapi
Installation
$ npx skills add https://github.com/lignertys/reddit-research-skill --skill reddapi
SKILL.md
reddapi.dev Skill
Overview

Access Reddit's complete data archive through reddapi.dev's powerful API. This skill provides semantic search, subreddit discovery, and trend analysis capabilities.

Key Advantage: This is a third-party service (not Reddit official), meaning:

✅ No rate limits - Unlimited QPS and request volume
✅ No time restrictions - 24/7 availability
✅ No daily/monthly quotas - Use as much as you need
✅ Full Reddit archive - Access historical and real-time discussions
Key Features
🔍 Semantic Search

Natural language search across millions of Reddit posts and comments.

# Search for user pain points
curl -X POST "https://reddapi.dev/api/v1/search/semantic" \
  -H "Authorization: Bearer $REDDAPI_API_KEY" \
  -d '{"query": "best productivity tools for remote teams", "limit": 100}'

# Find complaints and frustrations
curl -X POST "https://reddapi.dev/api/v1/search/semantic" \
  -H "Authorization: Bearer $REDDAPI_API_KEY" \
  -d '{"query": "frustrations with current TOOL_NAME", "limit": 100}'

📊 Trends API

Discover trending topics with engagement metrics.

# Get trending topics
curl "https://reddapi.dev/api/v1/trends" \
  -H "Authorization: Bearer $REDDAPI_API_KEY"


Response includes:

post_count: Number of posts
total_upvotes: Engagement score
avg_sentiment: Sentiment analysis (-1 to 1)
trending_keywords: Top keywords
growth_rate: Trend momentum
📝 Subreddit Discovery
# List popular subreddits
curl "https://reddapi.dev/api/subreddits?limit=100" \
  -H "Authorization: Bearer $REDDAPI_API_KEY"

# Get specific subreddit info
curl "https://reddapi.dev/api/subreddits/programming" \
  -H "Authorization: Bearer $REDDAPI_API_KEY"

Use Cases
Market Research
# Analyze competitor discussions
curl -X POST "https://reddapi.dev/api/v1/search/semantic" \
  -H "Authorization: Bearer $REDDAPI_API_KEY" \
  -d '{"query": "COMPETITOR problems complaints", "limit": 200}'

Niche Discovery
# Find underserved user needs
curl -X POST "https://reddapi.dev/api/v1/search/semantic" \
  -H "Authorization: Bearer $REDDAPI_API_KEY" \
  -d '{"query": "I wish there was an app that", "limit": 100}'

Trend Analysis
# Monitor topic growth
curl "https://reddapi.dev/api/v1/trends" \
  -H "Authorization: Bearer $REDDAPI_API_KEY" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for trend in data.get('data', {}).get('trends', []):
    print(f\"{trend['topic']}: {trend['growth_rate']}% growth\")
"

Response Format
Search Results
{
  "success": true,
  "results": [
    {
      "id": "post123",
      "title": "User post title",
      "selftext": "Post content...",
      "subreddit": "r/somesub",
      "score": 1234,
      "num_comments": 89,
      "created_utc": "2024-01-15T10:30:00Z"
    }
  ],
  "total": 15000
}

Trends Response
{
  "success": true,
  "data": {
    "trends": [
      {
        "topic": "AI regulation",
        "post_count": 1247,
        "total_upvotes": 45632,
        "avg_sentiment": 0.42,
        "growth_rate": 245.3
      }
    ]
  }
}

Environment Variables
export REDDAPI_API_KEY="your_api_key"


Get your API key at: https://reddapi.dev

Related Skills
niche-hunter: Automated opportunity discovery
market-analysis: Comprehensive research workflows
Weekly Installs
1.1K
Repository
lignertys/reddi…ch-skill
GitHub Stars
1
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn