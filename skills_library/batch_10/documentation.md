---
title: documentation
url: https://skills.sh/xbklairith/kisune/documentation
---

# documentation

skills/xbklairith/kisune/documentation
documentation
Installation
$ npx skills add https://github.com/xbklairith/kisune --skill documentation
SKILL.md
Documentation Skill
Purpose

Generate comprehensive, maintainable documentation including code docstrings, API specifications, architecture diagrams, README files, and clear code explanations.

Activation Triggers

Activate this skill when:

User says "document this", "explain this code", "how does this work?"
User mentions "README", "docs", or "documentation"
After completing a feature or creating API endpoints
User says "write comments for this"
Documentation Types
1. Code Documentation (Docstrings)

Goal: Clear, comprehensive function/class documentation

Key Components:

Brief description (one line)
Detailed explanation (purpose and behavior)
Args/Parameters (types, constraints, examples)
Returns (type and meaning)
Example (realistic usage)
Raises/Throws (error conditions)
Note (implementation details)

Language-Specific Formats:

Python: """triple quotes""", Args/Returns/Raises format
JavaScript/TypeScript: JSDoc /** */, @param/@returns/@throws tags
Java: Javadoc /** */, @param/@return/@throws tags
C#: XML comments /// <summary>
2. API Documentation

Goal: Complete API reference for each endpoint

Required sections per endpoint:

HTTP method and path
Brief description
Request schema (params, body with types and constraints)
Success response (status code, schema, example)
Error responses (status codes, error codes, messages)
Example usage (cURL and/or language-specific)
Security notes (auth, rate limits, etc.)

Template:

### METHOD /api/path

Description of what this endpoint does.

**Request:**
- `field` (type, required/optional): Description

**Response (200 OK):**
- `field` (type): Description

**Errors:** 400 (validation), 401 (auth), 429 (rate limit)

**Security:** Auth required, rate limit X req/min

3. Architecture Documentation

Goal: Clear system overview and component relationships

Required sections:

Overview: System purpose and architecture style
System Diagram: ASCII or Mermaid diagram showing components and connections
Core Components: For each component: responsibility, functions, technology, scaling strategy
Data Flow: Step-by-step flows for key operations
Integration Points: External services and internal APIs
Security Architecture: Authentication, authorization, data protection
Performance: Caching strategy, database optimization, scaling strategy
Monitoring: Metrics, logging, alerts
4. README Generation

Goal: Comprehensive project README

Essential Sections:

Title + one-line description - What problem it solves
Features - Key features as bullet list
Installation - Clone, install, configure, run
Usage - Basic code example
Configuration - Environment variables table (Variable, Description, Required)
Development - Test, lint, build commands
License

Optional Sections (add as needed):

Demo/screenshots, API Reference, Project Structure, Deployment, Contributing
5. Code Explanations

Goal: Clear explanations of complex code

Process:

High-Level Purpose - What problem does this solve? Where does it fit?
Step-by-Step Logic - Break down into phases, explain each clearly
Key Algorithms/Patterns - Identify algorithms, explain approach, note complexity
Edge Cases - Unusual inputs handled, assumptions made, validation performed

Structure each explanation as:

Purpose (what and why)
How It Works (numbered steps with formulas/logic)
Why This Approach (rationale and alternatives considered)
Edge Cases Handled (list with explanations)
When to Document

Always Document:

Public APIs and endpoints
Complex algorithms
Non-obvious logic
Security-sensitive code
Performance-critical sections
Error handling strategies

Consider Documenting:

Helper functions with multiple params
Class constructors
Configuration options
Database schema

Don't Bother Documenting:

Trivial getters/setters
Self-explanatory code
Temporary/experimental code
Best Practices
Write for Future You: Assume you'll forget everything in 6 months
Explain Why, Not What: Code shows what, docs explain why
Keep Examples Current: Update examples when code changes
Use Consistent Format: Follow language conventions
Be Concise: Every word should add value
Use Active Voice: "Returns user" not "User is returned"
Include Edge Cases: Document unusual inputs and outputs
Update With Code: Outdated docs are worse than no docs
Integration Points
Works with spec-driven skill for feature documentation
Works with review skill to verify docs exist
Auto-triggered after feature completion
Notes
Default to clear code over comments (code is always correct, comments lie)
Good naming reduces need for documentation
Complex logic deserves explanation
APIs require comprehensive documentation
When in doubt, document it
Weekly Installs
14
Repository
xbklairith/kisune
GitHub Stars
2
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass