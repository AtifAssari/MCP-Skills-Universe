---
rating: ⭐⭐
title: agency-technical-writer
url: https://skills.sh/nordz0r/skills/agency-technical-writer
---

# agency-technical-writer

skills/nordz0r/skills/agency-technical-writer
agency-technical-writer
Installation
$ npx skills add https://github.com/nordz0r/skills --skill agency-technical-writer
SKILL.md
Agency Technical Writer

Write docs that reduce ambiguity, support load, and operator mistakes.

Use with companion skills
Use agency-devops-automator when the document describes deployment, rollback, backups, or release automation.
Use ansible-playbook and kubernetes-specialist when the documentation needs exact operational commands.
Use agency-incident-response-commander when documenting incidents, timelines, or postmortems.
Core workflow
Identify the audience: contributor, operator, reviewer, end user, or on-call engineer.
Start from the user goal: install, deploy, debug, migrate, recover, or contribute.
Separate concepts from procedures. Explain the system briefly, then give runnable steps.
Make docs operationally honest: prerequisites, failure modes, validation, rollback, and ownership.
Prefer concise structure over narrative drift.
Default deliverables
Clear title and scope.
Prerequisites and assumptions.
Step-by-step procedure with exact commands when relevant.
Validation section that proves the procedure worked.
Rollback or recovery section when the task changes production state.
Guardrails
Do not ship docs that omit the verification step.
Do not bury prerequisites after the main procedure.
Keep one concept per section and one procedure per numbered flow.
Avoid vague verbs like "configure" unless the exact file, command, or field is shown.
If the repo already has a style, preserve it.
Common outputs
README for a service or repo.
Contributor guide.
Migration plan.
Runbook.
Architecture note.
Postmortem or incident summary.
Output pattern

Use this structure unless the user asked for something else:

Purpose
Prerequisites
Procedure
Validation
Rollback or troubleshooting
Weekly Installs
9
Repository
nordz0r/skills
GitHub Stars
2
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass