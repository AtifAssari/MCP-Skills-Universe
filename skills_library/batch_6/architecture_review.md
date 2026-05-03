---
title: architecture-review
url: https://skills.sh/srstomp/pokayokay/architecture-review
---

# architecture-review

skills/srstomp/pokayokay/architecture-review
architecture-review
Installation
$ npx skills add https://github.com/srstomp/pokayokay --skill architecture-review
SKILL.md
Architecture Review

Analyze, audit, and improve project structure.

Key Principles
Measure before changing — Map structure and identify concrete issues before proposing changes
Clear boundaries — Layers (UI, logic, data) separated with consistent dependency direction
Colocation — Related code together; easy to find, change, and delete features
Incremental migration — Refactor in phases, validate each step with tests
Quick Assessment
No circular dependencies
Consistent directory naming and grouping (by feature or by type)
Single responsibility per file/module, reasonable file sizes (<500 lines)
External dependencies isolated, shared code properly extracted
New developers can navigate and find code for any feature easily
Quick Start Checklist
Map current structure: directory tree, dependency graph, module boundaries
Identify issues: circular deps, god modules, leaky abstractions, deep nesting
Classify severity: critical (blocks dev), high (maintenance burden), medium/low (friction)
Propose target structure with migration plan
Execute incrementally, validating with tests after each move
References
Reference	Description
analysis-techniques.md	Dependency graphs, complexity metrics, code analysis
refactoring-patterns.md	Safe refactoring techniques, migration strategies
structural-patterns.md	Directory structures for different project types
dependency-management.md	Circular deps, coupling, module boundaries
cleanup-strategies.md	Dead code removal, consolidation, naming conventions
anti-rationalization.md	Iron Law, common rationalizations, red flag STOP list for architecture discipline
Weekly Installs
249
Repository
srstomp/pokayokay
GitHub Stars
6
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass