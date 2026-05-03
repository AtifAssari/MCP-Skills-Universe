---
title: recipe-batch-invite-to-event
url: https://skills.sh/googleworkspace/cli/recipe-batch-invite-to-event
---

# recipe-batch-invite-to-event

skills/googleworkspace/cli/recipe-batch-invite-to-event
recipe-batch-invite-to-event
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-batch-invite-to-event
Summary

Batch-add attendees to Google Calendar events with automatic notifications.

Requires the gws-calendar skill and gws binary to execute
Workflow includes three steps: retrieve the event, patch attendees with sendUpdates: "all" to notify participants, and verify the update
Supports adding multiple attendees in a single operation by passing an array of email addresses
SKILL.md
Add Multiple Attendees to a Calendar Event

PREREQUISITE: Load the following skills to execute this recipe: gws-calendar

Add a list of attendees to an existing Google Calendar event and send notifications.

Steps
Get the event: gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'
Add attendees: gws calendar events patch --params '{"calendarId": "primary", "eventId": "EVENT_ID", "sendUpdates": "all"}' --json '{"attendees": [{"email": "alice@company.com"}, {"email": "bob@company.com"}, {"email": "carol@company.com"}]}'
Verify attendees: gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'
Weekly Installs
11.2K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass