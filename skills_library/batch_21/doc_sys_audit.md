---
title: doc-sys-audit
url: https://skills.sh/vladm3105/aidoc-flow-framework/doc-sys-audit
---

# doc-sys-audit

skills/vladm3105/aidoc-flow-framework/doc-sys-audit
doc-sys-audit
Installation
$ npx skills add https://github.com/vladm3105/aidoc-flow-framework --skill doc-sys-audit
SKILL.md
doc-sys-audit
Purpose

Run a single SYS audit workflow that executes:

doc-sys-validator (structural/schema gate)
doc-sys-reviewer (semantic/content quality gate)

Then emit one combined report optimized for doc-sys-fixer input.

Layer: 6 (SYS Quality Gate Wrapper)

Upstream: SYS file(s)

Downstream:

Combined Audit Report: SYS-NN.A_audit_report_vNNN.md
Optional Fix Cycle trigger for doc-sys-fixer
Why This Skill Exists

Use this wrapper to avoid user confusion between validator and reviewer while preserving separation of concerns.

Concern	Owner Skill
Schema/template compliance	doc-sys-validator
Content quality and requirement completeness	doc-sys-reviewer
Single user-facing audit command	doc-sys-audit
When to Use

Use doc-sys-audit when:

You want one command for SYS quality checks
You need a combined report for doc-sys-fixer
You are running QA before REQ generation

Do NOT use when:

SYS does not exist (use doc-sys / doc-sys-autopilot generation first)
You only need one specific check domain (use validator or reviewer directly)
Execution Contract
Input
SYS path (docs/06_SYS/SYS-NN_*/...)
Optional: threshold (default review threshold: 90)
Sequence (Mandatory)
1) Run doc-sys-validator
2) Run doc-sys-reviewer
3) Normalize and merge findings
4) Write SYS-NN.A_audit_report_vNNN.md
5) If auto-fixable findings exist, hand off to doc-sys-fixer

Combined Status Rules
PASS: Validator PASS AND Reviewer score >= threshold AND no blocking issues
FAIL: Validator FAIL OR Reviewer score < threshold OR blocking/manual-required issues present
Combined Report Format (for doc-sys-fixer)

Output file: SYS-NN.A_audit_report_vNNN.md

Required sections:

## Summary
SYS ID, timestamp (EST), overall status
Validator status, reviewer score
## Score Calculation (Deduction-Based)
Formula: 100 - total_deductions
Threshold comparison (>=90 pass gate)
## Validator Findings
List by severity/code
## Reviewer Findings
List by severity/code
## Coverage Findings
Requirement completeness summary
Quality attribute coverage summary
Traceability/tag coverage summary
## Fix Queue for doc-sys-fixer
auto_fixable
manual_required
blocked
## Recommended Next Step
run doc-sys-fixer
or manual update required
Fix Queue Normalization

Each finding MUST include:

source: validator | reviewer
code: issue code
severity: error|warning|info
file: relative path
section: heading/anchor if known
action_hint: short imperative guidance
confidence: high|medium|manual-required
Hand-off Contract to doc-sys-fixer

doc-sys-fixer MUST accept combined audit report as equivalent upstream input:

SYS-NN.A_audit_report_vNNN.md (preferred)
SYS-NN.R_review_report_vNNN.md (legacy compatibility)

Precedence rule:

Select newest timestamp.
If timestamps are equal, prefer .A_audit_report over .R_review_report.
Example Invocation
/doc-sys-audit docs/06_SYS/SYS-01_f1_iam/


Expected outcome:

validator runs
reviewer runs
combined audit report generated
fixer can execute directly from combined report
Version History
Version	Date	Changes
1.0	2026-02-27	Initial SYS audit wrapper; validator→reviewer orchestration; combined report contract for fixer with .A_ preferred and .R_ legacy compatibility
Implementation Plan Consistency (IPLAN-004)
Treat plan-derived outputs as valid source mode and verify intent preservation from implementation plan scope/objectives.
Validate upstream autopilot precedence assumption: --iplan > --ref > --prompt.
Flag objective/scope conflicts between plan context and artifact output as blocking issues requiring clarification.
Do not introduce legacy fallback paths such as docs-v2.0/00_REF.
Weekly Installs
23
Repository
vladm3105/aidoc…ramework
GitHub Stars
14
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass