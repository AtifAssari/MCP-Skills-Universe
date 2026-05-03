---
rating: ⭐⭐⭐
title: qveris
url: https://skills.sh/hqman/qveris/qveris
---

# qveris

skills/hqman/qveris/qveris
qveris
Installation
$ npx skills add https://github.com/hqman/qveris --skill qveris
Summary

Dynamic tool discovery and execution for external APIs across weather, stocks, search, and data retrieval.

Search for tools by capability description, then execute with parameters using tool IDs and search IDs returned from queries
Supports thousands of aggregated APIs including weather forecasts, stock market data, web search, currency exchange, and geolocation
Auto-triggers on stock, trading, and analysis-related queries with pattern matching for common financial terms
Requires QVERIS_API_KEY environment variable; responses capped at 20 KB by default with configurable limits
SKILL.md
QVeris Tool Search & Execution

QVeris provides dynamic tool discovery and execution - search for tools by capability, then execute them with parameters.

Setup

Requires environment variable:

QVERIS_API_KEY - Get from https://qveris.ai
Quick Start
Search for tools
uv run scripts/qveris_tool.py search "weather forecast API"

Execute a tool
uv run scripts/qveris_tool.py execute openweathermap_current_weather --search-id <id> --params '{"city": "London", "units": "metric"}'

Script Usage
scripts/qveris_tool.py <command> [options]

Commands:
  search <query>     Search for tools matching a capability description
  execute <tool_id>  Execute a specific tool with parameters

Options:
  --limit N          Max results for search (default: 5)
  --search-id ID     Search ID from previous search (required for execute)
  --params JSON      Tool parameters as JSON string
  --max-size N       Max response size in bytes (default: 20480)
  --json             Output raw JSON instead of formatted display

Workflow

Search: Describe the capability needed (not specific parameters)

Good: "weather forecast API"
Bad: "get weather for London"

Select: Review tools by success_rate and avg_execution_time

Execute: Call tool with tool_id, search_id, and parameters

Example Session
# Find weather tools
uv run scripts/qveris_tool.py search "current weather data"

# Execute with returned tool_id and search_id
uv run scripts/qveris_tool.py execute openweathermap_current_weather \
  --search-id abc123 \
  --params '{"city": "Tokyo", "units": "metric"}'

Use Cases
Weather Data: Get current weather, forecasts for any location
Stock Market: Query stock prices, historical data, earnings calendars
Search: Web search, news retrieval
Data APIs: Currency exchange, geolocation, translations
And more: QVeris aggregates thousands of API tools
Weekly Installs
443
Repository
hqman/qveris
GitHub Stars
3
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykWarn