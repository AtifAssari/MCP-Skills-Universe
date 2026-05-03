---
title: extension-guide-v2
url: https://skills.sh/pacphi/sindri/extension-guide-v2
---

# extension-guide-v2

skills/pacphi/sindri/extension-guide-v2
extension-guide-v2
Installation
$ npx skills add https://github.com/pacphi/sindri --skill extension-guide-v2
SKILL.md
Sindri V2 Extension Development Guide

V2 extensions are YAML-driven, declarative configurations for the Bash/Docker-based Sindri platform.

V2 Paths and Resources
Resource	Path
Extensions Directory	v2/docker/lib/extensions/
Schema	v2/docker/lib/schemas/extension.schema.json
Registry	v2/docker/lib/registry.yaml
Categories	v2/docker/lib/categories.yaml
Profiles	v2/docker/lib/profiles.yaml
Extension Docs	docs/extensions/{NAME}.md
VisionFlow Docs	docs/extensions/vision-flow/VF-{NAME}.md
V2 Categories
# Valid V2 categories
- base          # Core system components
- agile         # Project management (Jira, Linear)
- language      # Programming runtimes
- dev-tools     # Development tools
- infrastructure # Cloud/container tools
- ai            # AI/ML tools
- database      # Database servers
- monitoring    # Observability tools
- mobile        # Mobile SDKs
- desktop       # GUI environments
- utilities     # General tools

Quick Start Checklist
 Create directory: v2/docker/lib/extensions/{name}/
 Create extension.yaml with required sections
 Add to v2/docker/lib/registry.yaml
 Validate: ./v2/cli/extension-manager validate {name}
 Test: ./v2/cli/extension-manager install {name}
 Create docs: docs/extensions/{NAME}.md
 Update catalog: v2/docs/EXTENSIONS.md
Extension Directory Structure
v2/docker/lib/extensions/{name}/
├── extension.yaml       # Required: Main definition
├── mise.toml            # Optional: mise configuration
├── scripts/             # Optional: Custom scripts
│   ├── install.sh
│   ├── uninstall.sh
│   └── validate.sh
└── templates/           # Optional: Config templates
    └── config.template

Minimal Extension Template
metadata:
  name: my-extension
  version: 1.0.0
  description: Brief description (10-200 chars)
  category: dev-tools
  dependencies: []

install:
  method: mise
  mise:
    configFile: mise.toml

validate:
  commands:
    - name: mytool
      versionFlag: --version
      expectedPattern: "v\\d+\\.\\d+\\.\\d+"

Install Methods
mise (Recommended for language tools)
install:
  method: mise
  mise:
    configFile: mise.toml
    reshimAfterInstall: true

apt (System packages)
install:
  method: apt
  apt:
    repositories:
      - name: docker
        key: https://download.docker.com/linux/ubuntu/gpg
        url: https://download.docker.com/linux/ubuntu
        suite: jammy
        component: stable
    packages:
      - docker-ce
      - docker-ce-cli

binary (Direct download)
install:
  method: binary
  binary:
    url: https://github.com/org/repo/releases/download/v1.0.0/tool.tar.gz
    extract: tar.gz  # tar.gz, zip, or none
    destination: ~/.local/bin/tool

npm (Node.js packages)
install:
  method: npm
  npm:
    packages:
      - typescript
      - eslint@8.0.0
    global: true

script (Custom installation)
install:
  method: script
  script:
    path: scripts/install.sh
    timeout: 300

hybrid (Multiple methods)
install:
  method: hybrid
  hybrid:
    steps:
      - method: apt
        apt:
          packages: [build-essential]
      - method: script
        script:
          path: scripts/install.sh

Capabilities (Optional - Advanced Extensions)

Most extensions don't need capabilities. Only use for extensions requiring:

Project initialization (e.g., claude-flow init)
Authentication validation
Lifecycle hooks
MCP server registration
capabilities:
  # Project initialization
  project-init:
    enabled: true
    commands:
      - command: "mytool init --force"
        description: "Initialize mytool"
        requiresAuth: anthropic  # or: openai, github, none
        conditional: false
    state-markers:
      - path: ".mytool"
        type: directory
        description: "Config directory"
    validation:
      command: "mytool --version"
      expectedPattern: "^\\d+\\.\\d+"

  # Authentication
  auth:
    provider: anthropic
    required: false
    methods: [api-key, cli-auth]
    envVars: [ANTHROPIC_API_KEY]
    validator:
      command: "claude --version"
      expectedExitCode: 0
    features:
      - name: agent-spawn
        requiresApiKey: false
        description: "CLI-based features"

  # Lifecycle hooks
  hooks:
    pre-install:
      command: "echo 'Preparing...'"
      description: "Pre-install checks"
    post-install:
      command: "mytool --version"
      description: "Verify installation"

  # MCP server
  mcp:
    enabled: true
    server:
      command: "npx"
      args: ["-y", "@mytool/mcp", "start"]
      env:
        MYTOOL_MCP_MODE: "1"
    tools:
      - name: "mytool-action"
        description: "Perform action"

Registry Entry

Add to v2/docker/lib/registry.yaml:

extensions:
  my-extension:
    category: dev-tools
    description: Short description
    dependencies: [nodejs]
    protected: false

Validation Commands
# Validate single extension
./v2/cli/extension-manager validate my-extension

# Validate all extensions
./v2/cli/extension-manager validate-all

# Check extension info
./v2/cli/extension-manager info my-extension

# Test installation
./v2/cli/extension-manager install my-extension

# Check status
./v2/cli/extension-manager status my-extension

Common Patterns
Language Runtime (No Capabilities)
# v2/docker/lib/extensions/nodejs/extension.yaml
metadata:
  name: nodejs
  version: 1.0.0
  description: Node.js LTS via mise
  category: language

install:
  method: mise
  mise:
    configFile: mise.toml

validate:
  commands:
    - name: node
      expectedPattern: "v\\d+\\.\\d+\\.\\d+"
    - name: npm

bom:
  tools:
    - name: node
      version: dynamic
      source: mise
      type: runtime
      license: MIT

AI Tool with Capabilities
# Extensions like claude-flow-v2, agentic-qe, spec-kit
metadata:
  name: ai-tool
  version: 1.0.0
  description: AI-powered tool
  category: ai
  dependencies: [nodejs]

install:
  method: mise
  mise:
    configFile: mise.toml

capabilities:
  project-init:
    enabled: true
    commands:
      - command: "ai-tool init"
        description: "Initialize project"
        requiresAuth: anthropic
    state-markers:
      - path: ".ai-tool"
        type: directory

  auth:
    provider: anthropic
    methods: [api-key, cli-auth]

  mcp:
    enabled: true
    server:
      command: "npx"
      args: ["-y", "@ai-tool/mcp"]
    tools:
      - name: "ai-tool-action"
        description: "Perform AI action"

V2-Specific Features
VisionFlow Extensions

VisionFlow extensions use the vf- prefix and are only available in V2:

v2/docker/lib/extensions/vf-{name}/
├── extension.yaml
└── ...


Document in: docs/extensions/vision-flow/VF-{NAME}.md

Shell Aliases

V2 supports 158+ shell aliases defined in extensions. These are configured in the configure.environment section with scope: bashrc.

Script Requirements

All scripts must:

#!/usr/bin/env bash
set -euo pipefail

echo "Installing..."
# Commands here
echo "Done"

Post-Extension Documentation

After creating an extension, update:

Registry: v2/docker/lib/registry.yaml
Extension Doc: docs/extensions/{NAME}.md
Catalog: v2/docs/EXTENSIONS.md
Profiles (if applicable): v2/docker/lib/profiles.yaml
Troubleshooting
Issue	Solution
Schema validation fails	Check YAML syntax, verify required fields
Dependencies not found	Add to registry.yaml first
Install times out	Increase timeout in script section
Validation fails	Check regex escaping in expectedPattern
Weekly Installs
19
Repository
pacphi/sindri
GitHub Stars
12
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn