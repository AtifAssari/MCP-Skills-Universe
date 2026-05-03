---
rating: ⭐⭐⭐
title: doc-bdd-audit
url: https://skills.sh/vladm3105/aidoc-flow-framework/doc-bdd-audit
---

# doc-bdd-audit

skills/vladm3105/aidoc-flow-framework/doc-bdd-audit
doc-bdd-audit
Installation
$ npx skills add https://github.com/vladm3105/aidoc-flow-framework --skill doc-bdd-audit
SKILL.md
doc-bdd-audit
Purpose

Run a single BDD audit workflow that executes:

doc-bdd-validator (structural/schema gate)
doc-bdd-reviewer (semantic/content quality gate)

Then emit one combined report optimized for doc-bdd-fixer input.

Layer: 4 (BDD Quality Gate Wrapper)

Upstream: BDD file(s)

Downstream:

Combined Audit Report: BDD-NN.A_audit_report_vNNN.md
Optional Fix Cycle trigger for doc-bdd-fixer
Why This Skill Exists

Use this wrapper to avoid user confusion between validator and reviewer while preserving separation of concerns.

Concern	Owner Skill
Schema/template compliance	doc-bdd-validator
Content quality and scenario completeness	doc-bdd-reviewer
Single user-facing audit command	doc-bdd-audit
When to Use

Use doc-bdd-audit when:

You want one command for BDD quality checks
You need a combined report for doc-bdd-fixer
You are running QA before ADR generation

Do NOT use when:

BDD does not exist (use doc-bdd / doc-bdd-autopilot generation first)
You only need one specific check domain (use validator or reviewer directly)
Execution Contract
Input
BDD path (docs/04_BDD/BDD-NN_*/...)
Optional: threshold (default review threshold: 90)
Sequence (Mandatory)
1) Run doc-bdd-validator
2) Run doc-bdd-reviewer
3) Normalize and merge findings
4) Write BDD-NN.A_audit_report_vNNN.md
5) If auto-fixable findings exist, hand off to doc-bdd-fixer

Combined Status Rules
PASS: Validator PASS AND Reviewer score >= threshold AND no blocking issues
FAIL: Validator FAIL OR Reviewer score < threshold OR blocking/manual-required issues present
Combined Report Format (for doc-bdd-fixer)

Output file: BDD-NN.A_audit_report_vNNN.md

Required sections:

## Summary
BDD ID, timestamp (EST), overall status
Validator status, reviewer score
## Score Calculation (Deduction-Based)
Formula: 100 - total_deductions
Threshold comparison (>=90 pass gate)
## Validator Findings
List by severity/code
## Reviewer Findings
List by severity/code
## Coverage Findings
Gherkin syntax compliance summary
Scenario completeness coverage summary
Traceability/tag coverage summary
## Fix Queue for doc-bdd-fixer
auto_fixable
manual_required
blocked
## Recommended Next Step
run doc-bdd-fixer
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
Hand-off Contract to doc-bdd-fixer

doc-bdd-fixer MUST accept combined audit report as equivalent upstream input:

BDD-NN.A_audit_report_vNNN.md (preferred)
BDD-NN.R_review_report_vNNN.md (legacy compatibility)

Precedence rule:

Select newest timestamp.
If timestamps are equal, prefer .A_audit_report over .R_review_report.
Example Invocation
/doc-bdd-audit docs/04_BDD/BDD-01_f1_iam/


Expected outcome:

validator runs
reviewer runs
combined audit report generated
fixer can execute directly from combined report
Version History
Version	Date	Changes
1.0	2026-02-27	Initial BDD audit wrapper; validator→reviewer orchestration; combined report contract for fixer with .A_ preferred and .R_ legacy compatibility
Implementation Plan Consistency (IPLAN-004)
Treat plan-derived outputs as valid source mode and verify intent preservation from implementation plan scope/objectives.
Validate upstream autopilot precedence assumption: --iplan > --ref > --prompt.
Flag objective/scope conflicts between plan context and artifact output as blocking issues requiring clarification.
Do not introduce legacy fallback paths such as docs-v2.0/00_REF.
Weekly Installs
22
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