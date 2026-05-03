---
title: architecture
url: https://skills.sh/sickn33/antigravity-awesome-skills/architecture
---

# architecture

skills/sickn33/antigravity-awesome-skills/architecture
architecture
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill architecture
Summary

Structured framework for analyzing requirements, evaluating trade-offs, and documenting architectural decisions.

Provides context discovery questions and project classification to align architecture with actual requirements
Includes trade-off analysis templates and ADR (Architecture Decision Record) documentation patterns for capturing decision rationale
Offers decision trees and anti-pattern guidance to help select appropriate architectural patterns
Emphasizes simplicity-first approach: add complexity only when proven necessary, with validation checklist covering requirements clarity, constraints, trade-off analysis, and team capability alignment
SKILL.md
Architecture Decision Framework

"Requirements drive architecture. Trade-offs inform decisions. ADRs capture rationale."

🎯 Selective Reading Rule

Read ONLY files relevant to the request! Check the content map, find what you need.

File	Description	When to Read
context-discovery.md	Questions to ask, project classification	Starting architecture design
trade-off-analysis.md	ADR templates, trade-off framework	Documenting decisions
pattern-selection.md	Decision trees, anti-patterns	Choosing patterns
examples.md	MVP, SaaS, Enterprise examples	Reference implementations
patterns-reference.md	Quick lookup for patterns	Pattern comparison
🔗 Related Skills
Skill	Use For
@[skills/database-design]	Database schema design
@[skills/api-patterns]	API design patterns
@[skills/deployment-procedures]	Deployment architecture
Core Principle

"Simplicity is the ultimate sophistication."

Start simple
Add complexity ONLY when proven necessary
You can always add patterns later
Removing complexity is MUCH harder than adding it
Validation Checklist

Before finalizing architecture:

 Requirements clearly understood
 Constraints identified
 Each decision has trade-off analysis
 Simpler alternatives considered
 ADRs written for significant decisions
 Team expertise matches chosen patterns
When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
784
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass