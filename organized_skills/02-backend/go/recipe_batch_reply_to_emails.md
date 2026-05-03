---
rating: ⭐⭐
title: recipe-batch-reply-to-emails
url: https://skills.sh/googleworkspace/cli/recipe-batch-reply-to-emails
---

# recipe-batch-reply-to-emails

skills/googleworkspace/cli/recipe-batch-reply-to-emails
recipe-batch-reply-to-emails
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-batch-reply-to-emails
Summary

Batch find Gmail messages matching a query and send standardized replies to each.

Requires the gws-gmail skill to execute; operates on Gmail messages via the Google Workspace API
Typical workflow: search for messages by query (unread, from specific senders, with labels), retrieve message details, send templated replies, and mark messages as read
Useful for handling repetitive support requests, acknowledgments, or bulk responses to similar inquiries
SKILL.md
Batch Reply to Similar Gmail Messages

PREREQUISITE: Load the following skills to execute this recipe: gws-gmail

Find Gmail messages matching a query and send a standard reply to each one.

Steps
Find messages needing replies: gws gmail users messages list --params '{"userId": "me", "q": "is:unread from:customers label:support"}' --format table
Read a message: gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'
Send a reply: gws gmail +send --to sender@example.com --subject 'Re: Your Request' --body 'Thank you for reaching out. We have received your request and will respond within 24 hours.'
Mark as read: gws gmail users messages modify --params '{"userId": "me", "id": "MSG_ID"}' --json '{"removeLabelIds": ["UNREAD"]}'
Weekly Installs
629
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn