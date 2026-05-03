---
title: docker-deployment
url: https://skills.sh/aaaaqwq/claude-code-skills/docker-deployment
---

# docker-deployment

skills/aaaaqwq/claude-code-skills/docker-deployment
docker-deployment
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill docker-deployment
SKILL.md
Docker Deployment with Nginx HTTPS
Quick Start

For Docker web application deployment with HTTPS support:

Configure Nginx with SSL certificates (see nginx-https.md)
Set up docker-compose.yml with certificate volume mounting
Configure Cloudflare Tunnel to connect external domain to local container
Common Tasks
Task	Reference
Nginx HTTPS configuration	nginx-https.md
Cloudflare Origin Certificate	cf-origin-cert.md
Docker data persistence	data-persistence.md
Cloudflare Tunnel setup	cf-tunnel.md
Architecture Overview
Internet → Cloudflare Edge (HTTPS) → Cloudflare Tunnel → Ubuntu/Docker (Nginx)

Key Principles
Always use named Docker volumes for persistent data
Nginx should redirect HTTP (80) to HTTPS (443) in production
Cloudflare Origin Certificates are for CF-to-origin encryption only
Tunnel connects to HTTP or HTTPS - configure based on nginx setup
Troubleshooting

HTTPS not working after enabling Cloudflare force HTTPS?

Check if nginx listens on port 443
Verify SSL certificates are mounted correctly
Ensure Cloudflare Tunnel service URL matches (http:// or https://)

Data lost after container restart?

Check docker-compose.yml uses named volumes, not bind mounts for critical data
Verify database path points to mounted volume directory

See individual reference files for detailed solutions.

Weekly Installs
47
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn