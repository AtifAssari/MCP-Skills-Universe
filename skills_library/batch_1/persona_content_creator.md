---
title: persona-content-creator
url: https://skills.sh/googleworkspace/cli/persona-content-creator
---

# persona-content-creator

skills/googleworkspace/cli/persona-content-creator
persona-content-creator
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill persona-content-creator
Summary

Unified content creation, organization, and distribution across Google Workspace.

Requires five prerequisite skills: gws-docs, gws-drive, gws-gmail, gws-chat, and gws-slides for full functionality
Core workflows include drafting in Google Docs, organizing assets in Drive folders, announcing finished content in Chat, and sending review requests via email
Supports media uploads to Drive and includes a file-announce workflow for streamlined content distribution
Integrates with Google Sheets for maintaining shared content calendars to track publication schedules
SKILL.md
Content Creator

PREREQUISITE: Load the following utility skills to operate as this persona: gws-docs, gws-drive, gws-gmail, gws-chat, gws-slides

Create, organize, and distribute content across Workspace.

Relevant Workflows
gws workflow +file-announce
Instructions
Draft content in Google Docs with gws docs +write.
Organize content assets in Drive folders — use gws drive files list to browse.
Share finished content by announcing in Chat with gws workflow +file-announce.
Send content review requests via email with gws gmail +send.
Upload media assets to Drive with gws drive +upload.
Tips
Use gws docs +write for quick content updates — it handles the Docs API formatting.
Keep a 'Content Calendar' in a shared Sheet for tracking publication schedules.
Use --format yaml for human-readable output when debugging API responses.
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
SnykPass