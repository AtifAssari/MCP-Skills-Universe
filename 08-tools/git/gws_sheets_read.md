---
rating: ⭐⭐
title: gws-sheets-read
url: https://skills.sh/googleworkspace/cli/gws-sheets-read
---

# gws-sheets-read

skills/googleworkspace/cli/gws-sheets-read
gws-sheets-read
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-sheets-read
Summary

Read cell values from a Google Sheet by spreadsheet ID and range.

Requires spreadsheet ID and range specification (e.g., Sheet1!A1:D10 or entire sheet name)
Read-only operation; never modifies the spreadsheet
Supports both specific ranges and full sheet reads
Depends on gws-shared for authentication and global configuration
SKILL.md
sheets +read

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Read values from a spreadsheet

Usage
gws sheets +read --spreadsheet <ID> --range <RANGE>

Flags
Flag	Required	Default	Description
--spreadsheet	✓	—	Spreadsheet ID
--range	✓	—	Range to read (e.g. 'Sheet1!A1:B2')
Examples
gws sheets +read --spreadsheet ID --range "Sheet1!A1:D10"
gws sheets +read --spreadsheet ID --range Sheet1

Tips
Read-only — never modifies the spreadsheet.
For advanced options, use the raw values.get API.
See Also
gws-shared — Global flags and auth
gws-sheets — All read and write spreadsheets commands
Weekly Installs
19.5K
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