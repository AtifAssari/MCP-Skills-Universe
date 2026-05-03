---
title: recipe-send-personalized-emails
url: https://skills.sh/googleworkspace/cli/recipe-send-personalized-emails
---

# recipe-send-personalized-emails

skills/googleworkspace/cli/recipe-send-personalized-emails
recipe-send-personalized-emails
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-send-personalized-emails
Summary

Read recipient data from Google Sheets and send personalized Gmail messages to each row.

Requires gws-sheets and gws-gmail skills to be loaded before execution
Reads recipient lists from a specified Google Sheets range, then iterates through each row to send customized emails
Supports dynamic personalization by embedding recipient data (name, email, etc.) into subject lines and message bodies
SKILL.md
Send Personalized Emails from a Sheet

PREREQUISITE: Load the following skills to execute this recipe: gws-sheets, gws-gmail

Read recipient data from Google Sheets and send personalized Gmail messages to each row.

Steps
Read recipient list: gws sheets +read --spreadsheet-id SHEET_ID --range 'Contacts!A2:C'
For each row, send a personalized email: gws gmail +send --to recipient@example.com --subject 'Hello, Name' --body 'Hi Name, your report is ready.'
Weekly Installs
627
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass