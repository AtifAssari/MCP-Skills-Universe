---
rating: ⭐⭐
title: pragma-post-writer
url: https://skills.sh/moazbuilds/pragma-post-writer/pragma-post-writer
---

# pragma-post-writer

skills/moazbuilds/pragma-post-writer/pragma-post-writer
pragma-post-writer
Installation
$ npx skills add https://github.com/moazbuilds/pragma-post-writer --skill pragma-post-writer
SKILL.md
Pragma Post Writer Router
START HERE

Your first question MUST be:

"What do you want: quick (Flash 💥) or expert (Ink 🖋️)?"

Then explain the options clearly:

Quick (Flash 💥): One-step writing pass for when the user already has a draft and wants a fast final version.
Expert (Ink 🖋️): Full 5-step structured workflow:
Pre-Writing - Find and validate the core idea
Hook - Craft the opening lines
Body - Build the main content
Ending - Land the kicker and CTA
Edit & Polish - Humanize and finalize

Wait for the answer before loading any workflow content.

ROUTING RULES

If user chooses quick or flash:

Read only: ./routes/flash.md
Execute that workflow
Do not load expert files

If user chooses expert or ink:

Read: ./routes/ink.md
Then follow step loading using the expert step paths in that file
Do not load quick files

If unclear:

Ask again with the same two options
Weekly Installs
10
Repository
moazbuilds/prag…t-writer
GitHub Stars
4
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass