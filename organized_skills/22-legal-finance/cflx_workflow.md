---
rating: ⭐⭐⭐
title: cflx-workflow
url: https://skills.sh/tumf/cflx-skills/cflx-workflow
---

# cflx-workflow

skills/tumf/cflx-skills/cflx-workflow
cflx-workflow
Installation
$ npx skills add https://github.com/tumf/cflx-skills --skill cflx-workflow
SKILL.md
Conflux Workflow Executor

Execute Conflux workflow operations autonomously. Called by orchestration system, not for direct human use.

CRITICAL: This skill CANNOT ask questions to users. All decisions must be made autonomously based on available context.

Operation Modes

This skill supports three operations, determined by the orchestrator's invocation:

apply - Implement an approved change
accept - Verify implementation against specs
archive - Finalize a deployed change
Operation Selection

The orchestrator specifies the operation. Parse the invocation to determine:

If change ID with "apply" or "implement" context → Execute Apply
If "accept" or "review" context → Execute Accept
If "archive" context → Execute Archive
Operation 1: Apply (Implementation)

Purpose: Implement an approved change autonomously with task tracking.

CRITICAL CONSTRAINTS:

NO QUESTIONS - Make autonomous decisions based on available context
NO DEFERRAL - Do not defer tasks based on difficulty or complexity
IMMEDIATE UPDATES - Update tasks.md after EVERY completed task
COMPLETE ALL TRUTHFULLY - A task may be marked [x] only when the corresponding repository change and required verification actually exist
ESCALATE BLOCKERS - If implementation is impossible, record an Implementation Blocker for acceptance review
NO CHECKLIST-ONLY COMPLETION - Do not mark implementation tasks complete based only on proposal/spec/tasks edits when the task requires code, tests, or runtime wiring
Execution Steps

Read Proposal

python3 "$SKILL_ROOT/scripts/cflx.py" show <change-id>

Read openspec/changes/<id>/proposal.md
Read openspec/changes/<id>/design.md (if exists)
Read openspec/changes/<id>/tasks.md

Work Through Tasks Sequentially

Start with first uncompleted task
Implement the change
Run verification (build/test/lint)
Mark task as [x] in tasks.md immediately after the implementation and verification evidence exist
Proceed to next task

Handle Ambiguity Autonomously

Use existing code patterns as reference
Make reasonable assumptions
Document decisions in code comments
Prefer simpler solutions

Update Progress Continuously

Update tasks.md after each task
Never batch updates
Keep progress visible

Verify Completion

Ensure all tasks are [x] or in Future Work
Run final validation
Confirm integration points
Truthful Completion Rules

Before changing any task to [x], verify all applicable conditions below are true:

The repository contains the required implementation artifact for that task.
Code task -> matching src/, app, config, or script diff exists.
Test task -> matching tests/ diff exists.
Wiring/integration task -> real entrypoint/call-site/config hookup exists.
Spec-only task -> it is explicitly documentation/spec work rather than implementation work.
The artifact is reachable from the intended flow when the task claims runtime integration.
The relevant verification command has been run successfully, or concrete blocker evidence has been recorded.
The task description still matches reality. If the task is too broad or ambiguous, refine it before completion.

Never mark a task complete based only on any of the following:

openspec/ files were updated
tasks.md was normalized
a proposal was archived or merged
code was discussed but no runtime/test artifact was added
a stub placeholder was added where a real execution path was required
Task Management

Move to Future Work ONLY if:

Requires human decision-making or judgment
Requires external system access outside repository
Requires long-wait verification (>1 day)
Already marked with '(future work)'

Do NOT move to Future Work:

Difficult or complex tasks (agent must attempt)
Tests (unit/integration/e2e)
Linting/formatting
Documentation updates
Any automatable task
Checkbox Rules

Active sections: Must have checkboxes - [ ] or - [x]

Excluded sections (Future Work, Out of Scope, Notes): Must NOT have checkboxes

## Implementation Tasks
- [x] Completed task
- [ ] Pending task

## Future Work
- Manual verification required
- External deployment needed

Mock-First Policy
Mock external dependencies when possible
Do not block on missing API keys/credentials
Implement stub/fixture for external services
Only truly non-mockable dependencies go to Future Work
Implementation Blocker Escalation

If apply determines the change is currently impossible to implement (for example: spec contradiction, non-mockable external limitation, or policy constraint), do not loop blindly.

Add a new section to openspec/changes/<change-id>/tasks.md:
## Implementation Blocker #<n>
- category: <spec_contradiction|external_non_mockable|policy_constraint|other>
- summary: <one-line human-facing blocker summary>
- evidence:
   - <file/path:line or concrete command output>
- impact: <what cannot be completed>
- unblock_actions:
   - <specific follow-up action 1>
   - <specific follow-up action 2>
- owner: <team_or_role>
- decision_due: <YYYY-MM-DD>

The blocker section is human-facing and MUST NOT use checkboxes.
Output a machine-readable marker at the end of apply output:
IMPLEMENTATION_BLOCKER:
category: <...>
tasks_section: "Implementation Blocker #<n>"
human_action_required: see openspec/changes/<change-id>/tasks.md#implementation-blocker-<n>

Keep evidence concrete and actionable so acceptance can judge whether loop stop is warranted.
Apply Completion Criteria
All tasks marked [x] or moved to Future Work (without checkboxes)
Code compiles/builds successfully
Tests pass
Lint passes
Integration points verified
Any task that claims implementation, runtime behavior, or entrypoint wiring has corresponding non-OpenSpec evidence in the repo
Changes that are spec-only MUST leave implementation tasks unchecked or blocked; they must not be represented as completed implementation

For detailed guidance, read references/cflx-apply.md.

Operation 2: Accept (Acceptance Review)

Purpose: Verify implementation meets specifications with automated checks.

CRITICAL: Output exactly ONE verdict at the end.

Required Checks

Git Working Tree Clean

git status --porcelain

Must output empty (no uncommitted changes)
If dirty, output FAIL with all changed files

Task Completion

All tasks marked [x] or in Future Work section
No checkboxes in excluded sections
Reject any task marked [x] without corresponding repo evidence

Spec Matching

Implementation matches specification in specs/
All scenarios are satisfied

Integration Check

Feature is executed in real flow
Called from CLI/TUI/API as specified

Dead Code Check

All implemented code is invoked
No orphan functions/classes

Regression Check

Existing features still work
No unintended side effects

Evidence Citation

Cite file path + function/method for integration
Provide concrete verification evidence

Checklist Truthfulness Check

FAIL if tasks.md claims completion but the corresponding code/tests/entrypoints do not exist
FAIL if a change was archived/spec-promoted while implementation tasks were marked complete without repository evidence
FAIL if the only evidence for an implementation task is openspec/ edits
Output Format

Output exactly ONE of these at the end:

PASS:

ACCEPTANCE: PASS


FAIL:

ACCEPTANCE: FAIL

FINDINGS:
1. [file:line] Description of issue
2. [file:line] Description of issue
...


Then update tasks.md with:

## Acceptance #N Failure Follow-up

- [ ] Fix issue 1
- [ ] Fix issue 2


CONTINUE (only if verification incomplete):

ACCEPTANCE: CONTINUE


BLOCKED (when blocker escalation is valid):

ACCEPTANCE: BLOCKED

BLOCKER:
- category: <...>
- reason: <short rationale>
- evidence: <file/path:line or command evidence>

Recommended:
- summary: <one-line human-facing blocker summary>
- unblock_actions:
  - <specific follow-up action 1>
  - <specific follow-up action 2>

Accept Rules
Each finding must include concrete evidence (file path, function, line)
Each finding must be actionable by AI agent
Missing secrets MUST NOT cause CONTINUE if mocking is possible
Dirty working tree is always FAIL
ACCEPTANCE: BLOCKED is allowed only when a valid Implementation Blocker #<n> exists with concrete evidence and unblock actions
If blocker data is weak, speculative, or fixable within repo scope, return FAIL instead of BLOCKED

For detailed guidance, read references/cflx-accept.md.

Operation 3: Archive

Purpose: Archive deployed change and update canonical specs.

Execution Steps

Identify Change ID

From orchestrator invocation
Or from context (must be unambiguous)

Validate Change Status

python3 "$SKILL_ROOT/scripts/cflx.py" list
python3 "$SKILL_ROOT/scripts/cflx.py" show <id>

Ensure change exists
Ensure not already archived
Ensure ready for archive

Run Archive

python3 "$SKILL_ROOT/scripts/cflx.py" archive <id> --yes

Use --skip-specs only for tooling-only changes

Verify Results

Confirm moved to changes/archive/
Confirm specs updated
python3 "$SKILL_ROOT/scripts/cflx.py" validate --strict

Archive Completion Criteria
Change moved to openspec/changes/archive/<id>/
Canonical specs updated (unless --skip-specs)
Validation passes with --strict

For detailed guidance, read references/cflx-archive.md.

Built-in Tools
# List changes
python3 "$SKILL_ROOT/scripts/cflx.py" list

# List specs
python3 "$SKILL_ROOT/scripts/cflx.py" list --specs

# Show change details
python3 "$SKILL_ROOT/scripts/cflx.py" show <id>

# Show JSON output
python3 "$SKILL_ROOT/scripts/cflx.py" show <id> --json

# Show deltas only
python3 "$SKILL_ROOT/scripts/cflx.py" show <id> --json --deltas-only

# Validate change
python3 "$SKILL_ROOT/scripts/cflx.py" validate <id> --strict

# Validate all
python3 "$SKILL_ROOT/scripts/cflx.py" validate --strict

# Archive change
python3 "$SKILL_ROOT/scripts/cflx.py" archive <id> --yes

# Archive without spec updates
python3 "$SKILL_ROOT/scripts/cflx.py" archive <id> --yes --skip-specs

Autonomous Decision Framework

When facing ambiguous situations, follow this priority:

Existing patterns - Follow patterns in the codebase
Specification - Refer to spec deltas and scenarios
Simplicity - Choose simpler implementation
Documentation - Document decision in code comments

Never:

Ask user for clarification
Stop and wait for input
Leave tasks incomplete due to uncertainty
Task Format Requirements

Valid:

- [ ] Task description
- [x] Completed task
1. [ ] Numbered task


Invalid (must fix):

## N. Task              → - [ ] N. Task
- Task                 → - [ ] Task
1. Task                → 1. [ ] Task


If 0/0 tasks detected, fix format first.

Error Handling
Validation Failure
Parse error messages
Fix identified issues
Re-run validation
Repeat until passing
Build/Test Failure
Analyze error output
Fix code issues
Re-run verification
Update tasks on success
Incomplete Information
Make reasonable assumption
Implement based on assumption
Document assumption in code
Continue with next task
Reference Files

Detailed operation guides:

references/cflx-apply.md - Apply operation details
references/cflx-accept.md - Accept operation details
references/cflx-archive.md - Archive operation details
Summary
Operation	Trigger	Output	Constraints
Apply	"apply "	Completed tasks + code	No questions, update immediately
Accept	"accept"	PASS/FAIL/CONTINUE/BLOCKED	Output once, cite evidence
Archive	"archive "	Archived change	Validate before/after

REMEMBER: This skill operates autonomously. Never ask questions. Make decisions based on available context.

Weekly Installs
10
Repository
tumf/cflx-skills
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass