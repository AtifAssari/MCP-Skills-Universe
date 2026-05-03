---
rating: ⭐⭐
title: gws-sheets-append
url: https://skills.sh/googleworkspace/cli/gws-sheets-append
---

# gws-sheets-append

skills/googleworkspace/cli/gws-sheets-append
gws-sheets-append
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-sheets-append
Summary

Append rows to a Google Sheet with simple or bulk input modes.

Supports single-row appends via comma-separated values or multi-row bulk inserts using JSON array format
Requires spreadsheet ID and optional values; defaults to appending to the first available row
Write operation that should be confirmed with the user before execution
Depends on gws binary and shared Google Workspace authentication from gws-shared
SKILL.md
sheets +append

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Append a row to a spreadsheet

Usage
gws sheets +append --spreadsheet <ID>

Flags
Flag	Required	Default	Description
--spreadsheet	✓	—	Spreadsheet ID
--values	—	—	Comma-separated values (simple strings)
--json-values	—	—	JSON array of rows, e.g. '[["a","b"],["c","d"]]'
--range	—	A1	Target range in A1 notation (e.g. 'Sheet2!A1') to select a specific tab
Examples
gws sheets +append --spreadsheet ID --values 'Alice,100,true'
gws sheets +append --spreadsheet ID --json-values '[["a","b"],["c","d"]]'
gws sheets +append --spreadsheet ID --range "Sheet2!A1" --values 'Alice,100'

Tips
Use --values for simple single-row appends.
Use --json-values for bulk multi-row inserts.
Use --range to append to a specific sheet tab (default: A1, i.e. first sheet).

[!CAUTION] This is a write command — confirm with the user before executing.

See Also
gws-shared — Global flags and auth
gws-sheets — All read and write spreadsheets commands
Weekly Installs
18.2K
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