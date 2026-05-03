---
rating: ⭐⭐
title: eve-se-index
url: https://skills.sh/incept5/eve-skillpacks/eve-se-index
---

# eve-se-index

skills/incept5/eve-skillpacks/eve-se-index
eve-se-index
Installation
$ npx skills add https://github.com/incept5/eve-skillpacks --skill eve-se-index
SKILL.md
Eve SE Index (Load First)

Use this skill as the entry point for Eve SE. It routes to the correct skill for the task.

Scope

Eve SE is for app developers using Eve to deploy and run their apps. It does not cover operating the Eve platform itself.

Quick Routing
Need	Load this skill
Full onboarding (new or existing user)	eve-bootstrap
Understand Eve CLI primitives	eve-cli-primitives
Set up a new project from the starter	eve-new-project-setup
Connect an existing repo to Eve (already authed)	eve-project-bootstrap
Implement a plan via Eve jobs	eve-plan-implementation
Edit the manifest	eve-manifest-authoring
Configure auth + secrets	eve-auth-and-secrets
Local docker-compose dev loop	eve-local-dev-loop
Deploy to staging + debug	eve-deploy-debugging
Pipelines + workflows	eve-pipelines-workflows
Troubleshoot failures	eve-troubleshooting
Keep repo aligned with platform	eve-repo-upkeep
Web UI testing with agent-browser	eve-web-ui-testing-agent-browser
Author verification plans for an app	eve-verification-plans
Design an agent-native app	eve-agent-native-design (eve-design pack)
Default Workflow (Local -> Staging)
Run locally with Docker Compose: eve-local-dev-loop.
Ensure manifest matches runtime: eve-manifest-authoring.
Set secrets and auth: eve-auth-and-secrets.
Deploy to staging and debug: eve-deploy-debugging.
What This Pack Does NOT Cover
Running Eve Horizon itself (k8s, docker, infra)
Platform operator workflows (./bin/eh, cluster secrets)

If you need platform operations, load the private eve-dev pack instead.

Weekly Installs
238
Repository
incept5/eve-skillpacks
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass