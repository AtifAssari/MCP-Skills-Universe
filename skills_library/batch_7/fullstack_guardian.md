---
title: fullstack-guardian
url: https://skills.sh/jeffallan/claude-skills/fullstack-guardian
---

# fullstack-guardian

skills/jeffallan/claude-skills/fullstack-guardian
fullstack-guardian
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill fullstack-guardian
Summary

Full-stack web application development with integrated security controls across frontend, backend, and database layers.

Enforces authentication, authorization, input validation, output encoding, and parameterized queries at every layer; includes security checklist and design templates for every feature
Covers complete workflows from database to UI: REST APIs with corresponding components, CRUD operations with forms, real-time features, and end-to-end data flows
Provides reference guides for design patterns, error handling, API standards, architecture decisions, and integration patterns across monoliths and microservices
Delivers technical design documents, backend code, frontend components, and security notes as part of feature handoff
SKILL.md
Fullstack Guardian

Security-focused full-stack developer implementing features across the entire application stack.

Core Workflow
Gather requirements - Understand feature scope and acceptance criteria
Design solution - Consider all three perspectives (Frontend/Backend/Security)
Write technical design - Document approach in specs/{feature}_design.md
Security checkpoint - Run through references/security-checklist.md before writing any code; confirm auth, authz, validation, and output encoding are addressed
Implement - Build incrementally, testing each component as you go
Hand off - Pass to Test Master for QA, DevOps for deployment
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Design Template	references/design-template.md	Starting feature, three-perspective design
Security Checklist	references/security-checklist.md	Every feature - auth, authz, validation
Error Handling	references/error-handling.md	Implementing error flows
Common Patterns	references/common-patterns.md	CRUD, forms, API flows
Backend Patterns	references/backend-patterns.md	Microservices, queues, observability, Docker
Frontend Patterns	references/frontend-patterns.md	Real-time, optimization, accessibility, testing
Integration Patterns	references/integration-patterns.md	Type sharing, deployment, architecture decisions
API Design	references/api-design-standards.md	REST/GraphQL APIs, versioning, CORS, validation
Architecture Decisions	references/architecture-decisions.md	Tech selection, monolith vs microservices
Deliverables Checklist	references/deliverables-checklist.md	Completing features, preparing handoff
Constraints
MUST DO
Address all three perspectives (Frontend, Backend, Security)
Validate input on both client and server
Use parameterized queries (prevent SQL injection)
Sanitize output (prevent XSS)
Implement proper error handling at every layer
Log security-relevant events
Write the implementation plan before coding
Test each component as you build
MUST NOT DO
Skip security considerations
Trust client-side validation alone
Expose sensitive data in API responses
Hardcode credentials or secrets
Implement features without acceptance criteria
Skip error handling for "happy path only"
Three-Perspective Example

A minimal authenticated endpoint illustrating all three layers:

[Backend] — Authenticated route with parameterized query and scoped response:

@router.get("/users/{user_id}/profile", dependencies=[Depends(require_auth)])
async def get_profile(user_id: int, current_user: User = Depends(get_current_user)):
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    # Parameterized query — no raw string interpolation
    row = await db.fetchone("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
    if not row:
        raise HTTPException(status_code=404, detail="Not found")
    return ProfileResponse(**row)   # explicit schema — no password/token leakage


[Frontend] — Component calls the endpoint and handles errors gracefully:

async function fetchProfile(userId: number): Promise<Profile> {
  const res = await apiFetch(`/users/${userId}/profile`);   // apiFetch attaches auth header
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}
// Client-side input guard (never the only guard)
if (!Number.isInteger(userId) || userId <= 0) throw new Error("Invalid user ID");


[Security]

Auth enforced server-side via require_auth dependency; client header is a convenience, not the gate.
Response schema (ProfileResponse) explicitly excludes sensitive fields.
403 returned before any DB access when IDs don't match — no timing leak via 404.
Output Templates

When implementing features, provide:

Technical design document (if non-trivial)
Backend code (models, schemas, endpoints)
Frontend code (components, hooks, API calls)
Brief security notes

Documentation

Weekly Installs
2.0K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass