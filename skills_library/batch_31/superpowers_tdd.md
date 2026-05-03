---
title: superpowers-tdd
url: https://skills.sh/anthonylee991/gemini-superpowers-antigravity/superpowers-tdd
---

# superpowers-tdd

skills/anthonylee991/gemini-superpowers-antigravity/superpowers-tdd
superpowers-tdd
Installation
$ npx skills add https://github.com/anthonylee991/gemini-superpowers-antigravity --skill superpowers-tdd
SKILL.md
TDD Skill
When to use this skill
new features that can be unit tested
bug fixes (always add a regression test if practical)
refactors (protect behavior with tests first)
Rules
Prefer red -> green -> refactor.
If tests are hard, still add verification: minimal repro script, integration test, or clear manual steps.
Keep tests focused: one behavior per test where possible.
Name tests by behavior, not implementation details.
Process
Define the behavior change (what should be true after).
Write/adjust a test to capture it (make it fail first if possible).
Implement the minimal change to pass.
Refactor if needed (keep passing).
Run the relevant test suite + any linters.
Output requirements

When you change code, include:

what tests you added/changed
how to run them
what they prove
Weekly Installs
34
Repository
anthonylee991/g…igravity
GitHub Stars
740
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass