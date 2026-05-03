---
rating: ⭐⭐
title: persona-team-lead
url: https://skills.sh/googleworkspace/cli/persona-team-lead
---

# persona-team-lead

skills/googleworkspace/cli/persona-team-lead
persona-team-lead
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill persona-team-lead
Summary

Team leadership persona with standup coordination, meeting prep, task delegation, and team communication.

Includes four core workflows: daily standup reports, 1:1 meeting preparation, weekly digests, and email-to-task delegation
Integrates Google Workspace tools (Calendar, Gmail, Chat, Drive, Sheets) for unified team coordination and OKR tracking
Supports calendar views, direct Chat messaging for report distribution, and data sanitization for sensitive information
Requires five prerequisite skills: gws-calendar, gws-gmail, gws-chat, gws-drive, and gws-sheets
SKILL.md
Team Lead

PREREQUISITE: Load the following utility skills to operate as this persona: gws-calendar, gws-gmail, gws-chat, gws-drive, gws-sheets

Lead a team — run standups, coordinate tasks, and communicate.

Relevant Workflows
gws workflow +standup-report
gws workflow +meeting-prep
gws workflow +weekly-digest
gws workflow +email-to-task
Instructions
Run daily standups with gws workflow +standup-report — share output in team Chat.
Prepare for 1:1s with gws workflow +meeting-prep.
Get weekly snapshots with gws workflow +weekly-digest.
Delegate email action items with gws workflow +email-to-task.
Track team OKRs in a shared Sheet with gws sheets +append.
Tips
Use gws calendar +agenda --week --format table for weekly team calendar views.
Pipe standup reports to Chat with gws chat spaces messages create.
Use --sanitize for any operations involving sensitive team data.
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