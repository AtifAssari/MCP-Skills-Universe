---
rating: ⭐⭐
title: cmk:codebase-summary
url: https://skills.sh/commandosslabs/ai-devkit/cmk:codebase-summary
---

# cmk:codebase-summary

skills/commandosslabs/ai-devkit/cmk:codebase-summary
cmk:codebase-summary
Installation
$ npx skills add https://github.com/commandosslabs/ai-devkit --skill cmk:codebase-summary
SKILL.md
Codebase Summary
Intents
Document the repository structure and key entry points

Update the codebase summary — we reorganized the src/ directory

Map the codebase so new contributors can get oriented quickly

Where does everything live in this project?

References

Read references/codebase-summary-conventions.md for placement rules and references/codebase-summary-template.md for section structure.

Scope

Codebase summary captures repository structure and navigation — how to find things. Architecture rationale belongs in system-design; feature behavior in specs.

Input

Synthesize from: direct codebase exploration (directories, entry points, modules), existing docs (README, package.json, etc.), conversation context, or direct prompts.

Workflow: Create
Explore the repository to understand layout, entry points, and module boundaries.
Map into template sections from references/codebase-summary-template.md. Align to local convention if one exists.
Place at the repository's existing path, or fallback: docs/codebase-summary.md.
Include local dev commands if discoverable.
Workflow: Iterate
Read the existing summary in full.
Explore current codebase to identify what changed.
Update affected sections in place. Preserve unchanged content.
Update Last updated date.
Output
Create: complete codebase summary at docs/codebase-summary.md
Iterate: targeted updates to affected sections only
Layout matches actual directory structure
Entry points and dev commands are current and runnable
No architecture rationale (belongs in system-design)
Weekly Installs
13
Repository
commandosslabs/ai-devkit
GitHub Stars
3
First Seen
Mar 9, 2026