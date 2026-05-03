---
title: agent-repo-init
url: https://skills.sh/study8677/antigravity-workspace-template/agent-repo-init
---

# agent-repo-init

skills/study8677/antigravity-workspace-template/agent-repo-init
agent-repo-init
Installation
$ npx skills add https://github.com/study8677/antigravity-workspace-template --skill agent-repo-init
SKILL.md
Agent Repo Init

Initialize a new project from this repository template with two modes.

Modes
quick: Fast scaffold with clean copy and minimal setup.
full: quick plus runtime profile setup (.env, mission, context profile, init report) and optional git init.
Run via Script

Use the portable script in this skill directory:

python skills/agent-repo-init/scripts/init_project.py \
  --project-name my-agent \
  --destination-root /absolute/path \
  --mode quick


Full mode example:

python skills/agent-repo-init/scripts/init_project.py \
  --project-name my-agent \
  --destination-root /absolute/path \
  --mode full \
  --llm-provider openai \
  --enable-mcp \
  --disable-swarm \
  --sandbox-runtime microsandbox \
  --init-git

Expected Output
New project at <destination_root>/<project_name>
Clean copy without local runtime state
Initialization report at artifacts/logs/agent_repo_init_report.md
Script is self-contained and does not import project src/ modules
Notes
Keep destination outside the current template repository.
For full mode, review .context/agent_runtime_profile.md after generation.
Weekly Installs
12
Repository
study8677/antig…template
GitHub Stars
1.1K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass