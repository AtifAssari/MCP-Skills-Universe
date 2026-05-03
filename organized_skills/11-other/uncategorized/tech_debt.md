---
rating: ⭐⭐
title: tech-debt
url: https://skills.sh/anthropics/knowledge-work-plugins/tech-debt
---

# tech-debt

skills/anthropics/knowledge-work-plugins/tech-debt
tech-debt
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill tech-debt
SKILL.md
Tech Debt Management

Systematically identify, categorize, and prioritize technical debt.

Categories
Type	Examples	Risk
Code debt	Duplicated logic, poor abstractions, magic numbers	Bugs, slow development
Architecture debt	Monolith that should be split, wrong data store	Scaling limits
Test debt	Low coverage, flaky tests, missing integration tests	Regressions ship
Dependency debt	Outdated libraries, unmaintained dependencies	Security vulns
Documentation debt	Missing runbooks, outdated READMEs, tribal knowledge	Onboarding pain
Infrastructure debt	Manual deploys, no monitoring, no IaC	Incidents, slow recovery
Prioritization Framework

Score each item on:

Impact: How much does it slow the team down? (1-5)
Risk: What happens if we don't fix it? (1-5)
Effort: How hard is the fix? (1-5, inverted — lower effort = higher priority)

Priority = (Impact + Risk) x (6 - Effort)

Output

Produce a prioritized list with estimated effort, business justification for each item, and a phased remediation plan that can be done alongside feature work.

Weekly Installs
2.0K
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass