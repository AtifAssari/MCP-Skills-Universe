---
title: agency-incident-response-commander
url: https://skills.sh/nordz0r/skills/agency-incident-response-commander
---

# agency-incident-response-commander

skills/nordz0r/skills/agency-incident-response-commander
agency-incident-response-commander
Installation
$ npx skills add https://github.com/nordz0r/skills --skill agency-incident-response-commander
SKILL.md
Agency Incident Response Commander

Turn ambiguous production chaos into structured response.

Use with companion skills
Use agency-sre for SLO framing, observability gaps, and follow-up reliability work.
Use agency-devops-automator when the safest mitigation is a controlled rollback or pipeline intervention.
Use kubernetes-specialist, administering-linux, and ssh for the concrete technical recovery actions.
Incident workflow
Establish impact first: affected users, affected features, start time, and current blast radius.
Assign severity deliberately. Do not skip triage language such as SEV1, SEV2, or equivalent internal labels.
Stabilize before deep root-cause analysis. Roll back, fail over, disable a feature flag, or isolate the broken dependency if that reduces impact fastest.
Maintain a live timeline: observations, actions, timestamps, and outcomes.
Separate facts, hypotheses, and decisions. Do not present guesses as confirmed root cause.
Exit the incident with explicit follow-ups, owners, and deadlines.
Default deliverables
Current incident summary in one screenful.
Severity assessment with rationale.
Immediate mitigation options ranked by speed and risk.
Stakeholder update text for engineering and non-engineering audiences.
Postmortem skeleton: timeline, impact, root causes, contributing factors, corrective actions.
Guardrails
Bias toward service restoration over elegant debugging during active impact.
Communicate at fixed intervals, even if the update is "no material change."
Be blameless. Focus on systemic gaps: missing alert, unsafe deploy path, absent guardrail, hidden dependency.
Timebox dead-end investigations. If an approach is not proving out, pivot.
Always capture the recovery path that worked. It becomes the next runbook revision.
Severity cues
SEV1: broad outage, data loss risk, or major customer impact.
SEV2: major degradation, partial outage, important feature unavailable.
SEV3: contained issue with workaround or limited blast radius.
SEV4: low urgency defect or operational debt item.
Output pattern

Use this structure unless the user asked for something else:

Incident status
Impact and severity
Mitigation plan
Timeline
Follow-up actions
Weekly Installs
8
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