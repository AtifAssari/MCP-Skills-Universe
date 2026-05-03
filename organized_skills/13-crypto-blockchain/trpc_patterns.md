---
rating: ⭐⭐
title: trpc-patterns
url: https://skills.sh/blogic-cz/blogic-marketplace/trpc-patterns
---

# trpc-patterns

skills/blogic-cz/blogic-marketplace/trpc-patterns
trpc-patterns
Installation
$ npx skills add https://github.com/blogic-cz/blogic-marketplace --skill trpc-patterns
SKILL.md
TRPC Patterns
Overview

Implement TRPC routers using established blogic-template-ts patterns for input schemas, procedure selection, middleware composition, and error handling.

When to Use This Skill

Use this skill when implementing or refactoring TRPC routers and procedures, especially when selecting base procedures, adding authorization middleware, or standardizing error handling.

Core Rules
1) Keep simple schemas inline

Define simple input schemas directly in the procedure.

Use project enums and shared types instead of hardcoded string literals.

protectedProcedure.input(z.object({ organizationId: z.string().min(1) }));


Apply these rules:

Keep straightforward schemas inline.
Reuse shared enums/types from project packages.
Extract a schema constant only when reuse or complexity justifies it.

Read detailed examples in references/simple-schemas.md.

2) Select the narrowest valid base procedure

Select base procedures in this order:

Start from access requirement, not implementation convenience.
Pick publicProcedure when no authentication is required.
Pick protectedProcedure when any authenticated user can access.
Pick adminProcedure when global admin role is required.
Pick protectedMemberAccessProcedure when organizationId-scoped membership is required.
Build a custom procedure with .use() only when none of the existing procedures encode the required access rule.

Apply this decision tree:

No auth needed -> publicProcedure
Auth needed, no org scope -> protectedProcedure
Global admin-only action -> adminProcedure
Org-scoped action with membership check -> protectedMemberAccessProcedure
Additional role/permission/resource checks -> extend with middleware on top of the closest base procedure

Read full procedure examples and context behavior in references/custom-procedures.md.

3) Compose middleware with context enhancement

Create reusable middleware with .use() and always continue with opts.next(...).

const procedure = protectedProcedure.use(async (opts) => opts.next({ ctx: {} }));


Apply these rules:

Name middleware functions by responsibility.
Enhance context only with values needed by downstream handlers.
Build from existing base procedures before introducing new ones.

Read advanced middleware patterns in references/middleware-patterns.md.

4) Throw standardized application errors

Import and throw standardized error helpers from project infrastructure.

if (!resource) throw notFoundError("Resource not found");


Apply these rules:

Throw helper-based errors (badRequestError, unauthorizedError, forbiddenError, notFoundError).
Do not instantiate TRPCError manually in route and middleware code when project helpers exist.
Keep error messages action-oriented and domain-specific.

Read full patterns in references/error-handling.md.

5) Treat imports as project conventions

Follow these conventions for blogic-template-ts repositories:

Import shared domain enums/types from project packages (for example @project/common).
Import standardized error helpers from project infrastructure modules (for example @/infrastructure/errors).

When working outside this ecosystem, map these conventions to equivalent modules in the target codebase.

Type Inference Guidance

Rely on static TypeScript inference from backend router definitions.

Apply these rules:

Export root router types consistently.
Import router types into frontend TRPC client setup.
Avoid manual endpoint response/input types that duplicate inferred TRPC types.

Read additional examples in references/custom-procedures.md and keep router exports consistent.

Scope Boundaries

Focus this skill on TRPC router structure, access control, middleware, and errors.

Delegate query-level performance tuning (JOIN strategy, batch reads, N+1 reduction, indexing) to the performance-optimization skill.

Resources

Read long-form examples and implementation details in:

references/simple-schemas.md - Complete examples of inline schema patterns
references/custom-procedures.md - Base procedure behavior and context enhancement
references/middleware-patterns.md - Advanced middleware composition patterns
references/error-handling.md - Detailed helper-based error patterns

For query and database performance guidance, load the performance-optimization skill.

Weekly Installs
61
Repository
blogic-cz/blogi…ketplace
GitHub Stars
3
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass