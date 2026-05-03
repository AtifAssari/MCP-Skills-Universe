---
title: vm0-cli
url: https://skills.sh/vm0-ai/vm0-skills/vm0-cli
---

# vm0-cli

skills/vm0-ai/vm0-skills/vm0-cli
vm0-cli
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill vm0-cli
SKILL.md
VM0 CLI

Build and run AI agents in secure sandboxed environments using the VM0 command-line interface.

Official docs: https://docs.vm0.ai

When to Use

Use this skill when you need to:

Install and set up the VM0 CLI
Create and configure AI agent projects
Deploy agents to the VM0 platform
Run agents with prompts and inputs
Manage input files (volumes) and output files (artifacts)
View logs and usage statistics
Prerequisites
Installation

Install the VM0 CLI globally via npm:

npm install -g @vm0/cli


Tip: If you don't want to install globally, you can run VM0 CLI directly using npx -y @vm0/cli (e.g., npx -y @vm0/cli --version).

Verify installation:

vm0 --version

Authentication

Log in to your VM0 account:

vm0 auth login


This opens a browser for authentication. After login, verify status:

vm0 auth status


For CI/CD environments, get your API token:

vm0 auth setup-token


Then set the environment variable:

export VM0_TOKEN=vm0_live_your-api-key

Quick Start
1. Initialize a Project

Create a new VM0 project in the current directory:

vm0 init


This creates a vm0.yaml configuration file interactively. For non-interactive mode:

vm0 init --name my-agent

2. Configure the Agent

Edit vm0.yaml to define your agent:

version: "1.0"

agents:
  my-agent:
    framework: claude-code
    instructions: AGENTS.md
    skills:
      - https://github.com/vm0-ai/vm0-skills/tree/main/github
    environment:
      DEBUG: "${{ vars.DEBUG }}"
      API_KEY: "${{ secrets.API_KEY }}"

3. Deploy the Agent

Deploy your agent configuration:

vm0 compose vm0.yaml


Skip confirmation prompts with -y:

vm0 compose vm0.yaml -y

4. Run the Agent

Execute the agent with a prompt:

vm0 run my-agent "Please analyze the codebase and suggest improvements"


Or use cook for one-click execution from vm0.yaml:

vm0 cook "Analyze the code"

Core Operations
Running Agents

Basic run:

vm0 run my-agent "Your prompt here"


Run with variables and secrets:

vm0 run my-agent "Process data" --vars DEBUG=true --secrets API_KEY=xxx


Run with environment file:

vm0 run my-agent "Process data" --env-file=.env.local


Load environment variables from a file. The file should contain KEY=value pairs (one per line). This is useful for local development when you don't want to use the ${{ secrets.* }} syntax in vm0.yaml.

Example .env.local file:

GH_TOKEN=github_pat_xxx
API_KEY=sk-xxx
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/xxx


Run with artifact storage:

vm0 run my-agent "Generate report" --artifact-name my-output


Run with input volumes:

vm0 run my-agent "Process files" --volume-version input-data=latest


Enable verbose output:

vm0 run my-agent "Hello" -v


Resume from checkpoint:

vm0 run resume <checkpoint-id> "Continue the task"


Continue from session:

vm0 run continue <session-id> "Next step"

One-Click Execution (cook)

Run directly from vm0.yaml in current directory:

vm0 cook "Your prompt"


Skip confirmation:

vm0 cook -y "Your prompt"


Run with environment file:

vm0 cook --env-file=.env.local "Your prompt"


Load environment variables from a file for the agent run. Combine with -y to skip confirmation:

vm0 cook -y --env-file=.env.local "Your prompt"


Continue last session:

vm0 cook continue "Follow up"


Resume from last checkpoint:

vm0 cook resume "Continue"


View logs from last cook run:

vm0 cook logs

Viewing Logs

View agent events (default):

vm0 logs <run-id>


View system logs:

vm0 logs <run-id> --system


View metrics:

vm0 logs <run-id> --metrics


View network logs:

vm0 logs <run-id> --network


Filter by time:

vm0 logs <run-id> --since 5m
vm0 logs <run-id> --since 2h
vm0 logs <run-id> --since 2024-01-15T10:30:00Z


Show last N entries:

vm0 logs <run-id> --tail 20

Storage Management
Volumes (Input Files)

Volumes store input files that agents can read.

Initialize a volume (interactive):

cd my-data-directory
vm0 volume init


Initialize a volume (non-interactive):

cd my-data-directory
vm0 volume init --name my-data


Push local files to cloud:

vm0 volume push


Pull cloud files to local:

vm0 volume pull


Pull specific version:

vm0 volume pull abc123de


Check volume status:

vm0 volume status


List all volumes:

vm0 volume list


Clone a remote volume:

vm0 volume clone my-volume ./local-dir

Artifacts (Output Files)

Artifacts store output files created by agents.

Initialize an artifact (interactive):

cd my-output-directory
vm0 artifact init


Initialize an artifact (non-interactive):

cd my-output-directory
vm0 artifact init --name my-output


Push local files to cloud:

vm0 artifact push


Pull cloud files to local:

vm0 artifact pull


Pull specific version:

vm0 artifact pull abc123de


Check artifact status:

vm0 artifact status


List all artifacts:

vm0 artifact list


Clone a remote artifact:

vm0 artifact clone my-artifact ./local-dir

Agent Management
List Agents
vm0 agent list


With details:

vm0 agent list --verbose

Inspect Agent

View agent configuration:

vm0 agent inspect my-agent


View specific version:

vm0 agent inspect my-agent:abc123

Clone Agent

Download an agent's compose configuration to local directory:

vm0 agent clone my-agent


Clone to a specific directory:

vm0 agent clone my-agent ./my-project


This command:

Downloads compose configuration and saves as vm0.yaml
Downloads instructions file (e.g., AGENTS.md) if exists
Preserves environment variables with ${{ secrets.X }} syntax
Fails if destination directory already exists
Usage Statistics

View your usage statistics:

vm0 usage


Filter by date range:

vm0 usage --since 7d
vm0 usage --since 30d
vm0 usage --since 2024-01-01 --until 2024-01-31

Model Provider Configuration

Manage LLM model providers for agent runs.

Supported Provider Types
Type	Description
anthropic-api-key	Anthropic API key (Claude models)
openrouter-api-key	OpenRouter API with auto model routing
moonshot-api-key	Moonshot AI (Kimi) API key
minimax-api-key	MiniMax API key

List providers:

vm0 model-provider list


Setup a provider (interactive):

vm0 model-provider setup


Setup a provider (non-interactive):

vm0 model-provider setup --type anthropic-api-key --credential "sk-ant-xxx"


Set default provider:

vm0 model-provider set-default anthropic-api-key


Delete a provider:

vm0 model-provider delete anthropic-api-key

OpenRouter Provider

OpenRouter supports multiple model providers through a single API. Two modes available:

Auto mode (default): OpenRouter automatically routes to the best available model.

vm0 model-provider setup --type openrouter-api-key --credential "sk-or-xxx"


Explicit model selection: Specify a model from supported list.

vm0 model-provider setup --type openrouter-api-key --credential "sk-or-xxx" --model anthropic/claude-sonnet-4.5


Supported models include Claude (anthropic/claude-), Kimi (moonshotai/kimi-), DeepSeek (deepseek/), GLM (z-ai/glm-), MiniMax (minimax/), and Qwen (qwen/) series.

Secret Management

Store secrets remotely for agent runs. Secrets are for sensitive values (API keys, tokens) and are referenced in vm0.yaml as ${{ secrets.NAME }}.

List secrets:

vm0 secret list


Set a secret (interactive — prompts for value):

vm0 secret set MY_API_KEY


Set a secret (non-interactive):

vm0 secret set MY_API_KEY --body "sk-xxx-secret-value"


Set a secret with description:

vm0 secret set MY_API_KEY --body "sk-xxx" --description "OpenAI API key for summarization"


Delete a secret:

vm0 secret delete MY_API_KEY


Delete without confirmation:

vm0 secret delete MY_API_KEY -y

Variable Management

Store variables remotely for agent runs. Variables are for non-sensitive configuration and are referenced in vm0.yaml as ${{ vars.NAME }}.

List variables:

vm0 variable list


Set a variable:

vm0 variable set DEBUG true


Set a variable with description:

vm0 variable set ENV_NAME production --description "Target environment"


Delete a variable:

vm0 variable delete DEBUG


Delete without confirmation:

vm0 variable delete ENV_NAME -y

vm0.yaml Reference
Basic Structure
version: "1.0"

agents:
  agent-name:
    framework: claude-code
    instructions: AGENTS.md
    skills:
      - https://github.com/vm0-ai/vm0-skills/tree/main/github
      - https://github.com/vm0-ai/vm0-skills/tree/main/slack
    environment:
      VAR_NAME: "value"
      SECRET_VAR: "${{ secrets.SECRET_NAME }}"
      CONFIG_VAR: "${{ vars.CONFIG_NAME }}"

Fields
Field	Description
version	Configuration version (currently "1.0")
agents	Map of agent definitions
framework	Agent framework (e.g., claude-code)
instructions	Path to instructions file
skills	List of skill URLs to include
environment	Environment variables for the agent
Variable Syntax
${{ secrets.NAME }} - Sensitive values stored securely
${{ vars.NAME }} - Non-sensitive configuration values
Direct values - Plain text values
Environment Information

View system and environment details:

vm0 info

Non-Interactive Mode (CI/CD)

All commands support non-interactive mode for use in CI/CD pipelines, scripts, and automated environments. The CLI detects non-TTY environments (process.stdout.isTTY === false) and requires explicit flags for all inputs.

Authentication

Set the VM0_TOKEN environment variable instead of interactive login:

export VM0_TOKEN=vm0_live_your-api-key

Command Reference
Command	Non-Interactive Flags	Notes
vm0 init	--name <name>	Required in non-TTY
vm0 compose	-y, --yes	Skip new secrets confirmation
vm0 run	--env-file <file>	Load environment variables from file
vm0 cook	-y, --yes, --env-file <file>	Skip prompts; load env vars from file
vm0 volume init	--name <name>	Required in non-TTY
vm0 artifact init	--name <name>	Required in non-TTY
vm0 schedule init	--name, --frequency, --time, --prompt	All required; --day for weekly/monthly
vm0 schedule delete	-f, --force	Skip deletion confirmation
vm0 secret set	-b, --body <value>	Required in non-TTY
vm0 secret delete	-y, --yes	Skip confirmation
vm0 variable delete	-y, --yes	Skip confirmation
vm0 model-provider setup	--type <type> --credential <value>	Both required together
CI/CD Example
# Set authentication
export VM0_TOKEN=${{ secrets.VM0_TOKEN }}

# Initialize project (non-interactive)
vm0 init --name my-agent --force

# Initialize storage (non-interactive)
cd input-data && vm0 volume init --name input-data && cd ..
cd artifact && vm0 artifact init --name artifact && cd ..

# Deploy agent (skip confirmation)
vm0 compose vm0.yaml -y

# Run agent with environment file
vm0 run my-agent --artifact-name artifact --env-file=.env.local "Execute the task"

GitHub Actions Example
jobs:
  run-agent:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install VM0 CLI
        run: npm install -g @vm0/cli

      - name: Run Agent
        env:
          VM0_TOKEN: ${{ secrets.VM0_TOKEN }}
        run: |
          vm0 compose vm0.yaml -y
          vm0 run my-agent --artifact-name output --env-file=.env "Generate daily report"

Model Provider Setup (Non-Interactive)
vm0 model-provider setup --type anthropic-api-key --credential "sk-ant-xxx"

Guidelines
Always authenticate first - Run vm0 auth login before using other commands
Use vm0 init for new projects - Creates proper project structure
Deploy before running - Run vm0 compose after modifying vm0.yaml
Use volumes for input data - Push data files as volumes before running agents
Check logs for debugging - Use vm0 logs to troubleshoot failed runs
Use scopes for organization - Set appropriate scope for team collaboration
Common Workflows
Deploy and Run Agent
# 1. Initialize project
vm0 init --name my-agent

# 2. Edit vm0.yaml and AGENTS.md

# 3. Deploy configuration
vm0 compose vm0.yaml

# 4. Run the agent
vm0 run my-agent "Execute the task"

# 5. Check logs if needed
vm0 logs <run-id>

Provide Input Files to Agent
# 1. Create and navigate to data directory
mkdir input-data && cd input-data

# 2. Add your files
cp ~/documents/*.pdf .

# 3. Initialize and push volume (use --name for non-interactive)
vm0 volume init --name input-data
vm0 volume push

# 4. Run agent with volume
cd ..
vm0 run my-agent "Process the documents" --volume-version input-data=latest

Download Agent Output
# 1. List artifacts
vm0 artifact list

# 2. Clone the artifact locally
vm0 artifact clone my-output ./results

# 3. Or pull to existing directory
cd my-output-dir
vm0 artifact pull

Troubleshooting
Authentication Issues
# Check auth status
vm0 auth status

# Re-login if needed
vm0 auth logout
vm0 auth login

Agent Not Found
# List available agents
vm0 agent list

# Check if deployed
vm0 compose vm0.yaml

View Detailed Errors
# Use verbose mode
vm0 run my-agent "prompt" -v

# Check system logs
vm0 logs <run-id> --system

Weekly Installs
50
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail