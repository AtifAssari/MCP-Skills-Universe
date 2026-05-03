---
title: docker-patterns
url: https://skills.sh/langchain-ai/skills-benchmarks/docker-patterns
---

# docker-patterns

skills/langchain-ai/skills-benchmarks/docker-patterns
docker-patterns
Installation
$ npx skills add https://github.com/langchain-ai/skills-benchmarks --skill docker-patterns
SKILL.md
Docker Containerization Patterns

Build efficient, secure Docker images using modern patterns.

Multi-Stage Builds

Always use multi-stage builds to minimize image size:

# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# Production stage
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
USER node
CMD ["node", "server.js"]

Security Best Practices
Never run as root - use USER directive
Use specific version tags, not latest
Scan images with docker scout or Trivy
Use .dockerignore to exclude sensitive files
Health Checks
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

Compose Patterns
services:
  app:
    build:
      context: .
      target: production
    environment:
      - NODE_ENV=production
    deploy:
      resources:
        limits:
          memory: 512M

Weekly Installs
19
Repository
langchain-ai/sk…nchmarks
GitHub Stars
95
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass