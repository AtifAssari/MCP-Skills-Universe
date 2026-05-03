---
rating: ⭐⭐⭐
title: refactor-plan
url: https://skills.sh/github/awesome-copilot/refactor-plan
---

# refactor-plan

skills/github/awesome-copilot/refactor-plan
refactor-plan
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill refactor-plan
SKILL.md
Refactor Plan

Create a detailed plan for this refactoring task.

Refactor Goal

{{refactor_description}}

Instructions
Search the codebase to understand current state
Identify all affected files and their dependencies
Plan changes in a safe sequence (types first, then implementations, then tests)
Include verification steps between changes
Consider rollback if something fails
Output Format
## Refactor Plan: [title]

### Current State
[Brief description of how things work now]

### Target State
[Brief description of how things will work after]

### Affected Files
| File | Change Type | Dependencies |
|------|-------------|--------------|
| path | modify/create/delete | blocks X, blocked by Y |

### Execution Plan

#### Phase 1: Types and Interfaces
- [ ] Step 1.1: [action] in `file.ts`
- [ ] Verify: [how to check it worked]

#### Phase 2: Implementation
- [ ] Step 2.1: [action] in `file.ts`
- [ ] Verify: [how to check]

#### Phase 3: Tests
- [ ] Step 3.1: Update tests in `file.test.ts`
- [ ] Verify: Run `npm test`

#### Phase 4: Cleanup
- [ ] Remove deprecated code
- [ ] Update documentation

### Rollback Plan
If something fails:
1. [Step to undo]
2. [Step to undo]

### Risks
- [Potential issue and mitigation]


Shall I proceed with Phase 1?

Weekly Installs
9.9K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass