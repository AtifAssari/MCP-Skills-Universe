---
rating: ⭐⭐
title: designing-systems
url: https://skills.sh/dralgorhythm/claude-agentic-framework/designing-systems
---

# designing-systems

skills/dralgorhythm/claude-agentic-framework/designing-systems
designing-systems
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill designing-systems
SKILL.md
Designing Systems
Workflows
 Requirements: Gather functional and non-functional requirements
 Diagrams: Create C4 diagrams (Context, Container)
 Data: Define data model and storage strategy
 API: Define interfaces and contracts
 Risks: Identify single points of failure
 Document: Save to ./artifacts/adr_[topic].md
Feedback Loops
Draft design document
Review with stakeholders
Create POC for risky components
Refine design based on POC
Finalize ADR
Blueprint Template

Every system design should include:

High-Level Diagram: Mermaid graph showing components
Component Boundaries: Clear responsibility definitions
API Definitions: OpenAPI or GraphQL specs
Data Models: Schema definitions
Trade-off Analysis: Rationale for key decisions
C4 Model Levels
Level 1: Context

Who uses the system? What external systems does it interact with?

Level 2: Container

What are the major deployable units? (APIs, databases, queues)

Level 3: Component

What are the major building blocks within each container?

Level 4: Code

Class/function level (usually not needed in architecture docs)

Trade-off Analysis

For major decisions, explicitly document:

Decision	Option A	Option B
Pros	...	...
Cons	...	...
When to Choose	...	...
Non-Functional Requirements

Always consider:

Scalability: Expected load, growth rate
Availability: SLA targets, failure modes
Latency: P50, P95, P99 requirements
Security: Authentication, authorization, data protection
Cost: Infrastructure, operational overhead
Resources
System Design Template
ADR Template
Weekly Installs
38
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass