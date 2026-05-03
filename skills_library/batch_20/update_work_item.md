---
title: update-work-item
url: https://skills.sh/squirrel289/pax/update-work-item
---

# update-work-item

skills/squirrel289/pax/update-work-item
update-work-item
Installation
$ npx skills add https://github.com/squirrel289/pax --skill update-work-item
SKILL.md
Update Work Item
Overview

Update progress on an existing work item: change status, record actual effort, add test results, mark related commits, validate dependencies, and add implementation notes as work progresses.

When to Use

Update a work item when:

Starting work (change status to in-progress)
Completing implementation (change status to ready-for-review)
Recording actual hours spent
Adding related commit hashes
Logging test results or CI status
Adjusting estimates based on new information
Adding implementation notes or blockers
Validating dependencies before closing
When NOT to Use

Skip updates for:

Creating new items (use create-work-item skill)
Finalizing and archiving (use finalize-work-item skill)
Minor comments (just edit as needed, no skill required)
Frontmatter Fields
Status and Status Reason Fields
status: proposed | ready | in-progress | ready-for-review | closed
status_reason: null | success | obsolete | redundant | superseded | cancelled

Status	status_reason	Meaning	When to Use
proposed	(none)	Work item proposed but not yet ready	Initial creation
ready	(none)	Work item ready to start	Prior to in-progress
in-progress	(none)	Active development	Actively working
ready-for-review	(none)	Impl done, awaiting review/tests	Tests running, PR submitted
closed	success	Finished successfully	All criteria met, merged
closed	obsolete	No longer relevant	Market changed, approach outdated
closed	redundant	Duplicate item	Same work in another item
closed	superseded	Made moot by other item	Different item solves it better
closed	cancelled	Work stopped	Stopped, won't implement

Important: Before transitioning to closed, validate that all items in links.depends_on are already in closed status.

Effort Tracking
estimated: 20 # Set when created (hours as decimal)
actual: 18 # Update as work progresses, finalize when complete
completed_date: null # Set when status = closed (YYYY-MM-DD format)


Guidelines:

estimated: Set once, don't change unless scope significantly shifts
actual: Start as null, update when complete
completed_date: Set only when moving to closed status
Commit Tracking
commits:
  6d8c044: 'feat(sdk): initial FilterAdapter interface'
  f00459b: 'feat(filters): implement selectattr and map'
  a1b2c3d: 'docs: add filter usage examples'


Record commit SHAs (7+ character hashes or 40-character full hashes) mapped to their commit messages. Helps trace implementation back to work items.

To get commit message:

git log <short_hash> -n 1 --pretty=format:"%s"

Test Results
test_results:
  - timestamp: 2024-06-01T12:00:00Z
    note: 'https://github.com/squirrel289/temple/actions/runs/12345678'


Record test results with timestamps:

test_results:
  - timestamp: 2024-06-01T12:00:00Z
    note: 'All 47 tests pass, coverage 89%'
  - timestamp: 2024-06-02T10:00:00Z
    note: '3 test failures in test_renderer.py (see PR comments)'

Dependencies
links:
  depends_on:
    - '[[wi-054_complete_temple_native.md]]'
    - '[[wi-043_implement_template_syntax_validation.md]]'


Update if new dependencies emerge during implementation. Critical: Before closing a work item, verify all items in links.depends_on are already closed.

Workflow: Updating Work Items
1. Moving to In-Progress

When starting work (changing status from proposed or ready to in-progress):

Automatically create and checkout a local feature branch via feature-branch-management skill:

# Triggered automatically when status: in-progress
feature-branch-management create feature/wi-060

Branch naming convention: feature/wi-<id> (e.g., feature/wi-060)
Branch is created from main and checked out automatically
If the branch already exists, it is checked out
This ensures all work is isolated and traceable to the work item

Update the work item file frontmatter:

---
title: 'Implement FilterAdapter'
id: 'wi-060'
status: in-progress
priority: high
estimated: 20
actual: 2
completed_date: null
status_reason: null
notes:
  - timestamp: 2024-06-01T12:00:00Z
    note: |
      Started implementation of FilterAdapter in packages/core/.
      Initial focus: selectattr and map filters.
---


Update actual as work progresses:

actual: 5 # Increment as work progresses, use decimals (e.g., 5.5 for 5h 30m)

2. Recording Actual Hours

As work progresses, update actual:

estimated: 20
actual: 6 # 2 hours initial + 4 more hours


Update periodically (after major milestones, at end of session) so you have a sense of actual time investment.

3. Adding Related Commits

When work is committed, record the commit SHA and message:

commits:
  6d8c044: 'feat(sdk): FilterAdapter interface'
  f00459b: 'feat(filters): selectattr and map'
  a1b2c3d: 'docs: add filter usage examples'


Use short (7-character) or full (40-character) hashes as keys, with commit subject as the value.

Keep hashes in chronological order. Multiple commits are fine—they show the evolution of the work.

4. Transitioning to Ready-for-Review

When implementation is done and ready for review, move to ready-for-review:

Sync branch with main via feature-branch-management:

# Triggered automatically when status: ready-for-review
feature-branch-management sync --base=main

Rebases feature branch on latest main to avoid conflicts
Ensures clean commit history for PR review
If conflicts detected, will prompt with suggested resolution steps

Create Pull Request via create-pr skill (automatic):

# Triggered automatically when status: ready-for-review
create-pr work_item=wi-060

PR title auto-generated: "wi-060: Implement FilterAdapter"
PR description auto-generated from work item notes + commit history
PR links to work item via "Closes wi-060" reference
PR URL recorded in work item metadata

Update work item frontmatter:

status: ready-for-review
actual: 18 # Finalize effort
status_reason: null
links:
  pull_requests:
    - 'https://github.com/templjs/templjs/pull/247'
notes:
  - timestamp: 2024-06-01T12:00:00Z
    note: |
      Implementation complete. All filters implemented with type signatures.
      PR submitted for review: #247
      Awaiting code review and approval.


Do NOT set completed_date or status_reason yet.

5. Recording Test Results

After running tests:

status: ready-for-review
test_results:
  - timestamp: 2024-06-01T12:00:00Z
    note: 'https://github.com/templjs/templjs/actions/runs/98765432'
  - timestamp: 2024-06-02T08:00:00Z
    note: |
      CI results:
      - 98 tests pass
      - 2 tests fail in test_filter_edge_cases.py (filter_args validation)
      - Coverage 87% (target 85%)

      Known issues:
      - Filter arg validation too strict for varargs
      - Will fix in follow-up PR


If tests fail, add notes on what needs fixing. Update status back to in-progress if rework needed:

status: in-progress
actual: 19
test_results:
  - timestamp: 2024-06-02T10:00:00Z
    note: 'Test failures exposed issue with varargs handling. Reworking in feature/wi-060.'
notes:
  - timestamp: 2024-06-02T10:00:00Z
    note: 'Tests exposed issue with varargs handling. Working on fix.'

6. Moving to Closed

When all tests pass, work is approved, and PR is merged:

Verify dependencies closed: Before moving to closed, check that all items in links.depends_on have status: closed

Update work item frontmatter:

status: closed
status_reason: success
actual: 22
completed_date: 2026-02-12
test_results:
  - timestamp: 2024-06-01T12:00:00Z
    note: 'https://github.com/templjs/templjs/actions/runs/98765432'
links:
  pull_requests:
    - 'https://github.com/templjs/templjs/pull/247'
commits:
  a1b2c3d: 'chore: merge PR #247 (FilterAdapter implementation)'
notes:
  - timestamp: 2024-06-02T15:00:00Z
    note: |
      All acceptance criteria met:
      - FilterAdapter interface implemented and documented
      - Core filters (selectattr, map, join, default) working
      - 95% test coverage
      - Code reviewed and approved
      - Merged to main


Set status_reason to one of:

success: Normal completion with acceptance criteria met
obsolete: Item no longer needed (note why in notes)
redundant: Duplicate of another item (reference it via links)
superseded: Made moot by another item (reference it via links)
cancelled: Work stopped before completion (note why in notes)

Leave file in /backlog/. The finalize-work-item skill handles archiving to /backlog/archive/.

7. Adjusting Estimates

If scope changes significantly during work:

estimated: 28 # Increased from 20 due to validation requirements
actual: 14
notes:
  - timestamp: 2024-06-01T12:00:00Z
    note: |
      Scope expanded: discovered need for JSON Schema validation in filter 
      arguments. Adjusted estimate by +8 hours.


Or revert the work item to proposed if scope change is fundamental:

status: proposed
estimated: 28
actual: 14
notes:
  - timestamp: 2024-06-01T12:00:00Z
    note: 'Scope significantly expanded. Reverting to proposed for re-estimation.'

8. Updating Dependencies

If new dependencies discovered during work:

links:
  depends_on:
    - '[[wi-054_complete_temple_native.md]]'
    - '[[wi-044_implement_semantic_validation.md]]' # Added: type checking needed


Update the work item file to reflect these. Document in notes why the dependency was added.

Examples
Example 1: Feature Work Progress

Initial creation (status: proposed):

---
title: 'Implement FilterAdapter'
id: 'wi-060'
status: proposed
priority: high
estimated: 20
actual: null
completed_date: null
status_reason: null
links:
  depends_on:
    - '[[wi-054_complete_temple_native.md]]'
---


After moving to in-progress (2 hours):

status: in-progress
actual: 2
notes:
  - timestamp: 2024-06-01T12:00:00Z
    note: |
      Started with interface design and type signatures.
      SelectAttr filter drafted.


After ready-for-review (18 hours):

status: ready-for-review
status_reason: null
actual: 18
commits:
  6d8c044: 'feat(sdk): FilterAdapter interface'
  f00459b: 'feat(filters): selectattr, map, join, default'
links:
  pull_requests:
    - 'https://github.com/templjs/templjs/pull/247'
test_results:
  - timestamp: 2024-06-01T18:00:00Z
    note: 'https://github.com/templjs/templjs/actions/runs/12345678'
notes:
  - timestamp: 2024-06-01T18:00:00Z
    note: |
      Implementation complete. All tests pass. 95% coverage.
      PR #247 submitted for review.


After merge to closed (22 hours):

status: closed
status_reason: success
actual: 22
completed_date: 2026-02-12
test_results:
  - timestamp: 2024-06-01T18:00:00Z
    note: 'https://github.com/templjs/templjs/actions/runs/12345678'
links:
  pull_requests:
    - 'https://github.com/templjs/templjs/pull/247'
commits:
  6d8c044: 'feat(sdk): FilterAdapter interface'
  f00459b: 'feat(filters): selectattr, map, join, default'
  a1b2c3d: 'merge: PR #247 FilterAdapter implementation'
notes:
  - timestamp: 2024-06-02T12:00:00Z
    note: |
      Merged to main. All acceptance criteria met.
      Ready for finalization.

Example 2: Bug Fix with Rework

Starting work:

---
title: 'Fix elif parsing edge case'
id: 'wi-059'
status: in-progress
estimated: 4
actual: 1
---


Test failure (rework needed):

status: in-progress
actual: 3
test_results:
  - timestamp: 2024-06-01T10:00:00Z
    note: 'Local: 1 test fails in test_parser.py::test_consecutive_elif'
notes:
  - timestamp: 2024-06-01T10:00:00Z
    note: |
      Found deeper issue: elif blocks interfere when nested.
      Need to refactor block termination logic.
      Revising approach—effort may exceed estimate.


Resolution (ready-for-review):

status: ready-for-review
actual: 7
estimated: 4
commits:
  abc1234: 'fix(parser): elif block termination logic'
test_results:
  - timestamp: 2024-06-01T14:00:00Z
    note: 'https://github.com/templjs/templjs/actions/runs/87654321'
notes:
  - timestamp: 2024-06-01T14:00:00Z
    note: |
      Fixed by refactoring block_ends() logic. Took longer due to edge cases.
      All tests now pass including new consecutive_elif tests.
      PR submitted for review.

Example 3: Spike/Research Update
---
title: 'Evaluate expression engines'
id: 'wi-061'
status: in-progress
estimated: 16
actual: 8
notes:
  - timestamp: 2024-06-01T08:00:00Z
    note: |
      Evaluation candidates:
      1. JMESPath - mature, good for JSON, limited type support
      2. Custom recursive descent - flexible, small footprint
      3. meval - lightweight Python evaluator

      Progress:
      - JMESPath prototype working (2h)
      - Custom parser WIP (6h) - complexity clear now, drafting comparison doc

      Leaning toward option 2 (custom) due to control of type system.
---

Tips & Conventions
Atomic Updates

Each update should correspond to a logical work milestone:

End of session: time tracking
After tests run: test results
After commit: commit hash
Status change: full progress summary

Don't update work items excessively—focus on meaningful changes.

Notes Field

Use notes for:

Progress summary
Blockers or issues
Scope changes
Decision points
Follow-up items

Avoid: detailed implementation notes (keep in commit messages instead)

Time Tracking Accuracy

Record hours regularly:

At end of each session
After significant milestone
Final tally when completed

Use decimals for partial hours (e.g., 5.5 for 5 hours 30 minutes).

Commit Message Integration

Reference work items in commit messages:

feat(filters): implement selectattr and map

Implements core filtering operations for FilterAdapter.
Supports filtering sequences by attribute value and projection.

Closes wi-60
See backlog/wi-060_implement_filter_adapter.md


Then update the work item with the commit hash.

Dependency Validation

Before marking a work item as closed:

Check the links.depends_on section
Verify each referenced work item has status: closed
If any depends_on items are not closed, leave this item at ready-for-review with a note explaining what's blocking closure

Example:

status: ready-for-review
notes:
  - timestamp: 2024-06-02T15:00:00Z
    note: |
      Implementation complete and tested. Awaiting closure of:
      - [[wi-054_complete_temple_native.md]] (currently in-progress)
      - [[wi-043_implement_syntax_validation.md]] (currently ready-for-review)

      Ready to move to closed once dependencies are resolved.

Common Patterns
Weekly Status Update

Review active work items weekly:

status: in-progress
actual: 12 # Update from 10
notes:
  - timestamp: 2024-06-08T17:00:00Z
    note: |
      Week of Feb 10: 2 hours progress (mid-week catchup).
      Current blockers: Decision on filter signature format—waiting for architecture review.
      Expected completion: Feb 17

Handling Blockers
notes:
  - timestamp: 2024-06-01T14:00:00Z
    note: |
      BLOCKED: Waiting for ADR-006 decision on expression language.
      Cannot finalize filter syntax without it.
      Unblocked when: ADR merged and decision published
      Impact: Pushed completion target to 2026-02-20

Scope Creep Recognition
notes:
  - timestamp: 2024-06-01T14:00:00Z
    note: |
      Original estimate: 12 hours (selectattr, map, join)
      Current scope: +default filter + type validation = ~18 hours likely
      Recommendation: Create follow-up item for advanced filters, limit this to core 3.

Tips & Conventions
Atomic Updates

Each update should correspond to a logical work milestone:

End of session: time tracking
After tests run: test results
After commit: commit hash
Status change: full progress summary

Don't update work items excessively—focus on meaningful changes.

Notes Field

Use notes for:

Progress summary
Blockers or issues
Scope changes
Decision points
Follow-up items

Avoid: detailed implementation notes (keep in commit messages instead)

Time Tracking Accuracy

Record hours regularly:

At end of each session
After significant milestone
Final tally when completed

Use decimals for partial hours (e.g., 5.5 for 5 hours 30 minutes).

Commit Message Integration

Reference work items in commit messages:

feat(filters): implement selectattr and map

Implements core filtering operations for FilterAdapter.
Supports filtering sequences by attribute value and projection.

Closes wi-60
See backlog/wi-060_implement_filter_adapter.md


Then update the work item with the commit hash.

Related Skills
create-work-item: For creating new work items from scratch
feature-branch-management: Invoked automatically on status transitions (create branch on in-progress, sync on ready-for-review)
create-pr: Invoked automatically when status → ready-for-review (create PR from feature branch)
handle-pr-feedback: For addressing PR review feedback and managing rework
resolve-pr-comments: For addressing specific code review comments
finalize-work-item: For archiving completed work items after merge
git-commit: For recording commits that can be linked in commits
Weekly Installs
9
Repository
squirrel289/pax
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass