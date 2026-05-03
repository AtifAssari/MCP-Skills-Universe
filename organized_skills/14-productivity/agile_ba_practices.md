---
rating: ⭐⭐
title: agile ba practices
url: https://skills.sh/danhvb/my-ba-skills/agile-ba-practices
---

# agile ba practices

skills/danhvb/my-ba-skills/Agile BA Practices
Agile BA Practices
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Agile BA Practices'
SKILL.md
Agile BA Practices Skill
Purpose

Guide AI assistants in applying BA practices within Agile and Hybrid methodologies, balancing lightweight documentation with comprehensive analysis.

BA Role in Agile
Traditional BA vs Agile BA
Aspect	Traditional BA	Agile BA
Documentation	Comprehensive upfront	Just enough, just in time
Requirements	Complete before dev	Emergent, evolving
Deliverables	BRD, FRS, Use Cases	User stories, acceptance criteria
Approach	Waterfall/phases	Iterative/incremental
Feedback	End of project	Continuous, each sprint
Change	Formal change control	Embrace change
BA Role in Scrum

Sprint Planning:

Clarify user stories with team
Answer questions about requirements
Help estimate complexity
Identify dependencies

During Sprint:

Available for clarification
Accept completed stories
Refine upcoming stories
Write acceptance criteria

Sprint Review:

Demo features with PO
Gather stakeholder feedback
Note change requests

Sprint Retrospective:

Reflect on BA processes
Improve collaboration

Backlog Refinement:

Elaborate upcoming stories
Add acceptance criteria
Split large stories
Prioritize with PO
Core Agile BA Artifacts
Product Backlog

Structure:

Epic > Feature > User Story > Task


Example:

Epic: Customer Self-Service Portal
├── Feature: Account Management
│   ├── User Story: View profile
│   ├── User Story: Update profile
│   └── User Story: Change password
├── Feature: Order History
│   ├── User Story: View orders
│   └── User Story: Track shipments
└── Feature: Support
    ├── User Story: Submit ticket
    └── User Story: View FAQs

User Story Template
**Title**: [Short, descriptive title]

As a [user role]
I want [goal]
So that [benefit]

**Acceptance Criteria**:
- Given... When... Then...
- Given... When... Then...

**Notes**: [Technical notes, wireframe links]

**Story Points**: [Estimate]

Definition of Ready (DoR)

Story is Ready when:

 User story follows format (As a... I want... So that...)
 Acceptance criteria are clear and testable
 Story is independent of other stories in sprint
 Story is small enough to complete in sprint
 Technical approach discussed with team
 Dependencies identified and resolved
 Wireframes/designs available (if UI work)
Definition of Done (DoD)

Story is Done when:

 All acceptance criteria met
 Code peer reviewed
 Unit tests written and passing
 Integration tests passing
 No critical bugs
 Documentation updated
 Deployed to staging
 PO accepted
Agile Documentation Approach
Just Enough Documentation

Write documentation when:

Required for compliance/audit
Multiple teams need to understand
Complex business rules
Integration specifications
Knowledge needs to persist

Keep lean when:

Small team with good communication
Frequent face-to-face interaction
Simple, well-understood domain
Short project duration
Lightweight Artifacts
Traditional	Agile Alternative
100-page BRD	1-page project brief + backlog
Detailed FRS	User stories + acceptance criteria
Use Case documents	Acceptance scenarios
Data dictionary	Entity definitions in stories
Test plan	Automated tests + DoD
Living Documentation
Keep docs in version control (Git)
Update as requirements evolve
Use wikis (Lark, Notion, Confluence)
Automate where possible
Backlog Refinement
Purpose
Break down large stories
Add detail to upcoming stories
Clarify requirements
Estimate stories
Prioritize backlog
Cadence
1-2 hours per week
1-2 sprints ahead
Regular rhythm
Refinement Activities

Story Splitting:

By workflow step
By business rule
By data variation
By platform (iOS/Android)
By user role

Estimation:

Planning poker
Story points (Fibonacci)
T-shirt sizing
Relative sizing

Prioritization with PO:

Business value
Risk reduction
Dependencies
Technical debt
Story Mapping
What is Story Mapping?

Visual technique to organize user stories along the user journey.

Structure
Activities (top row)
    ↓
Tasks (second row)
    ↓
Details/Stories (lower rows, by priority)

Example: E-commerce Story Map
Browse Products → Add to Cart → Checkout → Order Tracking
     ↓              ↓             ↓            ↓
View catalog     Add item      Shipping      View status
Search products  Update qty    Payment       Track shipment
Filter/sort      Save for later Review order  Get notifications

MVP ─────────────────────────────────────────────────
View catalog     Add item      Shipping      View status
Search           Update qty    Payment

Release 2 ───────────────────────────────────────────
Filter/sort      Save for later Review order Track shipment

Hybrid Methodology
When to Use Hybrid
Large enterprise projects
Regulatory requirements
Fixed-scope contracts
Distributed teams
Mixed maturity levels
Hybrid Approach

Waterfall Elements:

Initial discovery/analysis phase
Formal BRD for approval
Architecture design upfront
Go-live planning

Agile Elements:

Iterative development
User stories and sprints
Continuous delivery
Sprint demos
Example Hybrid Flow
Discovery (2-4 weeks): Requirements, BRD, Architecture
    ↓
Sprint 0: Setup, detailed design, initial stories
    ↓
Sprints 1-N: Agile development
    ↓
UAT Sprint: User acceptance testing
    ↓
Go-live: Deployment, hypercare

Scaled Agile (SAFe Basics)
Hierarchy
Portfolio: Strategic initiatives
Program: Agile Release Train (ART)
Team: Scrum teams
Key Roles
Product Manager (portfolio)
Product Owner (team)
System Architect
Release Train Engineer
Key Events
PI Planning (Program Increment)
System Demo
Inspect & Adapt
Tools for Agile BA
Backlog Management
Jira
Azure DevOps
Trello
Lark Base
Documentation
Lark Docs
Notion
Confluence
Collaboration
Miro/FigJam (story mapping)
Figma (wireframes)
Lark Meetings
Best Practices
Communication

✅ Face-to-face over documentation ✅ Working software over comprehensive docs ✅ Daily standups for alignment ✅ Demo early and often

Requirements

✅ Embrace change ✅ Just-in-time elaboration ✅ Collaborative refinement ✅ Testable acceptance criteria

Documentation

✅ Write just enough ✅ Keep it current ✅ Make it accessible ✅ Automate when possible

Collaboration

✅ Work closely with PO ✅ Be available to team ✅ Facilitate, don't dictate ✅ Learn technical basics

Common Anti-Patterns

❌ Big Design Up Front: Too much analysis before development ❌ Requirements Dumping: Writing stories without collaboration ❌ Absent BA: Not available during sprints ❌ Gold Plating: Over-documenting everything ❌ Scope Denial: Not adapting to changing requirements

References
Agile Manifesto
Scrum Guide
User Story Mapping (Jeff Patton)
SAFe Framework
Agile Extension to BABOK
Weekly Installs
–
Repository
danhvb/my-ba-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass