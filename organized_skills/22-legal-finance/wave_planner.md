---
rating: ⭐⭐
title: wave-planner
url: https://skills.sh/asm3r96/wave-driven-dev/wave-planner
---

# wave-planner

skills/asm3r96/wave-driven-dev/wave-planner
wave-planner
Installation
$ npx skills add https://github.com/asm3r96/wave-driven-dev --skill wave-planner
SKILL.md
Wave Planner

Create and run a Wave-Driven Development plan for large, cross-stack tasks.

Objective

Produce:

Vision and scope boundaries
Decision Log
Wave 0 contracts
Wave 1..N parallel implementation waves
Integration wave
Final verification wave
Documentation update step
Ready-to-send worker prompts and execution checklist
Workflow
Decide whether to use this skill:
Use only if work is large, multi-step, and touches multiple parts/stacks.
If not large enough, do not use this skill.
Ask for Gate 1 user approval before planning:
Send a short reason: "I recommend Wave method because . Do you agree?"
Stop until user accepts or declines.
If accepted, draft the plan:
Clarify done criteria and out-of-scope.
Build Decision Log (naming, API shape, error model, logging, tests, style constraints).
Define Wave 0 contracts first (types/interfaces/schemas, boundaries, API shapes, constants, flags/migrations).
Choose wave and agent count with balancing rules:
Use the minimum number of waves that still avoids conflicts.
Group independent tasks into the same wave.
Move dependency-bound tasks to later waves.
Keep each worker task medium-sized (not tiny and not overloaded).
Ensure each worker has explicit file/module ownership.
Produce a one-line execution preview before full detail:
One line per wave.
One line per worker with task summary.
Produce the full plan with complete shared context:
Include full vision and all waves so each worker sees global intent.
Include worker-specific goals, files, constraints, and verification.
Include explicit wave order for execution (Wave 0, then Wave 1..N, then Integration, then Final Verification, then Docs).
Ask for Gate 2 user approval before execution:
"Plan is ready. Execute now?"
Stop until user accepts or declines.
If accepted, load and use acpx skill, then execute:
Use acpx to create/run named sessions per worker in current wave.
Run workers in parallel inside a wave, but execute waves sequentially.
Wait for all workers in wave to finish and validate handoffs before next wave.
Close worker sessions after completion.
After all waves:
Main agent reviews merged result and runs verification tests.
Main agent updates existing docs if needed, or adds new docs for new features.
Follow existing documentation format and conventions.
Global Rules
Gating rule: planning and execution require explicit user approvals (Gate 1 and Gate 2).
Ownership rule: workers edit only assigned files.
Dependency rule: if outside scope is needed, return a Dependency Note instead of editing.
Consistency rule: follow existing repo patterns; do not invent new architecture unless requested.
Verifiability rule: each worker includes at least one concrete verification method.
Ordering rule: wave order is strict; do not start next wave early.
Session rule: one named session per worker; close finished sessions.
Docs rule: docs update is mandatory in final step (update existing docs or add new).
Model Routing Configuration

Read templates/model-routing.md before choosing models.

Rules:

Classify each worker task as hard, middle, or easy.
Select the first available model from that class's ordered list.
If a model fails/unavailable, fallback to the next model in order.
If placeholder guidance still exists in routing config, stop and tell user to edit routing first.
Mandatory Worker Handoff Format
Summary (1-3 lines)
Files changed (exact list)
Patch/diffs (or exact edits)
How to test (commands + expected result)
Risks/TODOs/Dependency Notes
Main plan log entry (what to append to shared execution log)
Completion marker: WAVE {WAVE_ID} / {AGENT_NAME} DONE
Output Contract

Always output the final plan using this section order:

A) Vision
B) Decision Log
C) Contracts (Wave 0)
D) Waves (1..N with agents)
E) Integration + Final Verification + Docs
F) Worker prompts
G) Execution checklist (acpx sessions + wave order)

Use templates from templates/ when helpful.

Weekly Installs
9
Repository
asm3r96/wave-driven-dev
GitHub Stars
1
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass