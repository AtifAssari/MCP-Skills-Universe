---
title: cli-anything-dify-workflow
url: https://skills.sh/hkuds/cli-anything/cli-anything-dify-workflow
---

# cli-anything-dify-workflow

skills/hkuds/cli-anything/cli-anything-dify-workflow
cli-anything-dify-workflow
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-dify-workflow
SKILL.md
Dify Workflow CLI Skill
Installation

Install the upstream Dify workflow CLI first:

python -m pip install "dify-ai-workflow-tools @ git+https://github.com/Akabane71/dify-workflow-cli.git@main"


Then install the CLI-Anything harness:

pip install git+https://github.com/HKUDS/CLI-Anything.git#subdirectory=dify-workflow/agent-harness

Usage

The harness forwards to the upstream dify-workflow CLI.

cli-anything-dify-workflow guide
cli-anything-dify-workflow list-node-types
cli-anything-dify-workflow create -o workflow.yaml --mode workflow --template llm
cli-anything-dify-workflow inspect workflow.yaml -j
cli-anything-dify-workflow validate workflow.yaml -j
cli-anything-dify-workflow edit add-node -f workflow.yaml --type code --title "Process"
cli-anything-dify-workflow config set-model -f app.yaml --provider openai --name gpt-4o

Command Groups
guide
list-node-types
create
inspect
validate
checklist
edit add-node|remove-node|update-node|add-edge|remove-edge|set-title
config set-model|set-prompt|add-variable|set-opening|add-question|add-tool|remove-tool
export
import
diff
layout
Agent Guidance
Prefer -j / --json-output on upstream commands when available.
The harness itself is a wrapper. Real workflow logic is provided by the upstream project.
If dify-workflow is not on PATH but the dify_workflow Python package is installed, the wrapper falls back to python -m dify_workflow.cli.
All operations are local file edits on Dify YAML/JSON DSL files.
Weekly Installs
93
Repository
hkuds/cli-anything
GitHub Stars
33.2K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykPass