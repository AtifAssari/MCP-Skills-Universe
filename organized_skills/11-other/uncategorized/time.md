---
rating: ⭐⭐⭐
title: time
url: https://skills.sh/dianel555/dskills/time
---

# time

skills/dianel555/dskills/time
time
Installation
$ npx skills add https://github.com/dianel555/dskills --skill time
SKILL.md
Time

Time and timezone conversion utilities. Standalone CLI only (no MCP dependency).

Execution Methods

Run scripts/time_cli.py via Bash:

# Prerequisites: pip install pytz (or use Python 3.9+ with zoneinfo)

# Get current time in a timezone
python scripts/time_cli.py get --timezone "Asia/Shanghai"
python scripts/time_cli.py get --timezone "America/New_York"
python scripts/time_cli.py get  # Uses system timezone

# Convert time between timezones
python scripts/time_cli.py convert \
  --time "16:30" \
  --from "America/New_York" \
  --to "Asia/Tokyo"

# List available timezones
python scripts/time_cli.py list [--filter "Asia"]

Tool Capability Matrix
Tool	Parameters	Output
get_current_time	timezone (required, IANA name)	{timezone, datetime, is_dst}
convert_time	source_timezone, time (HH:MM), target_timezone	{source, target, time_difference}
Common IANA Timezone Names
Region	Timezone
China	Asia/Shanghai
Japan	Asia/Tokyo
Korea	Asia/Seoul
US East	America/New_York
US West	America/Los_Angeles
UK	Europe/London
Germany	Europe/Berlin
France	Europe/Paris
Australia	Australia/Sydney
UTC	UTC
Workflow
Getting Current Time
Identify target timezone (use IANA name)
Call get_current_time with timezone parameter
Response includes ISO 8601 datetime and DST status
Converting Time
Identify source timezone and time (24-hour format HH:MM)
Identify target timezone
Call convert_time with all parameters
Response includes both times and time difference
Output Format
get_current_time Response
{
  "timezone": "Asia/Shanghai",
  "datetime": "2024-01-01T21:00:00+08:00",
  "is_dst": false
}

convert_time Response
{
  "source": {
    "timezone": "America/New_York",
    "datetime": "2024-01-01T16:30:00-05:00",
    "is_dst": false
  },
  "target": {
    "timezone": "Asia/Tokyo",
    "datetime": "2024-01-02T06:30:00+09:00",
    "is_dst": false
  },
  "time_difference": "+14.0h"
}

Error Handling
Error	Recovery
Invalid timezone	Check IANA timezone name spelling
Invalid time format	Use 24-hour format HH:MM
MCP unavailable	Fall back to CLI script
Anti-Patterns
Prohibited	Correct
Use city names directly	Use IANA timezone names (e.g., Asia/Tokyo not Tokyo)
Use 12-hour format	Use 24-hour format (e.g., 16:30 not 4:30 PM)
Assume timezone	Always specify timezone explicitly
Weekly Installs
8
Repository
dianel555/dskills
GitHub Stars
64
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass