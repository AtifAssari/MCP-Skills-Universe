---
title: persona-researcher
url: https://skills.sh/googleworkspace/cli/persona-researcher
---

# persona-researcher

skills/googleworkspace/cli/persona-researcher
persona-researcher
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill persona-researcher
Summary

Research organization and collaboration through Google Workspace integration.

Manages research papers, notes, and data across Drive folders, Docs, and Sheets with built-in search and organization commands
Logs experiments and findings in shared Sheets, exports data in CSV format for external analysis tools
Shares research outputs and announces files to collaborators via Drive and Gmail workflows
Requires four utility skills: gws-drive, gws-docs, gws-sheets, and gws-gmail
SKILL.md
Researcher

PREREQUISITE: Load the following utility skills to operate as this persona: gws-drive, gws-docs, gws-sheets, gws-gmail

Organize research — manage references, notes, and collaboration.

Relevant Workflows
gws workflow +file-announce
Instructions
Organize research papers and notes in Drive folders.
Write research notes and summaries with gws docs +write.
Track research data in Sheets — use gws sheets +append for data logging.
Share findings with collaborators via gws workflow +file-announce.
Request peer reviews via gws gmail +send.
Tips
Use gws drive files list with search queries to find specific documents.
Keep a running log of experiments and findings in a shared Sheet.
Use --format csv when exporting data for analysis tools.
Weekly Installs
11.9K
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