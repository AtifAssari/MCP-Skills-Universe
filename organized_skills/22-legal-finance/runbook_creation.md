---
rating: ⭐⭐⭐⭐⭐
title: runbook-creation
url: https://skills.sh/aj-geddes/useful-ai-prompts/runbook-creation
---

# runbook-creation

skills/aj-geddes/useful-ai-prompts/runbook-creation
runbook-creation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill runbook-creation
SKILL.md
Runbook Creation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create comprehensive operational runbooks that provide step-by-step procedures for common operational tasks, incident response, and system maintenance.

When to Use
Incident response procedures
Standard operating procedures (SOPs)
On-call playbooks
System maintenance guides
Disaster recovery procedures
Deployment runbooks
Escalation procedures
Service restoration guides
Quick Start

Minimal working example:

# Incident Response Runbook

## Quick Reference

**Severity Levels:**

- P0 (Critical): Complete outage, data loss, security breach
- P1 (High): Major feature down, significant user impact
- P2 (Medium): Minor feature degradation, limited user impact
- P3 (Low): Cosmetic issues, minimal user impact

**Response Times:**

- P0: Immediate (24/7)
- P1: 15 minutes (business hours), 1 hour (after hours)
- P2: 4 hours (business hours)
- P3: Next business day

**Escalation Contacts:**

- On-call Engineer: PagerDuty rotation
- Engineering Manager: +1-555-0100
- VP Engineering: +1-555-0101
- CTO: +1-555-0102

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Symptoms](references/symptoms.md) | Symptoms, Severity: P0 (Critical), Initial Response (5 minutes) |
| [Investigation Steps](references/investigation-steps.md) | Investigation Steps |
| [Resolution Steps](references/resolution-steps.md) | Resolution Steps |
| [Verification](references/verification.md) | Verification |
| [Communication](references/communication.md) | Communication |
| [Post-Incident](references/post-incident.md) | Post-Incident |

## Best Practices

### ✅ DO

- Include quick reference section at top
- Provide exact commands to run
- Document expected outputs
- Include verification steps
- Add communication templates
- Define severity levels clearly
- Document escalation paths
- Include useful links and contacts
- Keep runbooks up-to-date
- Test runbooks regularly
- Include screenshots/diagrams
- Document common gotchas

### ❌ DON'T

- Use vague instructions
- Skip verification steps
- Forget to document prerequisites
- Assume knowledge of tools
- Skip communication guidelines
- Forget to update after incidents

Weekly Installs
276
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass