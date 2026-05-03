---
rating: ⭐⭐
title: recipe-share-event-materials
url: https://skills.sh/googleworkspace/cli/recipe-share-event-materials
---

# recipe-share-event-materials

skills/googleworkspace/cli/recipe-share-event-materials
recipe-share-event-materials
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-share-event-materials
Summary

Automatically share Google Drive files with all attendees of a Calendar event.

Requires gws-calendar and gws-drive skills as dependencies
Retrieves event attendee list from Google Calendar, then grants each attendee reader access to specified Drive files
Includes verification step to confirm sharing permissions were applied successfully
SKILL.md
Share Files with Meeting Attendees

PREREQUISITE: Load the following skills to execute this recipe: gws-calendar, gws-drive

Share Google Drive files with all attendees of a Google Calendar event.

Steps
Get event attendees: gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'
Share file with each attendee: gws drive permissions create --params '{"fileId": "FILE_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "attendee@company.com"}'
Verify sharing: gws drive permissions list --params '{"fileId": "FILE_ID"}' --format table
Weekly Installs
10.9K
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