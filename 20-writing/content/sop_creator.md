---
title: sop-creator
url: https://skills.sh/coleam00/second-brain-skills/sop-creator
---

# sop-creator

skills/coleam00/second-brain-skills/sop-creator
sop-creator
Installation
$ npx skills add https://github.com/coleam00/second-brain-skills --skill sop-creator
SKILL.md
SOP & Runbook Creator

Create practical documentation that people actually follow.

Philosophy

Nobody reads 50-page docs. Make it scannable, actionable, and impossible to misunderstand.

Core principles:

Scannable - Headers, bullets, tables. No walls of text.
Actionable - Every step is something you DO, not something you "consider"
Specific - Numbers, names, thresholds. No "as needed" or "when appropriate"
Testable - Clear success criteria. How do you know it worked?
Maintained - Owner, last updated, review schedule
SOP Categories

Pick the right format for your use case:

Tech/Engineering
Type	When to Use
Runbook	Emergency response, incidents, on-call
Deployment Playbook	Releases, migrations, maintenance
Troubleshooting Guide	Debugging, diagnosis trees
How-To Guide	One-off setup, configuration
ADR	Architecture decisions
Operations/Business
Type	When to Use
Process SOP	Repeatable business workflows
Checklist	Quality control, verification
Decision Tree	Complex if/then scenarios
Handoff Doc	Role transitions, shift changes
Content/Creative
Type	When to Use
Production Workflow	Content creation pipelines
Review Process	Approval workflows
Publishing Checklist	Pre-launch verification
General
Type	When to Use
Standard SOP	Any repeatable process
Quick Reference	Condensed version of longer SOP
Onboarding Guide	New person ramping up
Universal Structure

Every SOP needs at minimum:

# [What This Does]

> **TL;DR:** One sentence - what, when, who.

## Definition of Done

This is complete when:
- [ ] [Primary outcome]
- [ ] [Verification step]
- [ ] [Any handoff/notification]

## When to Use This
[Trigger conditions]

## Prerequisites
[What you need before starting]

## The Process
[Numbered steps - the actual work]

## Verify Completion
[Return to Definition of Done, confirm all checked]

## When Things Go Wrong
[Common issues and fixes]

## Questions?
[Who to contact]


Definition of Done is the most important section. Put it near the top. Make it a checklist. Be specific.

Writing Rules
Be Specific
Don't Write	Write Instead
"Contact the team"	"Message @sarah in #ops-team"
"Wait until ready"	"Wait until status shows 'Complete' (~5 min)"
"Review carefully"	"Check items A, B, C in the dashboard"
"As appropriate"	"If value > 100"
"Regularly"	"Every Monday at 9am"
"Soon"	"Within 2 hours"
Action-First Steps
# Bad
"The report should be reviewed before sending to ensure
accuracy and completeness of all data fields."

# Good
1. Open the report in [System]
2. Verify these fields are populated:
   - [ ] Customer name
   - [ ] Amount
   - [ ] Date
3. Click "Send"

Warnings Come First
# Bad
1. Delete the old records
   Note: This cannot be undone

# Good
> **WARNING:** This permanently deletes records. Export first if needed.

1. Delete the old records

Decision Points are Clear
# Bad
"Handle the request based on priority level"

# Good
**If priority is:**
- **Critical:** Drop everything, handle now, notify manager
- **High:** Handle within 4 hours
- **Normal:** Handle within 24 hours
- **Low:** Add to weekly batch

Format Selection Guide

Ask yourself:

Is this for emergencies? → Runbook
Is this a complex multi-phase project? → Playbook
Is this a simple repeated task? → Standard SOP or Checklist
Does it have lots of if/then branching? → Decision Tree
Is it for debugging? → Troubleshooting Guide
Is it recording a decision? → ADR
Is it for someone new? → Onboarding Guide
Metadata (Keep it Light)
---
title: [Clear name]
owner: [Person or team]
last_updated: [Date]
review_schedule: [quarterly/annually/as-needed]
---


That's it. No document IDs, version matrices, or approval chains unless you actually need them.

Templates

Each template is in references/:

Template	Use For
runbook.md	Incidents, emergencies, on-call
standard-sop.md	Any repeatable process
how-to-guide.md	One-off tasks, setup
onboarding-guide.md	New person ramping up
decision-tree.md	Complex if/then flows
checklist.md	QC, verification

All templates have Definition of Done as the primary success criteria.

Quality Checklist

Before publishing:

 Can someone unfamiliar follow this?
 Are all steps actionable (verbs, not descriptions)?
 Are specifics provided (names, numbers, thresholds)?
 Is there a clear "done" state?
 Is the owner/contact info current?
 Has it been tested recently?
Anti-Patterns

Kill these:

"Per company policy..." (just state what to do)
"It is recommended that..." (just say "do X")
"Please ensure..." (just say "check X")
Passive voice ("the form should be submitted" → "submit the form")
Describing what to do instead of showing it
Walls of text with no structure
Screenshots that will be outdated in a month

Do these:

Start with the most common path
Put edge cases at the bottom
Link to related docs instead of duplicating
Use tables for reference info
Use checklists for verification steps
Include "I'm stuck" escape hatches
Weekly Installs
55
Repository
coleam00/second…n-skills
GitHub Stars
706
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass