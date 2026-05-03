---
title: weather-fetcher
url: https://skills.sh/shanraisshan/claude-code-best-practice/weather-fetcher
---

# weather-fetcher

skills/shanraisshan/claude-code-best-practice/weather-fetcher
weather-fetcher
Installation
$ npx skills add https://github.com/shanraisshan/claude-code-best-practice --skill weather-fetcher
SKILL.md
Weather Fetcher Skill

This skill provides instructions for fetching current weather data.

Task

Fetch the current temperature for Dubai, UAE in the requested unit (Celsius or Fahrenheit).

Instructions

Fetch Weather Data: Use the WebFetch tool to get current weather data for Dubai from the Open-Meteo API.

For Celsius:

URL: https://api.open-meteo.com/v1/forecast?latitude=25.2048&longitude=55.2708&current=temperature_2m&temperature_unit=celsius

For Fahrenheit:

URL: https://api.open-meteo.com/v1/forecast?latitude=25.2048&longitude=55.2708&current=temperature_2m&temperature_unit=fahrenheit

Extract Temperature: From the JSON response, extract the current temperature:

Field: current.temperature_2m
Unit label is in: current_units.temperature_2m

Return Result: Return the temperature value and unit clearly.

Expected Output

After completing this skill's instructions:

Current Dubai Temperature: [X]°[C/F]
Unit: [Celsius/Fahrenheit]

Notes
Only fetch the temperature, do not perform any transformations or write any files
Open-Meteo is free, requires no API key, and uses coordinate-based lookups for reliability
Dubai coordinates: latitude 25.2048, longitude 55.2708
Return the numeric temperature value and unit clearly
Support both Celsius and Fahrenheit based on the caller's request
Weekly Installs
115
Repository
shanraisshan/cl…practice
GitHub Stars
50.1K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass