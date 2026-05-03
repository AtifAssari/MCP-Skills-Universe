---
rating: ⭐⭐⭐
title: ba best practices
url: https://skills.sh/danhvb/my-ba-skills/ba-best-practices
---

# ba best practices

skills/danhvb/my-ba-skills/BA Best Practices
BA Best Practices
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'BA Best Practices'
SKILL.md
BA Best Practices Skill
Purpose

Guide AI assistants in applying professional BA best practices to ensure high-quality requirements, effective collaboration, and successful project outcomes.

Requirements Quality Attributes
1. Clear
Use simple, unambiguous language
Avoid jargon without definition
One requirement per statement
Specific and concrete

❌ Bad: "System should be user-friendly" ✅ Good: "System shall complete checkout process in maximum 3 clicks"

2. Complete
All necessary information included
Edge cases addressed
Exceptions documented
Success and failure scenarios covered
3. Consistent
No contradictions with other requirements
Consistent terminology throughout
Aligned with business objectives
Follows documentation standards
4. Testable
Can be verified through testing
Measurable acceptance criteria
Observable outcomes
Objective pass/fail determination

❌ Bad: "System should load quickly" ✅ Good: "System shall load homepage in < 3 seconds on 4G connection"

5. Traceable
Linked to business need
Source documented
Unique identifier
Impact analysis possible
6. Feasible
Technically achievable
Within budget constraints
Realistic timeline
Resources available
Documentation Standards
Naming Conventions

Requirements IDs:

Format: [TYPE]-[MODULE]-[NUMBER]
Examples: FR-AUTH-001, NFR-PERF-005, BR-PRICING-003

Documents:

BRD_ProjectName_v1.0.pdf
FRS_ModuleName_v2.1.pdf
UseCases_FeatureName_v1.0.pdf
Version Control

Semantic Versioning:

Major.Minor.Patch (1.0.0)
Major: Significant changes, restructuring
Minor: New sections, requirements added
Patch: Corrections, clarifications

Change Log:

Date	Version	Author	Changes	Reason
2026-01-15	1.0	John	Initial	New project
2026-01-20	1.1	Jane	Added FR-005-010	Stakeholder feedback
Document Structure

Standard Sections:

Document Control (version, approvals, distribution)
Table of Contents
Introduction (purpose, scope, audience)
Main Content
Appendices (glossary, references, diagrams)
Requirements Traceability Matrix (RTM)

Purpose: Link requirements to business needs, design, and tests

Req ID	Business Need	Design Element	Test Case	Status
FR-001	BN-001	DES-UI-001	TC-001, TC-002	Implemented
FR-002	BN-001	DES-API-003	TC-003	In Progress

Benefits:

Ensure all business needs addressed
Impact analysis for changes
Test coverage verification
Audit trail
Change Management
Change Request Process

Request Submission

Change description
Business justification
Impact assessment
Priority

Impact Analysis

Requirements affected
Design impact
Development effort
Testing impact
Timeline impact
Cost impact

Review & Approval

Change Control Board (CCB) review
Stakeholder approval
Budget approval (if needed)

Implementation

Update requirements
Update design
Communicate changes
Update traceability

Verification

Validate changes implemented correctly
Update documentation
Close change request
Change Request Template
# Change Request CR-001

**Date**: 2026-01-20
**Requested By**: Marketing Manager
**Priority**: High

## Change Description
Add social login (Google, Facebook) to registration process

## Business Justification
- Reduce registration friction
- Increase conversion by estimated 25%
- Competitive parity

## Impact Analysis
**Requirements**: Add FR-AUTH-015, FR-AUTH-016
**Design**: New OAuth integration components
**Development**: 2 weeks (40 hours)
**Testing**: 1 week UAT
**Timeline**: Delay release by 2 weeks
**Cost**: $8,000

## Approval
- [ ] Product Owner
- [ ] Technical Lead
- [ ] Project Manager

## Decision
☐ Approved  ☐ Rejected  ☐ Deferred

**Reason**: _____________________

Review & Approval Workflows
Requirements Review Checklist

Content Review:

 All requirements follow quality attributes
 Business rules clearly documented
 Assumptions explicitly stated
 Constraints identified
 Dependencies mapped
 Acceptance criteria defined

Technical Review:

 Technically feasible
 Integration points identified
 Performance requirements realistic
 Security requirements addressed
 Scalability considered

Business Review:

 Aligned with business objectives
 Business value clear
 Stakeholder needs addressed
 Priorities appropriate
 Budget and timeline realistic
Approval Levels
Document Type	Approvers	Timeline
BRD	Business Owner, Product Manager, Finance	1 week
FRS	Technical Lead, Architect, BA	3 days
User Stories	Product Owner, Scrum Master	1 day
Change Requests	CCB, Affected Stakeholders	2-5 days
Communication Best Practices
Stakeholder Communication

Frequency:

Executive: Monthly status updates
Product Owner: Weekly sync
Development Team: Daily standup, sprint ceremonies
End Users: Milestone demos, UAT sessions

Communication Channels:

Formal: Email, official documents, presentations
Informal: Chat (Slack, Teams), quick calls
Collaborative: Workshops, working sessions
Broadcast: Newsletters, town halls
Meeting Best Practices

Before Meeting:

Clear agenda sent 24 hours ahead
Pre-read materials shared
Objectives defined
Right participants invited

During Meeting:

Start and end on time
Follow agenda
Take notes and action items
Encourage participation
Park off-topic items

After Meeting:

Share notes within 24 hours
Distribute action items with owners and due dates
Follow up on commitments
Collaboration Techniques
Hybrid Team Collaboration

Challenges:

Time zone differences
Communication gaps
Tool fragmentation
Cultural differences

Solutions:

Overlap hours for real-time collaboration
Async communication (Lark, Notion)
Single source of truth for documentation
Regular video calls for relationship building
Clear documentation of decisions
Conflict Resolution

When stakeholders disagree:

Understand Both Perspectives

Listen actively to each side
Ask clarifying questions
Document concerns

Find Common Ground

Identify shared objectives
Focus on business value
Separate positions from interests

Explore Options

Brainstorm alternatives
Consider compromises
Evaluate trade-offs

Use Data

Customer feedback
Analytics
Competitive analysis
Cost-benefit analysis

Escalate if Needed

Document the conflict
Present options with pros/cons
Let decision-maker decide
Accept and move forward
Common Pitfalls & How to Avoid
Pitfall 1: Gold Plating

Problem: Adding unnecessary features Solution: Always tie requirements to business value, challenge "nice-to-haves"

Pitfall 2: Scope Creep

Problem: Uncontrolled growth of requirements Solution: Formal change management process, clear scope boundaries

Pitfall 3: Analysis Paralysis

Problem: Over-analyzing, never finishing Solution: Time-box analysis, "good enough" vs. perfect, iterative approach

Pitfall 4: Assuming Understanding

Problem: Not validating requirements with stakeholders Solution: Always confirm understanding, use prototypes, get sign-off

Pitfall 5: Ignoring Non-Functional Requirements

Problem: Focus only on features, ignore performance, security Solution: Explicitly elicit NFRs, include in DoD

Pitfall 6: Poor Documentation

Problem: Incomplete, outdated, or unclear documentation Solution: Documentation standards, version control, regular reviews

Pitfall 7: Weak Stakeholder Engagement

Problem: Stakeholders not involved or committed Solution: Regular communication, show value, involve in decisions

Continuous Improvement
Retrospectives

After Each Project/Sprint:

What went well?
What could be improved?
What will we do differently?
Action items for improvement
Metrics to Track

Requirements Quality:

% requirements changed after approval
defects traced to requirements
Requirements review cycle time

Stakeholder Satisfaction:

Survey scores
Feedback themes
Engagement levels

Delivery:

% requirements delivered on time
% requirements delivered in scope
Rework rate
Professional Development

Certifications:

CBAP (Certified Business Analysis Professional)
PMI-PBA (Professional in Business Analysis)
IIBA Certifications
Agile certifications (CSPO, CSM)

Continuous Learning:

Industry conferences
Webinars and workshops
Professional communities
Reading (BABOK, industry blogs)
Tools & Templates
Recommended Tools

Documentation:

Lark Docs (collaborative)
Notion (knowledge base)
Confluence (enterprise)

Diagrams:

Figma (UI/UX)
Miro (collaboration)
Lucidchart (process flows)
Mermaid (code-based diagrams)

Requirements Management:

Jira (Agile)
Azure DevOps
Lark Base (flexible)

Communication:

Lark (all-in-one)
Slack/Teams (chat)
Zoom (video)
References
BABOK® Guide (IIBA)
PMI-PBA Handbook
Agile Extension to BABOK®
IEEE 29148 Standards
Requirements Engineering by Klaus Pohl
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