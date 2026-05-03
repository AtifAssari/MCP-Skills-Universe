---
title: issue-progress-tracking
url: https://skills.sh/yonatangross/orchestkit/issue-progress-tracking
---

# issue-progress-tracking

skills/yonatangross/orchestkit/issue-progress-tracking
issue-progress-tracking
Installation
$ npx skills add https://github.com/yonatangross/orchestkit --skill issue-progress-tracking
SKILL.md
Issue Progress Tracking

Ceremony guide for tracking GitHub issue progress via gh CLI. Ensures issues stay updated as work progresses from start to PR.

Quick Start
/ork:issue-progress-tracking 123

Phase 1: Start Work

Label the issue and create a feature branch:

# Move issue to in-progress
gh issue edit $ARGUMENTS[0] --add-label "status:in-progress" --remove-label "status:todo"
gh issue comment $ARGUMENTS[0] --body "Starting work on this issue."

# Create feature branch
git checkout -b issue/$ARGUMENTS[0]-brief-description


Rules:

Always branch from the default branch (main/dev)
Branch name format: issue/<number>-<brief-description>
Never work directly on main/dev
Phase 2: During Work — Small Commits

Commit after each logical step, not at the end. Every commit references the issue:

# Each commit references the issue number
git commit -m "feat(#$ARGUMENTS[0]): add user model

Co-Authored-By: Claude <noreply@anthropic.com>"


Rules:

One logical change per commit (atomic)
Reference issue in every commit: type(#N): description
Commit early and often — don't accumulate a massive diff
Phase 3: Report Progress (Long Implementations)

For multi-step work, post progress updates:

gh issue comment $ARGUMENTS[0] --body "Progress update:
- Completed: database schema, API endpoints
- In progress: frontend components
- Remaining: tests, documentation"


When to post updates:

After completing a major milestone
When blocked or changing approach
Before stepping away from a long task
Phase 4: Complete Work

Create the PR and update labels:

# Create PR that closes the issue
gh pr create \
  --title "feat(#$ARGUMENTS[0]): brief description" \
  --body "Closes #$ARGUMENTS[0]

## Changes
- Change 1
- Change 2

## Test Plan
- [ ] Unit tests pass
- [ ] Manual verification"

# Update issue status
gh issue edit $ARGUMENTS[0] --add-label "status:in-review" --remove-label "status:in-progress"

Rules Quick Reference
Rule	Impact	What It Covers
Start Work Ceremony	HIGH	Branch creation, label updates, initial comment
Small Commits	HIGH	Atomic commits referencing issues

Total: 2 rules across 2 categories

Key Decisions
Decision	Choice	Rationale
Label prefix	status:	Consistent with GitHub conventions
Branch format	issue/<N>-desc	Links branch to issue automatically
Commit reference	type(#N):	Conventional commits + issue linking
Progress comments	Manual	Keeps humans in the loop
Common Mistakes
Starting work without labeling — team loses visibility into who is working on what
Giant commits at the end — makes review harder and history useless for bisect
Forgetting to link PR to issue — issue stays open after merge
Not updating labels on PR creation — issue shows "in-progress" during review
Closing issues manually with gh issue close — issues are closed ONLY by merging a PR with Closes #N in the body. During work, comment progress with gh issue comment; never close directly.
Related Skills
ork:commit — Commit with conventional format
ork:fix-issue — Full issue resolution workflow
ork:implement — Feature implementation with parallel agents
ork:create-pr — Create pull requests
Weekly Installs
124
Repository
yonatangross/orchestkit
GitHub Stars
163
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass