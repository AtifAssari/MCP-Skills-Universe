---
rating: ⭐⭐
title: test strategy design
url: https://skills.sh/danhvb/my-ba-skills/test-strategy-design
---

# test strategy design

skills/danhvb/my-ba-skills/Test Strategy Design
Test Strategy Design
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Test Strategy Design'
SKILL.md
Test Strategy Design Skill
Purpose

Enable the QA Lead Agent to define the overall approach to quality assurance for a project, ensuring all risks are mitigated through appropriate testing.

Test Pyramid Strategy

Based on Mike Cohn's Test Pyramid:

Unit Tests (70%): Component level, fast, isolated. (Dev responsibility)
Integration Tests (20%): API level, service interaction. (Dev/QA responsibility)
E2E / UI Tests (10%): User journey, slow, fragile. (QA responsibility)
Test Plan Components
1. Scope
In Scope: Modules, browsers (Chrome, Safari), devices (iOS, Android).
Out of Scope: Performance (unless specified), third-party system internals.
2. Testing Types
Functional: Sanity, Smoke, Regression.
Non-Functional: Performance, Security, Accessibility, Usability.
3. Environment Strategy
Dev: Unstable, for unit tests.
QA/Staging: Stable, mirror of Prod, for functional/regression.
Prod: For smoke tests / monitoring.
4. Data Strategy
Synthetic data generation?
Anonymized prod dump?
Hardcoded test users?
Automation Framework Design
Selection Criteria
Tech Stack: Playwright (JS/TS), Selenium (Java/Python), Cypress (JS).
CI/CD Integration: Github Actions, Jenkins.
Reporting: Allure, HTML reports.
Best Practices
Page Object Model (POM): Separation of page structure from tests.
Atomic Tests: Each test is independent.
Data Driven: Separate data from logic.
Risk-Based Testing

Prioritize testing based on:

Impact: What happens if this fails? (Financial loss, data loss?)
Probability: How likely is it to fail? (New complex code vs. old stable code).
Deliverables
Master Test Plan (MTP).
Test Case Suite.
Defect Reports.
Test Summary Report.
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