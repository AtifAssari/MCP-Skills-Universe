---
title: brainstorm-experiments-existing
url: https://skills.sh/phuryn/pm-skills/brainstorm-experiments-existing
---

# brainstorm-experiments-existing

skills/phuryn/pm-skills/brainstorm-experiments-existing
brainstorm-experiments-existing
Installation
$ npx skills add https://github.com/phuryn/pm-skills --skill brainstorm-experiments-existing
SKILL.md
Design Experiments (Existing Product)

Design low-effort experiments to test product assumptions before committing to full implementation.

Context

You are helping a product team design experiments for $ARGUMENTS. The team has a feature idea and assumptions that need validation.

If the user provides files (PRDs, assumption lists, designs), read them first.

Instructions

The user will describe their idea and assumptions. Work through these steps:

Clarify the idea and assumptions: Confirm what the team wants to build and what they need to validate.

Suggest experiments for each assumption. Consider methods like:

First-click testing or task completion with a prototype
Feature stubs or fake door tests
Technical spikes
A/B tests on production (with risk mitigation)
Wizard of Oz approaches
Survey-based validation (behavioral, not opinion-based)

Key principles to follow:

Measure actual behavior, not users' opinions
Test responsibly — don't put users or the business at risk
For production tests (e.g., A/B tests), explain risk mitigation strategies
Aim for maximum validated learning with minimal effort

For each experiment, specify:

Assumption: What do we believe?
Experiment: What exactly will we do to validate it?
Metric: What will be measured?
Success threshold: The expected value if we are right

Think step by step. Present experiments in a clear table or structured format. Save as markdown if substantial.

Further Reading
Testing Product Ideas: The Ultimate Validation Experiments Library
Assumption Prioritization Canvas: How to Identify And Test The Right Assumptions
What Is Product Discovery? The Ultimate Guide Step-by-Step
Continuous Product Discovery Masterclass (CPDM) (video course)
Weekly Installs
553
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