---
title: implement
url: https://skills.sh/webriq/claude-skills/implement
---

# implement

skills/webriq/claude-skills/implement
implement
Installation
$ npx skills add https://github.com/webriq/claude-skills --skill implement
SKILL.md
/implement - Implementation Agent

Model: sonnet (strong coding with better cost efficiency than opus)

Command Flags
Flag	Short	Description
--help	-h	Show available commands and options
--version	-v	Show workflow skills version
--multi	-m	Multi-task mode: spawn parallel agents
auto		Enable auto-chain (test → document → ship)
Flag Handling

On -h or --help:

/implement - Implementation Agent

Usage:
  /implement {ID}                    Implement a single task
  /implement auto {ID}               Implement with auto-chain enabled
  /implement -m {ID1} {ID2} ...      Implement multiple tasks in parallel
  /implement auto -m {ID1} {ID2}     Multi-task with auto-chain
  /implement -h, --help              Show this help message
  /implement -v, --version           Show version

Arguments:
  {ID}    Task ID (number) or task filename (e.g., 001-auth-jwt)

Options:
  auto    After implementation, automatically chain through:
          test → document → ship
  -m      Spawn parallel agents for each task

Examples:
  /implement 1                       # Implement task #1
  /implement 001-auth-jwt            # Using task filename
  /implement auto 1                  # With auto-chain
  /implement -m 1 2 3                # Three tasks in parallel

Next: /test {ID}


On -v or --version: Display:

Workflow Skills v1.5.1
https://github.com/eljun/workflow-skills

When to Use

Invoke /implement {ID} when:

A task document exists in docs/task/
Task is in "Planned" status in TASKS.md
Ready to start coding

Example: /implement 1 or /implement 001-dashboard-redesign

Invocation Options
Command	Mode	Behavior
/implement {ID}	Manual	Implement single task, then notify user to run /test
/implement auto {ID}	Automated	Implement, then auto-chain through test → document → ship
/implement -m {ID1} {ID2} ...	Multi-task	Spawn parallel agents for each task
/implement --multi {ID1} {ID2}	Multi-task	Same as -m
/implement auto -m {ID1} {ID2}	Multi + Auto	Parallel tasks with auto-chain
Task ID Resolution

The {ID} can be:

Numeric ID: 1, 2, 3 → Looks up in TASKS.md, finds matching task document
Padded ID: 001, 002 → Same as numeric
Full filename: 001-dashboard-redesign → Direct file reference

Resolution process:

If numeric → Read TASKS.md, find row with matching ID, get task doc path
If filename → Look for docs/task/{filename}.md directly
Auto Mode

When invoked with auto, the implement skill:

Sets Automation: auto in the task document (overrides any existing value)
Implements the task as normal
After completion, automatically spawns /simplify {ID} (sonnet)
The pipeline continues: simplify → test → document → ship

This lets you skip /task auto and trigger the full pipeline from implement:

/implement auto {ID} → implement code
    ↓
/simplify (sonnet) ← quality gate
    │
PASS → /test (haiku)
    │
PASS → /document → /ship → PR + notify
FAIL → /implement (with test report) → /simplify → retry

Multi-Task Mode

When invoked with -m or --multi, the implement skill spawns parallel agents:

/implement -m 1 2 3
       │
       ├── Validate all tasks exist in TASKS.md
       ├── Check for file overlap warnings
       │
       └── Spawn in parallel (using Task tool):
           ├── Agent-1: /implement 1
           ├── Agent-2: /implement 2
           └── Agent-3: /implement 3
       │
       └── Wait for all agents to complete
       └── Report combined status


Multi-task with auto mode:

/implement auto -m 1 2 3


Each spawned agent runs with auto mode, chaining to test → document → ship.

Pre-Flight Checks for Multi-Task

CRITICAL: Background agents cannot prompt for permissions interactively. You MUST complete all checks and get user approval BEFORE spawning agents.

Step 1: Validate Tasks Exist
✓ Task 1: 001-auth-jwt.md (found)
✓ Task 2: 002-fix-portal.md (found)
✗ Task 3: Not found in TASKS.md → STOP if any missing

Step 2: Check for File Overlap

Read each task's "File Changes" section:

⚠️ Warning: Tasks 1 and 2 both modify src/auth/middleware.ts

Options:
1. Continue anyway (may need manual conflict resolution)
2. Run sequentially instead
3. Cancel

Step 3: Check Dependencies
⚠️ Task 2 is blocked by Task 1
Recommendation: Run sequentially or resolve dependency first

Step 4: Scan for Dangerous Operations

Read each task document and scan for these keywords:

Keywords Found	Risk Level	Action
migration, schema, ALTER TABLE, prisma migrate	⚠️ Database	Require explicit approval
rm , delete file, remove, unlink	🚫 Deletion	Block - user must do manually
DROP, TRUNCATE, DELETE FROM (without WHERE)	🚫 Data loss	Block - user must do manually
--force, reset --hard, -rf	🚫 Destructive	Block
API_KEY, SECRET, password, credential	⚠️ Sensitive	Warn user
sudo, chmod 777, chown	🚫 System	Block
Step 5: Permission Approval (REQUIRED)

Display this prompt and WAIT for user confirmation:

═══════════════════════════════════════════════════════════════
MULTI-TASK PERMISSION CHECK
═══════════════════════════════════════════════════════════════

Tasks to implement in parallel:
  #1 {Task 1 name}
  #2 {Task 2 name}
  #3 {Task 3 name}

PERMISSIONS FOR BACKGROUND AGENTS
───────────────────────────────────────────────────────────────
✅ GRANTED (safe operations):
   • Read, Edit, Write files
   • Glob, Grep (search)
   • Git: add, commit, status, diff, checkout -b, log
   • npm/npx: install, run, build, test, lint

⚠️ REQUIRES APPROVAL (detected in tasks):
   • {e.g., "Database migration in Task #2"}
   • {e.g., "Schema changes in Task #1"}
   • (None detected)

🚫 BLOCKED (agents will stop if needed):
   • File deletion (rm, unlink, rimraf)
   • Destructive git (push --force, reset --hard, clean -f)
   • Database destruction (DROP, TRUNCATE)
   • System commands (sudo, chmod)

───────────────────────────────────────────────────────────────
If agents encounter blocked operations, they will STOP and
report back. You can then perform those manually.
═══════════════════════════════════════════════════════════════

Approve and start parallel implementation? (yes/no)


DO NOT spawn agents until user types "yes" or confirms.

Step 6: Spawn Agents with Pre-Authorized Tools

Only after user approval, spawn agents with these allowed tools:

Task({
  subagent_type: "general-purpose",
  model: "sonnet",
  isolation: "worktree",
  prompt: "/implement {ID}",
  run_in_background: true,
  allowed_tools: [
    "Read",
    "Edit",
    "Write",
    "Glob",
    "Grep",
    "Skill",
    "Bash(git add *)",
    "Bash(git commit *)",
    "Bash(git status)",
    "Bash(git diff *)",
    "Bash(git push *)",
    "Bash(git log *)",
    "Bash(npm install *)",
    "Bash(npm run *)",
    "Bash(npx *)"
  ]
})


Note: Dangerous operations are NOT in allowed_tools, so agents physically cannot perform them.

Workflow
/implement [auto] [-m] {ID} [{ID2} ...]
       ↓
0. Read LEARNINGS.md (if exists) — avoid known mistakes
1. Parse arguments: detect "auto" flag, "-m/--multi" flag, task ID(s)
2. If multi-task → Run pre-flight checks, spawn parallel agents, exit
3. Resolve task ID → find docs/task/{ID}-{name}.md
4. Read task document — this is the ONLY codebase context needed
   └── Only read source files explicitly listed in task doc's "File Changes"
   └── Do NOT explore directories, grep broadly, or read files not in the plan
5. Enter worktree isolation: EnterWorktree({ name: "task-{ID}" })
   └── Creates .claude/worktrees/task-{ID}/ on a new branch
   └── All edits, commits, and pushes happen inside the worktree
   └── User's working directory stays on main — never switches branch
6. If "auto" flag → set Automation: auto in task doc
7. Check Automation field (manual | auto)
8. Move task to "## In Progress" in TASKS.md
9. Invoke specialized skills if relevant (see Step 3 below)
   └── /vercel-react-best-practices (if installed + React code)
   └── /supabase-postgres-best-practices (if installed + DB code)
10. Implement following task document steps
11. Commit with [task-{ID}] prefix for traceability
12. Push branch to origin (git push -u origin {branch})
13. Update status to "TESTING" when complete
       ↓
┌─── Automation Mode? ───┐
│                        │
▼ Manual                 ▼ Auto
Notify user              Invoke /simplify {ID}
Ready for /simplify


Note: Step 9 pays dividends — invoking specialized skills before writing code surfaces platform-specific patterns and pitfalls upfront, saving rework later. See "Step 3: Invoke Specialized Skills" in the checklist below.

Auto Mode Behavior

When invoked with /implement auto {ID} OR task document has Automation: auto:

If invoked with auto argument, update the task document to set Automation: auto
After implementation completes, automatically invoke /simplify {ID}
Pre-Implementation Checklist

Before writing ANY code:

0. Read Project Learnings
If LEARNINGS.md exists → read it entirely (costs ~200 tokens, saves thousands)


Focus on:

Common Mistakes to Avoid — don't repeat what previous tasks already learned the hard way
Established Coding Patterns — use patterns already proven in this codebase
Architecture & Decisions — honor past decisions rather than re-inventing alternatives
Tech Stack Notes — non-obvious behaviors that previous tasks discovered

Context Efficiency Rule: The task doc created by /task (opus) already contains all the codebase research you need — exact file paths, patterns, snippets. Your job is to read the task doc and implement it. Only open source files that are explicitly listed in the task doc's "## File Changes" section. Do NOT explore directories, run broad find commands, or read files not mentioned in the plan. If the task doc is missing context, that's a gap to flag — not an invitation to explore.

0.5. Parse Arguments

Check for flags and task ID(s):

-m or --multi → Multi-task mode (spawn parallel agents)
auto → Set automation mode
Remaining args → Task ID(s)

Examples:

/implement 1 → Single task, manual mode
/implement auto 1 → Single task, auto mode
/implement -m 1 2 3 → Multi-task, manual mode
/implement auto -m 1 2 → Multi-task, auto mode

If auto is detected, update the task document header:

> **Automation:** auto

1. Resolve Task ID

Convert the task ID to the task document path:

Read TASKS.md
Find the row with matching ID in the first column
Get the task doc path from that row
Verify the file exists in docs/task/

Example:

Input: /implement 1
TASKS.md row: | 1 | Dashboard Redesign | HIGH | [001-dashboard-redesign.md](...) |
Resolved: docs/task/001-dashboard-redesign.md

1.5. Enter Worktree Isolation

Before any file edits or git operations, call EnterWorktree:

EnterWorktree({ name: "task-{ID}" })


This creates .claude/worktrees/task-{ID}/ on a new branch and switches the session into it. The user's working directory stays on main for the entire implementation.

Why this matters:

User's branch never changes — no git checkout -b in their directory
Uncommitted changes in the user's main directory are unaffected
Multiple agents can run in parallel with zero branch conflicts
After PR merges, git pull on main is a clean fast-forward
2. Read the Task Document — Then Stop Exploring
docs/task/{ID}-{task-name}.md


The task document was created by /task (opus), which already did thorough codebase research and embedded the relevant code into ## Code Context. Your reading list is:

✅ ALWAYS READ:
   - docs/task/{ID}-{task-name}.md          (your primary source)
   - LEARNINGS.md                            (already done in Step 0)
   - Files listed in ## File Changes         (only these, nothing else)

❌ DO NOT READ unless the task doc explicitly names them:
   - package.json / tsconfig.json / .env
   - Any config file not in ## File Changes
   - Files in directories not mentioned in the task doc
   - Adjacent files "for context"

❌ DO NOT RUN:
   - find . -type f       (directory sweeps)
   - ls -R / ls -la       (directory listing)
   - cat on unlisted files
   - Any grep to "understand patterns" — patterns are in ## Code Context


If a file isn't in the task doc and you think you need it: check ## Code Context first — the pattern you're looking for is probably already pasted there. If it genuinely isn't, use a targeted Grep for the specific symbol, not a directory sweep.

If the task doc is missing context you need: note it in the implementation summary. Don't explore — flag the gap so /task can improve next time.

Understand from the task doc:

Task ID (for commit messages)
Requirements (must have vs nice to have)
Proposed solution and architecture
File changes — your complete reading list
Implementation steps — follow them in order
Code Context — current code already embedded, no re-reading needed
3. Invoke Specialized Skills

Before writing any code, check whether platform-specific skills are installed and relevant to this task. These skills encode patterns and pitfalls from Vercel and Supabase engineers that are easy to miss — loading them upfront is much cheaper than fixing issues in review.

Skill	Invoke When
/vercel-react-best-practices	Task involves React, Next.js, or TypeScript
/supabase-postgres-best-practices	Task involves database queries, RLS, schema, or Supabase

Check the available skills list. If a relevant skill is there, invoke it now — before writing code — then apply what it tells you.

# For React/Next.js projects:
/vercel-react-best-practices

# For Supabase/PostgreSQL projects:
/supabase-postgres-best-practices


If you realize partway through that you skipped a relevant skill, go back and invoke it, then review your code against its guidance before continuing.

4. Update TASKS.md

Move task from "Planned" to "In Progress":

## In Progress

| ID | Task | Started | Task Doc | Status |
|----|------|---------|----------|--------|
| 1 | Quick Actions Redesign | Jan 25 | [001-quick-actions.md](docs/task/001-quick-actions.md) | Implementing |

5. Verify Dependencies

Check that all prerequisites exist:

Required API endpoints
Required types/interfaces
Required packages installed
No blocking tasks
Commit Convention

IMPORTANT: All commits must include the task ID prefix for traceability.

Format
[task-{ID}] {type}: {description}

{optional body}

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

Examples
# Feature commit
git commit -m "[task-1] feat: Add JWT authentication middleware

Implements token validation and refresh logic.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

# Fix commit
git commit -m "[task-2] fix: Resolve portal login redirect issue

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

Why This Matters

The [task-{ID}] prefix enables:

Traceability: Easy to see which commits belong to which task
Multi-task support: When multiple agents work in parallel, /ship can identify task-specific changes
Filtering: git log --grep="\[task-1\]" shows all commits for task 1
PR generation: /ship can create accurate PR descriptions
Implementation Guidelines
Follow the Task Document

The task document is your spec. Follow it step by step:

Step 1 → Complete → Verify
Step 2 → Complete → Verify
Continue until all steps done
Invoke Specialized Skills When Applicable
Situation	Skill
React/Next.js code	/vercel-react-best-practices (if installed)
Database work	/supabase-postgres-best-practices (if installed)
Need clarification	Ask user
Quality Standards
No any types - use proper TypeScript types
All hooks before early returns
AbortController in useEffect with fetches
Clean, readable code
Handle loading/error/empty states
Track Progress

Update the task document as you go:

Check off completed requirements
Note any deviations from plan
Document blockers encountered
Common Implementation Patterns
Creating New Files
// 1. Create the file
// 2. Add to index exports if needed
// 3. Import where used

Modifying Existing Files
// 1. Read the file first (always!)
// 2. Understand existing patterns
// 3. Make minimal, focused changes
// 4. Don't refactor unrelated code

Web Development
Check project's CLAUDE.md for patterns
Follow existing code patterns
Use proper authentication
Use ORM for database queries, not raw SQL
Completion Checklist

Before marking as ready for testing:

Code Quality
 Code compiles without errors
 No TypeScript errors
 Follows existing patterns
 No unnecessary complexity
Functionality
 All "Must Have" requirements implemented
 Happy path works
 Loading states handled
 Error states handled
 Empty states handled
Task Document
 Requirements checked off
 Any deviations documented
 Notes added for tester
Update Status to TESTING

When implementation is complete:

1. Update TASKS.md

Move to "Testing" section:

## Testing

| ID | Task | Task Doc | Test Report | Status |
|----|------|----------|-------------|--------|
| 1 | Quick Actions Redesign | [001-quick-actions.md](docs/task/001-quick-actions.md) | Pending | Ready for test |

2. Update Task Document

Add completion notes:

> **Status:** TESTING
> **Completed:** {Date}
> **Implementation Notes:** {Any important notes for tester}

3. Push Branch to Origin

Before marking complete, push the feature branch so /ship can create a PR without checking out locally:

git push -u origin {branch-name}


This is required. /ship expects the branch to already exist on origin when worktree isolation is used.

4. Pre-Completion Verification

Before marking implementation complete, do a quick sanity check:

Did this task involve React/Next.js? → Did you invoke /vercel-react-best-practices (if installed)?
Did this task involve database/Supabase? → Did you invoke /supabase-postgres-best-practices (if installed)?

If a relevant skill was available but skipped, invoke it now, review your code against its guidance, and make any corrections before proceeding.

5. Inform User / Chain to Next Skill

Check the task document for Automation: auto field.

Manual Mode (or if Automation field is missing)
Implementation complete for: #{ID} - {Task Title}

Files changed:
- path/to/file1.tsx (created)
- path/to/file2.tsx (modified)

Commits made:
- [task-{ID}] feat: Add authentication middleware
- [task-{ID}] feat: Add token refresh logic

Next Steps:
  /simplify {ID}          # e.g., /simplify 1  (quality gate before testing)
  /test {ID}              # skip simplify only if you've already reviewed manually

Auto Mode
Implementation complete for: #{ID} - {Task Title}

Files changed:
- path/to/file1.tsx (created)
- path/to/file2.tsx (modified)

[AUTO] Spawning /simplify with sonnet model...


Use Task tool to spawn simplify agent with model: sonnet: Task({ subagent_type: "general-purpose", model: "sonnet", prompt: "/simplify {ID}" })

Multi-Task Completion

When all parallel agents complete:

Multi-task implementation complete!

Results:
├── Task #1: ✓ Complete (3 commits)
├── Task #2: ✓ Complete (2 commits)
└── Task #3: ✗ Failed (blocked by missing API)

Next Steps (for successful tasks):
  /simplify 1              # Quality gate for task #1
  /simplify 2              # Quality gate for task #2

Failed task requires attention:
  Task #3: See docs/task/003-feature-name.md for blocker details

Handling Issues
Blocked by Missing Dependency
Document the blocker in task document
Update TASKS.md status to "Blocked"
Inform user with specific blocker details
Create sub-task if needed via /task
Requirement Unclear
Ask user for clarification
Update task document with clarified requirements
Continue implementation
Scope Creep
Stick to task document scope
Note additional ideas in "Nice to Have" or separate task
Don't expand scope without user approval
Specialized Skills (Install Separately)

These plugins are optional but highly recommended for their respective stacks. Once installed, invoke them before writing code for relevant tasks.

Plugin	Install From	When to Invoke
vercel-react-best-practices	vercel-labs/agent-skills	React/Next.js/TypeScript code
supabase-postgres-best-practices	supabase/agent-skills	Database queries, RLS, schema, Supabase code
Weekly Installs
32
Repository
webriq/claude-skills
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass