---
title: fastapi-development
url: https://skills.sh/aj-geddes/useful-ai-prompts/fastapi-development
---

# fastapi-development

skills/aj-geddes/useful-ai-prompts/fastapi-development
fastapi-development
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill fastapi-development
SKILL.md
FastAPI Development
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create fast, modern Python APIs using FastAPI with async/await support, automatic API documentation, type validation using Pydantic, dependency injection, JWT authentication, and SQLAlchemy ORM integration.

When to Use
Building high-performance Python REST APIs
Creating async API endpoints
Implementing automatic OpenAPI/Swagger documentation
Leveraging Python type hints for validation
Building microservices with async support
Integrating Pydantic for data validation
Quick Start

Minimal working example:

# main.py
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI instance
app = FastAPI(
    title="API Service",
    description="A modern FastAPI application",
    version="1.0.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
FastAPI Application Setup	FastAPI Application Setup
Pydantic Models for Validation	Pydantic Models for Validation
Async Database Models and Queries	Async Database Models and Queries
Security and JWT Authentication	Security and JWT Authentication
Service Layer for Business Logic	Service Layer for Business Logic
API Routes with Async Endpoints	API Routes with Async Endpoints
Best Practices
✅ DO
Use async/await for I/O operations
Leverage Pydantic for validation
Use dependency injection for services
Implement proper error handling with HTTPException
Use type hints for automatic OpenAPI documentation
Create service layers for business logic
Implement authentication on protected routes
Use environment variables for configuration
Return appropriate HTTP status codes
Document endpoints with docstrings and tags
❌ DON'T
Use synchronous database operations
Trust user input without validation
Store secrets in code
Ignore type hints
Return database models in responses
Implement authentication in route handlers
Use mutable default arguments
Forget to validate query parameters
Expose stack traces in production
Weekly Installs
416
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass