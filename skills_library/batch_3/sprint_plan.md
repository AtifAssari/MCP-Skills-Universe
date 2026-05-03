---
title: sprint-plan
url: https://skills.sh/phuryn/pm-skills/sprint-plan
---

# sprint-plan

skills/phuryn/pm-skills/sprint-plan
sprint-plan
Installation
$ npx skills add https://github.com/phuryn/pm-skills --skill sprint-plan
SKILL.md
Sprint Planning

Plan a sprint by estimating team capacity, selecting and sequencing stories, and identifying risks.

Context

You are helping plan a sprint for $ARGUMENTS.

If the user provides files (backlogs, velocity data, team rosters, or previous sprint reports), read them first.

Instructions

Estimate team capacity:

Number of team members and their availability (PTO, meetings, on-call)
Historical velocity (average story points per sprint from last 3 sprints)
Capacity buffer: reserve 15-20% for unexpected work, bugs, and tech debt
Calculate available capacity in story points or ideal hours

Review and select stories:

Pull from the prioritized backlog (highest priority first)
Verify each story meets the Definition of Ready (clear AC, estimated, no blockers)
Flag stories that need refinement before committing
Stop adding stories when capacity is reached

Map dependencies:

Identify stories that depend on other stories or external teams
Sequence dependent stories appropriately
Flag external dependencies and owners
Identify the critical path

Identify risks and mitigations:

Stories with high uncertainty or complexity
External dependencies that could slip
Knowledge concentration (only one person can do it)
Suggest mitigations for each risk

Create the sprint plan summary:

Sprint Goal: [One sentence describing what success looks like]
Duration: [2 weeks / 1 week / etc.]
Team Capacity: [X story points]
Committed Stories: [Y story points across Z stories]
Buffer: [remaining capacity]

Stories:
1. [Story title] — [points] — [owner] — [dependencies]
...

Risks:
- [Risk] → [Mitigation]


Define the sprint goal: A single, clear sentence that captures the sprint's primary value delivery.

Think step by step. Save as markdown.

Further Reading
Product Owner vs Product Manager: What's the difference?
Weekly Installs
555
Repository
phuryn/pm-skills
GitHub Stars
10.8K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass