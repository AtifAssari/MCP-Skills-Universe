---
title: muapi-workflow
url: https://skills.sh/samuraigpt/generative-media-skills/muapi-workflow
---

# muapi-workflow

skills/samuraigpt/generative-media-skills/muapi-workflow
muapi-workflow
Installation
$ npx skills add https://github.com/samuraigpt/generative-media-skills --skill muapi-workflow
SKILL.md
AI Workflow Builder

Chain any combination of muapi.ai generation steps into automated pipelines. The AI architect converts your plain-language description into a runnable node graph.

Prerequisites

Always ensure the muapi CLI is up-to-date before running any commands. Reinstall from source at the start of every session:

pip install --upgrade /path/to/muapi-cli


Replace /path/to/muapi-cli with the actual path to the muapi-cli directory in the workspace (the directory containing pyproject.toml).

Core Operations
Generate (generate-workflow.sh) — AI architect creates a workflow from a description
Discover (discover-workflow.sh) — Find a relevant existing workflow by natural language
Edit (generate-workflow.sh --workflow-id) — Modify an existing workflow with a prompt
Interactive Run (interactive-run.sh) — Prompt for inputs and execute a workflow
Run (run-workflow.sh) — Execute a workflow, poll node-by-node, collect outputs
CLI (muapi workflow) — Full CRUD + visualization directly from the terminal
Agent Guided Discovery & Selection

As an AI agent, you have the ability to read and understand the purpose of available workflows to select the best one for the user's task (e.g., "create a UGC video").

Discover: Fetch the catalog of available workflows and their descriptions in JSON format.
muapi workflow discover --output-json

Match (Internal Reasoning): Use your LLM capabilities to analyze the name, category, and description fields of the returned workflows. Find the best match for the user's intent.
Analyze: If you find a promising candidate, inspect its structure to ensure it has the necessary nodes and parameters.
muapi workflow get <workflow_id>

CRITICAL RULE: The output of muapi workflow get will include an "API Inputs" table. You MUST read this table to understand what inputs are required.
Choose & Confirm & Prompt User:
If one workflow is a perfect match, you MUST ask the user to provide the exact values for the required API inputs before executing it. Never invent or guess input values (like prompts, URLs, etc.) on your own.
If multiple workflows are highly relevant, present the options to the user with their descriptions and ask them to confirm which one to use, and also ask for the required inputs.
If no workflow matches the user's complex request, offer to architect a new one using muapi workflow create.
Example Agent Reasoning

"The user wants a product promo video. I fetched the catalog using discover. I see two potential workflows:

wf_123: 'Product promo with background music'
wf_456: 'Simple video gen' I will analyze wf_123 with get. It has the required nodes. I will suggest wf_123 or just run it if the match is precise."
Protocol: Building a Workflow
Step 1 — Describe your pipeline
muapi workflow create "take a text prompt, generate an image with flux-dev, then upscale it to 4K"


The architect returns a workflow with a unique ID and a node graph. Save the ID.

Step 2 — Inspect and visualize
# Rich ASCII node graph in the terminal
muapi workflow get <workflow_id>

# Or raw JSON
muapi workflow get <workflow_id> --output-json

Step 3 — Run it
# Run with specific inputs
muapi workflow execute <workflow_id> \
  --input "node1.prompt=a glowing crystal cave at midnight"

# Use --download to pull results locally
muapi workflow execute <workflow_id> \
  --input "node1.prompt=a sunset" \
  --download ./outputs

Step 4 — Discovery (Optional)

If you want to reuse an existing workflow instead of creating a new one:

# Search by keywords
muapi workflow discover "ugc video"

Step 5 — Interactive Execution

Run a workflow and have the CLI prompt you for each required input:

muapi workflow run-interactive <workflow_id>

Workflow Examples
Image Pipelines
# Text → Image → Upscale
muapi workflow create "take a text prompt, generate with flux-dev, upscale the result"

# Text → Image → Background removal → Product shot
muapi workflow create "generate a product image with hidream, remove background, create professional product shot"

Video Pipelines
# Text → Video
muapi workflow create "generate a 10-second cinematic video from a text prompt using kling-master"

# Image → Video → Lipsync
muapi workflow create "animate an input image with seedance, then apply lipsync from an audio file"

Editing an Existing Workflow
# Add a step
muapi workflow edit <id> --prompt "add a face-swap step after the image generation"

# Swap a model
muapi workflow edit <id> --prompt "change the video model from kling to veo3"

CLI Reference
# List all your workflows
muapi workflow list

# Browse templates
muapi workflow templates

# Generate new workflow
muapi workflow create "text → flux image → upscale → face swap"

# Visualize a workflow
muapi workflow get <id>

# Execute with inputs
muapi workflow execute <id> --input "node1.prompt=a sunset"

# Monitor a run
muapi workflow status <run_id>

# Get outputs
muapi workflow outputs <run_id> --download ./results

# Edit with AI
muapi workflow edit <id> --prompt "add lipsync at the end"

# Rename / delete
muapi workflow rename <id> --name "Product Pipeline v2"
muapi workflow delete <id>

MCP Tools (for AI agents)
Tool	Description
muapi_workflow_list	List user's workflows
muapi_workflow_create	AI architect: prompt → workflow
muapi_workflow_get	Get workflow definition + node graph
muapi_workflow_execute	Run with specific inputs
muapi_workflow_status	Node-by-node run status
muapi_workflow_outputs	Final output URLs
Constraints
Workflows can contain any combination of muapi.ai nodes (image, video, audio, enhance, edit)
Node outputs are automatically wired as inputs to downstream nodes
--sync mode waits up to 120s for generation; use --async for complex workflows and poll separately
Run timeouts: 10 minutes maximum per workflow execution
Weekly Installs
204
Repository
samuraigpt/gene…a-skills
GitHub Stars
3.2K
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail