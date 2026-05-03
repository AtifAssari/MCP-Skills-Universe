---
title: python-fastapi-development
url: https://skills.sh/sickn33/antigravity-awesome-skills/python-fastapi-development
---

# python-fastapi-development

skills/sickn33/antigravity-awesome-skills/python-fastapi-development
python-fastapi-development
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill python-fastapi-development
SKILL.md
Python/FastAPI Development Workflow
Overview

Specialized workflow for building production-ready Python backends with FastAPI, featuring async patterns, SQLAlchemy ORM, Pydantic validation, and comprehensive API patterns.

When to Use This Workflow

Use this workflow when:

Building new REST APIs with FastAPI
Creating async Python backends
Implementing database integration with SQLAlchemy
Setting up API authentication
Developing microservices
Workflow Phases
Phase 1: Project Setup
Skills to Invoke
app-builder - Application scaffolding
python-development-python-scaffold - Python scaffolding
fastapi-templates - FastAPI templates
uv-package-manager - Package management
Actions
Set up Python environment (uv/poetry)
Create project structure
Configure FastAPI app
Set up logging
Configure environment variables
Copy-Paste Prompts
Use @fastapi-templates to scaffold a new FastAPI project

Use @python-development-python-scaffold to set up Python project structure

Phase 2: Database Setup
Skills to Invoke
prisma-expert - Prisma ORM (alternative)
database-design - Schema design
postgresql - PostgreSQL setup
pydantic-models-py - Pydantic models
Actions
Design database schema
Set up SQLAlchemy models
Create database connection
Configure migrations (Alembic)
Set up session management
Copy-Paste Prompts
Use @database-design to design PostgreSQL schema

Use @pydantic-models-py to create Pydantic models for API

Phase 3: API Routes
Skills to Invoke
fastapi-router-py - FastAPI routers
api-design-principles - API design
api-patterns - API patterns
Actions
Design API endpoints
Create API routers
Implement CRUD operations
Add request validation
Configure response models
Copy-Paste Prompts
Use @fastapi-router-py to create API endpoints with CRUD operations

Use @api-design-principles to design RESTful API

Phase 4: Authentication
Skills to Invoke
auth-implementation-patterns - Authentication
api-security-best-practices - API security
Actions
Choose auth strategy (JWT, OAuth2)
Implement user registration
Set up login endpoints
Create auth middleware
Add password hashing
Copy-Paste Prompts
Use @auth-implementation-patterns to implement JWT authentication

Phase 5: Error Handling
Skills to Invoke
fastapi-pro - FastAPI patterns
error-handling-patterns - Error handling
Actions
Create custom exceptions
Set up exception handlers
Implement error responses
Add request logging
Configure error tracking
Copy-Paste Prompts
Use @fastapi-pro to implement comprehensive error handling

Phase 6: Testing
Skills to Invoke
python-testing-patterns - pytest testing
api-testing-observability-api-mock - API testing
Actions
Set up pytest
Create test fixtures
Write unit tests
Implement integration tests
Configure test database
Copy-Paste Prompts
Use @python-testing-patterns to write pytest tests for FastAPI

Phase 7: Documentation
Skills to Invoke
api-documenter - API documentation
openapi-spec-generation - OpenAPI specs
Actions
Configure OpenAPI schema
Add endpoint documentation
Create usage examples
Set up API versioning
Generate API docs
Copy-Paste Prompts
Use @api-documenter to generate comprehensive API documentation

Phase 8: Deployment
Skills to Invoke
deployment-engineer - Deployment
docker-expert - Containerization
Actions
Create Dockerfile
Set up docker-compose
Configure production settings
Set up reverse proxy
Deploy to cloud
Copy-Paste Prompts
Use @docker-expert to containerize FastAPI application

Technology Stack
Category	Technology
Framework	FastAPI
Language	Python 3.11+
ORM	SQLAlchemy 2.0
Validation	Pydantic v2
Database	PostgreSQL
Migrations	Alembic
Auth	JWT, OAuth2
Testing	pytest
Quality Gates
 All tests passing (>80% coverage)
 Type checking passes (mypy)
 Linting clean (ruff, black)
 API documentation complete
 Security scan passed
 Performance benchmarks met
Related Workflow Bundles
development - General development
database - Database operations
security-audit - Security testing
api-development - API patterns
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
308
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass