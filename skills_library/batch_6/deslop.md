---
title: deslop
url: https://skills.sh/davila7/claude-code-templates/deslop
---

# deslop

skills/davila7/claude-code-templates/deslop
deslop
Originally frombrianlovin/claude-config
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill deslop
SKILL.md
Remove AI Code Slop

Check the diff against main and remove all AI-generated slop introduced in this branch.

What to Remove
Extra comments that a human wouldn't add or are inconsistent with the rest of the file
Extra defensive checks or try/catch blocks that are abnormal for that area of the codebase (especially if called by trusted/validated codepaths)
Casts to any to get around type issues
Inline imports in Python (move to top of file with other imports)
Any other style that is inconsistent with the file
Process
Get the diff against main: git diff main...HEAD
Review each changed file for slop patterns
Remove identified slop while preserving legitimate changes
Report a 1-3 sentence summary of what was changed
Weekly Installs
266
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass