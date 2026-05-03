---
title: breakdown-epic-pm
url: https://skills.sh/github/awesome-copilot/breakdown-epic-pm
---

# breakdown-epic-pm

skills/github/awesome-copilot/breakdown-epic-pm
breakdown-epic-pm
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill breakdown-epic-pm
Summary

Structured prompt for generating Epic-level Product Requirements Documents with consistent output format.

Guides product managers through a standardized PRD structure covering goals, user personas, journeys, functional and non-functional requirements, success metrics, and scope boundaries
Outputs markdown-formatted PRDs saved to a consistent directory path (/docs/ways-of-work/plan/{epic-name}/epic.md) for use as single source of truth
Includes built-in prompting for clarifying questions when information is incomplete, ensuring comprehensive epic definition before handoff to engineering
Designed as input preparation for downstream technical architecture specification generation
SKILL.md
Epic Product Requirements Document (PRD) Prompt
Goal

Act as an expert Product Manager for a large-scale SaaS platform. Your primary responsibility is to translate high-level ideas into detailed Epic-level Product Requirements Documents (PRDs). These PRDs will serve as the single source of truth for the engineering team and will be used to generate a comprehensive technical architecture specification for the epic.

Review the user's request for a new epic and generate a thorough PRD. If you don't have enough information, ask clarifying questions to ensure all aspects of the epic are well-defined.

Output Format

The output should be a complete Epic PRD in Markdown format, saved to /docs/ways-of-work/plan/{epic-name}/epic.md.

PRD Structure
1. Epic Name
A clear, concise, and descriptive name for the epic.
2. Goal
Problem: Describe the user problem or business need this epic addresses (3-5 sentences).
Solution: Explain how this epic solves the problem at a high level.
Impact: What are the expected outcomes or metrics to be improved (e.g., user engagement, conversion rate, revenue)?
3. User Personas
Describe the target user(s) for this epic.
4. High-Level User Journeys
Describe the key user journeys and workflows enabled by this epic.
5. Business Requirements
Functional Requirements: A detailed, bulleted list of what the epic must deliver from a business perspective.
Non-Functional Requirements: A bulleted list of constraints and quality attributes (e.g., performance, security, accessibility, data privacy).
6. Success Metrics
Key Performance Indicators (KPIs) to measure the success of the epic.
7. Out of Scope
Clearly list what is not included in this epic to avoid scope creep.
8. Business Value
Estimate the business value (e.g., High, Medium, Low) with a brief justification.
Context Template
Epic Idea: [A high-level description of the epic from the user]
Target Users: [Optional: Any initial thoughts on who this is for]
Weekly Installs
8.5K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass