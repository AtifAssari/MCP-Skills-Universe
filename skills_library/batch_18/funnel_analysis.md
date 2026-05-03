---
title: funnel-analysis
url: https://skills.sh/nicepkg/ai-workflow/funnel-analysis
---

# funnel-analysis

skills/nicepkg/ai-workflow/funnel-analysis
funnel-analysis
Installation
$ npx skills add https://github.com/nicepkg/ai-workflow --skill funnel-analysis
SKILL.md
Funnel Analysis Skill

Analyze user behavior through multi-step conversion funnels to identify bottlenecks and optimization opportunities in marketing campaigns, user journeys, and business processes.

Quick Start

This skill helps you:

Build conversion funnels from multi-step user data
Calculate conversion rates between each step
Perform segmentation analysis by different user attributes
Create interactive visualizations with Plotly
Generate business insights and optimization recommendations
When to Use
Marketing campaign analysis (promotion → purchase)
User onboarding flow analysis
Website conversion funnel optimization
App user journey analysis
Sales pipeline analysis
Lead nurturing process analysis
Key Requirements

Install required packages:

pip install pandas plotly matplotlib numpy seaborn

Core Workflow
1. Data Preparation

Your data should include:

User journey steps (clicks, page views, actions)
User identifiers (customer_id, user_id, etc.)
Timestamps or step indicators
Optional: user attributes for segmentation (gender, device, location)
2. Analysis Process
Load and merge user journey data
Define funnel steps and calculate metrics
Perform segmentations (by device, gender, etc.)
Create visualizations
Generate insights and recommendations
3. Output Deliverables
Funnel visualization charts
Conversion rate tables
Segmented analysis reports
Optimization recommendations
Example Usage Scenarios
E-commerce Purchase Funnel
# Steps: Promotion → Search → Product View → Add to Cart → Purchase
# Analyze by device type and customer segment

User Registration Funnel
# Steps: Landing Page → Sign Up → Email Verification → Profile Complete
# Identify where users drop off most

Content Consumption Funnel
# Steps: Article View → Comment → Share → Subscribe
# Measure engagement conversion rates

Common Analysis Patterns
Bottleneck Identification: Find steps with highest drop-off rates
Segment Comparison: Compare conversion across user groups
Temporal Analysis: Track conversion over time
A/B Testing: Compare different funnel variations
Optimization Impact: Measure changes before/after improvements
Integration Examples

See examples/ directory for:

basic_funnel.py - Simple funnel analysis
segmented_funnel.py - Advanced segmentation analysis
Sample datasets for testing
Best Practices
Ensure data quality and consistency
Define clear funnel steps
Consider user journey time windows
Validate statistical significance
Focus on actionable insights
Weekly Installs
22
Repository
nicepkg/ai-workflow
GitHub Stars
176
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass