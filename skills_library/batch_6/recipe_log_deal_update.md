---
title: recipe-log-deal-update
url: https://skills.sh/googleworkspace/cli/recipe-log-deal-update
---

# recipe-log-deal-update

skills/googleworkspace/cli/recipe-log-deal-update
recipe-log-deal-update
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-log-deal-update
Summary

Append deal status updates to a Google Sheets sales tracking spreadsheet.

Requires gws-sheets and gws-drive skills to locate and modify the Sales Pipeline sheet
Workflow: find the tracking sheet by name, read existing pipeline data, then append new deal rows with date, company, status, amount, quarter, and owner fields
Integrates with Google Drive and Sheets APIs to maintain a centralized sales pipeline log
SKILL.md
Log Deal Update to Sheet

PREREQUISITE: Load the following skills to execute this recipe: gws-sheets, gws-drive

Append a deal status update to a Google Sheets sales tracking spreadsheet.

Steps
Find the tracking sheet: gws drive files list --params '{"q": "name = '\''Sales Pipeline'\'' and mimeType = '\''application/vnd.google-apps.spreadsheet'\''"}'
Read current data: gws sheets +read --spreadsheet SHEET_ID --range "Pipeline!A1:F"
Append new row: gws sheets +append --spreadsheet SHEET_ID --range 'Pipeline' --values '["2024-03-15", "Acme Corp", "Proposal Sent", "$50,000", "Q2", "jdoe"]'
Weekly Installs
10.8K
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