---
title: gws-calendar-agenda
url: https://skills.sh/googleworkspace/cli/gws-calendar-agenda
---

# gws-calendar-agenda

skills/googleworkspace/cli/gws-calendar-agenda
gws-calendar-agenda
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-calendar-agenda
Summary

Display upcoming events across all Google Calendars with flexible time range and filtering options.

Query events by preset ranges (today, tomorrow, week) or custom day count, with optional filtering by calendar name or ID
Respects your Google account timezone by default; override with IANA timezone flag for different regions
Read-only operation; never modifies events or calendar data
Requires gws binary and Google Calendar authentication via shared gws-shared skill
SKILL.md
calendar +agenda

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Show upcoming events across all calendars

Usage
gws calendar +agenda

Flags
Flag	Required	Default	Description
--today	—	—	Show today's events
--tomorrow	—	—	Show tomorrow's events
--week	—	—	Show this week's events
--days	—	—	Number of days ahead to show
--calendar	—	—	Filter to specific calendar name or ID
--timezone	—	—	IANA timezone override (e.g. America/Denver). Defaults to Google account timezone.
Examples
gws calendar +agenda
gws calendar +agenda --today
gws calendar +agenda --week --format table
gws calendar +agenda --days 3 --calendar 'Work'
gws calendar +agenda --today --timezone America/New_York

Tips
Read-only — never modifies events.
Queries all calendars by default; use --calendar to filter.
Uses your Google account timezone by default; override with --timezone.
See Also
gws-shared — Global flags and auth
gws-calendar — All manage calendars and events commands
Weekly Installs
19.1K
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