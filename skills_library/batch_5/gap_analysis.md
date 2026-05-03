---
title: gap-analysis
url: https://skills.sh/aj-geddes/useful-ai-prompts/gap-analysis
---

# gap-analysis

skills/aj-geddes/useful-ai-prompts/gap-analysis
gap-analysis
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill gap-analysis
SKILL.md
Gap Analysis
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Gap analysis systematically compares current capabilities with desired future state, revealing what needs to change and what investments are required.

When to Use
Strategic planning and goal setting
Technology modernization assessment
Process improvement initiatives
Skills and training planning
System evaluation and selection
Organizational change planning
Capability building programs
Quick Start

Minimal working example:

# Systematic gap identification

class GapAnalysis:
    GAP_CATEGORIES = {
        'Business Capability': 'Functions organization can perform',
        'Process': 'How work gets done',
        'Technology': 'Tools and systems available',
        'Skills': 'Knowledge and expertise',
        'Data': 'Information available',
        'People/Culture': 'Team composition and mindset',
        'Organization': 'Structure and roles',
        'Metrics': 'Ability to measure performance'
    }

    def identify_gaps(self, current_state, future_state):
        """Compare current vs desired and find gaps"""
        gaps = []

        for capability in future_state['capabilities']:
            current_capability = self.find_capability(
                capability['name'],
                current_state['capabilities']
            )

            if current_capability is None:
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Gap Identification Framework	Gap Identification Framework
Gap Analysis Template	Gap Analysis Template
Gap Closure Planning	Gap Closure Planning
Communication & Tracking	Communication & Tracking
Best Practices
✅ DO
Compare current to clearly defined future state
Include all relevant capability areas
Involve stakeholders in gap identification
Prioritize by value and effort
Create detailed closure plans
Track progress to closure
Document gap analysis findings
Review and update analysis quarterly
Link gaps to business strategy
Communicate findings transparently
❌ DON'T
Skip current state assessment
Create vague future state
Identify gaps without solutions
Ignore implementation effort
Plan all gaps in parallel
Forget about dependencies
Ignore resource constraints
Hide difficult findings
Plan for 100% effort allocation
Forget about change management
Weekly Installs
287
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass