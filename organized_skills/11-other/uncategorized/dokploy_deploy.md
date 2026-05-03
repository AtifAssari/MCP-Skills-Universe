---
rating: ⭐⭐⭐
title: dokploy-deploy
url: https://skills.sh/jpropato/siba/dokploy-deploy
---

# dokploy-deploy

skills/jpropato/siba/dokploy-deploy
dokploy-deploy
Installation
$ npx skills add https://github.com/jpropato/siba --skill dokploy-deploy
SKILL.md
Dokploy Deployment

This skill enables you to manage and deploy applications to a Dokploy instance. Dokploy is an open-source PaaS (Platform as a Service) that simplifies deployment on your own VPS.

Prerequisites
Access to a Dokploy instance.
Dokploy CLI installed (npm install -g dokploy).
API Token (generated from Dokploy Dashboard > Settings > Profile).
How to Deploy
1. Using Dokploy CLI

If the CLI is available in the environment:

# Login
dokploy login --host <your-dokploy-host> --token <your-token>

# Create a Project (if not exists)
dokploy project create --name <project-name>

# Create an Application
dokploy app create --name <app-name> --projectName <project-name>

# Deploy
dokploy app deploy --name <app-name> --projectName <project-name>

2. Manual Deployment via Dashboard
Navigate to your Dokploy host (e.g., http://vps-ip:3000).
Create or select a Project.
Add a new Service > Application.
Connect your Git Repository (GitHub/GitLab) or use a Docker Image.
Configure Nixpacks or Dockerfile for the build.
Click Deploy.
Best Practices
Environment Variables: Always use the Dokploy dashboard or CLI to set secrets. Do not commit .env files.
Health Checks: Configure health checks in the Dokploy dashboard to ensure zero-downtime deployments.
Nixpacks: Prefers Nixpacks for automatic language detection and build optimization.
Triggering via API

You can trigger a deployment programmatically using a POST request to the Dokploy API:

POST https://<your-dokploy-host>/api/deployments/deploy
Authorization: Bearer <your-token>
Content-Type: application/json

{
  "applicationId": "<your-application-id>"
}

Weekly Installs
46
Repository
jpropato/siba
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail