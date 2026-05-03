---
title: recipe-create-gmail-filter
url: https://skills.sh/googleworkspace/cli/recipe-create-gmail-filter
---

# recipe-create-gmail-filter

skills/googleworkspace/cli/recipe-create-gmail-filter
recipe-create-gmail-filter
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-create-gmail-filter
Summary

Automated Gmail message routing through filters that label, star, or archive incoming mail.

Requires the gws-gmail skill and gws binary to execute filter operations
Supports filter criteria matching (sender, subject, keywords) with actions including label assignment, removal from inbox, and archiving
Includes commands to list existing labels, create new labels, apply filters, and verify filter configuration
SKILL.md
Create a Gmail Filter

PREREQUISITE: Load the following skills to execute this recipe: gws-gmail

Create a Gmail filter to automatically label, star, or categorize incoming messages.

Steps
List existing labels: gws gmail users labels list --params '{"userId": "me"}' --format table
Create a new label: gws gmail users labels create --params '{"userId": "me"}' --json '{"name": "Receipts"}'
Create a filter: gws gmail users settings filters create --params '{"userId": "me"}' --json '{"criteria": {"from": "receipts@example.com"}, "action": {"addLabelIds": ["LABEL_ID"], "removeLabelIds": ["INBOX"]}}'
Verify filter: gws gmail users settings filters list --params '{"userId": "me"}' --format table
Weekly Installs
11.9K
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