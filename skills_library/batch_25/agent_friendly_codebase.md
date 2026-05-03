---
title: agent-friendly-codebase
url: https://skills.sh/hornet1130/agent-friendly-codebase/agent-friendly-codebase
---

# agent-friendly-codebase

skills/hornet1130/agent-friendly-codebase/agent-friendly-codebase
agent-friendly-codebase
Installation
$ npx skills add https://github.com/hornet1130/agent-friendly-codebase --skill agent-friendly-codebase
SKILL.md
Agent-Friendly Codebase Audit

You are an AFC audit team conducting a structured investigation of a bounded work area. Your job is to uncover what makes this codebase hard for AI agents to work in, then tell the team exactly what's wrong and what to fix, in priority order.

The core insight: agents do what's written. What isn't written gets inferred. Inference fails. That failure compounds — like autoregressive token generation, one bad early judgment poisons everything built on top of it.

An agent-friendly codebase lets an agent:

reach relevant context with low exploration cost
make bounded changes with a predictable blast radius
verify changes with a short trusted proof path
hand off or split work with low ambiguity
Work area

A work area is an app, package, or service — a unit with its own entrypoints, public contracts, build/test/lint commands, and tests. This is the natural audit boundary because AFC scoring categories (commands, contracts, guidance hierarchy, verification) only have meaning at this level.

If the user points at a file, function, or feature directory, expand scope to the app or package it belongs to.

If the user names a path without specifying scope, propose a work area boundary by examining dependencies and contract surfaces. Present the proposed boundary for confirmation before proceeding.

If the area is too large for a single audit pass (e.g., a monorepo root or an app with many independent feature areas), recommend splitting into sub-areas and list them. Each sub-area can be audited independently — and in parallel if the environment supports subagents or agent teams. When parallel audits complete, aggregate into a single report: per-area AFC Scores, combined findings ordered by impact, and a unified improvement roadmap.

Examples: apps/web, apps/api, packages/shared/http-client

Workflow and output

Follow these steps in order. The output of each step becomes a section in the final report.

Step 1 — Bound the area

Identify the work area and produce the Area profile:

Bounded paths, entrypoints, key contracts
Canonical commands (install, build, test, lint, dev) and proof path
If the user mentions parallel agents or handoff, also map ownership lanes, handoff boundaries, and collision hotspots
Step 2 — Scan for friction patterns

Scan the area for patterns A, B, C, D (see "The four agent-friction patterns" below). Collect evidence.

Step 3 — Score

Score each category S1–S5 (see "AFC Score" below). Follow the scoring discipline: evidence first, score second.

Produce the AFC Score section: per-category score with evidence, total, and band.

Step 4 — Surface findings

Produce the Findings section. For each finding:

Finding: what's wrong
Pattern: A / B / C / D
Evidence: file paths, code, concrete observations
Agent impact: what an agent would do wrong because of this

Order by impact, not by category.

Step 5 — Build improvement roadmap

Produce the Improvement roadmap organized by maturity level (see "AFC maturity model" below), not by finding.

L1 — Enforce: tooling gates the team can add now
L2 — Document: what to write down so agents stop inferring
L3 — Specify: structural changes for machine-verified compliance

Each item must be specific enough to assign — file path, threshold, artifact name.

The four agent-friction patterns

Actively scan for these in Step 2. Each one is a distinct source of agent error.

Pattern A — Tacit knowledge

Things the team "just knows" but aren't written anywhere. A 5-year engineer knows "this API is only called with a valid agtCode." The agent doesn't — it infers, and inference fails.

Evidence: unexplained constraints, undocumented field semantics, "legacy" code with no recorded reason, business rules in Slack but not in code.

Pattern B — Code/doc divergence

README says one thing, code does another. The agent can't judge which to trust. Stale docs actively poison context — worse than no docs at all.

Evidence: outdated README, stale CLAUDE.md rules, comments describing what the code did months ago.

Pattern C — Competing patterns

Two ways to do the same thing coexist. The agent picks by frequency, not intent. CLAUDE.md says "use Jotai" but 40 Recoil files outnumber 3 Jotai files. Frequency beats documentation.

Evidence: multiple libraries for the same concern, two import styles, mixed async patterns, in-progress migration with no status marker.

Pattern D — No feedback loop

Without tests the agent can't verify its own work. It reports "done" and validation falls entirely to the human. Tests are the agent's only feedback loop.

Evidence: low test count, no CI gate, validation requiring manual inspection, no runnable proof path.

AFC Score

5 categories, each 0–20. Total 0–100, expressed as AFC Score (%).

Bands: Good >= 80, So-so 50–79, Bad < 50

Scoring anchors
Score	Meaning
0	absent — effectively unusable
5	weak — mostly implicit
10	partial — important gaps remain
15	solid — moderate friction only
20	explicit — current, low ambiguity

In-between scores allowed when evidence supports it. Must items present → above 10. Must items complete and working → 15. Should items → toward 20.

Scoring discipline
Evidence first, score second. List what you found before assigning a number. Never score then justify.
Each score must cite a specific file, section, or command. No evidence → score 0 or 5.
Default to the lower score when between two anchors. Upgrade only with clear evidence.
Absence = 0, not unknown. If reasonable exploration finds nothing, score 0.
S1. Boundary & entrypoints (0–20)

Can the agent find where to start and where to stop?

Must: name the primary paths, entrypoints, dependencies and reverse dependencies
Should: document usual starting files, keep frequently edited files easy to find
S2. Commands & environment (0–20)

Can the agent build, test, and run without human memory?

Must: define canonical install, build, test, lint, dev commands and keep them reproducible
Must: provide at least one automated validation path covering representative task types
Must: identify main logs, error paths, or state checkpoints
Should: area-scoped validation commands, common failure causes and workarounds, reusable fixtures/seeds/mocks/snapshots, regression coverage to catch obvious spillover
Should: debug starting points for common failures, env/config mismatch easy to check
S3. Contracts & change surface (0–20)

Can the agent predict blast radius from what's visible?

Must: expose public contracts (routes, APIs, schemas, DTOs, env dependencies) and external system boundaries
Must: make the common edit surface observable, explain when cross-boundary edits are required
Should: document failure modes, include input/output examples, expose shared package blast radius, avoid turning a small feature change into a repo-wide edit
S4. Context hierarchy & economy (0–20)

Is guidance high-signal, layered, and appropriately scoped?

Must: keep always-loaded rules short and high signal, push detail to supporting files
Must: distinguish repo-wide guidance from area-local guidance, let specific rules refine broader ones
Budget: root ~100-200 lines, area ~50-150 lines
Should: narrowing path root → app/service → feature/package, area-local skills close to code
S5. Examples, verification & persistence (0–20)

Can the agent learn from examples and verify its own work?

Must: provide at least one canonical example for a representative task type
Must: externalize recurring patterns, mistakes, conventions into docs, skills, tests, or ADRs
Must: define a lightweight audit rubric and proof path
Should: cover recurring tasks with diffs/PRs, structured gotchas and debug notes, explicit place for learned patterns, keep proof outputs when changes matter
AFC maturity model

Use these levels to frame improvement recommendations in Step 5. Each level is independently valuable.

L1 — Safety net: make wrong things impossible

Enforce via tooling. lint, tsc, build, test give immediate pass/fail.

CLAUDE.md can say "don't use Recoil" — but subagents may never see CLAUDE.md. A no-restricted-imports lint rule fires every time.

Examples: no-restricted-imports, pre-commit hooks on generated files, strict TS + no as any, coverage ratchet, codegen drift check.

L2 — Explicitness: make tacit knowledge explicit

Document what tooling can't enforce. Reduce inference.

Examples: single canonical pattern per problem, pipeline docs (source → generator → output → trigger), directory structure in CLAUDE.md, migration status table, "why" comments, domain glossary.

CLAUDE.md at app/package root only. More than that and noise exceeds signal.

L3 — Spec-driven: specs as input, machines verify compliance

The clearest input for an agent is a specification. Compliance is machine-verified.

Examples: SPEC.md → schema → test → implementation, Storybook stories as visual specs, scaffold generators, required SPEC.md per module.

L1 blocks what's forbidden. L3 verifies what's required.

Guardrails
More documentation is not improvement by default. Noisy docs burn context.
Prefer area-scoped guidance over repo-wide blanket rules.
Prefer executable verification over narrative claims.
Prefer a few high-value artifacts over documentation sprawl.
Be specific. "Add tests" is not a finding. Name the file, the gap, the impact.
Mark partial evidence as estimated or missing.
Weekly Installs
21
Repository
hornet1130/agen…codebase
GitHub Stars
2
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass