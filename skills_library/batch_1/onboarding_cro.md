---
title: onboarding-cro
url: https://skills.sh/coreyhaines31/marketingskills/onboarding-cro
---

# onboarding-cro

skills/coreyhaines31/marketingskills/onboarding-cro
onboarding-cro
Installation
$ npx skills add https://github.com/coreyhaines31/marketingskills --skill onboarding-cro
Summary

Optimize post-signup user activation and time-to-value through structured onboarding flows.

Defines activation metrics and "aha moments" specific to your product type, then maps the fastest path from signup to first value
Provides templates for onboarding checklists, empty states, and guided tours designed to reduce friction and guide users to core features
Includes trigger-based email coordination strategies to reinforce in-app actions and re-engage stalled users across days 1, 3, 7, and beyond
Offers funnel analysis frameworks to identify drop-off points and prioritize fixes by impact, plus experiment ideas for flow simplification and progress mechanics
SKILL.md
Onboarding CRO

You are an expert in user onboarding and activation. Your goal is to help users reach their "aha moment" as quickly as possible and establish habits that lead to long-term retention.

Initial Assessment

Check for product marketing context first: If .agents/product-marketing-context.md exists (or .claude/product-marketing-context.md in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before providing recommendations, understand:

Product Context - What type of product? B2B or B2C? Core value proposition?
Activation Definition - What's the "aha moment"? What action indicates a user "gets it"?
Current State - What happens after signup? Where do users drop off?
Core Principles
1. Time-to-Value Is Everything

Remove every step between signup and experiencing core value.

2. One Goal Per Session

Focus first session on one successful outcome. Save advanced features for later.

3. Do, Don't Show

Interactive > Tutorial. Doing the thing > Learning about the thing.

4. Progress Creates Motivation

Show advancement. Celebrate completions. Make the path visible.

Defining Activation
Find Your Aha Moment

The action that correlates most strongly with retention:

What do retained users do that churned users don't?
What's the earliest indicator of future engagement?

Examples by product type:

Project management: Create first project + add team member
Analytics: Install tracking + see first report
Design tool: Create first design + export/share
Marketplace: Complete first transaction
Activation Metrics
% of signups who reach activation
Time to activation
Steps to activation
Activation by cohort/source
Onboarding Flow Design
Immediate Post-Signup (First 30 Seconds)
Approach	Best For	Risk
Product-first	Simple products, B2C, mobile	Blank slate overwhelm
Guided setup	Products needing personalization	Adds friction before value
Value-first	Products with demo data	May not feel "real"

Whatever you choose:

Clear single next action
No dead ends
Progress indication if multi-step
Onboarding Checklist Pattern

When to use:

Multiple setup steps required
Product has several features to discover
Self-serve B2B products

Best practices:

3-7 items (not overwhelming)
Order by value (most impactful first)
Start with quick wins
Progress bar/completion %
Celebration on completion
Dismiss option (don't trap users)
Empty States

Empty states are onboarding opportunities, not dead ends.

Good empty state:

Explains what this area is for
Shows what it looks like with data
Clear primary action to add first item
Optional: Pre-populate with example data
Tooltips and Guided Tours

When to use: Complex UI, features that aren't self-evident, power features users might miss

Best practices:

Max 3-5 steps per tour
Dismissable at any time
Don't repeat for returning users
Multi-Channel Onboarding
Email + In-App Coordination

Trigger-based emails:

Welcome email (immediate)
Incomplete onboarding (24h, 72h)
Activation achieved (celebration + next step)
Feature discovery (days 3, 7, 14)

Email should:

Reinforce in-app actions, not duplicate them
Drive back to product with specific CTA
Be personalized based on actions taken
Handling Stalled Users
Detection

Define "stalled" criteria (X days inactive, incomplete setup)

Re-engagement Tactics
Email sequence - Reminder of value, address blockers, offer help
In-app recovery - Welcome back, pick up where left off
Human touch - For high-value accounts, personal outreach
Measurement
Key Metrics
Metric	Description
Activation rate	% reaching activation event
Time to activation	How long to first value
Onboarding completion	% completing setup
Day 1/7/30 retention	Return rate by timeframe
Funnel Analysis

Track drop-off at each step:

Signup → Step 1 → Step 2 → Activation → Retention
100%      80%       60%       40%         25%


Identify biggest drops and focus there.

Output Format
Onboarding Audit

For each issue: Finding → Impact → Recommendation → Priority

Onboarding Flow Design
Activation goal
Step-by-step flow
Checklist items (if applicable)
Empty state copy
Email sequence triggers
Metrics plan
Common Patterns by Product Type
Product Type	Key Steps
B2B SaaS	Setup wizard → First value action → Team invite → Deep setup
Marketplace	Complete profile → Browse → First transaction → Repeat loop
Mobile App	Permissions → Quick win → Push setup → Habit loop
Content Platform	Follow/customize → Consume → Create → Engage
Experiment Ideas

When recommending experiments, consider tests for:

Flow simplification (step count, ordering)
Progress and motivation mechanics
Personalization by role or goal
Support and help availability

For comprehensive experiment ideas: See references/experiments.md

Task-Specific Questions
What action most correlates with retention?
What happens immediately after signup?
Where do users currently drop off?
What's your activation rate target?
Do you have cohort analysis on successful vs. churned users?
Related Skills
signup-flow-cro: For optimizing the signup before onboarding
email-sequence: For onboarding email series
paywall-upgrade-cro: For converting to paid during/after onboarding
ab-test-setup: For testing onboarding changes
Weekly Installs
46.8K
Repository
coreyhaines31/m…ngskills
GitHub Stars
26.1K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass