---
title: test-data-generation
url: https://skills.sh/aj-geddes/useful-ai-prompts/test-data-generation
---

# test-data-generation

skills/aj-geddes/useful-ai-prompts/test-data-generation
test-data-generation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill test-data-generation
SKILL.md
Test Data Generation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Test data generation creates realistic, consistent, and maintainable test data for automated testing. Well-designed test data reduces test brittleness, improves readability, and makes it easier to create diverse test scenarios.

When to Use
Creating fixtures for integration tests
Generating fake data for development databases
Building test data with complex relationships
Creating realistic user inputs for testing
Seeding test databases
Generating edge cases and boundary values
Building reusable test data factories
Quick Start

Minimal working example:

// tests/factories/userFactory.js
const { faker } = require("@faker-js/faker");

class UserFactory {
  static build(overrides = {}) {
    return {
      id: faker.string.uuid(),
      email: faker.internet.email(),
      firstName: faker.person.firstName(),
      lastName: faker.person.lastName(),
      age: faker.number.int({ min: 18, max: 80 }),
      phone: faker.phone.number(),
      address: {
        street: faker.location.streetAddress(),
        city: faker.location.city(),
        state: faker.location.state(),
        zip: faker.location.zipCode(),
        country: "USA",
      },
      role: "user",
      isActive: true,
      createdAt: faker.date.past(),
      ...overrides,
    };
  }
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Factory Pattern for Test Data	Factory Pattern for Test Data
Builder Pattern for Complex Objects	Builder Pattern for Complex Objects
Fixtures for Integration Tests	Fixtures for Integration Tests
Realistic Data Generation	Realistic Data Generation
Best Practices
✅ DO
Use faker libraries for realistic data
Create reusable factories for common objects
Make factories flexible with overrides
Generate unique values where needed (emails, IDs)
Use builders for complex object construction
Create fixtures for integration test setup
Generate edge cases (empty strings, nulls, boundaries)
Keep test data deterministic when possible
❌ DON'T
Hardcode test data in multiple places
Use production data in tests
Generate truly random data for reproducible tests
Create overly complex factory hierarchies
Ignore data relationships and constraints
Generate massive datasets for simple tests
Forget to clean up generated data
Use the same test data for all tests
Weekly Installs
294
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