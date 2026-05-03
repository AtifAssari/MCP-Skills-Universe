---
title: debug
url: https://skills.sh/scando1993/sugar/debug
---

# debug

skills/scando1993/sugar/debug
debug
Installation
$ npx skills add https://github.com/scando1993/sugar --skill debug
SKILL.md
Systematic Debugging
Iron Law

IF >= 3 FIXES TRIED, STOP AND QUESTION THE ARCHITECTURE

Phases
1. Reproduce

Confirm the bug with a minimal, exact reproduction case.

Get the exact error message and stack trace
Write a failing test if possible
If you cannot reproduce it, you cannot fix it
2. Hypothesize

Form 3 hypotheses about the root cause.

Rank them by likelihood
Explain the reasoning behind each
Do NOT skip to fixing before hypothesizing
3. Investigate

Pick ONE investigation technique and apply it:

Binary search: narrow the problem space by halving (comment out half the code, does it still fail?)
Trace: follow the execution path from input to failure point
Instrument: add logging/assertions at key points to observe state
4. Fix

Apply a minimal, targeted change that addresses the root cause.

Explain what the fix does and why it solves the root cause
Do NOT fix symptoms — fix root causes
If the fix touches more than 10 lines, question whether it's minimal
5. Verify

Run the original reproduction case.

It must pass
The bug must no longer occur
6. Regression

Run the full test suite.

No new failures introduced
If regressions appear, your fix changed behavior — investigate before committing
Red Flags — If You Catch Yourself Thinking:
Thought	Reality
"I think I know what's wrong, let me just fix it"	You have NO hypothesis until you've reproduced. Reproduce FIRST.
"Let me try a different fix" (3rd time)	STOP. You're guessing. Question the architecture.
"The fix is too big to test incrementally"	Break it down. Every fix is testable.
"It works on my end"	Reproduce in the EXACT environment where it fails.
Rules
NEVER skip reproduction
NEVER apply more than 3 fixes without stepping back and questioning the architecture
ALWAYS verify the fix doesn't introduce regressions
Document what you tried and what you learned in progress.txt
Weekly Installs
11
Repository
scando1993/sugar
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass