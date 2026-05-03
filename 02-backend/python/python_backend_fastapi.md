---
rating: ⭐⭐
title: python-backend-fastapi
url: https://skills.sh/janjaszczak/cursor/python-backend-fastapi
---

# python-backend-fastapi

skills/janjaszczak/cursor/python-backend-fastapi
python-backend-fastapi
Installation
$ npx skills add https://github.com/janjaszczak/cursor --skill python-backend-fastapi
SKILL.md
Python backend (FastAPI + Pydantic v2 + Alembic)
Activation cues

Use this skill when the task involves:

new or modified FastAPI endpoints, routers, dependencies, middleware
request/response validation, schema design, OpenAPI correctness (Pydantic v2)
database schema changes (Alembic revisions)
backend logging and request tracing
ETL / parsers / import pipelines with memory constraints and “bad rows” reporting
Operating principles (agent workflow)
Start with a short plan before editing code. Prefer file-path-specific steps and repository-aligned patterns.
Ask up to 1–3 clarifying questions only if truly blocking.
Prefer verifiable goals: tests, migrations, reproducible API calls, and deterministic outputs.
For complex/high-risk changes, run an internal Chain-of-Verification (CoVe): draft → 3–5 verification questions → answer independently → revise; surface only final result + (optional) UNCERTAIN items and how to verify them.
Standard implementation workflow
1) Context discovery (do not invent patterns)
Locate existing routers, dependency injection conventions, error handling, and response schema patterns.
Identify service layer boundaries (or create them if missing).
Find existing migration conventions and logging format.
2) API contract first (Pydantic v2)
Define/extend request & response models with Pydantic v2.
Ensure OpenAPI reflects reality (status codes, response shapes, optional fields).
Keep handlers thin: parse/validate, delegate to service, map service result to response.

Definition of “thin handler”:

No business rules in the endpoint function beyond wiring + basic validation.
No direct DB logic in the handler unless the codebase already standardizes it there.
3) Service layer + tests (pytest)
Move business logic to a service module with unit tests.
Prefer tests that encode behavior and edge cases (happy path, validation, not found, conflicts).
Add/extend fixtures in line with repo conventions.
4) Dependency Injection (FastAPI Depends)
Use Depends for DI and request-scoped dependencies.
If a request-id is used in the project, propagate it through dependencies/services.
5) Alembic migrations (every schema change)
Create a new revision for each schema change.
Make migrations idempotent and safe:
avoid non-deterministic operations
provide both upgrade and downgrade
ensure ordering is correct with dependencies
If the change is data-destructive, clearly annotate risk and required operator steps.
6) Logging (stdlib logging)
Use Python stdlib logging.
Include request id (if available) and key fields relevant to the operation.
Avoid logging secrets/PII; log identifiers and high-level state transitions instead.
7) ETL / parsers (streaming, error CSV)

When implementing ingestion/parsing:

Process input file-by-file (and ideally row-by-row) to avoid loading all data into memory.
For invalid records:
write a CSV containing: timestamp, file, line, error, original_row
keep original_row as close to raw input as possible (avoid “fixing” it before logging)
Logging must allow operators to reproduce and patch upstream data.
Definition of done (backend changes)

A change is “done” only if:

endpoint behavior matches contract (schemas + status codes)
tests exist and pass for new/changed logic
migrations exist for schema changes (upgrade + downgrade)
logging is present for operationally relevant paths
for new endpoints: provide example curl or httpie calls + expected responses
Examples (template snippets)
Example: endpoint acceptance checklist
Request model defined (Pydantic v2)
Response model defined (Pydantic v2)
Handler delegates to service
Tests cover core behavior + edge case
Example curl included in PR/plan notes
Example: ETL error row
timestamp: ISO-8601
file: input filename
line: input line number (1-based)
error: short human-readable description
original_row: raw row payload
Weekly Installs
8
Repository
janjaszczak/cursor
First Seen
Feb 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass