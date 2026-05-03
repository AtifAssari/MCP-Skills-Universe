---
title: recipe-create-expense-tracker
url: https://skills.sh/googleworkspace/cli/recipe-create-expense-tracker
---

# recipe-create-expense-tracker

skills/googleworkspace/cli/recipe-create-expense-tracker
recipe-create-expense-tracker
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-create-expense-tracker
Summary

Google Sheets spreadsheet template for expense tracking with automated setup and sharing.

Creates a new spreadsheet with standard expense columns (Date, Category, Description, Amount) and sample entries
Includes built-in sharing capabilities to grant read or edit access to team members via email
Requires gws-sheets and gws-drive skills; uses Google Workspace APIs for spreadsheet and file management
SKILL.md
Create a Google Sheets Expense Tracker

PREREQUISITE: Load the following skills to execute this recipe: gws-sheets, gws-drive

Set up a Google Sheets spreadsheet for tracking expenses with headers and initial entries.

Steps
Create spreadsheet: gws drive files create --json '{"name": "Expense Tracker 2025", "mimeType": "application/vnd.google-apps.spreadsheet"}'
Add headers: gws sheets +append --spreadsheet SHEET_ID --range 'Sheet1' --values '["Date", "Category", "Description", "Amount"]'
Add first entry: gws sheets +append --spreadsheet SHEET_ID --range 'Sheet1' --values '["2025-01-15", "Travel", "Flight to NYC", "450.00"]'
Share with manager: gws drive permissions create --params '{"fileId": "SHEET_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "manager@company.com"}'
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