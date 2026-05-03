---
title: agentic-engineering
url: https://skills.sh/affaan-m/everything-claude-code/agentic-engineering
---

# agentic-engineering

skills/affaan-m/everything-claude-code/agentic-engineering
agentic-engineering
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill agentic-engineering
Summary

AI-driven engineering workflows with eval-first execution, task decomposition, and cost-aware model routing.

Defines an eval-first loop: establish baseline evals before implementation, then re-run post-execution to measure deltas and catch regressions
Decomposes work into 15-minute units with single dominant risks, independent verifiability, and clear done conditions
Routes tasks by complexity: Haiku for classification and boilerplate, Sonnet for implementation, Opus for architecture and multi-file invariants
Emphasizes review focus on invariants, edge cases, error boundaries, and security rather than style enforcement
Tracks cost discipline per task including model tier, token estimates, retries, and wall-clock time to guide escalation decisions
SKILL.md
Agentic Engineering

Use this skill for engineering workflows where AI agents perform most implementation work and humans enforce quality and risk controls.

Operating Principles
Define completion criteria before execution.
Decompose work into agent-sized units.
Route model tiers by task complexity.
Measure with evals and regression checks.
Eval-First Loop
Define capability eval and regression eval.
Run baseline and capture failure signatures.
Execute implementation.
Re-run evals and compare deltas.
Task Decomposition

Apply the 15-minute unit rule:

each unit should be independently verifiable
each unit should have a single dominant risk
each unit should expose a clear done condition
Model Routing
Haiku: classification, boilerplate transforms, narrow edits
Sonnet: implementation and refactors
Opus: architecture, root-cause analysis, multi-file invariants
Session Strategy
Continue session for closely-coupled units.
Start fresh session after major phase transitions.
Compact after milestone completion, not during active debugging.
Review Focus for AI-Generated Code

Prioritize:

invariants and edge cases
error boundaries
security and auth assumptions
hidden coupling and rollout risk

Do not waste review cycles on style-only disagreements when automated format/lint already enforce style.

Cost Discipline

Track per task:

model
token estimate
retries
wall-clock time
success/failure

Escalate model tier only when lower tier fails with a clear reasoning gap.

Weekly Installs
2.9K
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