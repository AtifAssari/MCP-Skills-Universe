---
rating: ⭐⭐
title: skill-optimizer
url: https://skills.sh/mcollina/skills/skill-optimizer
---

# skill-optimizer

skills/mcollina/skills/skill-optimizer
skill-optimizer
Installation
$ npx skills add https://github.com/mcollina/skills --skill skill-optimizer
SKILL.md
When to use

Use this skill when you need to:

Improve whether a skill is actually applied by models
Diagnose why some criteria fail across all models
Prevent a skill from making outputs worse
Refactor skill text for stronger retrieval under context pressure
Build repeatable benchmark loops and release gates
Optimization loop (default workflow)
Measure baseline and skill-on behavior (per model, per scenario, per criterion)
Find failure pattern:
universal failure (0% with skill)
model-specific weakness
regression (negative delta)
Edit for salience:
add explicit triggers
add concrete integrated examples
tighten checklists and decision rules
Re-run evals and compare deltas
Ship with guardrails (documented gate + run history + follow-up issues)
How to use

Read individual rule files for detailed procedures and templates:

rules/benchmark-loop.md - End-to-end benchmark loop and scoring
rules/activation-design.md - Improve retrieval and instruction uptake
rules/context-budget.md - Reduce token cost without losing behavior
rules/regression-triage.md - Diagnose and fix skill-on regressions
rules/release-gates.md - Go/no-go criteria before shipping skill updates
Practical heuristics
Prefer few high-signal rules over many soft recommendations
Put fragile, high-value behaviors in top-level checklists
Include at least one integrated example per common scenario
Add explicit wording for what must not be omitted
Track gains/losses with with-skill vs without-skill comparisons
Weekly Installs
442
Repository
mcollina/skills
GitHub Stars
1.8K
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass