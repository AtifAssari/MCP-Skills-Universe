---
title: finish
url: https://skills.sh/scando1993/sugar/finish
---

# finish

skills/scando1993/sugar/finish
finish
Installation
$ npx skills add https://github.com/scando1993/sugar --skill finish
SKILL.md
Branch Finishing and PR Preparation
Iron Law

NEVER MERGE WITHOUT ALL CHECKS PASSING

Steps
1. Verify

Confirm the branch is ready for review.

Run the full test suite — all tests must pass
Run typecheck and lint — zero errors
Verify all acceptance criteria from the story/PRD are met
Check for leftover debug code, TODOs, or commented-out blocks
Ensure no untracked files that should be committed
2. Rebase

Bring the branch up to date with the target branch.

git fetch origin
git rebase origin/main

Resolve any conflicts carefully — do not blindly accept incoming or current
After rebase, re-run all quality checks (tests, typecheck, lint)
If rebase conflicts are extensive, consider whether the branch diverged too far
3. Clean History

Ensure commits tell a clear story.

Each commit should be atomic — one logical change per commit
Commit messages should explain WHY, not just WHAT
Squash fixup commits (typo fixes, lint fixes) into their parent commit
Reorder commits so dependencies come before dependents
Every commit in the history should pass quality checks independently
4. Write PR Description

Create a clear, reviewable pull request description.

Title: Concise summary of what the PR does (under 72 characters)
Summary: 2-3 sentences explaining the change and its motivation
Changes: Bulleted list of what was added, modified, or removed
Testing: How the changes were tested, what to verify
Screenshots: If UI changes, include before/after
Related issues: Link to the story, issue, or PRD that motivated this work
5. Self-Review

Review your own diff before requesting review from others.

Read every changed line as if someone else wrote it
Check for security issues (hardcoded secrets, injection vectors)
Check for performance issues (N+1 queries, unbounded loops)
Verify error handling is adequate
Confirm naming is clear and consistent
6. Push and Create PR

Push the branch and open the pull request.

git push origin <branch-name>
gh pr create --title "<title>" --body "<description>"

Set appropriate reviewers
Add relevant labels
Link to the related issue or story
Do not merge your own PR unless explicitly permitted
Red Flags — If You Catch Yourself Thinking:
Thought	Reality
"Tests mostly pass, one flaky test is fine"	ALL tests must pass. Fix the flaky test or skip it with documentation.
"The commit history is messy but the code is right"	Messy history makes review harder and bisect useless. Clean it up.
"I'll write the PR description later"	The PR description IS the review guide. Write it now while context is fresh.
"This is a small change, no need for self-review"	Small changes cause big bugs. Review every line.
Rules
All quality checks must pass before pushing
Every commit must be atomic and independently valid
PR description is required — never create a PR without one
Self-review before requesting external review
Never force-push to a shared branch without coordinating with collaborators
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