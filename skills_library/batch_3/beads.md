---
title: beads
url: https://skills.sh/steveyegge/beads/beads
---

# beads

skills/steveyegge/beads/beads
beads
Installation
$ npx skills add https://github.com/steveyegge/beads --skill beads
Summary

Dolt-backed issue tracker for multi-session work with dependencies and conversation compaction survival.

Persists task context across conversation compaction and multiple sessions using a local Dolt database, with atomic claim-and-start workflow to prevent race conditions
Tracks task dependencies, blockers, and discovery relationships; use bd ready to surface unblocked work and bd show <id> --long to recover full context after compaction
Essential commands: bd create, bd ready, bd update --claim, bd close, and bd dolt push for team sync; append --json for structured output in agent workflows
Requires bd CLI v0.60.0+, optional Git repository, and one-time bd init setup; includes error recovery guidance and troubleshooting for common I/O and database issues
SKILL.md
Beads - Persistent Task Memory for AI Agents

Graph-based issue tracker that survives conversation compaction. Provides persistent memory for multi-session work with complex dependencies.

bd vs TodoWrite

Decision test: "Will I need this context in 2 weeks?" YES = bd, NO = TodoWrite.

bd (persistent)	TodoWrite (ephemeral)
Multi-session, dependencies, compaction survival	Single-session linear tasks
Dolt-backed team sync	Conversation-scoped

See BOUNDARIES.md for detailed comparison.

Prerequisites
bd --version  # Requires v0.60.0+

bd CLI installed and in PATH
Git repository (optional — use BEADS_DIR + --stealth for git-free operation)
Initialization: bd init run once (humans do this, not agents)
CLI Reference

Run bd prime for AI-optimized workflow context (auto-loaded by hooks). Run bd <command> --help for specific command usage.

Essential commands: bd ready, bd create, bd show, bd update, bd close, bd dolt push

Session Protocol
bd ready — Find unblocked work
bd show <id> — Get full context
bd update <id> --claim — Claim and start work atomically
Add notes as you work (critical for compaction survival)
bd close <id> --reason "..." — Complete task
bd dolt push — Push to Dolt remote (if configured)
Output

Append --json to any command for structured output. Use bd show <id> --long for extended metadata. Status icons: ○ open ◐ in_progress ● blocked ✓ closed ❄ deferred.

Error Handling
Error	Fix
database not found	bd init <prefix> in project root
not in a git repository	git init first
disk I/O error (522)	Move .beads/ off cloud-synced filesystem
Status updates lag	Use server mode: bd dolt start

See TROUBLESHOOTING.md for full details.

Examples

Track a multi-session feature:

bd create "OAuth integration" -t epic -p 1 --json
bd create "Token storage" -t task --deps blocks:oauth-id --json
bd ready --json                    # Shows unblocked work
bd update <id> --claim --json      # Claim and start
bd close <id> --reason "Implemented with refresh tokens" --json


Recover after compaction: bd list --status in_progress --json then bd show <id> --long

Discover work mid-task: bd create "Found bug" -t bug -p 1 --deps discovered-from:<current-id> --json

Advanced Features
Feature	CLI	Resource
Molecules (templates)	bd mol --help	MOLECULES.md
Chemistry (pour/wisp)	bd pour, bd wisp	CHEMISTRY_PATTERNS.md
Agent beads	bd agent --help	AGENTS.md
Async gates	bd gate --help	ASYNC_GATES.md
Worktrees	bd worktree --help	WORKTREES.md
Resources
Category	Files
Getting Started	BOUNDARIES.md, CLI_REFERENCE.md, WORKFLOWS.md
Core Concepts	DEPENDENCIES.md, ISSUE_CREATION.md, PATTERNS.md
Resilience	RESUMABILITY.md, TROUBLESHOOTING.md
Advanced	MOLECULES.md, CHEMISTRY_PATTERNS.md, AGENTS.md, ASYNC_GATES.md, WORKTREES.md
Reference	STATIC_DATA.md, INTEGRATION_PATTERNS.md
Validation

If bd --version reports newer than 0.60.0, this skill may be stale. Run bd prime for current CLI guidance — it auto-updates with each bd release and is the canonical source of truth (ADR-0001).

Weekly Installs
765
Repository
steveyegge/beads
GitHub Stars
22.9K
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn