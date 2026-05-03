---
title: recipe-create-meet-space
url: https://skills.sh/googleworkspace/cli/recipe-create-meet-space
---

# recipe-create-meet-space

skills/googleworkspace/cli/recipe-create-meet-space
recipe-create-meet-space
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-create-meet-space
Summary

Create a Google Meet meeting space and email the join link to participants.

Requires two prerequisite skills: gws-meet for space creation and gws-gmail for sending invitations
Creates an open-access meeting space via the Meet API and extracts the meeting URI from the response
Automates sharing the join link by composing and sending an email with the meeting details to specified recipients
SKILL.md
Create a Google Meet Conference

PREREQUISITE: Load the following skills to execute this recipe: gws-meet, gws-gmail

Create a Google Meet meeting space and share the join link.

Steps
Create meeting space: gws meet spaces create --json '{"config": {"accessType": "OPEN"}}'
Copy the meeting URI from the response
Email the link: gws gmail +send --to team@company.com --subject 'Join the meeting' --body 'Join here: MEETING_URI'
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