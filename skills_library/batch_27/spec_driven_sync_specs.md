---
title: spec-driven-sync-specs
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-sync-specs
---

# spec-driven-sync-specs

skills/kw12121212/auto-spec-driven/spec-driven-sync-specs
spec-driven-sync-specs
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-sync-specs
SKILL.md

You are helping the user synchronize .spec-driven/specs/ with behavior that already exists in the repository.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

init: node {{SKILL_DIR}}/scripts/spec-driven.js init
verify-spec-mappings: node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

Steps

Choose the scan scope — determine whether the user wants:

a repository-wide scan
a scoped scan for a specific directory, module, or feature area

If the user already gave a scope, use it. If not, ask whether to scan the whole repository or a narrower target.

Read spec context first — before deciding that any drift exists, read:

.spec-driven/config.yaml
.spec-driven/specs/INDEX.md
every main spec file that appears relevant to the chosen scan scope

Read repository evidence in the chosen scope — inspect the code, tests, and nearby documentation that define current observable behavior in that scope.

Prefer files that expose behavior directly: CLI commands, handlers, user-facing flows, tests, and docs
Do not treat internal implementation details as requirements

Classify drift findings — compare the repository evidence to the current specs and sort findings into:

confirmed behavior that exists in code but is missing from specs
existing requirements that appear outdated or incomplete
ambiguous findings that need human confirmation before they become specs
areas with no meaningful drift in the scanned scope

Report drift summary in chat — present a concise summary covering:

the scan scope that was analyzed
confirmed gaps or outdated spec areas, with specific file references
ambiguous findings that need human input
areas in scope where no meaningful drift was found

Get user confirmation — before editing any spec file, ask the user to confirm the proposed changes. List each spec file that will be added, modified, or removed. Do not proceed until the user explicitly approves.

Edit spec files directly — for each confirmed gap:

edit the corresponding file under .spec-driven/specs/
add, modify, or remove ### Requirement: blocks as appropriate
preserve or update mapping.implementation and mapping.tests frontmatter to match the repository evidence used for the sync
describe observable behavior only
if no existing category or file fits, create the new file under .spec-driven/specs/ with the correct relative path

Refresh INDEX.md — after all spec edits are complete, run:

node {{SKILL_DIR}}/scripts/spec-driven.js init


This regenerates .spec-driven/specs/INDEX.md to reflect the current file state.

If mapping frontmatter changed, also run:

node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings


Report final changes — summarize what was done:

which spec files were added, modified, or removed
a brief description of the drift that was fixed in each file
any ambiguous findings that were left unresolved and why
Rules
This is a documentation skill only — do not change product code
Read spec context before judging drift
Respect the user-selected scope; do not imply full-repository coverage after a scoped scan
Use code, tests, and nearby docs as evidence, but write only observable behavior into the specs
Do not create a change — edit .spec-driven/specs/ files directly
Do not write a standalone report file; the summary belongs in chat
Get explicit user confirmation before editing any spec file
Keep implementation and test mappings in frontmatter, not in requirement prose
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