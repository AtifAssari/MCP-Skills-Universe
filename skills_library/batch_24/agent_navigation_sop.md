---
title: agent-navigation-sop
url: https://skills.sh/igorwarzocha/opencode-workflows/agent-navigation-sop
---

# agent-navigation-sop

skills/igorwarzocha/opencode-workflows/agent-navigation-sop
agent-navigation-sop
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill agent-navigation-sop
SKILL.md
Agent Navigation SOP

This SOP COMPLEMENTS the /init command by providing deep-dive mapping for developer-facing AGENTS.md files.

Tooling & Scripts: Identify one-shot commands for Build, Test, Lint, and Typecheck.
Process Constraints: Identify dev servers and watch-modes to EXCLUDE.
Conventions: Identify project-specific naming, architectural patterns, and unique error handling.
Phase 2: AGENTS.md Composition

Target a high-density output of ~50 lines.

1. Build & Test (Instructions)
List copy-pasteable, one-shot commands.
MUST NOT include dev, watch, or interactive commands.
2. Constraints & Patterns (Rules)
CRITICAL: The agent MUST explicitly forbid running blocking processes (dev servers, watch modes).
Identify read-only or restricted paths that agents SHOULD NOT modify.
Document repository-specific coding patterns (e.g., "Use Bun APIs", "Prefer functional over class").
3. Task Routing (Routing)
Map common tasks (feature addition, bug fix) to specific directories and related tests.
Reference nested AGENTS.md files for package-level details instead of duplicating them.
Identify repetitive tasks and SHOULD suggest creating new skills using skill-creator to extend agent capabilities.
Weekly Installs
35
Repository
igorwarzocha/op…orkflows
GitHub Stars
111
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass