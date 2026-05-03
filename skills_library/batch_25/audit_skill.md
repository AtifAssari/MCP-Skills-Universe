---
title: audit skill
url: https://skills.sh/bhargavtz/audit-skill/audit-skill
---

# audit skill

skills/bhargavtz/audit-skill/Audit Skill
Audit Skill
Installation
$ npx skills add https://github.com/bhargavtz/audit-skill --skill 'Audit Skill'
SKILL.md
When to use
Check for security vulnerabilities
Performance optimization
Instructions

A comprehensive audit skill that covers two major domains:

Full Codebase Audit — UI, bugs, accessibility, performance, security, test coverage
System Prompt Audit — AI agent architecture review, prompt quality scoring, bottleneck analysis

Read the relevant reference file(s) based on what the user needs:

Codebase audit → docs/references/codebase-audit.md
System prompt audit → docs/references/prompt-audit.md
Both → read both files
Step 1: Determine Audit Scope

Ask the user (or infer from context):

What is being audited? (repo URL/ZIP, pasted code, or system prompts)
What type of audit? (codebase, system prompts, or both)
Any specific flows, agents, or areas of concern?
Build commands, env vars, test credentials (for codebase audits)
Browsers/viewports to test (for UI audits)

If the user pastes code or prompts directly, begin immediately without asking.

Step 2: Run the Audit

Follow the instructions in the relevant reference file(s). Always:

Produce a human-readable Executive Summary (top 5 findings + business impact)
Produce a Technical Appendix (per-issue detail with file refs + line numbers)
Produce a JSON summary (machine-readable, see schema in references/json-schema.md)
Produce code patches or rewrites for all Critical/High issues
Produce a 2-week sprint plan
Step 3: Output Format

Always structure output as:

# Audit Report: [Project/System Name]

## Executive Summary
[Top 5 findings, business impact, remediation roadmap]

## Technical Findings
[Per-issue detail — see references for full format]

## Patches & Fixes
[Copy-paste ready code diffs for Critical/High issues]

## CI Recommendations
[Automated checks to add]

## Sprint Plan
[2-week remediation roadmap]

## JSON Summary
[Machine-readable findings]

Severity Definitions
Level	Definition
Critical	Data loss, security breach, system down, blocks all users
High	Major feature broken, significant UX failure, exploitable vuln
Medium	Degraded UX, minor data issue, non-critical bug
Low	Polish, minor inconsistency, nice-to-have improvement
Reference Files
docs/references/codebase-audit.md — Full instructions for repo/UI/bug/perf/security/a11y audit
docs/references/prompt-audit.md — Full instructions for AI system prompt audit
docs/references/json-schema.md — JSON output schema for both audit types
docs/examples/codebase-report.md — Example output for a codebase audit
docs/examples/prompt-report.md — Example output for a system prompt audit
Weekly Installs
–
Repository
bhargavtz/audit-skill
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail