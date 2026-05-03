---
title: dockerize-project
url: https://skills.sh/gemini960114/skills/dockerize-project
---

# dockerize-project

skills/gemini960114/skills/dockerize-project
dockerize-project
Installation
$ npx skills add https://github.com/gemini960114/skills --skill dockerize-project
SKILL.md
Dockerize Current Project (Minimal)
Goal

Analyze the current project’s files and generate a minimal, working Dockerfile and docker-compose.yml so the project can be started with docker compose up --build.

Instructions
Inspect the current project structure and identify the primary tech stack:
Python (pyproject.toml, uv.lock, requirements.txt, manage.py, app.py, main.py)
Node.js (package.json)
Other / generic
Check whether Docker-related files already exist:
Dockerfile
docker-compose.yml / docker-compose.yaml
.dockerignore
If any exist, do NOT overwrite them. Ask the user whether to merge, regenerate with backups, or cancel.
Infer a reasonable default entrypoint and port from the codebase.
If the entrypoint or port is unclear, ask up to three concise clarification questions.
Generate the following files as complete code blocks:
Dockerfile (development-oriented, readable, non-root when reasonable)
docker-compose.yml (no version: field)
.dockerignore
Prefer bind mounts for local development and explain how to change this if needed.
Constraints
Do not use sudo.
Do not hardcode secrets; use environment variables or an .env / .env.docker template if necessary.
Do not run Docker commands automatically.
Keep the setup minimal and easy to modify.
Output Format
Detection Summary
Detected stack
Assumed entrypoint
Assumed port
Generated Files
Dockerfile
docker-compose.yml
.dockerignore
How to Run
docker compose up --build
Common commands (logs, exec)
Notes
What to change if the entrypoint, port, or environment differs.
Example

User: Dockerize this project for local development
Result:

Detect Python project
Generate Dockerfile + docker-compose.yml
Explain how to start and customize
Weekly Installs
12
Repository
gemini960114/skills
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass