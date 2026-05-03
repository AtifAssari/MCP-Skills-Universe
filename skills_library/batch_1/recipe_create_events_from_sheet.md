---
title: recipe-create-events-from-sheet
url: https://skills.sh/googleworkspace/cli/recipe-create-events-from-sheet
---

# recipe-create-events-from-sheet

skills/googleworkspace/cli/recipe-create-events-from-sheet
recipe-create-events-from-sheet
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-create-events-from-sheet
Summary

Bulk-create Google Calendar events from spreadsheet rows using a two-step workflow.

Reads event data directly from Google Sheets ranges, extracting summary, start time, end time, and attendee information
Creates calendar entries via the gws-calendar skill with support for multiple attendees and custom time ranges
Requires both gws-sheets and gws-calendar skills to be loaded before execution
SKILL.md
Create Google Calendar Events from a Sheet

PREREQUISITE: Load the following skills to execute this recipe: gws-sheets, gws-calendar

Read event data from a Google Sheets spreadsheet and create Google Calendar entries for each row.

Steps
Read event data: gws sheets +read --spreadsheet SHEET_ID --range "Events!A2:D"
For each row, create a calendar event: gws calendar +insert --summary 'Team Standup' --start '2026-01-20T09:00:00' --end '2026-01-20T09:30:00' --attendee alice@company.com --attendee bob@company.com
Weekly Installs
11.2K
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