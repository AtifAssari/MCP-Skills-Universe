---
title: cmk:feature-spec
url: https://skills.sh/commandosslabs/ai-devkit/cmk:feature-spec
---

# cmk:feature-spec

skills/commandosslabs/ai-devkit/cmk:feature-spec
cmk:feature-spec
Installation
$ npx skills add https://github.com/commandosslabs/ai-devkit --skill cmk:feature-spec
SKILL.md
Feature Spec
Intents
Create a feature spec for checkout retry logic

Use this Notion doc to draft a feature spec for tenant-level rate limiting: [link]

Update the retry spec — we changed the backoff strategy to exponential with jitter

Spec out the user authentication flow

Break the PRD into feature specs

References

Read references/spec-conventions.md for placement rules and references/feature-spec-template.md for section structure.

Scope

Feature specs capture implementation-level detail for a single feature. Product requirements belong in the PRD; architecture in system-design. Feature-scoped decisions stay here; system-wide decisions go in ADRs.

Input

Synthesize from whatever the user provides: conversation context, local docs, external links, direct prompts, or docs/knowledge/ entries (when explicitly referenced).

Workflow: Create
Normalize input into feature context: problem, users, constraints, open questions.
Map into template sections from references/feature-spec-template.md. Align to local convention if one exists.
Place at the repository's existing path, or fallback: docs/specs/{NNNN}-{feature-name}/spec.md. Determine {NNNN} by scanning existing specs and incrementing (start at 0001 if none exist).
Mark unknowns in Open Points — don't guess.
Set status to draft.
Workflow: Iterate
Read the existing spec in full.
Upstream check: If upstream docs exist (docs/PRD.md, docs/system-design.md), scan for conflicts. Warn the user if the update contradicts upstream scope, requirements, or architecture.
Identify what changed and why.
Update affected sections in place. Preserve unchanged content.
Update Last updated date.
Transition status when appropriate: draft → active → shipped, or any → deprecated.
Output
Create: complete spec.md at canonical path
Iterate: targeted updates to affected sections only
Unresolved decisions go in Open Points
Requirements are concrete and evaluable (FR and NFR)
Flows include success and failure paths
Boundaries clearly define owns vs does-not-own
Weekly Installs
13
Repository
commandosslabs/ai-devkit
GitHub Stars
3
First Seen
Mar 9, 2026