---
title: roadmap-propose
url: https://skills.sh/kw12121212/auto-spec-driven/roadmap-propose
---

# roadmap-propose

skills/kw12121212/auto-spec-driven/roadmap-propose
roadmap-propose
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill roadmap-propose
SKILL.md

You are helping the user turn planned roadmap work into a normal spec-driven change.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

init: node {{SKILL_DIR}}/scripts/spec-driven.js init
propose: node {{SKILL_DIR}}/scripts/spec-driven.js propose <name>
verify: node {{SKILL_DIR}}/scripts/spec-driven.js verify <name>

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

If .spec-driven/roadmap/ is missing, repair the scaffold first:

node {{SKILL_DIR}}/scripts/spec-driven.js init

Steps

Identify the target planned change — determine which milestone item the user wants to turn into a real change. If they already gave a change name, use it. Otherwise ask which Planned Changes item to promote.

Read roadmap and spec context first — before scaffolding anything, read:

.spec-driven/config.yaml
.spec-driven/roadmap/INDEX.md
the milestone file that contains the target item
.spec-driven/specs/INDEX.md
the relevant main spec files the new change is likely to touch
the selected planned change entry as a single-line roadmap input

Confirm it is already planned work — verify that the selected name is present under a milestone ## Planned Changes section before scaffolding.

Extract the roadmap handoff context — treat the selected planned change entry as more than a name lookup:

use the canonical first line to identify the change name while treating the declared status and summary as metadata on that same line
use the surrounding milestone sections as context for scope, rationale, sequencing, or constraints when the one-line summary is not sufficient
treat milestone declared statuses as limited to proposed, active, blocked, or complete
treat planned change declared statuses as limited to planned or complete

Scaffold the change — run:

node {{SKILL_DIR}}/scripts/spec-driven.js propose <name>


This creates .spec-driven/changes/<name>/ with seeded artifact templates.

Fill the standard proposal artifacts — populate:

proposal.md

design.md

tasks.md using this canonical structure:

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

If the relevant command cannot be determined confidently from repository context, add an open question instead of guessing.

questions.md

delta specs under changes/<name>/specs/

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

Do not invent mapping paths when the repository evidence is unclear

mapping frontmatter in delta spec files when implementation and test paths are knowable from repository context Use the roadmap milestone as planning input, but treat the selected planned change as a single-line item and derive any extra context from the milestone sections rather than multiline planned change detail.

Validate artifact format — run:

node {{SKILL_DIR}}/scripts/spec-driven.js verify <name>


If the command reports repairable format issues, fix them and rerun verify.

Offer the execution handoff — report the new change path, note which milestone it came from, surface any open questions that must be resolved before implementation, and ask the user whether they want to:

enter /spec-driven-apply <name> for the stepwise execution path
enter /spec-driven-auto for the end-to-end execution path Do not auto-enter either execution path without the user's explicit choice.
Rules
This skill creates planning artifacts only — do not implement product code
Only turn Planned Changes into change scaffolds
Create the same five artifacts as spec-driven-propose
Keep implementation and test mappings in spec frontmatter, not in requirement prose
If testing commands are not knowable from repository context, add an open question instead of guessing them
Before finishing, rerun verify until all repairable format issues are fixed
Weekly Installs
30
Repository
kw12121212/auto…c-driven
First Seen
Apr 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass