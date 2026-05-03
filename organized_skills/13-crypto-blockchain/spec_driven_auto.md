---
rating: ⭐⭐⭐
title: spec-driven-auto
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-auto
---

# spec-driven-auto

skills/kw12121212/auto-spec-driven/spec-driven-auto
spec-driven-auto
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-auto
SKILL.md

You are running the full spec-driven workflow end-to-end for a single change.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

propose: node {{SKILL_DIR}}/scripts/spec-driven.js propose <name>
apply: node {{SKILL_DIR}}/scripts/spec-driven.js apply <name>
verify: node {{SKILL_DIR}}/scripts/spec-driven.js verify <name>
audit-unmapped-spec-evidence: node {{SKILL_DIR}}/scripts/spec-driven.js audit-unmapped-spec-evidence [--implementation <repo-path> ...] [--tests <repo-path> ...]
verify-spec-mappings: node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings
archive: node {{SKILL_DIR}}/scripts/spec-driven.js archive <name>

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

Steps

Load context — rebuild working context from the current files before doing anything:

You MUST treat all prior conversational context as stale, unreliable, and non-authoritative.
You MUST NOT use prior chat context as a source of truth for requirements, task state, implementation details, or completion status.
You MUST rebuild working context from the current change artifacts, relevant base specs, and the current repository state before taking any workflow action.
If prior chat context differs from the files or repository state in any way, you MUST discard the prior chat context and follow the files and repository state only.
Do not use prior chat context unless it has been explicitly re-validated against the current files and repository state.

Assess complexity — before doing anything else, evaluate the change using a two-tier model:

Read .spec-driven/config.yaml for project context
Read .spec-driven/specs/INDEX.md and relevant spec files to understand the current system
Read the codebase files that the change will likely touch — estimate the number of files, modules, and cross-cutting concerns involved
Classify the change into one of two tiers:
Green (proceed): clear scope and a concrete definition of done within a single repository, including changes that touch up to 15 modules or packages, modify up to 50 files, involve schema migrations with data transformation, modify existing auth/authz/payment logic, or make cross-cutting changes across multiple subsystems — proceed automatically
Red (suggest brainstorm): requires coordinating across multiple services or repositories, scope is vague or open-ended (e.g. "refactor the codebase", "improve performance"), or has no clear definition of done — explain why and suggest running /spec-driven-brainstorm first to converge the idea, then entering /spec-driven-auto to execute the resulting proposal
If Red, stop and suggest brainstorm
If Green, proceed

Propose — run /spec-driven-propose:

Run node {{SKILL_DIR}}/scripts/spec-driven.js propose <name>
Fill all artifacts: proposal.md (with Unchanged Behavior), specs/ delta files, design.md, tasks.md (with ## Testing), questions.md (open questions)
Show the user a summary: scope, key decisions, task count, unchanged behaviors, and any open questions
If questions.md has open questions, list them and stop for user resolution before proceeding — do not continue until every open question is explicitly resolved
If there are no open questions, proceed directly to Step 4 without waiting for confirmation

Apply — implement all tasks:

Run node {{SKILL_DIR}}/scripts/spec-driven.js apply <name> to show task summary
Check questions.md for open - [ ] Q: entries — if any, present each unresolved question using:
Question
Explanation
Impact
Recommendation
Explanation must clarify why the question is still unresolved after reading the current change artifacts, relevant main specs, and repository state
Impact must describe what implementation choice, task, behavior, or unchanged-behavior guarantee depends on the answer
Recommendation may suggest a preferred answer, but only as a suggestion
After presenting those blocks, ask the user to answer or confirm the decision needed, and stop until the user explicitly resolves every open question
You MAY recommend a preferred answer, but only as a suggestion; you MUST NOT treat your own recommendation as a resolved answer or continue implementation until the user explicitly confirms it
Work through each - [ ] task in order: read code, implement, verify Unchanged Behavior, mark - [x]
For ## Testing tasks: actually run the tests and confirm they pass
Run node {{SKILL_DIR}}/scripts/spec-driven.js apply <name> to confirm remaining === 0

Verify — check completeness:

Run node {{SKILL_DIR}}/scripts/spec-driven.js verify <name>
Then perform the rest of the /spec-driven-verify checks: task completion, open questions, implementation evidence, and spec alignment
If the change-local evidence set includes implementation files or directly verifying test files, run node {{SKILL_DIR}}/scripts/spec-driven.js audit-unmapped-spec-evidence [--implementation <repo-path> ...] [--tests <repo-path> ...] as part of this verify pass and treat its current-change blocking findings the same way /spec-driven-verify would
Treat script errors plus any CRITICAL findings from those checks as blockers
If there are blockers you can safely fix, fix them automatically, then rerun both node {{SKILL_DIR}}/scripts/spec-driven.js verify <name> and the verification pass
If any blocker cannot be auto-fixed: stop and ask the user
Re-read delta spec files and update them to match what was actually implemented
Ensure delta spec mapping frontmatter reflects the implementation and test files actually changed or relied on

Review — check code quality:

Read every file changed by this change
Review findings must be author-agnostic: do not trust or excuse code just because it was generated or edited earlier in this same auto run
Check: readability, security, error handling, performance, best practices, test quality
Reuse the verify-phase node {{SKILL_DIR}}/scripts/spec-driven.js audit-unmapped-spec-evidence [--implementation <repo-path> ...] [--tests <repo-path> ...] result unless review fixes changed the relevant implementation or direct test files; only rerun that same command when the reviewed evidence set materially changed
MUST FIX issues: fix them automatically, then re-review
If MUST FIX issues cannot be auto-fixed: stop and ask the user
SHOULD FIX and NITS: fix if straightforward, otherwise note in the final report

Archive — close out the change:

Confirm there are no incomplete tasks before archiving
List all delta files in specs/ and merge each into the corresponding main spec file
If changes/<name>/specs/ is empty, ask the user to confirm this change has no observable spec impact before continuing
Update .spec-driven/specs/INDEX.md if new spec files were created
Run node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings after merging mapping frontmatter into main specs
Run node {{SKILL_DIR}}/scripts/spec-driven.js archive <name>
If .spec-driven/roadmap/ exists, treat any milestone declared status or roadmap index updates performed by the archive command as part of archive closeout
Report the final result: what was built, files changed, tests passing, archive location, and any roadmap status changes caused by archive
If the user wants to commit and push the completed archived change, offer /spec-driven-ship <name> as the next explicit handoff. Keep that handoff advisory only: do not stage files, inspect push eligibility, enter that workflow, commit, or push unless the user explicitly chooses it.
Rules
The context reset in Step 1 is mandatory — never skip it
The complexity check in Step 2 is mandatory — never skip it
The workflow runs fully automatically — do not pause for confirmation except when open questions in questions.md need user resolution
Additional confirmations are required whenever the workflow is blocked by unresolved questions or an empty delta-spec archive decision
All other steps run automatically unless blocked by an unresolvable issue
Follow all config.yaml rules (specs, change, code, test) throughout
If anything goes wrong mid-flow, stop and explain — do not silently continue
Mark tasks complete one at a time, not in bulk
Recommended answers do not count as question resolution without explicit user confirmation
Keep implementation and test mappings in frontmatter, not in requirement prose
Do not commit or push automatically. Shipping is handled only by the explicit /spec-driven-ship <name> workflow after successful archive closeout.
Weekly Installs
36
Repository
kw12121212/auto…c-driven
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass