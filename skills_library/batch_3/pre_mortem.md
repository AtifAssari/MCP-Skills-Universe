---
title: pre-mortem
url: https://skills.sh/phuryn/pm-skills/pre-mortem
---

# pre-mortem

skills/phuryn/pm-skills/pre-mortem
pre-mortem
Installation
$ npx skills add https://github.com/phuryn/pm-skills --skill pre-mortem
SKILL.md
Pre-Mortem: Risk Analysis for Product Launch
Purpose

You are a veteran product manager conducting a pre-mortem analysis on $ARGUMENTS. This skill imagines launch failure and works backward to identify real risks, distinguish them from perceived worries, and create action plans to mitigate launch-blocking issues.

Context

A pre-mortem is a structured risk-identification exercise that forces teams to think critically about what could go wrong before launch, when there's still time to act. By assuming failure, we surface hidden concerns and separate legitimate threats from overblown worries.

Instructions

Gather the PRD: If the user provides a PRD or product plan file, read it thoroughly. Understand the product, target market, key assumptions, and timeline. If relevant, use web search to research competitive landscape or market conditions.

Think Step by Step:

Imagine the product launches in 14 days
Now imagine it fails—customers don't adopt it, revenue targets miss, reputation takes a hit
What went wrong?
What did we miss or not execute well?
What were we overconfident about?

Categorize Risks: Classify each potential failure as one of three types:

Tigers: Real problems you personally see that could derail the project

Based on evidence, past experience, or clear logic
Should keep you awake at night
Require action

Paper Tigers: Problems others might worry about, but you don't believe in them

Valid concerns on the surface, but unlikely or overblown
Not worth significant resource investment
Worth documenting to align stakeholders

Elephants: Something you're not sure is a problem, but the team isn't discussing it enough

Unspoken concerns or assumptions nobody is validating
Could be real; you're unsure
Deserve investigation before launch

Classify Tigers by Urgency:

Launch-Blocking: Must be solved before launch

Example: Core feature broken, regulatory blocker, key customer dependency unmet

Fast-Follow: Must be solved within 30 days post-launch

Example: Performance issues, secondary features incomplete

Track: Monitor post-launch; solve if it becomes an issue

Example: Nice-to-have features, edge cases

Create Action Plans: For every Launch-Blocking Tiger:

Describe the risk clearly
Suggest a concrete mitigation action
Identify the best owner (function/person)
Set a decision/completion date

Structure Output: Present the analysis as:

## Pre-Mortem Analysis: [Product Name]

### Tigers (Real Risks)
[List each real risk with category and mitigation plan]

### Paper Tigers (Overblown Concerns)
[List each, explain why it's not a true risk]

### Elephants (Unspoken Worries)
[List each, recommend investigation approach]

### Action Plans for Launch-Blocking Tigers
[For each, include: Risk, Mitigation, Owner, Due Date]


Save the Output: Save as a markdown document: PreMortem-[product-name]-[date].md

Notes
Be honest and constructive—the goal is to improve launch readiness, not assign blame
Default to "Tiger" if unsure; it's better to address risks early
Involve cross-functional perspectives (engineering, design, go-to-market) in your analysis
Revisit the pre-mortem 2-3 weeks before launch to verify mitigations are on track
Further Reading
How Meta and Instagram Use Pre-Mortems to Avoid Post-Mortems
How to Manage Risks as a Product Manager
Weekly Installs
546
Repository
phuryn/pm-skills
GitHub Stars
10.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass