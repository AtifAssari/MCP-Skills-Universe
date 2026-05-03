---
rating: ⭐⭐⭐
title: loose-ends
url: https://skills.sh/elliotjlt/claude-skill-potions/loose-ends
---

# loose-ends

skills/elliotjlt/claude-skill-potions/loose-ends
loose-ends
Installation
$ npx skills add https://github.com/elliotjlt/claude-skill-potions --skill loose-ends
SKILL.md
Loose Ends
When To Activate
Instructions
The Loose Ends Checklist

Before declaring complete, run through:

Code Hygiene
 No unused imports
 No unused variables
 No commented-out code (unless intentional)
 No console.log/print statements left in
 No debugger statements
TODOs and FIXMEs
 No new TODOs created and forgotten
 Any existing TODOs in touched files addressed or noted
Tests
 New code has tests (or explicit reason why not)
 Existing tests still pass
 Edge cases considered
Types (if applicable)
 No any types added
 No type assertions without reason
 Interfaces/types defined for new structures
References
 Old references updated if things were renamed
 No broken imports
 No stale comments referring to old code
Error Handling
 Errors handled or explicitly bubbled up
 User-facing errors have good messages
 No silent failures
Automated Sweep

Run the sweep script to find common cruft:

python scripts/sweep.py


Scans for:

console.log, print(), debugger statements
TODO, FIXME, XXX, HACK comments
dd(), var_dump(), binding.pry (PHP/Ruby)
Quick Scan Commands
# Find TODOs in changed files
git diff --name-only | xargs grep -n "TODO\|FIXME"

# Find console.log in changed files
git diff --name-only | xargs grep -n "console.log"

# Find unused imports (TypeScript)
npx tsc --noEmit 2>&1 | grep "declared but"

# Find any types added
git diff | grep ": any"

Prioritize by Impact

Not all loose ends are equal:

Priority	Type	Action
Fix now	Broken imports, missing exports	Blocks functionality
Fix now	console.log in production code	Leaks info
Should fix	Unused imports/variables	Code smell
Should fix	Missing tests for new logic	Technical debt
Note for later	Old TODOs in touched files	Existing debt
Ignore	Style inconsistencies	Not your scope
Output Format
## Loose Ends Check

**Files changed:** [count]

**Fixed:**
- [x] Removed unused import in `file.ts`
- [x] Removed console.log in `handler.ts`

**Noted:**
- [ ] `utils.ts:45` has existing TODO (not from this change)

**Clean:** No loose ends found / All addressed

NEVER
Declare "done" without scanning for loose ends
Leave console.log in production code
Create TODOs and forget about them
Leave unused imports from experimentation
Skip the checklist because "it's a small change"
ALWAYS
Scan changed files before committing
Remove debugging artifacts
Address or document any TODOs you create
Verify imports are used
Check that tests pass after changes
Example

After implementing a new API endpoint:

## Loose Ends Check

**Files changed:** 4

**Scanning...**

`api/users.ts`:
- Line 3: unused import `lodash` → Removed
- Line 45: console.log for debugging → Removed

`types/user.ts`:
- Clean

`tests/users.test.ts`:
- New endpoint has test → Good
- Edge case (empty input) not tested → Added

`services/user.ts`:
- Line 23: TODO I wrote: "validate email format" → Addressed now

**Result:** 4 loose ends found and fixed. Ready to commit.

Weekly Installs
8
Repository
elliotjlt/claud…-potions
GitHub Stars
55
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass