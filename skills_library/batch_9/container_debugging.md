---
title: container-debugging
url: https://skills.sh/aj-geddes/useful-ai-prompts/container-debugging
---

# container-debugging

skills/aj-geddes/useful-ai-prompts/container-debugging
container-debugging
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill container-debugging
SKILL.md
Container Debugging
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Container debugging focuses on issues within Docker/Kubernetes environments including resource constraints, networking, and application runtime problems.

When to Use
Container won't start
Application crashes in container
Resource limits exceeded
Network connectivity issues
Performance problems in containers
Quick Start

Minimal working example:

# Check container status
docker ps -a
docker inspect <container-id>
docker stats <container-id>

# View container logs
docker logs <container-id>
docker logs --follow <container-id>  # Real-time
docker logs --tail 100 <container-id>  # Last 100 lines

# Connect to running container
docker exec -it <container-id> /bin/bash
docker exec -it <container-id> sh

# Inspect container details
docker inspect <container-id> | grep -A 5 "State"
docker inspect <container-id> | grep -E "Memory|Cpu"

# Check container processes
docker top <container-id>

# View resource usage
docker stats <container-id>
# Shows: CPU%, Memory usage, Network I/O

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Docker Debugging Basics	Docker Debugging Basics
Common Container Issues	Common Container Issues
Container Optimization	Container Optimization
Debugging Checklist	Debugging Checklist
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
299
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