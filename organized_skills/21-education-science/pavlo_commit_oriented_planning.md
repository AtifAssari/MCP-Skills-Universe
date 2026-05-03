---
rating: ⭐⭐⭐
title: pavlo-commit-oriented-planning
url: https://skills.sh/pavloglushko/ai-skills/pavlo-commit-oriented-planning
---

# pavlo-commit-oriented-planning

skills/pavloglushko/ai-skills/pavlo-commit-oriented-planning
pavlo-commit-oriented-planning
Installation
$ npx skills add https://github.com/pavloglushko/ai-skills --skill pavlo-commit-oriented-planning
SKILL.md
Skill: Step-Oriented Planning

Framework for breaking down a task into logically independent, testable steps. Each step represents a single cohesive unit of work that can stand alone — all tests pass after applying it, and it results in a single git commit.

When to Use

When planning a complex feature, refactoring, or multi-step task. Helps ensure:

Clear communication (each step has a clear purpose)
Easier code review (reviewers understand intent per step)
Safer rollback (a broken step can be reverted independently)
Better git history (clear cause-and-effect, no intermingled concerns)
Principles
One logical unit per step: Each step should address a single concern — one feature, one refactoring, one set of tests, or one documentation update.
Tests pass after every step: After applying a step, the test suite should pass. This enables bisecting and selective reverting.
Independent verification: A code reviewer should be able to understand the step's purpose without context from other steps in the series.
Ordered by dependency: If Step B depends on infrastructure from Step A, list A first.
Planning Process

Break down the task into smaller pieces:

Infrastructure changes (types, entities, repositories)
Service/business logic changes
Integration into use cases or adapters
Tests for each component
Documentation updates

Group by cohesion:

Don't mix unrelated changes (e.g., don't add a new feature and refactor unrelated code in one step)
Don't split a logical unit (e.g., a feature + its tests should be one step)

Order by dependency:

If Step B uses something introduced in Step A, put A first
Abstract types (interfaces) often come before implementations
Domain logic often comes before adapters

Number and name clearly:

Use format: Step 1: ..., Step 2: ...
Use a short title describing the one thing this step does
Optional: add a scope (e.g., Step 3: [domain/services] Add X validation)

Estimate scope:

Small steps (~50–150 lines changed) are easier to review
Complex steps may be larger but should still address a single concept

Cross-reference the ticket:

Where the ticket provides detailed specifications, pseudocode, or code drafts (e.g., an implementation sketch, an ABC signature, a helper function body), add an explicit cross-reference in the step description pointing to the exact ticket section (e.g., "PROJ-42_ticket.md R2, code block 'Implementation Sketch'").
The plan must be self-sufficient for step ordering and scope, but it must not duplicate large code blocks from the ticket. Instead, reference them so the implementer knows where to look.
Every step that implements a ticket requirement with non-trivial specification detail should include at least one such reference.

Self-verify and auto-fix (see Plan Self-Verification below):

Run the verification checklist against the draft plan
Fix every found issue directly in the plan file
Only present the plan to the user after verification passes
Plan Self-Verification

After producing the initial draft plan, before presenting it to the user, run through the following checklist automatically. Fix every issue found directly in the plan. Do not ask the user for permission to fix — just fix and note what changed.

Checklist
Logical issues

No circular dependencies — Step B must not require something introduced in Step C if C comes after B. Fix by reordering steps.

No broken-test steps — after every step, all tests must pass. If a step introduces code whose tests live in a later step, either merge the tests into the same step or ensure the code is unreachable / untested-but-passing until the test step.

No split logical units — a feature and its direct tests should be in the same step unless the test step is explicitly a bulk test step covering multiple features.

No vague or mixed-concern steps — each step title must name one specific change. If a step description lists unrelated items, split it.

Correct layer ordering — domain steps before application steps, application steps before adapter steps. Flag and reorder any violation.

Ticket consistency

All In Scope items are covered — every item in the ticket's ## Scope → In Scope section must map to at least one step. Flag any uncovered scope item and add a step for it.

No Out of Scope items are planned — if a step description implements something listed under ## Scope → Out of Scope, remove or revise it.

Requirements are fully addressed — every ### R<N> section in the ticket must be traceable to at least one step. Flag gaps and add steps.

Acceptance Criteria are traceable — every checkbox in ## Acceptance Criteria must be achievable by the steps as planned. Flag any criterion that no step addresses.

Documentation step is always last — every plan must end with an "Update documentation" step. This step updates whatever documentation is relevant in the repository (README, API docs, inline docs, etc.). It must always be the final step in the plan, even if the ticket does not explicitly mention docs.

After Fixing

Append a short ## Verification Notes section at the bottom of the plan file listing what was changed during self-verification (e.g., "Reordered steps 3 and 4 to fix dependency order", "Added Step 7 to cover R8 — Activation-Interval Coverage Test"). If nothing needed fixing, write "No issues found."

Example Structure
## Plan: Add new feature X

### Step 1: [domain/entities] Define Foo entity
- Add `Foo` immutable Pydantic model with fields a, b, c

### Step 2: [domain/services] Add FooService business logic
- Add stateless `FooService.process(foo)` method
- Pure domain logic, no dependencies on adapters

### Step 3: [application/use_cases] Add ProcessFooUseCase
- Orchestrate domain service with repository
- Inject `FooService` and `FooRepository`

### Step 4: [adapters/outbound] Implement FooRepository
- In-memory dict implementation for storage
- Register in DI container

### Step 5: [tests] Add comprehensive test suite
- Domain tests for FooService
- Application tests for ProcessFooUseCase (with mocks)
- Adapter tests for FooRepository

### Step 6: [docs] Update documentation
- Update relevant repository documentation
  (README, API docs, inline docs, etc.)


Note: The documentation step is always the last step in every plan, regardless of whether the ticket explicitly requires it.

Benefits
Easier code review: Reviewers see one logical change at a time
Safer merging: Each step is independently testable and reversible
Better blame history: git blame shows intent per line, not side-effects from unrelated changes
Incremental CI: CI can run tests after each step, catching issues early
Flexible rebasing: You can reorder, squash, or cherry-pick commits more easily
Anti-Patterns to Avoid
❌ One mega-step with mixed concerns (feature + refactoring + tests)
❌ Steps that break tests (even if "fixed in the next step")
❌ Splitting a logical unit across steps for no reason
❌ Vague step titles ("WIP", "cleanup", "fix stuff")
❌ Circular dependencies (Step A depends on B, B depends on A)
❌ Including Jira ticket metadata JSON blocks (ticket, epic, type, priority, labels, components, story_points, sprint, etc.) in the plan. The plan is about steps, not ticket bookkeeping. Omit any such JSON metadata entirely.
Real-World Example

See examples/E1_PR2_plan.md for a complete plan reference. Read it before generating a new plan to match the style, detail level, and structure.

Related Skills
Step-by-Step Execution: Guides how to execute the plan
Commit Rewriter: Can improve commit messages after execution; expects Step X: prefix for plan-mapped commits.
Weekly Installs
11
Repository
pavloglushko/ai-skills
First Seen
Apr 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass