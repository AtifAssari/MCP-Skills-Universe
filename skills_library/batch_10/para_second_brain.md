---
title: para-second-brain
url: https://skills.sh/robdefeo/agent-skills/para-second-brain
---

# para-second-brain

skills/robdefeo/agent-skills/para-second-brain
para-second-brain
Installation
$ npx skills add https://github.com/robdefeo/agent-skills --skill para-second-brain
SKILL.md
PARA Method

Use this skill to help users organize and maintain a second brain using the PARA system (Projects, Areas, Resources, Archives).

Routing

Pick the entry point based on user intent:

Classification and "where does this go?" questions: read references/decision-trees.md
Example requests and edge-case comparisons: read references/examples.md
Operational process requests (inbox, review, setup, close-out, archive): read references/workflows.md
Troubleshooting pain points and validation guidance: read references/common-problems.md

If the request is broad or does not clearly match one route, default to references/decision-trees.md.

Output Convention
Classification guidance and Q&A: answer in chat
Validation workflows: run scripts/validate.sh and write report output to PARA-validation-YYYY-MM-DD.md in the current working directory
Installation location: out of scope for this skill; installation is handled by separate tooling
Terminology
Use "second brain" for the user's vault/folder structure
Use "PARA system" only for the method/framework
Validation Workflow

When the user asks to validate structure or project health:

Read references/common-problems.md for interpretation guidance.
Run scripts/validate.sh <path> (or omit path to use current directory).
Save report output to PARA-validation-YYYY-MM-DD.md if user wants a file.
Summarize critical findings and recommended next actions.
Weekly Installs
318
Repository
robdefeo/agent-skills
GitHub Stars
3
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass