---
title: fastapi-project-structure
url: https://skills.sh/vanman2024/ai-dev-marketplace/fastapi-project-structure
---

# fastapi-project-structure

skills/vanman2024/ai-dev-marketplace/fastapi-project-structure
fastapi-project-structure
Installation
$ npx skills add https://github.com/vanman2024/ai-dev-marketplace --skill fastapi-project-structure
SKILL.md
FastAPI Project Structure Skill

Production-ready FastAPI project scaffolding templates and best practices for building scalable, maintainable backend applications with MCP integration support.

Instructions
1. Choose Project Template

Select the appropriate project template based on your use case:

minimal: Basic FastAPI app structure (single file, quick prototypes)
standard: Standard production structure (API routes, models, services)
mcp-server: FastAPI app with MCP server integration
full-stack: Complete backend with auth, database, background tasks
microservice: Microservice-ready structure with health checks, metrics
2. Generate Project Structure

Use the setup script to scaffold a new FastAPI project:

cd /home/gotime2022/.claude/plugins/marketplaces/ai-dev-marketplace/plugins/fastapi-backend/skills/fastapi-project-structure
./scripts/setup-project.sh <project-name> <template-type>


Template types: minimal, standard, mcp-server, full-stack, microservice

Example:

./scripts/setup-project.sh my-api-service standard


What This Creates:

Complete directory structure
Configuration files (pyproject.toml, .env.example)
Main application entry point
Settings management system
Docker configuration (for production templates)
README with setup instructions
3. Configure Application Settings

The skill uses Pydantic Settings for configuration management:

Settings Structure:

# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Configuration
    PROJECT_NAME: str = "FastAPI App"
    VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Server Configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Database Configuration (if needed)
    DATABASE_URL: str

    # Security
    SECRET_KEY: str
    ALLOWED_ORIGINS: list[str] = ["*"]

    class Config:
        env_file = ".env"
        case_sensitive = True


Environment Variables: Copy .env.example to .env and customize:

cp .env.example .env
# Edit .env with your configuration

4. Project Structure Patterns
Standard Structure
my-api-service/
├── app/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py        # Settings management
│   │   └── dependencies.py  # Dependency injection
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes/          # API route handlers
│   │   │   ├── __init__.py
│   │   │   ├── health.py
│   │   │   └── users.py
│   │   └── deps.py          # Route dependencies
│   ├── models/              # Pydantic models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/             # Request/Response schemas
│   │   ├── __init__.py
│   │   └── user.py
│   └── services/            # Business logic
│       ├── __init__.py
│       └── user_service.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_api/
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── Dockerfile (optional)

MCP Server Integration Structure
my-mcp-api/
├── app/
│   ├── main.py              # FastAPI + MCP server
│   ├── core/
│   │   ├── config.py
│   │   └── mcp_config.py    # MCP-specific settings
│   ├── api/
│   │   └── routes/
│   ├── mcp/
│   │   ├── __init__.py
│   │   ├── server.py        # MCP server instance
│   │   ├── tools/           # MCP tools
│   │   ├── resources/       # MCP resources
│   │   └── prompts/         # MCP prompts
│   └── services/
├── .mcp.json                # MCP configuration
├── pyproject.toml
└── README.md

5. Validate Project Structure

Run validation to ensure proper structure and dependencies:

./scripts/validate-structure.sh <project-directory>


Validation Checks:

Directory structure compliance
Required files present (main.py, config.py, pyproject.toml)
Python syntax validation
Dependency declarations
Environment variable configuration
Import structure validity
Type hints presence
6. Development Setup

Initialize the development environment:

# Navigate to project
cd <project-name>

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Run development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

7. MCP Server Integration (Optional)

For projects with MCP server support:

# Configure MCP settings
cp templates/mcp-config-template.json .mcp.json

# Edit MCP configuration
# Add tools, resources, and prompts

# Run as MCP server (STDIO mode)
python -m app.main --mcp

# Run as HTTP server
uvicorn app.main:app --host 0.0.0.0 --port 8000

Available Templates
Core Templates
pyproject.toml: Modern Python project configuration with dependencies
main.py: Application entry point with FastAPI initialization
config.py: Pydantic Settings-based configuration management
dependencies.py: Dependency injection patterns
health.py: Health check endpoints with database/service checks
docker-template: Multi-stage Docker build for production
nginx-template: Nginx reverse proxy configuration
MCP Integration Templates
mcp-server.py: MCP server initialization with FastAPI
mcp-tool-template.py: MCP tool implementation pattern
mcp-resource-template.py: MCP resource pattern
mcp-config.json: MCP server configuration
Settings & Configuration
.env.example: Environment variables template
settings-dev.py: Development-specific settings
settings-prod.py: Production-specific settings
logging-config.yaml: Structured logging configuration
Key Features
Settings Management
Pydantic-based type-safe configuration
Environment-specific settings (dev, staging, prod)
Automatic validation and type conversion
Secret management with environment variables
Nested configuration support
Dependency Injection
FastAPI's built-in DI system
Reusable dependencies for auth, database, services
Request-scoped and application-scoped dependencies
Easy testing with dependency overrides
Project Organization
Clear separation of concerns (routes, models, services)
Scalable directory structure
Consistent naming conventions
Module-based organization for large projects
MCP Integration
Dual-mode operation (HTTP + MCP STDIO)
MCP tools, resources, and prompts
Configuration management via .mcp.json
FastMCP framework compatibility
Production-Ready
Docker multi-stage builds
Health check endpoints
Structured logging
Error handling middleware
CORS configuration
Security headers
Examples

See the examples directory for:

minimal-api/: Simple FastAPI application
crud-api/: Complete CRUD API with database
mcp-integrated-api/: FastAPI + MCP server
microservice-template/: Production microservice
auth-api/: API with JWT authentication
Configuration Files Generated
pyproject.toml
[project]
name = "my-api-service"
version = "1.0.0"
description = "FastAPI application"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.32.0",
    "pydantic>=2.0.0",
    "pydantic-settings>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.24.0",
    "httpx>=0.27.0",
    "ruff>=0.6.0",
    "mypy>=1.11.0",
]
mcp = [
    "mcp>=1.0.0",
]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.mypy]
python_version = "3.11"
strict = true

main.py (Standard Template)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import health, users

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}

Dockerfile (Production Template)
FROM python:3.11-slim as builder
WORKDIR /app
COPY pyproject.toml .
RUN pip install --no-cache-dir build && \
    python -m build --wheel

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app/dist/*.whl .
RUN pip install --no-cache-dir *.whl && rm *.whl
COPY app/ ./app/
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

Best Practices

Project Structure:

Keep business logic in services, not routes
Use schemas for request/response validation
Separate models (DB) from schemas (API)
Implement dependency injection for services
Use async/await for I/O-bound operations

Configuration:

Never commit secrets (.env in .gitignore)
Use Pydantic Settings for type safety
Separate dev/staging/prod configurations
Validate all environment variables at startup
Document required environment variables in .env.example

Code Organization:

One router per resource (users.py, posts.py)
Group related endpoints in routers
Keep route handlers thin (delegate to services)
Use consistent naming conventions
Type-hint all function parameters and returns

Testing:

Use TestClient for API testing
Override dependencies for mocking
Separate unit and integration tests
Use fixtures for common test data
Test both success and error cases

Security:

Validate all inputs with Pydantic
Implement proper CORS configuration
Use environment variables for secrets
Enable security headers middleware
Implement rate limiting for public APIs

Performance:

Use async route handlers for I/O
Implement connection pooling for databases
Add response caching where appropriate
Use background tasks for non-critical operations
Monitor with health check endpoints
Common Workflows
Creating a New API Endpoint
# 1. Generate project structure
./scripts/setup-project.sh my-api standard

# 2. Add new route file
# Create app/api/routes/items.py

# 3. Add schemas
# Create app/schemas/item.py

# 4. Add service logic
# Create app/services/item_service.py

# 5. Register router in main.py
# app.include_router(items.router, prefix="/api/v1/items")

Setting Up MCP Integration
# 1. Generate MCP-enabled project
./scripts/setup-project.sh my-mcp-api mcp-server

# 2. Configure .mcp.json
cp templates/mcp-config-template.json my-mcp-api/.mcp.json

# 3. Add MCP tools
# Copy from templates/mcp-tool-template.py to app/mcp/tools/

# 4. Run in MCP mode
cd my-mcp-api
python -m app.main --mcp

Production Deployment
# 1. Build Docker image
docker build -t my-api:latest .

# 2. Run container
docker run -d -p 8000:8000 \
  --env-file .env.prod \
  --name my-api \
  my-api:latest

# 3. Health check
curl http://localhost:8000/health

Troubleshooting

Import errors: Ensure virtual environment is activated and dependencies installed

Port already in use: Change PORT in .env or use different port with --port flag

Environment variables not loading: Check .env file location and syntax, ensure pydantic-settings installed

MCP server not starting: Verify .mcp.json configuration and mcp package installed

Type checking errors: Run mypy app/ to see detailed type errors, ensure all dependencies have type stubs

Plugin: fastapi-backend Version: 1.0.0 Category: Project Structure & Scaffolding Skill Type: Templates & Automation

Weekly Installs
9
Repository
vanman2024/ai-d…ketplace
GitHub Stars
10
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass