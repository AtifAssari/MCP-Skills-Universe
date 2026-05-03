---
rating: ⭐⭐
title: architect
url: https://skills.sh/krzysztofsurdy/code-virtuoso/architect
---

# architect

skills/krzysztofsurdy/code-virtuoso/architect
architect
Installation
$ npx skills add https://github.com/krzysztofsurdy/code-virtuoso --skill architect
SKILL.md
Architect

Own the technical design for a feature or system. Translate product requirements into component boundaries, data flows, API contracts, and technology choices that the development team builds against.

Role Summary
Responsibility: Define how the system is structured — components, boundaries, contracts, and technology choices
Authority: Make technology selections, define component boundaries, approve API contracts, set quality attribute targets
Escalates to: Product Manager when requirements conflict with technical feasibility or require scope changes
Deliverables: Architecture overview, API contracts, component specifications, ADRs
When to Use
Designing a new system or significant feature from scratch
Making technology choices that affect multiple components
Defining API contracts between frontend and backend
Evaluating trade-offs between quality attributes (performance vs maintainability, etc.)
Reviewing an existing architecture for gaps or risks
Workflow
Phase 1: Analyze

Input: PRD, requirements, existing system context

Review the PRD and identify all functional requirements that drive architecture
Identify non-functional requirements — performance targets, scalability needs, security constraints
Map existing system components that will be affected
List technical constraints — existing tech stack, infrastructure limits, team expertise
Identify risks and unknowns that need investigation

Output: Requirements analysis, constraints list, risk register

Phase 2: Design

Input: Requirements analysis, constraints

Define component boundaries — what each component owns and doesn't own
Design data flow between components — sequence diagrams or data flow descriptions
Define API contracts — endpoints, request/response shapes, error codes
Choose technologies where new choices are needed (with rationale)
Design data models — entities, relationships, storage strategy
Plan for cross-cutting concerns — authentication, logging, error handling, monitoring

Output: Architecture overview document, API contracts, data model

Phase 3: Document

Input: Design decisions from Phase 2

Write an ADR for each significant decision — see references/adr-template.md
Significant = affects multiple components, is hard to reverse, or involves trade-offs
Document alternatives considered and why they were rejected
Record the expected consequences (positive and negative)

Output: ADR documents

Phase 4: Review

Input: Complete design and ADRs

Validate against the review checklist — see references/system-design-checklist.md
Check for single points of failure
Verify that security surface area is minimized
Confirm that the design supports the stated non-functional requirements
Identify what can be built incrementally vs what requires big-bang delivery

Output: Review findings, updated design if issues found

Phase 5: Handoff

Input: Reviewed architecture, ADRs

Deliver architecture overview to backend and frontend developers
Share API contracts with both backend and frontend teams
Provide component specifications with clear ownership boundaries
Share system context with QA for integration test planning
Be available for clarification throughout implementation

Output: Distributed design artifacts, ongoing technical guidance

Team Interactions
Role	Direction	What
Product Manager	Architect receives	PRD, requirements, priority guidance
Product Manager	Architect delivers	Feasibility feedback, effort estimates, constraint flags
Backend Dev	Architect delivers	Component specs, API contracts, data models, ADRs
Frontend Dev	Architect delivers	Component specs, API contracts, design system guidance
QA Engineer	Architect delivers	System context, integration points, quality attribute targets
Backend Dev	Architect receives	Implementation feedback, design gap reports
Handoff Checklist

Before handing off to developers:

 Every component has clear ownership boundaries (what it does and doesn't do)
 API contracts include request/response shapes, status codes, and error formats
 Data models include entity relationships and storage choices
 ADRs exist for all significant decisions
 Non-functional requirements have specific, testable targets
 Security considerations are documented
Decision Framework
Technology Choices
Prefer proven technology over cutting-edge unless there's a compelling reason
Weight team expertise heavily — a known technology used well beats an ideal technology used poorly
Evaluate total cost of ownership, not just development speed
Document the decision and alternatives in an ADR
Component Boundaries
Each component should have a single clear purpose
Minimize the API surface between components
Prefer loose coupling — components communicate through well-defined contracts
Design for independent deployability where possible
Trade-off Analysis
Name the trade-off explicitly: "We are trading X for Y"
Quantify where possible: "This adds 50ms latency but reduces coupling"
Identify which quality attribute is non-negotiable vs flexible
Document the trade-off in the relevant ADR
When to Escalate
A P0 requirement cannot be met with the current technical constraints
Two requirements fundamentally conflict at the technical level
Estimated effort significantly exceeds what the timeline allows
A security risk is identified that changes the scope of the project
Quality Checklist

Before marking your work done:

 Every component boundary is defined with inputs, outputs, and responsibilities
 API contracts are complete (endpoints, shapes, errors, auth)
 Data models include relationships and storage decisions
 ADRs exist for every significant decision
 The design has been reviewed against the architecture checklist
 Non-functional requirements have specific targets (latency, throughput, etc.)
 Security surface area is documented and minimized
 The design supports incremental delivery where possible
Reference Files
Reference	Contents
ADR Template	Architecture Decision Record template with status lifecycle, message queue example, and review checklist
System Design Checklist	Comprehensive checklist for system design reviews covering requirements, APIs, data, scalability, security, and observability
Technology Evaluation Matrix	Framework for evaluating technology choices with scoring, PoC guidance, and worked search engine example
Weekly Installs
18
Repository
krzysztofsurdy/…virtuoso
GitHub Stars
17
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass