---
title: subagent-driven-development
url: https://skills.sh/izyanrajwani/agent-skills-library/subagent-driven-development
---

# subagent-driven-development

skills/izyanrajwani/agent-skills-library/subagent-driven-development
subagent-driven-development
Installation
$ npx skills add https://github.com/izyanrajwani/agent-skills-library --skill subagent-driven-development
SKILL.md
Subagent-Driven Development

Dispatch fresh subagent per task with two-stage review after each.

Core principle: Fresh subagent per task + two-stage review (spec then quality) + diff-based validation = high quality, fast iteration

Quick Reference
Phase	Actor	Action	Exit Condition
1	Controller	Read plan, extract tasks, capture BASE_SHA, create task list	All tasks tracked with BASE_SHA
2	Subagent	Implement (templates/implementer.md)	Commit exists + tests pass + report includes HEAD_SHA
3	Subagent	Spec review (templates/spec-reviewer.md)	Reviewer checked diff(BASE..HEAD) and returned ✅ or file:line issues
4	Subagent	Quality review (templates/code-quality-reviewer.md)	Reviewer approved diff or returned severity-tagged issues
5	Controller	Update state, mark complete, loop to step 2	All tasks done
6	Subagent	Final review of entire implementation	Approved
7	Controller	Use finishing-a-development-branch	Branch complete
Task Contract

Every task must satisfy these constraints:

Scope:

One task = one commit (or tight commit stack)
No drive-by refactors; no formatting churn
No unrelated file changes

Verification:

All tests pass (run full suite or affected subset)
Lint/typecheck pass (if applicable)
Commands actually executed (not assumed)

Report must include:

BASE_SHA (from controller)
HEAD_SHA (after commit)
Commands run (exact, copy-pasteable)
Test output summary (pass/fail + counts)
Files changed (list)
Scope confirmation ("No unrelated changes")
State Tracking

Controller maintains per-task record:

{
  task_id: string,
  base_sha: string,      # Captured before implementer starts
  head_sha: string,      # From implementer report after commit
  status: pending|in_progress|spec_review|quality_review|complete,
  spec_review_cycles: number,
  quality_review_cycles: number
}


Update state after each phase transition.

Process
Setup (Once)
Read plan file once
Extract all tasks with full text and context
Capture current HEAD as BASE_SHA for first task
Create task list with all tasks (status: pending)
Per Task Loop
Record BASE_SHA for this task (current HEAD)
Dispatch implementer with full task text + context + BASE_SHA
If questions: Answer completely, re-dispatch with answers
Implementer completes: implements, tests, commits, reports HEAD_SHA
Update state: Record HEAD_SHA, set status to spec_review
Dispatch spec reviewer with task requirements + diff(BASE_SHA..HEAD_SHA)
If spec issues: Implementer fixes → spec reviewer re-reviews → increment cycle count → repeat until ✅
Update state: Set status to quality_review
Dispatch code quality reviewer with BASE_SHA, HEAD_SHA
If quality issues: Implementer fixes → quality reviewer re-reviews → increment cycle count → repeat until ✅
Update state: Set status to complete, BASE_SHA for next task = current HEAD_SHA
Completion
Dispatch final code reviewer for entire implementation (first BASE_SHA to final HEAD_SHA)
Use finishing-a-development-branch skill
Prompt Templates
templates/implementer.md — Implementation subagent
templates/spec-reviewer.md — Spec compliance verification (diff-based)
templates/code-quality-reviewer.md — Code quality assessment (diff-based)

See references/example-workflow.md for complete walkthrough with SHA tracking.

Red Flags

Never:

Skip reviews (spec compliance OR code quality)
Proceed with unfixed issues
Dispatch parallel implementers in same working tree (conflicts)
Make subagent read plan file (provide full text)
Skip BASE_SHA/HEAD_SHA tracking
Let reviewers assess "the repo" instead of the specific diff
Accept reports without required fields (SHA, commands, test output)

Parallel clarification: "Parallel sessions" (separate branches/worktrees) is fine via executing-plans. "Parallel implementers" touching same working tree is forbidden.

If subagent asks questions: Answer clearly and completely before they proceed.

If reviewer finds issues: Implementer fixes → reviewer re-reviews specific diff → repeat until approved.

If implementer discovers required refactor: Stop, report to controller, request plan amendment. Don't bulldoze.

Dependencies

Requires: writing-plans (creates the plan)

Subagents use: test-driven-development, requesting-code-review (template)

Completes with: finishing-a-development-branch

Alternative: executing-plans (for parallel sessions/branches, not parallel implementers)

Environment notes: This skill assumes availability of: git (for SHA tracking), a task list tool (TodoWrite or equivalent), and ability to dispatch subagents. Adapt tool names to your environment.

Weekly Installs
70
Repository
izyanrajwani/ag…-library
GitHub Stars
3
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass