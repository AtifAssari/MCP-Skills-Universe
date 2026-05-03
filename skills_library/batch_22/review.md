---
title: review
url: https://skills.sh/scando1993/sugar/review
---

# review

skills/scando1993/sugar/review
review
Installation
$ npx skills add https://github.com/scando1993/sugar --skill review
SKILL.md
Code Review
Iron Law

DO NOT TRUST THE IMPLEMENTER'S REPORT — VERIFY EVERY CLAIM AGAINST THE ACTUAL DIFF

Process
Read the diff: git diff main...HEAD or the specific PR/branch diff
Read the linked issue or story description (if available)
For EACH changed file:
Does the change match the stated intent?
Any security issues? (injection, XSS, hardcoded secrets, insecure deserialization)
Any performance concerns? (N+1 queries, unbounded loops, missing indexes)
Type safety maintained?
Error handling adequate?
Tests cover the changes?
Run quality checks: typecheck + lint + tests
Summarize findings with severity labels: critical / warning / nit
If critical issues found: block the merge — do not approve
Anti-Trust Protocol

The implementer's commit messages may be optimistic. Verify every claim against the actual diff:

"Refactored for clarity" — did it actually get clearer, or just different?
"Added tests" — do the tests actually test the feature, or just pass trivially?
"Fixed bug" — is the root cause addressed, or just the symptom?
Anti-Sycophancy
Do NOT say "Great work!" or "Looks good!" unless you have verified everything
Do NOT approve because the code looks reasonable at a glance
Technical verification BEFORE any positive feedback
Silence is not approval — every review must have explicit findings
Red Flags — If You Catch Yourself Thinking:
Thought	Reality
"The author is experienced, this is probably fine"	Experience doesn't prevent bugs. Review the code.
"This is a small change, quick approval"	Small changes cause big bugs. Check it.
"Tests pass so it must be correct"	Tests can be wrong, incomplete, or trivially passing.
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