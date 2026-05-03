---
rating: ⭐⭐⭐
title: runbook
url: https://skills.sh/anthropics/knowledge-work-plugins/runbook
---

# runbook

skills/anthropics/knowledge-work-plugins/runbook
runbook
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill runbook
SKILL.md
/runbook

If you see unfamiliar placeholders or need to check which tools are connected, see CONNECTORS.md.

Create a step-by-step operational runbook for a recurring task or procedure.

Usage
/runbook $ARGUMENTS

Output
## Runbook: [Task Name]
**Owner:** [Team/Person] | **Frequency:** [Daily/Weekly/Monthly/As Needed]
**Last Updated:** [Date] | **Last Run:** [Date]

### Purpose
[What this runbook accomplishes and when to use it]

### Prerequisites
- [ ] [Access or permission needed]
- [ ] [Tool or system required]
- [ ] [Data or input needed]

### Procedure

#### Step 1: [Name]


[Exact command, action, or instruction]

**Expected result:** [What should happen]
**If it fails:** [What to do]

#### Step 2: [Name]


[Exact command, action, or instruction]

**Expected result:** [What should happen]
**If it fails:** [What to do]

### Verification
- [ ] [How to confirm the task completed successfully]
- [ ] [What to check]

### Troubleshooting
| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| [What you see] | [Why] | [What to do] |

### Rollback
[How to undo this if something goes wrong]

### Escalation
| Situation | Contact | Method |
|-----------|---------|--------|
| [When to escalate] | [Who] | [How to reach them] |

### History
| Date | Run By | Notes |
|------|--------|-------|
| [Date] | [Person] | [Any issues or observations] |

If Connectors Available

If ~~knowledge base is connected:

Search for existing runbooks to update rather than create from scratch
Publish the completed runbook to your ops wiki

If ~~ITSM is connected:

Link the runbook to related incident types and change requests
Auto-populate escalation contacts from on-call schedules
Tips
Be painfully specific — "Run the script" is not a step. "Run python sync.py --prod --dry-run from the ops server" is.
Include failure modes — What can go wrong at each step and what to do about it.
Test the runbook — Have someone unfamiliar with the process follow it. Fix where they get stuck.
Weekly Installs
826
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass