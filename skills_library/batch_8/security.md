---
title: security
url: https://skills.sh/boshu2/agentops/security
---

# security

skills/boshu2/agentops/security
security
Installation
$ npx skills add https://github.com/boshu2/agentops --skill security
SKILL.md
Security Skill

Purpose: Run repeatable security checks across code, scripts, hooks, and release gates.

Use this skill when you need deterministic security validation before merge/release, or recurring scheduled checks.

Quick Start
/security                      # quick security gate
/security --full               # full gate with test-inclusive toolchain checks
/security --release            # full gate for release readiness
/security --json               # machine-readable report output

Execution Contract
1) Pre-PR (fast)

Run quick gate:

scripts/security-gate.sh --mode quick


Expected behavior:

Fails on high/critical findings from available scanners.
Writes artifacts under $TMPDIR/agentops-security/<run-id>/.
2) Pre-Release (strict)

Run full gate:

scripts/security-gate.sh --mode full


Expected behavior:

Full scanner pass before release workflow can continue.
Artifacts retained for audit and incident response.
3) Nightly (continuous)

Nightly workflow should run:

scripts/security-gate.sh --mode full


Expected behavior:

Detects drift/regressions outside active PR windows.
Failing run creates actionable signal in workflow summary/issues.
Triage Guidance

When gate fails:

Open latest artifact in $TMPDIR/agentops-security/ and identify scanner + file.
Classify severity (critical/high/medium).
Fix immediately for critical/high or create tracked follow-up issue with owner.
Re-run scripts/security-gate.sh until gate passes.
Reporting Template
Security gate run: <run-id>
Mode: <quick|full>
Result: <pass|blocked>
Top findings:
- <scanner> <severity> <file> <summary>
Actions:
- <fix or issue id>

Notes
Use this as the canonical security runbook instead of ad-hoc scanner commands.
Keep workflow wiring aligned with this contract in:
.github/workflows/validate.yml
.github/workflows/nightly.yml
.github/workflows/release.yml
For binary/internal black-box assurance plus offline repo-surface redteam, use:
skills/security-suite/SKILL.md (includes security_suite.py and prompt_redteam.py)
For dependency vulnerability and license scanning, use:
deps — Dependency audit, vulnerability scanning, and license compliance
Examples
Scenario: Quick Security Gate Before Opening a PR

User says: /security

What happens:

The skill runs scripts/security-gate.sh --mode quick, which executes available scanners (semgrep, gosec, gitleaks) against the current working tree and flags high/critical findings.
Run /deps vuln to scan for vulnerable dependencies (OWASP A06: Vulnerable and Outdated Components).
Scan artifacts are written to $TMPDIR/agentops-security/<run-id>/ for review, and the gate reports a pass/blocked verdict.

Result: The gate passes with no high/critical findings, confirming the branch is safe to open a PR.

Scenario: Full Security Gate for a Release

User says: /security --release

What happens:

The skill runs scripts/security-gate.sh --mode full, which performs a comprehensive scan including all scanner passes, test-inclusive toolchain checks, and stricter severity thresholds.
Artifacts are retained under $TMPDIR/agentops-security/<run-id>/ for audit trail and incident response, and a structured report is generated.

Result: The full gate blocks the release on two medium-severity findings in cli/internal/config.go; the operator triages and fixes them before re-running the gate to get a clean pass.

Troubleshooting
Problem	Cause	Solution
Gate reports "scanner not found" and skips checks	Required scanner (semgrep, gosec, or gitleaks) is not installed	Install the missing scanner: brew install semgrep, go install github.com/securego/gosec/v2/cmd/gosec@latest, or brew install gitleaks.
Gate passes locally but fails in CI	CI environment has additional scanners or stricter config	Compare $TMPDIR/agentops-security/ artifacts from both environments; align scanner versions and config files across local and CI.
False positive blocking the gate	Scanner flags a non-issue as high/critical severity	Add a scanner-specific inline suppression comment (e.g., # nosemgrep: rule-id) or update the scanner config to exclude the pattern, then document the suppression reason.
Artifacts directory $TMPDIR/agentops-security/ not created	Script lacks write permissions or $TMPDIR is not writable	Verify $TMPDIR is set and writable; the script auto-creates subdirectories on each run.
Nightly scan not detecting regressions	Nightly workflow is not configured or is pointing at stale branch	Verify .github/workflows/nightly.yml runs scripts/security-gate.sh --mode full against the correct branch (typically main).
Weekly Installs
418
Repository
boshu2/agentops
GitHub Stars
323
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass