---
rating: ⭐⭐
title: requirements validation
url: https://skills.sh/danhvb/my-ba-skills/requirements-validation
---

# requirements validation

skills/danhvb/my-ba-skills/Requirements Validation
Requirements Validation
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Requirements Validation'
SKILL.md
Requirements Validation Skill
Purpose

Ensure that the requirements are correct, complete, consistent, and actually solve the business problem before development begins. "Building the right thing" vs. "Building the thing right".

Verification vs. Validation
Verification: "Are we building the product right?" (Does the Requirement meet quality standards?)
Validation: "Are we building the right product?" (Does the Requirement solve the user's need?)
Key Validation Techniques
1. Peer Review / Walkthroughs
Process: Informal or semi-formal review with colleagues (Devs, other BAs).
Goal: Find logic errors, ambiguities, and missing edge cases.
Checklist:
Is it clear?
Is it testable?
Is it feasible?
2. Stakeholder Inspections / Sign-off
Process: Formal review with Business Owners.
Goal: Approval to proceed.
Method: Don't just read the doc. Walk through scenarios/examples.
3. Prototyping
Method: Show, don't tell. Use wireframes or mockups.
Goal: Validate UI/UX requirements. "Is this what you imagined?"
4. Acceptance Criteria Review
Method: Review "Given-When-Then" scenarios.
Goal: Ensure the requirement is specific enough to be tested.
Requirements Traceability Matrix (RTM)
Purpose

Link Requirements to their origin and downstream deliverables.

Forward Traceability: Requirement → Design → Code → Test. (Ensures everything required is built).
Backward Traceability: Test → Requirement → Business Goal. (Ensures no "Gold Plating" / unnecessary features).
RTM Template
Req ID	Description	Source (Stakeholder)	Business Goal	Design Doc	Test Case ID	Status
FR-01	Guest Checkout	Marketing VP	Increase Conv	DD-Checkout	TC-001, 002	Implemented
FR-02	Apple Pay	CEO	Mobile Strategy	DD-Payment	TC-005	Approved
FR-03	3D Secure	Compliance	Legal Reqs	DD-Security	TC-010	Tested
Quality Checklist (INVEST)

For User Stories:

Independent
Negotiable
Valuable
Estimable
Small
Testable
Handling Validation Issues
Ambiguity: "System must be fast."
Fix: "System must load in < 2s."
Conflict: Stakeholder A wants Blue, B wants Red.
Fix: Facilitate negotiation or escalate to Sponsor.
Incompleteness: Missing error states.
Fix: Ask "What happens if this fails?"
Output
Validated Requirements Package: Clean, approved docs.
Sign-off Artifact: Email or digital signature approving the scope.
Updated Traceability Matrix.
Tools
Jira (Linking Stories to Epics/Tests).
Excel/Lark Base (RTM).
Confluence/Lark Docs (Approvals).
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