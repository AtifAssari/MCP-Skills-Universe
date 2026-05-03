---
rating: ⭐⭐
title: ralphinho-rfc-pipeline
url: https://skills.sh/affaan-m/everything-claude-code/ralphinho-rfc-pipeline
---

# ralphinho-rfc-pipeline

skills/affaan-m/everything-claude-code/ralphinho-rfc-pipeline
ralphinho-rfc-pipeline
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill ralphinho-rfc-pipeline
Summary

Multi-agent DAG execution framework for decomposing large features into independently verifiable work units with quality gates.

Structures complex features as directed acyclic graphs with explicit dependencies, complexity tiers (isolated edits to schema/security changes), and per-unit acceptance criteria
Enforces a seven-stage pipeline: RFC intake, DAG decomposition, unit assignment, implementation, validation, merge queue processing, and final system verification
Implements merge queue rules preventing dependency failures, enforcing rebasing on the integration branch, and re-running tests after each merge
Includes recovery mechanisms for stalled units: eviction, findings snapshot, scope regeneration, and retry with updated constraints
Produces RFC execution logs, unit scorecards, dependency graphs, and integration risk summaries for visibility across the orchestration workflow
SKILL.md
Ralphinho RFC Pipeline

Inspired by humanplane style RFC decomposition patterns and multi-unit orchestration workflows.

Use this skill when a feature is too large for a single agent pass and must be split into independently verifiable work units.

Pipeline Stages
RFC intake
DAG decomposition
Unit assignment
Unit implementation
Unit validation
Merge queue and integration
Final system verification
Unit Spec Template

Each work unit should include:

id
depends_on
scope
acceptance_tests
risk_level
rollback_plan
Complexity Tiers
Tier 1: isolated file edits, deterministic tests
Tier 2: multi-file behavior changes, moderate integration risk
Tier 3: schema/auth/perf/security changes
Quality Pipeline per Unit
research
implementation plan
implementation
tests
review
merge-ready report
Merge Queue Rules
Never merge a unit with unresolved dependency failures.
Always rebase unit branches on latest integration branch.
Re-run integration tests after each queued merge.
Recovery

If a unit stalls:

evict from active queue
snapshot findings
regenerate narrowed unit scope
retry with updated constraints
Outputs
RFC execution log
unit scorecards
dependency graph snapshot
integration risk summary
Weekly Installs
2.5K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass