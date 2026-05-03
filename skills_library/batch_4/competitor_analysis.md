---
title: competitor-analysis
url: https://skills.sh/aj-geddes/useful-ai-prompts/competitor-analysis
---

# competitor-analysis

skills/aj-geddes/useful-ai-prompts/competitor-analysis
competitor-analysis
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill competitor-analysis
SKILL.md
Competitor Analysis
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Systematic competitor analysis reveals market positioning, identifies competitive advantages, and informs strategic product decisions.

When to Use
Product strategy development
Market entry planning
Pricing strategy
Feature prioritization
Market positioning
Threat assessment
Investment decisions
Quick Start

Minimal working example:

# Identify and categorize competitors

class CompetitorAnalysis:
    COMPETITOR_TYPES = {
        'Direct': 'Same market, same features',
        'Indirect': 'Different approach, same problem',
        'Adjacent': 'Related market, potential crossover',
        'Emerging': 'New entrants, potential disruptors'
    }

    def identify_competitors(self, market_segment):
        """Find all competitors"""
        return {
            'direct_competitors': [
                {'name': 'Competitor A', 'market_share': '25%', 'founded': 2015},
                {'name': 'Competitor B', 'market_share': '18%', 'founded': 2012}
            ],
            'indirect_competitors': [
                {'name': 'Different Approach A', 'method': 'AI-powered'}
            ],
            'emerging_threats': [
                {'name': 'Startup X', 'funding': '$10M Series A', 'differentiator': 'Mobile-first'}
            ]
        }

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Competitor Identification	Competitor Identification
Competitive Matrix	Competitive Matrix
SWOT Analysis	SWOT Analysis
Competitive Insights Report	Competitive Insights Report
Best Practices
✅ DO
Analyze current and emerging competitors
Monitor competitor activities regularly
Understand customer perception of competition
Use competitive insights to inform strategy
Focus on differentiation, not just comparison
Include market trends in analysis
Update competitive analysis quarterly
Share insights across organization
Use data to back up claims
Consider indirect competitors too
❌ DON'T
Obsess over competitor pricing
Copy competitor features blindly
Ignore emerging threats
Use only marketing materials for analysis
Focus only on feature comparison
Neglect customer feedback on competition
Make analysis too complex
Hide uncomfortable truths
Change strategy based on every competitor move
Ignore your competitive advantages
Weekly Installs
414
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn