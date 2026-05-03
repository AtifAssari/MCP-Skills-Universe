---
title: docker-workflows
url: https://skills.sh/autumnsgrove/groveengine/docker-workflows
---

# docker-workflows

skills/autumnsgrove/groveengine/docker-workflows
docker-workflows
Installation
$ npx skills add https://github.com/autumnsgrove/groveengine --skill docker-workflows
SKILL.md
Docker Workflows Skill
When to Activate

Activate this skill when:

Creating Dockerfiles for applications
Setting up docker-compose environments
Containerizing Python/UV projects
Configuring multi-stage builds
Managing container secrets
Quick Commands
# Build image
docker build -t my-app:latest .

# Run container
docker run -d -p 8000:8000 --name my-app my-app:latest

# View logs
docker logs -f my-app

# Execute in container
docker exec -it my-app bash

# Stop and remove
docker stop my-app && docker rm my-app

# Clean up
docker system prune -a

Basic Dockerfile (Python/UV)
FROM python:3.11-slim

WORKDIR /app

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files (layer caching)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy application
COPY . .

EXPOSE 8000

CMD ["uv", "run", "python", "main.py"]

Multi-Stage Build (Production)
# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY . .

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Create non-root user
RUN useradd -m -u 1000 appuser && chown appuser:appuser /app

# Copy from builder
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app /app

USER appuser

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000
CMD ["python", "main.py"]

.dockerignore
__pycache__/
*.pyc
.git/
.env
.venv/
venv/
*.log
.DS_Store
.pytest_cache/
tests/
docs/
*.md

Docker Compose (App + Database)
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/myapp
    depends_on:
      - db
    volumes:
      - ./app:/app  # Development: live reload

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:

Compose Commands
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop services
docker-compose down

# Rebuild and restart
docker-compose up -d --build

# Run command in service
docker-compose exec app bash

# Remove volumes (deletes data!)
docker-compose down -v

Layer Caching Best Practice
# Good: Dependencies cached separately
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY . .

# Bad: Cache invalidated on every code change
COPY . .
RUN uv sync --frozen --no-dev

Security Essentials
# Use official slim images
FROM python:3.11-slim

# Run as non-root
RUN useradd -m -u 1000 appuser
USER appuser

# Don't include secrets in images
# Use runtime environment variables instead

Runtime Secrets
# Pass via environment
docker run -e API_KEY=secret my-app

# Use env file
docker run --env-file .env.production my-app

# With compose
services:
  app:
    env_file:
      - .env.production

Volume Types
# Named volume (data persistence)
docker run -v postgres_data:/var/lib/postgresql/data postgres

# Bind mount (development)
docker run -v $(pwd)/app:/app my-app

Debugging
# Interactive shell
docker exec -it container_name bash

# Real-time logs
docker logs -f --tail 100 container_name

# Inspect configuration
docker inspect container_name

# Resource usage
docker stats container_name

# Copy files
docker cp container_name:/app/logs ./logs

Common Issues
Container exits immediately
docker logs container_name  # Check for errors
docker run -it app:v1 bash  # Debug interactively

Can't connect to container
docker ps                           # Check port mapping
docker inspect container_name       # Check network config

Out of disk space
docker system df           # Check usage
docker system prune -a     # Clean everything

Related Resources

See AgentUsage/docker_guide.md for complete documentation including:

Advanced multi-stage patterns
Docker Compose variations
Production optimization
CI/CD integration
Weekly Installs
68
Repository
autumnsgrove/groveengine
GitHub Stars
5
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail