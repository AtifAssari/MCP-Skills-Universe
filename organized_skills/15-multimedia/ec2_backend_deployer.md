---
rating: ⭐⭐
title: ec2-backend-deployer
url: https://skills.sh/shipshitdev/library/ec2-backend-deployer
---

# ec2-backend-deployer

skills/shipshitdev/library/ec2-backend-deployer
ec2-backend-deployer
Installation
$ npx skills add https://github.com/shipshitdev/library --skill ec2-backend-deployer
SKILL.md
EC2 Backend Deployer

Expert in deploying backend applications to EC2 instances using CI/CD pipelines, Docker containers, and GitHub Actions.

When to Use This Skill

Use when you're:

Setting up CI/CD for backend deployment to EC2
Configuring Docker-based deployments
Implementing automated deployment pipelines
Deploying NestJS, Next.js, or Express backends
Setting up container registries and image management
Configuring secure EC2 access (Tailscale)
Quick Workflow
Dockerfile: Multi-stage build (base → builder → production)
Registry: GitHub Container Registry (ghcr.io) recommended
CI/CD: GitHub Actions with Tailscale for secure SSH
Deploy: Docker Compose on EC2 with health checks
Verify: Health endpoint + deployment verification
Key Components
Docker
Multi-stage builds for smaller images
Non-root user for security
HEALTHCHECK for container orchestration
BuildKit secrets for sensitive data
GitHub Actions
docker/build-push-action for image building
tailscale/github-action for secure access
appleboy/ssh-action for deployment
EC2
Docker Compose v2 required
Health check verification
Rollback procedures
References
Full guide: Dockerfile, CI/CD workflow, deployment, troubleshooting
Weekly Installs
95
Repository
shipshitdev/library
GitHub Stars
21
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass