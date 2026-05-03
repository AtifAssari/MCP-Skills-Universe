---
rating: ⭐⭐
title: fusion-issue-author-task
url: https://skills.sh/equinor/fusion-skills/fusion-issue-author-task
---

# fusion-issue-author-task

skills/equinor/fusion-skills/fusion-issue-author-task
fusion-issue-author-task
Installation
$ npx skills add https://github.com/equinor/fusion-skills --skill fusion-issue-author-task
SKILL.md
Author Task Issue
Dependency

Requires fusion-issue-authoring as the top-level orchestrator for classification, shared gates, and publish flow.

When to use

Use this skill for planning, research, specification, migration, testing, documentation, or other enablement work.

When not to use

Do not use this skill when the request is clearly a bug, feature, or user-story issue.

Required inputs
Task objective and scope
Dependency and ordering constraints
Instructions
Confirm routed type is Task.
Start with a concise checklist of small tasks when request is broad.
For multi-issue requests, define logical order and blockers before drafting.
Draft locally in .tmp/TASK-<context>.md.
Use appropriate task template variant (planning/research/spec/testing/documentation/generic).
Include dependency notes and blocker mapping in the draft.
Return draft summary for orchestrator review/publish flow.

Template fallback:

skills/fusion-issue-author-task/assets/issue-templates/task.md
skills/fusion-issue-author-task/assets/issue-templates/task.planning.md
skills/fusion-issue-author-task/assets/issue-templates/task.research.md
skills/fusion-issue-author-task/assets/issue-templates/task.spec.md
skills/fusion-issue-author-task/assets/issue-templates/task.ux.md
skills/fusion-issue-author-task/assets/issue-templates/task.testing.md
skills/fusion-issue-author-task/assets/issue-templates/task.documentation.md
Expected output
Checklist (for broad task requests)
Draft file path in .tmp/
Dependency plan (order + blockers)
Task-specific decomposition summary
Safety & constraints

Never create contradictory dependency links. Always model sequencing before adding blockers. Do not perform mutation directly; mutation stays in fusion-issue-authoring.

Weekly Installs
46
Repository
equinor/fusion-skills
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass