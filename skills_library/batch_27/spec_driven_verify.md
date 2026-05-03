---
title: spec-driven-verify
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-verify
---

# spec-driven-verify

skills/kw12121212/auto-spec-driven/spec-driven-verify
spec-driven-verify
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-verify
SKILL.md

You are helping the user verify a spec-driven change before archiving.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

modify: node {{SKILL_DIR}}/scripts/spec-driven.js modify
verify: node {{SKILL_DIR}}/scripts/spec-driven.js verify <name>
verify-spec-mappings: node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings
apply: node {{SKILL_DIR}}/scripts/spec-driven.js apply <name>
audit-spec-mapping-coverage: node {{SKILL_DIR}}/scripts/spec-driven.js audit-spec-mapping-coverage <spec-path> [--implementation <repo-path> ...] [--tests <repo-path> ...]
audit-unmapped-spec-evidence: node {{SKILL_DIR}}/scripts/spec-driven.js audit-unmapped-spec-evidence [--implementation <repo-path> ...] [--tests <repo-path> ...]

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

Steps

Select the change — run node {{SKILL_DIR}}/scripts/spec-driven.js modify to list active changes. Ask which change to verify. If already specified, use it.

Format check — run:

node {{SKILL_DIR}}/scripts/spec-driven.js verify <name>


Report any errors (blocking) or warnings (non-blocking).

Treat any testing-readiness error from the script as CRITICAL, including missing ## Testing, missing lint/validation coverage, missing unit test coverage, or required testing tasks with no explicit runnable command.

Also run:

node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings


Treat malformed spec mapping frontmatter, missing mapping fields, or missing mapped files as CRITICAL findings for affected main specs.

Task completion check — run:

node {{SKILL_DIR}}/scripts/spec-driven.js apply <name>


If remaining > 0, list the incomplete tasks. These are CRITICAL issues.

Open questions check — read .spec-driven/changes/<name>/questions.md and scan for - [ ] Q: entries:

Any open question is CRITICAL
The script also reports these as errors; treat them as CRITICAL here

Implementation evidence check — for each completed task in tasks.md:

Identify what code or files the task should have changed
Verify the change actually exists (read relevant files)
If a completed task claims implementation, test, or spec work and there is no visible evidence, treat that as CRITICAL unless the ambiguity is clearly documented in questions.md

Build a mapping evidence set — before judging mapping quality, build a change-local evidence set from:

each touched delta spec file under .spec-driven/changes/<name>/specs/
implementation files actually changed for the completed behavior
test files actually changed for the completed behavior
files explicitly relied on to provide or directly verify the completed behavior

Prefer the smallest confident evidence set. Do not infer semantic coverage from distant helpers when the main implementation or direct test files are clear.

For each touched delta spec file, run:

node {{SKILL_DIR}}/scripts/spec-driven.js audit-spec-mapping-coverage <spec-path> [--implementation <repo-path> ...] [--tests <repo-path> ...]


Use the evidence set you built as the explicit --implementation and --tests inputs.

Also run:

node {{SKILL_DIR}}/scripts/spec-driven.js audit-unmapped-spec-evidence [--implementation <repo-path> ...] [--tests <repo-path> ...]


Use the same evidence set to identify implementation or test files that are not mapped by any main spec.

Spec alignment check — read .spec-driven/specs/, .spec-driven/config.yaml, .spec-driven/changes/<name>/proposal.md, and all files in .spec-driven/changes/<name>/specs/:

Does the implementation match what was proposed?
Do the delta files in changes/<name>/specs/ accurately describe what was implemented? Empty specs/ with real behavior changes is a CRITICAL.
Does each delta file mirror its corresponding main spec file path? Mismatched paths mean the merge will fail.
Do the delta files use the standard format (### Requirement: <name>, RFC 2119 keywords, #### Scenario: blocks)? Non-conforming format is a CRITICAL — the spec format is mandatory.
For each touched delta spec file, compare mapping.implementation and mapping.tests against the change-local evidence set using the audit output from node {{SKILL_DIR}}/scripts/spec-driven.js audit-spec-mapping-coverage <spec-path> [--implementation <repo-path> ...] [--tests <repo-path> ...].
If the evidence clearly shows that a touched spec depends on an implementation file or directly verifying test file missing from the mapping, report that omission as CRITICAL.
If the evidence is ambiguous, prefer the smaller confident set and report the ambiguity instead of inventing semantic coverage.
Report repo-wide structural mapping errors from verify-spec-mappings separately from change-local mapping omissions using the result from node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings.
If the unmapped-evidence audit shows that a primary implementation file or directly verifying test file from this change is not mapped by any main spec, report that as CRITICAL when the gap leaves this change's spec coverage incomplete.
If the unmapped-evidence audit only finds files outside this change scope or weakly related candidates, report them separately as REPO DEBT or lower-confidence WARNINGs.
If config.yaml has a rules field (including any fileMatch entries), check whether the implementation and artifacts comply — violations are WARNINGs
If proposal.md has an Unchanged Behavior section with content, verify the implementation has not violated any listed behaviors — violations are CRITICALs
Flag misalignments as WARNINGs or CRITICALs

Output a tiered report:

CRITICAL (blocks archive):
  - [list or "none"]

REPO DEBT (outside this change):
  - [list or "none"]

WARNING (should address):
  - [list or "none"]

SUGGESTION (optional improvements):
  - [list or "none"]


Recommend next step:

If CRITICAL issues: address them before archiving
If only WARNINGs: ask user if they want to address them or proceed
If clean: suggest /spec-driven-review <name>
Rules
Be honest — don't pass a change just because tasks are checked off
CRITICALs are things that would make the change incorrect or incomplete
REPO DEBT is pre-existing repository state outside the change scope; report it clearly and separately from change-local findings
WARNINGs are things that reduce confidence but don't necessarily block
SUGGESTIONs are optional quality improvements
Keep implementation and test mappings in frontmatter, not in requirement prose
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