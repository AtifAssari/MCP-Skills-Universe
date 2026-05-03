---
rating: ⭐⭐
title: recipe-save-email-to-doc
url: https://skills.sh/googleworkspace/cli/recipe-save-email-to-doc
---

# recipe-save-email-to-doc

skills/googleworkspace/cli/recipe-save-email-to-doc
recipe-save-email-to-doc
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-save-email-to-doc
Summary

Save Gmail messages to Google Docs for archival and reference.

Requires gws-gmail and gws-docs skills to be loaded
Workflow: search Gmail by query, retrieve message content, create a new Google Doc, and append the email body as formatted text
Supports filtering by subject, sender, and other Gmail query parameters for targeted message selection
SKILL.md
Save a Gmail Message to Google Docs

PREREQUISITE: Load the following skills to execute this recipe: gws-gmail, gws-docs

Save a Gmail message body into a Google Doc for archival or reference.

Steps
Find the message: gws gmail users messages list --params '{"userId": "me", "q": "subject:important from:boss@company.com"}' --format table
Get message content: gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'
Create a doc with the content: gws docs documents create --json '{"title": "Saved Email - Important Update"}'
Write the email body: `gws docs +write --document-id DOC_ID --text 'From: boss@company.com Subject: Important Update

[EMAIL BODY]'`

Weekly Installs
11.4K
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