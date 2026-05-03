---
title: cook-fast
url: https://skills.sh/duc01226/easyplatform/cook-fast
---

# cook-fast

skills/duc01226/easyplatform/cook-fast
cook-fast
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill cook-fast
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Critical Thinking Mindset — Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence >80% to act. Anti-hallucination: Never present guess as fact — cite sources for every claim, admit uncertainty freely, self-check output for errors, cross-reference independently, stay skeptical of own confidence — certainty without evidence root of all hallucination.

AI Mistake Prevention — Failure modes to avoid on every task:

Check downstream references before deleting. Deleting components causes documentation and code staleness cascades. Map all referencing files before removal.
Verify AI-generated content against actual code. AI hallucinates APIs, class names, and method signatures. Always grep to confirm existence before documenting or referencing.
Trace full dependency chain after edits. Changing a definition misses downstream variables and consumers derived from it. Always trace the full chain.
Trace ALL code paths when verifying correctness. Confirming code exists is not confirming it executes. Always trace early exits, error branches, and conditional skips — not just happy path.
When debugging, ask "whose responsibility?" before fixing. Trace whether bug is in caller (wrong data) or callee (wrong handling). Fix at responsible layer — never patch symptom site.
Assume existing values are intentional — ask WHY before changing. Before changing any constant, limit, flag, or pattern: read comments, check git blame, examine surrounding code.
Verify ALL affected outputs, not just the first. Changes touching multiple stacks require verifying EVERY output. One green check is not all green checks.
Holistic-first debugging — resist nearest-attention trap. When investigating any failure, list EVERY precondition first (config, env vars, DB names, endpoints, DI registrations, data preconditions), then verify each against evidence before forming any code-layer hypothesis.
Surgical changes — apply the diff test. Bug fix: every changed line must trace directly to the bug. Don't restyle or improve adjacent code. Enhancement task: implement improvements AND announce them explicitly.
Surface ambiguity before coding — don't pick silently. If request has multiple interpretations, present each with effort estimate and ask. Never assume all-records, file-based, or more complex path.

Understand Code First — HARD-GATE: Do NOT write, plan, or fix until you READ existing code.

Search 3+ similar patterns (grep/glob) — cite file:line evidence
Read existing files in target area — understand structure, base classes, conventions
Run python .claude/scripts/code_graph trace <file> --direction both --json when .code-graph/graph.db exists
Map dependencies via connections or callers_of — know what depends on your target
Write investigation to .ai/workspace/analysis/ for non-trivial tasks (3+ files)
Re-read analysis file before implementing — never work from memory alone
NEVER invent new patterns when existing ones work — match exactly or document deviation

BLOCKED until: - [ ] Read target files - [ ] Grep 3+ patterns - [ ] Graph trace (if graph.db exists) - [ ] Assumptions verified with evidence

docs/project-reference/domain-entities-reference.md — Domain entity catalog, relationships, cross-service sync (read when task involves business entities/models) (content auto-injected by hook — check for [Injected: ...] header before reading)
docs/specs/ — Test specifications by module (read existing TCs; generate/update test specs via /tdd-spec after implementation)

Plan Quality — Every plan phase MUST ATTENTION include test specifications.

Add ## Test Specifications section with TC-{FEAT}-{NNN} IDs to every phase file
Map every functional requirement to ≥1 TC (or explicit TBD with rationale)
TC IDs follow TC-{FEATURE}-{NNN} format — reference by ID, never embed full content
Before any new workflow step: call TaskList and re-read the phase file
On context compaction: call TaskList FIRST — never create duplicate tasks
Verify TC satisfaction per phase before marking complete (evidence must be file:line, not TBD)

Mode: TDD-first → reference existing TCs with Evidence: TBD. Implement-first → use TBD → /tdd-spec fills after.

Rationalization Prevention — AI skips steps via these evasions. Recognize and reject:

Evasion	Rebuttal
"Too simple for a plan"	Simple + wrong assumptions = wasted time. Plan anyway.
"I'll test after"	RED before GREEN. Write/verify test first.
"Already searched"	Show grep evidence with file:line. No proof = no search.
"Just do it"	Still need TaskCreate. Skip depth, never skip tracking.
"Just a small fix"	Small fix in wrong location cascades. Verify file:line first.
"Code is self-explanatory"	Future readers need evidence trail. Document anyway.
"Combine steps to save time"	Combined steps dilute focus. Each step has distinct purpose.

Red Flag Stop Conditions — STOP and escalate to user via AskUserQuestion when:

Confidence drops below 60% on any critical decision
Changes would affect >20 files (blast radius too large)
Cross-service boundary is being crossed
Security-sensitive code (auth, crypto, PII handling)
Breaking change detected (interface, API contract, DB schema)
Test coverage would decrease after changes
Approach requires technology/pattern not in the project

NEVER proceed past a red flag without explicit user approval.

Skill Variant: Variant of /cook — fast implementation skipping research with minimal planning.

Quick Summary

Goal: Implement features quickly with minimal research and streamlined planning.

Workflow:

Scout — Quick codebase scan for patterns
Plan — Lightweight implementation plan
Implement — Execute with code-simplifier review

Key Rules:

Skip deep research; rely on codebase patterns
Still requires user approval before implementing
Break work into todo tasks; add final self-review task
Frontend/UI Context (if applicable)

When this task involves frontend or UI changes,

UI System Context — For ANY task touching .ts, .html, .scss, or .css files:

MUST ATTENTION READ before implementing:

docs/project-reference/frontend-patterns-reference.md — component base classes, stores, forms
docs/project-reference/scss-styling-guide.md — BEM methodology, SCSS variables, mixins, responsive
docs/project-reference/design-system/README.md — design tokens, component inventory, icons

Reference docs/project-config.json for project-specific paths.

Component patterns: docs/project-reference/frontend-patterns-reference.md
Styling/BEM guide: docs/project-reference/scss-styling-guide.md
Design system tokens: docs/project-reference/design-system/README.md

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Start working on these tasks immediately with minimal planning: $ARGUMENTS

Mode: FAST - Skip research, minimal planning, trust your knowledge.

Workflow
Quick Planning (skip research phase)
Analyze task requirements directly
Create minimal todo list with TaskCreate
NO researcher subagents, NO scout commands
For non-trivial tasks: write brief analysis to .ai/workspace/analysis/{task-name}.analysis.md before implementing.

Graph-Assisted Investigation — MANDATORY when .code-graph/graph.db exists.

HARD-GATE: MUST ATTENTION run at least ONE graph command on key files before concluding any investigation.

Pattern: Grep finds files → trace --direction both reveals full system flow → Grep verifies details

Task	Minimum Graph Action
Investigation/Scout	trace --direction both on 2-3 entry files
Fix/Debug	callers_of on buggy function + tests_for
Feature/Enhancement	connections on files to be modified
Code Review	tests_for on changed functions
Blast Radius	trace --direction downstream

CLI: python .claude/scripts/code_graph {command} --json. Use --node-mode file first (10-30x less noise), then --node-mode function for detail.

After implementing, run python .claude/scripts/code_graph connections <file> --json on modified files to verify no related files need updates.

Graph-Trace Quick Check

When graph DB is available, run a quick downstream trace before implementing:

python .claude/scripts/code_graph trace <file-to-modify> --direction downstream --json — fast check for downstream impact

Rapid Implementation

Use /code directly on tasks
Skip multi-step planning documents
Focus on working code over documentation

Quick Validation

Run type-check and compile
Manual spot-check over full test suite
Skip code-reviewer subagent

Commit (optional)

Ask user if ready to commit via AskUserQuestion
If yes, use /commit
When to Use
Simple features with clear requirements
Bug fixes with known solutions
Refactoring tasks
When user says "just do it"
Trade-offs
Aspect	Fast Mode	Full Mode
Research	Skipped	Multiple agents
Planning	Minimal	Full plan docs
Testing	Quick check	Full test suite
Review	Skipped	Code-reviewer
Speed	~2x faster	Thorough
Next Steps (Standalone: MUST ATTENTION ask user via AskUserQuestion. Skip if inside workflow.)

MANDATORY IMPORTANT MUST ATTENTION — NO EXCEPTIONS: If this skill was called outside a workflow, you MUST ATTENTION use AskUserQuestion to present these options. Do NOT skip because the task seems "simple" or "obvious" — the user decides:

"Proceed with full workflow (Recommended)" — I'll detect the best workflow to continue from here (feature implemented). This ensures review, testing, and docs steps aren't skipped.
"/code-simplifier" — Simplify and clean up implementation
"/workflow-review-changes" — Review changes before commit
"Skip, continue manually" — user decides

If already inside a workflow, skip — the workflow handles sequencing.

Closing Reminders
MANDATORY IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
MANDATORY IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
MANDATORY IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
MANDATORY IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
MANDATORY IMPORTANT MUST ATTENTION validate decisions with user via AskUserQuestion — never auto-decide
MANDATORY IMPORTANT MUST ATTENTION search 3+ existing patterns and read code BEFORE any modification. Run graph trace when graph.db exists.
MANDATORY IMPORTANT MUST ATTENTION include ## Test Specifications with TC IDs per phase. Call TaskList before creating new tasks.
MANDATORY IMPORTANT MUST ATTENTION follow ALL steps regardless of perceived simplicity. "Too simple to plan" is an evasion, not a reason.
MANDATORY IMPORTANT MUST ATTENTION STOP after 3 failed fix attempts. Report all attempts, ask user before continuing.
MANDATORY IMPORTANT MUST ATTENTION read frontend-patterns-reference, scss-styling-guide, design-system/README before any UI change.
MANDATORY IMPORTANT MUST ATTENTION run at least ONE graph command on key files when graph.db exists. Pattern: grep → graph trace → grep verify.
MUST ATTENTION apply critical thinking — every claim needs traced proof, confidence >80% to act. Anti-hallucination: never present guess as fact.
MUST ATTENTION apply AI mistake prevention — holistic-first debugging, fix at responsible layer, surface ambiguity before coding, re-read files after compaction.

[TASK-PLANNING] Before acting, analyze task scope and systematically break it into small todo tasks and sub-tasks using TaskCreate.

Weekly Installs
35
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