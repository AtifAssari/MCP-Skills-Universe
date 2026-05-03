---
rating: ⭐⭐
title: recipe-email-drive-link
url: https://skills.sh/googleworkspace/cli/recipe-email-drive-link
---

# recipe-email-drive-link

skills/googleworkspace/cli/recipe-email-drive-link
recipe-email-drive-link
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-email-drive-link
Summary

Share Google Drive files and email access links to recipients in a single workflow.

Combines Google Drive file sharing with Gmail delivery in three sequential steps: locate files, grant access permissions, and send notification emails
Requires both gws-drive and gws-gmail skills to be loaded before execution
Supports role-based sharing (reader, commenter, editor) and targets specific email addresses with custom messages
SKILL.md
Email a Google Drive File Link

PREREQUISITE: Load the following skills to execute this recipe: gws-drive, gws-gmail

Share a Google Drive file and email the link with a message to recipients.

Steps
Find the file: gws drive files list --params '{"q": "name = '\''Quarterly Report'\''"}'
Share the file: gws drive permissions create --params '{"fileId": "FILE_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "client@example.com"}'
Email the link: gws gmail +send --to client@example.com --subject 'Quarterly Report' --body 'Hi, please find the report here: https://docs.google.com/document/d/FILE_ID'
Weekly Installs
11.5K
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