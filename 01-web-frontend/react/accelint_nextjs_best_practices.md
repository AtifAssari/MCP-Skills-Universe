---
title: accelint-nextjs-best-practices
url: https://skills.sh/gohypergiant/agent-skills/accelint-nextjs-best-practices
---

# accelint-nextjs-best-practices

skills/gohypergiant/agent-skills/accelint-nextjs-best-practices
accelint-nextjs-best-practices
Installation
$ npx skills add https://github.com/gohypergiant/agent-skills --skill accelint-nextjs-best-practices
SKILL.md
Next.js Best Practices

Comprehensive performance optimization and best practices for Next.js applications, designed for AI agents and LLMs working with Next.js code.

When to Activate This Skill

Use this skill when the task involves:

Writing Next.js Code
Creating Server Components or Client Components
Implementing Server Actions with "use server"
Writing API route handlers
Setting up data fetching in RSC (React Server Components)
Implementing Suspense boundaries
Using Next.js-specific APIs (headers(), cookies(), after())
Refactoring Next.js Code
Optimizing server-side data fetching
Reducing RSC serialization overhead
Converting sequential to parallel operations
Restructuring component composition for better performance
Migrating between Server and Client Components
Performance Optimization
Eliminating server-side waterfalls
Reducing response times in API routes and Server Actions
Minimizing data transfer at RSC boundaries
Implementing request deduplication with React.cache()
Using after() for non-blocking operations
Next.js-Specific Issues
Authentication/authorization in Server Actions
RSC serialization duplication problems
Import optimization (barrel file issues)
Server vs Client Component decision-making
Parallel data fetching patterns
Code Review
Reviewing Next.js code for performance anti-patterns
Identifying security issues in Server Actions
Checking proper Server/Client Component boundaries
Ensuring proper authentication patterns
Validating Suspense boundary placement
When NOT to Use This Skill

Do not activate for:

React-specific optimizations (use accelint-react-best-practices skill)
Build configuration (webpack, turbopack) unless Next.js-specific
General TypeScript/JavaScript questions (use accelint-ts-best-practices skill)
Deployment/hosting configuration
Testing setup (use accelint-ts-testing skill)
Example Trigger Phrases

This skill should activate when users say things like:

Performance Issues:

"This Next.js API route is slow"
"My Server Component is blocking the entire page"
"Optimize this Server Action"
"The page takes forever to load data"
"There's a waterfall in my data fetching"

Security Issues:

"Add authentication to this Server Action"
"This Server Action needs authorization"
"Secure this API route"
"Validate input in this Server Action"

Debugging Issues:

"Why is my RSC props so large?"
"This data is being duplicated in the HTML"
"My imports are slow in development"
"Should this be a Server or Client Component?"

Code Review:

"Review this Next.js code for performance issues"
"Is this Server Action secure?"
"Can you optimize this data fetching?"
"Check if this component should be server or client"

Refactoring:

"Parallelize these data fetches"
"Reduce the serialization size"
"Convert this to use Suspense"
"Optimize this barrel import"
How to Use

This skill uses a progressive disclosure structure to minimize context usage:

1. Start with the Overview (AGENTS.md)

Read AGENTS.md for a concise overview of all rules with one-line summaries.

2. Load Specific Rules as Needed

When you identify a relevant optimization, load the corresponding reference file for detailed implementation guidance:

General Patterns:

prevent-waterfall-chains.md (1.1)
parallelize-independent-operations.md (1.2)
strategic-suspense-boundaries.md (1.3)

Server-Side Performance:

server-actions-security.md (2.1)
avoid-duplicate-serialization.md (2.2)
minimize-serialization.md (2.3)
parallel-data-fetching.md (2.4)
react-cache-deduplication.md (2.5)
use-after-non-blocking.md (2.6)

Misc:

avoid-barrel-imports.md (3.1)
server-vs-client-component.md (3.2)

Quick References:

quick-checklist.md
compound-patterns.md

Automation Scripts:

scripts/ - Helper scripts to detect anti-patterns
3. Apply the Pattern

Each reference file contains:

❌ Incorrect examples showing the anti-pattern
✅ Correct examples showing the optimal implementation
Explanations of why the pattern matters
Performance impact metrics
Related patterns and references
4. Use the Report Template

When this skill is invoked for Next.js code review, use the standardized report format:

Template: assets/output-report-template.md

The report format provides:

Executive Summary with impact assessment
Severity levels (Critical, High, Medium, Low) for prioritization
Impact analysis (performance, security, data transfer, maintainability)
Categorization (Server Actions, RSC Serialization, Data Fetching, Component Architecture)
Pattern references linking to detailed guidance in references/
Summary table for tracking all issues

When to use the report template:

Skill invoked directly via /accelint-nextjs-best-practices <path>
User asks to "review Next.js code" or "audit Next.js app" across file(s), invoking skill implicitly

When NOT to use the report template:

User asks to "fix this Server Action" (direct implementation)
User asks "what's wrong with this code?" (answer the question)
User requests specific fixes (apply fixes directly without formal report)
Examples
Example 1: Optimizing Server Action Security

Task: "Add authentication to this Server Action"

Approach:

Read AGENTS.md overview
Identify issue: Server Action needs authentication
Load server-actions-security.md
Apply authentication pattern with validation
Example 2: Eliminating Waterfalls

Task: "This page loads slowly with multiple fetches"

Approach:

Read AGENTS.md overview
Identify issue: Sequential data fetching
Load prevent-waterfall-chains.md and parallelize-independent-operations.md
Start operations immediately and use Promise.allSettled()
Example 3: Reducing Serialization

Task: "The HTML response is huge with user data"

Approach:

Read AGENTS.md overview
Identify issue: Over-serialization at RSC boundary
Load minimize-serialization.md
Pass only necessary fields, transform on client
Additional Resources

Official Next.js documentation:

App Router Documentation
Server Components
Server Actions
Authentication Guide
Performance Optimization
Weekly Installs
210
Repository
gohypergiant/ag…t-skills
GitHub Stars
11
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass