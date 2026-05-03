---
rating: ⭐⭐⭐
title: flightclaw
url: https://skills.sh/jackculpan/flightclaw/flightclaw
---

# flightclaw

skills/jackculpan/flightclaw/flightclaw
flightclaw
Installation
$ npx skills add https://github.com/jackculpan/flightclaw --skill flightclaw
Summary

Search, monitor, and get alerts for flight price changes across Google Flights.

Search flights by route, date range, and cabin class with filtering options for stops, airlines, duration, and departure/arrival times
Track routes over time with optional target price alerts that trigger when prices drop below a threshold
Scheduled price checking compares current prices against historical data and reports percentage drops
Runs as both a command-line tool and MCP server, with automatic currency detection based on user location
Price history persists locally in JSON format with R2 backup support
SKILL.md
flightclaw

Track flight prices from Google Flights. Search routes, monitor prices over time, and get alerts when prices drop.

Install
npx skills add jackculpan/flightclaw


Or manually:

bash skills/flightclaw/setup.sh

Scripts
Search Flights

Find flights for a specific route and date. Supports multiple airports and date ranges.

python skills/flightclaw/scripts/search-flights.py LHR JFK 2025-07-01
python skills/flightclaw/scripts/search-flights.py LHR JFK 2025-07-01 --cabin BUSINESS
python skills/flightclaw/scripts/search-flights.py LHR JFK 2025-07-01 --return-date 2025-07-08
python skills/flightclaw/scripts/search-flights.py LHR JFK 2025-07-01 --stops NON_STOP --results 10
# Multiple airports (searches all combinations)
python skills/flightclaw/scripts/search-flights.py LHR,MAN JFK,EWR 2025-07-01
# Date range (searches each day)
python skills/flightclaw/scripts/search-flights.py LHR JFK 2025-07-01 --date-to 2025-07-05
# Both
python skills/flightclaw/scripts/search-flights.py LHR,MAN JFK,EWR 2025-07-01 --date-to 2025-07-03


Arguments:

origin - IATA airport code(s), comma-separated (e.g. LHR or LHR,MAN)
destination - IATA airport code(s), comma-separated (e.g. JFK or JFK,EWR)
date - Departure date (YYYY-MM-DD)
--date-to - End of date range (YYYY-MM-DD). Searches each day from date to date-to inclusive.
--return-date - Return date for round trips (YYYY-MM-DD)
--cabin - ECONOMY (default), PREMIUM_ECONOMY, BUSINESS, FIRST
--stops - ANY (default), NON_STOP, ONE_STOP, TWO_STOPS
--results - Number of results (default: 5)
Track a Flight

Add a route to the price tracking list and record the current price. Supports multiple airports and date ranges (creates a separate tracking entry for each combination).

python skills/flightclaw/scripts/track-flight.py LHR JFK 2025-07-01
python skills/flightclaw/scripts/track-flight.py LHR JFK 2025-07-01 --target-price 400
python skills/flightclaw/scripts/track-flight.py LHR JFK 2025-07-01 --return-date 2025-07-08 --cabin BUSINESS
# Track multiple airports and dates
python skills/flightclaw/scripts/track-flight.py LHR,MAN JFK,EWR 2025-07-01 --date-to 2025-07-03 --target-price 400


Arguments:

Same as search-flights, plus:
--target-price - Alert when price drops below this amount
Check Prices

Check all tracked flights for price changes. Designed to run on a schedule (cron).

python skills/flightclaw/scripts/check-prices.py
python skills/flightclaw/scripts/check-prices.py --threshold 5


Arguments:

--threshold - Percentage drop to trigger alert (default: 10)

Output: Reports price changes for tracked flights. Highlights drops and alerts when target prices are reached.

List Tracked Flights

Show all flights being tracked with current vs original prices.

python skills/flightclaw/scripts/list-tracked.py

MCP Server

FlightClaw also runs as an MCP server with extended search capabilities:

pip install flights "mcp[cli]"
claude mcp add flightclaw -- python3 server.py


MCP tools: search_flights, search_dates, track_flight, check_prices, list_tracked, remove_tracked

Additional MCP filters: passengers (adults/children/infants), airline filter, price limit, max flight duration, departure/arrival time restrictions, layover duration, sort order, and cheapest-date calendar search.

Currency

Prices are returned in the user's local currency based on their IP location. The currency is auto-detected from the Google Flights API response and displayed with the correct symbol (e.g. $, £, ฿, €). Tracked flights store the currency code in tracked.json.

Data

Price history is stored in skills/flightclaw/data/tracked.json and persists via R2 backup.

Weekly Installs
803
Repository
jackculpan/flightclaw
GitHub Stars
51
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn