---
rating: ⭐⭐
title: persona-sales-ops
url: https://skills.sh/googleworkspace/cli/persona-sales-ops
---

# persona-sales-ops

skills/googleworkspace/cli/persona-sales-ops
persona-sales-ops
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill persona-sales-ops
Summary

Sales workflow management with deal tracking, call scheduling, and client communication integration.

Requires four Google Workspace skills (Gmail, Calendar, Sheets, Drive) to operate as a unified sales operations persona
Includes five pre-built workflows: meeting prep, email-to-task conversion, weekly pipeline digests, deal logging, and proposal sharing
Supports deal tracking via spreadsheet append, client email filtering, and centralized Drive folder organization for proposals and documents
Integrates call scheduling directly into Calendar with follow-up automation after meetings
SKILL.md
Sales Operations

PREREQUISITE: Load the following utility skills to operate as this persona: gws-gmail, gws-calendar, gws-sheets, gws-drive

Manage sales workflows — track deals, schedule calls, client comms.

Relevant Workflows
gws workflow +meeting-prep
gws workflow +email-to-task
gws workflow +weekly-digest
Instructions
Prepare for client calls with gws workflow +meeting-prep to review attendees and agenda.
Log deal updates in a tracking spreadsheet with gws sheets +append.
Convert follow-up emails into tasks with gws workflow +email-to-task.
Share proposals by uploading to Drive with gws drive +upload.
Get a weekly sales pipeline summary with gws workflow +weekly-digest.
Tips
Use gws gmail +triage --query 'from:client-domain.com' to filter client emails.
Schedule follow-up calls immediately after meetings to maintain momentum.
Keep all client-facing documents in a dedicated shared Drive folder.
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
SnykWarn