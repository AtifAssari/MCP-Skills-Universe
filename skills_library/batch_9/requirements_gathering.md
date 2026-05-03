---
title: requirements-gathering
url: https://skills.sh/aj-geddes/useful-ai-prompts/requirements-gathering
---

# requirements-gathering

skills/aj-geddes/useful-ai-prompts/requirements-gathering
requirements-gathering
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill requirements-gathering
SKILL.md
Requirements Gathering
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Effective requirements gathering establishes a shared understanding of what will be built, preventing misalignment and expensive changes later in the project.

When to Use
Project kickoff and planning
Feature development initiation
Product roadmap planning
System modernization projects
Customer discovery
Stakeholder alignment sessions
Writing user stories and acceptance criteria
Quick Start

Minimal working example:

# Identify and analyze stakeholders

class StakeholderDiscovery:
    STAKEHOLDER_CATEGORIES = [
        'End Users',
        'Business Owners',
        'Technical Leads',
        'Operations/Support',
        'Customers',
        'Regulatory Bodies',
        'Integration Partners'
    ]

    def identify_stakeholders(self, project):
        """Map all stakeholder groups"""
        return {
            'primary': self.get_primary_stakeholders(project),
            'secondary': self.get_secondary_stakeholders(project),
            'tertiary': self.get_tertiary_stakeholders(project),
            'total_to_engage': self.calculate_engagement_strategy(project)
        }

    def analyze_stakeholder_needs(self, stakeholder):
        """Understand what each stakeholder needs"""
        return {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Stakeholder Discovery	Stakeholder Discovery
Requirements Elicitation Techniques	Requirements Elicitation Techniques
Requirements Documentation	Requirements Documentation
Requirement Validation & Sign-Off	Requirement Validation & Sign-Off
Requirements Traceability Matrix	Requirements Traceability Matrix
Best Practices
✅ DO
Engage all key stakeholders early
Document requirements in writing
Use specific, measurable language
Define acceptance criteria
Prioritize using MoSCoW method
Get stakeholder sign-off
Create traceability matrix
Review requirements regularly
Distinguish must-haves from nice-to-haves
Document assumptions and constraints
❌ DON'T
Rely on memory or verbal agreements
Create requirements without stakeholder input
Use ambiguous language (quickly, easily, etc.)
Skip non-functional requirements
Ignore constraints and dependencies
Over-document trivial details
Rush through requirements phase
Build without stakeholder agreement
Make scope changes without process
Forget about edge cases and error conditions
Weekly Installs
378
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