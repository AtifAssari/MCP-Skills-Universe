---
title: jira-ticket-writer
url: https://skills.sh/miguelez11/skills/jira-ticket-writer
---

# jira-ticket-writer

skills/miguelez11/skills/jira-ticket-writer
jira-ticket-writer
Installation
$ npx skills add https://github.com/miguelez11/skills --skill jira-ticket-writer
SKILL.md
Jira Ticket Writer
Quick start
Identify ticket type (Bug, Story, Task, Spike)
Ask what the user knows — summary, context, problem or goal
Fill the template by asking targeted questions for any missing fields
Present the full draft — iterate until approved
Optionally create or update via jira (see jira-cli skill)
Workflow
 Confirm ticket type
 Gather context: what, why, who is affected, what is the expected outcome
 Fill type-specific sections (see TEMPLATES.md)
 Ensure each acceptance criterion is independently testable
 Include a clear definition of done
 Present full draft and iterate on feedback
 Offer to submit via jira cli (jira cli does not work in sandbox mode)
Key principles

Summary line: <Verb> <object> <context> — 80 chars max.

Good: Fix login redirect loop on expired sessions
Bad: Login problem

Context: Answer "why does this matter?" — business impact, affected users, frequency.

Acceptance criteria: Each item must be independently verifiable. Prefer:

Checkbox lists for features
Given / When / Then for behaviour

Definition of done: What makes this closeable? (e.g. code reviewed, unit tests passing, deployed to staging, product sign-off)

Priority guide:

Critical — system down, data loss, security breach
High — major flow broken, significant user impact
Medium — degraded experience, workaround exists
Low — minor polish, rare edge case

See TEMPLATES.md for full templates by ticket type.

Weekly Installs
8
Repository
miguelez11/skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass