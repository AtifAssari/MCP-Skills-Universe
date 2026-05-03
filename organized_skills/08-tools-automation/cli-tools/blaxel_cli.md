---
rating: ⭐⭐⭐
title: blaxel-cli
url: https://skills.sh/blaxel-ai/agent-skills/blaxel-cli
---

# blaxel-cli

skills/blaxel-ai/agent-skills/blaxel-cli
blaxel-cli
Installation
$ npx skills add https://github.com/blaxel-ai/agent-skills --skill blaxel-cli
SKILL.md
Blaxel CLI

A CLI to manage Blaxel cloud resources from the command line: agents, sandboxes, jobs, MCP servers, drives, and more.

Prerequisites

The bl command must be available on PATH. To check:

bl version


If not installed, install via the official install script:

curl -fsSL https://raw.githubusercontent.com/blaxel-ai/toolkit/main/install.sh | sh


Or via Homebrew:

brew tap blaxel-ai/blaxel && brew install blaxel


After installation, log in to your workspace:

bl login my-workspace

Global Flags

All commands support these flags:

Flag	Description
-o, --output <format>	Output format: pretty, yaml, json, table
-w, --workspace <name>	Override workspace for this command
-v, --verbose	Enable verbose output
-u, --utc	Enable UTC timezone
--skip-version-warning	Skip version warning
Non-Interactive Mode

For commands that prompt for input (confirmations, selections), add -y or --yes to auto-confirm. This is required when running in non-interactive / no-TTY environments (scripts, CI, agents).

Available Commands
bl apply       # Apply configuration changes to resources declaratively using YAML files.
bl chat        # Start an interactive chat session with a deployed agent.
bl connect     # Open an interactive terminal session to a sandbox
bl delete      # Delete Blaxel resources from your workspace.
bl deploy      # Deploy your Blaxel project to the cloud.
bl get         # Retrieve information about Blaxel resources in your workspace.
bl login       # Authenticate with Blaxel to access your workspace.
bl logout      # Remove stored credentials for a workspace.
bl logs        # View logs for Blaxel resources.
bl new         # Create a new Blaxel resource from templates.
bl push        # Build and push a container image to the Blaxel registry without creating a deployment.
bl run         # Execute a Blaxel resource with custom input data.
bl serve       # Start a local development server for your Blaxel project.
bl share       # Share Blaxel resources with other workspaces in your account.
bl token       # Retrieve the authentication token for the specified workspace.
bl unshare     # Remove shared Blaxel resources from other workspaces.
bl upgrade     # Upgrade the Blaxel CLI to the latest version.
bl version     # Print the version number
bl workspaces  # List and manage Blaxel workspaces.

Reference Documentation
apply - Apply configuration changes to resources declaratively using YAML files.
chat - Start an interactive chat session with a deployed agent.
connect - Open an interactive terminal session to a sandbox
delete - Delete Blaxel resources from your workspace.
deploy - Deploy your Blaxel project to the cloud.
get - Retrieve information about Blaxel resources in your workspace.
login - Authenticate with Blaxel to access your workspace.
logout - Remove stored credentials for a workspace.
logs - View logs for Blaxel resources.
new - Create a new Blaxel resource from templates.
push - Build and push a container image to the Blaxel registry without creating a deployment.
run - Execute a Blaxel resource with custom input data.
serve - Start a local development server for your Blaxel project.
share - Share Blaxel resources with other workspaces in your account.
token - Retrieve the authentication token for the specified workspace.
unshare - Remove shared Blaxel resources from other workspaces.
upgrade - Upgrade the Blaxel CLI to the latest version.
version - Print the version number
workspaces - List and manage Blaxel workspaces.
Discovering Options

To see available subcommands and flags, run --help on any command:

bl --help
bl deploy --help
bl get --help
bl get agents --help

Common Workflows
Create a sandbox, run a command, and get its logs
# 1. Create a sandbox with bl apply
bl apply -f - <<EOF
apiVersion: blaxel.ai/v1alpha1
kind: Sandbox
metadata:
  name: my-sandbox
spec:
  runtime:
    image: blaxel/base-image:latest
    memory: 2048
  lifecycle:
    expirationPolicies:
      - type: ttl-idle
        value: 1h       # Delete after 1 hour of inactivity. Units: h, d, w
        action: delete
EOF

# 2. Retrieve sandbox configuration
bl get sandbox my-sandbox

# 3. Execute a command in the sandbox and get stdout of the command
bl run sandbox my-sandbox --path /process --data '{"command": "echo hello world", "name": "my-cmd", "waitForCompletion": true}'

# 4. Retrieve the logs for that command in case stdout was not sufficient
bl logs sandbox my-sandbox my-cmd

Run a complex command in a sandbox (agent guideline)

bl run sandbox ... --path /process --data '<json>' requires the JSON payload to survive shell quoting. As soon as the command embeds nested quotes, backslashes, multiple lines, or interpreters like sh -lc / python3 -c, inline --data becomes brittle and the API rejects the request with 400 Bad Request: invalid character ... in string escape code.

Decision rule for an agent:

Command has no single quotes, no backslashes, no newlines → use --data '{"command": "...", "waitForCompletion": true}' directly.
Anything more complex (nested quotes, escapes, multiline, scripts) → write the JSON payload to a file with your Write/file-creation tool (this bypasses the shell entirely), then run with --file.
# Step 1 — agent writes /tmp/process.json with content like:
# {
#   "command": "sh -lc 'python3 -c \"print(\\\"hello\\\")\"'",
#   "name": "cve-check",
#   "waitForCompletion": true
# }
#
# Step 2 — execute it
bl run sandbox my-sandbox --path /process --file /tmp/process.json

Deploy an agent
bl new agent my-agent
cd my-agent
bl serve --hotreload    # Test locally
bl deploy               # Deploy to cloud
bl chat my-agent        # Chat with it

Manage sandboxes
bl get sandboxes                    # List all
bl get sandbox my-sandbox --watch   # Watch status
bl connect sandbox my-sandbox       # Interactive terminal
bl logs sandbox my-sandbox --follow # Stream logs
bl delete sandbox my-sandbox        # Clean up

Multi-workspace deployment
bl workspaces dev     # Switch to dev
bl deploy             # Deploy to dev
bl workspaces prod    # Switch to prod
bl deploy             # Deploy to prod

Weekly Installs
34
Repository
blaxel-ai/agent-skills
GitHub Stars
2
First Seen
3 days ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail