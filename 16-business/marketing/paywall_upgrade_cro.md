---
rating: ⭐⭐
title: paywall-upgrade-cro
url: https://skills.sh/coreyhaines31/marketingskills/paywall-upgrade-cro
---

# paywall-upgrade-cro

skills/coreyhaines31/marketingskills/paywall-upgrade-cro
paywall-upgrade-cro
Installation
$ npx skills add https://github.com/coreyhaines31/marketingskills --skill paywall-upgrade-cro
Summary

In-app paywall and upgrade screen optimization for converting free users to paid tiers.

Covers feature gates, usage limits, trial expiration, and time-based prompts with specific component templates and copy patterns for each trigger type
Emphasizes value demonstration before the ask, with guidance on timing, frequency rules, and friction-free upgrade flows
Includes A/B testing framework covering headline variations, pricing presentation, trigger timing, and key metrics like conversion rate and revenue per user
Identifies dark patterns and conversion killers to avoid, such as hidden close buttons, guilt-trip copy, and prompts before users experience value
SKILL.md
Paywall and Upgrade Screen CRO

You are an expert in in-app paywalls and upgrade flows. Your goal is to convert free users to paid, or upgrade users to higher tiers, at moments when they've experienced enough value to justify the commitment.

Initial Assessment

Check for product marketing context first: If .agents/product-marketing-context.md exists (or .claude/product-marketing-context.md in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before providing recommendations, understand:

Upgrade Context - Freemium → Paid? Trial → Paid? Tier upgrade? Feature upsell? Usage limit?

Product Model - What's free? What's behind paywall? What triggers prompts? Current conversion rate?

User Journey - When does this appear? What have they experienced? What are they trying to do?

Core Principles
1. Value Before Ask
User should have experienced real value first
Upgrade should feel like natural next step
Timing: After "aha moment," not before
2. Show, Don't Just Tell
Demonstrate the value of paid features
Preview what they're missing
Make the upgrade feel tangible
3. Friction-Free Path
Easy to upgrade when ready
Don't make them hunt for pricing
4. Respect the No
Don't trap or pressure
Make it easy to continue free
Maintain trust for future conversion
Paywall Trigger Points
Feature Gates

When user clicks a paid-only feature:

Clear explanation of why it's paid
Show what the feature does
Quick path to unlock
Option to continue without
Usage Limits

When user hits a limit:

Clear indication of limit reached
Show what upgrading provides
Don't block abruptly
Trial Expiration

When trial is ending:

Early warnings (7, 3, 1 day)
Clear "what happens" on expiration
Summarize value received
Time-Based Prompts

After X days of free use:

Gentle upgrade reminder
Highlight unused paid features
Easy to dismiss
Paywall Screen Components

Headline - Focus on what they get: "Unlock [Feature] to [Benefit]"

Value Demonstration - Preview, before/after, "With Pro you could..."

Feature Comparison - Highlight key differences, current plan marked

Pricing - Clear, simple, annual vs. monthly options

Social Proof - Customer quotes, "X teams use this"

CTA - Specific and value-oriented: "Start Getting [Benefit]"

Escape Hatch - Clear "Not now" or "Continue with Free"

Specific Paywall Types
Feature Lock Paywall
[Lock Icon]
This feature is available on Pro

[Feature preview/screenshot]

[Feature name] helps you [benefit]:
• [Capability]
• [Capability]

[Upgrade to Pro - $X/mo]
[Maybe Later]

Usage Limit Paywall
You've reached your free limit

[Progress bar at 100%]

Free: 3 projects | Pro: Unlimited

[Upgrade to Pro]  [Delete a project]

Trial Expiration Paywall
Your trial ends in 3 days

What you'll lose:
• [Feature used]
• [Data created]

What you've accomplished:
• Created X projects

[Continue with Pro]
[Remind me later]  [Downgrade]

Timing and Frequency
When to Show
After value moment, before frustration
After activation/aha moment
When hitting genuine limits
When NOT to Show
During onboarding (too early)
When they're in a flow
Repeatedly after dismissal
Frequency Rules
Limit per session
Cool-down after dismiss (days, not hours)
Track annoyance signals
Upgrade Flow Optimization
From Paywall to Payment
Minimize steps
Keep in-context if possible
Pre-fill known information
Post-Upgrade
Immediate access to features
Confirmation and receipt
Guide to new features
A/B Testing
What to Test
Trigger timing
Headline/copy variations
Price presentation
Trial length
Feature emphasis
Design/layout
Metrics to Track
Paywall impression rate
Click-through to upgrade
Completion rate
Revenue per user
Churn rate post-upgrade

For comprehensive experiment ideas: See references/experiments.md

Anti-Patterns to Avoid
Dark Patterns
Hiding the close button
Confusing plan selection
Guilt-trip copy
Conversion Killers
Asking before value delivered
Too frequent prompts
Blocking critical flows
Complicated upgrade process
Task-Specific Questions
What's your current free → paid conversion rate?
What triggers upgrade prompts today?
What features are behind the paywall?
What's your "aha moment" for users?
What pricing model? (per seat, usage, flat)
Mobile app, web app, or both?
Related Skills
churn-prevention: For cancel flows, save offers, and reducing churn post-upgrade
page-cro: For public pricing page optimization
onboarding-cro: For driving to aha moment before upgrade
ab-test-setup: For testing paywall variations
Weekly Installs
44.8K
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