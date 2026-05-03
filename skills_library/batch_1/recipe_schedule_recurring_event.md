---
title: recipe-schedule-recurring-event
url: https://skills.sh/googleworkspace/cli/recipe-schedule-recurring-event
---

# recipe-schedule-recurring-event

skills/googleworkspace/cli/recipe-schedule-recurring-event
recipe-schedule-recurring-event
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-schedule-recurring-event
Summary

Schedule recurring Google Calendar events with attendees and recurrence rules.

Requires the gws-calendar skill and gws bin to be loaded
Supports full iCalendar recurrence rules (RRULE) for flexible scheduling patterns like weekly, monthly, or custom intervals
Includes attendee management, timezone configuration, and event verification via agenda view
SKILL.md
Schedule a Recurring Meeting

PREREQUISITE: Load the following skills to execute this recipe: gws-calendar

Create a recurring Google Calendar event with attendees.

Steps
Create recurring event: gws calendar events insert --params '{"calendarId": "primary"}' --json '{"summary": "Weekly Standup", "start": {"dateTime": "2024-03-18T09:00:00", "timeZone": "America/New_York"}, "end": {"dateTime": "2024-03-18T09:30:00", "timeZone": "America/New_York"}, "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO"], "attendees": [{"email": "team@company.com"}]}'
Verify it was created: gws calendar +agenda --days 14 --format table
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