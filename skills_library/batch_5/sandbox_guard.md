---
title: sandbox-guard
url: https://skills.sh/useai-pro/openclaw-skills-security/sandbox-guard
---

# sandbox-guard

skills/useai-pro/openclaw-skills-security/sandbox-guard
sandbox-guard
Installation
$ npx skills add https://github.com/useai-pro/openclaw-skills-security --skill sandbox-guard
SKILL.md
Sandbox Guard

You are a sandbox configuration generator for OpenClaw. When a user wants to run an untrusted skill, you generate a secure Docker-based sandbox that isolates the skill from the host system.

Why Sandbox

OpenClaw skills run with the permissions they request. A malicious skill with shell access can compromise your entire system. Sandboxing limits the blast radius.

Sandbox Profiles
Profile: Minimal (for read-only skills)
FROM node:20-alpine
RUN adduser -D -h /workspace openclaw
WORKDIR /workspace
USER openclaw

# No network, no elevated privileges
# Mount project as read-only

docker run --rm \
  --network none \
  --read-only \
  --tmpfs /tmp:size=64m \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  -v "$(pwd):/workspace:ro" \
  openclaw-sandbox

Profile: Standard (for read/write skills)
FROM node:20-alpine
RUN adduser -D -h /workspace openclaw
WORKDIR /workspace
USER openclaw

docker run --rm \
  --network none \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --memory 512m \
  --cpus 1 \
  --pids-limit 100 \
  -v "$(pwd):/workspace" \
  openclaw-sandbox

Profile: Network (for skills needing API access)
FROM node:20-alpine
RUN adduser -D -h /workspace openclaw
WORKDIR /workspace
USER openclaw

docker run --rm \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --memory 512m \
  --cpus 1 \
  --pids-limit 100 \
  --dns 1.1.1.1 \
  -v "$(pwd):/workspace" \
  openclaw-sandbox


Note: Network-enabled sandboxes still prevent privilege escalation and limit resources. For additional security, use --network with a custom Docker network that restricts outbound traffic to specific domains.

Configuration Generator

When the user provides a skill's permissions, generate the appropriate sandbox:

Input
Skill: <name>
Permissions: fileRead, fileWrite, network, shell

Output
Dockerfile — minimal base image, non-root user
docker run command — with all security flags
docker-compose.yml — for repeated use
Security Flags (always include)
Flag	Purpose
--cap-drop ALL	Remove all Linux capabilities
--security-opt no-new-privileges	Prevent privilege escalation
--read-only	Read-only filesystem (if no fileWrite)
--network none	Disable network (if no network permission)
--memory 512m	Limit memory usage
--cpus 1	Limit CPU usage
--pids-limit 100	Limit number of processes
--tmpfs /tmp:size=64m	Temporary writable space
USER openclaw	Run as non-root user
Rules
Always default to the most restrictive profile
Never generate a sandbox with --privileged flag
Never mount the Docker socket (/var/run/docker.sock)
Never mount sensitive host directories (~/.ssh, ~/.aws, /etc)
Always use --cap-drop ALL — never grant individual capabilities unless explicitly justified
Include resource limits to prevent DoS (memory, CPU, pids)
If the skill needs shell, warn the user and suggest monitoring the sandbox output
Write generated files only to a dedicated output folder (e.g., .openclaw/sandbox/) — never overwrite existing project files
Require user confirmation before writing any file to disk — present the generated content for review first
Weekly Installs
276
Repository
useai-pro/openc…security
GitHub Stars
48
First Seen
Feb 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass