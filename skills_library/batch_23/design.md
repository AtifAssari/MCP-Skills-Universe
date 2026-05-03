---
title: design
url: https://skills.sh/knoopx/pi/design
---

# design

skills/knoopx/pi/design
design
Installation
$ npx skills add https://github.com/knoopx/pi --skill design
SKILL.md
Design

Guidelines for requirements analysis, design principles, architecture, and security.

Requirements Analysis
Before Writing Code
 Understand the requirements
 Consider edge cases
 Plan the approach
 Think about testing
Tools for Understanding Existing Code

Before designing new features, understand the existing codebase:

# Get project overview with codemapper
cm stats . --format ai
cm map . --level 2 --format ai

# Find entry points and main flows
cm query main . --format ai
cm callees main . --format ai

# Understand module dependencies
cm deps . --format ai
cm deps . --circular --format ai  # Check for issues

Core Principles
SOLID Principles
Principle	Description	Violation Sign
Single Responsibility	A class/module should have one reason to change	Class doing too many things
Open/Closed	Open for extension, closed for modification	Modifying existing code for new features
Liskov Substitution	Subtypes must be substitutable for base types	Overridden methods breaking contracts
Interface Segregation	Many specific interfaces > one general interface	Clients forced to depend on unused methods
Dependency Inversion	Depend on abstractions, not concretions	High-level modules importing low-level details
DRY, KISS, YAGNI
DRY   - Don't Repeat Yourself: Extract common logic, but don't over-abstract
KISS  - Keep It Simple, Stupid: Prefer clarity over cleverness
YAGNI - You Aren't Gonna Need It: Don't build features until needed


Detect DRY violations with jscpd:

# Find duplicate code blocks
npx jscpd /path/to/source
npx jscpd --pattern "src/**/*.ts"

Simplicity Over Complexity

Simple, working code beats clever, complex code.

❌ OVERENGINEERed                    ✅ SIMPLE
─────────────────────────────────────────────────────
AbstractFactoryProvider              Direct instantiation
5 layers of indirection              1-2 layers max
Generic solution for 1 use case      Specific solution that works
"Future-proof" architecture          Solve today's problem
Premature optimization               Optimize when needed

Security by Design
Threat Modeling
 Identify threat vectors
 Plan for input validation
 Consider authentication/authorization
 Plan for data protection
 Plan for logging and monitoring
 Plan for audit trails
Input Validation
// ✅ GOOD: Validate all inputs
interface CreateUserInput {
  name: string;
  email: string;
  age?: number;
}

function createUser(input: CreateUserInput): User {
  if (!input.name || input.name.length < 2) {
    throw new ValidationError("Name must be at least 2 characters");
  }

  if (!isValidEmail(input.email)) {
    throw new ValidationError("Invalid email format");
  }

  if (input.age !== undefined && (input.age < 0 || input.age > 120)) {
    throw new ValidationError("Age must be between 0 and 120");
  }

  // Proceed with valid input
}

Authentication & Authorization
// ✅ GOOD: Proper auth and authorization
interface AuthenticatedRequest {
  userId: string;
  role: "admin" | "user" | "guest";
}

function deleteUser(request: AuthenticatedRequest, userId: string) {
  if (request.role !== "admin") {
    throw new ForbiddenError("Only admins can delete users");
  }

  if (userId === request.userId) {
    throw new BadRequestError("Cannot delete yourself");
  }

  // Proceed with authorized operation
}

Health Assessment Before Design

Before designing new features, assess the health of the area you're changing:

Mechanical Check (quick, verifiable)
 No unused imports or dead exports in affected files
 No import cycles involving the module
 No orphaned files (files nothing imports)
 No near-duplicate logic across sibling files
 Complexity within bounds (no functions > 50 LOC, nesting > 4)
Subjective Check (requires reading)
 Names communicate intent — would a stranger understand without reading the body?
 Error handling is consistent with sibling modules
 Abstractions earn their cost — no single-use wrappers
 Dependencies point in the right direction (domain has no infrastructure imports)
 Conventions match the rest of the directory
If Health Is Poor

Fix the existing issues before adding new features. Adding features to unhealthy code compounds debt. The order is:

Fix T1/T2 mechanical issues (unused, dead, lint)
Fix convention drift (make siblings consistent)
Add the new feature
Verify no new issues introduced
Related Skills
swe: Code quality guidelines, anti-patterns, code health dimensions
typescript: Type safety and interfaces
vitest: Test design and patterns
Weekly Installs
29
Repository
knoopx/pi
GitHub Stars
45
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass