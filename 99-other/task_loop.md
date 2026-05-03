---
title: task-loop
url: https://skills.sh/duyet/claude-plugins/task-loop
---

# task-loop

skills/duyet/claude-plugins/task-loop
task-loop
Installation
$ npx skills add https://github.com/duyet/claude-plugins --skill task-loop
SKILL.md
Task Loop

Duyetbot's loop-based approach to task execution.

Philosophy
Small steps: Each iteration = one meaningful change
Verification: Every change validated before continuing
Visibility: Progress tracked and communicated
Adaptability: Plan adjusts based on what's learned
Loop Structure
┌──────────────┐
│  UNDERSTAND  │  What's current state?
└──────┬───────┘
       ▼
┌──────────────┐
│     PLAN     │  What's single next step?
└──────┬───────┘
       ▼
┌──────────────┐
│   EXECUTE    │  One change only
└──────┬───────┘
       ▼
┌──────────────┐
│    VERIFY    │  Did it work?
└──────┬───────┘
       ▼
   Complete? ──NO──► Loop
       │
      YES
       ▼
     DONE

Iteration Template
### Iteration N

**State**: What's done / pending
**Goal**: What this iteration accomplishes

**Execution**:
[1] Action → Result

**Verify**:
- [ ] Works as expected
- [ ] Tests pass

**Next**: What comes after

Progress Format
[x] Step 1: Done (iter 1)
[x] Step 2: Done (iter 2)
[ ] Step 3: Current (iter 3)
[ ] Step 4: Pending

Termination
Success
All acceptance criteria met
Tests passing
Code clean
Stop
Blocker requiring human input
Max iterations reached
Same step failed 3x
Anti-Patterns
Don't: Giant Iterations
BAD:  Iteration 1: Implement entire feature
GOOD: Iteration 1: Data model
      Iteration 2: Core logic
      Iteration 3: Error handling
      Iteration 4: Tests

Don't: Skip Verification
BAD:  Execute → Execute → Execute → Check
GOOD: Execute → Verify → Execute → Verify

Don't: Ignore Failures
BAD:  Test failed, moving on
GOOD: Test failed, investigating cause

Weekly Installs
15
Repository
duyet/claude-plugins
GitHub Stars
4
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass