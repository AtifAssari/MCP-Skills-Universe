---
rating: ⭐⭐⭐
title: serpapi
url: https://skills.sh/vm0-ai/vm0-skills/serpapi
---

# serpapi

skills/vm0-ai/vm0-skills/serpapi
serpapi
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill serpapi
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name SERPAPI_TOKEN or zero doctor check-connector --url https://serpapi.com/search --method GET

How to Use

All examples below assume you have SERPAPI_TOKEN set.

Base URL: https://serpapi.com/search

1. Basic Google Search

Search Google and get structured JSON results:

curl -s "https://serpapi.com/search?engine=google&q=artificial+intelligence&api_key=$SERPAPI_TOKEN" | jq '.organic_results[:3] | .[] | {title, link, snippet}'

2. Search with Location

Search from a specific location:

curl -s "https://serpapi.com/search?engine=google&q=best+coffee+shops&location=San+Francisco,+California&gl=us&hl=en&api_key=$SERPAPI_TOKEN" | jq '.organic_results[:3]'


Parameters:

location: City, state, or address
gl: Country code (us, uk, de, etc.)
hl: Language code (en, de, fr, etc.)
3. Google Image Search

Search for images:

curl -s "https://serpapi.com/search?engine=google_images&q=sunset+beach&api_key=$SERPAPI_TOKEN" | jq '.images_results[:3] | .[] | {title, original, thumbnail}'

4. Google News Search

Search news articles:

curl -s "https://serpapi.com/search?engine=google_news&q=technology&api_key=$SERPAPI_TOKEN" | jq '.news_results[:3] | .[] | {title, link, source, date}'

5. Google Shopping Search

Search products:

curl -s "https://serpapi.com/search?engine=google_shopping&q=wireless+headphones&api_key=$SERPAPI_TOKEN" | jq '.shopping_results[:3] | .[] | {title, price, source}'

6. YouTube Search

Search YouTube videos:

curl -s "https://serpapi.com/search?engine=youtube&search_query=python+tutorial&api_key=$SERPAPI_TOKEN" | jq '.video_results[:3] | .[] | {title, link, channel, views}'

7. Google Maps / Local Results

Search local businesses:

curl -s "https://serpapi.com/search?engine=google_maps&q=restaurants&ll=@40.7128,-74.0060,15z&api_key=$SERPAPI_TOKEN" | jq '.local_results[:3] | .[] | {title, rating, address}'


If using location with Google Maps, include z or m:

curl -s "https://serpapi.com/search?engine=google_maps&q=3PL&location=Dallas-Fort+Worth,+Texas&z=14&api_key=$SERPAPI_TOKEN"


Defensive local-results extraction:

curl -s "https://serpapi.com/search?engine=google_maps&q=3PL&ll=@32.7767,-96.7970,14z&api_key=$SERPAPI_TOKEN" \
  | jq 'if has("error") then .error else (.local_results[:5] | map({title,address,phone,website,link,type})) end'


Parameters:

ll: Latitude, longitude, and zoom level (e.g., @40.7128,-74.0060,15z)
8. Pagination

Get more results using the start parameter:

# First page (results 1-10)
curl -s "https://serpapi.com/search?engine=google&q=machine+learning&start=0&api_key=$SERPAPI_TOKEN" | jq '.organic_results | length'

# Second page (results 11-20)
curl -s "https://serpapi.com/search?engine=google&q=machine+learning&start=10&api_key=$SERPAPI_TOKEN" | jq '.organic_results | length'

9. Check Account Info

Check your API usage and credits:

curl -s "https://serpapi.com/account?api_key=$SERPAPI_TOKEN" | jq '{plan_name, searches_per_month, this_month_usage}'

Supported Engines
Engine	Parameter	Description
Google Search	engine=google	Web search results
Google Images	engine=google_images	Image search
Google News	engine=google_news	News articles
Google Shopping	engine=google_shopping	Product search
Google Maps	engine=google_maps	Local businesses
YouTube	engine=youtube	Video search
Bing	engine=bing	Bing web search
DuckDuckGo	engine=duckduckgo	Privacy-focused search
Common Parameters
Parameter	Description
q	Search query (required)
engine	Search engine to use
location	Geographic location for search
gl	Country code (e.g., us, uk)
hl	Language code (e.g., en, de)
start	Pagination offset (0, 10, 20...)
num	Number of results (max 100)
safe	Safe search (active or off)
device	Device type (desktop, mobile, tablet)
Guidelines
Use specific engines: Use google_images, google_news etc. instead of tbm parameter for cleaner results
Add location for local searches: Use location and gl for geo-targeted results
Cache results: SerpApi caches results by default; use no_cache=true for fresh data
Monitor usage: Check /account endpoint to track API credits
Use jq filters: Filter large JSON responses to extract only needed data
Weekly Installs
275
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn