---
title: code-simplify
url: https://skills.sh/paulrberg/agent-skills/code-simplify
---

# code-simplify

skills/paulrberg/agent-skills/code-simplify
code-simplify
Installation
$ npx skills add https://github.com/paulrberg/agent-skills --skill code-simplify
SKILL.md
Code Simplify
Objective

Simplify code while preserving behavior, public contracts, and side effects. Favor explicit code and local clarity over clever or compressed constructs.

Arguments
--no-verify: Skip verification because a parent orchestrator will verify the final result separately.
--no-report: Skip the full user-facing report. Keep only concise working notes needed by the caller.
Default: verify touched behavior and present the full report.
Scope Resolution
Verify repository context: git rev-parse --git-dir. If this fails, stop and tell the user to run from a git repository.
If user provides file paths/patterns, a commit/range, or a Resolved scope fenced block with one repo-relative path per line, scope is exactly those targets.
Otherwise, scope is only session-modified files. Do not include other uncommitted changes.
If there are no session-modified files, fall back to all uncommitted tracked + untracked files:
tracked: git diff --name-only --diff-filter=ACMR
untracked: git ls-files --others --exclude-standard
combine both lists and de-duplicate.
Exclude generated/low-signal files unless requested: lockfiles, minified bundles, build outputs, vendored code.
If scope still resolves to zero files, report and stop.
Operating Rules
Preserve runtime behavior exactly. Keep inputs, outputs, side effects, and error behavior stable.
Prefer project conventions over personal preferences. Infer conventions from existing code, linters, formatters, and tests.
Limit scope to user-requested files or recently modified code unless explicitly asked to broaden.
Make small, reversible edits. Avoid broad rewrites when targeted simplifications solve the problem.
Call out uncertainty immediately when behavior may change.
Workflow
1) Determine Scope
Resolve target files using the "Scope Resolution" section above.
2) Build a Behavior Baseline
Read surrounding context, not only changed lines.
Identify invariants that must not change:
function signatures and exported APIs
state transitions and side effects
persistence/network behavior
user-facing messages and error semantics where externally relied on
Note available verification commands (lint, tests, typecheck).
3) Apply Simplification Passes (in this order)
Control flow:
Flatten deep nesting with guard clauses and early returns.
Replace nested ternaries with clearer conditionals.
Naming and intent:
Rename ambiguous identifiers when local context supports safe renaming.
Separate mixed concerns into small helpers with intent-revealing names.
Duplication:
Remove obvious duplication.
Abstract only when at least two real call sites benefit and the abstraction reduces cognitive load.
Data shaping:
Break dense transform chains into named intermediate steps when readability improves.
Keep hot-path performance characteristics stable unless improvement is explicit and measured.
Type and contract clarity:
Add or tighten type annotations when they improve readability and safety without forcing broad churn.
Preserve external interfaces unless asked to change them.
4) Enforce Safety Constraints
Do not convert sync APIs to async (or reverse) unless explicitly requested.
Do not alter error propagation strategy unless behavior remains equivalent and verified.
Do not remove logging, telemetry, guards, or retries that encode operational intent.
Do not collapse domain-specific steps into generic helpers that hide intent.
5) Verify

Skip this step when --no-verify is set. Otherwise:

Run the narrowest useful checks first:
formatter/lint on touched files
targeted tests related to touched modules
typecheck when relevant
If fast targeted checks pass, run broader checks only when risk warrants it.
If checks cannot run, state what was skipped and why.
6) Report

Skip the full report when --no-report is set. In that mode, keep only terse working notes covering touched scope, key simplifications, and residual risks for a parent orchestrator.

Otherwise provide:

Scope touched (files/functions)
Key simplifications with concise rationale
Verification commands run and outcomes
Residual risks or assumptions
Simplification Heuristics
Prefer explicit local variables over nested inline expressions when it reduces cognitive load.
Prefer one clear branch per condition over compact but ambiguous condition trees.
Keep function length manageable, but do not split purely for line count.
Keep comments that explain intent, invariants, or non-obvious constraints.
Remove comments that restate obvious code behavior.
Optimize for the next maintainer's comprehension time, not minimum character count.
Anti-Patterns
Do not perform speculative architecture rewrites.
Do not introduce framework-wide patterns while simplifying a small local change.
Do not replace understandable duplication with opaque utility layers.
Do not bundle unrelated cleanups into one patch.
Stop Conditions
Stop and ask for direction when:
simplification requires changing public API/contracts
behavior parity cannot be confidently verified
the code appears intentionally complex due to domain constraints
the requested scope implies a larger redesign rather than simplification
Output Contract

When --no-report is not set, present simplification results like this:

Show the exact files and regions changed.
Explain each meaningful change in one sentence focused on readability/maintainability gain.
Confirm behavior-preservation assumptions explicitly.
Summarize verification performed (or clearly state omissions).
Weekly Installs
1.2K
Repository
paulrberg/agent-skills
GitHub Stars
51
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass