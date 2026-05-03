---
rating: ⭐⭐
title: pickup
url: https://skills.sh/jellydn/my-ai-tools/pickup
---

# pickup

skills/jellydn/my-ai-tools/pickup
pickup
Installation
$ npx skills add https://github.com/jellydn/my-ai-tools --skill pickup
SKILL.md
Pickup Handoff

Resumes work from a previous handoff session which are stored in .claude/handoffs/.

Usage

/pickup [HANDOFF_FILE]

If no handoff file is specified, will show available handoffs and prompt for selection.

Process
Find available handoffs in .claude/handoffs/
Read the selected handoff file
Present the handoff summary to the user
Ask the user to confirm they want to continue
If confirmed, proceed with the next step described in the handoff
Available Handoffs

To see available handoffs:

ls -la .claude/handoffs/


Handoffs are named in format: [YYYY-MM-DD]-[slug].md

Weekly Installs
30
Repository
jellydn/my-ai-tools
GitHub Stars
71
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass