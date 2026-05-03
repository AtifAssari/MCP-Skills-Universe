---
title: workspace-surface-audit
url: https://skills.sh/affaan-m/everything-claude-code/workspace-surface-audit
---

# workspace-surface-audit

skills/affaan-m/everything-claude-code/workspace-surface-audit
workspace-surface-audit
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill workspace-surface-audit
SKILL.md
Workspace Surface Audit

Read-only audit skill for answering the question "what can this workspace and machine actually do right now, and what should we add or enable next?"

This is the ECC-native answer to setup-audit plugins. It does not modify files unless the user explicitly asks for follow-up implementation.

When to Use
User says "set up Claude Code", "recommend automations", "what plugins or MCPs should I use?", or "what am I missing?"
Auditing a machine or repo before installing more skills, hooks, or connectors
Comparing official marketplace plugins against ECC-native coverage
Reviewing .env, .mcp.json, plugin settings, or connected-app surfaces to find missing workflow layers
Deciding whether a capability should be a skill, hook, agent, MCP, or external connector
Non-Negotiable Rules
Never print secret values. Surface only provider names, capability names, file paths, and whether a key or config exists.
Prefer ECC-native workflows over generic "install another plugin" advice when ECC can reasonably own the surface.
Treat external plugins as benchmarks and inspiration, not authoritative product boundaries.
Separate three things clearly:
already available now
available but not wrapped well in ECC
not available and would require a new integration
Audit Inputs

Inspect only the files and settings needed to answer the question well:

Repo surface
package.json, lockfiles, language markers, framework config, README.md
.mcp.json, .lsp.json, .claude/settings*.json, .codex/*
AGENTS.md, CLAUDE.md, install manifests, hook configs
Environment surface
.env* files in the active repo and obvious adjacent ECC workspaces
Surface only key names such as STRIPE_API_KEY, TWILIO_AUTH_TOKEN, FAL_KEY
Connected tool surface
Installed plugins, enabled connectors, MCP servers, LSPs, and app integrations
ECC surface
Existing skills, commands, hooks, agents, and install modules that already cover the need
Audit Process
Phase 1: Inventory What Exists

Produce a compact inventory:

active harness targets
installed plugins and connected apps
configured MCP servers
configured LSP servers
env-backed services implied by key names
existing ECC skills already relevant to the workspace

If a surface exists only as a primitive, call that out. Example:

"Stripe is available via connected app, but ECC lacks a billing-operator skill"
"Google Drive is connected, but there is no ECC-native Google Workspace operator workflow"
Phase 2: Benchmark Against Official and Installed Surfaces

Compare the workspace against:

official Claude plugins that overlap with setup, review, docs, design, or workflow quality
locally installed plugins in Claude or Codex
the user's currently connected app surfaces

Do not just list names. For each comparison, answer:

what they actually do
whether ECC already has parity
whether ECC only has primitives
whether ECC is missing the workflow entirely
Phase 3: Turn Gaps Into ECC Decisions

For every real gap, recommend the correct ECC-native shape:

Gap Type	Preferred ECC Shape
Repeatable operator workflow	Skill
Automatic enforcement or side-effect	Hook
Specialized delegated role	Agent
External tool bridge	MCP server or connector
Install/bootstrap guidance	Setup or audit skill

Default to user-facing skills that orchestrate existing tools when the need is operational rather than infrastructural.

Output Format

Return five sections in this order:

Current surface
what is already usable right now
Parity
where ECC already matches or exceeds the benchmark
Primitive-only gaps
tools exist, but ECC lacks a clean operator skill
Missing integrations
capability not available yet
Top 3-5 next moves
concrete ECC-native additions, ordered by impact
Recommendation Rules
Recommend at most 1-2 highest-value ideas per category.
Favor skills with obvious user intent and business value:
setup audit
billing/customer ops
issue/program ops
Google Workspace ops
deployment/ops control
If a connector is company-specific, recommend it only when it is genuinely available or clearly useful to the user's workflow.
If ECC already has a strong primitive, propose a wrapper skill instead of inventing a brand-new subsystem.
Good Outcomes
The user can immediately see what is connected, what is missing, and what ECC should own next.
Recommendations are specific enough to implement in the repo without another discovery pass.
The final answer is organized around workflows, not API brands.
Weekly Installs
1.5K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass