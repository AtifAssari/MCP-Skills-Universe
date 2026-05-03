---
title: writing-plans
url: https://skills.sh/bbeierle12/skill-mcp-claude/writing-plans
---

# writing-plans

skills/bbeierle12/skill-mcp-claude/writing-plans
writing-plans
Installation
$ npx skills add https://github.com/bbeierle12/skill-mcp-claude --skill writing-plans
SKILL.md
Writing Plans
Core Principle

Write plans clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow.

Plan Structure

Save plans to: docs/plans/YYYY-MM-DD-<feature-name>.md

# [Feature Name] Implementation Plan

> **For Claude:** Use executing-plans skill to implement this plan task-by-task.

## Overview
Brief description of what we're building and why.

## Prerequisites
- [ ] Dependency 1 installed
- [ ] Service 2 running
- [ ] Access to X configured

## Tasks

### Task 1: [Descriptive Name]
**File:** `path/to/file.ts`
**Test:** `path/to/file.test.ts`

#### Test First (RED)
```typescript
// Exact test code to write
describe('FeatureName', () => {
  it('should do specific thing', () => {
    // Arrange
    // Act  
    // Assert
  });
});

Implementation (GREEN)
// Exact implementation code
export function featureName() {
  // Implementation
}

Verification
npm test -- --grep "FeatureName"
# Expected: 1 passing

Task 2: [Next Task]

...

Integration Tests

After all tasks complete:

# Commands to run
npm run test:integration

Manual Verification

Steps to manually verify the feature works:

Step 1
Step 2
Expected result
Rollback Plan

If something goes wrong:

git revert HEAD
...

## Plan Quality Checklist

### Every Task Must Have:
- [ ] Exact file paths
- [ ] Complete code (not "add validation")
- [ ] Test written BEFORE implementation
- [ ] Verification command with expected output
- [ ] Clear success criteria

### Plan Must Include:
- [ ] Prerequisites listed
- [ ] Tasks in dependency order
- [ ] Integration test at end
- [ ] Rollback instructions

## Writing Guidelines

### Be Explicit
❌ "Add error handling"
✅ "Wrap the API call in try/catch, log errors with context, return null on failure"

### Be Complete
❌ "Update the config"
✅ ```json
{
  "setting": "value",
  "newSetting": "newValue"
}

Be Ordered

Tasks should be executable in sequence:

No forward dependencies
Each task builds on previous
Tests pass after each task
Execution Handoff

After saving the plan, offer execution choice:

"Plan complete and saved. Two execution options:

1. Subagent-Driven (this session)

Fresh subagent per task
Review between tasks
Fast iteration

2. Parallel Session (separate)

Open new session with executing-plans skill
Batch execution with checkpoints

Which approach?"

DRY, YAGNI, TDD Reminders

Include at top of every plan:

## Remember
- Exact file paths always
- Complete code in plan (not "add validation")
- Exact commands with expected output
- DRY, YAGNI, TDD, frequent commits

Anti-Patterns
Don't Do This
Vague task descriptions
Missing file paths
Incomplete code snippets
Implementation before tests
No verification steps
Assuming context
Weekly Installs
60
Repository
bbeierle12/skil…p-claude
GitHub Stars
8
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass