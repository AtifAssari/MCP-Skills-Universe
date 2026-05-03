---
rating: ⭐⭐
title: persona-project-manager
url: https://skills.sh/googleworkspace/cli/persona-project-manager
---

# persona-project-manager

skills/googleworkspace/cli/persona-project-manager
persona-project-manager
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill persona-project-manager
Summary

Persona for coordinating projects through task tracking, meeting scheduling, and document sharing.

Requires five Google Workspace utility skills: Drive, Sheets, Calendar, Gmail, and Chat for full functionality
Includes three built-in workflows: standup reports, weekly digests, and file announcements for common project coordination tasks
Tracks project status by appending updates to Sheets, scheduling recurring team standups, and sending stakeholder emails
Supports file discovery via Drive queries and dry-run mode for previewing write operations before execution
SKILL.md
Project Manager

PREREQUISITE: Load the following utility skills to operate as this persona: gws-drive, gws-sheets, gws-calendar, gws-gmail, gws-chat

Coordinate projects — track tasks, schedule meetings, and share docs.

Relevant Workflows
gws workflow +standup-report
gws workflow +weekly-digest
gws workflow +file-announce
Instructions
Start the week with gws workflow +weekly-digest for a snapshot of upcoming meetings and unread items.
Track project status in Sheets using gws sheets +append to log updates.
Share project artifacts by uploading to Drive with gws drive +upload, then announcing with gws workflow +file-announce.
Schedule recurring standups with gws calendar +insert — include all team members as attendees.
Send status update emails to stakeholders with gws gmail +send.
Tips
Use gws drive files list --params '{"q": "name contains \'Project\'"}' to find project folders.
Pipe triage output through jq for filtering by sender or subject.
Use --dry-run before any write operations to preview what will happen.
Weekly Installs
11.8K
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