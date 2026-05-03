---
rating: ⭐⭐⭐
title: docker-containerization
url: https://skills.sh/aj-geddes/useful-ai-prompts/docker-containerization
---

# docker-containerization

skills/aj-geddes/useful-ai-prompts/docker-containerization
docker-containerization
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill docker-containerization
SKILL.md
Docker Containerization
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build production-ready Docker containers following best practices for security, performance, and maintainability.

When to Use
Containerizing applications for deployment
Creating Dockerfiles for new services
Optimizing existing container images
Setting up development environments
Building CI/CD container pipelines
Implementing microservices
Quick Start

Minimal working example:

# Multi-stage build for Node.js application
# Stage 1: Build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:18-alpine
WORKDIR /app
# Copy only production dependencies and built files
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY package*.json ./

# Security: Run as non-root user
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
USER nodejs

EXPOSE 3000
CMD ["node", "dist/index.js"]

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Multi-Stage Builds	Multi-Stage Builds
Optimization Techniques	Optimization Techniques
Security Best Practices	Security Best Practices, Environment Configuration
Docker Compose for Multi-Container	Docker Compose for Multi-Container
.dockerignore File	.dockerignore File
Python	Python (Django/Flask), Java (Spring Boot), Go
Best Practices
✅ DO
Use official base images
Implement multi-stage builds
Run as non-root user
Use .dockerignore
Pin specific versions
Include health checks
Scan for vulnerabilities
Minimize layers
Use build caching effectively
❌ DON'T
Use 'latest' tag in production
Run as root user
Include secrets in images
Create unnecessary layers
Install unnecessary packages
Ignore security updates
Store data in containers
Weekly Installs
430
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass