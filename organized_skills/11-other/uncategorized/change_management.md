---
rating: ⭐⭐
title: change-management
url: https://skills.sh/7spade/black-tortoise/change-management
---

# change-management

skills/7spade/black-tortoise/change-management
change-management
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill change-management
SKILL.md
Change Management (Stable Interface / Deletion)
Use when
Changing public APIs across layers (ports, facades, stores).
Introducing a new pattern or architectural decision.
Workflow
Define minimal stable interface (MSI): smallest API callers need.
Prefer additive change; if breaking, include migration notes.
Add ADR-lite notes (what/why/risks) when boundaries change.
Verify deletion path: feature can be removed without global entanglement.
References
.github/instructions/68-change-management-copilot-instructions.md
Weekly Installs
8
Repository
7spade/black-tortoise
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass