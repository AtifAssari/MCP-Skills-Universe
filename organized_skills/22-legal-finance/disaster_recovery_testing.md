---
rating: ⭐⭐⭐
title: disaster-recovery-testing
url: https://skills.sh/aj-geddes/useful-ai-prompts/disaster-recovery-testing
---

# disaster-recovery-testing

skills/aj-geddes/useful-ai-prompts/disaster-recovery-testing
disaster-recovery-testing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill disaster-recovery-testing
SKILL.md
Disaster Recovery Testing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement systematic disaster recovery testing to validate recovery procedures, measure RTO/RPO, identify gaps, and ensure team readiness for actual incidents.

When to Use
Annual DR exercises
Infrastructure changes
New service deployments
Compliance requirements
Team training
Recovery procedure validation
Cross-region failover testing
Quick Start

Minimal working example:

# dr-test-plan.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: dr-test-procedures
  namespace: operations
data:
  dr-test-plan.md: |
    # Disaster Recovery Test Plan

    ## Test Objectives
    - Validate backup restoration procedures
    - Verify failover mechanisms
    - Test DNS failover
    - Validate data integrity post-recovery
    - Measure RTO and RPO
    - Train incident response team

    ## Pre-Test Checklist
    - [ ] Notify stakeholders
    - [ ] Schedule 4-6 hour window
    - [ ] Disable alerting to prevent noise
    - [ ] Backup production data
    - [ ] Ensure DR environment is isolated
    - [ ] Have rollback plan ready
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
DR Test Plan and Execution	DR Test Plan and Execution
DR Test Script	DR Test Script
DR Test Automation	DR Test Automation
Best Practices
✅ DO
Schedule regular DR tests
Document procedures in advance
Test in isolated environments
Measure actual RTO/RPO
Involve all teams
Automate validation
Record findings
Update procedures based on results
❌ DON'T
Skip DR testing
Test during business hours
Test against production
Ignore test failures
Neglect post-test analysis
Forget to re-enable monitoring
Use stale backup processes
Test only once a year
Weekly Installs
265
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail