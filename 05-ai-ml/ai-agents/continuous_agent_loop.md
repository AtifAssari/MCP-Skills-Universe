---
rating: ⭐⭐
title: continuous-agent-loop
url: https://skills.sh/affaan-m/everything-claude-code/continuous-agent-loop
---

# continuous-agent-loop

skills/affaan-m/everything-claude-code/continuous-agent-loop
continuous-agent-loop
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill continuous-agent-loop
Summary

Decision framework for autonomous agent loops with quality gates, evals, and recovery patterns.

Four loop modes available: continuous-pr for CI/PR workflows, rfc-dag for RFC decomposition, infinite for exploratory parallel generation, and sequential as default
Recommended production stack combines RFC decomposition, code quality gates, eval harness, and session persistence for robust autonomous execution
Built-in failure mode detection covers loop churn, repeated retries, merge queue stalls, and cost drift with explicit recovery procedures
Recovery workflow includes loop freezing, harness audits, scope reduction, and replay with acceptance criteria to handle degraded states
SKILL.md
Continuous Agent Loop

This is the v1.8+ canonical loop skill name. It supersedes autonomous-loops while keeping compatibility for one release.

Loop Selection Flow
Start
  |
  +-- Need strict CI/PR control? -- yes --> continuous-pr
  |
  +-- Need RFC decomposition? -- yes --> rfc-dag
  |
  +-- Need exploratory parallel generation? -- yes --> infinite
  |
  +-- default --> sequential

Combined Pattern

Recommended production stack:

RFC decomposition (ralphinho-rfc-pipeline)
quality gates (plankton-code-quality + /quality-gate)
eval loop (eval-harness)
session persistence (nanoclaw-repl)
Failure Modes
loop churn without measurable progress
repeated retries with same root cause
merge queue stalls
cost drift from unbounded escalation
Recovery
freeze loop
run /harness-audit
reduce scope to failing unit
replay with explicit acceptance criteria
Weekly Installs
2.7K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass