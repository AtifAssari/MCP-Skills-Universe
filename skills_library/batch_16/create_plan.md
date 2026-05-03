---
title: create-plan
url: https://skills.sh/darraghh1/my-claude-setup/create-plan
---

# create-plan

skills/darraghh1/my-claude-setup/create-plan
create-plan
Installation
$ npx skills add https://github.com/darraghh1/my-claude-setup --skill create-plan
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Create Complete Plan — Solo Session

Create a complete plan with phases for: $ARGUMENTS

Current Plans

Existing plans in the repository (avoid naming conflicts):

!ls plans/ 2>/dev/null || echo "(no plans directory yet)"

Architecture

This skill runs as a solo session — you do everything directly with full 1M context. No subagents, no teams, no delegation. You read templates, explore the codebase, create plan artifacts, self-review, and fix issues — all in one session.

Step 1: Clarify Requirements

The user has experienced 20-phase plans built on wrong assumptions — hours of work discarded because a 30-second question wasn't asked upfront. Clarification prevents this waste.

Read the task description above. If anything is ambiguous or underspecified, use AskUserQuestion to clarify before proceeding.

Questions to ask if not clear from the description:

Problem: What specific problem are we solving? What pain point does this address?
Scope: Is this a small feature, medium enhancement, or major system?
Users: Who uses this feature? (specific roles, account types)
Integrations: Does this connect to external services or APIs?
Data: What data does this create, read, update, or delete?
UI: Where does this appear in the app? New page, existing page, component?

If the description says "add voice commands" but doesn't specify which commands, ASK. If it says "improve performance" but doesn't specify what's slow, ASK. The user prefers a brief clarification dialogue over assumptions that lead to rework.

Step 2: Explore Codebase

Before estimating complexity or designing phases, ground yourself in the actual code. This prevents plans built on assumptions instead of code reality.

Use Glob, Grep, and Read to explore:

Affected Files/Modules — which files and directories will likely need changes
Existing Patterns — naming conventions, file structure, import patterns in those areas
Reusable Components — services, components, utilities that already exist and can be leveraged
Integration Points — where the new feature connects to existing code (routes, services, database tables)
Potential Conflicts — areas of complexity, recent changes that might complicate implementation

Keep notes concise. Focus on facts from the code, not assumptions.

Step 3: Read Templates

Read both templates — you'll need them for creating plan.md and phase files:

Read: ${CLAUDE_SKILL_DIR}/references/PLAN-TEMPLATE.md
Read: ${CLAUDE_SKILL_DIR}/references/PHASE-TEMPLATE.md

Step 4: Create plan.md

Create the plan folder and plan.md following the template structure.

Folder naming: plans/{YYMMDD}-{feature-name}/

Plan.md must include:

Executive Summary (mission, big shift, primary deliverables)
Phasing Strategy with Phase Table (status, title, skill, group, dependencies)
Group Summary table (groups, their phases, descriptions)
Architectural North Star
Security Requirements
Decision Log

GROUPING (critical for implementation):

Connected phases that build the same feature/component MUST share a group: name
Set group: in each phase's frontmatter (e.g., group: "auth-system")
Include a Group Summary table in plan.md showing groups, their phases, and descriptions
Order groups so dependencies flow top-to-bottom (group A before group B if B needs A)
Single-phase groups are valid for standalone work
Groups define implementation session boundaries — one /implement session per group
User Checkpoint 1

Show the user the plan summary — executive summary, phase breakdown, group structure, architecture decisions.

Ask for approval/feedback using AskUserQuestion:

Approved: Continue to Step 5
Changes needed: Revise plan.md and re-present
Step 5: Create Phase Files

Create all phase files following the PHASE-TEMPLATE.md structure. Each phase must include:

Frontmatter (title, description, skill, status, group, dependencies)
Goal and context
Implementation steps with code blocks grounded in codebase patterns (read real files before writing code blocks)
Acceptance criteria
Testing requirements (TDD — tests come first)
Files to create/modify

Phase sizing: 5-8 medium phases > 30 small phases. Each phase should be a coherent unit of work (service + actions + tests), not a micro-slice.

User Checkpoint 2

Show the user the full phase breakdown — titles, skills, groups, dependencies.

Ask for approval/feedback:

Approved: Continue to Step 6
Changes needed: Revise phases and re-present
Step 6: Flow Audit (3+ Phases)

For plans with 3 or more phases, run a structural flow audit BEFORE per-phase reviews. This catches design-level issues (circular dependencies, wrong ordering, incoherent data flow) that would invalidate all review work if discovered later.

Skip this step for 1-2 phase plans (too small for flow issues).

/audit-plan plans/{YYMMDD}-{feature-name}


Gate logic:

Overall Assessment	Action
"Unusable"	HARD BLOCK: Fix structural issues, re-audit
"Major Restructuring Needed"	HARD BLOCK: Fix issues, re-audit
"Significant Issues"	SOFT BLOCK: Show user, ask whether to proceed or fix
"Minor Issues" or "Coherent"	PROCEED to Step 7
Step 7: Self-Review

Review plan.md and each phase file sequentially using /review-plan.

For plan.md:

/review-plan plans/{YYMMDD}-{feature-name}


For each phase:

/review-plan plans/{YYMMDD}-{feature-name} phase 01
/review-plan plans/{YYMMDD}-{feature-name} phase 02
...


Fix any Critical/High issues found during review. Medium issues — use your judgment.

Step 8: Report Summary

Report to the user:

Folder location: plans/{YYMMDD}-{feature-name}/
Files created:
plan.md
phase-01-.md through phase-NN-.md
reviews/planning/ folder with review files
Review status:
Plan.md: template score (X/11)
Each phase: template score (X/12) + codebase score (N issues by severity)
Flow audit (3+ phases): overall assessment + Critical/High issue count
Overall verdict: Ready/Not Ready for implementation
Critical issues (if any) that need addressing before implementation
Resuming After Context Compact

If you notice context was compacted or you're unsure of current progress:

Run TaskList to see all tasks and their status
Find the in_progress task — that's where you were
Run TaskGet {id} on that task to read full details
Read plan.md to get the Phase Table for broader context
Continue from the in_progress step — don't restart from Step 1
Error Breakout Conditions

STOP and report to user if:

Flow audit returns "Unusable" and you cannot restructure
Review FAIL repeats 3+ times on the same file
Cannot resolve Critical review issues
User requests cancellation
Context window approaching limit with no clear path forward

Do not continue when blocked. Report and let the user decide.

Patterns That Prevent User-Reported Failures

The user experienced each of these failures. Understanding the harm helps you avoid them:

Pattern to Avoid	Harm When Ignored
Skipping requirements clarification	Wrong plan built on false premises, hours of wasted effort
Skipping user checkpoints	User discovers wrong assumptions after all phases are written
Writing code blocks without reading codebase	Phases contain wrong patterns, caught late during implementation
Single-file micro-phases (too granular)	Excessive overhead — 30 phases for a medium feature wastes review/audit cycles
Folder without date prefix	Folders become unsorted chronologically
Skipping TaskList check after compact	Duplicates work if resuming
Template Locations
Plan: references/PLAN-TEMPLATE.md
Phase: references/PHASE-TEMPLATE.md
Weekly Installs
23
Repository
darraghh1/my-cl…de-setup
GitHub Stars
44
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn