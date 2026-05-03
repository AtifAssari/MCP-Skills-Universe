---
title: evolve
url: https://skills.sh/miles990/self-evolving-agent/evolve
---

# evolve

skills/miles990/self-evolving-agent/evolve
evolve
Installation
$ npx skills add https://github.com/miles990/self-evolving-agent --skill evolve
SKILL.md
⚠️ This file has moved

The Self-Evolving Agent skill has been reorganized into an atomic architecture.

New Location

👉 skills/SKILL.md

Quick Links
Module	Description	Path
Getting Started	入門與環境設定	→
Core	核心流程（PSB + PDCA）	→
Checkpoints	強制檢查點（護欄）	→
Memory	記憶系統操作	→
Emergence	涌現機制	→
Integration	外部工具整合	→
Scaling	大規模專案優化	→
Evolution	自我進化機制	→
Why the Change?
Easier to maintain: Small modules > monolithic file
Easier to contribute: Community content in community/ directories
Easier to learn: Read modules progressively
Easier to extend: Add new modules without touching existing content
Migration

If you were using the old SKILL.md, simply update your imports:

Old: SKILL.md (2000+ lines)
New: skills/SKILL.md (entry point) + skills/*/_base/*.md (modules)

Weekly Installs
93
Repository
miles990/self-e…ng-agent
GitHub Stars
1
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn