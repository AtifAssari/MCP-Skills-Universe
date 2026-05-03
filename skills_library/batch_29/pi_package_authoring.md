---
title: pi-package-authoring
url: https://skills.sh/romiluz13/pi-agent-skills/pi-package-authoring
---

# pi-package-authoring

skills/romiluz13/pi-agent-skills/pi-package-authoring
pi-package-authoring
Installation
$ npx skills add https://github.com/romiluz13/pi-agent-skills --skill pi-package-authoring
SKILL.md
Pi package authoring
Grounding
pi-mono/packages/coding-agent/docs/packages.md — manifest, install commands, layout.
pi-mono/packages/coding-agent/README.md — Pi Packages section (pi install, package.json pi key, keywords).
pi-mono/packages/coding-agent/src/core/package-manager.ts — resourcePrecedenceRank (package-origin resources sort after user/project).
Invariants
Packages integrate through the same resource resolution pipeline as local dirs; package-origin metadata ranks after user/project auto paths — see resourcePrecedenceRank in pi-mono/packages/coding-agent/src/core/package-manager.ts.
Third-party packages execute code; skills can instruct arbitrary actions — security notes are first-party in docs/packages.md and coding-agent README.
Workflows
Define a package: Mirror the package.json example from docs/packages.md / README; verify conventional dirs (skills/, extensions/, etc.) against those docs.
Predict overrides: Combine package-manager precedence with loadSkills “first name wins” (pi-mono/packages/coding-agent/src/core/skills.ts).
Anti-patterns
Do not invent CLI flags not documented in docs/packages.md / README.
Weekly Installs
16
Repository
romiluz13/pi-ag…t-skills
GitHub Stars
11
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn