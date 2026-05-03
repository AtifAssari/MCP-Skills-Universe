---
rating: ⭐⭐⭐
title: deploy-checklist
url: https://skills.sh/anthropics/knowledge-work-plugins/deploy-checklist
---

# deploy-checklist

skills/anthropics/knowledge-work-plugins/deploy-checklist
deploy-checklist
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill deploy-checklist
SKILL.md
/deploy-checklist

If you see unfamiliar placeholders or need to check which tools are connected, see CONNECTORS.md.

Generate a pre-deployment checklist to verify readiness before shipping.

Usage
/deploy-checklist $ARGUMENTS

Output
## Deploy Checklist: [Service/Release]
**Date:** [Date] | **Deployer:** [Name]

### Pre-Deploy
- [ ] All tests passing in CI
- [ ] Code reviewed and approved
- [ ] No known critical bugs in release
- [ ] Database migrations tested (if applicable)
- [ ] Feature flags configured (if applicable)
- [ ] Rollback plan documented
- [ ] On-call team notified

### Deploy
- [ ] Deploy to staging and verify
- [ ] Run smoke tests
- [ ] Deploy to production (canary if available)
- [ ] Monitor error rates and latency for 15 min
- [ ] Verify key user flows

### Post-Deploy
- [ ] Confirm metrics are nominal
- [ ] Update release notes / changelog
- [ ] Notify stakeholders
- [ ] Close related tickets

### Rollback Triggers
- Error rate exceeds [X]%
- P50 latency exceeds [X]ms
- [Critical user flow] fails

Customization

Tell me about your deploy and I'll customize the checklist:

"We use feature flags" → adds flag verification steps
"This includes a database migration" → adds migration-specific checks
"This is a breaking API change" → adds consumer notification steps
If Connectors Available

If ~~source control is connected:

Pull the release diff and list of changes
Verify all PRs are approved and merged

If ~~CI/CD is connected:

Check build and test status automatically
Verify pipeline is green before deploy

If ~~monitoring is connected:

Pre-fill rollback trigger thresholds from current baselines
Set up post-deploy metric watch
Tips
Run before every deploy — Even routine ones. Checklists prevent "I forgot to..."
Customize once, reuse — Tell me your stack and I'll remember your deploy process.
Include rollback criteria — Decide when to roll back before you deploy, not during.
Weekly Installs
1.6K
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass