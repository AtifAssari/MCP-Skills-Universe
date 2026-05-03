---
title: spec-driven-resync-code-mapping
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-resync-code-mapping
---

# spec-driven-resync-code-mapping

skills/kw12121212/auto-spec-driven/spec-driven-resync-code-mapping
spec-driven-resync-code-mapping
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-resync-code-mapping
SKILL.md

You are helping the user retrofit or repair spec-code mapping frontmatter in .spec-driven/specs/ files.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

verify-spec-mappings: node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings
audit-spec-mapping-coverage: node {{SKILL_DIR}}/scripts/spec-driven.js audit-spec-mapping-coverage <spec-path> [--implementation <repo-path> ...] [--tests <repo-path> ...]
audit-unmapped-spec-evidence: node {{SKILL_DIR}}/scripts/spec-driven.js audit-unmapped-spec-evidence [--implementation <repo-path> ...] [--tests <repo-path> ...]

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

Steps

Choose the remapping scope — determine whether the user wants to remap:

all main spec files
one spec category or file
only specs reported by verify-spec-mappings as malformed or stale

If the user already gave a scope, use it. If not, ask which scope to repair.

Read spec context first — before proposing mapping edits, read:

.spec-driven/config.yaml
.spec-driven/specs/INDEX.md
every main spec file in the selected scope
any existing mapping frontmatter in those spec files

Run mapping validation — run:

node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings


Use the JSON result to identify missing frontmatter, malformed mapping fields, non-string entries, and missing mapped files.

Inspect repository evidence — infer mappings by converging on the current repository evidence, not by trying to list every related file. Keep implementation files separate from test files.

Derive search terms from the spec path, filename, requirement titles, scenario titles, and distinctive command names, skill names, config keys, or domain terms in the spec body.
Search likely implementation and test locations for exact terms first, then obvious variants such as kebab-case, snake_case, camelCase, and singular/plural forms.
Keep files that directly implement, expose, validate, or verify the behavior. Exclude generic helpers unless the behavior is primarily implemented there or the entrypoint would otherwise be misleading without it.
Follow at most one level of structural evidence when needed: imports, exports, command registries, dispatch tables, and tests that directly execute or assert the behavior.
mapping.implementation should contain primary implementation files, feature entrypoints, and thin orchestrators that materially wire the behavior together.
mapping.tests should contain tests that directly verify the behavior.
If behavior spans multiple primary files, include all of them. If evidence is weak or conflicting, keep the smaller confident set and report the ambiguity.
Stop once the mapping covers the main files a maintainer would inspect first. Do not chase every transitive helper.
For framework or meta-specs, start with files named directly in the spec, then add workflow artifacts that define or enforce the behavior, such as relevant skills/*/SKILL.md, scripts/spec-driven.ts, install.sh, test files, and top-level docs.
Use repo structure as evidence: installation specs map to installer code, installation tests, and shipped skills; mapping-validation specs map to validator code, spec-format docs, and validator tests.
Treat the mapping as complete when each requirement is covered by at least one primary implementation file and one test or verification path where such evidence exists.
If a requirement still has no confident mapping, mark it ambiguous and ask the user instead of inventing coverage.

Classify findings — sort findings into:

missing mapping frontmatter that can be confidently added
malformed mapping frontmatter that can be repaired without changing requirement behavior
stale paths that can be replaced with current implementation or test files
behavior/spec drift that requires /spec-driven-sync-specs, /spec-driven-spec-edit, or a normal change workflow
ambiguous mappings that require human input

For each target spec with a confident candidate mapping, run:

node {{SKILL_DIR}}/scripts/spec-driven.js audit-spec-mapping-coverage <spec-path> [--implementation <repo-path> ...] [--tests <repo-path> ...]


Use the candidate implementation and test sets as the explicit evidence inputs. Use the node {{SKILL_DIR}}/scripts/spec-driven.js audit-spec-mapping-coverage ... output to identify missing and extra mapping entries before presenting the edit.

Also run:

node {{SKILL_DIR}}/scripts/spec-driven.js audit-unmapped-spec-evidence [--implementation <repo-path> ...] [--tests <repo-path> ...]


Use the same candidate evidence set to check whether some files are not mapped by any main spec at all. If that happens, decide whether the likely next step is mapping repair for another spec, spec synchronization, direct spec editing, or a normal change workflow.

Present proposed mapping edits — before editing any file, show the user:

each spec file whose frontmatter will change
the proposed mapping.implementation paths
the proposed mapping.tests paths
any behavior/spec drift or ambiguous mapping that will not be edited by this skill

Wait for explicit confirmation before writing files.

Apply confirmed mapping repairs — after confirmation, edit only mapping frontmatter in the selected main spec files. Do not change implementation files. Do not rewrite requirement bodies unless the user switches to /spec-driven-sync-specs, /spec-driven-spec-edit, or a normal change workflow.

Validate after editing — rerun:

node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings


Fix safe frontmatter format issues immediately and rerun node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings. If any remaining error needs human judgment, report it clearly.

Report final result — summarize:

which spec files had mapping frontmatter added or repaired
which stale paths were replaced
whether mapping validation now passes
any behavior/spec drift or ambiguity left for another workflow
Rules
This is a planning/documentation skill only — do not change implementation code or tests
Do not create, modify, archive, or cancel entries under .spec-driven/changes/
Do not rewrite requirement behavior while repairing mappings
Keep mapping.implementation and mapping.tests separate
Use repo-relative file paths only
Keep mappings at file granularity; do not use line numbers, ranges, or symbols
Always run node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings before and after confirmed edits
Get explicit user confirmation before editing any spec file
If mapping repair reveals behavior/spec drift, recommend the appropriate spec synchronization or change workflow instead of silently changing requirements
Weekly Installs
13
Repository
kw12121212/auto…c-driven
First Seen
Apr 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass