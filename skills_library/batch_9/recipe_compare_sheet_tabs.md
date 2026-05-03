---
title: recipe-compare-sheet-tabs
url: https://skills.sh/googleworkspace/cli/recipe-compare-sheet-tabs
---

# recipe-compare-sheet-tabs

skills/googleworkspace/cli/recipe-compare-sheet-tabs
recipe-compare-sheet-tabs
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-compare-sheet-tabs
Summary

Compare data across two Google Sheets tabs to identify differences.

Reads data from two separate sheet tabs using the gws-sheets skill
Requires the Google Workspace (gws) bin and gws-sheets skill as prerequisites
Follows a three-step workflow: read first tab, read second tab, then compare and report changes
Supports flexible range selection (e.g., January!A1:D, February!A1:D) for targeted data extraction
SKILL.md
Compare Two Google Sheets Tabs

PREREQUISITE: Load the following skills to execute this recipe: gws-sheets

Read data from two tabs in a Google Sheet to compare and identify differences.

Steps
Read the first tab: gws sheets +read --spreadsheet SHEET_ID --range "January!A1:D"
Read the second tab: gws sheets +read --spreadsheet SHEET_ID --range "February!A1:D"
Compare the data and identify changes
Weekly Installs
11.6K
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