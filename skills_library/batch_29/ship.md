---
title: ship
url: https://skills.sh/open-horizon-labs/skills/ship
---

# ship

skills/open-horizon-labs/skills/ship
ship
Installation
$ npx skills add https://github.com/open-horizon-labs/skills --skill ship
SKILL.md
/ship

Optimize the delivery path from completed work to working install. When execution is cheap, delivery is the work.

Ship is the final step of the Execution phase. Code that isn't in users' hands isn't delivering value.

When to Use

Invoke /ship when execution is complete, tests pass, review is done, and you need to get changes to users. Also usable as a standalone diagnostic: run /ship against a stalled delivery pipeline to surface delivery-path tax without deploying anything.

Do not use when: You're still building. Ship is for completed work.

The Ship Process
Step 1: Identify the Delivery Path

Map the path from code to working install:

"The delivery path for this change is: [local] → [PR/review] → [merge] → [CI/CD] → [staging/prod] → [user install]."

Be specific. Name each step and who/what owns it.

Step 2: Assess the Delivery-Path Tax

The delivery-path tax is friction that slows velocity. Identify where time is lost across: review queue, merge conflicts/stability, gate/scan time (serial vs parallel, flaky), approval bottlenecks, deploy duration, rollback readiness, and manual steps.

Step 3: Execute the Ship
With CI/CD Context
Reference the pipeline — point to the specific build/deploy configuration
Trigger the appropriate workflow — label PRs, push to deploy branches, etc.
Monitor the pipeline — watch for failures, report status
Verify deployment — confirm the change is live
Without CI/CD Context
List deployment steps — what needs to happen in order
Execute each step — or provide commands to execute
Verify each stage — confirm success before proceeding
Report final status — confirm user-facing change is live
Step 4: Post-Ship Verification

Shipping isn't done until you verify:

Is it running? — deployed and executing
Is it working? — intended behavior is present
Is it reachable? — users can access/use it
Were the promised characteristics delivered? — shipped result matches the declared success criteria from /execute

Create ad-hoc verification tests if needed — the point is confidence, not permanent infrastructure. Verification ties back to what the work claimed it would deliver, not only whether deployment completed.

Output Format
## Ship Report

**Shipped:** [what was shipped]
**Target:** [where it was shipped to]
**Path:** [the delivery path taken]

### Delivery-Path Tax Identified
- [Friction point 1]: [time/effort cost]
- [Friction point 2]: [time/effort cost]

### Ship Actions Taken
1. [Action 1 - result]
2. [Action 2 - result]

### Verification
- [x] Deployed successfully
- [x] Running in target environment
- [x] User-facing functionality confirmed

### Delivered Characteristics Validation
- [x] [Declared criterion/characteristic 1]
- [ ] [Declared criterion/characteristic 2, if not yet verified]

### Recommendations
[Any suggestions for reducing delivery-path tax in future]

Session Persistence

Reads: Aim, Solution Space, Execute status — including declared success criteria and deliverable characteristics.

Writes: Deployment status and delivered-characteristics validation:

## Ship
**Updated:** <timestamp>
**Status:** [staged | deployed | verified | rolled-back]

[shipping notes, verification results, delivered-characteristics validation]

Position in Framework

Comes after: /execute (the work is done, now deliver it). Leads to: /review (did the shipped change achieve the aim?), then back to /aim. This is the end of the line: Ship is where code becomes value.

Key Vocabulary
Delivery Path: The journey from merged code to working install
Delivery-Path Tax: Friction that slows delivery (review time, merge time, gate time, approval time)
Working Install: The code is running and users can interact with it
Weekly Installs
78
Repository
open-horizon-labs/skills
GitHub Stars
1
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass