---
title: recipe-reschedule-meeting
url: https://skills.sh/googleworkspace/cli/recipe-reschedule-meeting
---

# recipe-reschedule-meeting

skills/googleworkspace/cli/recipe-reschedule-meeting
recipe-reschedule-meeting
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-reschedule-meeting
Summary

Reschedule Google Calendar events and automatically notify all attendees of time changes.

Requires the gws-calendar skill to function
Uses a three-step workflow: find the event via agenda, retrieve full event details, then patch the event with new start and end times
Automatically sends update notifications to all attendees through the sendUpdates: "all" parameter
Supports timezone-aware scheduling with configurable date, time, and timezone fields
SKILL.md
Reschedule a Google Calendar Meeting

PREREQUISITE: Load the following skills to execute this recipe: gws-calendar

Move a Google Calendar event to a new time and automatically notify all attendees.

Steps
Find the event: gws calendar +agenda
Get event details: gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'
Update the time: gws calendar events patch --params '{"calendarId": "primary", "eventId": "EVENT_ID", "sendUpdates": "all"}' --json '{"start": {"dateTime": "2025-01-22T14:00:00", "timeZone": "America/New_York"}, "end": {"dateTime": "2025-01-22T15:00:00", "timeZone": "America/New_York"}}'
Weekly Installs
11.5K
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