---
rating: ⭐⭐⭐
title: sugar
url: https://skills.sh/scando1993/sugar/sugar
---

# sugar

skills/scando1993/sugar/sugar
sugar
Installation
$ npx skills add https://github.com/scando1993/sugar --skill sugar
SKILL.md
Phased Software Engineering Execution
Task

$ARGUMENTS

Reference

Subagent execution follows the Ralph pattern. Each phase workspace is a self-contained Ralph environment: CLAUDE.md (agent instructions), prd.json (story state machine), progress.txt (learning persistence). Subagents are autonomous — they read their workspace instructions and execute independently.

The Sugar library (src/lib/) is the source of truth for all execution logic. Skills delegate to sugar CLI commands for workspace management, story state, consensus, and pattern propagation. Do not embed procedural bash scripts or Python one-liners — use Sugar CLI instead.

Prompt reinforcement

Use prompt repetition at every decision boundary: state the task, provide context, give the instruction, restate context briefly, repeat the instruction. Apply at skill level (restate $ARGUMENTS before each phase), subagent level (each workspace CLAUDE.md repeats the task), and per-story (restate acceptance criteria before implementing).

Core behavior

Execute in strict phases. Never move to the next phase without explicit user approval.

Before every phase, restate: "The original task is: $ARGUMENTS. This phase's goal is: [phase goal]."

Phase 1 — Planning
Goal

Analyze the task and produce a complete execution plan. Do not implement any code.

Restate: The original task is $ARGUMENTS. This phase produces plan.md and todo.md only.

Actions

Use the /prd skill approach: analyze the task, ask clarifying questions if ambiguous, then produce structured requirements.

Create plan.md at the repo root containing:

objective, scope, assumptions, constraints, risks
dependency map — which parts depend on other parts
architecture / refactor / testing strategy as relevant
execution phases with explicit dependency annotations
blockers

Create todo.md at the repo root containing:

small, actionable, idempotent tasks grouped by phase
checkbox progress tracking (- [ ])
dependency annotations per task
completion criteria per phase
Rules
Do not implement anything or create branches
Stop after Phase 1 and wait for user approval
Phase 2 — Workspace and branch setup
Goal

Create an isolated Ralph workspace for each execution phase.

Restate: The original task is $ARGUMENTS. This phase creates one git worktree per phase, each pre-loaded with the Ralph agent structure.

Preconditions

Only start after explicit user approval.

Actions

Use the Sugar CLI to create workspaces:

# Create workspace for each phase
sugar workspace create <phase-name>

# List created workspaces
sugar workspace list


Branch naming: phase-a-<scope>, phase-b-<scope>, etc.

Rules
One worktree per phase, one branch per phase
Do not start implementation unless user approves Phase 3
Document setup problems in plan.md
Phase 3 — Dependency analysis, PRD generation, and parallel implementation
Preconditions

Only start after explicit user approval.

Restate: The original task is $ARGUMENTS. This phase analyzes dependencies, generates Ralph workspaces with prd.json and CLAUDE.md per phase, then launches all independent phases as parallel subagents.

Sub-phases: 3a → 3b → 3c.

Phase 3a — Dependency analysis

Read plan.md thoroughly. For each phase determine:

Produces: artifacts, files, APIs, types, state changes
Consumes: what it needs from other phases
Hard dependencies: must complete before this starts
Soft dependencies: helpful but not blocking
Independence: zero overlap with other phases

Build the dependency graph. Identify parallel groups, sequential chains, and the critical path.

Phase 3b — Generate execution.md, prd.json, and CLAUDE.md per workspace

The Sugar library generates all workspace files. Use the Orchestrator class or CLI commands:

# Initialize config if not present
sugar config init

# The orchestrator generates: execution.md, prd.json, CLAUDE.md, VERIFY.md, ralph-loop.sh per workspace


For each workspace, the library generates:

prd.json — Ralph-format user stories with consensus state machine
CLAUDE.md — Agent instructions with iron laws, quality protocol, red flags
VERIFY.md — Verifier agent instructions with vote format
ralph-loop.sh — Iteration engine that spawns fresh agents per story
execution.md at repo root — dependency graph, parallel groups, model strategy

Story rules: completable in one pass, ordered by dependency (schema → backend → UI), verifiable criteria, always include "Typecheck passes".

Rules
Every workspace must have: prd.json, progress.txt, CLAUDE.md, ralph-loop.sh, VERIFY.md
Do not proceed to 3c until all workspaces are fully set up
Validate each prd.json: sugar validate <workspace>/prd.json
Phase 3c — Parallel execution via ralph-loop.sh
Goal

Launch the Ralph iteration loop for each phase in parallel.

How iteration works
ralph-loop.sh (the loop — runs in bash)
  ├── Iteration 1: claude < CLAUDE.md → implements US-001 → exits
  ├── Iteration 2: claude < CLAUDE.md → implements US-002 → exits
  ├── Iteration 3: claude < CLAUDE.md → implements US-003 → outputs PHASE_COMPLETE
  └── Loop exits successfully


Each iteration is a fresh agent instance with clean context. Memory persists via:

prd.json — which stories are done (status: "passed"/"pending"/"rejected")
progress.txt — learnings and codebase patterns
git history — all committed code
Execution

Follow execution.md group ordering. Launch ralph loops per group:

# Launch all independent phases in parallel
/tmp/<repo>-phases/phase-a/ralph-loop.sh 20 sonnet &
/tmp/<repo>-phases/phase-b/ralph-loop.sh 20 sonnet &
wait

# Propagate patterns between groups
sugar propagate-patterns --base /tmp/<repo>-phases

# Launch next group
/tmp/<repo>-phases/phase-c/ralph-loop.sh 20 sonnet &
wait


The ralph-loop.sh uses Sugar CLI for state management:

sugar pick-story — get next story
sugar story-update — update story status in prd.json
sugar snapshot — create git snapshot tag before each attempt
Model selection per phase
Sonnet (default): Well-scoped implementation tasks
Haiku: Mechanical tasks — config changes, boilerplate
Opus: Complex architectural decisions, ambiguous requirements

Auto-escalates to Opus on 2+ consecutive failures.

Completion tracking
Phase complete when ralph-loop.sh exits 0
After each group: sugar propagate-patterns to extract and inject patterns
Monitor progress: sugar status-all /tmp/<repo>-phases
Rules
Never launch a dependent phase before prerequisites are confirmed complete
Propagate codebase patterns between groups
One story per commit, all commits must pass quality checks
Phase 4 — Merge
Goal

Safely integrate all completed phase branches.

Restate: The original task is $ARGUMENTS. All phases complete. Merge in dependency order.

Preconditions

Only start after explicit user approval.

Actions
# View workspace status first
sugar status-all /tmp/<repo>-phases


Create merge_order.md at repo root with:

merge order aligned with dependency graph (foundations first)
rationale for ordering
expected conflict areas
conflict resolution notes
validation steps after each merge

Automatic merge:

Merge in documented order
Resolve conflicts using best engineering judgment
Validate after each merge: run quality checks
Update merge_order.md with actual conflict notes
Post-merge validation

Phase 4 is not complete until the final merged result passes all checks.

Cleanup
sugar workspace cleanup

Iron Laws

Three inviolable rules enforced in every workspace:

ONE STORY per iteration — no "while I'm here" additions
NEVER COMMIT BROKEN code — every commit must pass all quality checks
READ PROGRESS.TXT FIRST — check codebase patterns before writing
Red Flags — If You Catch Yourself Thinking:
Thought	Reality
"I'll just implement two quick stories in one iteration"	ONE story per iteration. The loop handles iteration. No exceptions.
"The tests mostly pass, I'll commit and fix later"	ALL commits must pass quality checks. Broken commits poison every future iteration.
"This dependency isn't really needed, I'll skip it"	The dependency graph exists for a reason. Never start dependent work before prerequisites complete.
"I know what changed, I don't need to read progress.txt"	Progress.txt IS your memory. You have NO context without it. Read it FIRST.
"This is a trivial change, I don't need to run checks"	Every commit gets checked. No exceptions. The one you skip is the one that breaks everything.
"I'll refactor this while I'm here"	Stay in scope. Implement the story. Nothing more.
How to interpret user requests
User says	Start from
Planning only / no qualifier	Phase 1
Planning is approved	Phase 2
Setup is done	Phase 3 (3a → 3b → 3c)
PRDs exist, ready to implement	Phase 3c
All branches done, wants merge	Phase 4
Testing only	Phase 1 (testing strategy), then normal flow
Execution rules
Source of truth
Before Phase 3c: todo.md
During Phase 3c: each workspace's prd.json
After each phase completes: sync back to todo.md
Commits
One per story: feat: [Story ID] - [Story Title]
Must pass quality checks
Never bundle unrelated changes
General
Never skip phases or continue without approval
Keep all tracking files current
Document assumptions and blockers explicitly
Propagate codebase patterns between groups
Managed files
File	Location	Created in
plan.md	repo root	Phase 1
todo.md	repo root	Phase 1
execution.md	repo root	Phase 3b
prd.json	each worktree	Phase 3b
progress.txt	each worktree	Phase 2
CLAUDE.md	each worktree	Phase 3b
ralph-loop.sh	each worktree	Phase 3b
VERIFY.md	each worktree	Phase 3b
patterns.json	repo root	Phase 3c (between groups)
merge_order.md	repo root	Phase 4

The first deliverable is always Phase 1 planning only, unless the user explicitly states that a later phase is already approved.

Restate: Given the task $ARGUMENTS — start with Phase 1. Produce plan.md and todo.md. Stop and wait for approval.

Weekly Installs
9
Repository
scando1993/sugar
First Seen
11 days ago
Security Audits
Gen Agent Trust HubWarn
SnykPass