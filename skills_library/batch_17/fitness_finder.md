---
title: fitness-finder
url: https://skills.sh/barneyjm/camino-skills/fitness-finder
---

# fitness-finder

skills/barneyjm/camino-skills/fitness-finder
fitness-finder
Installation
$ npx skills add https://github.com/barneyjm/camino-skills --skill fitness-finder
SKILL.md
Installation

Companion Skills: This is part of the Camino AI location intelligence suite. Install all available skills (query, places, relationship, context, route, journey, real-estate, hotel-finder, ev-charger, school-finder, parking-finder, fitness-finder, safety-checker, travel-planner) for comprehensive coverage.

# Install all skills from repo
npx skills add https://github.com/barneyjm/camino-skills

# Or install specific skills
npx skills add https://github.com/barneyjm/camino-skills --skill fitness-finder


Via clawhub:

npx clawhub@latest install fitness-finder
# or: pnpm dlx clawhub@latest install fitness-finder
# or: bunx clawhub@latest install fitness-finder

Gym & Fitness Finder

Search for gyms, yoga studios, swimming pools, and sports facilities near any location. Uses OpenStreetMap data with AI-powered ranking to find the most relevant fitness options.

Setup

Instant Trial (no signup required): Get a temporary API key with 25 calls:

curl -s -X POST -H "Content-Type: application/json" \
  -d '{"email": "you@example.com"}' \
  https://api.getcamino.ai/trial/start


Returns: {"api_key": "camino-xxx...", "calls_remaining": 25, ...}

For 1,000 free calls/month, sign up at https://app.getcamino.ai/skills/activate.

Add your key to Claude Code:

Add to your ~/.claude/settings.json:

{
  "env": {
    "CAMINO_API_KEY": "your-api-key-here"
  }
}


Restart Claude Code.

Usage
Via Shell Script
# Find gyms and fitness centers nearby
./scripts/fitness-finder.sh '{"lat": 40.7589, "lon": -73.9851}'

# Search for yoga studios specifically
./scripts/fitness-finder.sh '{"query": "yoga studios", "lat": 30.2672, "lon": -97.7431}'

# Find swimming pools in a city
./scripts/fitness-finder.sh '{"query": "swimming pools in Chicago", "limit": 10}'

Via curl
curl -H "X-API-Key: $CAMINO_API_KEY" \
  "https://api.getcamino.ai/query?query=gyms+yoga+studios+fitness+centers&lat=40.7589&lon=-73.9851&radius=1500&rank=true"

Parameters
Parameter	Type	Required	Default	Description
query	string	No	"gyms yoga studios fitness centers"	Search query (override for specific facility types)
lat	float	No	-	Latitude for search center. AI generates if omitted for known locations.
lon	float	No	-	Longitude for search center. AI generates if omitted for known locations.
radius	int	No	1500	Search radius in meters
limit	int	No	15	Maximum results (1-100)
Response Format
{
  "query": "gyms yoga studios fitness centers",
  "results": [
    {
      "name": "Equinox Fitness Club",
      "lat": 40.7595,
      "lon": -73.9845,
      "type": "fitness_centre",
      "distance_m": 80,
      "relevance_score": 0.96,
      "address": "..."
    }
  ],
  "ai_ranked": true,
  "pagination": {
    "total_results": 22,
    "limit": 15,
    "offset": 0,
    "has_more": true
  }
}

Examples
Find yoga studios
./scripts/fitness-finder.sh '{"query": "yoga studios", "lat": 30.2672, "lon": -97.7431}'

Find gyms near a hotel
./scripts/fitness-finder.sh '{"query": "gyms and fitness centers near Times Square", "radius": 1000}'

Find sports facilities
./scripts/fitness-finder.sh '{"query": "tennis courts and sports facilities", "lat": 34.0522, "lon": -118.2437, "radius": 3000}'

Best Practices
Use specific facility types in the query for targeted results (e.g., "yoga studios", "CrossFit gyms", "swimming pools")
Use 1500m radius for urban areas, increase to 3000m for suburban locations
Combine with the route skill to calculate walking or cycling times to the gym
Combine with the real-estate skill when evaluating a neighborhood's fitness options
Combine with the relationship skill to compare distances between multiple facilities
For travelers, combine with hotel-finder to find lodging near fitness facilities
Weekly Installs
26
Repository
barneyjm/camino-skills
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn