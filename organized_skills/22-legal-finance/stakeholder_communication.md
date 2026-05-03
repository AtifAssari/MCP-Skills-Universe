---
rating: ⭐⭐
title: stakeholder-communication
url: https://skills.sh/aj-geddes/useful-ai-prompts/stakeholder-communication
---

# stakeholder-communication

skills/aj-geddes/useful-ai-prompts/stakeholder-communication
stakeholder-communication
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill stakeholder-communication
SKILL.md
Stakeholder Communication
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Effective stakeholder communication ensures alignment, manages expectations, builds trust, and keeps projects on track by addressing concerns proactively.

When to Use
Project kickoff and initiation
Weekly/monthly status updates
Major milestone achievements
Changes to scope, timeline, or budget
Risks or issues requiring escalation
Stakeholder onboarding
Handling difficult conversations
Quick Start

Minimal working example:

# Stakeholder identification and engagement planning

class StakeholderAnalysis:
    ENGAGEMENT_LEVELS = {
        'Unaware': 'Provide basic information',
        'Resistant': 'Address concerns, build trust',
        'Neutral': 'Keep informed, demonstrate value',
        'Supportive': 'Engage as advocates',
        'Champion': 'Leverage for change leadership'
    }

    def __init__(self, project_name):
        self.project_name = project_name
        self.stakeholders = []

    def identify_stakeholders(self):
        """Common stakeholder categories"""
        return {
            'Executive Sponsors': {
                'interests': ['ROI', 'Strategic alignment', 'Timeline'],
                'communication': 'Monthly executive summary',
                'influence': 'High',
                'impact': 'High'
            },
            'Project Team': {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Stakeholder Analysis	Stakeholder Analysis
Communication Planning	Communication Planning
Status Communication Templates	Status Communication Templates
Difficult Conversations	Difficult Conversations
Best Practices
✅ DO
Tailor messages to stakeholder interests and influence
Communicate proactively, not reactively
Be transparent about issues and risks
Provide regular scheduled updates
Document decisions and communication
Acknowledge stakeholder concerns
Follow up on action items
Build relationships outside crisis mode
Use multiple communication channels
Celebrate wins together
❌ DON'T
Overcommunicate or undercommunicate
Use jargon stakeholders don't understand
Surprise stakeholders with bad news
Promise what you can't deliver
Make excuses without solutions
Communicate through intermediaries for critical issues
Ignore feedback or concerns
Change communication style inconsistently
Share inappropriate confidential details
Communicate budget/timeline bad news via email
Weekly Installs
296
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