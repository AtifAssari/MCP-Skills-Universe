---
title: safe-refactor
url: https://skills.sh/elliotjlt/claude-skill-potions/safe-refactor
---

# safe-refactor

skills/elliotjlt/claude-skill-potions/safe-refactor
safe-refactor
Installation
$ npx skills add https://github.com/elliotjlt/claude-skill-potions --skill safe-refactor
SKILL.md
Safe Refactor
Prerequisites

This elixir works best with these skills installed:

Skill	Purpose	If Missing
pre-mortem	Risk assessment before starting	Falls back to built-in checklist
prove-it	Verification enforcement	Falls back to built-in verification
retrospective	Document learnings	Skipped (optional phase)
When To Activate
Instructions
Phase 1: Assess Risk

<phase_risk> If pre-mortem skill installed: Invoke it now.

If not installed, evaluate:

## Refactor Risk Assessment

**What's changing:**
- [ ] Files affected: [list them]
- [ ] Functions/classes modified: [list them]
- [ ] Estimated lines changed: [number]

**Risk factors:**
- [ ] Touches shared/core code (used by multiple features)
- [ ] Affects data persistence (database, files, cache)
- [ ] Changes public API/interfaces
- [ ] Lacks test coverage
- [ ] Written by someone else / unfamiliar code
- [ ] Production-critical path

**Risk level:** [Low / Medium / High / Abort]


GATE: Do not proceed if:

Risk is "Abort"
More than 3 risk factors checked AND no tests exist
You can't list all affected files

If high risk: Consider breaking into smaller refactors. </phase_risk>

Phase 2: Prepare

<phase_prepare> Before touching code:

Ensure tests exist (or write them first)

- [ ] Existing tests cover the behavior being preserved
- [ ] If no tests: write characterization tests NOW


Create escape hatch

git stash  # or commit current state
git checkout -b refactor/[description]


Document current behavior

Before: [How it works now]
After: [How it should work - must be identical externally]


GATE: Do not proceed without:

Tests that verify current behavior
Clean git state (can revert easily)
Clear before/after behavior description </phase_prepare>
Phase 3: Implement

<phase_implement> Rules for safe refactoring:

One thing at a time

Don't mix refactoring with feature changes
Don't fix bugs you discover (note them, fix separately)
Don't "while I'm here" other improvements

Small commits

# Good: multiple small commits
git commit -m "Extract helper function"
git commit -m "Rename variables for clarity"
git commit -m "Move file to new location"

# Bad: one giant commit
git commit -m "Refactor everything"


Run tests frequently

After each logical change
Before each commit
If tests fail: revert and try smaller steps

Preserve behavior exactly

No "improvements" to logic
No fixing edge cases (that's a separate change)
External behavior must be identical </phase_implement>
Phase 4: Verify

<phase_verify> If prove-it skill installed: Invoke it now.

If not installed:

## Refactor Verification

**Automated checks:**
- [ ] All existing tests pass
- [ ] No new linter errors
- [ ] Type checking passes (if applicable)

**Manual verification:**
- [ ] Tested the primary use case manually
- [ ] Checked one edge case
- [ ] Compared behavior before/after for critical paths

**Regression check:**
- [ ] git diff shows only intended changes
- [ ] No accidental behavior changes
- [ ] No debug code left in


GATE: Do not merge until all checks pass.

If verification fails:

git revert HEAD  # or reset to before refactor
# Start over with smaller scope


</phase_verify>

Phase 5: Document (Optional)

<phase_document> If retrospective skill installed: Invoke for significant refactors.

For large refactors, capture:

What was refactored and why
Any tricky parts or gotchas discovered
Patterns that emerged (potential future skills) </phase_document>
Output Format
## Safe Refactor: [Description]

### Risk Assessment
- Risk level: [Low/Medium/High]
- Files affected: [count]
- Risk factors: [list]

### Preparation
- [x] Tests verified/written
- [x] Branch created: refactor/[name]
- [x] Current behavior documented

### Implementation
- Commits: [count]
- Approach: [brief description]

### Verification
- [x] Tests pass
- [x] Manual verification complete
- [x] No regressions detected

### Learnings (if significant)
[What you'd do differently]

NEVER
Refactor and add features in the same change
Skip the risk assessment ("it's just a small cleanup")
Make large changes without test coverage
Commit all changes in one giant commit
"Fix" bugs discovered during refactoring (note them separately)
Proceed when tests are failing
ALWAYS
Assess risk before starting
Ensure tests exist (write them if needed)
Work on a branch with escape hatch ready
Make small, incremental commits
Run tests after each logical change
Verify behavior is preserved exactly
Example

User: "Refactor the authentication module to use the new token format"

Phase 1 - Risk Assessment:

Refactor Risk Assessment:

Files affected: auth.ts, token.ts, middleware.ts, 12 test files
Risk factors: ✓ Core code, ✓ Production-critical, ✓ Written by someone else
Risk level: High

Recommendation: Break into smaller refactors:

First: Add new token format support alongside old
Second: Migrate consumers one by one
Third: Remove old format

Phase 2 - Prepare:

 Existing tests cover token generation and validation
 Created branch: refactor/token-format-v2
 Documented: Old format is JWT with RS256, new format adds typ header

Phase 3 - Implement:

Making changes incrementally...

Commit 1: "Add TokenV2 class with new format"
Commit 2: "Add feature flag for token format"
Commit 3: "Update token generation to use flag"
Tests passing after each commit ✓

Phase 4 - Verify:

 All 47 auth tests pass
 Manual test: login flow works with both formats
 Manual test: token refresh works
 git diff shows only intended changes

Ready to merge.

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