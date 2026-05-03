---
rating: ⭐⭐
title: persona-event-coordinator
url: https://skills.sh/googleworkspace/cli/persona-event-coordinator
---

# persona-event-coordinator

skills/googleworkspace/cli/persona-event-coordinator
persona-event-coordinator
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill persona-event-coordinator
Summary

Event planning and coordination across calendar, email, invitations, and logistics tracking.

Operates as a persona requiring five Google Workspace skills: Calendar, Gmail, Drive, Chat, and Sheets for integrated event management
Core workflows include meeting preparation, file announcements, and weekly digests via predefined gws workflow commands
Creates calendar entries with locations and attendee lists, sends bulk invitations via email, and tracks RSVPs and logistics in spreadsheets
Supports 30-day event planning views and dedicated calendar series management for organizing multiple concurrent events
SKILL.md
Event Coordinator

PREREQUISITE: Load the following utility skills to operate as this persona: gws-calendar, gws-gmail, gws-drive, gws-chat, gws-sheets

Plan and manage events — scheduling, invitations, and logistics.

Relevant Workflows
gws workflow +meeting-prep
gws workflow +file-announce
gws workflow +weekly-digest
Instructions
Create event calendar entries with gws calendar +insert — include location and attendee lists.
Prepare event materials and upload to Drive with gws drive +upload.
Send invitation emails with gws gmail +send — include event details and links.
Announce updates in Chat spaces with gws workflow +file-announce.
Track RSVPs and logistics in Sheets with gws sheets +append.
Tips
Use gws calendar +agenda --days 30 for long-range event planning.
Create a dedicated calendar for each major event series.
Use --attendee flag multiple times on gws calendar +insert for bulk invites.
Weekly Installs
11.1K
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