---
title: weather
url: https://skills.sh/hkuds/nanobot/weather
---

# weather

skills/hkuds/nanobot/weather
weather
Installation
$ npx skills add https://github.com/hkuds/nanobot --skill weather
SKILL.md
Weather

Two free services, no API keys needed.

wttr.in (primary)

Quick one-liner:

curl -s "wttr.in/London?format=3"
# Output: London: ⛅️ +8°C


Compact format:

curl -s "wttr.in/London?format=%l:+%c+%t+%h+%w"
# Output: London: ⛅️ +8°C 71% ↙5km/h


Full forecast:

curl -s "wttr.in/London?T"


Format codes: %c condition · %t temp · %h humidity · %w wind · %l location · %m moon

Tips:

URL-encode spaces: wttr.in/New+York
Airport codes: wttr.in/JFK
Units: ?m (metric) ?u (USCS)
Today only: ?1 · Current only: ?0
PNG: curl -s "wttr.in/Berlin.png" -o /tmp/weather.png
Open-Meteo (fallback, JSON)

Free, no key, good for programmatic use:

curl -s "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"


Find coordinates for a city, then query. Returns JSON with temp, windspeed, weathercode.

Docs: https://open-meteo.com/en/docs

Weekly Installs
16
Repository
hkuds/nanobot
GitHub Stars
40.5K
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass