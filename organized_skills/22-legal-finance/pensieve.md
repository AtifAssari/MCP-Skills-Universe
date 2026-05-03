---
rating: ⭐⭐
title: pensieve
url: https://skills.sh/kingkongshot/pensieve/pensieve
---

# pensieve

skills/kingkongshot/pensieve/pensieve
pensieve
Installation
$ npx skills add https://github.com/kingkongshot/pensieve --skill pensieve
SKILL.md
Pensieve

Route user requests to the correct tool. When in doubt, confirm first.

Routing
Init: Initialize the current project's user data directory and populate seed files. Tool spec: .src/tools/init.md.
Upgrade: Refresh Pensieve skill source code in the global git clone. Tool spec: .src/tools/upgrade.md.
Migrate: Structural migration and legacy cleanup. Tool spec: .src/tools/migrate.md.
Doctor: Read-only scan of the current project's user data directory. Tool spec: .src/tools/doctor.md.
Self-Improve: Extract reusable conclusions and write to user data. Tool spec: .src/tools/self-improve.md.
Refine: Refine the knowledge base (triage five-question review + compress abstraction). Tool spec: .src/tools/refine.md.
Graph View: Read <project-root>/.pensieve/.state/pensieve-user-data-graph.md.
Project Data

Project-level user data is stored in <project-root>/.pensieve/. See .pensieve/state.md for the current project's lifecycle state; see .pensieve/.state/pensieve-user-data-graph.md for the knowledge graph (read on demand).

Weekly Installs
15
Repository
kingkongshot/pensieve
GitHub Stars
2.5K
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn