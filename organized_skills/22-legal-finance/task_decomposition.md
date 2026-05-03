---
rating: ⭐⭐⭐
title: task-decomposition
url: https://skills.sh/hieutrtr/ai1-skills/task-decomposition
---

# task-decomposition

skills/hieutrtr/ai1-skills/task-decomposition
task-decomposition
Installation
$ npx skills add https://github.com/hieutrtr/ai1-skills --skill task-decomposition
SKILL.md
Task Decomposition
When to Use

Activate this skill when:

A feature or objective requires 4 or more implementation steps
Changes span multiple files across backend and frontend layers
The user says "break this down", "decompose", "create subtasks", or "what are the steps"
Tracking progress across context windows or sessions is needed
A project-planner output (module map, risks, acceptance criteria) needs to be broken into atomic, executable tasks
Work needs to be parallelized across multiple agents or developers

Expected input: Read plan.md (or plan-<feature-name>.md) produced by project-planner. This file contains the module map, risks, and acceptance criteria. If no plan file exists, accept a high-level objective directly and work from that. The project-planner skill produces the strategic plan (what modules are affected and why). This skill turns that plan into ordered, executable atomic tasks with persistent tracking.

Do NOT use this skill for:

High-level project planning or feature scoping (use project-planner)
Architecture decisions or technology trade-offs (use system-architecture)
Writing implementation code (use python-backend-expert or react-frontend-expert)
Writing tests (use pytest-patterns or react-testing-patterns)
Instructions
Decomposition Rules

Every task produced by this skill MUST follow these rules:

Atomic scope: Each task touches at most 2-3 files. If a task requires changes to more than 3 files, split it further.
Single outcome: Each task has exactly one clear, observable result.
Independent verification: Each task includes a concrete verification command that confirms completion (e.g., pytest tests/unit/test_user.py -x, npm test -- --grep "Component").
Explicit preconditions: Each task lists which other tasks must be completed first, by task ID.
Size limit: If a task involves more than 200 lines of changes, split it into smaller tasks.
No orphans: Every task must either have no preconditions (root task) or depend on another task in the plan.
Task Template

Use this format for every task:

### Task [N]: [Short descriptive title]
- **Files:** [list of files to create or modify]
- **Preconditions:** [task IDs that must be done first, or "None"]
- **Steps:**
  1. [Specific, unambiguous action]
  2. [Specific, unambiguous action]
- **Done when:** [verification command] → [expected result]
- **Complexity:** [trivial / small / medium / large]

Task Sizing Criteria
Size	Files	Lines Changed	Verification	Typical Duration
Trivial	1	<20	Quick check	Single action
Small	1-2	20-100	Unit test	Few steps
Medium	2-3	100-200	Unit + integration	Multiple steps
Large	3+	>200	Full test suite	Split further

If any task is sized "large", it MUST be decomposed into smaller tasks.

Prioritization Order

When ordering tasks, follow this priority sequence:

Infrastructure & configuration — Environment setup, config changes, dependency installation
Database & migrations — Schema changes, Alembic migrations (must precede code that uses new schema)
Shared types & interfaces — TypeScript types, Pydantic schemas shared across layers
Backend services — Repository and service layer implementations
Backend routes — API endpoint handlers
Frontend data layer — TanStack Query hooks, API client functions
Frontend components — UI components and pages
Tests — Unit tests for each layer, then integration tests
Integration & E2E — Full-stack integration verification
Persistent Task Files

Create these files to maintain state across context windows:

task_plan.md

The complete task list with status tracking:

# Task Plan: [Feature Name]

## Status: IN_PROGRESS
## Total Tasks: [N]
## Completed: [M] / [N]

### Task 1: [Title] ✅ DONE
[task details]

### Task 2: [Title] 🔄 IN PROGRESS
[task details]

### Task 3: [Title] ⏳ PENDING
[task details]


Update status markers as tasks complete:

⏳ PENDING — Not yet started
🔄 IN PROGRESS — Currently being worked on
✅ DONE — Completed and verified
❌ BLOCKED — Cannot proceed (list reason)
progress.md

Current state for resuming after context window reset:

# Progress: [Feature Name]

## Current State
- **Last completed task:** Task [N]: [Title]
- **Current task:** Task [M]: [Title]
- **Next task:** Task [P]: [Title]

## What's Been Done
- [Summary of completed work]

## What's Next
- [Immediate next steps]

## Blockers
- [Any issues preventing progress]

findings.md

Notes, decisions, and discoveries made during work:

# Findings: [Feature Name]

## Decisions Made
- [Decision 1: context and rationale]

## Discoveries
- [Unexpected finding 1]

## Blockers Encountered
- [Blocker 1: description and resolution]

Dependency Graph

After decomposing, produce a text-based dependency graph showing task ordering:

Task 1 (migration) ──→ Task 2 (schema)
                                ↓
Task 3 (service) ──→ Task 4 (route) ──→ Task 6 (frontend)
                                ↓
                        Task 5 (tests)


Verify there are no circular dependencies. If found, restructure tasks to break the cycle.

Decomposition Workflow

Follow these steps to decompose any objective:

Read the objective — Understand the full scope of what needs to be done
Identify layers — Which backend modules, frontend components, shared types, and tests are affected
Create root tasks — Tasks with no preconditions (usually infrastructure, config, or migration)
Chain dependent tasks — Build the dependency graph layer by layer
Verify atomicity — Check each task against the decomposition rules
Size check — Ensure no task exceeds the "large" threshold; split if needed
Write persistent files — Create task_plan.md, progress.md, and findings.md
Present the plan — Show the task list with dependency graph to the user
Examples

See references/decomposition-examples.md for complete worked examples including:

Adding user authentication (8 tasks)
Adding full-text search (6 tasks)
Adding file upload with S3 storage (7 tasks)
Quick Example: Add Email Verification

Objective: Add email verification to user registration.

Task 1: Add email_verified field to User model + migration
Task 2: Create email verification token schema and service
Task 3: Add /verify-email endpoint
Task 4: Modify registration to send verification email
Task 5: Add frontend verification page
Task 6: Write tests for verification flow


Dependency graph:

Task 1 ──→ Task 2 ──→ Task 3 ──→ Task 4 ──→ Task 6
                                    ↓
                              Task 5 ──→ Task 6

Edge Cases

Circular dependencies: If Task A requires Task B and Task B requires Task A, restructure by extracting the shared dependency into a new Task C that both depend on.

Tasks that are hard to verify in isolation: Add a lightweight integration test as the verification step. If no automated test is possible, document a manual verification procedure.

Context window running out: Immediately save current state to progress.md before the window resets. Include: last completed task, current task state, any in-progress changes, and the next step to take when resuming.

Scope creep during decomposition: If decomposition reveals the feature is larger than expected, flag this. Consider splitting into multiple phases with separate task plans rather than creating an unmanageable single plan.

Cross-cutting concerns: When a task affects a horizontal layer (auth middleware, logging, error handling), make it a root task that all subsequent tasks depend on. Do not scatter cross-cutting changes across multiple tasks.

Partially completed tasks on resume: When resuming from progress.md, verify the current task's "Done when" condition. If it passes, mark as done and move to the next task. If it fails, continue from where the progress notes indicate.

Weekly Installs
40
Repository
hieutrtr/ai1-skills
GitHub Stars
8
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass