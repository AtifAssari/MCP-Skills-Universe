---
rating: ⭐⭐
title: user story writing
url: https://skills.sh/danhvb/my-ba-skills/user-story-writing
---

# user story writing

skills/danhvb/my-ba-skills/User Story Writing
User Story Writing
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'User Story Writing'
SKILL.md
User Story Writing Skill
Purpose

Write clear, valuable user stories that communicate requirements in Agile/Hybrid environments and guide development teams.

When to Use
Agile or Hybrid projects
Sprint planning and backlog refinement
Breaking down features into implementable chunks
Communicating requirements to development teams
User Story Format
Basic Template
As a [user role]
I want [goal/desire]
So that [benefit/value]

Enhanced Template (Recommended)
Title: [Short, descriptive title]

As a [user role]
I want [goal/desire]
So that [benefit/value]

Acceptance Criteria:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

Notes:
[Additional context, wireframes, business rules]

Definition of Done:
- [ ] Code complete and peer reviewed
- [ ] Unit tests written and passing
- [ ] Integration tests passing
- [ ] Acceptance criteria met
- [ ] Documentation updated

INVEST Criteria

Every user story should be:

Independent: Can be developed and delivered independently
Negotiable: Details can be discussed and refined
Valuable: Delivers value to users or business
Estimable: Team can estimate effort required
Small: Can be completed within one sprint
Testable: Clear acceptance criteria for testing
Examples by Domain
E-commerce Examples

Story 1: Guest Checkout

Title: Guest Checkout Without Account Creation

As a first-time customer
I want to complete my purchase without creating an account
So that I can checkout quickly without friction

Acceptance Criteria:
- Given I have items in my cart
  When I click "Checkout as Guest"
  Then I can enter shipping and payment info without login
- Given I complete guest checkout
  When I receive order confirmation
  Then I see an option to create an account
- Given my order total is over $5000
  When I try to checkout as guest
  Then I am required to create an account for security

Business Rules:
- Guest checkout not available for orders > $5000
- Email required for order confirmation
- Guest orders linked to email for future reference

Story Points: 8
Priority: Must Have
Sprint: Sprint 3


Story 2: Real-time Shipping Calculation

Title: Real-time Shipping Cost Display

As a customer
I want to see shipping costs before entering payment information
So that I know the total cost upfront and avoid surprises

Acceptance Criteria:
- Given I enter a valid shipping address
  When I proceed to shipping method selection
  Then I see all available shipping options with costs
- Given I select a shipping method
  When I view the order summary
  Then the shipping cost is included in the total
- Given the shipping API is unavailable
  When I try to calculate shipping
  Then I see a fallback message with estimated costs

Technical Notes:
- Integrate with ShipStation API
- Cache shipping rates for 5 minutes
- Timeout after 5 seconds, show fallback

Story Points: 5
Priority: Must Have
Sprint: Sprint 3

CRM Examples

Story 3: Automatic Lead Scoring

Title: Automatic Lead Scoring Based on Behavior

As a sales manager
I want leads to be automatically scored based on their activities
So that my team focuses on the most qualified prospects

Acceptance Criteria:
- Given a lead visits the pricing page
  When the activity is tracked
  Then 15 points are added to their score
- Given a lead's score reaches 60
  When the score is updated
  Then the lead is automatically marked as MQL
- Given a lead's score reaches 75
  When the score is updated
  Then the lead is assigned to a sales rep and rep is notified
- Given I view a lead record
  When I look at the lead score
  Then I can see the scoring breakdown (why this score)

Scoring Rules:
- Demographic: Job title (0-20), Company size (0-15), Industry (0-5)
- Behavioral: Pricing page (15), Whitepaper (10), Webinar (15), Demo request (25)

Story Points: 13
Priority: Must Have
Sprint: Sprint 5

Mobile/Web Examples

Story 4: Offline Order Viewing

Title: View Orders Offline in Mobile App

As a mobile app user
I want to view my order history when offline
So that I can check order details without internet connection

Acceptance Criteria:
- Given I have previously viewed orders while online
  When I open the app offline
  Then I can see my cached order history
- Given I am offline
  When I try to view order details
  Then I see the last synced information with "offline" indicator
- Given I regain internet connection
  When the app detects connectivity
  Then order data is automatically refreshed in background

Technical Notes:
- Cache last 50 orders in local storage
- Use SQLite for offline storage
- Sync on app foreground if connected

Story Points: 8
Priority: Should Have
Sprint: Sprint 7

ERP Examples

Story 5: Multi-level Purchase Approval

Title: Multi-level Purchase Order Approval Workflow

As a procurement manager
I want purchase orders to route through appropriate approval levels
So that spending is controlled according to company policy

Acceptance Criteria:
- Given a PO is created for $1K-$10K
  When the PO is submitted
  Then it routes to department manager for approval
- Given a PO is created for $10K-$50K
  When the PO is submitted
  Then it routes to department manager, then finance director
- Given a PO is created for >$50K
  When the PO is submitted
  Then it routes to department manager, finance director, then CFO
- Given an approver is out of office
  When a PO requires their approval
  Then it automatically routes to their designated backup
- Given an approver rejects a PO
  When the rejection is submitted
  Then the requester is notified with rejection reason

Approval Matrix:
- $0-$1K: Auto-approved
- $1K-$10K: Department Manager
- $10K-$50K: Department Manager → Finance Director
- >$50K: Department Manager → Finance Director → CFO

Story Points: 13
Priority: Must Have
Sprint: Sprint 4

CDP Examples

Story 6: Customer Identity Resolution

Title: Unify Customer Profiles Across Channels

As a marketing analyst
I want customer data from web, mobile, and CRM to be unified
So that I have a complete view of each customer

Acceptance Criteria:
- Given a customer logs in on web and mobile with same email
  When identity resolution runs
  Then both profiles are merged into single customer record
- Given a customer has multiple emails
  When I manually link the profiles
  Then all activities are consolidated under primary profile
- Given profiles are merged
  When I view the customer record
  Then I see all touchpoints across channels in timeline
- Given a merge conflict occurs (different names, addresses)
  When the system detects conflict
  Then it flags for manual review

Matching Rules:
- Email (exact match) - High confidence
- Phone + Name (fuzzy match) - Medium confidence
- Cookie ID + Email domain - Low confidence

Story Points: 21
Priority: Must Have
Sprint: Sprint 2-3 (2 sprints)

Story Hierarchy
Epic → Feature → User Story → Task

Epic: Large body of work (multiple sprints)

Epic: Mobile App Customer Self-Service
Goal: Enable customers to manage accounts via mobile app
Timeline: Q1 2026
Stories: 25-30 stories


Feature: Group of related stories (1-3 sprints)

Feature: Order Management in Mobile App
Stories: View orders, Track shipments, Initiate returns
Sprint: Sprint 5-6


User Story: Single piece of functionality (1 sprint)

Story: View Order History
Tasks: API integration, UI development, Offline caching
Sprint: Sprint 5


Task: Technical implementation step (hours/days)

Task: Implement order list API endpoint
Estimate: 4 hours

Acceptance Criteria Formats
Given-When-Then (Gherkin)
Given [context/precondition]
When [action/event]
Then [expected outcome]


Example:

Given I am a logged-in customer
When I click "View Orders"
Then I see a list of my orders sorted by date (newest first)

Checklist Format
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3


Example:

- [ ] Order list displays order number, date, total, status
- [ ] Orders are paginated (20 per page)
- [ ] User can filter by status (All, Processing, Shipped, Delivered)
- [ ] User can search by order number
- [ ] Clicking an order opens order details

Scenario-Based
Scenario 1: [Happy path]
Scenario 2: [Alternative path]
Scenario 3: [Error case]

Story Splitting Techniques
When a story is too large (>13 points), split by:

1. Workflow Steps

Original: "User can complete checkout"
Split: "Enter shipping info", "Select shipping method", "Enter payment", "Review order"

2. Business Rules

Original: "Calculate shipping costs"
Split: "Standard shipping", "Express shipping", "International shipping"

3. CRUD Operations

Original: "Manage products"
Split: "Create product", "Update product", "Delete product", "View products"

4. Data Variations

Original: "Import customer data"
Split: "Import from CSV", "Import from Excel", "Import from API"

5. Platforms

Original: "Mobile app checkout"
Split: "iOS checkout", "Android checkout"

6. Simple/Complex

Original: "Search products"
Split: "Basic keyword search", "Advanced filters", "Faceted search"
Story Estimation
Story Points (Fibonacci: 1, 2, 3, 5, 8, 13, 21)
1 point: Trivial change (few hours)
2 points: Simple feature (half day)
3 points: Straightforward feature (1 day)
5 points: Moderate complexity (2-3 days)
8 points: Complex feature (3-5 days)
13 points: Very complex (5-8 days) - consider splitting
21+ points: Too large - must split
T-Shirt Sizing (Alternative)
XS: 1-2 points
S: 3-5 points
M: 8 points
L: 13 points
XL: 21+ points (split required)
Definition of Ready (DoR)

Story is ready for sprint when:

 User story follows INVEST criteria
 Acceptance criteria are clear and testable
 Dependencies identified and resolved
 Wireframes/mockups available (if UI work)
 Business rules documented
 Story estimated by team
 Priority assigned
 Technical approach discussed
Definition of Done (DoD)

Story is complete when:

 Code complete and peer reviewed
 Unit tests written (>80% coverage)
 Integration tests passing
 All acceptance criteria met
 Manual testing completed
 Documentation updated
 Deployed to staging environment
 Product owner approved
Best Practices

✅ Do:

Write from user perspective
Focus on value, not implementation
Keep stories small and focused
Include clear acceptance criteria
Involve the team in writing stories
Refine stories before sprint planning
Link stories to epics and features

❌ Don't:

Write technical tasks as user stories
Make stories too large (>13 points)
Skip acceptance criteria
Write vague or ambiguous stories
Include implementation details
Create dependencies between stories in same sprint
Tools
Lark
Use Lark Base for backlog management
Create story template with custom fields
Link stories to epics and sprints
Track story status and progress
Notion
Create user story database
Use kanban board for sprint planning
Link stories to requirements and test cases
Template for consistent story format
Common Patterns
E-commerce
As a customer, I want [shopping/checkout feature]
As an admin, I want [product/order management]
As a merchant, I want [analytics/reporting]
CRM
As a sales rep, I want [lead/opportunity management]
As a manager, I want [pipeline/forecasting]
As a marketer, I want [campaign/automation]
ERP
As a user, I want [process automation]
As an approver, I want [workflow management]
As an admin, I want [configuration/setup]
Mobile/Web
As a mobile user, I want [on-the-go features]
As a user, I want [responsive/accessible UI]
As a user, I want [offline capabilities]
Next Steps

After writing user stories:

Refine with team during backlog grooming
Create acceptance criteria (see acceptance-criteria skill)
Estimate during planning poker
Break into technical tasks
Link to test cases for UAT
References
Mike Cohn - User Stories Applied
INVEST Criteria - Bill Wake
Agile Alliance - User Story Guidelines
Scrum Guide - Product Backlog Management
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