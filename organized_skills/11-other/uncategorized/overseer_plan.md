---
rating: ⭐⭐⭐
title: overseer-plan
url: https://skills.sh/dmmulroy/overseer/overseer-plan
---

# overseer-plan

skills/dmmulroy/overseer/overseer-plan
overseer-plan
Installation
$ npx skills add https://github.com/dmmulroy/overseer --skill overseer-plan
SKILL.md
Converting Markdown Documents to Overseer Tasks

Use /overseer-plan to convert any markdown planning document into trackable Overseer tasks.

When to Use
After completing a plan in plan mode
Converting specs/design docs to implementation tasks
Creating tasks from roadmap or milestone documents
Usage
/overseer-plan <markdown-file-path>
/overseer-plan <file> --priority 1           # Set priority (0-2, 0=highest)
/overseer-plan <file> --parent <task-id>     # Create as child of existing task

What It Does
Reads markdown file
Extracts title from first # heading (strips "Plan: " prefix)
Creates Overseer milestone (or child task if --parent provided)
Analyzes structure for child task breakdown
Creates child tasks (depth 1) or subtasks (depth 2) when appropriate
Returns task ID and breakdown summary
Hierarchy Levels
Depth	Name	Example
0	Milestone	"Add user authentication system"
1	Task	"Implement JWT middleware"
2	Subtask	"Add token verification function"
Breakdown Decision

Create subtasks when:

3-7 clearly separable work items
Implementation across multiple files/components
Clear sequential dependencies

Keep single milestone when:

1-2 steps only
Work items tightly coupled
Plan is exploratory/investigative
Task Quality Criteria

Every task must be:

Atomic: Single committable unit of work
Validated: Has tests OR explicit acceptance criteria in context ("Done when: ...")
Clear: Technical, specific, imperative verb

Every milestone must:

Demoable: Produces runnable/testable increment
Builds on prior: Can depend on previous milestone's output
Review Workflow
Analyze document → propose breakdown
Invoke Oracle to review breakdown and suggest improvements
Incorporate feedback
Create in Overseer (persists to SQLite via MCP)
After Creating
await tasks.get("<id>");                    // TaskWithContext (full context + learnings)
await tasks.list({ parentId: "<id>" });     // Task[] (children without context chain)
await tasks.start("<id>");                  // Task (VCS required - creates bookmark, records start commit)
await tasks.complete("<id>", { result: "...", learnings: [...] });  // Task (VCS required - commits, bubbles learnings)


VCS Required: start and complete require jj or git (fail with NotARepository if none found). CRUD operations work without VCS.

Note: Priority must be 1-5. Blockers cannot be ancestors or descendants.

When NOT to Use
Document incomplete or exploratory
Content not actionable
No meaningful planning content
Reading Order
Task	File
Understanding API	@file references/api.md
Agent implementation	@file references/implementation.md
See examples	@file references/examples.md
In This Reference
File	Purpose
references/api.md	Overseer MCP codemode API types/methods
references/implementation.md	Step-by-step execution instructions for agent
references/examples.md	Complete worked examples
Weekly Installs
115
Repository
dmmulroy/overseer
GitHub Stars
220
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass