---
title: log-stripe-issues
url: https://skills.sh/phrazzld/claude-config/log-stripe-issues
---

# log-stripe-issues

skills/phrazzld/claude-config/log-stripe-issues
log-stripe-issues
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill log-stripe-issues
SKILL.md
/log-stripe-issues

Run Stripe integration audit and create GitHub issues for all findings.

What This Does
Invoke /check-stripe to audit Stripe integration
Parse findings by priority (P0-P3)
Check existing issues to avoid duplicates
Create GitHub issues for each finding

This is an issue-creator. It creates work items, not fixes. Use /fix-stripe to fix issues.

Process
1. Run Primitive

Invoke /check-stripe skill to get structured findings.

2. Check Existing Issues
gh issue list --state open --label "domain/stripe" --limit 50

3. Create Issues

For each finding:

gh issue create \
  --title "[P0] Webhook signature not verified" \
  --body "$(cat <<'EOF'
## Problem
Stripe webhook endpoint does not verify signatures. Security vulnerability.

## Impact
- Attackers can forge webhook events
- Fake payment confirmations possible
- Customer data manipulation risk
- PCI compliance violation

## Location
`app/api/webhooks/stripe/route.ts`

## Suggested Fix
Run `/fix-stripe` or manually add:
```typescript
const event = stripe.webhooks.constructEvent(
  body,
  signature,
  process.env.STRIPE_WEBHOOK_SECRET!
);


Created by /log-stripe-issues EOF )"
--label "priority/p0,domain/stripe,type/bug"


### 4. Issue Format

**Title:** `[P{0-3}] Stripe issue description`

**Labels:**
- `priority/p0` | `priority/p1` | `priority/p2` | `priority/p3`
- `domain/stripe`
- `type/bug` | `type/enhancement` | `type/chore`

**Body:**
```markdown
## Problem
What's wrong with Stripe integration

## Impact
Business/security/user impact

## Location
File:line if applicable

## Suggested Fix
Code snippet or skill to run

---
Created by `/log-stripe-issues`

Priority Mapping
Gap	Priority
Missing webhook secret	P0
Hardcoded keys	P0
Webhook verification missing	P1
No customer portal	P1
Subscription status not checked	P1
No idempotency keys	P2
Poor error handling	P2
CLI profile issues	P2
Advanced features	P3
Output

After running:

Stripe Issues Created:
- P0: 1 (webhook verification)
- P1: 3 (portal, subscription checks)
- P2: 2 (idempotency, error handling)
- P3: 2 (advanced features)

Total: 8 issues created
View: gh issue list --label domain/stripe

Related
/check-stripe - The primitive (audit only)
/fix-stripe - Fix Stripe issues
/stripe - Full Stripe lifecycle
/stripe-health - Webhook diagnostics
/groom - Full backlog grooming
Weekly Installs
24
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