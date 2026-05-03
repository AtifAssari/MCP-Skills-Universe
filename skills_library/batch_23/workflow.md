---
title: workflow
url: https://skills.sh/epicenterhq/epicenter/workflow
---

# workflow

skills/epicenterhq/epicenter/workflow
workflow
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill workflow
SKILL.md
Standard Workflow
First think through the problem, read the codebase for relevant files, and write a plan to specs/[timestamp] [feature-name].md where [timestamp] is the timestamp in YYYYMMDDThhmmss format and [feature-name] is the name of the feature.
The plan should have a list of todo items that you can check off as you complete them
Before you begin working, check in with me and I will verify the plan. For non-trivial changes (multiple approaches, 3+ files, architecture shifts), present competing options with before/after diffs and ASCII diagrams before implementing (see change-proposal skill).
Then, begin working on the todo items, marking them as complete as you go.
Please every step of the way just give me a high level explanation of what changes you made
Make every task and code change you do as simple as possible. We want to avoid making any massive or complex changes. Every change should impact as little code as possible. Everything is about simplicity.
Finally, add a review section to the .md file with a summary of the changes you made and any other relevant information.
When to Apply This Skill

Use this pattern when you need to:

Start a non-trivial feature with a timestamped planning spec in specs/.
Build a checklist-driven implementation plan before writing code.
Get plan verification before execution begins.
Execute work in small, simple steps with high-level progress updates.
Close work by adding a review summary to the spec.
Spec Placement

All specs live in the root /specs/ directory. Do not create nested specs in apps/ or packages/.

Weekly Installs
63
Repository
epicenterhq/epicenter
GitHub Stars
4.5K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass