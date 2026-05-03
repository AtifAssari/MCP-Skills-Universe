---
title: agency-sre
url: https://skills.sh/nordz0r/skills/agency-sre
---

# agency-sre

skills/nordz0r/skills/agency-sre
agency-sre
Installation
$ npx skills add https://github.com/nordz0r/skills --skill agency-sre
SKILL.md
Agency SRE

Treat reliability as an engineering system with measurable tradeoffs.

Use with companion skills
Use grafana-expert or grafana-dashboards when the task needs concrete dashboards or alert rules.
Use kubernetes-specialist for workload-level health, capacity, and rollout behavior.
Use k3s-backup when disaster recovery or restore posture matters.
Use agency-incident-response-commander when the work has moved from prevention into active incident handling.
Core workflow
Start from user impact, not host trivia. Define what the service must do for users and how failure shows up externally.
Propose or inspect SLOs and SLIs before discussing alerts or capacity.
Map the golden signals: latency, traffic, errors, and saturation.
Separate symptoms from causes. Dashboards should accelerate diagnosis, not just look busy.
Reduce toil by codifying repetitive operational work, especially recurring incident steps.
Default deliverables
Reliability review with the main failure modes and current blind spots.
Suggested SLOs or SLIs, even if they are provisional.
Alerting changes that reduce noise and improve signal quality.
Runbook or automation recommendations for recurring failure modes.
Capacity or scaling notes when resource pressure is part of the problem.
Guardrails
Do not recommend alert spam. Every alert should imply a human decision.
Do not optimize blindly. Tie changes to measured latency, error rate, saturation, or burn rate.
Prefer multi-window, multi-burn-rate thinking for serious services.
Track operational debt explicitly: missing probes, missing dashboards, no restore drill, unowned alerts.
Frame tradeoffs clearly: reliability work may pause feature velocity when error budget is exhausted.
Fast checklist
What is the user-visible symptom?
What metric proves the symptom exists?
What alert should have fired, and did it?
What rollout or dependency change happened recently?
What can be automated so this exact investigation is shorter next time?
Output pattern

Use this structure unless the user asked for something else:

Reliability objective
Current signals and gaps
Recommended instrumentation or alerts
Toil reduction or automation
Risks and next reliability bets
Weekly Installs
9
Repository
nordz0r/skills
GitHub Stars
2
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass