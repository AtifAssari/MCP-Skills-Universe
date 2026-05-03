---
title: spec-driven-spec-content
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-spec-content
---

# spec-driven-spec-content

skills/kw12121212/auto-spec-driven/spec-driven-spec-content
spec-driven-spec-content
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-spec-content
SKILL.md

You are helping the user place spec content into the correct delta spec file for an existing spec-driven change.

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

Steps

Select the change — run node {{SKILL_DIR}}/scripts/spec-driven.js modify to list active changes. Ask which change to edit if the user did not specify one.

Understand the request — identify whether the user wants to:

add new spec content
extend an existing spec
modify an existing requirement
remove one or more existing requirements

Read index-first context — before deciding any path, read:

.spec-driven/config.yaml
.spec-driven/specs/INDEX.md
any existing files under .spec-driven/changes/<name>/specs/ that already look related

Choose candidate targets from INDEX.md — use the index to determine which existing categories and spec files might already cover the requested behavior.

If one or more candidates exist, read the full main spec files before making any routing decision
Only create a new category if no existing category fits the behavior
Only create a new spec file inside an existing category if the behavior does not fit any existing file in that category

Decide the delta spec path — classify the request into exactly one of:

update an existing delta file that mirrors an existing main spec file
create a new delta file under an existing category
create a new delta file under a new category
revise existing requirements in a delta file that already exists

Keep the delta path aligned with the main spec path that should exist after archive.

If the chosen delta spec file already exists under .spec-driven/changes/<name>/specs/, read that exact file before appending or revising content

Edit the delta spec content — preserve the standard delta format:

Use ## ADDED Requirements for new requirements
Use ## MODIFIED Requirements for changed requirements, including a Previously: note
Use ## REMOVED Requirements for deletions, including the reason
Keep ### Requirement: headings intact
Describe observable behavior, not implementation details

Handle removals explicitly — if the request removes spec content:

identify the exact ### Requirement: heading or headings being removed
write those removals explicitly in the delta file
do not use vague phrasing like "remove old spec" or "delete obsolete content"
if the target requirement is ambiguous after reading the relevant specs, stop and ask the user which requirement should be removed

Run the final spec format check — after any spec edit, run:

node {{SKILL_DIR}}/scripts/spec-driven.js verify <name>

Treat missing artifacts, malformed delta section markers/headings, and other spec structure problems as the format issues to repair
Fix any safe format issues immediately and rerun verify
If verify reports only non-format workflow blockers such as open questions in questions.md, surface those separately instead of misreporting them as spec-format failures
Do not finish without this check
If unresolved format or structure errors remain, report them clearly to the user

Summarize the routing decision — tell the user:

which category/file was chosen
whether it was an existing file, new file, or new category
whether the change added, modified, or removed requirements
whether the final format check passed
Rules
Read .spec-driven/specs/INDEX.md before choosing a category or file name
Prefer existing categories and files unless the content clearly requires a new path
Read the relevant main specs before editing delta specs
If the chosen delta file already exists, read that exact file before editing it
Do not implement code — this skill edits planning artifacts only
Always finish with a spec format check
Weekly Installs
12
Repository
kw12121212/auto…c-driven
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass