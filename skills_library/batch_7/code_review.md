---
title: code-review
url: https://skills.sh/paulrberg/agent-skills/code-review
---

# code-review

skills/paulrberg/agent-skills/code-review
code-review
Installation
$ npx skills add https://github.com/paulrberg/agent-skills --skill code-review
SKILL.md
Code Review
Objective

Find high-impact defects in changed code with evidence. Prioritize security, correctness, and regressions over style nits.

Arguments
--fix: After reporting findings, apply all suggested fixes automatically in severity order (CRITICAL -> HIGH -> MEDIUM -> LOW), then rerun targeted checks and report exactly what changed.
--skip-profile <name>: Skip an optional domain profile by stem or filename. Repeatable. Example: --skip-profile naming.
Default: Report findings and wait for confirmation before editing.
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
Workflow
Resolve scope and read diffs plus minimal surrounding context.
Classify files by domain/risk.
Apply the core checks below plus only the domain profiles that match the current diff. Honor any --skip-profile exclusions.
Generate findings with: location, impact, evidence, confidence, and concrete fix.
Assign severity with the model below.
Default behavior: report and wait.
With --fix: apply all suggested fixes in severity order, then run targeted verification.
Report using the output schema below.
Core Review Checks

Apply on every run.

Checks
CORE-001 Behavior regression (HIGH): changed branch/state transition alters external behavior.
CORE-002 Error-path safety (HIGH): failures can cascade, crash, or return unsafe defaults.
CORE-003 Boundary handling (HIGH): null/empty/overflow/edge inputs are not handled.
CORE-004 Resource hygiene (MEDIUM): leaked timers/listeners/handles/connections.
CORE-005 Complexity hotspot (MEDIUM): change introduces avoidable coupling or hidden side effects.
CORE-006 Test gap (MEDIUM): changed behavior has no targeted test coverage.
Evidence Expectations
Show the concrete input/state that triggers failure.
Point to changed lines or nearby guards that caused the risk.
Profile Dispatch
references/profiles/security.md: auth, external input, secrets, crypto, public network surfaces, unsafe parsing.
references/profiles/configuration.md: env/config, timeouts, retries, pools, limits, resource tuning, rollout controls.
references/profiles/typescript-react.md: TypeScript/JavaScript/React/Node files.
references/profiles/python.md: Python services, scripts, async workloads.
references/profiles/shell.md: shell scripts, CI command blocks, deployment scripts.
references/profiles/smart-contracts.md: Solidity/Solana/on-chain protocol code.
references/profiles/data-formats.md: CSV/JSON/YAML/binary ingestion/export/parsing.
references/profiles/naming.md: naming/intent clarity after correctness and security issues are handled. This profile is optional and can be skipped explicitly.

Load only profiles relevant to touched files. Prefer no more than three domain profiles per pass unless the user requests a deep audit.

Severity Model
CRITICAL: exploitable security flaw, data loss path, or outage risk on critical paths.
HIGH: logic defect or performance failure that can break core behavior.
MEDIUM: maintainability/reliability issue likely to cause near-term defects.
LOW: localized clarity/style/documentation improvements.
Output Schema

Use this structure and order for every review result.

1. Scope

List reviewed files and any excluded patterns.

2. Findings (ordered)

Order by severity: CRITICAL -> HIGH -> MEDIUM -> LOW.

For each finding, use this shape:

[SEVERITY] Title — path/to/file.ext:line
Impact: concrete user/system impact.
Evidence: exact code behavior or diff evidence.
Fix: smallest practical remediation.
Confidence: high | medium | low.
3. Suggested Fixes

Include when not using --fix.

4. Applied Fixes

Include only when --fix is used. List each change with file references.

5. Verification

List commands run and outcomes. Explicitly list skipped checks.

6. Residual Risks / Open Questions

Capture unresolved assumptions and follow-ups.

Rules
Do not fabricate locations.
Merge duplicate findings.
Keep style-only issues at LOW unless they create operational risk.
Evidence Rules
Never fabricate line numbers.
Tie each finding to concrete code evidence.
Explain blast radius and failure mode succinctly.
Prefer targeted fixes over broad rewrites.
Verification

Run the narrowest checks that validate touched behavior:

formatter/lint on touched files,
targeted tests for impacted modules,
typecheck when relevant.

If checks cannot run, state exactly what was skipped and why.

Stop Conditions

Stop and ask for direction when:

fixes require API/contract redesign,
behavior intent is too ambiguous to classify severity,
required validation tooling is unavailable and risk is high.
Weekly Installs
1.1K
Repository
paulrberg/agent-skills
GitHub Stars
51
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail