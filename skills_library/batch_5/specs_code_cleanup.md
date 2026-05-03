---
title: specs-code-cleanup
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/specs-code-cleanup
---

# specs-code-cleanup

skills/giuseppe-trisciuoglio/developer-kit/specs-code-cleanup
specs-code-cleanup
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill specs-code-cleanup
SKILL.md
Code Cleanup
Overview

Performs post-review cosmetic cleanup to make code production-ready. This is the final workflow step after /developer-kit-specs:specs.task-review approval.

Input: docs/specs/[id]/tasks/TASK-XXX.md (reviewed status)
Output: Cleaned code, task marked completed

When to Use
Use when asked to clean up code, polish, finalize, tidy up, or remove technical debt after review approval.
Use to prepare code for completion: remove debug logs, dead code, optimize imports, and improve readability.
Use as the final quality gate in the specification-driven development workflow.
Not for refactoring logic or fixing bugs — focused solely on cosmetic and hygiene cleanup.
Arguments
Argument	Required	Description
--lang	No	java, spring, typescript, nestjs, react, python, general
--task	Yes	Path to task file
Best Practices
Clean, not change: Only remove or reorganize — never change functionality
Preserve behavior: Code must work exactly the same after cleanup
Use project tools: Prefer ./mvnw spotless:apply, npm run lint:fix, black, etc.
Use TodoWrite: Track progress through all 8 phases
Stop on failure: If tests fail, stop and report — do not proceed

See references/language-patterns.md for language-specific formatter commands, import ordering, and grep patterns.

Instructions
Phase 1: Task Verification

Parse $ARGUMENTS for parameters:

--lang (optional): Target language/framework
--task (required): Task ID or file path
--spec (optional): Spec folder path (used with task ID)

Support two formats:

Format 1 (direct path): --task=docs/specs/001-feature/tasks/TASK-001.md
Format 2 (spec+task): --spec=docs/specs/001-feature --task=TASK-001

If Format 2 is used, construct the task file path as: {spec}/tasks/{task}.md

Read the task file. Verify:

Status is reviewed or implemented (not completed)
Review report TASK-XXX--review.md exists and is approved

If not reviewed → stop and tell user to run /developer-kit-specs:specs.task-review first

Extract task ID, title, and provides files

Phase 2: Identify Files to Clean
Read TASK-XXX--review.md for files created/modified
Read task provides field for file paths
Verify files exist; build cleanup list
Categorize: source files, test files, config files
Phase 3: Technical Debt Removal

Search files for temporary/debug artifacts with Grep:

console.log, System.out.println, print(, // DEBUG:, // temp, // hack
Resolved TODO/FIXME comments (keep unresolved ones)

Review context for each finding. Remove confirmed debt and document what was removed.

Phase 4: Import Optimization
Run language-specific import optimizer if available (see references)
Manually remove unused imports if no tool exists
Document files changed
Phase 5: Code Readability Improvements
Run language-specific formatter if available (see references)
If no formatter: fix indentation, break long lines (>120), fix spacing
Remove dead code only if obviously safe
Document changes
Phase 6: Documentation Verification
Verify class/file headers and public API docs
Check remaining TODOs are still valid and have context
Remove or update outdated comments
Document documentation changes
Phase 7: Final Verification
Run linters if available
Run tests if available
Verify no logic or signature changes were introduced
If tests fail → stop and report failures
Phase 8: Task Completion

Auto-update task status:

Add a ## Cleanup Summary section to the task file
Check any remaining boxes in the DoD section
Hooks automatically update status to completed and set completed_date + cleanup_date

Append ## Cleanup Summary to task file with:

Files cleaned
Changes made
Verification checklist (linters, tests, no functionality changes)

Mark all todos complete

Examples
Spring Boot Cleanup
/developer-kit-specs:specs-code-cleanup --lang=spring --task="docs/specs/001-user-auth/tasks/TASK-001.md"


Actions:

Verify TASK-001 status is reviewed
Files: UserController.java, UserService.java, UserRepository.java
Remove 5 System.out.println and 2 resolved TODOs
Run ./mvnw spotless:apply
Run ./mvnw test -q
Mark task completed
TypeScript Cleanup
/developer-kit-specs:specs-code-cleanup --lang=typescript --task="docs/specs/002-dashboard/tasks/TASK-003.md"


Actions:

Verify TASK-003 status is reviewed
Files: Dashboard.tsx, useDashboard.ts, Dashboard.test.tsx
Remove 8 console.log statements
Run npm run lint:fix and npm run format
Run npm test
Mark task completed
Constraints and Warnings
Never change logic or signatures during cleanup
Stop immediately and report if tests fail
Verify behavior is unchanged before marking complete
Weekly Installs
272
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass