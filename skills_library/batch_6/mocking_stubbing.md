---
title: mocking-stubbing
url: https://skills.sh/aj-geddes/useful-ai-prompts/mocking-stubbing
---

# mocking-stubbing

skills/aj-geddes/useful-ai-prompts/mocking-stubbing
mocking-stubbing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill mocking-stubbing
SKILL.md
Mocking and Stubbing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Mocking and stubbing are essential techniques for isolating units of code during testing by replacing dependencies with controlled test doubles. This enables fast, reliable, and focused unit tests that don't depend on external systems like databases, APIs, or file systems.

When to Use
Isolating unit tests from external dependencies
Testing code that depends on slow operations (DB, network)
Simulating error conditions and edge cases
Verifying interactions between objects
Testing code with non-deterministic behavior (time, randomness)
Avoiding expensive operations in tests
Testing error handling without triggering real failures
Quick Start

Minimal working example:

// services/UserService.ts
import { UserRepository } from "./UserRepository";
import { EmailService } from "./EmailService";

export class UserService {
  constructor(
    private userRepository: UserRepository,
    private emailService: EmailService,
  ) {}

  async createUser(userData: CreateUserDto) {
    const user = await this.userRepository.create(userData);
    await this.emailService.sendWelcomeEmail(user.email, user.name);
    return user;
  }

  async getUserStats(userId: string) {
    const user = await this.userRepository.findById(userId);
    if (!user) throw new Error("User not found");

    const orderCount = await this.userRepository.getOrderCount(userId);
    return { ...user, orderCount };
  }
}

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Jest Mocking (JavaScript/TypeScript)	Jest Mocking (JavaScript/TypeScript)
Python Mocking with unittest.mock	Python Mocking with unittest.mock
Mockito for Java	Mockito for Java
Advanced Mocking Patterns	Advanced Mocking Patterns
Best Practices
✅ DO
Mock external dependencies (DB, API, file system)
Use dependency injection for easier mocking
Verify important interactions with mocks
Reset mocks between tests
Mock at the boundary (repositories, services)
Use spies for partial mocking when needed
Create reusable mock factories
Test both success and failure scenarios
❌ DON'T
Mock everything (don't mock what you own)
Over-specify mock interactions
Use mocks in integration tests
Mock simple utility functions
Create complex mock hierarchies
Forget to verify mock calls
Share mocks between tests
Mock just to make tests pass
Weekly Installs
265
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