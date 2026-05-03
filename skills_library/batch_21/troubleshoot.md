---
title: troubleshoot
url: https://skills.sh/mwguerra/claude-code-plugins/troubleshoot
---

# troubleshoot

skills/mwguerra/claude-code-plugins/troubleshoot
troubleshoot
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill troubleshoot
SKILL.md
Docker Troubleshooting Skill
Overview

This skill helps diagnose and resolve common Docker issues:

Container startup failures
Networking problems
Permission errors
Port conflicts
Data persistence issues
Health check failures
Process
1. Consult Documentation

Read relevant documentation:

17-troubleshooting.md for common issues
15-port-conflicts.md for port problems
16-restart-strategies.md for restart issues
2. Diagnose Issue

Gather information:

# Check container status
docker compose ps -a

# View logs
docker compose logs servicename

# Check configuration
docker compose config

# Inspect container
docker inspect containername

3. Apply Solution
Common Issues and Solutions
Container Won't Start

Diagnosis:

docker compose logs servicename
docker inspect --format='{{.State.ExitCode}}' containername


Solutions:

Check logs for error messages
Verify configuration syntax
Check dependencies are running
Verify image exists
Port Already in Use

Diagnosis:

lsof -i :3000
# or
netstat -tulpn | grep 3000


Solutions:

# Kill process
kill $(lsof -t -i:3000)

# Or change port in compose
ports:
  - "3001:3000"

Permission Denied

Diagnosis:

docker compose exec app ls -la /app/data


Solutions:

# Fix in compose
services:
  app:
    user: "1000:1000"

# Or fix in container
docker compose exec -u root app chown -R appuser:appgroup /app/data

Data Disappearing

Diagnosis:

docker volume ls
docker compose config | grep -A5 "volumes:"


Solutions:

# Use named volumes instead of anonymous
volumes:
  - postgres_data:/var/lib/postgresql/data  # Named (persists)
  # NOT: - /var/lib/postgresql/data  # Anonymous (deleted)

Container Can't Reach Other Container

Diagnosis:

docker network inspect networkname
docker compose exec app ping db
docker compose exec app nslookup db


Solutions:

# Ensure same network
services:
  app:
    networks:
      - backend
  db:
    networks:
      - backend

networks:
  backend:

Health Check Failing

Diagnosis:

docker inspect --format='{{json .State.Health}}' containername | jq


Solutions:

healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s  # Give time to start

Out of Disk Space

Diagnosis:

docker system df
docker system df -v


Solutions:

# Clean unused resources
docker system prune -a --volumes

Build Cache Issues

Solutions:

docker compose build --no-cache
docker builder prune -a

Debugging Commands
# Shell into running container
docker compose exec app sh

# Shell into failed container
docker compose run --entrypoint sh app

# View resource usage
docker stats

# View container processes
docker compose top

# View real-time events
docker events

# Copy files from container
docker compose cp app:/app/logs ./logs

Quick Diagnostic Checklist
Check if container is running: docker compose ps
Check logs: docker compose logs servicename
Check network: docker network ls
Check volumes: docker volume ls
Check resources: docker stats
Validate config: docker compose config
Check disk space: docker system df
Error Messages Reference
Error	Cause	Solution
"port is already allocated"	Port in use	Kill process or change port
"network not found"	Missing network	Create network or check name
"volume not found"	Missing volume	Create volume or check name
"no such service"	Service name typo	Check compose.yaml
"unauthorized"	Auth issue	docker login
"image not found"	Missing image	docker compose pull
"permission denied"	File permissions	Fix ownership/permissions
"out of memory"	Memory limit	Increase limit or optimize app
Weekly Installs
17
Repository
mwguerra/claude…-plugins
GitHub Stars
29
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn