---
rating: ⭐⭐⭐
title: feishu-calendar-advanced
url: https://skills.sh/site/skills.volces.com/feishu-calendar-advanced
---

# feishu-calendar-advanced

skills/skills.volces.com/feishu-calendar-advanced
feishu-calendar-advanced
$ npx skills add https://skills.volces.com/skills/clawhub/boyd4y@feishu-calendar-advanced
SKILL.md
Feishu Calendar Advanced

Manage your Feishu (Lark) calendar using the feishu-agent CLI tool.

Dependencies
Dependency	Required	Description
bun	Yes	Bun runtime (for running bunx commands)
@teamclaw/feishu-agent	Yes	Installed automatically via bunx
Check Dependencies
# Check bun availability
bun --version

Setup
First Time Setup
Install and configure feishu-agent:
# Interactive setup wizard (recommended)
bunx @teamclaw/feishu-agent setup

# Or manual configuration
bunx @teamclaw/feishu-agent config set appId <your_app_id>
bunx @teamclaw/feishu-agent config set appSecret <your_app_secret>

OAuth Authorization:
bunx @teamclaw/feishu-agent auth

Verify setup:
bunx @teamclaw/feishu-agent whoami

Usage
/feishu-calendar-advanced [command] [options]

Commands
Command	Description
calendars	List all calendars (primary, subscribed)
events	List events in primary calendar
create --summary "Meeting" --start "2026-03-05 14:00" --end "2026-03-05 15:00"	Create a new event
create --summary "Meeting" --start "..." --end "..." --attendee user_id	Create event with attendees
delete --event-id <event_id>	Delete an event by ID
Options
Option	Description
--summary	Event title/summary (required for create)
--start	Start time in format "YYYY-MM-DD HH:MM" (required for create)
--end	End time in format "YYYY-MM-DD HH:MM" (required for create)
--attendee	Add attendee by user_id (can be used multiple times)
--event-id	Event ID (required for delete)
Examples
# List all calendars
/feishu-calendar-advanced calendars

# List events in primary calendar
/feishu-calendar-advanced events

# Create a simple event
/feishu-calendar-advanced create --summary "Team Standup" --start "2026-03-05 10:00" --end "2026-03-05 10:30"

# Create event with attendees
/feishu-calendar-advanced create --summary "Project Review" --start "2026-03-05 14:00" --end "2026-03-05 15:00" --attendee user_id_1 --attendee user_id_2

# Delete an event
/feishu-calendar-advanced delete --event-id evt_xxxxxxxxxxxxx

Troubleshooting

"User authorization required"

Run bunx @teamclaw/feishu-agent auth to authorize

"Token expired"

Run bunx @teamclaw/feishu-agent auth again to refresh

"Time conflict detected"

The requested time slot is already busy
Choose a different time or check your calendar with bunx @teamclaw/feishu-agent calendar events

"Permission denied"

Check app permissions in Feishu Developer Console
Required: calendar:calendar, calendar:event
Weekly Installs
111
Source
skills.volces.c…advanced
First Seen
Mar 12, 2026