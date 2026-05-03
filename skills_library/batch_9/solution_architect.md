---
title: solution-architect
url: https://skills.sh/404kidwiz/claude-supercode-skills/solution-architect
---

# solution-architect

skills/404kidwiz/claude-supercode-skills/solution-architect
solution-architect
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill solution-architect
SKILL.md
Solution Architect
Purpose

Provides expertise in designing enterprise-scale solutions that align technology with business objectives. Specializes in architecture frameworks, trade-off analysis, technology selection, and ensuring solutions meet functional and non-functional requirements.

When to Use
Designing end-to-end solution architecture for new initiatives
Evaluating technology options and making selection decisions
Creating architecture decision records (ADRs)
Ensuring solutions meet enterprise architecture standards
Analyzing trade-offs between competing approaches
Designing integration patterns between systems
Translating business requirements into technical architecture
Conducting architecture reviews and assessments
Quick Start

Invoke this skill when:

Designing end-to-end solution architecture for new initiatives
Evaluating technology options and making selection decisions
Creating architecture decision records (ADRs)
Ensuring solutions meet enterprise architecture standards
Analyzing trade-offs between competing approaches

Do NOT invoke when:

Implementing code changes → use appropriate developer skill
Designing cloud infrastructure → use cloud-architect
Reviewing code quality → use code-reviewer
Managing project execution → use project-manager
Decision Framework
Architecture Decision?
├── Technology Selection → Build evaluation matrix + PoC
├── Integration Pattern → Sync/Async + coupling analysis
├── Data Architecture → Consistency + availability trade-offs
├── Security Architecture → Defense in depth + compliance
├── Scalability → Horizontal/vertical + bottleneck analysis
└── Cost Optimization → Build vs buy + TCO analysis

Core Workflows
1. Solution Design Process
Gather and analyze business requirements
Identify key functional and non-functional requirements
Map to existing enterprise architecture patterns
Design candidate architectures (2-3 options)
Evaluate trade-offs using weighted criteria
Document decisions in ADRs with rationale
Create implementation roadmap with phases
2. Architecture Decision Record
State the decision context and problem
List considered alternatives
Document decision drivers and criteria
Explain chosen option with justification
Note consequences and trade-offs
Record related decisions and dependencies
3. Technology Evaluation
Define evaluation criteria from requirements
Weight criteria by business importance
Score candidates against each criterion
Conduct proof-of-concept for top candidates
Assess vendor viability and support
Calculate total cost of ownership
Document recommendation with rationale
Best Practices
Start with business outcomes, not technology preferences
Document decisions and rationale in ADRs
Consider total cost of ownership, not just initial cost
Design for change; isolate volatile components
Validate assumptions early with prototypes
Engage stakeholders throughout design process
Anti-Patterns
Technology-first thinking → Start from business requirements
Analysis paralysis → Time-box decisions, use reversibility
Ivory tower architecture → Collaborate with implementation teams
Ignoring NFRs → Address security, scalability, operability early
Vendor lock-in blindness → Evaluate portability and exit costs
Weekly Installs
273
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass