---
rating: ⭐⭐
title: recipe-backup-sheet-as-csv
url: https://skills.sh/googleworkspace/cli/recipe-backup-sheet-as-csv
---

# recipe-backup-sheet-as-csv

skills/googleworkspace/cli/recipe-backup-sheet-as-csv
recipe-backup-sheet-as-csv
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-backup-sheet-as-csv
Summary

Export Google Sheets spreadsheets as CSV files for backup or local processing.

Requires gws-sheets and gws-drive skills as prerequisites
Offers three export approaches: retrieve spreadsheet metadata, export via Drive API with MIME type specification, or read sheet values directly in CSV format
Supports flexible range selection and sheet targeting for granular control over exported data
SKILL.md
Export a Google Sheet as CSV

PREREQUISITE: Load the following skills to execute this recipe: gws-sheets, gws-drive

Export a Google Sheets spreadsheet as a CSV file for local backup or processing.

Steps
Get spreadsheet details: gws sheets spreadsheets get --params '{"spreadsheetId": "SHEET_ID"}'
Export as CSV: gws drive files export --params '{"fileId": "SHEET_ID", "mimeType": "text/csv"}'
Or read values directly: gws sheets +read --spreadsheet SHEET_ID --range 'Sheet1' --format csv
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