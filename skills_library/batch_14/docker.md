---
title: docker
url: https://skills.sh/stuartf303/sorcha/docker
---

# docker

skills/stuartf303/sorcha/docker
docker
Installation
$ npx skills add https://github.com/stuartf303/sorcha --skill docker
SKILL.md
Docker Skill

Sorcha uses Docker for local development and production deployment. Services run as Ubuntu Chiseled (distroless) containers with multi-stage builds. Docker Compose orchestrates the full stack with health checks, shared networks, and volume mounts for persistence.

Quick Start
Start Full Stack
# Start all services with infrastructure
docker-compose up -d

# View logs for specific service
docker-compose logs -f blueprint-service

# Rebuild single service after code changes
docker-compose build blueprint-service && docker-compose up -d --force-recreate blueprint-service

Infrastructure Only (for Aspire development)
# Start databases without application services
docker-compose -f docker-compose.infrastructure.yml up -d

Key Concepts
Concept	Usage	Example
Chiseled images	Distroless for security	mcr.microsoft.com/dotnet/aspnet:10.0-noble-chiseled
Multi-stage builds	Separate build/runtime	FROM sdk AS build → FROM aspnet AS final
YAML anchors	Shared env config	<<: [*otel-env, *jwt-env]
Health checks	Startup dependencies	condition: service_healthy
Bridge network	Service DNS	http://wallet-service:8080
Common Patterns
Service Definition with Dependencies

When: Adding a new microservice

my-service:
  build:
    context: .
    dockerfile: src/Services/Sorcha.MyService/Dockerfile
  image: sorcha/my-service:latest
  container_name: sorcha-my-service
  restart: unless-stopped
  environment:
    <<: [*otel-env, *jwt-env]
    OTEL_SERVICE_NAME: my-service
    ASPNETCORE_ENVIRONMENT: Development
    ASPNETCORE_URLS: http://+:8080
    ConnectionStrings__Redis: redis:6379
  volumes:
    - dataprotection-keys:/home/app/.aspnet/DataProtection-Keys
  depends_on:
    redis:
      condition: service_healthy
  networks:
    - sorcha-network

Multi-Stage Dockerfile

When: Creating Dockerfile for .NET service

FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src
COPY ["src/Services/Sorcha.MyService/Sorcha.MyService.csproj", "src/Services/Sorcha.MyService/"]
RUN dotnet restore "src/Services/Sorcha.MyService/Sorcha.MyService.csproj"
COPY src/ ./src/
RUN dotnet publish "src/Services/Sorcha.MyService/Sorcha.MyService.csproj" -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:10.0-noble-chiseled AS final
WORKDIR /app
COPY --from=publish /app/publish .
USER $APP_UID
ENTRYPOINT ["dotnet", "Sorcha.MyService.dll"]

See Also
docker - Container patterns and anti-patterns
ci-cd - GitHub Actions workflows
deployment - Production deployment
monitoring - OpenTelemetry and Aspire Dashboard
Related Skills
See the aspire skill for .NET Aspire orchestration patterns
See the postgresql skill for database container configuration
See the mongodb skill for document database setup
See the redis skill for caching container patterns
See the yarp skill for API Gateway routing configuration
Documentation Resources

Fetch latest Docker documentation with Context7.

How to use Context7:

Use mcp__context7__resolve-library-id to search for "docker"
Prefer website documentation (IDs starting with /websites/) over source code repositories
Query with mcp__context7__query-docs using the resolved library ID

Library ID: /websites/docker (resolve using mcp__context7__resolve-library-id, prefer /websites/ when available)

Recommended Queries:

"docker compose health checks"
"multi-stage build best practices"
"docker networking bridge mode"
Weekly Installs
26
Repository
stuartf303/sorcha
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn