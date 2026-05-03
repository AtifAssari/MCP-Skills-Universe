---
title: recipe-forward-labeled-emails
url: https://skills.sh/googleworkspace/cli/recipe-forward-labeled-emails
---

# recipe-forward-labeled-emails

skills/googleworkspace/cli/recipe-forward-labeled-emails
recipe-forward-labeled-emails
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-forward-labeled-emails
Summary

Locate Gmail messages by label and automatically forward them to another recipient.

Requires the gws-gmail skill as a prerequisite dependency
Three-step workflow: search messages by label, retrieve full message content, and forward to a specified email address
Supports custom label queries and preserves original subject and body in forwarded messages
Designed as a recipe for productivity automation within agent workflows
SKILL.md
Forward Labeled Gmail Messages

PREREQUISITE: Load the following skills to execute this recipe: gws-gmail

Find Gmail messages with a specific label and forward them to another address.

Steps
Find labeled messages: gws gmail users messages list --params '{"userId": "me", "q": "label:needs-review"}' --format table
Get message content: gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'
Forward via new email: `gws gmail +send --to manager@company.com --subject 'FW: [Original Subject]' --body 'Forwarding for your review:

[Original Message Body]'`

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