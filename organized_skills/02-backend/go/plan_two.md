---
rating: ⭐⭐⭐
title: plan-two
url: https://skills.sh/duc01226/easyplatform/plan-two
---

# plan-two

skills/duc01226/easyplatform/plan-two
plan-two
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill plan-two
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Understand Code First — HARD-GATE: Do NOT write, plan, or fix until you READ existing code.

Search 3+ similar patterns (grep/glob) — cite file:line evidence
Read existing files in target area — understand structure, base classes, conventions
Run python .claude/scripts/code_graph trace <file> --direction both --json when .code-graph/graph.db exists
Map dependencies via connections or callers_of — know what depends on your target
Write investigation to .ai/workspace/analysis/ for non-trivial tasks (3+ files)
Re-read analysis file before implementing — never work from memory alone
NEVER invent new patterns when existing ones work — match exactly or document deviation

BLOCKED until: - [ ] Read target files - [ ] Grep 3+ patterns - [ ] Graph trace (if graph.db exists) - [ ] Assumptions verified with evidence

Estimation — Modified Fibonacci: 1(trivial) → 2(small) → 3(medium) → 5(large) → 8(very large) → 13(epic, SHOULD split) → 21(MUST ATTENTION split). Output story_points and complexity in plan frontmatter. Complexity auto-derived: 1-2=Low, 3-5=Medium, 8=High, 13+=Critical.

Plan Quality — Every plan phase MUST ATTENTION include test specifications.

Add ## Test Specifications section with TC-{FEAT}-{NNN} IDs to every phase file
Map every functional requirement to ≥1 TC (or explicit TBD with rationale)
TC IDs follow TC-{FEATURE}-{NNN} format — reference by ID, never embed full content
Before any new workflow step: call TaskList and re-read the phase file
On context compaction: call TaskList FIRST — never create duplicate tasks
Verify TC satisfaction per phase before marking complete (evidence must be file:line, not TBD)

Mode: TDD-first → reference existing TCs with Evidence: TBD. Implement-first → use TBD → /tdd-spec fills after.

Iterative Phase Quality — Score complexity BEFORE planning.

Complexity signals: >5 files +2, cross-service +3, new pattern +2, DB migration +2 Score >=6 → MUST ATTENTION decompose into phases. Each phase:

≤5 files modified
≤3h effort
Follows cycle: plan → implement → review → fix → verify
Do NOT start Phase N+1 until Phase N passes VERIFY

Phase success = all TCs pass + code-reviewer agent approves + no CRITICAL findings.

docs/test-specs/ — Test specifications by module (read existing TCs to include test strategy in plan)

Skill Variant: Variant of /plan — creates two alternative implementation approaches for comparison.

Quick Summary

Goal: Research and create an implementation plan with 2 distinct approaches for the user to compare and choose.

Workflow:

Research — Deep investigation of the problem space
Approach A — Design first implementation approach with trade-offs
Approach B — Design alternative approach with trade-offs
Compare — Present side-by-side comparison for user decision

Key Rules:

PLANNING-ONLY: do not implement, only create comparison plan
Both approaches must be genuinely viable, not strawman vs real
Always offer /plan-review after plan creation

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Activate planning skill.

PLANNING-ONLY — Collaboration Required

DO NOT use the EnterPlanMode tool — you are ALREADY in a planning workflow. DO NOT implement or execute any code changes. COLLABORATE with the user: ask decision questions, present options with recommendations. After plan creation, ALWAYS run /plan-review to validate the plan. ASK user to confirm the plan before any next step.

Your mission

Use the planner subagent to create 2 detailed implementation plans for this following task: $ARGUMENTS

Workflow
First: Create a directory using naming pattern from ## Naming section in injected context. Make sure you pass the directory path to every subagent during the process.
Follow strictly to the "Plan Creation & Organization" rules of planning skill.
Use multiple researcher agents in parallel to research for this task, each agent research for a different aspect of the task and perform max 5 researches (max 5 tool calls).
Use scout agent to search the codebase for files needed to complete the task.
Main agent gathers all research and scout report filepaths, and pass them to planner subagent with the detailed instructions prompt to create an implementation plan of this task. Output: Provide at least 2 implementation approaches with clear trade-offs, and explain the pros and cons of each approach, and provide a recommended approach.
Main agent receives the implementation plan from planner subagent, and ask user to review the plan
Plan File Specification

Every plan.md MUST ATTENTION start with YAML frontmatter:

---
title: '{Brief title}'
description: '{One sentence for card preview}'
status: pending
priority: P2
story_points: { 1-21 modified fibonacci }
effort: { sum of phases, e.g., 4h }
branch: { current git branch }
tags: [relevant, tags]
created: { YYYY-MM-DD }
---

IMPORTANT Task Planning Notes (MUST ATTENTION FOLLOW)
Always plan and break work into many small todo tasks using TaskCreate
Always add a final review todo task to verify work quality and identify fixes/enhancements
MANDATORY FINAL TASKS: After creating all planning todo tasks, ALWAYS add these three final tasks:
Task: "Write test specifications for each phase" — Add ## Test Specifications with TC-{FEAT}-{NNN} IDs to every phase file. Use /tdd-spec if feature docs exist. Use Evidence: TBD for TDD-first mode.
Task: "Run /plan-validate" — Trigger /plan-validate skill to interview the user with critical questions and validate plan assumptions
Task: "Run /plan-review" — Trigger /plan-review skill to auto-review plan for validity, correctness, and best practices
Important Notes

IMPORTANT: Analyze the skills catalog and activate the skills that are needed for the task during the process. IMPORTANT: Sacrifice grammar for the sake of concision when writing reports. IMPORTANT: Ensure token efficiency while maintaining high quality. IMPORTANT: In reports, list any unresolved questions at the end, if any.

Post-Plan Validation

After plan creation, use the AskUserQuestion tool to ask: "Want me to run /plan-review to validate, or proceed to implementation?" with options:

"Run /plan-review (Recommended)" — Execute /plan-review to validate the plan
"Proceed to implementation" — Skip validation and start implementing
REMINDER — Planning-Only Command

DO NOT use EnterPlanMode tool. DO NOT start implementing. ALWAYS validate with /plan-review after plan creation. ASK user to confirm the plan before any implementation begins. ASK user decision questions with your recommendations when multiple approaches exist.

Next Steps (Standalone: MUST ATTENTION ask user via AskUserQuestion. Skip if inside workflow.)

MANDATORY IMPORTANT MUST ATTENTION — NO EXCEPTIONS: If this skill was called outside a workflow, you MUST ATTENTION use AskUserQuestion to present these options. Do NOT skip because the task seems "simple" or "obvious" — the user decides:

"Proceed with full workflow (Recommended)" — I'll detect the best workflow to continue from here (plan created). This ensures review, validation, implementation, and testing steps aren't skipped.
"/plan-review" — Auto-review plan for validity and best practices
"/plan-validate" — Interview user to confirm plan decisions
"Skip, continue manually" — user decides

If already inside a workflow, skip — the workflow handles sequencing.

Closing Reminders
IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
IMPORTANT MUST ATTENTION include Test Specifications section and story_points in plan frontmatter
IMPORTANT MUST ATTENTION search 3+ existing patterns and read code BEFORE any modification. Run graph trace when graph.db exists.
IMPORTANT MUST ATTENTION include story_points and complexity in plan frontmatter. SP > 8 = split.
IMPORTANT MUST ATTENTION include ## Test Specifications with TC IDs per phase. Call TaskList before creating new tasks.
IMPORTANT MUST ATTENTION score complexity first. Score >=6 → decompose. Each phase: plan → implement → review → fix → verify. No skipping.
Weekly Installs
34
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass