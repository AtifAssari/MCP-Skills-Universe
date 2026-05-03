---
title: recipe-search-and-export-emails
url: https://skills.sh/googleworkspace/cli/recipe-search-and-export-emails
---

# recipe-search-and-export-emails

skills/googleworkspace/cli/recipe-search-and-export-emails
recipe-search-and-export-emails
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-search-and-export-emails
Summary

Search Gmail messages by query and export results for offline review.

Requires the gws-gmail skill as a prerequisite dependency
Supports Gmail query syntax for filtering by sender, date, labels, and other message properties
Exports search results to JSON format for further processing or archival
Retrieves full message details including headers and body content for selected emails
SKILL.md
Search and Export Emails

PREREQUISITE: Load the following skills to execute this recipe: gws-gmail

Find Gmail messages matching a query and export them for review.

Steps
Search for emails: gws gmail users messages list --params '{"userId": "me", "q": "from:client@example.com after:2024/01/01"}'
Get full message: gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'
Export results: gws gmail users messages list --params '{"userId": "me", "q": "label:project-x"}' --format json > project-emails.json
Weekly Installs
627
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass