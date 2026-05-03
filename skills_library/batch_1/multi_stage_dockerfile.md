---
title: multi-stage-dockerfile
url: https://skills.sh/github/awesome-copilot/multi-stage-dockerfile
---

# multi-stage-dockerfile

skills/github/awesome-copilot/multi-stage-dockerfile
multi-stage-dockerfile
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill multi-stage-dockerfile
Summary

Build optimized, secure multi-stage Dockerfiles for any language or framework.

Structures builds with separate builder and runtime stages, copying only necessary artifacts to minimize final image size and attack surface
Emphasizes layer caching optimization by ordering commands from least to most frequently changing, combined with .dockerignore and command consolidation
Recommends minimal base images (Alpine, distroless, or official slim variants) with exact version pinning for reproducibility
Covers security hardening: non-root users, build tool removal, vulnerability scanning, and secrets isolation through multi-stage separation
Includes performance patterns like build arguments, environment variable optimization, and healthcheck configuration for production readiness
SKILL.md

Your goal is to help me create efficient multi-stage Dockerfiles that follow best practices, resulting in smaller, more secure container images.

Multi-Stage Structure
Use a builder stage for compilation, dependency installation, and other build-time operations
Use a separate runtime stage that only includes what's needed to run the application
Copy only the necessary artifacts from the builder stage to the runtime stage
Use meaningful stage names with the AS keyword (e.g., FROM node:18 AS builder)
Place stages in logical order: dependencies → build → test → runtime
Base Images
Start with official, minimal base images when possible
Specify exact version tags to ensure reproducible builds (e.g., python:3.11-slim not just python)
Consider distroless images for runtime stages where appropriate
Use Alpine-based images for smaller footprints when compatible with your application
Ensure the runtime image has the minimal necessary dependencies
Layer Optimization
Organize commands to maximize layer caching
Place commands that change frequently (like code changes) after commands that change less frequently (like dependency installation)
Use .dockerignore to prevent unnecessary files from being included in the build context
Combine related RUN commands with && to reduce layer count
Consider using COPY --chown to set permissions in one step
Security Practices
Avoid running containers as root - use USER instruction to specify a non-root user
Remove build tools and unnecessary packages from the final image
Scan the final image for vulnerabilities
Set restrictive file permissions
Use multi-stage builds to avoid including build secrets in the final image
Performance Considerations
Use build arguments for configuration that might change between environments
Leverage build cache efficiently by ordering layers from least to most frequently changing
Consider parallelization in build steps when possible
Set appropriate environment variables like NODE_ENV=production to optimize runtime behavior
Use appropriate healthchecks for the application type with the HEALTHCHECK instruction
Weekly Installs
12.2K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass