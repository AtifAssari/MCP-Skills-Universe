---
title: brave-search
url: https://skills.sh/vm0-ai/vm0-skills/brave-search
---

# brave-search

skills/vm0-ai/vm0-skills/brave-search
brave-search
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill brave-search
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name BRAVE_API_KEY or zero doctor check-connector --url https://api.search.brave.com/res/v1/web/search --method GET

How to Use

All examples below assume you have BRAVE_API_KEY set.

The base URL for the API is:

https://api.search.brave.com/res/v1

Authentication uses the X-Subscription-Token header.

1. Basic Web Search

Search the web with a query:

curl -s "https://api.search.brave.com/res/v1/web/search?q=artificial+intelligence" -H "Accept: application/json" -H "X-Subscription-Token: $BRAVE_API_KEY" | jq '.web.results[:3] | .[] | {title, url, description}

2. Web Search with Parameters

Customize search with country, language, and result count:

Write to /tmp/brave_query.txt:

best restaurants

curl -s "https://api.search.brave.com/res/v1/web/search" -H "Accept: application/json" -H "X-Subscription-Token: $BRAVE_API_KEY" -G --data-urlencode "q@/tmp/brave_query.txt" -d "country=us" -d "search_lang=en" -d "count=5" | jq '.web.results[] | {title, url}'


Parameters:

q: Search query (required, max 400 chars / 50 words)
country: Two-letter country code (e.g., us, gb, jp)
search_lang: Language code (e.g., en, zh, ja)
count: Results per page (1-20, default: 10)
offset: Pagination offset (0-9, default: 0)
3. Safe Search Filter

Control explicit content filtering:

Write to /tmp/brave_query.txt:

programming tutorials

curl -s "https://api.search.brave.com/res/v1/web/search" -H "Accept: application/json" -H "X-Subscription-Token: $BRAVE_API_KEY" -G --data-urlencode "q@/tmp/brave_query.txt" -d "safesearch=strict" | jq '.web.results[:3] | .[] | {title, url}


Options: off, strict (Note: Image/Video search only supports off and strict)

4. Freshness Filter

Filter results by time:

Write to /tmp/brave_query.txt:

tech news

curl -s "https://api.search.brave.com/res/v1/web/search" -H "Accept: application/json" -H "X-Subscription-Token: $BRAVE_API_KEY" -G --data-urlencode "q@/tmp/brave_query.txt" -d "freshness=pd" | jq '.web.results[:3] | .[] | {title, url, age}


Options:

pd: Past day (24 hours)
pw: Past week
pm: Past month
py: Past year
YYYY-MM-DDtoYYYY-MM-DD: Custom date range
5. Image Search

Search for images:

Write to /tmp/brave_query.txt:

sunset beach

curl -s "https://api.search.brave.com/res/v1/images/search" -H "Accept: application/json" -H "X-Subscription-Token: $BRAVE_API_KEY" -G --data-urlencode "q@/tmp/brave_query.txt" -d "count=5" -d "safesearch=strict" | jq '.results[] | {title, url: .properties.url, thumbnail: .thumbnail.src}


Image search supports up to 200 results per request.

6. Video Search

Search for videos:

Write to /tmp/brave_query.txt:

learn python

curl -s "https://api.search.brave.com/res/v1/videos/search" -H "Accept: application/json" -H "X-Subscription-Token: $BRAVE_API_KEY" -G --data-urlencode "q@/tmp/brave_query.txt" -d "count=5" | jq '.results[] | {title, url, duration}


Video search supports up to 50 results per request.

7. News Search

Search for recent news articles:

Write to /tmp/brave_query.txt:

technology

curl -s "https://api.search.brave.com/res/v1/news/search" -H "Accept: application/json" -H "X-Subscription-Token: $BRAVE_API_KEY" -G --data-urlencode "q@/tmp/brave_query.txt" -d "count=3" | jq '.results[:3] | .[] | {title, url, age}


News search defaults to past day (pd) freshness.

8. Pagination

Get more results with offset:

Write to /tmp/brave_query.txt:

machine learning

curl -s "https://api.search.brave.com/res/v1/web/search" -H "Accept: application/json" -H "X-Subscription-Token: $BRAVE_API_KEY" -G --data-urlencode "q@/tmp/brave_query.txt" -d "count=10" -d "offset=1" | jq '.web.results[] | {title, url}


offset=1 skips the first page of results.

9. Get Raw JSON Response

View the full response structure:

curl -s "https://api.search.brave.com/res/v1/web/search?q=test" -H "Accept: application/json" -H "X-Subscription-Token: $BRAVE_API_KEY" | jq 'keys'


Response includes: query, mixed, type, web, videos, news, etc.

Response Structure
Web Search Response
{
  "query": { "original": "search term" },
  "web": {
  "results": [
  {
  "title": "Page Title",
  "url": "https://example.com",
  "description": "Page description...",
  "age": "2 days ago"
  }
  ]
  }
}

Image Search Response
{
  "results": [
  {
  "title": "Image Title",
  "properties": { "url": "https://..." },
  "thumbnail": { "src": "https://..." }
  }
  ]
}

Guidelines
URL encode queries: Use --data-urlencode for special characters
Respect rate limits: Free tier is 1 query/second
Use freshness for news: Time-sensitive searches benefit from pd or pw
Pagination limit: Maximum offset is 9 (100 results total with count=10)
Pro plan for local: Local business search requires Pro subscription
No tracking: Brave doesn't track users or store search history
Weekly Installs
79
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn