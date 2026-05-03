---
title: recipe-send-team-announcement
url: https://skills.sh/googleworkspace/cli/recipe-send-team-announcement
---

# recipe-send-team-announcement

skills/googleworkspace/cli/recipe-send-team-announcement
recipe-send-team-announcement
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-send-team-announcement
Summary

Send team announcements simultaneously via Gmail and Google Chat.

Combines email and chat messaging in a single workflow, ensuring announcements reach team members through both channels
Requires gws-gmail and gws-chat skills to be loaded; uses the gws binary for command execution
Typical pattern: send formatted email to a distribution list, then post a notification message to a Google Chat space with optional emoji and summary text
SKILL.md
Announce via Gmail and Google Chat

PREREQUISITE: Load the following skills to execute this recipe: gws-gmail, gws-chat

Send a team announcement via both Gmail and a Google Chat space.

Steps
Send email: gws gmail +send --to team@company.com --subject 'Important Update' --body 'Please review the attached policy changes.'
Post in Chat: gws chat +send --space spaces/TEAM_SPACE --text '📢 Important Update: Please check your email for policy changes.'
Weekly Installs
10.9K
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