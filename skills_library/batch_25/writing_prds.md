---
title: writing-prds
url: https://skills.sh/nguyenhuuca/assessment/writing-prds
---

# writing-prds

skills/nguyenhuuca/assessment/writing-prds
writing-prds
Installation
$ npx skills add https://github.com/nguyenhuuca/assessment --skill writing-prds
SKILL.md
Writing PRDs
Workflows
 Define Goals: Articulate business goals and success metrics
 Identify Stakeholders: List all relevant stakeholders
 Draft User Stories: Capture user needs
 Detail Requirements: List functional and non-functional requirements
 Save Artifact: Save to ./artifacts/prd_[feature].md
 Review: Conduct stakeholder review
PRD Structure
Overview: What and why
Goals & Success Metrics: How we measure success
User Stories: Who benefits and how
Requirements: What must be built
Out of Scope: What we're NOT building
Timeline: Key milestones
User Story Format
As a [role],
I want [feature],
So that [benefit].

Example
As a registered user,
I want to reset my password via email,
So that I can regain access to my account if I forget it.

Acceptance Criteria

Use Given/When/Then format:

Given I am on the login page
When I click "Forgot Password"
Then I see a form to enter my email

Given I enter a valid registered email
When I submit the form
Then I receive a password reset email within 5 minutes

INVEST Criteria

Good user stories are:

Independent: Can be developed separately
Negotiable: Details can be discussed
Valuable: Delivers user value
Estimable: Can be sized
Small: Fits in a sprint
Testable: Has clear acceptance criteria
Resources
PRD Template
Weekly Installs
10
Repository
nguyenhuuca/assessment
GitHub Stars
24
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass