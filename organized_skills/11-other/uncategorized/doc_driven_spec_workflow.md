---
rating: ⭐⭐
title: doc-driven-spec-workflow
url: https://skills.sh/adol1111/doc-driven-spec-workflow/doc-driven-spec-workflow
---

# doc-driven-spec-workflow

skills/adol1111/doc-driven-spec-workflow/doc-driven-spec-workflow
doc-driven-spec-workflow
Installation
$ npx skills add https://github.com/adol1111/doc-driven-spec-workflow --skill doc-driven-spec-workflow
SKILL.md
Using Doc-Driven Spec Workflow

Use this root skill only to select and coordinate the next docs-driven stage. Stage-specific skills own the actual bootstrap, planning, spec, plan, execution, and closing behavior.

Mandatory Rules
MUST start docs-driven repository work by identifying the current workflow stage.
MUST load exactly one stage skill next unless the user explicitly asks for a comparison or audit.
MUST delegate stage behavior to the selected skill instead of restating or bypassing that skill's rules.
MUST treat roadmap planning and task reshaping as docs governance. They do not authorize spec writing or implementation by themselves.
MUST distinguish review pauses from hard gates.
MUST treat any clear forward-motion message after a review pause as approval to follow the recommended next step unless the current stop is a hard gate. Do not require specific wording.
MUST require explicit confirmation only for hard gates such as destructive cleanup, risky stay-on-current-branch choices, deleting branches/worktrees, or advancing across an unresolved milestone-closure boundary.
MUST preserve handoff context when switching skills: what is decided, what is undecided, and why the next skill applies.
Routing Rules

Default chain: docs-workflow-bootstrap -> superpowers:brainstorming -> milestone-planning -> task-preparation -> task-execution-simple. Skip stages only when their decision is already settled.

Choose the next skill by the user's current uncertainty:

Current uncertainty	Next skill
Minimum docs scaffold is missing	docs-workflow-bootstrap
Goals, constraints, success criteria, or "now versus later" boundaries are unresolved by docs or prompt evidence	superpowers:brainstorming
Milestone count, module grouping, task breakdown, delivery order, or stage boundaries are unclear	milestone-planning
A concrete task is selected or selectable from confirmed roadmap state	task-preparation

Use docs-workflow-bootstrap when any minimum scaffold file is missing: docs/index.md, docs/architecture/index.md, docs/tasks/index.md, docs/tasks/planning-inbox.md, or docs/context/index.md.

Use superpowers:brainstorming for positive ambiguity evidence only. Missing or stale docs alone route to bootstrap or planning.

Use task-preparation only when all are true:

the task milestone has Roadmap confirmed: yes
previous milestone closure is resolved when crossing milestones
task status is planned or in_progress
dependencies are satisfied or waived
no prior hard gate remains unresolved
the user selected it, or docs/tasks/ clearly identifies it as next by order/status

Do not skip from ambiguous scope to spec writing, use task execution to invent roadmap structure, or keep planning after the question is current-task execution.

Handoff Rules
Bootstrap -> brainstorming or planning: minimum docs scaffold exists.
Brainstorming -> planning: scope, boundaries, and success criteria are clear enough to plan delivery structure.
Planning -> task preparation: selected concrete task is in confirmed roadmap state, dependencies and prior hard gates are clear, and the user wants spec-first execution.
Task preparation -> simple execution: task-local docs are complete, the auto follow-up outcome has been explicitly reported, and the next work is straightforward direct implementation.

At each handoff, briefly restate:

what is decided
what is undecided
what the next skill owns
whether the next stop is a review pause or a hard gate

From task-preparation, also state the docs follow-up outcome explicitly: committed by default unless the user explicitly refused that commit, or intentionally left uncommitted with affected files listed.

Treat any user message that clearly means "move forward" as permission to advance after a review pause. If the recommended next step includes a routine commit, status update, isolation step, or stage handoff, do it without a second approval question. Stop only when a hard gate is outstanding.

Response Shape

Keep orchestration responses compact: current stage, why it applies, next skill, and expected stop point.

Weekly Installs
31
Repository
adol1111/doc-dr…workflow
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass