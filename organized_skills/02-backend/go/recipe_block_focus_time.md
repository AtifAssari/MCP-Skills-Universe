---
rating: ⭐⭐
title: recipe-block-focus-time
url: https://skills.sh/googleworkspace/cli/recipe-block-focus-time
---

# recipe-block-focus-time

skills/googleworkspace/cli/recipe-block-focus-time
recipe-block-focus-time
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-block-focus-time
Summary

Recurring focus time blocks on Google Calendar to protect deep work hours.

Creates weekly recurring focus blocks (Monday–Friday by default) that display as busy time, preventing calendar conflicts
Requires the gws-calendar skill and uses Google Calendar's recurrence rules for flexible scheduling
Includes verification step to confirm blocks appear correctly in calendar agenda view
SKILL.md
Block Focus Time on Google Calendar

PREREQUISITE: Load the following skills to execute this recipe: gws-calendar

Create recurring focus time blocks on Google Calendar to protect deep work hours.

Steps
Create recurring focus block: gws calendar events insert --params '{"calendarId": "primary"}' --json '{"summary": "Focus Time", "description": "Protected deep work block", "start": {"dateTime": "2025-01-20T09:00:00", "timeZone": "America/New_York"}, "end": {"dateTime": "2025-01-20T11:00:00", "timeZone": "America/New_York"}, "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"], "transparency": "opaque"}'
Verify it shows as busy: gws calendar +agenda
Weekly Installs
11.3K
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