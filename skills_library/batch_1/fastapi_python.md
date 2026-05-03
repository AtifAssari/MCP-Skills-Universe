---
title: fastapi-python
url: https://skills.sh/mindrally/skills/fastapi-python
---

# fastapi-python

skills/mindrally/skills/fastapi-python
fastapi-python
Installation
$ npx skills add https://github.com/mindrally/skills --skill fastapi-python
Summary

Expert guidance for building high-performance FastAPI APIs with async best practices and clean Python patterns.

Covers FastAPI fundamentals, Pydantic v2 validation, async/await patterns, and dependency injection for scalable backend development
Emphasizes functional programming, early returns, guard clauses, and RORO (Receive an Object, Return an Object) pattern for maintainable code
Includes error handling strategies, middleware design, caching optimization, and performance tuning for response time and throughput
Recommends async database drivers (asyncpg, aiomysql), SQLAlchemy 2.0, and lifespan context managers for resource management
SKILL.md
FastAPI Python

You are an expert in FastAPI and Python backend development.

Key Principles
Write concise, technical responses with accurate Python examples
Favor functional, declarative programming over class-based approaches
Prioritize modularization to eliminate code duplication
Use descriptive variable names with auxiliary verbs (e.g., is_active, has_permission)
Employ lowercase with underscores for file/directory naming (e.g., routers/user_routes.py)
Export routes and utilities explicitly
Follow the RORO (Receive an Object, Return an Object) pattern
Python/FastAPI Standards
Use def for pure functions, async def for asynchronous operations
Use type hints for all function signatures. Prefer Pydantic models over raw dictionaries
Structure: exported router, sub-routes, utilities, static content, types (models, schemas)
Omit curly braces for single-line conditionals
Write concise one-line conditional syntax
Error Handling
Handle edge cases at function entry points
Employ early returns for error conditions
Place happy path logic last
Avoid unnecessary else statements; use if-return patterns
Implement guard clauses for preconditions
Provide proper error logging and user-friendly messaging
FastAPI-Specific Guidelines
Use functional components (plain functions) and Pydantic models for input validation
Declare routes with clear return type annotations
Prefer lifespan context managers for managing startup and shutdown events
Leverage middleware for logging, error monitoring, and optimization
Use HTTPException for expected errors and model them as specific HTTP responses
Apply Pydantic's BaseModel consistently for validation
Performance Optimization
Minimize blocking I/O; use async for all database and API calls
Implement caching with Redis or in-memory stores
Optimize Pydantic serialization/deserialization
Use lazy loading for large datasets
Key Conventions
Rely on FastAPI's dependency injection system
Prioritize API performance metrics (response time, latency, throughput)
Structure routes and dependencies for readability and maintainability
Dependencies

FastAPI, Pydantic v2, asyncpg/aiomysql, SQLAlchemy 2.0

Weekly Installs
8.0K
Repository
mindrally/skills
GitHub Stars
88
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass