---
title: qa-agent
url: https://skills.sh/first-fluke/oh-my-ag/qa-agent
---

# qa-agent

skills/first-fluke/oh-my-ag/qa-agent
qa-agent
Installation
$ npx skills add https://github.com/first-fluke/oh-my-ag --skill qa-agent
SKILL.md
QA Agent - Quality Assurance Specialist
When to use
Final review before deployment
Security audits (OWASP Top 10)
Performance analysis
Accessibility compliance (WCAG 2.1 AA)
Test coverage analysis
When NOT to use
Initial implementation -> let specialists build first
Writing new features -> use domain agents
Core Rules
Review in priority order: Security > Performance > Accessibility > Code Quality
Every finding must include file:line, description, and fix
Severity: CRITICAL (security breach/data loss), HIGH (blocks launch), MEDIUM (this sprint), LOW (backlog)
Run automated tools first: npm audit, bandit, lighthouse
No false positives - every finding must be reproducible
Provide remediation code, not just descriptions
When relevant, map findings to ISO/IEC 25010 quality characteristics and propose ISO/IEC 29119-aligned test improvements
How to Execute

Follow resources/execution-protocol.md step by step. See resources/examples.md for input/output examples. Use resources/iso-quality.md when the user needs enterprise QA, audit readiness, or standards-based recommendations. Before submitting, run resources/self-check.md.

Execution Protocol (CLI Mode)

See ../_shared/execution-protocols/ for vendor-specific protocols. When spawned via oh-my-ag agent:spawn, the protocol is injected automatically.

References
Execution steps: resources/execution-protocol.md
Report examples: resources/examples.md
ISO quality guide: resources/iso-quality.md
QA checklist: resources/checklist.md
Self-check: resources/self-check.md
Error recovery: resources/error-playbook.md
Context loading: ../_shared/context-loading.md
Context budget: ../_shared/context-budget.md
Lessons learned: ../_shared/lessons-learned.md
Weekly Installs
43
Repository
first-fluke/oh-my-ag
GitHub Stars
874
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass