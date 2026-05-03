---
rating: ⭐⭐
title: speckit-constitution
url: https://skills.sh/dceoy/speckit-agent-skills/speckit-constitution
---

# speckit-constitution

skills/dceoy/speckit-agent-skills/speckit-constitution
speckit-constitution
Installation
$ npx skills add https://github.com/dceoy/speckit-agent-skills --skill speckit-constitution
SKILL.md
Spec Kit Constitution Skill
When to Use
Initial project setup or when governance principles need updates.
Inputs
User-provided principles or amendments.
Existing .specify/memory/constitution.md and templates.

If the request is missing or ambiguous, ask focused questions before proceeding.

Workflow

You are updating the project constitution at .specify/memory/constitution.md. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. [PROJECT_NAME], [PRINCIPLE_1_NAME]). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

Load the existing constitution template at .specify/memory/constitution.md.

Identify every placeholder token of the form [ALL_CAPS_IDENTIFIER]. IMPORTANT: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

Collect/derive values for placeholders:

If user input (conversation) supplies a value, use it.
Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
For governance dates: RATIFICATION_DATE is the original adoption date (if unknown ask or mark TODO), LAST_AMENDED_DATE is today if changes are made, otherwise keep previous.
CONSTITUTION_VERSION must increment according to semantic versioning rules:
MAJOR: Backward incompatible governance/principle removals or redefinitions.
MINOR: New principle/section added or materially expanded guidance.
PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
If version bump type ambiguous, propose reasoning before finalizing.

Draft the updated constitution content:

Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

Consistency propagation checklist (convert prior checklist into active validations):

Read .specify/templates/plan-template.md and ensure any "Constitution Check" or rules align with updated principles.
Read .specify/templates/spec-template.md for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
Read .specify/templates/tasks-template.md and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
Review runtime prompts/agents for outdated references and align with updated principles:
.claude/commands/speckit.*.md
.codex/prompts/speckit.*.md
.gemini/commands/speckit.*.toml
.github/prompts/speckit.*.prompt.md
.github/agents/speckit.*.agent.md
skills/speckit-*/SKILL.md
Read any runtime guidance docs (e.g., README.md, docs/quickstart.md, or agent-specific guidance files if present). Update references to principles changed.

Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):

Version change: old → new
List of modified principles (old title → new title if renamed)
Added sections
Removed sections
Templates requiring updates (✅ updated / ⚠ pending) with file paths
Follow-up TODOs if any placeholders intentionally deferred.

Validation before final output:

No remaining unexplained bracket tokens.
Version line matches report.
Dates ISO format YYYY-MM-DD.
Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

Write the completed constitution back to .specify/memory/constitution.md (overwrite).

Output a final summary to the user with:

New version and bump rationale.
Any files flagged for manual follow-up.
Suggested commit message (e.g., docs: amend constitution to vX.Y.Z (principle additions + governance update)).

Formatting & Style Requirements:

Use Markdown headings exactly as in the template (do not demote/promote levels).
Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
Keep a single blank line between sections.
Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert TODO(<FIELD_NAME>): explanation and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing .specify/memory/constitution.md file.

Outputs
Updated .specify/memory/constitution.md (with Sync Impact Report comment)
Any updated templates or runtime guidance files required to stay consistent with the constitution
Next Steps

After updating the constitution:

Specify new features with speckit-specify.
Weekly Installs
172
Repository
dceoy/speckit-a…t-skills
GitHub Stars
76
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass