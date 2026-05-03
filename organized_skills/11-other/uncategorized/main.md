---
rating: ⭐⭐
title: main
url: https://skills.sh/sipengxie2024/superpower-planning/main
---

# main

skills/sipengxie2024/superpower-planning/main
main
Installation
$ npx skills add https://github.com/sipengxie2024/superpower-planning --skill main
SKILL.md
How to Access Skills

In Claude Code: Use the Skill tool. When you invoke a skill, its content is loaded and presented to you -- follow it directly. Never use the Read tool on skill files.

In other environments: Check your platform's documentation for how skills are loaded.

Using Skills
The Rule

Invoke relevant or requested skills BEFORE any response or action. Even a 1% chance a skill might apply means you should invoke the skill to check. If an invoked skill turns out to be wrong for the situation, you don't need to use it.

When multiple skills could apply: process skills first (brainstorming, debugging), then implementation skills (executing-plans, tdd).

If you're thinking "this doesn't need a skill" — it probably does. Check BEFORE any action.

Planning Context

When starting a complex task (multi-step, research, >5 tool calls):

Check if .planning/ directory exists in the project root
If NOT found, run ${CLAUDE_PLUGIN_ROOT}/scripts/init-planning-dir.sh to initialize it
If FOUND, read the existing planning files to recover context (see Session Recovery below)

The .planning/ directory is your "RAM on disk" -- persistent working memory that survives context resets.

Session Recovery

On session start, check for an existing .planning/ directory. If found:

Read .planning/progress.md -- Task Status Dashboard shows current status; session log shows what was done
Read .planning/findings.md -- recall discoveries and decisions
Run git diff --stat to see what changed since last session
Update planning files with recovered context
Continue with the task
Planning Approach Routing

When facing a non-trivial task (multi-step, architectural decisions, multi-file changes), do NOT automatically call EnterPlanMode or invoke brainstorming. Instead, present the choice to the user via AskUserQuestion:

Option 1: Quick Planning (Plan Mode) — Lightweight read-only exploration. Best for medium-scope tasks with known approach, quick alignment before implementation.

Option 2: Lightweight Execution — Fast structured execution with .planning/ tracking but no review loops or formal plans. Best for clear requirements, 2-5 files, <10 tasks. Code gets written in this session.

Option 3: Structured Brainstorming — Full brainstorming pipeline with design doc, spec interview, implementation plan. Best for complex features, creative design decisions, multi-file refactors.

Option 4: Stash Current Work — Pause unfinished work safely, save current .planning/ context into .planning/stash/, and switch away cleanly. Best when changing projects or waiting on external input.

When to skip this choice:

Trivial tasks (typo, single-line fix) → just do it, no planning needed
User explicitly requests one mode (e.g., "let's brainstorm", "/plan") → use what they asked for
Already inside plan mode or brainstorming → continue the current flow

After Plan Mode completes: If the approved plan reveals complex work (3+ tasks, multiple files), suggest transitioning to brainstorming/writing-plans for a formal implementation plan. Plan mode output can inform writing-plans — reference it, don't re-derive.

When Lightweight Execution is chosen: Invoke superpower-planning:lightweight-execute. This skill handles everything: .planning/ init, exploration, task checklist, implementation, verification, and finishing-branch. No further routing is needed.

Execution Routing

When the user requests plan execution (e.g., "execute the plan", "implement it", "start building"), do NOT directly invoke a single execution skill. Instead:

If no plan exists at .planning/plan.md, invoke superpower-planning:writing-plans first.
If a plan exists, present the execution strategy choice via AskUserQuestion:
Subagent-Driven (this session, sequential) → superpower-planning:subagent-driven
Team-Driven (this session, parallel) → superpower-planning:team-driven
Parallel Session (separate session) → superpower-planning:executing-plans
Recommend based on: high parallelism + heavy tasks → Team-Driven; light serial → Subagent-Driven; manual checkpoints → Parallel Session.
Available Skills
Skill	Purpose
superpower-planning:planning-foundation	Persistent file-based planning with .planning/ directory. Foundation layer inherited by all other skills.
superpower-planning:lightweight-execute	Fast structured execution for clear, medium-scope tasks (2-5 files). Skips formal plans and review loops, keeps .planning/ tracking and verification.
superpower-planning:brainstorming	Structured brainstorming before implementation. Think before you code.
superpower-planning:spec-interview	Refine design docs through systematic deep questioning. Auto-invoked after brainstorming.
superpower-planning:writing-plans	Write detailed implementation plans with phases and checkpoints.
superpower-planning:executing-plans	Execute plans in a separate session with batch execution and human checkpoints. One of 3 execution strategies — see Execution Routing.
superpower-planning:subagent-driven	Execute plans in this session, sequentially via fresh subagents with two-stage review. One of 3 execution strategies — see Execution Routing.
superpower-planning:team-driven	Execute plans in this session, in parallel via Agent Team with dedicated reviewer. One of 3 execution strategies — see Execution Routing.
superpower-planning:parallel-agents	Run multiple subagents in parallel for independent tasks.
superpower-planning:tdd	Test-driven development: write tests first, then make them pass.
superpower-planning:debugging	Systematic debugging: reproduce, isolate, fix, verify.
superpower-planning:git-worktrees	Use git worktrees for parallel branch work without stashing.
superpower-planning:finishing-branch	Clean up and finalize a development branch before merge/PR.
superpower-planning:archiving	Archive completed plans, consolidate memory, and reset .planning/ for the next task.
superpower-planning:stashing	Pause unfinished work, save it into .planning/stash/, and support later resume with stale-findings check.
superpower-planning:requesting-review	Prepare and submit code for review with context and rationale.
superpower-planning:receiving-review	Process review feedback systematically and address all comments.
superpower-planning:verification	Verify work is complete and correct before declaring done.
superpower-planning:releasing	Bump versions, tag, and publish GitHub Releases with changelogs.
Stash / Resume Routing
When the user says they want to pause current unfinished work, switch projects, or come back later: use superpower-planning:stashing or /stash
When the user says they want to continue paused work, resume a previous project, or recover a stashed task: use /resume-stash
Resume must include a stale-findings check before execution continues
User Instructions

Instructions say WHAT, not HOW. "Add X" or "Fix Y" doesn't mean skip workflows.

Weekly Installs
9
Repository
sipengxie2024/s…planning
GitHub Stars
1
First Seen
Feb 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass