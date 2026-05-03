---
rating: ⭐⭐
title: eve-job-lifecycle
url: https://skills.sh/incept5/eve-skillpacks/eve-job-lifecycle
---

# eve-job-lifecycle

skills/incept5/eve-skillpacks/eve-job-lifecycle
eve-job-lifecycle
Installation
$ npx skills add https://github.com/incept5/eve-skillpacks --skill eve-job-lifecycle
SKILL.md
Eve Job Lifecycle

Use jobs as the unit of work and keep phases explicit.

Phases
idea -> backlog -> ready -> active -> review -> done or cancelled
Jobs default to ready and can be scheduled immediately.
Create jobs
eve job create --description "..."
Add details with --project, --priority, --phase, --labels, --review.
Create sub-jobs with eve job create --parent <job-id> --description "...".
Update and complete
eve job update <id> --phase <phase>
eve job submit <id> --summary "..."
eve job approve <id> or eve job reject <id> --reason "..."
eve job close <id> --reason "..."
eve job cancel <id> --reason "..."
Dependencies
eve job dep add <job> <blocking-job>
Use dependencies only for true blockers.
Inspect with eve job dep list <id>.
Agent control signals
Emit a fenced json-result block with eve.status as waiting, success, or failed.
Return waiting only after dependencies exist.
Weekly Installs
245
Repository
incept5/eve-skillpacks
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass