---
title: recipe-share-doc-and-notify
url: https://skills.sh/googleworkspace/cli/recipe-share-doc-and-notify
---

# recipe-share-doc-and-notify

skills/googleworkspace/cli/recipe-share-doc-and-notify
recipe-share-doc-and-notify
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-share-doc-and-notify
Summary

Share a Google Doc with collaborators and send them notification emails.

Combines three Google Workspace skills (Drive, Docs, Gmail) to locate documents, grant editor access, and notify recipients in sequence
Automates the workflow of finding docs by name, adding collaborators with write permissions, and emailing them the share link
Requires gws-drive, gws-docs, and gws-gmail skills to be loaded before execution
SKILL.md
Share a Google Doc and Notify Collaborators

PREREQUISITE: Load the following skills to execute this recipe: gws-drive, gws-docs, gws-gmail

Share a Google Docs document with edit access and email collaborators the link.

Steps
Find the doc: gws drive files list --params '{"q": "name contains '\''Project Brief'\'' and mimeType = '\''application/vnd.google-apps.document'\''"}'
Share with editor access: gws drive permissions create --params '{"fileId": "DOC_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "reviewer@company.com"}'
Email the link: gws gmail +send --to reviewer@company.com --subject 'Please review: Project Brief' --body 'I have shared the project brief with you: https://docs.google.com/document/d/DOC_ID'
Weekly Installs
11.2K
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