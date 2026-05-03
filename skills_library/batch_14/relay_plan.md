---
title: relay-plan
url: https://skills.sh/sungjunlee/dev-relay/relay-plan
---

# relay-plan

skills/sungjunlee/dev-relay/relay-plan
relay-plan
Installation
$ npx skills add https://github.com/sungjunlee/dev-relay --skill relay-plan
SKILL.md
Relay Plan

Build a scoring rubric from the task's intended outcome: explicit Acceptance Criteria (AC) when available, inferred Done Criteria when missing or incomplete, repo quality signals, historical relay signal, and task-specific risk. Then generate a dispatch prompt that drives autonomous iteration until convergence.

Process
1. Read the task

Read the normalized task source (try in order, use first that succeeds):

Relay-ready handoff brief from relay-intake: ~/.relay/requests/<repo-slug>/<request-id>/relay-ready/<leaf-id>.md
Local task file: backlog/tasks/{PREFIX}-{N} - {Title}.md
GitHub: gh issue view <N>
User-provided description

If relay-intake already produced a handoff brief, treat that file as the source of truth instead of re-reading the raw request.

2. Read historical signal

Before designing the rubric, read relay reliability history:

node ${CLAUDE_SKILL_DIR}/../relay-dispatch/scripts/reliability-report.js --repo . --json


Use historical_signal.stuck_factors, divergence_hotspots, and avg_rounds to tighten factor wording and calibration. The signal does not gate dispatch or alter state. Empty/failure cases render as no historical data available; details: references/signals.md.

3. Read probe quality signals

Before designing the rubric, read repo-local quality signals:

node ${CLAUDE_SKILL_DIR}/scripts/probe-executor-env.js . --project-only --json


Use probe_signal.test_infra, lint_format, type_check, ci, and scripts to inform rubric design, prerequisites, and Available Tools. The signal exposes data; it does not pick. No-signal/failure cases render as no quality infra detected; details: references/signals.md. The test_infra field is consumed by references/rubric-pattern-tdd-flavor.md and scripts/tdd-suggestion.js.

4. Recover Done Criteria

Before drafting factors, identify the evaluation source model:

Explicit AC from the task source, when present
Inferred Done Criteria from user intent, issue body, relay-intake handoff, and nearby repo conventions
Repo quality signal from probes and available commands
Historical relay signal from stuck factors and score divergence
Task-specific risk from touched domains, trust boundaries, data loss, migrations, UX flows, or operational failure modes

If AC are missing, vague, or incomplete, write observable Done Criteria first. Treat explicit AC as high-priority evidence, not the only source. If the final review anchor is planner-authored or differs from the task source, persist it in step 8 so the reviewer has the same anchor.

5. Build the rubric

Use the guided interview (references/rubric-design-guide.md) to synthesize factors from the recovered Done Criteria, or convert directly:

rubric:
  prerequisites:
    - command: "npm test"
      target: "exit 0"
  factors:
    - name: API returns cursor-paginated response
      tier: contract
      type: automated
      command: "curl -s localhost:3000/api/items?limit=10 | jq '.next_cursor'"
      target: "non-null cursor string"
      weight: required
    - name: Pagination robustness
      tier: quality
      type: evaluated
      criteria: "Last page works; cursor is opaque and stable under writes."
      scoring_guide: { low: "happy path only", mid: "last page handled", high: "opaque stable cursor" }
      target: ">= 8/10"
      weight: required


Tier classification, type, weight, setup/baseline, criteria, scoring_guide, and optional per-factor tdd_anchor / tdd_runner: see references/rubric-design-guide.md. For event-schema evolution, use the event-shape rubric pattern. For red-first factor opt-in, use the TDD factor flavor pattern.

Domain references

Consult references/rubric-*.md for frontend, backend, security, refactoring, documentation, and design thinking. Design factors from task-specific evidence and risk, informed by references.

Trust-model audit factor (auth-boundary tasks)

If the task crosses an auth boundary (trust root, anchor, invariant, validate, forge, bypass, gate-check, auth-boundary, or validateTransition* / validateManifest* / evaluateReviewGate), follow references/rubric-trust-model.md. Each question becomes a named factor. Record answers under ### Trust-model audit in the PR body before dispatch.

6. Validate the rubric

Quick gate before dispatch:

Prerequisites hold repo-wide hygiene only; factors stay substantive (tier test)
Contract/Quality tier minimums met for task size (S/M/L/XL)
S-size mechanical tasks may use 1 contract factor and no quality factor; do not invent quality factors just to fill a quota
≥ 1 automated check across prerequisites + factors
Every evaluated factor has scoring_guide with low/mid/high anchors
Criteria are specific and reference discoverable artifacts; targets are concrete

Full checklist, factor counts, grading, and risk signals: references/rubric-validation.md. Grade D = revise; Grade C = warn and state the tradeoff.

7. Simplify the rubric

Before persisting the draft rubric, apply the 6 heuristics in references/rubric-simplification.md.

Apply to all task sizes: rewrite HOW into observable WHAT, merge overlaps, remove unsupported defensive clauses, and verify weights.

8. Persist planner-authored Done Criteria

If operator planning writes the final Done Criteria, persist that decision before dispatch so fresh-context review uses the same anchor. This includes AC-missing inputs, user-provided descriptions, and any case where planning expands, rejects, or narrows issue-body AC:

node ${CLAUDE_SKILL_DIR}/scripts/persist-done-criteria.js --repo . \
  --run-id "$RUN_ID" --file /tmp/done-criteria-<N>.md --json


Dispatch with the same RUN_ID and --done-criteria-file ~/.relay/runs/<repo-slug>/$RUN_ID/done-criteria.md. Skip this step only when the issue or intake handoff already provides the final Done Criteria without planner changes.

9. Review the rubric (triggered by ambiguity/risk)

S/M usually skips, but ambiguity or risk can opt any size into stress-test. Run stress-test for L/XL rubrics with evaluated factors and an ambiguity/risk signal, and for smaller rubrics when the recovered Done Criteria are novel, vague, or easy to game. XL adds calibration simulation only when novel or subjective evaluated factors need it. Skip re-dispatches with iteration history, all-automated rubrics, and simple tasks where recovered Done Criteria map cleanly to checks. Protocol: references/rubric-stress-test.md.

10. Generate dispatch prompt

Take the base template (../relay/references/prompt-template.md) and append Setup, Scoring Rubric, Iteration Protocol, and Score Log sections. Insert the optional Step 0a block from references/iteration-protocol.md iff any factor has a non-empty tdd_anchor; when no factor has tdd_anchor, keep the emitted prompt identical to the pre-TDD baseline.

Full iteration-protocol text + Score Log format: references/iteration-protocol.md.

11. Dispatch

Write the rubric YAML to a temp file alongside the dispatch prompt. Every relay dispatch must pass --rubric-file so the rubric is persisted at anchor.rubric_path for review and merge gates.

node ${CLAUDE_SKILL_DIR}/../relay-dispatch/scripts/dispatch.js . \
  -b issue-42 --prompt-file /tmp/dispatch-42.md --rubric-file /tmp/rubric-42.yaml --timeout 3600

When to use

All tasks dispatched via relay. Rubric depth scales with task size (determined by orchestrator judgment on recovered Done Criteria, file scope, ambiguity, and risk, not raw issue AC count):

S (simple fix, typo, 1-liner): 1 contract factor; add a quality factor only when the task has real design judgment; skip stress-test
M (standard feature): 3-5 factors, skip stress-test
L (cross-cutting, multi-file): 4-6 factors; stress-test only when evaluated factors plus ambiguity/risk signal exist
XL (architecture change): 5-8 factors; stress-test only when evaluated factors plus ambiguity/risk signal exist; add calibration only when useful

Re-dispatches automatically prepend previous Score Log + reviewer feedback to the prompt (see relay-dispatch docs). Full rubric guide: references/rubric-design-guide.md.

Weekly Installs
13
Repository
sungjunlee/dev-relay
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn