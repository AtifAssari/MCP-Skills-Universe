---
title: implement
url: https://skills.sh/delexw/claude-code-misc/implement
---

# implement

skills/delexw/claude-code-misc/implement
implement
Installation
$ npx skills add https://github.com/delexw/claude-code-misc --skill implement
SKILL.md
Contains Hooks

This skill uses Claude hooks which can execute code automatically in response to events. Review carefully before installing.

Implement: JIRA Ticket Processor
Arguments
$ARGUMENTS[0] — JIRA ticket URL (format: https://[domain].atlassian.net/browse/[TICKET-ID])
$ARGUMENTS[1] — Additional context (quoted string, optional)

Orchestrates end-to-end JIRA ticket processing:

Initialization
JIRA Analysis (via Skill("jira-ticket-viewer")) 2.5. Create Git Branch (named {TICKET-ID}-{slugified-title})
Discovery & Scanning (parallel):
3.1 Domain Discovery (via Skill("domain-discover"))
3.2 Resource Scanning (links, Figma designs)
3.3 Page Inspection (conditional, via Skill("page-inspector"))
Prompt Optimization (via Skill("meta-prompter"))
Implementation Planning (present plan, then proceed)
Execute per planning 6.5. QA Web Test (conditional: user-visible web changes)
Verification
Phase Dependencies

The following skills are invoked during execution using the Skill() tool:

Skill("jira-ticket-viewer") — Fetch JIRA ticket details via jira CLI
Skill("confluence-page-viewer") — Read Confluence pages via confluence CLI
Skill("figma-reader") — Read Figma designs (when Figma links present in ticket)
Skill("domain-discover") — Domain knowledge discovery
Skill("page-inspector") — Capture current page layout/styles as baseline (conditional: frontend/UI-affecting changes)
Skill("meta-prompter") — Prompt evaluation and optimization
Skill("qa-web-test") — Visual QA testing via Chrome DevTools MCP (conditional: user-visible web changes)
Execution

Follow references/phases.md for step-by-step phase instructions.

Weekly Installs
42
Repository
delexw/claude-code-misc
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn