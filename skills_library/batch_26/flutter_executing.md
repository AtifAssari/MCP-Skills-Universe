---
title: flutter-executing
url: https://skills.sh/vp-k/flutter-craft/flutter-executing
---

# flutter-executing

skills/vp-k/flutter-craft/flutter-executing
flutter-executing
Installation
$ npx skills add https://github.com/vp-k/flutter-craft --skill flutter-executing
SKILL.md
Executing Flutter Implementation Plans
Overview

Load plan, review critically, execute tasks in batches, run Flutter verifications, report for review between batches.

Core principle: Batch execution with checkpoints for review.

Announce at start: "I'm using the flutter-executing skill to implement this plan."

The Process
Step 1: Load and Review Plan

Read plan file

cat docs/plans/YYYY-MM-DD-<feature>-plan.md


Check dependencies first

cat pubspec.yaml


Install new dependencies if needed

flutter pub get


Review critically:

Are file paths correct?
Is layer order followed (Domain → Data → Presentation)?
Are there any gaps in the plan?

If concerns: Raise them before starting

If no concerns: Create TodoWrite and proceed

Step 2: Execute Batch

Default: First 3 tasks

For each task:

Mark as in_progress in TodoWrite
Create/modify files as specified
Write complete code (from plan)
Run verification:
flutter analyze lib/features/<feature>/

Commit:
git add <files>
git commit -m "<conventional commit message>"

Mark as completed in TodoWrite
Step 3: Verify Batch

After completing 3 tasks, run full verification:

# Static analysis
flutter analyze
# Expected: No issues found!

# Run tests (if test files exist)
flutter test test/features/<feature>/
# Expected: All tests passed!

# Quick build check (optional)
flutter build apk --debug --target-platform android-arm64
# Expected: Built successfully

Step 4: Report

When batch complete, report:

## Batch N Complete

**Tasks completed:**
1. ✅ Task 1: [description]
2. ✅ Task 2: [description]
3. ✅ Task 3: [description]

**Verification:**
- flutter analyze: No issues found
- flutter test: X/X passed

**Files created/modified:**
- lib/features/.../entity.dart
- lib/features/.../repository.dart
- ...

**Ready for feedback.**

Step 5: Continue

Based on feedback:

Apply changes if needed
Execute next batch of 3 tasks
Repeat until all tasks complete
Step 6: Complete Development

After all tasks complete and verified:

Run final verification:

flutter analyze
flutter test
flutter build apk --debug  # or ios


Announce: "I'm using the flutter-finishing skill to complete this work."

REQUIRED SUB-SKILL: Use flutter-craft:flutter-finishing

Verify tests
Present 4 options (merge/PR/keep/discard)
Execute choice
Cleanup worktree if applicable
Flutter-Specific Verification Commands
Stage	Command	Expected Output
Per-file	flutter analyze lib/path/file.dart	No issues found
Per-batch	flutter analyze lib/features/<feature>/	No issues found
Test	flutter test test/features/<feature>/	All tests passed
Final	flutter build apk --debug	Built successfully
When to Stop and Ask for Help

STOP executing immediately when:

flutter analyze shows errors (not just warnings)
Tests fail with unclear cause
Missing dependency not in pubspec.yaml
Plan has unclear instructions
File path in plan doesn't match project structure
State management pattern unclear

Ask for clarification rather than guessing.

Layer Order Verification

Before executing, verify plan follows this order:

1. Domain Layer tasks first
   ├── Entities
   ├── Repository interfaces
   └── UseCases

2. Data Layer tasks second
   ├── Models
   ├── DataSources
   └── Repository implementations

3. Presentation Layer tasks third
   ├── State Management
   ├── Widgets
   └── Screens

4. Test tasks after implementation
   ├── Repository tests (priority 1)
   ├── State tests (priority 2)
   └── Widget tests (priority 3)


If plan doesn't follow this order, raise concern before starting.

REQUIRED SUB-SKILL
During Execution

After EACH batch, you MUST invoke: → flutter-craft:flutter-verification (verify before continuing)

After All Tasks Complete

You MUST invoke: → flutter-craft:flutter-finishing (present completion options)

Remember
Review plan critically first - Don't blindly execute
Follow layer order - Domain → Data → Presentation
Run flutter analyze per batch - Catch errors early
Commit after each task - Atomic commits
Report and wait - Don't continue without feedback
Stop when blocked - Don't guess, ask
Weekly Installs
12
Repository
vp-k/flutter-craft
GitHub Stars
6
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass