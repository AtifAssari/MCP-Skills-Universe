---
rating: ⭐⭐⭐
title: spec-driven-propose
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-propose
---

# spec-driven-propose

skills/kw12121212/auto-spec-driven/spec-driven-propose
spec-driven-propose
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-propose
SKILL.md

You are helping the user create a new spec-driven change proposal.

Do not ask follow-up questions or require confirmation during the proposal stage. Derive the strongest proposal you can from the user request, project context, and existing specs. Record any remaining ambiguity in questions.md for /spec-driven-apply to surface before implementation begins.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

propose: node {{SKILL_DIR}}/scripts/spec-driven.js propose <name>
verify: node {{SKILL_DIR}}/scripts/spec-driven.js verify <name>

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

Steps

Determine the change name — use the user-provided kebab-case name when one is already available. Otherwise, derive a short kebab-case name from the request and the proposal scope yourself instead of stopping to ask for one.

Read project context and existing specs — read the following before generating anything:

.spec-driven/config.yaml — use context to inform content; treat rules as binding constraints; note any fileMatch entries that apply to files this change will touch
.spec-driven/specs/INDEX.md — identifies all existing spec files and their scope
Every spec file referenced in INDEX.md that this change is likely to touch — read the full content to understand existing requirements before writing MODIFIED or ADDED entries

Scaffold the change — run:

node {{SKILL_DIR}}/scripts/spec-driven.js propose <name>


This creates .spec-driven/changes/<name>/ with seeded artifact templates.

Fill proposal.md — write a clear, concise proposal covering:

What: What the change does (observable behavior, not implementation)
Why: Motivation and context
Scope: What is in scope, what is explicitly out of scope
Unchanged Behavior: List existing behaviors that must not break — things adjacent to or potentially affected by this change. Leave blank if truly nothing is at risk.

Fill design.md — write the technical approach:

Approach: How you'll implement it at a high level
Key Decisions: Significant choices and their rationale
Alternatives Considered: What was ruled out and why

Populate specs/ delta files — look at the project's .spec-driven/specs/ directory structure. For each spec file that this change touches, create a corresponding file under .spec-driven/changes/<name>/specs/ mirroring the same relative path (e.g. specs/auth/login.md → changes/<name>/specs/auth/login.md). If the change introduces a new spec area, create the new relative path that should exist under .spec-driven/specs/ after archive.

Mirror the main spec path exactly. For example, .spec-driven/specs/skills/planning.md maps to .spec-driven/changes/<name>/specs/skills/planning.md.

Use this canonical sample as the format target:

---
mapping:
  implementation:
    - path/to/implementation.ts
  tests:
    - test/path/to/test.ts
---

## ADDED Requirements

### Requirement: new-capability
The system MUST provide <observable behavior>.

#### Scenario: success
- GIVEN <precondition>
- WHEN <action>
- THEN <result>

## MODIFIED Requirements

### Requirement: existing-capability
Previously: The system MUST <old behavior>.
The system MUST <new behavior>.

## REMOVED Requirements

### Requirement: old-capability
Reason: This behavior is removed because <reason>.


Each delta file uses ADDED/MODIFIED/REMOVED sections with the standard format:

YAML frontmatter with mapping.implementation and mapping.tests when related files are knowable from repository context
### Requirement: <name> headings and RFC 2119 keywords (MUST/SHOULD/MAY)
#### Scenario: blocks (GIVEN/WHEN/THEN) where helpful
ADDED: new requirements; MODIFIED: changed requirements (include Previously: note); REMOVED: removed requirements (include reason)
Omit sections that don't apply — do not leave empty sections
If this change has no observable spec impact, leave changes/<name>/specs/ empty — do not create a prose-only delta file that breaks the delta spec format
Do not invent mapping paths when the related implementation or test files are not clear; leave mapping completion to /spec-driven-apply

Fill tasks.md — write a concrete implementation checklist using this canonical structure:

# Tasks: <change-name>

## Implementation
- [ ] Describe the first atomic implementation task
- [ ] Describe the second atomic implementation task

## Testing

- [ ] Run `npm run lint` — lint or validation task
- [ ] Run `npm test` — unit test task

## Verification
- [ ] Verify implementation matches proposal scope


Each task uses - [ ] checkboxes. Tasks should be independently completable.

The ## Testing section MUST satisfy these verification keyword requirements:

At least one task MUST contain a lint/validation keyword: lint, validate, validation, typecheck, type-check, or build
At least one task MUST contain a unit test keyword: unit test or unit tests
Both tasks MUST name an explicit runnable command in backticks or use a known runner (npm, pnpm, yarn, bun, node, bash, sh, pytest, jest, vitest, go, cargo, make, uv, poetry)
Paraphrasing these keywords (e.g. "run tests" instead of "run unit tests") will cause verify to fail

If the relevant command cannot be determined confidently from repository context, add an open question to questions.md instead of guessing. Do NOT add an "Update specs" task — the specs/ directory contains the spec artifacts.

Fill questions.md — document any open questions or ambiguities:

For every unclear point (motivation, scope boundaries, technical approach, etc.), add an entry under ## Open:
- [ ] Q: <specific question>
  Context: <why this matters / what depends on the answer>

If everything is clear, leave ## Open empty with a note: <!-- No open questions -->
Do NOT use [NEEDS CLARIFICATION] inline markers in any artifact — questions.md is the single place for all open questions

Validate artifact format — run:

node {{SKILL_DIR}}/scripts/spec-driven.js verify <name>


Treat this as a final structure and format check before presenting the proposal.

If it reports missing artifacts, malformed delta spec sections/headings, or unfilled placeholders you can safely fix, fix them immediately and rerun verify
If verify still reports a format or structure problem you cannot confidently repair, stop and report the issue to the user
If the only remaining error is open questions in questions.md, treat that as expected at proposal time and surface those questions clearly to the user

Hand off — show the user the five files and summarize the scope, key decisions, and any open questions. Do not require a confirmation checkpoint after writing the proposal. If questions.md has open questions, make clear that /spec-driven-apply will surface them as an implementation blocker and require explicit user resolution before coding starts, and mention /spec-driven-modify only as an optional revision path.

Rules
Do not implement anything — this is planning only
Keep tasks atomic and verifiable
Do not ask follow-up questions or require a proposal-stage confirmation checkpoint
proposal.md describes what and why; design.md describes how; tasks.md is the checklist; questions.md is for open questions
Document ambiguities in questions.md — never guess at unclear requirements, and never use [NEEDS CLARIFICATION] inline markers
Do not add a post-proposal confirmation gate once the artifacts are written
Open questions are allowed at proposal handoff time; leave them in questions.md for /spec-driven-apply to surface and block on
Before finishing, rerun verify until all repairable format issues are fixed; if any non-question error remains, report it to the user
Keep spec-code mappings in frontmatter, not in requirement prose
Weekly Installs
35
Repository
kw12121212/auto…c-driven
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass