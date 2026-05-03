---
title: log-production-issues
url: https://skills.sh/phrazzld/claude-config/log-production-issues
---

# log-production-issues

skills/phrazzld/claude-config/log-production-issues
log-production-issues
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill log-production-issues
SKILL.md
/log-production-issues

Run production health audit and create GitHub issues for all findings.

What This Does
Invoke /check-production to audit production health
Parse findings by priority (P0-P3)
Check existing issues to avoid duplicates
Create GitHub issues for each finding

This is an issue-creator. It creates work items, not fixes. Use /triage to fix issues.

Process
1. Run Primitive

Invoke /check-production skill to get structured findings.

2. Check Existing Issues
gh issue list --state open --label "domain/production" --limit 50

3. Create Issues

For each finding, create a GitHub issue:

gh issue create \
  --title "[P0] PaymentIntent failed - 23 users affected" \
  --body "$(cat <<'EOF'
## Problem
Sentry issue SENTRY-123 shows PaymentIntent failures affecting 23 users.

## Impact
- Users cannot complete checkout
- Revenue loss estimated at $X/hour
- First seen: 2 hours ago

## Location
`api/checkout.ts:45`

## Suggested Fix
Run `/triage investigate SENTRY-123` to diagnose and fix.

## Source
- Sentry: SENTRY-123
- Score: 147

---
Created by `/log-production-issues`
EOF
)" \
  --label "priority/p0,domain/production,type/bug"

4. Issue Format

All issues follow this structure:

Title: [P{0-3}] Concise problem statement

Labels:

priority/p0 | priority/p1 | priority/p2 | priority/p3
domain/production
type/bug | type/enhancement | type/chore

Body:

## Problem
What's wrong (specific, measurable)

## Impact
Who/what is affected, severity

## Location
File:line or service/component

## Suggested Fix
Skill to run or action to take

## Source
Where this was detected (Sentry ID, log line, etc.)

---
Created by `/log-production-issues`

Deduplication

Before creating an issue:

Search for existing issues with same Sentry ID or similar title
If found: Update existing issue with new occurrence count
If not found: Create new issue
# Check for existing
gh issue list --state open --search "SENTRY-123" --limit 5

Priority Mapping
Source	Priority
Active Sentry errors (>5 users)	P0
5xx errors in Vercel logs	P1
Slow health endpoint	P1
Silent failures (empty catch)	P2
Missing monitoring	P3
Output

After running:

Production Issues Created:
- P0: 1 (payment failures)
- P1: 2 (5xx errors, slow health)
- P2: 2 (silent failures)
- P3: 1 (missing monitoring)

Total: 6 issues created
View: gh issue list --label domain/production

Related
/check-production - The primitive (audit only)
/triage - Fix production issues
/groom - Full backlog grooming (runs this skill)
Weekly Installs
23
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass