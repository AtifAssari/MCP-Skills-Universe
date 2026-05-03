---
title: resolve-pr-comments
url: https://skills.sh/squirrel289/pax/resolve-pr-comments
---

# resolve-pr-comments

skills/squirrel289/pax/resolve-pr-comments
resolve-pr-comments
Installation
$ npx skills add https://github.com/squirrel289/pax --skill resolve-pr-comments
SKILL.md
Resolve PR Comments

A workflow skill that systematically addresses and resolves all review comments on a pull request.

Purpose

Automates the process of reviewing, addressing, and resolving PR review feedback by composing multiple general-purpose skills into a cohesive workflow.

When to Use

Use this workflow when:

PR has received review comments that need to be addressed
You want to systematically work through all feedback
You need to resolve threads after making changes
PR is blocked on unresolved review comments
Skill Composition

This workflow composes:

pull-request-tool: Fetch review comments, reply to threads, resolve threads
sequential-execution OR parallel-execution: Process comments in order (sequential) or concurrently (parallel), handle dependencies as needed
yolo OR collaborative: Execution mode (autonomous vs interactive)
Parameters
Required

You must specify the pull request to process using either of the following input formats:

Separate Parameters: - pr-number: Pull request number (e.g., 42) - repository: Repository in the format owner/repo (e.g., octocat/Hello-World)

Combined URL: - pr-url: Full pull request URL (e.g., https://github.com/owner/repo/pull/42)

If both formats are provided, pr-url takes precedence.

Optional
interaction-mode: yolo (autonomous) or collaborative (interactive)
execution-mode: sequential (default) or parallel
filter: unresolved-only (default), all, by-reviewer
auto-resolve: Automatically resolve threads after addressing (default: true)
reviewer: Filter comments by specific reviewer
Workflow Steps
Phase 1: Discovery

Fetch PR details (pull-request-tool)

Get PR metadata
Verify PR is open
Check current status

List review comments (pull-request-tool)

Get all review threads
Filter based on parameters
Group by file and thread
Phase 2: Analysis

Analyze comments (sequential-execution OR parallel-execution)

Categorize by type (question, change request, suggestion)
Identify dependencies between comments
Prioritize or group for resolution

Plan approach

Determine which comments need code changes
Which need clarification/discussion
Which can be resolved with replies
Phase 3: Resolution

Address each comment (sequential-execution OR parallel-execution)

For each comment (in order or concurrently, based on execution-mode):

a. Review the feedback - Read comment and context - Understand the request - Check referenced code

b. Determine action - Code change needed? - Just needs reply/clarification? - Already addressed?

c. Take action - Make code changes if needed - Reply to thread with explanation - Mark as resolved if appropriate

d. Verify resolution - Ensure change addresses feedback - Run tests if code changed - Confirm reviewer intent met

Phase 4: Finalization

Push changes (if any code changes made)

Commit all changes
Push to PR branch
Trigger CI checks

Final verification

Verify all targeted comments addressed
Check for any new comments
Update PR description if needed
Interaction and Execution Modes
YOLO Mode (Autonomous)
When interaction-mode = yolo:
- Automatically determine best response to each comment
- Make code changes without confirmation
- Auto-resolve threads after addressing
- Report only final summary

Collaborative Mode (Interactive)
When interaction-mode = collaborative:
- Show each comment to user
- Propose response/change
- Get approval before proceeding
- Confirm before resolving threads

Sequential vs Parallel Execution
sequential: Comments are processed one after another, respecting dependencies.
parallel: Independent comments are processed concurrently for faster resolution.
Example Workflows
Example 1: YOLO + Parallel
Task: Resolve all unresolved PR comments on PR #42 in owner/repo using parallel execution

Execution:
1. Fetch unresolved comments (5 found)
2. Process all comments in parallel:
     - Comment 1: "Add error handling" → Add try/catch, reply, resolve
     - Comment 2: "Fix typo" → Fix, reply, resolve
     - ...
3. Push changes
4. Report: "Resolved 5 comments, updated 3 files"

Example 2: Collaborative + Sequential
Task: Address review comments collaboratively, one at a time

Execution:
1. Fetch 3 unresolved comments
2. Show comment 1, get user input, apply change, resolve
3. Repeat for each comment in order
4. Show summary, push changes

Output Format
YOLO Mode Output
TASK: Resolve PR Comments (#42)
STATUS: Complete

COMMENTS ADDRESSED: 8/8
- 5 required code changes
- 2 clarifications
- 1 acknowledgment

FILES MODIFIED:
- src/auth.ts (2 changes)
- src/api.ts (1 change)
- src/utils.ts (2 changes)

THREADS RESOLVED: 8
CHANGES PUSHED: Yes
CI STATUS: Passing

Collaborative Mode Output
PR Comment Resolution Progress

✅ Comment 1/8 - "Add error handling" - Resolved
✅ Comment 2/8 - "Fix typo" - Resolved  
⏳ Comment 3/8 - "Refactor function" - In progress

Current: Reviewing proposed refactoring approach
Next: 5 comments remaining

Error Handling
Common Issues

Conflict with recent changes

Pull latest changes
Re-evaluate comment applicability
Resolve conflicts if needed

Unclear feedback

YOLO: Make best-effort interpretation, document assumption
Collaborative: Ask user for clarification

Comment already addressed

Verify fix is present
Reply explaining it's addressed
Resolve thread

Tests fail after changes

YOLO: Attempt auto-fix, revert if fails
Collaborative: Show failure, ask for guidance
Best Practices
Process in logical order: Group related comments, handle dependencies first
Verify before resolving: Ensure feedback truly addressed
Clear communication: Explain what was done in thread replies
Test after changes: Run tests before pushing
Commit logically: Group related changes in commits
Update PR description: Reflect significant changes made
Track progress: Use todo list for multi-comment PRs
Request re-review: Notify reviewers of significant changes
Integration Example
# Full PR processing using composed skills

1. resolve-pr-comments (this workflow)
     - Uses: pull-request-tool + sequential-execution OR parallel-execution + yolo
     - Addresses all review feedback

2. Check CI status
     - Uses: pull-request-tool
     - Verify tests pass

3. Merge PR
     - Uses: merge-pr workflow
     - Complete the process

Quick Reference
PURPOSE:
    Systematically address and resolve PR review comments

COMPOSITION:
    pull-request-tool + sequential-execution OR parallel-execution + (yolo OR collaborative)

MODES:
    **YOLO**:          Autonomous resolution
    **Collaborative**: Interactive with user input

EXECUTION:
    **sequential**:    One comment at a time
    **parallel**:      Multiple comments concurrently

PHASES:
    1. **Discovery**:   Fetch PR and comments
    2. **Analysis**:    Categorize and prioritize
    3. **Resolution**:  Address each comment
    4. **Finalization**: Push changes, verify

PARAMETERS:
- **pr-number** (required): Pull request number (e.g., `42`)
- **repository** (required): Repository in the format `owner/repo` (e.g., `octocat/Hello-World`)
- **pr-url**: Full pull request URL (e.g., `https://github.com/owner/repo/pull/42`). Takes precedence if provided.
- **interaction-mode**: `yolo` (autonomous) or `collaborative` (interactive)
- **execution-mode**: `sequential` (default) or `parallel`
- **filter**: `unresolved-only` (default), `all`, or `by-reviewer`
- **auto-resolve**: Automatically resolve threads after addressing (default: true)
- **reviewer**: Filter comments by specific reviewer

OUTPUT:
    Summary of comments addressed, files changed, status

Related Skills
pull-request-tool: For fetching PR details, posting replies, resolving threads
handle-pr-feedback: For triage and decision routing based on feedback severity
update-work-item: For reverting work item status when major feedback is detected
process-pr: Orchestrates full PR workflow including feedback resolution
sequential-execution: For ordered comment processing
parallel-execution: For concurrent comment addressing
Weekly Installs
11
Repository
squirrel289/pax
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn