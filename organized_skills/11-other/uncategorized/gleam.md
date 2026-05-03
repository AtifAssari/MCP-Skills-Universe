---
rating: ⭐⭐⭐
title: gleam
url: https://skills.sh/anntnzrb/agents/gleam
---

# gleam

skills/anntnzrb/agents/gleam
gleam
Installation
$ npx skills add https://github.com/anntnzrb/agents --skill gleam
SKILL.md
Gleam Development

Idiomatic Gleam with type-driven design and TDD.

Workflow
1. MODEL    → Define domain types first (make illegal states unrepresentable)
2. RED      → Write failing test
3. GREEN    → Minimal implementation
4. REFACTOR → Clean up, use pipelines
5. RUN      → gleam test && gleam run

Research

Use context7 docs first, then gh as fallback. Routing table and example queries live in reference.md.

CLI
gleam check                    # Fast type feedback (use often)
gleam test                     # Run tests
gleam run                      # Execute main
gleam format                   # Format all
gleam add pkg --dev            # Dev dependency

References
reference.md - Research routing, patterns, anti-patterns
Weekly Installs
16
Repository
anntnzrb/agents
GitHub Stars
1
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn