---
title: refactoring-specialist
url: https://skills.sh/404kidwiz/claude-supercode-skills/refactoring-specialist
---

# refactoring-specialist

skills/404kidwiz/claude-supercode-skills/refactoring-specialist
refactoring-specialist
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill refactoring-specialist
SKILL.md
Refactoring Specialist
Purpose

Provides expertise in systematically improving code quality and structure without altering external behavior. Specializes in applying design patterns, enforcing SOLID principles, and managing technical debt through incremental refactoring strategies.

When to Use
Improving code readability and maintainability
Reducing code duplication and complexity
Applying design patterns to solve structural problems
Breaking apart monolithic classes or functions
Introducing proper abstraction layers
Preparing codebase for new feature development
Migrating legacy code to modern patterns
Establishing anti-corruption layers between systems
Quick Start

Invoke this skill when:

Improving code readability and maintainability
Reducing code duplication and complexity
Applying design patterns to solve structural problems
Breaking apart monolithic classes or functions
Introducing proper abstraction layers

Do NOT invoke when:

Adding new features (refactor first, then add) → use appropriate domain skill
Debugging runtime errors → use debugger
Reviewing code for security issues → use security-auditor
Optimizing performance bottlenecks → use performance-engineer
Decision Framework
Code Smell Detected?
├── Duplication → Extract Method/Class, Template Method pattern
├── Long Method → Extract Method, Decompose Conditional
├── Large Class → Extract Class, Single Responsibility
├── Feature Envy → Move Method to appropriate class
├── Primitive Obsession → Introduce Value Objects
├── Shotgun Surgery → Move related changes together
└── Divergent Change → Split by responsibility

Core Workflows
1. Safe Refactoring Cycle
Ensure comprehensive test coverage exists
Identify specific code smell to address
Apply smallest possible refactoring step
Run tests to verify behavior unchanged
Commit the change
Repeat until smell eliminated
2. Pattern Introduction
Identify recurring structural problem
Select appropriate design pattern
Create new structure alongside existing code
Migrate consumers incrementally
Remove old implementation
Document pattern usage for team
3. Anti-Corruption Layer Implementation
Identify boundary between systems/domains
Define clean interface for internal domain
Create adapter/translator layer
Route all cross-boundary calls through ACL
Evolve internal model independently
Best Practices
Always refactor with tests as a safety net
Make small, incremental changes with frequent commits
Refactor before adding new features, not during
Use IDE refactoring tools for mechanical transformations
Document why patterns were applied, not just what
Prioritize refactoring by business value and risk
Anti-Patterns
Big Bang refactoring → Use incremental strangler pattern
Refactoring without tests → Add characterization tests first
Over-engineering → Apply patterns only when needed
Refactoring during feature work → Separate refactoring commits
Ignoring team conventions → Align with existing codebase style
Weekly Installs
126
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass