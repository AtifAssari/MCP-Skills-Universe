---
title: security-reviewer-formats
url: https://skills.sh/microsoft/hve-core/security-reviewer-formats
---

# security-reviewer-formats

skills/microsoft/hve-core/security-reviewer-formats
security-reviewer-formats
Installation
$ npx skills add https://github.com/microsoft/hve-core --skill security-reviewer-formats
SKILL.md
Security Reviewer Formats — Skill Entry

This SKILL.md is the entrypoint for the security reviewer format specifications skill.

The skill provides shared format templates and data contracts used by the security reviewer orchestrator and its subagents during vulnerability assessments. Each reference file covers a focused area of the reporting pipeline.

Normative references
Report Formats — VULN_REPORT_V1 template, diff mode qualifiers, and PLAN_REPORT_V1 template.
Finding Formats — Finding Serialization Format and Verified Findings Collection Format.
Completion Formats — Scan Status Format, Scan Completion Format, and Minimal Profile Stub Format.
Severity Definitions — Standard severity level definitions for all OWASP skill assessments.
Skill layout
SKILL.md — this file (skill entrypoint).
references/ — format specification documents.
report-formats.md — full report templates for audit, diff, and plan modes.
finding-formats.md — serialization and collection formats for findings exchange between subagents.
completion-formats.md — status updates, completion summaries, and the minimal profile stub.
severity-definitions.md — severity level table shared across all assessments.

🤖 Crafted with precision by ✨Copilot following brilliant human instruction, then carefully refined by our team of discerning human reviewers.

Weekly Installs
9
Repository
microsoft/hve-core
GitHub Stars
1.0K
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass