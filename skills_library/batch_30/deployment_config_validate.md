---
title: deployment-config-validate
url: https://skills.sh/jsonlee12138/easy-deployment/deployment-config-validate
---

# deployment-config-validate

skills/jsonlee12138/easy-deployment/deployment-config-validate
deployment-config-validate
Installation
$ npx skills add https://github.com/jsonlee12138/easy-deployment --skill deployment-config-validate
SKILL.md
Deployment Config Validate
Validate only config-dependent stages.
Ensure Makefile deployment block and required targets exist.
Ensure .deploy.env.common and .deploy.env.<ENV_MODE> exist and merge correctly.
Ensure required keys and REMOTE_PORT are valid.
Validate compose file for stages that depend on compose.
Command
python3 skills/deployment-config-validate/scripts/validate_config.py \
  --root . \
  --env-mode test \
  --stage remote-deploy

Weekly Installs
17
Repository
jsonlee12138/ea…ployment
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass