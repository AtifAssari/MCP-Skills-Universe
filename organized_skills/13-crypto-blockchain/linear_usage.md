---
rating: ⭐⭐⭐
title: linear-usage
url: https://skills.sh/fcakyon/claude-codex-settings/linear-usage
---

# linear-usage

skills/fcakyon/claude-codex-settings/linear-usage
linear-usage
Installation
$ npx skills add https://github.com/fcakyon/claude-codex-settings --skill linear-usage
SKILL.md
Linear & Issue Tracking Best Practices
Issue Writing Guidelines
Clear Titles

Write titles that describe the problem or outcome:

Good: "Users can't reset password on mobile Safari"
Bad: "Password bug"
Good: "Add export to CSV for user reports"
Bad: "Export feature"
Effective Descriptions

Include:

Context: Why this matters
Current behavior: What happens now (for bugs)
Expected behavior: What should happen
Steps to reproduce: For bugs
Acceptance criteria: Definition of done
Templates

Bug report:

## Description
Brief description of the issue.

## Steps to Reproduce
1. Step one
2. Step two
3. Issue occurs

## Expected Behavior
What should happen.

## Actual Behavior
What happens instead.

## Environment
- Browser/OS
- User type


Feature request:

## Problem Statement
What problem does this solve?

## Proposed Solution
High-level approach.

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

Label Taxonomy
Recommended Labels

Type labels:

bug - Something isn't working
feature - New functionality
improvement - Enhancement to existing feature
chore - Maintenance, refactoring

Area labels:

frontend, backend, api, mobile
Or by feature area: auth, payments, onboarding

Status labels (if not using workflow states):

needs-triage, blocked, needs-design
Label Best Practices
Keep label count manageable (15-25 total)
Use consistent naming convention
Color-code by category
Review and prune quarterly
Priority and Estimation
Priority Levels
Urgent (P0): Production down, security issue
High (P1): Major functionality broken, key deadline
Medium (P2): Important but not urgent
Low (P3): Nice to have, minor improvements
Estimation Tips
Use relative sizing (points) not hours
Estimate complexity, not time
Include testing and review time
Re-estimate if scope changes significantly
Cycle/Sprint Planning
Cycle Best Practices
Duration: 1-2 weeks typically
Capacity: Plan for 70-80% to allow for interrupts
Carryover: Review why items didn't complete
Retrospective: Brief review at cycle end
Planning Process
Review backlog priorities
Pull issues into cycle
Break down large items (>5 points)
Assign owners
Identify dependencies and blockers
Project Organization
Projects vs Initiatives

Projects: Focused, time-bound work (1-3 months)

Single team typically
Clear deliverable
Example: "Mobile app v2 launch"

Initiatives: Strategic themes

May span multiple projects
Longer-term goals
Example: "Platform reliability"
Roadmap Tips
Keep roadmap items high-level
Update status regularly
Link to detailed issues/projects
Share with stakeholders
Triage Workflows
Triage Process
Review new issues daily
Add missing information (labels, priority)
Assign to appropriate team/person
Link related issues
Move to backlog or close if invalid
Closing Issues

Close with clear reason:

Completed: Work is done
Duplicate: Link to original
Won't fix: Explain why
Invalid: Missing info, not reproducible
GitHub Integration
Linking PRs to Issues
Reference Linear issue ID in PR title or description
Linear auto-links and updates status
Use branch names with issue ID for automatic linking
Workflow Automation
PR opened → Issue moves to "In Progress"
PR merged → Issue moves to "Done"
Configure in Linear settings
Weekly Installs
37
Repository
fcakyon/claude-…settings
GitHub Stars
657
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass