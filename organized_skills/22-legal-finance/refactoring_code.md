---
rating: ⭐⭐
title: refactoring-code
url: https://skills.sh/dralgorhythm/claude-agentic-framework/refactoring-code
---

# refactoring-code

skills/dralgorhythm/claude-agentic-framework/refactoring-code
refactoring-code
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill refactoring-code
SKILL.md
Refactoring Code
The Refactoring Hat

When refactoring, you change structure without changing behavior. Always have tests passing before and after.

Workflows
 Tests Green: Ensure all tests pass before starting
 Analyze: Use Grep to understand dependencies
 Small Steps: Make one small change at a time
 Verify Usages: Use Grep to find all usages before changes
 Commit Often: Commit after each successful refactoring
 Tests Green: Verify tests still pass after each change
Common Refactorings
Extract Method

When a code block does one thing, extract it to a named method.

Use Grep to verify extraction won't break callers
Extract the method
Run tests
Rename for Clarity

Names should reveal intent.

Use Grep to find ALL usages
Use Edit with replace_all for codebase-wide rename
Verify no missed references
Remove Dead Code
Use Grep to verify code is unused
If zero references, safe to remove
If references exist, trace to understand usage
Code Smells to Address
Long Method: Extract smaller methods
Long Parameter List: Introduce parameter object
Duplicate Code: Extract to shared function (use Grep to locate duplicates)
Feature Envy: Move method to the class it uses most
Data Clumps: Group related data into objects
Primitive Obsession: Replace primitives with value objects
Safety Rules
Never refactor and add features simultaneously
Always use Grep to find all usages before removing/renaming
Run tests after every change
Use targeted Edit operations instead of broad find-replace
Commit working states frequently
Weekly Installs
39
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass