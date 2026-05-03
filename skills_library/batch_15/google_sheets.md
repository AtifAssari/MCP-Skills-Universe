---
title: google-sheets
url: https://skills.sh/abdullahbeam/nexus-design-abdullah/google-sheets
---

# google-sheets

skills/abdullahbeam/nexus-design-abdullah/google-sheets
google-sheets
Installation
$ npx skills add https://github.com/abdullahbeam/nexus-design-abdullah --skill google-sheets
SKILL.md
Google Sheets

Read, write, and manage Google Sheets via OAuth authentication.

Pre-Flight Check (ALWAYS FIRST)
python3 00-system/skills/google/google-master/scripts/google_auth.py --check --service sheets


Exit codes:

0: Ready - proceed with user's request
1: Need login - run python3 00-system/skills/google/google-master/scripts/google_auth.py --login
2: Missing deps - see ../google-master/references/setup-guide.md
Quick Reference
Read Data
python3 00-system/skills/google/google-sheets/scripts/sheets_operations.py read <spreadsheet_id> "Sheet1!A1:D10"

Write Data
python3 00-system/skills/google/google-sheets/scripts/sheets_operations.py write <spreadsheet_id> "Sheet1!A1" --values '[["Name", "Amount"], ["Contract A", 5000]]'

Append Rows
python3 00-system/skills/google/google-sheets/scripts/sheets_operations.py append <spreadsheet_id> "Sheet1!A:D" --values '[["New Row", "Data", "Here", "Now"]]'

Get Sheet Info
python3 00-system/skills/google/google-sheets/scripts/sheets_operations.py info <spreadsheet_id>

List Spreadsheets
python3 00-system/skills/google/google-sheets/scripts/sheets_operations.py list --query "tracking"

Create Spreadsheet
python3 00-system/skills/google/google-sheets/scripts/sheets_operations.py create "New Spreadsheet" --sheets "Data" "Summary"

Common Workflows
Extract Data -> Update Sheet
from sheets_operations import append_rows

data = [
    ["Contract A", "2024-01-15", 5000, "Active"],
    ["Contract B", "2024-02-01", 7500, "Pending"]
]
result = append_rows(spreadsheet_id, "Contracts!A:D", data)
print(f"Added {result['updated_rows']} rows")

Batch Update Multiple Cells
from sheets_operations import batch_update

data = [
    {"range": "Sheet1!A1", "values": [["Header 1"]]},
    {"range": "Sheet1!B1", "values": [["Header 2"]]},
]
batch_update(spreadsheet_id, data)

Spreadsheet ID

The spreadsheet ID is in the URL:

https://docs.google.com/spreadsheets/d/[SPREADSHEET_ID]/edit

A1 Notation
Example	Meaning
A1	Single cell
A1:B5	Range from A1 to B5
Sheet1!A1:B5	Range in specific sheet
A:A	Entire column A
1:1	Entire row 1
Available Operations
Operation	Function	Description
Read	read_range()	Read data from range
Write	write_range()	Write data to range
Append	append_rows()	Append rows to sheet
Clear	clear_range()	Clear values (keep formatting)
Batch	batch_update()	Update multiple ranges
Create	create_spreadsheet()	Create new spreadsheet
Info	get_spreadsheet_info()	Get metadata and sheets
List	list_spreadsheets()	List accessible spreadsheets
Error Handling

See ../google-master/references/error-handling.md for common errors and solutions.

Setup

First-time setup: ../google-master/references/setup-guide.md

Quick start:

pip install google-auth google-auth-oauthlib google-api-python-client
Create OAuth credentials in Google Cloud Console (enable Google Sheets API & Drive API, choose "Desktop app")
Add to .env file at Nexus root:
GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret
GOOGLE_PROJECT_ID=your-project-id

Run python3 00-system/skills/google/google-master/scripts/google_auth.py --login
Weekly Installs
19
Repository
abdullahbeam/ne…abdullah
GitHub Stars
2
First Seen
5 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn