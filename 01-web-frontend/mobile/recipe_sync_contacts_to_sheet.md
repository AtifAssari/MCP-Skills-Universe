---
rating: ⭐⭐
title: recipe-sync-contacts-to-sheet
url: https://skills.sh/googleworkspace/cli/recipe-sync-contacts-to-sheet
---

# recipe-sync-contacts-to-sheet

skills/googleworkspace/cli/recipe-sync-contacts-to-sheet
recipe-sync-contacts-to-sheet
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-sync-contacts-to-sheet
Summary

Export your Google Contacts directory to a Google Sheets spreadsheet in three steps.

Requires gws-people and gws-sheets skills to be loaded before execution
Lists contacts from your domain directory with names, email addresses, and phone numbers
Creates a new sheet with headers and appends each contact as a row for easy reference and sharing
SKILL.md
Export Google Contacts to Sheets

PREREQUISITE: Load the following skills to execute this recipe: gws-people, gws-sheets

Export Google Contacts directory to a Google Sheets spreadsheet.

Steps
List contacts: gws people people listDirectoryPeople --params '{"readMask": "names,emailAddresses,phoneNumbers", "sources": ["DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE"], "pageSize": 100}' --format json
Create a sheet: gws sheets +append --spreadsheet SHEET_ID --range 'Contacts' --values '["Name", "Email", "Phone"]'
Append each contact row: gws sheets +append --spreadsheet SHEET_ID --range 'Contacts' --values '["Jane Doe", "jane@company.com", "+1-555-0100"]'
Weekly Installs
10.9K
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