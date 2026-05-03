---
rating: ⭐⭐
title: datocms-setup
url: https://skills.sh/datocms/agent-skills/datocms-setup
---

# datocms-setup

skills/datocms/agent-skills/datocms-setup
datocms-setup
Installation
$ npx skills add https://github.com/datocms/agent-skills --skill datocms-setup
SKILL.md
DatoCMS Setup

This is the single public setup entrypoint for DatoCMS project scaffolding. Keep the public surface small, inspect the repo first, and load only the internal recipe files needed for the user's requested outcome.

Workflow
Silently inspect the repo before asking questions, following references/repo-conventions.md and the shared rules in patterns/MANDATORY_RULES.md.
Read references/router.md.
Read references/recipe-manifest.json and select the smallest recipe or internal bundle that satisfies the request.
Use targeted mode when the request clearly names a setup outcome. Use discovery mode only when the request is broad or ambiguous:
Stage A picks the setup lane.
Stage B asks the smallest setup-specific follow-up only when repo inspection still leaves a high-impact decision unresolved.
Queue prerequisites from the manifest before dependent recipes. Never tell the user to invoke another setup skill separately.
For visual-editing, always apply draft-mode and content-link.
Add web-previews unless the user explicitly wants website-only click-to-edit.
Add realtime only when the user explicitly asks for live updates or confirms them in the Stage B follow-up.
Load only the selected recipes/<group>/<recipe>/recipe.md files, the shared setup references they call for, and the sibling-skill references they point to.
Patch existing project code in place by default instead of rewriting working implementations.
End with the shared handoff contract in patterns/OUTPUT_STATUS.md: report scaffolded vs production-ready, summarize the selected recipes, and list unresolved placeholders explicitly.
Rules
Do not load every recipe up front.
Do not reference or depend on any external setup bundles. Prefer sibling DatoCMS skill references over copied duplicates when a recipe reuses existing documentation.
Treat recipe ids such as draft-mode, web-previews, visual-editing, and migration-release-workflow as internal orchestration labels.
If several requested outcomes share a foundation, apply that foundation once and continue through the queued recipes.
If the user asks for broad setup, ask one compact grouped Stage A clarification pass, then execute the minimal recipe bundle.
Use Stage B only for unresolved, high-impact setup decisions that the repo cannot answer safely.
For migration-heavy requests, ask the smallest extra grouped follow-up needed to separate baseline migrations, named profiles, shared histories, release helpers, sandbox reset loops, and diff-based generation.
Report scaffolded when a recipe still depends on placeholders, provider choices, route mappings, or unresolved ownership the repo could not resolve automatically.
Report production-ready only when the selected recipe no longer depends on unresolved customer-specific values.
End by summarizing which internal recipes were used and which optional follow-up recipe ids are available inside datocms-setup.
Weekly Installs
79
Repository
datocms/agent-skills
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass