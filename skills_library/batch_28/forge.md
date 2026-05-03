---
title: forge
url: https://skills.sh/delexw/claude-code-misc/forge
---

# forge

skills/delexw/claude-code-misc/forge
forge
Installation
$ npx skills add https://github.com/delexw/claude-code-misc --skill forge
SKILL.md
Forge: JIRA Ticket → Dynamic Skill → Implementation
Inputs

Raw arguments: $ARGUMENTS

Infer from the arguments:

TICKET_URL: the JIRA ticket URL
ADDITIONAL_CONTEXT: any extra context provided beyond the URL (optional)

Orchestrates end-to-end JIRA ticket processing. Phases 1–5 gather context and write output files into a dynamically created skill at ~/.claude/skills/{ticket_id}/. Phase 6 invokes that skill — context files are lazy-loaded on demand.

Initialization — create skill directory at ~/.claude/skills/{ticket_id}/
JIRA Analysis (via Skill("jira-ticket-viewer"))
Discovery & Scanning (all 3.x run concurrently):
3.1 Domain Index (lightweight Glob/Grep)
3.2 Resource Scanning (links, Figma designs)
3.3 Page Inspection (conditional, via Skill("page-inspector"))
Prompt Optimization (conditional, via Skill("meta-prompter"))
Skill Generation — generate SKILL.md for the dynamic skill
Execute — invoke Skill("{ticket_id}-impl")

Also check the ADDITIONAL_CONTEXT as dev server info hint if provided.

Skill Dependencies

The following skills are invoked during orchestration:

Skill("jira-ticket-viewer") — Fetch JIRA ticket details via jira CLI
Skill("confluence-page-viewer") — Read Confluence pages via confluence CLI
Skill("figma-reader") — Read Figma designs (when Figma links present in ticket)
Skill("page-inspector") — Capture current page layout/styles as baseline (conditional: frontend/UI-affecting changes)
Skill("meta-prompter") — Prompt evaluation and optimization (conditional: skipped if ticket is well-specified)
Skill("{ticket_id}-impl") — Dynamically generated skill for execution (created in Phase 5)
Execution

Follow references/phases.md for step-by-step phase instructions.

Weekly Installs
60
Repository
delexw/claude-code-misc
GitHub Stars
1
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail