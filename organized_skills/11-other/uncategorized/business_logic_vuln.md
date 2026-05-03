---
rating: ⭐⭐
title: business-logic-vuln
url: https://skills.sh/yaklang/hack-skills/business-logic-vuln
---

# business-logic-vuln

skills/yaklang/hack-skills/business-logic-vuln
business-logic-vuln
Installation
$ npx skills add https://github.com/yaklang/hack-skills --skill business-logic-vuln
SKILL.md
Business Logic Router

This is the routing entry point for business-logic and state-machine issues.

When to Use
The target involves coupons, inventory, payment, approvals, quotas, invites, trials, or state transitions
The issue is not parser-level; it is about when checks happen and which business conditions are checked
You suspect race conditions, workflow bypass, price tampering, negative values, stacked discounts, or multi-step flaws
Skill Map
Business Logic Vulnerabilities
Recommended Flow
First map key business states and one-time actions
Then check for check-then-act windows, sequence dependencies, or missing cross-step authorization
If the chain depends on APIs, uploads, or object permissions, return to the corresponding router skill to complete the path
Related Categories
api-sec
auth-sec
file-access-vuln
Weekly Installs
326
Repository
yaklang/hack-skills
GitHub Stars
368
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass