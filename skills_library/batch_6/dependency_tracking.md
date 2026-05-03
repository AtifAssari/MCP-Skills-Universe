---
title: dependency-tracking
url: https://skills.sh/aj-geddes/useful-ai-prompts/dependency-tracking
---

# dependency-tracking

skills/aj-geddes/useful-ai-prompts/dependency-tracking
dependency-tracking
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill dependency-tracking
SKILL.md
Dependency Tracking
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Dependency tracking ensures visibility of task relationships, identifies blocking issues early, and enables better resource planning and risk mitigation.

When to Use
Multi-team projects and programs
Complex technical integrations
Cross-organizational initiatives
Identifying critical path items
Resource allocation planning
Preventing schedule delays
Onboarding new team members
Quick Start

Minimal working example:

# Dependency mapping and tracking

class DependencyTracker:
    DEPENDENCY_TYPES = {
        'Finish-to-Start': 'Task B cannot start until Task A is complete',
        'Start-to-Start': 'Task B cannot start until Task A starts',
        'Finish-to-Finish': 'Task B cannot finish until Task A is complete',
        'Start-to-Finish': 'Task B cannot finish until Task A starts'
    }

    def __init__(self):
        self.tasks = []
        self.dependencies = []
        self.critical_path = []

    def create_dependency_map(self, tasks):
        """Create visual dependency network"""
        dependency_graph = {
            'nodes': [],
            'edges': [],
            'critical_items': []
        }

        for task in tasks:
            dependency_graph['nodes'].append({
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Dependency Mapping	Dependency Mapping
Dependency Management Board	Dependency Management Board
Dependency Resolution	Dependency Resolution
Dependency Dashboard Metrics	Dependency Dashboard Metrics
Best Practices
✅ DO
Map dependencies early in planning
Update dependency tracking weekly
Identify and monitor critical path items
Proactively communicate blockers
Have contingency plans for key dependencies
Break complex dependencies into smaller pieces
Track external dependencies separately
Escalate blocked critical path items immediately
Remove unnecessary dependencies
Build in buffer time for risky dependencies
❌ DON'T
Ignore external dependencies
Leave circular dependencies unresolved
Assume dependencies will "work out"
Skip daily monitoring of critical path
Communicate issues only in status meetings
Create too many dependencies (couples systems)
Forget to document dependency rationale
Avoid escalating blocked critical work
Plan at 100% utilization (no buffer for dependencies)
Treat all dependencies as equal priority
Weekly Installs
269
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