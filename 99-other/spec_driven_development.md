---
title: spec-driven-development
url: https://skills.sh/n8n-io/n8n/spec-driven-development
---

# spec-driven-development

skills/n8n-io/n8n/spec-driven-development
spec-driven-development
Installation
$ npx skills add https://github.com/n8n-io/n8n --skill spec-driven-development
SKILL.md
Spec-Driven Development

Specs live in .claude/specs/. They are the source of truth for architectural decisions, API contracts, and implementation scope. Implementation and specs must stay in sync — neither leads exclusively.

Core Loop
Read spec → Implement → Verify alignment → Update spec or code → Repeat

Before Starting Work
Find the spec. Search .claude/specs/ for files matching the feature:
ls .claude/specs/


Read the full spec. Understand scope, decisions, API contracts, and open questions before writing code.

If no spec exists and the task is non-trivial (new module, new API, architectural change), ask the user whether to create one first.

During Implementation
Reference spec decisions — don't re-decide what the spec already settled.
When you diverge from the spec (better approach found, user requested change, constraint discovered), update the spec immediately in the same session. Don't leave spec and code out of sync.
Tick off TODO checkboxes (- [ ] → - [x]) as items are completed.
Strike through or annotate items that were deliberately skipped or replaced, with a brief reason:
- [x] ~~OpenRouter proxy~~ → Direct execution: nodes call OpenRouter directly

After Completing Work

Run a spec verification pass:

Re-read the spec alongside the implementation.
Check each section:
Do API endpoints in spec match the controller?
Do config/env vars in spec match the config class?
Does the module structure in spec match the actual file tree?
Do type definitions in spec match @n8n/api-types?
Are all TODO items correctly checked/unchecked?
Update the spec for any drift found. Common drift:
New files added that aren't listed in the structure section
API response shapes changed during implementation
Config defaults adjusted
Architectural decisions refined
Flag unresolved gaps to the user — things the spec promises but implementation doesn't deliver yet (acceptable for MVP, but should be noted).
Spec File Conventions
One or more markdown files per feature in .claude/specs/.
Keep specs concise. Use tables for mappings, code blocks for shapes.
Use ## Implementation TODO with checkboxes to track progress.
Split into multiple files when it helps (e.g. separate backend/frontend), but don't enforce a rigid naming scheme.
When the User Asks to "Self-Review" or "Verify Against Spec"
Read all relevant specs.
Read all implementation files.
Produce a structured comparison:
Aligned: items where spec and code match
Drift: items where they diverge (fix immediately)
Gaps: spec items not yet implemented (note as future work)
Fix drift, update specs, report gaps to the user.
Weekly Installs
142
Repository
n8n-io/n8n
GitHub Stars
186.4K
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass