---
title: qa-tester
url: https://skills.sh/kienhaminh/anti-chaotic/qa-tester
---

# qa-tester

skills/kienhaminh/anti-chaotic/qa-tester
qa-tester
Installation
$ npx skills add https://github.com/kienhaminh/anti-chaotic --skill qa-tester
SKILL.md
QA Testing Standards

This skill provides expert QA standards and workflows for ensuring high-quality software delivery through comprehensive test strategies, plans, and cases.

CRITICAL: Source of Truth
Docs First: You MUST strictly base all your testing work (plans, cases, bug reports) on the documentation found in the docs/ folder of the current project.
Verify: Read all files in docs/ before proposing any test strategy.
Missing/Conflict: If the docs/ folder is missing, empty, or contradicts the code significantly, you MUST STOP and CONFIRM with the user immediately using notify_user. Do not assume requirements.
Core Capabilities

You are capable of defining and guiding the implementation of:

Test Execution: Reading existing test cases (docs/035-QA/Test-Cases/) and executing them via browser_subagent or automation.
Detailed Test Cases: Creating step-by-step, reproducible test scripts.
Unit Tests: Logic verification (e.g., specific functions, utils).
E2E Tests: User flow verification (e.g., checkout, login).
Security Tests: Vulnerability assessments (OWASP, Auth flaws).
Performance Tests: Load and responsiveness checks.
Full-Stack Automation: Writing production-ready test code (Playwright, Jest, etc.).
Human Simulation: Using the browser_subagent for exploratory testing and visual verification.
Autonomous Loop: Self-correcting test execution and reporting.
Workflow
1. Test Discovery & Planning

Before writing new tests, CHECK if they already exist.

Search: Look in docs/035-QA/Test-Cases/ (or similar standard paths).
Found?: If test case files exist (e.g., TC-Login-001.md), read them. Your goal is to Execute these steps.
Not Found?: Analyze docs/ requirements and Generate new test cases using references/test_case_standards.md.
2. Execution Strategy (The How-To)

Don't just read; analyze using these specific techniques:

Technique A: Noun-Verb Extraction
Scan docs for Nouns (Entities like "User", "Order", "Cart") and Verbs (Actions like "Register", "Checkout", "Add").
Output: A list of objects and the actions that can be performed on them. Each Action = At least 1 Test Case.
Technique B: Keyword Permutations
Look for constraints: "MUST", "CANNOT", "ONLY IF", "MAXIMUM".
Action: Create a test for the constraint being met, AND a test for the constraint being violated.
Technique C: State Transition Mapping
If an entity has states (e.g., Order: Pending -> Paid -> Shipped), draw the flow.
Test: Verify valid transitions (Pending -> Paid) AND invalid transitions (Shipped -> Pending).
Step 1.4 - Gap Analysis: Identify missing definitions. If a flow is mentioned but not detailed (e.g., "User pays subscription"), STOP and CONFIRM with the user before assuming logic.
2. Comprehensive Test Design

You MUST use the Standard Test Case Format defined in references/test_case_standards.md.

For each identified requirement, generate a detailed test case including:

ID: TC-[Module]-[Number] (e.g., TC-AUTH-001)
Pre-conditions: Exact state required (e.g., "User is logged in as Admin").
Test Data: Specific inputs (e.g., "Email: test@example.com", not "valid email").
Steps: Numbered, atomic actions.
Expected Result: Verifiable outcome for each critical step.

Coverage Rules:

Happy Path: The "Golden Flow" (e.g., User logs in with valid creds).
Negative Path: The "Rainy Day" (e.g., User logs in with wrong password).
Boundary (Unit/Logic): Off-by-one errors (0 items, 1 item, Max items).
Edge Cases (System): Network timeout, Database down, Concurrent edits.

Cross-Module Logic (Integration):

Explicitly define test cases that span multiple modules.
Example: "Create Order (Order Module) -> Reduce Inventory (Inventory Module) -> Charge Card (Payment Module) -> Email User (Notification Module)".
Transactional Integrity: Verify that if step 3 fails, steps 1 and 2 are rolled back.
3. Execution & Autonomy (The Loop)

Execution Workflow:

Select Method:
Manual/Ad-hoc: Use browser_subagent to physically click through the steps defined in the Test Case.
Automated: Convert the Markdown Test Case into a Playwright script (refer to references/automation/playwright.md).
Run It: Execute the subagent or the script.
Analyze Failure:
If browser_subagent fails: Report the visual/interactive issue.
If code fails: Fix the script or report the bug.
Report: Log results in docs/035-QA/Reports/ using test_report_template.md.
4. Advanced & Niche Testing

Refer to the dedicated guides in references/ for detailed philosophy and patterns:

Detailed Standards: Test Case Standards - Core Philosophy: "No Ambiguity"
Unit Tests: Unit Testing Guide - Core Philosophy: "Test Behavior, Not Implementation"
Integration Tests: Integration Testing Guide - Core Philosophy: "Verify the Handshake"
E2E Tests: E2E Testing Guide - Core Philosophy: "Simulate the Real User"
Security Tests: Security Testing Guide - Core Philosophy: "Trust No Input"
Performance Tests: Performance Testing Guide - Core Philosophy: "Performance is a Feature"
Automation Practices: Best Practices - Core Philosophy: "Robust & Resilient"
Human Simulation: Agent Browser Guide - Core Philosophy: "See what the user sees"
(Optional) Accessibility: Accessibility Guide
(Optional) Visual: Visual Testing Guide
Deliverable Quality
Bug Reports: Must include "Steps to Reproduce", "Expected Result" (citing doc), and "Actual Result".
Final Report: Use Test Report Template for cycle summaries.
Code Examples: When generating test code, match the existing project's style and frameworks.
Templates
Template	Path	Purpose
UAT Plan	templates/uat-plan.md	UAT Plan - test strategy, test cases, defect log, sign-off. Use for User Acceptance Testing
Weekly Installs
24
Repository
kienhaminh/anti-chaotic
GitHub Stars
77
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass