---
title: spec-driven-brainstorm
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-brainstorm
---

# spec-driven-brainstorm

skills/kw12121212/auto-spec-driven/spec-driven-brainstorm
spec-driven-brainstorm
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-brainstorm
SKILL.md

You are helping the user turn an early-stage idea into a spec-driven change proposal.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

propose: node {{SKILL_DIR}}/scripts/spec-driven.js propose <name>
verify: node {{SKILL_DIR}}/scripts/spec-driven.js verify <name>

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

Steps

Start from the idea, not the artifact list — ask the user what they want to achieve, what problem they are trying to solve, and any known constraints or preferences. Do not require a change name up front.

Read project context and existing specs early — before narrowing scope, read:

.spec-driven/config.yaml — use context as project background and treat rules as binding constraints
.spec-driven/specs/INDEX.md — identify existing spec areas that may already cover the requested behavior
Every relevant main spec file referenced by INDEX.md that appears related to the idea being discussed

Brainstorm until the change is decision-ready — use the discussion to converge on:

the desired outcome and user-visible behavior
what is in scope and explicitly out of scope
important tradeoffs, constraints, risks, and unchanged behavior
which existing spec files will likely be modified, or whether a new spec area is needed
any questions that still need a human answer before implementation

Suggest the change name — once the idea is coherent enough, propose a short kebab-case change name. If the user already provided a valid name, keep it. If not, suggest one that reflects the agreed change scope.

Present a proposal checkpoint — before creating any files, summarize:

the proposed change name
the goal and scope
the main spec areas expected to change
key decisions or tradeoffs already settled
any unresolved questions that would go into questions.md

Then ask for explicit confirmation. If the user wants revisions, continue the brainstorm and re-summarize until confirmed.

Scaffold the change after confirmation — run:

node {{SKILL_DIR}}/scripts/spec-driven.js propose <name>


This creates .spec-driven/changes/<name>/ with the seeded templates.

Fill the five proposal artifacts — after scaffolding, complete the same proposal workflow used by /spec-driven-propose:

write proposal.md with What, Why, Scope, and Unchanged Behavior

write design.md with Approach, Key Decisions, and Alternatives Considered

populate changes/<name>/specs/ with delta spec files aligned by path with the main .spec-driven/specs/ structure

mirror the main spec path exactly, for example .spec-driven/specs/skills/planning.md becomes .spec-driven/changes/<name>/specs/skills/planning.md

use this canonical sample as the format target:

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


omit sections that do not apply instead of leaving blank placeholders

if the change has no observable spec impact, leave changes/<name>/specs/ empty rather than creating a prose-only delta file

Do not invent mapping.implementation or mapping.tests paths when the repository evidence is unclear

include mapping.implementation and mapping.tests frontmatter in delta spec files when related files are knowable from repository context

write tasks.md using this canonical structure:

# Tasks: <change-name>

## Implementation
- [ ] Describe the first atomic implementation task
- [ ] Describe the second atomic implementation task

## Testing

- [ ] Run `npm run lint` — lint or validation task
- [ ] Run `npm test` — unit test task

## Verification
- [ ] Verify implementation matches proposal scope


Each task uses - [ ] checkboxes and should be independently completable.

The ## Testing section MUST satisfy these verification keyword requirements:

At least one task MUST contain a lint/validation keyword: lint, validate, validation, typecheck, type-check, or build
At least one task MUST contain a unit test keyword: unit test or unit tests
Both tasks MUST name an explicit runnable command in backticks or use a known runner (npm, pnpm, yarn, bun, node, bash, sh, pytest, jest, vitest, go, cargo, make, uv, poetry)
Paraphrasing these keywords (e.g. "run tests" instead of "run unit tests") will cause verify to fail

If the relevant command cannot be determined confidently from repository context, record that in questions.md instead of guessing.

write questions.md, recording every unresolved point under ## Open, or leave <!-- No open questions --> if nothing is unclear

Validate before presenting the proposal — run:

node {{SKILL_DIR}}/scripts/spec-driven.js verify <name>

Fix any safe artifact-format issues immediately and rerun verify
If only open questions remain, treat that as expected at proposal time and surface those questions clearly
If any non-question error remains, stop and report it instead of presenting the proposal as ready

Hand off like propose — show the user the generated artifacts, summarize the final proposed scope, and list any open questions that must be answered before /spec-driven-apply.

Offer auto hand-off — after the hand-off, ask the user whether to enter /spec-driven-auto to execute the proposal end-to-end, or continue modifying the proposal with /spec-driven-modify. Do not auto-enter auto without the user's explicit choice.

Rules
Do not implement code — this skill is planning only
Do not scaffold proposal artifacts until the user explicitly confirms the brainstorm summary and change name
Read .spec-driven/config.yaml, INDEX.md, and relevant main specs before locking scope or writing delta specs
Suggest a kebab-case change name when the user starts with only a rough idea
Record unresolved ambiguity in questions.md; do not guess silently
If testing commands are not knowable from repository context, record that in questions.md instead of inventing them
After confirmation, follow the same artifact-writing and validation standard as /spec-driven-propose
Keep implementation and test mappings in spec frontmatter, not in requirement prose
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