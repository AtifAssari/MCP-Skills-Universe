---
title: test_driven_agent
url: https://skills.sh/cityfish91159/maihouses/test_driven_agent
---

# test_driven_agent

skills/cityfish91159/maihouses/test_driven_agent
test_driven_agent
Installation
$ npx skills add https://github.com/cityfish91159/maihouses --skill test_driven_agent
SKILL.md
Test Driven Agent Protocol
1. The Red-Green-Refactor Cycle
Red: Write a test that fails (demonstrating the bug or missing feature).
Agent Note: If fixing a bug, YOU MUST reproduce it with a test first.
Green: Write the minimal code to pass the test.
Refactor: Clean up the code while ensuring tests still pass.
2. Test Coverage Requirements
Happy Path: The "standard" usage case.
Sad Path: Error states, network failures, invalid inputs.
Edge Cases: Empty lists, max values, concurrent actions.
3. Self-Healing Mandate

If a test fails after your changes:

DO NOT delete the test.
DO NOT comment out the assertion.
DO NOT change the test expectation to match the buggy result (unless the spec changed).
DO: Fix the implementation logic until the test passes.
4. Integration vs Unit
Unit: Mock external dependencies (Supabase, API). Fast, isolated.
Integration: Test the hook or service with realistic (mocked) data flows.
5. Verification Checklist
 Did I write a test case for this requirement?
 Did I run npm test <filename>?
 Did I check specifically for regression in related headers/components?
Weekly Installs
17
Repository
cityfish91159/maihouses
GitHub Stars
1
First Seen
Jan 25, 2026