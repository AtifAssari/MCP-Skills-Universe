---
rating: ⭐⭐
title: debugging-protocol
url: https://skills.sh/jwilger/agent-skills/debugging-protocol
---

# debugging-protocol

skills/jwilger/agent-skills/debugging-protocol
debugging-protocol
Installation
$ npx skills add https://github.com/jwilger/agent-skills --skill debugging-protocol
SKILL.md
Debugging Protocol

Value: Feedback -- systematic investigation produces understanding. Understanding produces correct fixes. Correct fixes prevent recurrence. Skipping investigation produces symptom fixes that hide bugs.

Purpose

Teaches a disciplined 4-phase debugging process that enforces root cause analysis before any fix attempt. Prevents the most common debugging failure mode: jumping to a fix without understanding why the problem exists.

Practices
The Iron Law: No Fixes Without Investigation

Never change code to fix a bug until you have completed root cause investigation. When you see an error and immediately know the fix, that is exactly when you are most likely to be wrong. Investigate first.

Do:

Read the complete error message and stack trace before doing anything else
Reproduce the bug consistently before investigating
Understand WHY something is broken, not just WHAT is broken

Do not:

Add a null check because you see a null pointer error (symptom fix)
Try "a few things" to see what sticks (random debugging)
Skip investigation because "this is an easy one"
Phase 1: Understand the Failure

Gather facts. Do not interpret yet.

Read the full error message -- every line, not just the first
Identify the exact file and line where the failure occurs
Reproduce the failure consistently (if it does not reproduce, that is important information)
Check recent changes: git log --oneline -10 and git diff
Note the data flow: where does the bad value come from?

Output: A clear statement of what is happening, where, and since when.

Phase 2: Find Working Examples

Compare broken against working. The difference is the bug.

Find similar code that works correctly
Compare setup, inputs, state, and configuration
Identify what differs between the working and failing case
Check dependencies: did a library update? Did an environment change?

Output: A specific difference between working and failing cases.

Phase 3: Test One Hypothesis

Form a single, explicit hypothesis. Test it with one change. Learn from the result.

State the hypothesis: "I believe the bug is caused by [X] because [evidence]"
Make ONE change to test it
Observe the result
If the hypothesis is wrong, UNDO the change completely
Form a new hypothesis incorporating what you learned

Do not change multiple things at once. If you change the import, the type, and the logic simultaneously, you cannot know which change mattered.

Output: Confirmed or refuted hypothesis with evidence.

Phase 4: Fix and Verify

Fix with confidence because you understand the root cause.

Write a failing test that reproduces the bug (if one does not already exist)
Implement the fix targeting the root cause identified in Phase 3
Verify: the new test passes, all existing tests still pass
Confirm you fixed the cause, not the symptom

Output: A fix backed by a test, with all tests green.

Escalation: Three Strikes Rule

If three fix attempts fail, stop. The problem is not what you think it is.

After the third failure:

Stop attempting fixes entirely
Document what you tried and why each attempt failed
Question your assumptions: wrong abstraction? Wrong domain model? Wrong problem entirely?
Seek a broader perspective -- architecture review, domain expert, or escalate to the user

Three failed fixes almost always signal a design problem, not a code problem. More code fixes will not help.

Example:

Attempt 1: Add caching (hypothesis: slow queries) -> Still slow
Attempt 2: Add index (hypothesis: missing index) -> Still slow
Attempt 3: Eager loading (hypothesis: N+1) -> Still slow
STOP. Profile the system.
Result: 90% of time in external API call. Not a database problem at all.

Enforcement Note
Standalone mode: Advisory. The Iron Law is self-enforced.
Pipeline mode: Gating. Debugging evidence is required before fix commits pass the TDD gate.

Hard constraints:

Iron Law (investigate before fix): [H]
Three Strikes escalation: [RP]
Constraints
Iron Law: The temptation to skip investigation is strongest when the fix seems obvious. That is exactly when investigation is most valuable -- because "obvious" fixes that are wrong waste more time than investigation would have cost. If you're reasoning about why THIS bug is the exception that doesn't need investigation, you're violating the Iron Law.
Three Strikes: After three failed hypotheses, the problem is not what you think it is. "Stop" means stop fixing and return to investigation. It does not mean stop working entirely. Re-examine your assumptions, widen your investigation, look at adjacent systems. If you still can't identify the root cause, escalate.
Undo failed hypotheses: "Undo completely" means the codebase returns to exactly the state before the hypothesis was tested. Not "mostly undone with a few improvements kept." Not "undone in the main file but I left the debug logging." Every change from the failed hypothesis is reverted.
Verification

After debugging guided by this skill, verify:

 Completed Phase 1 investigation before any code changes
 Read the complete error message (not just the first line)
 Reproduced the bug consistently
 Found a working example to compare against
 Stated an explicit hypothesis before each fix attempt
 Made only one change per hypothesis test
 Undid failed hypotheses before trying new ones
 Wrote or confirmed a failing test before implementing the fix
 Verified all tests pass after the fix
 Did not exceed three fix attempts without escalating

If any criterion is not met, revisit the relevant phase.

Dependencies

This skill works standalone with no required dependencies. It integrates with:

tdd: When a test fails unexpectedly during TDD, this skill guides investigation before modifying code
user-input-protocol: When debugging reaches an ambiguous decision point, pause and ask the user rather than guessing
domain-modeling: If three fixes fail, the root cause may be a domain modeling problem -- escalate to domain review

Missing a dependency? Install with:

npx skills add jwilger/agent-skills --skill tdd

Weekly Installs
99
Repository
jwilger/agent-skills
GitHub Stars
2
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass