---
rating: ⭐⭐
title: gws-calendar-insert
url: https://skills.sh/googleworkspace/cli/gws-calendar-insert
---

# gws-calendar-insert

skills/googleworkspace/cli/gws-calendar-insert
gws-calendar-insert
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-calendar-insert
Summary

Create a new Google Calendar event with customizable details and optional attendees.

Requires three core flags: event summary, start time, and end time in ISO 8601 format
Supports optional location, description, multiple attendees, and automatic Google Meet link generation
Defaults to the primary calendar but accepts a custom calendar ID via the --calendar flag
Write operation that should be confirmed with the user before execution
SKILL.md
calendar +insert

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

create a new event

Usage
gws calendar +insert --summary <TEXT> --start <TIME> --end <TIME>

Flags
Flag	Required	Default	Description
--calendar	—	primary	Calendar ID (default: primary)
--summary	✓	—	Event summary/title
--start	✓	—	Start time (ISO 8601, e.g., 2024-01-01T10:00:00Z)
--end	✓	—	End time (ISO 8601)
--location	—	—	Event location
--description	—	—	Event description/body
--attendee	—	—	Attendee email (can be used multiple times)
--meet	—	—	Add a Google Meet video conference link
Examples
gws calendar +insert --summary 'Standup' --start '2026-06-17T09:00:00-07:00' --end '2026-06-17T09:30:00-07:00'
gws calendar +insert --summary 'Review' --start ... --end ... --attendee alice@example.com
gws calendar +insert --summary 'Meet' --start ... --end ... --meet

Tips
Use RFC3339 format for times (e.g. 2026-06-17T09:00:00-07:00).
The --meet flag automatically adds a Google Meet link to the event.

[!CAUTION] This is a write command — confirm with the user before executing.

See Also
gws-shared — Global flags and auth
gws-calendar — All manage calendars and events commands
Weekly Installs
18.3K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass