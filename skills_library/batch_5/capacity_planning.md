---
title: capacity-planning
url: https://skills.sh/aj-geddes/useful-ai-prompts/capacity-planning
---

# capacity-planning

skills/aj-geddes/useful-ai-prompts/capacity-planning
capacity-planning
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill capacity-planning
SKILL.md
Capacity Planning
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Capacity planning ensures teams have sufficient resources to deliver work at sustainable pace, prevents burnout, and enables accurate commitment to stakeholders.

When to Use
Annual or quarterly planning cycles
Allocating people to projects
Adjusting team size
Planning for holidays and absences
Forecasting resource needs
Balancing multiple projects
Identifying bottlenecks
Quick Start

Minimal working example:

# Team capacity calculation and planning

class CapacityPlanner:
    # Standard work hours per week
    STANDARD_WEEK_HOURS = 40

    # Activities that reduce available capacity
    OVERHEAD_HOURS = {
        'meetings': 5,           # standups, 1-on-1s, planning
        'training': 2,           # learning new tech
        'administrative': 2,     # emails, approvals
        'support': 2,            # helping teammates
        'contingency': 2         # interruptions, emergencies
    }

    def __init__(self, team_size, sprint_duration_weeks=2):
        self.team_size = team_size
        self.sprint_duration_weeks = sprint_duration_weeks
        self.members = []

    def calculate_team_capacity(self):
        """Calculate available capacity hours"""
        # Base capacity
        base_hours = self.team_size * self.STANDARD_WEEK_HOURS * self.sprint_duration_weeks

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Capacity Assessment	Capacity Assessment
Capacity Planning Template	Capacity Planning Template
Resource Leveling	Resource Leveling
Capacity Forecasting	Capacity Forecasting
Best Practices
✅ DO
Plan capacity at 85% utilization (15% buffer)
Account for meetings, training, and overhead
Include known absences (vacation, holidays)
Identify skill bottlenecks early
Balance workload fairly across team
Review capacity monthly
Adjust plans based on actual velocity
Cross-train on critical skills
Communicate realistic commitments to stakeholders
Build contingency for emergencies
❌ DON'T
Plan at 100% utilization
Ignore meetings and overhead
Assign work without checking skills
Create overload with continuous surprises
Forget about learning/training time
Leave capacity planning to last minute
Overcommit team consistently
Burn out key people
Ignore team feedback on workload
Plan without considering absences
Weekly Installs
271
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass