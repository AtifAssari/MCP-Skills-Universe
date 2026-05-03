---
rating: ⭐⭐⭐⭐⭐
title: log-onboarding-issues
url: https://skills.sh/phrazzld/claude-config/log-onboarding-issues
---

# log-onboarding-issues

skills/phrazzld/claude-config/log-onboarding-issues
log-onboarding-issues
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill log-onboarding-issues
SKILL.md
/log-onboarding-issues

Run onboarding audit and create GitHub issues for all findings.

What This Does
Invoke /check-onboarding to audit new user experience
Parse findings by priority (P0-P3)
Check existing issues to avoid duplicates
Create GitHub issues for each finding

This is an issue-creator. It creates work items, not fixes. Use /fix-onboarding to fix issues.

Process
1. Run Primitive

Invoke /check-onboarding skill to get structured findings.

2. Check Existing Issues
gh issue list --state open --label "domain/onboarding" --limit 50

3. Create Issues

For each finding:

gh issue create \
  --title "[P0] No onboarding flow - users dropped into empty app" \
  --body "$(cat <<'EOF'
## Problem
After signup, users land on an empty dashboard with no guidance. They don't know what to do first.

## Impact
- High drop-off after signup
- Users never experience core value
- Support tickets asking "how do I start?"
- Lost users who never return

## Suggested Fix
Run `/fix-onboarding` or implement:

1. **First-run detection:**
```typescript
const isNewUser = !user.hasCompletedOnboarding;
if (isNewUser) redirect('/onboarding');

Onboarding wizard:
Welcome screen
First action prompt
Success celebration
Empty state with CTA: "Create your first X to get started"

Created by /log-onboarding-issues EOF )"
--label "priority/p0,domain/onboarding,type/enhancement"


### 4. Issue Format

**Title:** `[P{0-3}] Onboarding issue`

**Labels:**
- `priority/p0` | `priority/p1` | `priority/p2` | `priority/p3`
- `domain/onboarding`
- `type/enhancement` | `type/bug`

**Body:**
```markdown
## Problem
What's broken in new user experience

## Impact
Effect on activation and retention

## Suggested Fix
Code snippet, pattern, or skill to run

---
Created by `/log-onboarding-issues`

Priority Mapping
Gap	Priority
No onboarding flow	P0
Broken auth callback	P0
Paywall before value	P0
No empty states	P1
No first-action guidance	P1
Complex initial forms	P1
No loading states	P1
No progressive disclosure	P2
No tooltips/hints	P2
No tour option	P2
Retention hooks missing	P3
Output

After running:

Onboarding Issues Created:
- P0: 1 (no onboarding flow)
- P1: 4 (empty states, guidance, forms)
- P2: 3 (progressive disclosure, hints)
- P3: 2 (notifications, email capture)

Total: 10 issues created
View: gh issue list --label domain/onboarding

Related
/check-onboarding - The primitive (audit only)
/fix-onboarding - Fix onboarding issues
/cro - Conversion optimization
/groom - Full backlog grooming
Weekly Installs
25
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