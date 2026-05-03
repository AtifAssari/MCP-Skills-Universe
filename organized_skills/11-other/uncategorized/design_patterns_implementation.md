---
rating: ⭐⭐
title: design-patterns-implementation
url: https://skills.sh/aj-geddes/useful-ai-prompts/design-patterns-implementation
---

# design-patterns-implementation

skills/aj-geddes/useful-ai-prompts/design-patterns-implementation
design-patterns-implementation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill design-patterns-implementation
SKILL.md
Design Patterns Implementation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Apply proven design patterns to create maintainable, extensible, and testable code architectures.

When to Use
Solving common architectural problems
Making code more maintainable and testable
Implementing extensible plugin systems
Decoupling components
Following SOLID principles
Code reviews identifying architectural issues
Quick Start

Minimal working example:

class DatabaseConnection {
  private static instance: DatabaseConnection;
  private connection: any;

  private constructor() {
    this.connection = this.createConnection();
  }

  public static getInstance(): DatabaseConnection {
    if (!DatabaseConnection.instance) {
      DatabaseConnection.instance = new DatabaseConnection();
    }
    return DatabaseConnection.instance;
  }

  private createConnection() {
    return {
      /* connection logic */
    };
  }
}

// Usage
const db1 = DatabaseConnection.getInstance();
const db2 = DatabaseConnection.getInstance();
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Singleton Pattern	Singleton Pattern
Factory Pattern	Factory Pattern
Observer Pattern	Observer Pattern
Strategy Pattern	Strategy Pattern
Decorator Pattern	Decorator Pattern
Repository Pattern	Repository Pattern
Dependency Injection	Dependency Injection
Best Practices
✅ DO
Choose patterns that solve actual problems
Keep patterns simple and understandable
Document why patterns were chosen
Consider testability
Follow SOLID principles
Use dependency injection
Prefer composition over inheritance
❌ DON'T
Apply patterns without understanding them
Over-engineer simple solutions
Force patterns where they don't fit
Create unnecessary abstraction layers
Ignore team familiarity with patterns
Weekly Installs
387
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass