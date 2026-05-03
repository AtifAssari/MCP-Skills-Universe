---
rating: ⭐⭐
title: cmk:prd
url: https://skills.sh/commandosslabs/ai-devkit/cmk:prd
---

# cmk:prd

skills/commandosslabs/ai-devkit/cmk:prd
cmk:prd
Installation
$ npx skills add https://github.com/commandosslabs/ai-devkit --skill cmk:prd
SKILL.md
PRD
Intents
We just discussed the billing system requirements — save that as a PRD

Use this Notion doc to draft a PRD for the new onboarding flow: [link]

Update the PRD — we're cutting the SSO requirement from v1

Let's define what we're building for the payments feature

Use our infrastructure knowledge to inform the PRD requirements

References

Read references/prd-conventions.md for placement rules and references/prd-template.md for section structure.

Scope

PRDs capture product/business "what and why." Technical architecture belongs in system-design; implementation detail in feature specs.

Input

Synthesize from whatever the user provides: conversation context, user research, local docs, external links (Notion, Google Docs), direct prompts, or docs/knowledge/ entries (when explicitly referenced).

Workflow: Create
Normalize input into product context: problem, timing, success criteria, user needs, scope.
Map into template sections from references/prd-template.md. Align to local convention if one exists.
Place at the repository's existing PRD path, or fallback: docs/PRD.md.
Mark unknowns in Open Points — don't guess.
Set status to draft.
Workflow: Iterate
Read the existing PRD in full.
Identify what changed and why.
Update affected sections in place. Preserve unchanged content.
Update Last updated date.
Transition status when appropriate: draft → active → decomposed → shipped, or any → deprecated.
Output
Create: complete PRD at docs/PRD.md with known context populated
Iterate: targeted updates to affected sections only
Unresolved decisions go in Open Points
Problem names a specific user segment with concrete pain
Success criteria are measurable with targets
No technical architecture detail
Weekly Installs
12
Repository
commandosslabs/ai-devkit
GitHub Stars
3
First Seen
Mar 9, 2026