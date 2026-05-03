---
title: recipe-draft-email-from-doc
url: https://skills.sh/googleworkspace/cli/recipe-draft-email-from-doc
---

# recipe-draft-email-from-doc

skills/googleworkspace/cli/recipe-draft-email-from-doc
recipe-draft-email-from-doc
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-draft-email-from-doc
Summary

Draft Gmail messages directly from Google Doc content without manual copying.

Requires gws-docs and gws-gmail skills to be loaded
Workflow: retrieve document content, extract body text, and send as email in three sequential steps
Supports custom recipient, subject line, and automatic body population from the source document
SKILL.md
Draft a Gmail Message from a Google Doc

PREREQUISITE: Load the following skills to execute this recipe: gws-docs, gws-gmail

Read content from a Google Doc and use it as the body of a Gmail message.

Steps
Get the document content: gws docs documents get --params '{"documentId": "DOC_ID"}'
Copy the text from the body content
Send the email: gws gmail +send --to recipient@example.com --subject 'Newsletter Update' --body 'CONTENT_FROM_DOC'
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
SnykWarn