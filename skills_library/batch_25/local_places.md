---
title: local-places
url: https://skills.sh/insight68/skills/local-places
---

# local-places

skills/insight68/skills/local-places
local-places
Installation
$ npx skills add https://github.com/insight68/skills --skill local-places
SKILL.md
📍 Local Places

Find places, Go fast

Search for nearby places using a local Google Places API proxy. Two-step flow: resolve location first, then search.

Setup
cd {baseDir}
echo "GOOGLE_PLACES_API_KEY=your-key" > .env
uv venv && uv pip install -e ".[dev]"
uv run --env-file .env uvicorn local_places.main:app --host 127.0.0.1 --port 8000


Requires GOOGLE_PLACES_API_KEY in .env or environment.

Quick Start

Check server: curl http://127.0.0.1:8000/ping

Resolve location:

curl -X POST http://127.0.0.1:8000/locations/resolve \
  -H "Content-Type: application/json" \
  -d '{"location_text": "Soho, London", "limit": 5}'

Search places:
curl -X POST http://127.0.0.1:8000/places/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "coffee shop",
    "location_bias": {"lat": 51.5137, "lng": -0.1366, "radius_m": 1000},
    "filters": {"open_now": true, "min_rating": 4.0},
    "limit": 10
  }'

Get details:
curl http://127.0.0.1:8000/places/{place_id}

Conversation Flow
If user says "near me" or gives vague location → resolve it first
If multiple results → show numbered list, ask user to pick
Ask for preferences: type, open now, rating, price level
Search with location_bias from chosen location
Present results with name, rating, address, open status
Offer to fetch details or refine search
Filter Constraints
filters.types: exactly ONE type (e.g., "restaurant", "cafe", "gym")
filters.price_levels: integers 0-4 (0=free, 4=very expensive)
filters.min_rating: 0-5 in 0.5 increments
filters.open_now: boolean
limit: 1-20 for search, 1-10 for resolve
location_bias.radius_m: must be > 0
Response Format
{
  "results": [
    {
      "place_id": "ChIJ...",
      "name": "Coffee Shop",
      "address": "123 Main St",
      "location": { "lat": 51.5, "lng": -0.1 },
      "rating": 4.6,
      "price_level": 2,
      "types": ["cafe", "food"],
      "open_now": true
    }
  ],
  "next_page_token": "..."
}


Use next_page_token as page_token in next request for more results.

Weekly Installs
10
Repository
insight68/skills
GitHub Stars
4
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn