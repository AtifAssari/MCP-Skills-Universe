---
rating: ⭐⭐⭐
title: create-work-item
url: https://skills.sh/squirrel289/pax/create-work-item
---

# create-work-item

skills/squirrel289/pax/create-work-item
create-work-item
Installation
$ npx skills add https://github.com/squirrel289/pax --skill create-work-item
SKILL.md
Create Work Item
Overview

Create a new work item (backlog entry) in /backlog/ with consistent structure, YAML metadata, and conventions. Work items track features, bugs, spikes, and tasks with clear goals, dependencies, and acceptance criteria.

When to Use

Create a work item when:

Starting a new feature, spike, or task
Documenting a well-scoped request or bug
Breaking down larger epics into tracked subtasks
Proposing architectural changes or experiments
Establishing clear success criteria before implementation
When NOT to Use

Skip work items for:

Trivial one-off fixes (can be done directly)
Exploratory work without clear scope (start with spike first)
Time-critical hotfixes (commit directly, backlog after)
Duplicate items (update existing instead, see update-work-item skill)
Work Item Lifecycle
Created (not_started)
    ↓
Implementation (in_progress)
    ↓
Review + Testing (testing)
    ↓
Completed (completed)
    ↓
Archived (to archive/)

Backlog Structure

Directory: /backlog/ (current items) or /backlog/archive/ (completed/superseded)

Naming Convention: <number>_<slug>.md where:

<number>: Sequential integer (e.g., 54, 55, 56)
<slug>: Kebab-case description (e.g., complete_temple_native, implement_adapter_spec)

Numbering: Continue from highest existing number in /backlog/ (not archive)

File Structure
1. YAML Frontmatter
---
title: "Human-readable work item title"
id: <number>
status: not_started | in_progress | testing | completed
state_reason: null  # Set only when status = completed (success | obsolete | redundant | superseded | cancelled)
priority: low | medium | high | critical
complexity: low | medium | high
estimated_hours: <number>
actual_hours: null  # Set when completed
completed_date: null  # Set when completed
related_commit: []  # Array of commit hashes/refs
test_results: null  # URL or description of test results
dependencies:
  - "[[<other_item_number>_<slug>.md]]"
related_backlog:
  - "archive/<number>_<slug>.md"
related_spike:
  - "archive/<number>_<slug>.md"
notes:
  - timestamp: 2024-06-01T12:00:00Z
    user: @john
    note: |
      Optional additional context or implementation notes
---

2. Content Sections
## Goal

One-paragraph summary of what this work item achieves. Answer: "What is the end state?"

## Background

Context, motivation, or prior work. Answer: "Why are we doing this?"

## Tasks

Numbered list of implementation steps or subtasks:

1. **Task Name**: Brief description
   - Sub-point if needed
   - Code example if helpful

2. **Next Task**: Description

## Deliverables

What artifacts or code changes will result:

- New file/module: `path/to/file.py`
- Modified behavior: "CLI now accepts --flag"
- Documentation: "Updated architecture guide"

## Acceptance Criteria

Clear, verifiable markers of completion:

- [ ] All new tests pass (test_*.py)
- [ ] Code coverage > 80%
- [ ] Documented in docs/ (README or ADR)
- [ ] Reviewed and merged to main

Workflow: Creating a Work Item
1. Determine Next ID
Check highest numbered file in /backlog/ (not archive)
Next ID = max existing + 1

Example: If 56_jinja2_adapter_prototype.md is highest, next = 57_*

2. Draft Frontmatter
---
title: "Implementation feature name"
id: 57
status: not_started
state_reason: null
priority: high  # or medium/low/critical
complexity: medium  # or low/high
estimated_hours: 24
actual_hours: null
completed_date: null
related_commit: []
test_results: null
dependencies:
  - "[[54_complete_temple_native.md]]"  # Links to other work items
related_backlog:
  - "archive/06_rendering_engine.md"  # If refining prior work
notes:
  - timestamp: 2024-06-01T12:00:00Z
    user: @john
    note: Any additional context or decision points
---


Status Values:

not_started: Ready to begin
in_progress: Active work
testing: Implementation done, awaiting review/test results
completed: Finished (may have different reasons—see state_reason)

state_reason (used only when status: completed):

success: Work completed successfully, all criteria met
obsolete: Item no longer relevant (market/approach changed)
redundant: Duplicate of another work item
superseded: Made moot by another item (note which one)
cancelled: Work stopped, won't implement (note why)

Priority:

low: Nice-to-have, can be deferred
medium: Standard work item
high: Important, plan next
critical: Blocking other work

Complexity:

low: ≤6 hours, isolated change
medium: 6-20 hours, affects multiple areas
high: 20+ hours, architectural or cross-cutting
3. Write Goal Section

One sentence to one paragraph:

## Goal

Implement `FilterAdapter` interface in the core temple package to provide built-in filters for data transformation: `selectattr`, `map`, `join`, `default`, with type annotations.

4. Add Context Sections

Background: Why this matters, prior decisions, linked research

## Background

Filter support is required for ADR-003 (adapter architecture). Current prototype has hardcoded filter logic; ADR-005 proposes a pluggable FilterAdapter contract. This work implements the concrete contract in `temple/sdk/adapter.py` with 4 core filters and test coverage.


Tasks: Numbered, actionable steps

## Tasks

1. **Design FilterAdapter contract**
   - Extend `temple/sdk/adapter.py` with `FilterAdapter` class
   - Define `apply(input: Any, filter_name: str, args: List) -> Any`
   - Create `FilterSignature` with type hints

2. **Implement core filters in FilterRegistry**
   - `selectattr(objects, attr, value)` → List[T] where T.attr == value
   - `map(objects, attr)` → List[extracted]
   - `join(items, separator)` → str
   - `default(value, fallback)` → value if truthy else fallback

3. **Add type annotations and validation**
   - Each filter registers `FilterSignature` with parameter types
   - Validate filter arguments at parse time

4. **Write unit and integration tests**
   - Test each filter behavior
   - Test error cases (type mismatches, missing attributes)

5. Add Deliverables
## Deliverables

- `temple/sdk/adapter.py` extended with `FilterAdapter` and `FilterSignature`
- `temple/sdk/filters.py` with core filter implementations
- Unit tests in `tests/test_filters.py` (>80% coverage)
- Integration test in `tests/test_renderer_filters.py`
- Updated API docs in `docs/ADAPTER_SPEC.md`

6. Add Acceptance Criteria
## Acceptance Criteria

- [ ] All filter functions are type-annotated and pass mypy
- [ ] 100% of filter branches tested (unit + integration)
- [ ] Filters integrate seamlessly with renderer
- [ ] Code review approved
- [ ] Merged to main branch
- [ ] Release notes updated

Examples
Example 1: Feature Work Item
---
title: "Implement JSON Schema validation in template linter"
id: 57
status: not_started
priority: high
complexity: high
estimated_hours: 20
dependencies:
  - "[[54_complete_temple_native.md]]"
  - "[[44_implement_semantic_validation.md]]"
---

## Goal

Add JSON Schema validation to `temple-linter` to catch schema violations in templates at lint time, catching type mismatches and missing required fields before runtime.

...

Example 2: Spike/Research Work Item
---
title: "Evaluate expression engine alternatives for complex filters"
id: 58
status: not_started
priority: medium
complexity: medium
estimated_hours: 16
notes:
  - timestamp: 2024-06-01T12:00:00Z
    user: @john
    note: |
      Spike to evaluate JMESPath vs. custom expression engine for advanced filters.
      Decision will inform ADR-006 (expression language).
---

## Goal

Research and document three expression engine approaches for advanced data filtering in templates, with proof-of-concept for each.

...

Example 3: Bug/Fix Work Item
---
title: "Fix elif grammar parsing edge case"
id: 59
status: not_started
priority: high
complexity: low
estimated_hours: 4
dependencies:
  - "[[54_complete_temple_native.md]]"
---

## Goal

Fix parser to correctly handle consecutive `{% elif %}` blocks without requiring `{% else %}` at the end.

## Tasks

1. Add test case for multiple elif without else
2. Update grammar in `token_parser.py`
3. Verify fixture tests pass

## Acceptance Criteria

- [ ] Edge case test passes
- [ ] No regression in existing tests
- [ ] Merged to main

Tips & Conventions
Dependency Linking

Link to related work items using [[filename]] syntax:

dependencies:
  - "[[54_complete_temple_native.md]]"
  - "[[43_implement_template_syntax_validation.md]]"


The double-bracket syntax creates wiki-link references that tools can parse.

Commit Tracking

Record commits that implement this work:

related_commit:
  - 6d8c044  # feat(parser): canonicalize control-flow end tokens
  - f00459b  # fix(renderer): handle filter signature validation


Add these incrementally as work progresses, then complete the item.

Effort Estimation

Use fibonacci-like estimates:

1-2 hours: Trivial fixes
4-6 hours: Small feature or bug
8-12 hours: Medium feature
16-24 hours: Large feature
32+ hours: Epic or major refactor
Positioning in Backlog

Not all work needs an item:

Skip for: Inline changes, trivial docs fixes, emergency hotfixes
Create for: Features, spikes, architectural changes, tracked bugs

When in doubt, create the item—it's easier to abandon than to recreate.

Archiving

When a work item is completed:

Move file from /backlog/ to /backlog/archive/
Set completed_date: YYYY-MM-DD
Ensure actual_hours is recorded
Document related_commit with all implementation commits

Example: After completing #57, move 57_implement_json_schema_validation.md to archive/57_implement_json_schema_validation.md

Related Skills
update-work-item: For changing status, effort, and adding test results during work
feature-branch-management: Automatically invoked by update-work-item to create feature branches
create-pr: Automatically invoked to create pull requests when item status → testing
handle-pr-feedback: For addressing PR review feedback
finalize-work-item: For completing and archiving items after PR merged
git-commit: For recording implementation commits that reference work items
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