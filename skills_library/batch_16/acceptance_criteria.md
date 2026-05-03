---
title: acceptance criteria
url: https://skills.sh/danhvb/my-ba-skills/acceptance-criteria
---

# acceptance criteria

skills/danhvb/my-ba-skills/Acceptance Criteria
Acceptance Criteria
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Acceptance Criteria'
SKILL.md
Acceptance Criteria Skill
Purpose

Define clear, testable acceptance criteria that specify exactly when a requirement or user story is considered complete and working correctly.

When to Use
Writing user stories for Agile sprints
Defining requirements in FRS
Planning UAT test cases
Creating Definition of Done for features
Acceptance Criteria Formats
1. Given-When-Then (Gherkin)

Structure:

Given [precondition/context]
When [action/event]
Then [expected outcome]
And [additional outcome]


Example - Login:

Scenario: Successful login with valid credentials
Given I am on the login page
And I am a registered user with email "user@example.com"
When I enter "user@example.com" as email
And I enter "ValidPassword123" as password
And I click the "Sign In" button
Then I should be redirected to the dashboard
And I should see a welcome message "Welcome, John"
And my last login time should be updated

Scenario: Failed login with invalid password
Given I am on the login page
And I am a registered user
When I enter valid email
And I enter incorrect password
And I click the "Sign In" button
Then I should see error message "Invalid email or password"
And I should remain on the login page
And account lockout counter should increment

Scenario: Account lockout after 5 failed attempts
Given I am on the login page
And I have failed login 4 times
When I fail login a 5th time
Then my account should be locked for 30 minutes
And I should see message "Account locked. Try again in 30 minutes"
And I should receive a security alert email

2. Checklist Format

Example - Checkout:

## User Story: Guest Checkout

### Acceptance Criteria
- [ ] Guest can proceed to checkout without creating account
- [ ] Email field is required and validated
- [ ] Shipping address form includes: name, address, city, state, zip, country, phone
- [ ] All required fields show validation errors if empty on submit
- [ ] Address validation API is called and suggests corrections
- [ ] Shipping options are displayed with real-time prices
- [ ] Order summary shows all items, quantities, and prices
- [ ] Payment form accepts credit card information
- [ ] Order is created upon successful payment
- [ ] Confirmation page shows order number and details
- [ ] Confirmation email is sent within 1 minute
- [ ] Guest is offered option to create account after order

3. Scenario-Based

Example - Shopping Cart:

## User Story: Add to Cart

### Happy Path
- User selects product variant (size, color)
- User clicks "Add to Cart"
- Product is added to cart with correct quantity
- Cart icon updates with item count
- Mini cart shows added product confirmation
- User can continue shopping or go to cart

### Edge Cases
- Out of stock: "Add to Cart" button disabled, shows "Out of Stock"
- Limited stock: Shows "Only 3 left" warning
- Maximum quantity: "Only 5 per customer" message
- Already in cart: Updates quantity instead of adding duplicate
- Variant not selected: Prompts to select variant first

### Error Scenarios
- Network error: Shows "Unable to add. Please try again"
- Inventory changed: Shows "Sorry, this item is no longer available"
- Session expired: Redirects to login, preserves cart on return

Domain-Specific Examples
E-commerce: Payment Processing
Scenario: Successful credit card payment
Given I have items in my cart totaling $99.99
And I am on the payment page
When I enter valid card number "4242 4242 4242 4242"
And I enter expiration "12/27" and CVV "123"
And I click "Pay Now"
Then the payment should be processed successfully
And I should see order confirmation page
And I should receive confirmation email
And order status should be "Processing"

Scenario: Payment declined
Given I am on the payment page
When I enter a card that will be declined
And I click "Pay Now"
Then I should see "Payment declined. Please try another card"
And I should remain on payment page
And no order should be created
And no charge should be made

Scenario: 3D Secure authentication required
Given I am paying with a card requiring 3DS
When I submit payment
Then I should see 3D Secure popup
When I complete verification
Then payment should process normally

CRM: Lead Conversion
Scenario: Convert qualified lead to opportunity
Given I am viewing a lead with score >= 75
And lead status is "Qualified"
When I click "Convert to Opportunity"
Then I should see conversion dialog
And I should be able to create or select account
And new contact should be created
And new opportunity should be created with lead data
And original lead should be marked "Converted"
And conversion history should be logged

Scenario: Cannot convert unqualified lead
Given I am viewing a lead with score < 60
When I click "Convert to Opportunity"
Then I should see message "Lead must be qualified before conversion"
And conversion dialog should not open

ERP: Purchase Order Approval
Scenario: PO auto-approved under $1000
Given I create a purchase order for $500
When I submit the PO
Then PO status should be "Approved"
And I should see message "Auto-approved under $1,000 threshold"
And no approval notification should be sent

Scenario: PO routes to manager for approval
Given I create a purchase order for $5,000
When I submit the PO
Then PO status should be "Pending Approval"
And my manager should receive approval notification
And I should see message "Sent to manager for approval"

Scenario: Manager approves PO
Given I am a manager
And I have a pending PO for approval
When I click "Approve"
And I enter approval comments
Then PO status should change to "Approved"
And requestor should be notified
And PO should be sent to vendor

Mobile/Web: Offline Functionality
Scenario: View cached data offline
Given I have previously viewed my order history
And I am now offline
When I open the app
And I navigate to Order History
Then I should see cached orders
And I should see "Offline - Last updated: [timestamp]"
And I should not see loading spinner

Scenario: Attempt action that requires connectivity
Given I am offline
When I try to place a new order
Then I should see "You're offline. Connect to place order"
And I should have option to save cart for later
And action should not proceed

Scenario: Auto-sync when back online
Given I made changes while offline
When I regain internet connection
Then app should automatically sync changes
And I should see brief "Syncing..." indicator
And I should see "Up to date" when complete

Best Practices
Writing Good Acceptance Criteria

✅ Do:

Be specific and measurable
Cover happy path AND edge cases
Include error scenarios
Make each criterion independently testable
Use consistent language
Consider user perspective
Include data validation rules
Specify timing requirements (if applicable)

❌ Don't:

Be vague ("system should be fast")
Skip error handling
Assume implied knowledge
Make criteria too granular (test case level)
Forget about edge cases
Mix multiple features in one criterion
Testability Checklist
 Can QA write a test case from this?
 Is the expected outcome clear?
 Can we objectively say pass/fail?
 Are values specified (not "valid input")?
 Are timing requirements specified?
Completeness Checklist
 Happy path covered?
 Error cases covered?
 Edge cases covered?
 Empty/null states covered?
 Permission/access scenarios covered?
 Mobile/responsive scenarios covered?
Common Patterns
Form Validation
Given field X is empty
When user submits form
Then error "X is required" is shown below field X
And field X is highlighted in red
And form is not submitted

List/Search
Given there are N items matching criteria
When user searches for [criteria]
Then N results are displayed
And results are sorted by [default sort]
And each result shows [fields]

CRUD Operations
Create: Input validation, success message, list updates
Read: Display correct data, handle empty state
Update: Validate changes, show success, reflect changes
Delete: Confirm prompt, success message, item removed

Tools
Lark/Notion: Document criteria with user stories
Jira: Acceptance criteria field in story
Gherkin: Formal BDD syntax for automation
Cucumber/SpecFlow: Automated testing with Gherkin
Next Steps

After writing acceptance criteria:

Review with Product Owner
Review with QA for testability
Include in Definition of Ready
Use for UAT test case creation
References
Behavior Driven Development (BDD)
Gherkin Syntax Reference
User Story Mapping (Jeff Patton)
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