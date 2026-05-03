---
title: self-improvement-ci
url: https://skills.sh/pskoett/pskoett-ai-skills/self-improvement-ci
---

# self-improvement-ci

skills/pskoett/pskoett-ai-skills/self-improvement-ci
self-improvement-ci
Installation
$ npx skills add https://github.com/pskoett/pskoett-ai-skills --skill self-improvement-ci
Summary

Automated learning capture in CI pipelines that deduplicates failure patterns and proposes prevention rules.

Inspects PR check results and CI failures to identify recurring patterns tracked by stable pattern_key, promoting only when recurrence thresholds are met (3+ occurrences across 2+ distinct runs within 30 days)
Ingests learning candidates from simplify-and-harden-ci and emits machine-readable YAML output without interactive prompts, suitable for headless GitHub Actions workflows
Promotes durable prevention rules to documentation targets like CLAUDE.md, AGENTS.md, and .github/copilot-instructions.md when recurrence signals justify it
Requires GitHub Actions, authenticated GitHub CLI, and gh-aw extension for workflow authoring and validation
SKILL.md
Self-Improvement CI
Install
gh skill install pskoett/pskoett-skills self-improvement-ci


Fallback using the Agent Skills CLI:

npx skills add pskoett/pskoett-skills/skills/self-improvement-ci

Purpose

Run self-improvement in CI without interactive chat loops:

Inspect PR check results and CI failures
Ingest learning candidates from simplify-and-harden-ci
Deduplicate recurring patterns by stable pattern_key
Emit promotion-ready suggestions for agent context/system prompts

Use self-improvement for interactive/local sessions.

Context Limitation (Important)

CI agents do not have peak task context from the original implementation session. Use this skill to aggregate recurring patterns across runs, not to infer nuanced one-off intent.

Implications:

Favor stable pattern_key recurrence signals over single-run conclusions
Require recurrence thresholds before promotion
Route uncertain or high-impact recommendations to interactive review
Prerequisites
GitHub Actions enabled for the repository
GitHub CLI authenticated (gh auth status)
gh-aw installed for authoring/validation:
gh extension install github/gh-aw

CI Contract

The CI skill must:

Read only PR-scoped data (checks, workflow outcomes, existing learning entries)
Avoid direct code modifications in CI
Emit machine-readable learning output
Recommend promotion only when recurrence thresholds are met
Output Schema
self_improvement_ci:
  source:
    pr_number: 123
    commit_sha: "abc123"
  candidates:
    - pattern_key: "harden.input_validation"
      source: "simplify-and-harden-ci"
      recurrence_count: 3
      first_seen: "2026-02-01"
      last_seen: "2026-02-20"
      severity: "high"
      suggested_rule: "Validate and bound-check external inputs before use."
      promotion_ready: true
  summary:
    candidates_total: 4
    promotion_ready_total: 1
    followup_required: true

Recurrence and Promotion Rules
Track recurrence by pattern_key
Default threshold for promotion:
recurrence_count >= 3
seen in >= 2 distinct tasks/runs
within a 30-day window
Promotion targets:
CLAUDE.md
AGENTS.md
.github/copilot-instructions.md
SOUL.md / TOOLS.md when using openclaw workspace memory
Authoring Workflow (gh-aw)

Example-only templates live in references/workflow-example.md. Keep examples outside .github/workflows until you explicitly decide to enable CI automation.

When ready:

Copy the template into .github/workflows/self-improvement-ci.md
Customize tool access, outputs, and policy thresholds
Validate:
gh aw compile --validate --strict

Trigger test run manually:
gh aw run self-improvement-ci --push

Integration with Other Skills
Pair with simplify-and-harden-ci to ingest simplify_and_harden.learning_loop.candidates
Feed promoted patterns back into self-improvement memory workflow for durable prevention rules
Weekly Installs
453
Repository
pskoett/pskoett…i-skills
GitHub Stars
158
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass