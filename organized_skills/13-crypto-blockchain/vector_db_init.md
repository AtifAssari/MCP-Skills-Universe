---
rating: ⭐⭐
title: vector-db-init
url: https://skills.sh/richfrem/agent-plugins-skills/vector-db-init
---

# vector-db-init

skills/richfrem/agent-plugins-skills/vector-db-init
vector-db-init
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill vector-db-init
SKILL.md
Dependencies

This skill requires Python 3.8+ and standard library only. No external packages needed.

To install this skill's dependencies:

pip-compile ./requirements.in
pip install -r ./requirements.txt


See ./requirements.txt for the dependency lockfile (currently empty — standard library only).

Vector DB Initialization

The vector-db-init skill is an automated setup routine that prepares the environment for the Vector DBMS.

Examples

Real-world examples of each config file are in references/examples/:

File	Purpose
vector_profiles.json	Profile registry -- defines named vector collections and ChromaDB connection
vector_knowledge_manifest.json	Manifest -- what folders/globs to include/exclude in the vector index
When to Use This
When a user first installs the vector-db plugin.
If the user complains that chromadb is not installed or ModuleNotFoundError is thrown.
If the Vector DB profile is missing from .agent/learning/vector_profiles.json.
Instructions for Agent

Run the Initialization Script: You must execute the interactive initialization script located at scripts/init.py.

python3 .agents/skills/vector-db-init/scripts/init.py


Wait for Completion: The script will automatically run pip install, then prompt the user to select their deployment architecture (In-Process or Native Server). All settings are written to .agent/learning/vector_profiles.json.

Verify: After the script completes successfully, inform the user that their environment is ready, and they can now run the vector-db-launch skill to start the background server (if they chose Option 2).

Weekly Installs
22
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass