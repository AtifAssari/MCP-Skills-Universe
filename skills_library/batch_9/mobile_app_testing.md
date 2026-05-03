---
title: mobile-app-testing
url: https://skills.sh/aj-geddes/useful-ai-prompts/mobile-app-testing
---

# mobile-app-testing

skills/aj-geddes/useful-ai-prompts/mobile-app-testing
mobile-app-testing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill mobile-app-testing
Summary

Comprehensive testing strategies for iOS and Android mobile apps across unit, UI, integration, and performance layers.

Covers unit testing with Jest, component testing with React Testing Library, and UI automation using Detox, Appium, XCTest, and Espresso
Includes performance testing, regression testing, and integration testing with backend services
Provides best practices for test isolation, mocking, meaningful naming, and >80% code coverage targets
Emphasizes testing on real devices, critical user flows, and both success and failure paths
SKILL.md
Mobile App Testing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive testing strategies for mobile applications including unit tests, UI tests, integration tests, and performance testing.

When to Use
Creating reliable mobile applications with test coverage
Automating UI testing across iOS and Android
Performance testing and optimization
Integration testing with backend services
Regression testing before releases
Quick Start

Minimal working example:

// Unit test with Jest
import { calculate } from "../utils/math";

describe("Math utilities", () => {
  test("should add two numbers", () => {
    expect(calculate.add(2, 3)).toBe(5);
  });

  test("should handle negative numbers", () => {
    expect(calculate.add(-2, 3)).toBe(1);
  });
});

// Component unit test
import React from "react";
import { render, screen } from "@testing-library/react-native";
import { UserProfile } from "../components/UserProfile";

describe("UserProfile Component", () => {
  test("renders user name correctly", () => {
    const mockUser = { id: "1", name: "John Doe", email: "john@example.com" };
    render(<UserProfile user={mockUser} />);

    expect(screen.getByText("John Doe")).toBeTruthy();
  });
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
React Native Testing with Jest & Detox	React Native Testing with Jest & Detox
iOS Testing with XCTest	iOS Testing with XCTest
Android Testing with Espresso	Android Testing with Espresso
Performance Testing	Performance Testing
Best Practices
✅ DO
Write tests for business logic first
Use dependency injection for testability
Mock external API calls
Test both success and failure paths
Automate UI testing for critical flows
Run tests on real devices
Measure performance on target devices
Keep tests isolated and independent
Use meaningful test names
Maintain >80% code coverage
❌ DON'T
Skip testing UI-critical flows
Use hardcoded test data
Ignore performance regressions
Test implementation details
Make tests flaky or unreliable
Skip testing on actual devices
Ignore accessibility testing
Create interdependent tests
Test without mocking APIs
Deploy untested code
Weekly Installs
520
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass