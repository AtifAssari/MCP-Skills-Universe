---
title: task-management
url: https://skills.sh/jwilger/agent-skills/task-management
---

# task-management

skills/jwilger/agent-skills/task-management
task-management
Installation
$ npx skills add https://github.com/jwilger/agent-skills --skill task-management
SKILL.md
Task Management

Value: Communication and feedback. Breaking work into explicit, trackable units makes intent visible, progress measurable, and handoffs clean. Small tasks create short feedback loops that catch problems early.

Purpose

Teaches how to decompose work into well-structured tasks with clear acceptance criteria, manage dependencies between tasks, and track status through a consistent lifecycle. The outcome is a work breakdown where every task is unambiguous, appropriately scoped, and sequenced so nothing is blocked unnecessarily.

Practices
Decompose Top-Down, Execute Bottom-Up

Break large goals into progressively smaller tasks until each task represents a single deliverable outcome. Execute from the leaves up.

Start with the goal (epic or feature)
Identify 3-7 child tasks that together achieve the goal
For each child, ask: can one agent complete this in one session? If no, decompose further
Leaf tasks should take minutes to hours, not days

Example:

Epic: User Authentication
  Story: Registration flow
    Task: Create registration command handler
    Task: Build registration form component
    Task: Add email verification automation
  Story: Login flow
    Task: Create login command handler
    Task: Build login form component


Do:

Name tasks with a verb and an outcome ("Create registration handler")
Keep leaf tasks small enough for one focused session
Include acceptance criteria on every leaf task

Do not:

Create tasks so large that progress is invisible for hours
Decompose so finely that task overhead exceeds task work
Leave tasks as vague nouns ("Authentication" tells no one what to do)
Write Acceptance Criteria as Verifiable Statements

Every leaf task needs criteria that are binary: met or not met. Use Given/When/Then for behavior, checklists for deliverables.

State what must be true when the task is done
Each criterion is independently testable
Include edge cases that matter

Example:

Task: Create registration command handler

Acceptance Criteria:
- [ ] Given valid registration data, when command is processed,
      then UserRegistered event is stored
- [ ] Given a duplicate email, when command is processed,
      then command is rejected with a clear error
- [ ] Given a password under 12 characters, when command is processed,
      then validation fails before reaching the handler


Do not:

Write criteria that require subjective judgment ("works well")
Omit error cases -- they are where bugs live
Copy-paste generic criteria across unrelated tasks
Declare Dependencies Explicitly

When task B cannot start until task A completes, declare the dependency. Use the dependency graph to find unblocked work.

Before creating a task, ask: does this depend on another task's output?
Record the dependency in whatever tool you are using
Always query for unblocked/ready tasks rather than scanning the full list

Dependency patterns:

Sequential: Schema -> Repository -> Service -> API endpoint
Fan-out: One design task unblocks multiple implementation tasks
Fan-in: Multiple tasks must complete before integration testing

Do:

Keep dependency chains as short as possible -- long chains serialize work
Prefer parallel-safe decomposition (tasks that can run simultaneously)

Do not:

Create circular dependencies
Assume an implicit ordering -- make every dependency explicit
Block tasks unnecessarily (does B really need A, or just A's interface?)
Slice-to-Task Decomposition

When working from vertical slices with GWT (Given-When-Then) scenarios (e.g., from event modeling), decompose slices so that each task represents one testable behavior increment going through a full RED-GREEN-COMMIT cycle:

Each GWT scenario becomes at least one task
Each task = one TDD cycle: one failing test + its implementation + commit
Order tasks by:
Walking skeleton dependencies first -- infrastructure or plumbing that multiple scenarios need (each as its own TDD cycle)
Acceptance scenario tasks -- each scenario is a task that starts with the outermost failing test and completes through drill-down cycles
Each task includes:
Description: Verb + outcome (e.g., "Implement deposit scenario end-to-end via TDD")
Acceptance criteria: Directly from the GWT scenario
Estimated scope: Files likely affected (helps with mutation testing scoping)

Example:

Slice: "Customer deposits funds"
  Task 1: Walking skeleton — wire request-to-response path (RED: acceptance
    test hits endpoint and gets 404 → GREEN: route exists, returns stub →
    COMMIT)
  Task 2: Deposit scenario — deposit $100 into verified account (RED:
    acceptance test asserts balance increases → drill-down into command
    handler, event persistence, projection — each inner cycle is
    RED-GREEN-COMMIT within this task → outer acceptance test passes → COMMIT)


Anti-pattern: Do not create tasks that batch multiple types or behaviors into one RED phase followed by a separate GREEN phase — this is waterfall disguised as TDD. A task like "Create all domain types" followed by "Implement all handlers" splits phases across tasks instead of keeping each task as a complete TDD cycle.

Pipeline Tracking Metadata

When running in pipeline mode, tasks gain additional tracking fields:

slice_id -- Links the task to its originating vertical slice
gate_status -- pending, passed, or failed (reflects quality gate results)
rework_count -- Number of times the task returned from a quality gate failure

These fields are informational in standalone mode. In pipeline mode, the orchestrator uses them to track slice progress and detect tasks that are cycling through rework repeatedly.

Track Status Through a Consistent Lifecycle

Tasks move through a fixed set of states. Transitions are explicit.

Lifecycle: Open -> Active -> Closed

Open: Task is defined and waiting. May be blocked by dependencies.
Active: Work is in progress. Only one task should be active per agent at a time to maintain focus.
Closed: Work is done and acceptance criteria are met. Always record why.

Rules:

Activate a task before starting work on it
Close a task only when all acceptance criteria are met
Provide a close reason for audit trail
If a task is abandoned, close it with the reason ("Superseded by X" or "No longer needed")
Adapt to Available Tools

This skill works with whatever task tracking is available. Detect and use the best option:

Harness-native task tools (Claude Code TodoWrite, Codex tasks): Use them directly. They integrate with the agent's workflow.
dot CLI (.dots/ directory): File-based, version-controlled. Use dot ready to find unblocked work. Close tasks on the feature branch before creating PRs.
GitHub Issues: Use for cross-team visibility. Link PRs to issues.
File-based fallback: Create a TASKS.md in the repo root. Use markdown checklists. Commit with changes.

The methodology (decompose, specify criteria, track dependencies, manage lifecycle) is the same regardless of tool. The tool is interchangeable; the discipline is not.

Enforcement Note

Advisory in all modes. Task structure and dependency tracking are self-enforced.

Hard constraints:

Close reason required when closing a task: [RC]
Constraints
"One active task per agent": Per agent means per execution context. In pipeline mode with parallel worktrees, each worktree is a separate context. A single human operator managing multiple worktrees is not violating this rule. A single agent context with multiple "active" tasks is.
Binary acceptance criteria: "Binary" means an outside observer could verify met/not-met without subjective judgment. "Code is clean" is not binary. "All functions are under 50 lines" is binary. "Tests pass" is binary. "Code follows best practices" is not. If you have to argue about whether a criterion is met, it's not binary.

See CONSTRAINT-RESOLUTION.md in the template directory for pipeline parallelization rules.

Verification

After completing work guided by this skill, verify:

 Every unit of work has a corresponding task with acceptance criteria
 No task was worked on while its dependencies were still open
 Active tasks were limited to one at a time per agent
 Closed tasks have a recorded reason
 The task hierarchy is navigable (parent-child relationships are clear)
 Remaining open tasks accurately reflect outstanding work

If any criterion is not met, revisit the relevant practice before proceeding.

Dependencies

This skill works standalone. For enhanced workflows, it integrates with:

tdd: Each task maps to one or more TDD cycles. Task acceptance criteria become the tests you write in the red phase. In automated mode, task dependencies inform how work is delegated across agents.
architecture-decisions: Major structural tasks should reference relevant ADRs.

Missing a dependency? Install with:

npx skills add jwilger/agent-skills --skill tdd

Weekly Installs
113
Repository
jwilger/agent-skills
GitHub Stars
2
First Seen
5 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass