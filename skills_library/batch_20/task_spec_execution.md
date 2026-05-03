---
title: task-spec-execution
url: https://skills.sh/adol1111/doc-driven-spec-workflow/task-spec-execution
---

# task-spec-execution

skills/adol1111/doc-driven-spec-workflow/task-spec-execution
task-spec-execution
Installation
$ npx skills add https://github.com/adol1111/doc-driven-spec-workflow --skill task-spec-execution
SKILL.md
Task Spec Execution

task-spec-execution is deprecated and kept only as a compatibility shim during migration.

Migration Rule

If a prompt, saved workflow, or older test still says task-spec-execution, do not keep the old combined flow alive by default. Route immediately to one of these:

Use task-preparation when the next work is task-local spec.md, optional plan.md, or review/commit follow-up for those docs.
Use task-execution-simple when task-local docs are already ready and the next work is straightforward direct implementation.

Preserve the target stage's own gates, review pauses, and hard-gate behavior during the redirect. Do not use this compatibility shim to invent roadmap structure or bypass the split stages.

When To Use

Use only when older prompts, installed skills, tests, or habits still call task-spec-execution by name and you need a compatibility redirect. Prefer task-preparation or task-execution-simple directly in new workflows.

Weekly Installs
29
Repository
adol1111/doc-dr…workflow
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass