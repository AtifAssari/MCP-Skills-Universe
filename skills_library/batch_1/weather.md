---
title: weather
url: https://skills.sh/steipete/clawdis/weather
---

# weather

skills/steipete/clawdis/weather
weather
Installation
$ npx skills add https://github.com/steipete/clawdis --skill weather
Summary

Current weather and multi-day forecasts for any global location, no API key required.

Supports current conditions, 3-day forecasts, and week-long projections via wttr.in with customizable output formats
Includes one-liner summaries, detailed condition reports, JSON output, and PNG weather charts
Covers standard weather data: temperature, "feels like," wind, humidity, precipitation, and condition emojis
Works with city names, regions, and airport codes; rate-limited but requires no authentication
SKILL.md
Weather Skill

Get current weather conditions and forecasts.

When to Use

✅ USE this skill when:

"What's the weather?"
"Will it rain today/tomorrow?"
"Temperature in [city]"
"Weather forecast for the week"
Travel planning weather checks
When NOT to Use

❌ DON'T use this skill when:

Historical weather data → use weather archives/APIs
Climate analysis or trends → use specialized data sources
Hyper-local microclimate data → use local sensors
Severe weather alerts → check official NWS sources
Aviation/marine weather → use specialized services (METAR, etc.)
Location

Always include a city, region, or airport code in weather queries.

Commands
Current Weather
# One-line summary
curl "wttr.in/London?format=3"

# Detailed current conditions
curl "wttr.in/London?0"

# Specific city
curl "wttr.in/New+York?format=3"

Forecasts
# 3-day forecast
curl "wttr.in/London"

# Week forecast
curl "wttr.in/London?format=v2"

# Specific day (0=today, 1=tomorrow, 2=day after)
curl "wttr.in/London?1"

Format Options
# One-liner
curl "wttr.in/London?format=%l:+%c+%t+%w"

# JSON output
curl "wttr.in/London?format=j1"

# PNG image
curl "wttr.in/London.png"

Format Codes
%c — Weather condition emoji
%t — Temperature
%f — "Feels like"
%w — Wind
%h — Humidity
%p — Precipitation
%l — Location
Quick Responses

"What's the weather?"

curl -s "wttr.in/London?format=%l:+%c+%t+(feels+like+%f),+%w+wind,+%h+humidity"


"Will it rain?"

curl -s "wttr.in/London?format=%l:+%c+%p"


"Weekend forecast"

curl "wttr.in/London?format=v2"

Notes
No API key needed (uses wttr.in)
Rate limited; don't spam requests
Works for most global cities
Supports airport codes: curl wttr.in/ORD
Weekly Installs
3.9K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass