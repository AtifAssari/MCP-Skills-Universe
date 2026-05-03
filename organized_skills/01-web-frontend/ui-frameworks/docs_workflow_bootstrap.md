---
rating: ⭐⭐
title: docs-workflow-bootstrap
url: https://skills.sh/adol1111/doc-driven-spec-workflow/docs-workflow-bootstrap
---

# docs-workflow-bootstrap

skills/adol1111/doc-driven-spec-workflow/docs-workflow-bootstrap
docs-workflow-bootstrap
Installation
$ npx skills add https://github.com/adol1111/doc-driven-spec-workflow --skill docs-workflow-bootstrap
SKILL.md
Docs Workflow Bootstrap

Initialize the minimum docs-driven workflow scaffold for a repository. This skill is only for bootstrap docs governance; it does not plan milestones, create implementation tasks, write specs, or authorize code changes.

Composition
Entry: normally reached from doc-driven-spec-workflow when the repository lacks the minimum docs scaffold.
Owns: minimum docs entry points and compact bootstrap content.
Does not own: roadmap decomposition, task creation, task-local specs/plans, implementation, or branch closing.
Handoff: return to doc-driven-spec-workflow after reporting created or changed files, unless the user explicitly asks to continue to planning.
Mandatory Rules
MUST keep bootstrap work in docs governance mode.
MUST create only the minimum docs entry points unless the user explicitly asks for more.
MUST NOT create implementation tasks during bootstrap.
If the user provides actual roadmap or task content during bootstrap, record it only as compact planning-inbox.md candidate context when explicitly requested, then hand off to milestone-planning.
MUST NOT create docs/specs/, docs/plans/, or task-local spec.md / plan.md by default.
MUST report created or changed files and stop.
Bootstrap Layout

Create these files when missing:

docs/index.md
docs/architecture/index.md
docs/tasks/index.md
docs/tasks/planning-inbox.md
docs/context/index.md

Use the repository's documentation language instructions when available. Otherwise follow the user's current language request.

Default Content Shape

Keep generated files compact:

docs/index.md: explain the docs entry point and link to architecture, tasks, and context
docs/architecture/index.md: explain stable design and behavior boundaries
docs/tasks/index.md: explain roadmap/task tracking; include Open Milestones, Completed Milestones, and a link to Planning Inbox
docs/tasks/planning-inbox.md: explain that unconfirmed goals, opportunities, and roadmap candidates live there until promoted into a milestone, moved to backlog, or discarded
docs/context/index.md: explain research notes and supporting context

Do not create roadmap details during bootstrap unless the user supplies actual roadmap content.

Handoff

After bootstrap, return to doc-driven-spec-workflow so it can choose the next stage. Continue directly only when the user explicitly asks:

milestone-planning for milestone/module/task planning
task-preparation for a concrete selected task in confirmed roadmap state with dependencies and prior hard gates clear

Otherwise stop after reporting the bootstrap result.

Weekly Installs
28
Repository
adol1111/doc-dr…workflow
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass