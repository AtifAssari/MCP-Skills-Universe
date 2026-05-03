---
title: uat planning
url: https://skills.sh/danhvb/my-ba-skills/uat-planning
---

# uat planning

skills/danhvb/my-ba-skills/UAT Planning
UAT Planning
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'UAT Planning'
SKILL.md
UAT Planning Skill
Purpose

Plan and coordinate User Acceptance Testing (UAT) to ensure the solution meets business requirements and is ready for production deployment.

When to Use
Before production deployment
After development and QA testing complete
When business validation is required
For regulatory compliance
UAT Overview
What is UAT?

User Acceptance Testing is the final phase of testing where actual business users verify that the system meets their requirements and is fit for purpose.

UAT vs Other Testing
Testing Type	Who	Focus	When
Unit Testing	Developers	Code components	During development
Integration Testing	QA	System interfaces	After unit tests
System Testing	QA	End-to-end functionality	After integration
UAT	Business Users	Business requirements	Before go-live
Regression Testing	QA	No new defects	After changes
UAT Planning Process
1. UAT Strategy

Define:

Scope: What features/modules to test
Approach: Script-based, exploratory, or hybrid
Environment: UAT environment requirements
Data: Test data requirements
Timeline: Start/end dates, milestones
Resources: Testers, support

UAT Scope Example:

## In Scope
- New checkout flow (guest and registered)
- Payment processing (credit card, PayPal)
- Order confirmation and emails
- Order history viewing

## Out of Scope
- Admin functions (tested by IT)
- Existing functionality not changed
- Performance testing (separate test)

2. Entry Criteria

Before UAT begins:

 All development complete
 Unit and integration tests passing
 System testing complete with no critical bugs
 UAT environment set up and stable
 Test data prepared
 User credentials created
 UAT scripts reviewed and approved
 Training completed (if needed)
3. Exit Criteria

UAT is complete when:

 All critical and high-priority test cases passed
 No open critical or high-severity defects
 Medium/low defects documented with workarounds
 Sign-off from business stakeholders
 Go-live readiness confirmed
UAT Test Case Template
# Test Case: TC-UAT-001

**Feature**: Guest Checkout
**Priority**: High
**Prerequisite**: Products in cart, valid test credit card

## Test Steps

| Step | Action | Expected Result | Actual Result | Pass/Fail |
|------|--------|-----------------|---------------|-----------|
| 1 | Click "Checkout" with items in cart | Checkout page displays | | |
| 2 | Select "Checkout as Guest" | Email field displayed | | |
| 3 | Enter email "test@example.com" | Email accepted | | |
| 4 | Enter shipping address | Address validated | | |
| 5 | Select shipping method "Standard" | Shipping cost $5.99 shown | | |
| 6 | Enter card 4242-4242-4242-4242 | Card accepted | | |
| 7 | Click "Place Order" | Order confirmation displayed | | |
| 8 | Check email inbox | Confirmation email received | | |

## Test Data Required
- Product: "Test Product" - $29.99
- Credit Card: 4242424242424242, 12/25, 123
- Shipping Address: 123 Test St, San Francisco, CA 94102

## Notes
_Record any observations, issues, or deviations here_

**Tested By**: _____________ **Date**: _____________
**Result**: ☐ Pass ☐ Fail ☐ Blocked

UAT Execution Tracking
Daily Status Template
# UAT Daily Status - [Date]

## Summary
- Tests Planned: 50
- Tests Executed: 35
- Tests Passed: 30
- Tests Failed: 3
- Tests Blocked: 2

## Progress: 70% Complete

## Defects Raised Today
| ID | Severity | Summary | Status |
|----|----------|---------|--------|
| DEF-101 | High | Payment fails for Amex | Open |
| DEF-102 | Medium | Wrong shipping address format | Open |

## Blockers
1. UAT environment was down 2 hours (resolved)
2. Waiting for test credit card for PayPal

## Plan for Tomorrow
- Complete payment testing
- Start order management testing

Defect Severity
Severity	Definition	UAT Impact
Critical	System unusable, data loss	UAT blocked, immediate fix required
High	Major feature broken, no workaround	Must fix before go-live
Medium	Feature issues with workaround	Should fix, can go-live with workaround
Low	Minor issues, cosmetic	Nice to fix, doesn't block go-live
UAT Sign-off
Sign-off Template
# UAT Sign-off Document

**Project**: E-commerce Checkout Redesign
**UAT Period**: January 15-22, 2026
**Sign-off Date**: January 22, 2026

## Executive Summary
UAT for the checkout redesign has been completed. All critical functionality has been tested and approved.

## Test Summary
| Category | Total | Passed | Failed | Blocked |
|----------|-------|--------|--------|---------|
| Checkout Flow | 25 | 24 | 1 | 0 |
| Payment | 15 | 14 | 0 | 1 |
| Order Management | 10 | 10 | 0 | 0 |
| **Total** | **50** | **48** | **1** | **1** |

## Open Defects
| ID | Severity | Summary | Decision |
|----|----------|---------|----------|
| DEF-101 | Medium | Minor display issue on mobile | Go-live, fix in next sprint |

## Go/No-Go Recommendation
**☑ GO** - Recommended for production deployment

## Stakeholder Sign-off
| Name | Role | Signature | Date |
|------|------|-----------|------|
| John Smith | Business Owner | ___________ | |
| Mary Johnson | Product Manager | ___________ | |
| Sarah Lee | UAT Lead | ___________ | |

## Conditions/Notes
- DEF-101 to be fixed within 1 week post-launch
- Monitoring plan in place for first 48 hours
- Rollback plan documented and tested

Best Practices
Planning

✅ Do:

Involve business users early in planning
Create realistic test data
Allow buffer time for defect fixes
Train testers on new features
Document expected results clearly

❌ Don't:

Wait until last minute to start UAT
Use production data with sensitive info
Skip test case review
Underestimate time needed
Forget about regression testing
Execution

✅ Do:

Track progress daily
Triage defects quickly
Re-test after fixes
Document everything
Communicate blockers immediately

❌ Don't:

Let testers create ad-hoc tests only
Ignore "minor" issues
Skip re-testing after fixes
Delay communication of issues
Rush sign-off
Domain-Specific UAT
E-commerce
End-to-end purchase flow
Payment methods (all supported)
Shipping calculations
Promotional codes
Mobile checkout
ERP
Business process flows
Approval workflows
Report accuracy
Integration with other modules
Role-based access
CRM
Lead/opportunity workflows
Sales process stages
Email integrations
Report accuracy
Mobile access
Tools
Lark/Notion: Test case documentation
Jira/Azure DevOps: Defect tracking
TestRail/Zephyr: Test management
Lark Base: UAT tracking database
Next Steps

After UAT:

Final sign-off meeting
Go-live preparation
Production deployment
Post-go-live monitoring
Hypercare support
References
ISTQB Testing Standards
Agile Testing Quadrants
UAT Best Practices
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