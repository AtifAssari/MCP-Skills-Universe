---
title: devcontainer-setup
url: https://skills.sh/shipshitdev/library/devcontainer-setup
---

# devcontainer-setup

skills/shipshitdev/library/devcontainer-setup
devcontainer-setup
Installation
$ npx skills add https://github.com/shipshitdev/library --skill devcontainer-setup
SKILL.md
Devcontainer Setup Skill

Set up a complete VS Code Dev Container configuration with Docker and Claude Code CLI support.

Information Gathering

Before creating the devcontainer, gather the following information from the user:

Required Information

Project Name: What is the project/container name? (e.g., my-project, shipshitdev-api)

Base Image: What runtime does this project use?

oven/bun:1.3.5 - Bun projects (recommended for speed)
node:20-slim - Node.js projects
node:20 - Node.js with more tools
Custom image path

Package Manager: Which package manager?

bun - Bun (default for Bun projects)
npm - npm
pnpm - pnpm
yarn - Yarn

Ports: What ports need to be forwarded? (comma-separated, e.g., 3000, 3001, 5432)

Port Labels (optional): Labels for each port (e.g., 3000=Web, 5432=Postgres)

Parent Directory Mount: Should the parent directory be mounted for cross-repo access?

Yes - Mount parent as /workspace (good for monorepos, shared libraries)
No - Only mount this project

Claude Code Support: Include Claude Code CLI setup?

Yes - Install Claude Code and fix symlinks for container use
No - Skip Claude Code setup

VS Code Extensions (optional): Additional extensions to install (comma-separated extension IDs)

Monorepo Structure (if applicable):

Is this a monorepo with nested package.json files?
What are the app/package directories? (e.g., apps/*, packages/*)
File Structure to Create
.devcontainer/
├── devcontainer.json      # VS Code dev container config
├── Dockerfile             # Container image definition
├── docker-compose.yml     # Docker compose config
├── setup.sh               # Post-create setup script
└── README.md              # Documentation

Template: devcontainer.json
{
  "name": "{{PROJECT_NAME}}",
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  },
  "workspaceFolder": "/workspace/{{PROJECT_DIR}}",
  "containerName": "{{PROJECT_NAME}}",

  // Mounts - adjust based on user preferences
  "mounts": [
    // If parent mount enabled:
    "source=${localWorkspaceFolder}/..,target=/workspace,type=bind,consistency=cached",
    // Mount host Claude config for plugins, settings, history
    "source=${localEnv:HOME}/.claude,target=/root/.claude,type=bind,consistency=cached"
  ],

  // Features to install
  "features": {
    "ghcr.io/devcontainers/features/git:1": {},
    "ghcr.io/devcontainers/features/github-cli:1": {},
    "ghcr.io/devcontainers/features/node:1": {
      "version": "lts"
    }
  },

  // VS Code extensions
  "customizations": {
    "vscode": {
      "extensions": [
        "dbaeumer.vscode-eslint",
        "biomejs.biome",
        "bradlc.vscode-tailwindcss",
        "esbenp.prettier-vscode",
        "ms-playwright.playwright",
        "ms-vscode.vscode-typescript-next"
        // Add user-specified extensions here
      ],
      "settings": {
        "editor.defaultFormatter": "biomejs.biome",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
          "quickfix.biome": "explicit",
          "source.organizeImports.biome": "explicit"
        }
      }
    }
  },

  // Forward ports
  "forwardPorts": [{{PORTS}}],
  "portsAttributes": {
    // Add port labels here
  },

  // Post-create command runs the setup script
  "postCreateCommand": "bash /workspace/{{PROJECT_DIR}}/.devcontainer/setup.sh",

  // Use root to avoid permission issues
  "remoteUser": "root",

  // Keep container running
  "overrideCommand": true
}

Template: Dockerfile
# Development container for {{PROJECT_NAME}}
FROM {{BASE_IMAGE}}

WORKDIR /workspace/{{PROJECT_DIR}}

# Install dependencies
COPY package.json {{LOCK_FILE}} {{ADDITIONAL_CONFIG_FILES}} ./
{{#if MONOREPO_DIRS}}
{{#each MONOREPO_DIRS}}
COPY {{this}} ./{{this}}
{{/each}}
{{/if}}

RUN {{INSTALL_COMMAND}}

# Install useful dev tools
RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Expose ports
EXPOSE {{PORTS}}

CMD ["sleep", "infinity"]

Template: docker-compose.yml
version: '3.8'

services:
  {{SERVICE_NAME}}:
    build:
      context: ..
      dockerfile: .devcontainer/Dockerfile
    container_name: {{PROJECT_NAME}}
    volumes:
      # Mount entire parent folder for cross-repo access (if enabled)
      - ../..:/workspace
      # Mount host Claude config
      - ~/.claude:/root/.claude
      # Preserve node_modules in container (performance)
      - /workspace/{{PROJECT_DIR}}/node_modules
      {{#each MONOREPO_NODE_MODULES}}
      - /workspace/{{PROJECT_DIR}}/{{this}}/node_modules
      {{/each}}
    ports:
      {{#each PORTS}}
      - "{{this}}:{{this}}"
      {{/each}}
    environment:
      - NODE_ENV=development
    stdin_open: true
    tty: true
    working_dir: /workspace/{{PROJECT_DIR}}
    command: {{DEV_COMMAND}}

Template: setup.sh
#!/bin/bash
# Setup script for devcontainer
# Fixes symlinks and installs dependencies

set -e

echo "Setting up devcontainer..."

# Install dependencies
cd /workspace/{{PROJECT_DIR}}
{{INSTALL_COMMAND}}

{{#if CLAUDE_CODE_SUPPORT}}
# Install Claude Code CLI
npm install -g @anthropic-ai/claude-code

# Fix Claude config symlinks to point to container paths
# The host symlinks point to /Users/... which don't exist in container
CLAUDE_DIR="/root/.claude"

# Find the library directory dynamically
# Check common locations: sibling directory, parent directory, or LIBRARY_PATH env var
find_library() {
    # Check environment variable first
    if [ -n "$LIBRARY_PATH" ] && [ -d "$LIBRARY_PATH/agents/.claude" ]; then
        echo "$LIBRARY_PATH/agents/.claude"
        return
    fi

    # Check /workspace/library (common devcontainer mount)
    if [ -d "/workspace/library/agents/.claude" ]; then
        echo "/workspace/library/agents/.claude"
        return
    fi

    # Check sibling directories for a library folder
    for dir in /workspace/*/agents/.claude; do
        if [ -d "$dir" ]; then
            echo "$dir"
            return
        fi
    done

    echo ""
}

LIBRARY_CLAUDE=$(find_library)

if [ -d "$CLAUDE_DIR" ] && [ -n "$LIBRARY_CLAUDE" ] && [ -d "$LIBRARY_CLAUDE" ]; then
    echo "Fixing Claude config symlinks..."
    echo "Library found at: $LIBRARY_CLAUDE"

    # Remove broken symlinks and create new ones
    for item in rules commands agents skills; do
        if [ -L "$CLAUDE_DIR/$item" ] || [ -e "$CLAUDE_DIR/$item" ]; then
            rm -f "$CLAUDE_DIR/$item"
        fi
        if [ -d "$LIBRARY_CLAUDE/$item" ]; then
            ln -sf "$LIBRARY_CLAUDE/$item" "$CLAUDE_DIR/$item"
            echo "  Linked $item -> $LIBRARY_CLAUDE/$item"
        fi
    done
else
    echo "Note: Ship Shit Dev Library not found. Symlinks not configured."
    echo "Set LIBRARY_PATH environment variable to the library root if needed."
fi
{{/if}}

echo "Setup complete!"
{{#if CLAUDE_CODE_SUPPORT}}
echo ""
echo "To use Claude Code, set your API key:"
echo "  export ANTHROPIC_API_KEY='your-key'"
echo ""
echo "Then run: claude"
{{/if}}

Template: README.md

Generate a README.md that documents:

Quick start instructions (VS Code and Docker Compose methods)
Container name for docker commands
Mount paths table
Directory structure diagram
Port mappings table
Claude Code usage (if enabled)
Troubleshooting section
Package Manager Reference
Package Manager	Lock File	Install Command	Dev Command
bun	bun.lock*	bun install --frozen-lockfile	bun run dev
npm	package-lock.json	npm ci	npm run dev
pnpm	pnpm-lock.yaml	pnpm install --frozen-lockfile	pnpm run dev
yarn	yarn.lock	yarn install --frozen-lockfile	yarn dev
Implementation Steps
Ask the user the required questions above using AskUserQuestion
Create the .devcontainer directory
Generate each file with the gathered configuration
Make setup.sh executable
Provide summary of what was created and how to use it
Example Usage

User: "Set up devcontainer for my Next.js project"

Gather info: Project uses Bun, ports 3000, needs Claude Code support
Create all 5 files in .devcontainer/
Output: "Created devcontainer configuration. Open in VS Code and click 'Reopen in Container'."
Weekly Installs
108
Repository
shipshitdev/library
GitHub Stars
21
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass