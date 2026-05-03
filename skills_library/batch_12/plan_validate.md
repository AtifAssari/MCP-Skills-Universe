---
title: plan-validate
url: https://skills.sh/duc01226/easyplatform/plan-validate
---

# plan-validate

skills/duc01226/easyplatform/plan-validate
plan-validate
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill plan-validate
SKILL.md

[BLOCKING] This skill MUST ATTENTION use AskUserQuestion to interview the user. Completing without asking at least one question is a violation.

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

Plan Quality — Every plan phase MUST ATTENTION include test specifications.

Add ## Test Specifications section with TC-{FEAT}-{NNN} IDs to every phase file
Map every functional requirement to ≥1 TC (or explicit TBD with rationale)
TC IDs follow TC-{FEATURE}-{NNN} format — reference by ID, never embed full content
Before any new workflow step: call TaskList and re-read the phase file
On context compaction: call TaskList FIRST — never create duplicate tasks
Verify TC satisfaction per phase before marking complete (evidence must be file:line, not TBD)

Mode: TDD-first → reference existing TCs with Evidence: TBD. Implement-first → use TBD → /tdd-spec fills after.

External Memory: For complex or lengthy work (research, analysis, scan, review), write intermediate findings and final results to a report file in plans/reports/ — prevents context loss and serves as deliverable.

Evidence Gate: MANDATORY IMPORTANT MUST ATTENTION — every claim, finding, and recommendation requires file:line proof or traced evidence with confidence percentage (>80% to act, <80% must verify first).

Quick Summary

Goal: Interview the user with critical questions to validate assumptions and surface issues in a plan before coding begins.

Workflow:

Read Plan — Parse plan.md and phase files for decisions, assumptions, risks
Extract Topics — Scan for architecture, assumptions, tradeoffs, risks, scope keywords
Generate Questions — Formulate concrete questions with 2-4 options each
Interview User — Present questions using configured count range
Document Answers — Add Validation Summary section to plan.md

Key Rules:

Only ask about genuine decision points; don't manufacture artificial choices
Prioritize questions that could change implementation significantly
Do NOT modify phase files; just document what needs updating

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Your mission

Interview the user with critical questions to validate assumptions, confirm decisions, and surface potential issues in an implementation plan before coding begins.

Plan Resolution
If $ARGUMENTS provided -> Use that path
Else check ## Plan Context section -> Use active plan path
If no plan found -> Ask user to specify path or run /plan-hard first
Configuration (from injected context)

Check ## Plan Context section for validation settings:

mode - Controls auto/prompt/off behavior
questions - Range like 3-8 (min-max)

These values are automatically injected from user config. Use them as constraints.

Workflow
Step 1: Read Plan Files

Read the plan directory:

plan.md - Overview and phases list
phase-*.md - All phase files
Look for decision points, assumptions, risks, tradeoffs
Step 2: Extract Question Topics

Scan plan content for:

Category	Keywords to detect
Architecture	"approach", "pattern", "design", "structure", "database", "API"
Assumptions	"assume", "expect", "should", "will", "must", "default"
Tradeoffs	"tradeoff", "vs", "alternative", "option", "choice", "either/or"
Risks	"risk", "might", "could fail", "dependency", "blocker", "concern"
Scope	"phase", "MVP", "future", "out of scope", "nice to have"
New Tech/Lib	"install", "add package", "new dependency", "npm install", "dotnet add", framework names not in project
Test Specs	"TC-", "test case", "coverage", "TDD", "test specification", "test spec"
Step 3: Generate Questions

For each detected topic, formulate a concrete question:

Question format rules:

Each question must have 2-4 concrete options
Mark recommended option with "(Recommended)" suffix
Include "Other" option is automatic - don't add it
Questions should surface implicit decisions

Example questions:

Category: Architecture
Question: "How should the validation results be persisted?"
Options:
1. Save to plan.md frontmatter (Recommended) - Updates existing plan
2. Create validation-answers.md - Separate file for answers
3. Don't persist - Ephemeral validation only

Category: Assumptions
Question: "The plan assumes API rate limiting is not needed. Is this correct?"
Options:
1. Yes, rate limiting not needed for MVP
2. No, add basic rate limiting now (Recommended)
3. Defer to Phase 2

Step 4: Interview User

Use AskUserQuestion tool to present questions.

Rules:

Use question count from ## Plan Context -> Validation: mode=X, questions=MIN-MAX
Group related questions when possible (max 4 questions per tool call)
Focus on: assumptions, risks, tradeoffs, architecture
Step 5: Document Answers

After collecting answers, update the plan:

Add ## Validation Summary section to plan.md:
## Validation Summary

**Validated:** {date}
**Questions asked:** {count}

### Confirmed Decisions

- {decision 1}: {user choice}
- {decision 2}: {user choice}

### Action Items

- [ ] {any changes needed based on answers}

If answers require plan changes, note them but do not modify phase files - just document what needs updating.
Output

After validation completes, provide summary:

Number of questions asked
Key decisions confirmed
Any items flagged for plan revision
Recommendation: proceed to implementation or revise plan first
IMPORTANT Task Planning Notes (MUST ATTENTION FOLLOW)
Always plan and break work into many small todo tasks using TaskCreate
Always add a final review todo task to verify work quality and identify fixes/enhancements
MANDATORY FINAL TASKS: After creating all planning todo tasks, ALWAYS add these two final tasks:
Task: "Run /plan-validate" — Trigger /plan-validate skill to interview the user with critical questions and validate plan assumptions
Task: "Run /plan-review" — Trigger /plan-review skill to auto-review plan for validity, correctness, and best practices
Important Notes

IMPORTANT: Only ask questions about genuine decision points - don't manufacture artificial choices. IMPORTANT: If plan is simple with few decisions, it's okay to ask fewer than min questions. IMPORTANT: Prioritize questions that could change implementation significantly. MANDATORY IMPORTANT MUST ATTENTION If plan introduces new tech/packages/libraries, ask user: "Plan uses {lib}. Were alternatives evaluated? Confirm choice or research more?"

Next Steps

MANDATORY IMPORTANT MUST ATTENTION — NO EXCEPTIONS after completing this skill, you MUST ATTENTION use AskUserQuestion to present these options. Do NOT skip because the task seems "simple" or "obvious" — the user decides:

"/cook (Recommended)" — Begin implementation with validated plan
"/refine" — If plan needs PBI refinement first
"Skip, continue manually" — user decides
Closing Reminders

MANDATORY IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting. MANDATORY IMPORTANT MUST ATTENTION validate decisions with user via AskUserQuestion — never auto-decide. MANDATORY IMPORTANT MUST ATTENTION add a final review todo task to verify work quality. MANDATORY IMPORTANT MUST ATTENTION READ the following files before starting:

IMPORTANT MUST ATTENTION search 3+ existing patterns and read code BEFORE any modification. Run graph trace when graph.db exists.
IMPORTANT MUST ATTENTION include ## Test Specifications with TC IDs per phase. Call TaskList before creating new tasks.
Weekly Installs
39
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