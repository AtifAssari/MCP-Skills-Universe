---
title: generate-agent-instructions
url: https://skills.sh/sebkay/skills/generate-agent-instructions
---

# generate-agent-instructions

skills/sebkay/skills/generate-agent-instructions
generate-agent-instructions
Installation
$ npx skills add https://github.com/sebkay/skills --skill generate-agent-instructions
SKILL.md

Generate or update AGENTS.md using evidence from the current repository.

Ignore CLAUDE.md entirely if present.

Workflow
Locate existing AGENTS.md and treat it as the base when present.
Inspect the codebase deeply enough to understand:
Architecture across multiple files (major components, boundaries, data flow, and structural intent).
Real developer workflows (build, test, lint, run, debug, and release commands).
Project-specific conventions and non-obvious patterns.
Integrations, external services, and cross-component communication.
Extract only discoverable facts from code, config, scripts, and docs.
Merge intelligently with existing AGENTS.md: keep still-valid guidance, remove stale guidance, fill important gaps.
Write concise, actionable instructions targeted to future coding agents.
Output Requirements
Target roughly 20-50 lines in markdown.
Prefer repository-specific guidance over generic best practices.
Include concrete examples with key file or directory references.
Document current-state behavior only (no aspirational rules).
Preserve useful existing conventions from AGENTS.md when still accurate.
Keep wording imperative and easy to execute.
Quality Bar
Avoid assumptions that are not supported by repository evidence.
Prioritize information that prevents costly mistakes for new agents.
Capture the "why" behind important structure when it is inferable.

Update AGENTS.md, then ask the user for feedback on unclear or incomplete sections and iterate.

Weekly Installs
23
Repository
sebkay/skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass