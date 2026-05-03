---
rating: ⭐⭐
title: recipe-save-email-attachments
url: https://skills.sh/googleworkspace/cli/recipe-save-email-attachments
---

# recipe-save-email-attachments

skills/googleworkspace/cli/recipe-save-email-attachments
recipe-save-email-attachments
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-save-email-attachments
Summary

Automated workflow to find Gmail attachments and save them to Google Drive folders.

Requires both gws-gmail and gws-drive skills as prerequisites
Covers four core steps: searching emails by attachment criteria, retrieving message details, downloading attachments, and uploading files to Drive
Supports filtered searches using Gmail query syntax (e.g., sender, attachment presence) to target specific messages
Integrates Gmail and Drive operations in a single recipe for streamlined attachment management
SKILL.md
Save Gmail Attachments to Google Drive

PREREQUISITE: Load the following skills to execute this recipe: gws-gmail, gws-drive

Find Gmail messages with attachments and save them to a Google Drive folder.

Steps
Search for emails with attachments: gws gmail users messages list --params '{"userId": "me", "q": "has:attachment from:client@example.com"}' --format table
Get message details: gws gmail users messages get --params '{"userId": "me", "id": "MESSAGE_ID"}'
Download attachment: gws gmail users messages attachments get --params '{"userId": "me", "messageId": "MESSAGE_ID", "id": "ATTACHMENT_ID"}'
Upload to Drive folder: gws drive +upload --file ./attachment.pdf --parent FOLDER_ID
Weekly Installs
11.7K
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