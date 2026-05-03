---
rating: ⭐⭐
title: test case creation
url: https://skills.sh/danhvb/my-ba-skills/test-case-creation
---

# test case creation

skills/danhvb/my-ba-skills/Test Case Creation
Test Case Creation
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Test Case Creation'
SKILL.md
Test Case Creation Skill
Purpose

Translate requirements into executable steps to verify the system works as expected. While QA executes tests, BAs often define the scenarios to ensure business logic is covered.

When to Use
During Requirements phase (to ensure testability).
UAT Planning (writing scripts for users).
Reviewing QA Test Plans (validation).
Anatomy of a Good Test Case
ID: Unique (e.g., TC-001).
Title: Concise summary.
Preconditions: Setup required (e.g., "User logged in").
Test Steps: Step-by-step actions using imperative verbs ("Click", "Enter", "Verify").
Test Data: Specific data used (e.g., "Email: test@example.com").
Expected Result: What should happen? (Specific).
Postconditions: State after test (e.g., "Order created in DB").
Types of BA Test Cases
1. Happy Path (Positive)

The standard flow working perfectly.

"User enters valid email/pass -> Logs in successfully."
2. Negative Path (Error Handling)

Trying to break it / Invalid inputs.

"User enters invalid email -> Shows error message 'Invalid format'."
3. Edge Cases (Boundary)

Testing limits.

"User enters exactly 255 characters (max) -> Accepted."
"User enters 256 characters -> Rejected."
4. Business Logic / Complex Flow

Multi-step scenarios.

"User adds item -> Apply Discount -> Remove Item -> Verify Total recalculates."
Test Case Template

Scenario: Apply Promo Code

ID	TC-PROMO-01
Description	Verify 'SUMMER20' gives 20% discount.
Preconditions	User has $100 item in cart.
Steps	1. Navigate to Cart.2. Enter 'SUMMER20' in promo field.3. Click 'Apply'.
Expected Result	1. Success message 'Code Applied'.2. Discount line shows -$20.00.3. Total is $80.00.
Traceability

Ensure every Test Case links back to a Requirement (FR).

TC-PROMO-01 <--> FR-CART-05 (Promo Codes).
Best Practices
One Verification per Test: Don't test 10 things in one case. If one fails, the whole case fails.
Be Specific: Don't say "Check result". Say "Verify text says 'Success'".
Clean Up: Tests should clean up data (Postconditions) so the next test isn't blocked.
Tools
Lark Base / Excel: Simple test tracking.
Jira / Zephyr / Xray: Integrated test management.
TestRail: Dedicated test tool.
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