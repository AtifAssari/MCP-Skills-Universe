---
rating: ⭐⭐
title: recipe-create-vacation-responder
url: https://skills.sh/googleworkspace/cli/recipe-create-vacation-responder
---

# recipe-create-vacation-responder

skills/googleworkspace/cli/recipe-create-vacation-responder
recipe-create-vacation-responder
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-create-vacation-responder
Summary

Set up Gmail out-of-office auto-replies with custom messages and date ranges.

Enables vacation responder with customizable subject line, plain-text response body, and optional contact/domain restrictions
Supports three core operations: enable auto-reply, verify current settings, and disable when returning
Requires the gws-gmail skill as a dependency
SKILL.md
Set Up a Gmail Vacation Responder

PREREQUISITE: Load the following skills to execute this recipe: gws-gmail

Enable a Gmail out-of-office auto-reply with a custom message and date range.

Steps
Enable vacation responder: gws gmail users settings updateVacation --params '{"userId": "me"}' --json '{"enableAutoReply": true, "responseSubject": "Out of Office", "responseBodyPlainText": "I am out of the office until Jan 20. For urgent matters, contact backup@company.com.", "restrictToContacts": false, "restrictToDomain": false}'
Verify settings: gws gmail users settings getVacation --params '{"userId": "me"}'
Disable when back: gws gmail users settings updateVacation --params '{"userId": "me"}' --json '{"enableAutoReply": false}'
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