---
title: gws-workflow-meeting-prep
url: https://skills.sh/googleworkspace/cli/gws-workflow-meeting-prep
---

# gws-workflow-meeting-prep

skills/googleworkspace/cli/gws-workflow-meeting-prep
gws-workflow-meeting-prep
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-workflow-meeting-prep
Summary

Fetch your next meeting's agenda, attendees, and linked documents from Google Calendar.

Retrieves the upcoming event with full attendee list and description details
Supports multiple calendar selection via --calendar flag (defaults to primary calendar)
Read-only operation; never modifies calendar data
Output formats include JSON, table, YAML, and CSV for integration flexibility
SKILL.md
workflow +meeting-prep

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Prepare for your next meeting: agenda, attendees, and linked docs

Usage
gws workflow +meeting-prep

Flags
Flag	Required	Default	Description
--calendar	—	primary	Calendar ID (default: primary)
--format	—	—	Output format: json (default), table, yaml, csv
Examples
gws workflow +meeting-prep
gws workflow +meeting-prep --calendar Work

Tips
Read-only — never modifies data.
Shows the next upcoming event with attendees and description.
See Also
gws-shared — Global flags and auth
gws-workflow — All cross-service productivity workflows commands
Weekly Installs
12.1K
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