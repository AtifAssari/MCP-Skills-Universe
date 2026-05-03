---
title: recipe-label-and-archive-emails
url: https://skills.sh/googleworkspace/cli/recipe-label-and-archive-emails
---

# recipe-label-and-archive-emails

skills/googleworkspace/cli/recipe-label-and-archive-emails
recipe-label-and-archive-emails
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-label-and-archive-emails
Summary

Automatically label and archive Gmail messages matching custom search criteria.

Requires the gws-gmail skill to execute Gmail API operations
Three-step workflow: search for matching emails using query syntax, apply custom labels, and remove messages from inbox
Supports flexible filtering through Gmail's query language (e.g., sender, subject, date ranges)
Designed as a recipe template for building inbox automation workflows
SKILL.md
Label and Archive Gmail Threads

PREREQUISITE: Load the following skills to execute this recipe: gws-gmail

Apply Gmail labels to matching messages and archive them to keep your inbox clean.

Steps
Search for matching emails: gws gmail users messages list --params '{"userId": "me", "q": "from:notifications@service.com"}' --format table
Apply a label: gws gmail users messages modify --params '{"userId": "me", "id": "MESSAGE_ID"}' --json '{"addLabelIds": ["LABEL_ID"]}'
Archive (remove from inbox): gws gmail users messages modify --params '{"userId": "me", "id": "MESSAGE_ID"}' --json '{"removeLabelIds": ["INBOX"]}'
Weekly Installs
11.4K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass