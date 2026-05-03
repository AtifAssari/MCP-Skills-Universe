---
title: recipe-post-mortem-setup
url: https://skills.sh/googleworkspace/cli/recipe-post-mortem-setup
---

# recipe-post-mortem-setup

skills/googleworkspace/cli/recipe-post-mortem-setup
recipe-post-mortem-setup
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-post-mortem-setup
Summary

Orchestrate post-mortem workflows across Google Docs, Calendar, and Chat in one recipe.

Combines three Google Workspace skills to create a structured post-mortem document, schedule a review meeting, and send a team notification
Requires gws-docs, gws-calendar, and gws-chat skills to be loaded before execution
Provides templated steps with customizable incident names, attendees, and meeting times for consistent incident response processes
SKILL.md
Set Up Post-Mortem

PREREQUISITE: Load the following skills to execute this recipe: gws-docs, gws-calendar, gws-chat

Create a Google Docs post-mortem, schedule a Google Calendar review, and notify via Chat.

Steps
Create post-mortem doc: gws docs +write --title 'Post-Mortem: [Incident]' --body '## Summary\n\n## Timeline\n\n## Root Cause\n\n## Action Items'
Schedule review meeting: gws calendar +insert --summary 'Post-Mortem Review: [Incident]' --attendee team@company.com --start '2026-03-16T14:00:00' --end '2026-03-16T15:00:00'
Notify in Chat: gws chat +send --space spaces/ENG_SPACE --text '🔍 Post-mortem scheduled for [Incident].'
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