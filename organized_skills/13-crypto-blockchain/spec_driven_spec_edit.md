---
rating: ⭐⭐⭐
title: spec-driven-spec-edit
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-spec-edit
---

# spec-driven-spec-edit

skills/kw12121212/auto-spec-driven/spec-driven-spec-edit
spec-driven-spec-edit
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-spec-edit
SKILL.md

You are helping the user create or modify main spec files under .spec-driven/specs/ directly, without going through the change workflow. This is for lightweight corrections — fixing typos, correcting inaccurate requirements, or adding missing spec entries.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

verify-spec-mappings: node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

Steps

Read spec context first — before making any changes, read:

.spec-driven/config.yaml
.spec-driven/specs/INDEX.md
any existing main spec files relevant to the user's request

Understand the request — identify whether the user wants to:

add a new spec file or category
add new requirements to an existing spec file
modify an existing requirement
remove one or more existing requirements

Choose the target — use INDEX.md to determine where the content belongs:

If one or more existing spec files cover the behavior, use those
Only create a new spec file if no existing file fits
Only create a new category if no existing category fits

Prepare the changes — draft the exact modifications:

For additions: write the new ### Requirement: heading and body
For modifications: show the before and after content
For removals: identify the exact ### Requirement: heading(s) to remove
Describe observable behavior only, not implementation details

Present and confirm — show the user:

which file or files will be changed
the exact content that will be added, modified, or removed
whether INDEX.md needs updating

Wait for explicit user confirmation before writing anything.

Apply the changes — after confirmation:

Edit the target spec file(s) under .spec-driven/specs/
Preserve existing mapping.implementation and mapping.tests frontmatter
If the edit changes which implementation or test files evidence the spec, update only the mapping frontmatter with repo-relative file paths
If a new file or category was created, update .spec-driven/specs/INDEX.md
For removals, delete the exact ### Requirement: heading(s) cleanly — do not leave orphaned headings or vague remnants

Validate the result — after editing, verify:

Each edited file still follows the standard ### Requirement: heading format
Edited files still have valid mapping frontmatter
INDEX.md correctly reflects all spec files under .spec-driven/specs/
If format issues are found, fix them immediately Run node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings when mapping frontmatter changed.

Summarize — tell the user:

which file(s) were changed
what was added, modified, or removed
whether INDEX.md was updated
Rules
Always read existing specs before editing — never edit blind
Present changes and wait for confirmation before writing
Prefer existing categories and files unless the content clearly requires a new path
Describe observable behavior only, not implementation details
Do not implement product code — this skill edits planning artifacts only
Do not create or interact with .spec-driven/changes/
Keep implementation and test mappings in frontmatter, not in requirement prose
Weekly Installs
26
Repository
kw12121212/auto…c-driven
First Seen
Apr 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass