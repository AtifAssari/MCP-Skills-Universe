---
rating: ⭐⭐⭐
title: debug-to-fix
url: https://skills.sh/elliotjlt/claude-skill-potions/debug-to-fix
---

# debug-to-fix

skills/elliotjlt/claude-skill-potions/debug-to-fix
debug-to-fix
Installation
$ npx skills add https://github.com/elliotjlt/claude-skill-potions --skill debug-to-fix
SKILL.md
Debug to Fix
Prerequisites

This elixir works best with these skills installed:

Skill	Purpose	If Missing
rubber-duck	Structured problem clarification	Falls back to built-in questions
prove-it	Verification enforcement	Falls back to built-in verification
retrospective	Document learnings	Skipped (optional phase)

The elixir degrades gracefully - it will use built-in fallbacks for missing skills.

When To Activate
Instructions
Phase 1: Clarify

<phase_clarify> If rubber-duck skill installed: Invoke it now.

If not installed, ask:

Before we debug, let me understand the problem:

Expected: What should happen?
Actual: What actually happens?
Tried: What have you already attempted?
Changed: What changed before this broke?

GATE: Do not proceed until you can state the problem in one sentence: "When I [action], I expect [expected], but instead [actual]."

Write this sentence before continuing. </phase_clarify>

Phase 2: Investigate

<phase_investigate> Objective: Find the root cause, not just symptoms.

Investigation checklist:

Reproduce: Can you trigger the bug reliably?

 Yes, every time
 Sometimes (note conditions)
 Haven't tried yet → Try now

Isolate: Where does the bug live?

 Identified the file(s)
 Identified the function(s)
 Narrowed to specific lines

Understand: Why does it fail?

 Read the actual error (not just the message)
 Checked the data/state at failure point
 Understood the expected flow vs actual flow

Investigation techniques (try in order):

1. Read the error message completely - what does it actually say?
2. Add logging/print at the failure point - what are the actual values?
3. Trace backwards - where do the bad values come from?
4. Check recent changes - git diff, git log
5. Rubber duck the code flow aloud


GATE: Do not proceed until you can answer:

"The bug happens because [specific cause]"
"I know this because [evidence]"

Write both sentences before continuing. </phase_investigate>

Phase 3: Fix

<phase_fix> Now implement the fix.

Before writing code, state:

What you're changing
Why this fixes the root cause (not just symptoms)
Risk of this change breaking something else

Implement the minimal fix. Resist the urge to refactor nearby code. </phase_fix>

Phase 4: Verify

<phase_verify> If prove-it skill installed: Invoke it now.

If not installed:

Verification checklist:

 Original bug no longer reproduces
 Tested the exact scenario from Phase 1
 Checked for regressions in related functionality
 Tests pass (if applicable)

GATE: Do not declare victory until verification complete.

Show the evidence:

VERIFIED:
- [What you tested]
- [What you observed]
- [Why this confirms the fix]


</phase_verify>

Phase 5: Document (Optional)

<phase_document> If retrospective skill installed: Invoke it for significant bugs.

If not installed or bug was minor: Skip this phase.

For significant debugging sessions (>15 min), capture:

What the bug was
Why it was hard to find
What you'd do differently </phase_document>
Output Format
## Debug Session: [Brief description]

### Problem Statement
When I [action], I expect [expected], but instead [actual].

### Root Cause
The bug happens because [cause].
Evidence: [how you know]

### Fix
[What you changed and why]

### Verification
- [x] Original bug fixed
- [x] [Other checks performed]

### Learnings (if significant)
[What you'd do differently]

NEVER
Jump to fixes before completing Phase 1 (clarify)
Guess at root cause without evidence (Phase 2)
Declare "fixed" without verification (Phase 4)
Skip gates because "I already know the answer"
Refactor unrelated code while fixing a bug
ALWAYS
Write the problem statement sentence before investigating
State root cause with evidence before fixing
Verify the exact original scenario after fixing
Keep fixes minimal and focused
Example

User: "The login is broken, I don't know why"

Phase 1 - Clarify:

Before we debug, help me understand:

What should happen when you log in?
What actually happens?
What have you tried?
Did anything change recently?

[User answers]

Problem statement: "When I submit the login form, I expect to be redirected to /dashboard, but instead I see a blank page with no errors."

Phase 2 - Investigate:

Let me investigate...

Checked network tab: POST /api/login returns 200 ✓
Checked console: No errors ✓
Checked redirect logic: router.push('/dashboard') is called
Added logging: redirect fires but page doesn't change
Checked recent commits: Found change to middleware yesterday

Root cause: "The bug happens because new auth middleware redirects /dashboard back to /login for users without 'verified' flag, creating a loop that results in blank page." Evidence: "Middleware logs show redirect loop, user object missing 'verified' field."

Phase 3 - Fix:

Fixing: Add 'verified: true' to user object after successful login Why: Root cause is missing field, not redirect logic Risk: Low - only affects login success path

Phase 4 - Verify:

VERIFIED:

Logged in with test user → redirected to /dashboard ✓
No redirect loop in network tab ✓
Middleware logs show single redirect ✓
Existing tests pass ✓
Weekly Installs
8
Repository
elliotjlt/claud…-potions
GitHub Stars
55
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass