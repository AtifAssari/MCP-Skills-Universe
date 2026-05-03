---
title: recipe-find-free-time
url: https://skills.sh/googleworkspace/cli/recipe-find-free-time
---

# recipe-find-free-time

skills/googleworkspace/cli/recipe-find-free-time
recipe-find-free-time
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-find-free-time
Summary

Find overlapping free time slots across multiple Google Calendars for scheduling meetings.

Queries free/busy status for multiple users within a specified time range to identify available meeting windows
Requires the gws-calendar skill as a dependency
Integrates with Google Workspace Calendar API to retrieve availability data and create events with attendees in confirmed free slots
SKILL.md
Find Free Time Across Calendars

PREREQUISITE: Load the following skills to execute this recipe: gws-calendar

Query Google Calendar free/busy status for multiple users to find a meeting slot.

Steps
Query free/busy: gws calendar freebusy query --json '{"timeMin": "2024-03-18T08:00:00Z", "timeMax": "2024-03-18T18:00:00Z", "items": [{"id": "user1@company.com"}, {"id": "user2@company.com"}]}'
Review the output to find overlapping free slots
Create event in the free slot: gws calendar +insert --summary 'Meeting' --attendee user1@company.com --attendee user2@company.com --start '2024-03-18T14:00:00' --end '2024-03-18T14:30:00'
Weekly Installs
11.7K
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