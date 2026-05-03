---
rating: ⭐⭐
title: create-docker-skill
url: https://skills.sh/richfrem/agent-plugins-skills/create-docker-skill
---

# create-docker-skill

skills/richfrem/agent-plugins-skills/create-docker-skill
create-docker-skill
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill create-docker-skill
SKILL.md

Follow the create-docker-skill skill workflow to scaffold a compliant agent skill that depends on containerized runtimes (Docker, Nextflow, HPC).

Inputs
$ARGUMENTS — optional skill name or use-case description. Omit to start with discovery.
Steps
If $ARGUMENTS provides a skill name, use it to seed the discovery phase
Follow the create-docker-skill phased workflow: determine container runtime and workflow type, gather environment check requirements, design pre-flight validation and subprocess execution scaffolding, then generate the skill directory
Report the created skill path and Docker environment setup instructions
Output

Skill directory with SKILL.md containing pre-flight environment checks, subprocess execution patterns, security-override config, and Docker-aware error handling.

Edge Cases
If $ARGUMENTS is empty: begin with discovery — do not assume Docker is available
If Docker is not installed in the target environment: generate graceful degradation
If the workflow uses HPC or Nextflow instead of Docker: adapt scaffolding accordingly
Weekly Installs
21
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykFail