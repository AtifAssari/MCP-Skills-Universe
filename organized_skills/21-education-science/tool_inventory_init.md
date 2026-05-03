---
rating: ⭐⭐⭐
title: tool-inventory-init
url: https://skills.sh/richfrem/agent-plugins-skills/tool-inventory-init
---

# tool-inventory-init

skills/richfrem/agent-plugins-skills/tool-inventory-init
tool-inventory-init
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill tool-inventory-init
SKILL.md
Dependencies

This skill requires Python 3.8+ and standard library only. No external packages needed.

To install this skill's dependencies:

pip-compile ./requirements.in
pip install -r ./requirements.txt


See ./requirements.txt for the dependency lockfile (currently empty — standard library only).

Tool Inventory Init: The Librarian's Setup 🛠️

Initialize the semantic Tool Inventory for a new project. This is the first-run workflow for tracking executable scripts.

Architecture Note: This skill delegates the actual data storage and generation to the rlm-factory plugin, but it strongly enforces a pre-configured schema specifically for plugins/ and plugins/ scripts.

When to Use
Setting up Agent Skills inside a new root project repository.
Rebuilding the tool inventory ledger from scratch after severe corruption.
Moving from legacy JSON-only tracking to modern RLM tracking.
Interactive Setup Protocol
Step 1: Execute Initialization Script

Run the automated bootstrapping script. This script will ensure .agent/learning/rlm_profiles.json exists and will inject a tools profile if it doesn't.

python3 .agents/skills/tool-inventory-init/scripts/tool_inventory_init.py

Step 2: Serial Agent Distillation

The script above creates the target manifest, but YOU (the Agent) will execute the initial distillation pass if Ollama is unavailable, or you can delegate to batch mode if the project is massive.

Check what needs to be cached using the auditor:

# Hand off to the rlm-factory namespace
Trigger the 'rlm-curator' skill


If there are uncached tools:

Option A (Agent Distillation) - Recommended for < 20 tools: For each file identified as missing:

Read the tool script.
Summarize its purpose, layer, and CLI usage.
Trigger the 'rlm-curator' skill to inject the summary

Option B (Batch Distillation) - Recommended for > 20 tools:

# Hand off to the rlm-factory namespace
Trigger the 'rlm-distill-agent' skill

Step 3: Verify

Run the audit again to confirm 100% coverage:

# Hand off to the rlm-factory namespace
Trigger the 'rlm-curator' skill

After Init
The semantic registry is now active. You no longer need to run this command.
Use manage_tool_inventory.py (inside the tool-inventory skill) to register single new scripts organically during development.
Weekly Installs
21
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass