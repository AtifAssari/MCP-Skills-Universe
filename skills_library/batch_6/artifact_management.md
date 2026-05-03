---
title: artifact-management
url: https://skills.sh/aj-geddes/useful-ai-prompts/artifact-management
---

# artifact-management

skills/aj-geddes/useful-ai-prompts/artifact-management
artifact-management
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill artifact-management
SKILL.md
Artifact Management
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive artifact management strategies for storing, versioning, and distributing built binaries, Docker images, and packages across environments.

When to Use
Docker image registry management
Package publication and versioning
Build artifact storage and retrieval
Container image optimization
Artifact retention policies
Multi-registry distribution
Dependency caching
Quick Start

Minimal working example:

# Dockerfile with multi-stage build for optimization
FROM node:18-alpine AS dependencies
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:18-alpine AS runtime
WORKDIR /app
COPY --from=dependencies /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY package*.json ./

EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
  CMD node healthcheck.js

CMD ["node", "dist/server.js"]

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Docker Registry Configuration	Docker Registry Configuration
GitHub Container Registry (GHCR) Push	GitHub Container Registry (GHCR) Push
npm Package Publishing	npm Package Publishing, Artifact Retention Policy, Artifact Versioning, GitLab Package Registry
Best Practices
✅ DO
Use semantic versioning for artifacts
Implement image scanning before deployment
Set retention policies for old artifacts
Use multi-stage builds for Docker images
Sign and verify artifacts
Implement artifact immutability
Document artifact metadata
Use specific base image versions
Implement vulnerability scanning
Cache layers aggressively
Tag images with commit SHA
Compress artifacts for storage
❌ DON'T
Use latest tag as sole identifier
Store secrets in artifacts
Push artifacts without scanning
Use untrusted base images
Skip artifact verification
Overwrite published artifacts
Mix binary and source artifacts
Ignore image layer optimization
Store build logs with sensitive data
Weekly Installs
267
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