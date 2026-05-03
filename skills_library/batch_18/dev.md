---
title: dev
url: https://skills.sh/zackbart/motif/dev
---

# dev

skills/zackbart/motif/dev
dev
Installation
$ npx skills add https://github.com/zackbart/motif --skill dev
SKILL.md
Motif Development Workflow

You are running the motif workflow — a 5-stage development process. Research flows into Plan, which is the single approval gate. Once the plan is approved, Scaffold, Build, and Validate run autonomously.

Complexity Assessment

Before starting, assess task complexity on a 3-point scale:

Light (quick bug fix, small tweak, config change): abbreviated research, minimal planning, 1-3 tasks
Medium (feature addition, moderate refactor, new test coverage): standard research, full planning, 3-8 tasks
Heavy (large refactor, new system, architecture change): deep research, thorough planning with tradeoff analysis, 8+ tasks

State your assessment to the user before beginning Stage 1.

Approval Gate

The only pause point is after Stage 2 (Plan). Present the final plan (including critic triage if applicable) and ask:

Plan complete. [Brief summary of approach]

go — approve and execute (Scaffold → Build → Validate run autonomously)
redo — re-plan with feedback
stop — end here

Or discuss — ask questions, raise concerns, suggest changes. The plan is updated through conversation until you're satisfied.

Do not auto-advance past the plan. Once approved, Stages 3-5 run without pausing.

Stage 1: Research

Read-only codebase exploration. Do not create, edit, or delete any files.

If a subagent capability is available (e.g., a dedicated research agent), delegate to it. Otherwise, perform research directly.

Depth Calibration:

Light: Find the 1-3 most relevant files. Check for obvious patterns. Minimize tool calls.
Medium: Map the relevant module structure, identify patterns, check test coverage, review recent git history.
Heavy: Comprehensive module mapping, dependency tracing, git archaeology, related test suites, documentation review, similar precedents.

Research Process:

Orient — project structure (package.json, Cargo.toml, pyproject.toml, go.mod, etc.; top-level directories)
Locate — find files relevant to the task
Understand — read key files to understand current implementation
Context — git history for recent changes (git log --oneline -20 -- <path>)
Patterns — coding conventions, testing patterns, architectural decisions
Toolchain — find the test, build, and lint commands so you can run them in later stages

Output:

Relevant Files — each with a 1-line description
Patterns & Conventions — how similar work is done in this codebase
Constraints — build/CI requirements, type system, linting rules
Toolchain — exact commands for test, build, lint
Risks — fragile areas, edge cases, missing coverage
Post-Research Clarification

After research completes, review the findings for open questions or ambiguities. If the research surfaced meaningful unknowns — multiple valid approaches, unclear scope, design choices that would change the plan — ask the user before proceeding to Plan. Use AskUserQuestion to present the questions concisely.

Skip this for light tasks or when research findings are clear and unambiguous. Don't ask questions you can answer from the codebase — this is for genuine unknowns that only the user can resolve.

After clarification (or if none is needed), proceed to Plan.

Stage 2: Plan

Using research findings, produce an implementation plan.

Output:

Approach — what will change and how (be specific about the technique, not just "modify X")
Files — which files will be created, modified, or deleted
Testing — what tests to write or update, how to verify correctness
Tradeoffs (medium/heavy only) — alternatives considered and why this approach wins

Scale depth to complexity. A light plan can be a few sentences. A heavy plan needs alternatives and risk assessment.

Critic Review (medium/heavy tasks)

After drafting the plan, run a critic pass to pressure-test it. Build a complete briefing — the critic starts cold with zero context:

The plan — your full approach with specific files, functions, and techniques
Assumptions — what you're taking for granted
Project context — language, framework, relevant patterns from Research
File paths — every file the plan touches or depends on

Choosing the critic:

First, check whether Codex CLI is available and authenticated:

command -v codex >/dev/null 2>&1 && (test -f ~/.codex/auth.json || test -n "$OPENAI_API_KEY")

If available: tell the user Using Codex (gpt-5.4) for critic review. and spawn the codex-critic subagent with the full briefing.
If not available: tell the user Codex not found — using built-in critic. and spawn the critic subagent with the full briefing.

Present the raw critique to the user, then triage each point:

ACCEPT — the critique is valid. State the specific change to the plan.
REJECT — the critique doesn't hold. Provide evidence from the codebase.

Update the plan with accepted changes before presenting at the pause point.

For light tasks, skip the critic — the overhead isn't worth it.

Stage 3: Scaffold

Decompose the plan into a task list. Each task should be a single, verifiable unit of work.

Use the available task tracking tools (TaskCreate, TaskUpdate, etc.) to create and manage tasks.

Set dependencies where order matters
Include test tasks alongside the code they verify (not as a separate "write all tests" task)
Final task: validate the overall goal

After scaffolding, proceed directly to Build.

Stage 4: Build

This stage runs autonomously. Work through tasks in order without stopping for approval on each one.

For each task:

Mark in-progress
Implement the change
If tests are part of this task, write and run them
Mark completed
Parallel execution (medium/heavy tasks)

When the task list contains independent tasks with no dependencies between them, spawn subagents to work on them concurrently. Each subagent gets:

The specific task(s) to complete
The plan context relevant to those tasks
The patterns and conventions from Research

Keep dependent tasks sequential. For light tasks, just work through them one at a time — the parallelism overhead isn't worth it.

When to stop and ask
A task requires a design decision not covered by the plan
Tests fail in a way that suggests the plan is wrong (not just a typo)
You discover the plan missed something significant

For routine issues (lint errors, minor test fixes, small deviations), handle them and keep going. Use your judgment — the plan is a guide, not a contract.

After all tasks complete, proceed directly to Validate.

Stage 5: Validate

Run automatically after Build completes.

Spawn the validator subagent to independently audit the completed work. Build a complete briefing:

Original task description — what was supposed to be accomplished
The plan — the approach that was agreed on
Task list — the decomposed units of work and their status
Changed files — which files were created, modified, or deleted
Toolchain — test, build, and lint commands from Research

The validator reads every changed file, checks the diff, runs tests, traces callers for regressions, and returns a structured report with a verdict (PASS / PASS WITH NOTES / ISSUES FOUND).

Present the validator's report to the user. If issues are found:

fix + details → go back to Build for targeted fixes
done → accept current state
Weekly Installs
9
Repository
zackbart/motif
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass