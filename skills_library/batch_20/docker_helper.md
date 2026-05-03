---
title: docker-helper
url: https://skills.sh/jackspace/claudeskillz/docker-helper
---

# docker-helper

skills/jackspace/claudeskillz/docker-helper
docker-helper
Installation
$ npx skills add https://github.com/jackspace/claudeskillz --skill docker-helper
SKILL.md
Docker-helper
Instructions

When helping with Docker tasks:

Check running containers: docker ps -a
View logs: docker logs -f
Inspect container: docker inspect
Execute commands: docker exec -it /bin/bash
Use multi-stage builds to reduce image size
Order Dockerfile commands by frequency of change
Use .dockerignore to exclude unnecessary files
Avoid running as root; create non-privileged users
Use health checks in docker-compose
Networking: Check bridge networks and port mappings
Volumes: Verify volume mounts and permissions
Build cache: Use --no-cache when needed
Resource limits: Set memory/CPU limits appropriately
Use version 3+ syntax
Leverage environment files (.env)
Use depends_on with health checks
Implement restart policies
Examples

Add examples of how to use this skill here.

Notes
This skill was auto-generated
Edit this file to customize behavior
Weekly Installs
45
Repository
jackspace/claudeskillz
GitHub Stars
14
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass