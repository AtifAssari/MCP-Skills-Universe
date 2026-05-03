---
title: nx-workspace
url: https://skills.sh/nrwl/nx-ai-agents-config/nx-workspace
---

# nx-workspace

skills/nrwl/nx-ai-agents-config/nx-workspace
nx-workspace
Installation
$ npx skills add https://github.com/nrwl/nx-ai-agents-config --skill nx-workspace
Summary

Read-only exploration of Nx workspace structure, projects, configuration, and dependencies.

Query workspace projects with filtering by name, glob patterns, tags, and target availability using nx show projects
Retrieve full resolved project configuration including inferred targets via nx show project <name> --json, avoiding partial project.json reads
Inspect target definitions, executors, options, inputs, and outputs to understand available tasks and caching behavior
Analyze project dependencies and dependents through the project graph using nx graph --print
Use jq and command-line tools to programmatically process JSON output rather than manual parsing
SKILL.md
Nx Workspace Exploration

This skill provides read-only exploration of Nx workspaces. Use it to understand workspace structure, project configuration, available targets, and dependencies.

Keep in mind that you might have to prefix commands with npx/pnpx/yarn if nx isn't installed globally. Check the lockfile to determine the package manager in use.

Listing Projects

Use nx show projects to list projects in the workspace.

The project filtering syntax (-p/--projects) works across many Nx commands including nx run-many, nx release, nx show projects, and more. Filters support explicit names, glob patterns, tag references (e.g. tag:name), directories, and negation (e.g. !project-name).

# List all projects
nx show projects

# Filter by pattern (glob)
nx show projects --projects "apps/*"
nx show projects --projects "shared-*"

# Filter by tag
nx show projects --projects "tag:publishable"
nx show projects -p 'tag:publishable,!tag:internal'

# Filter by target (projects that have a specific target)
nx show projects --withTarget build

# Combine filters
nx show projects --type lib --withTarget test
nx show projects --affected --exclude="*-e2e"
nx show projects -p "tag:scope:client,packages/*"

# Negate patterns
nx show projects -p '!tag:private'
nx show projects -p '!*-e2e'

# Output as JSON
nx show projects --json

Project Configuration

Use nx show project <name> --json to get the full resolved configuration for a project.

Important: Do NOT read project.json directly - it only contains partial configuration. The nx show project --json command returns the full resolved config including inferred targets from plugins.

You can read the full project schema at node_modules/nx/schemas/project-schema.json to understand nx project configuration options.

# Get full project configuration
nx show project my-app --json

# Extract specific parts from the JSON
nx show project my-app --json | jq '.targets'
nx show project my-app --json | jq '.targets.build'
nx show project my-app --json | jq '.targets | keys'

# Check project metadata
nx show project my-app --json | jq '{name, root, sourceRoot, projectType, tags}'

Target Information

Targets define what tasks can be run on a project.

# List all targets for a project
nx show project my-app --json | jq '.targets | keys'

# Get full target configuration
nx show project my-app --json | jq '.targets.build'

# Check target executor/command
nx show project my-app --json | jq '.targets.build.executor'
nx show project my-app --json | jq '.targets.build.command'

# View target options
nx show project my-app --json | jq '.targets.build.options'

# Check target inputs/outputs (for caching)
nx show project my-app --json | jq '.targets.build.inputs'
nx show project my-app --json | jq '.targets.build.outputs'

# Find projects with a specific target
nx show projects --withTarget serve
nx show projects --withTarget e2e

Workspace Configuration

Read nx.json directly for workspace-level configuration. You can read the full project schema at node_modules/nx/schemas/nx-schema.json to understand nx project configuration options.

# Read the full nx.json
cat nx.json

# Or use jq for specific sections
cat nx.json | jq '.targetDefaults'
cat nx.json | jq '.namedInputs'
cat nx.json | jq '.plugins'
cat nx.json | jq '.generators'


Key nx.json sections:

targetDefaults - Default configuration applied to all targets of a given name
namedInputs - Reusable input definitions for caching
plugins - Nx plugins and their configuration
...and much more, read the schema or nx.json for details
Affected Projects

If the user is asking about affected projects, read the affected projects reference for detailed commands and examples.

Common Exploration Patterns
"What's in this workspace?"
nx show projects
nx show projects --type app
nx show projects --type lib

"How do I build/test/lint project X?"
nx show project X --json | jq '.targets | keys'
nx show project X --json | jq '.targets.build'

"What depends on library Y?"
# Use the project graph to find dependents
nx graph --print | jq '.graph.dependencies | to_entries[] | select(.value[].target == "Y") | .key'

Programmatic Answers

When processing nx CLI results, use command-line tools to compute the answer programmatically rather than counting or parsing output manually. Always use --json flags to get structured output that can be processed with jq, grep, or other tools you have installed locally.

Listing Projects
nx show projects --json


Example output:

["my-app", "my-app-e2e", "shared-ui", "shared-utils", "api"]


Common operations:

# Count projects
nx show projects --json | jq 'length'

# Filter by pattern
nx show projects --json | jq '.[] | select(startswith("shared-"))'

# Get affected projects as array
nx show projects --affected --json | jq '.'

Project Details
nx show project my-app --json


Example output:

{
  "root": "apps/my-app",
  "name": "my-app",
  "sourceRoot": "apps/my-app/src",
  "projectType": "application",
  "tags": ["type:app", "scope:client"],
  "targets": {
    "build": {
      "executor": "@nx/vite:build",
      "options": { "outputPath": "dist/apps/my-app" }
    },
    "serve": {
      "executor": "@nx/vite:dev-server",
      "options": { "buildTarget": "my-app:build" }
    },
    "test": {
      "executor": "@nx/vite:test",
      "options": {}
    }
  },
  "implicitDependencies": []
}


Common operations:

# Get target names
nx show project my-app --json | jq '.targets | keys'

# Get specific target config
nx show project my-app --json | jq '.targets.build'

# Get tags
nx show project my-app --json | jq '.tags'

# Get project root
nx show project my-app --json | jq -r '.root'

Project Graph
nx graph --print


Example output:

{
  "graph": {
    "nodes": {
      "my-app": {
        "name": "my-app",
        "type": "app",
        "data": { "root": "apps/my-app", "tags": ["type:app"] }
      },
      "shared-ui": {
        "name": "shared-ui",
        "type": "lib",
        "data": { "root": "libs/shared-ui", "tags": ["type:ui"] }
      }
    },
    "dependencies": {
      "my-app": [
        { "source": "my-app", "target": "shared-ui", "type": "static" }
      ],
      "shared-ui": []
    }
  }
}


Common operations:

# Get all project names from graph
nx graph --print | jq '.graph.nodes | keys'

# Find dependencies of a project
nx graph --print | jq '.graph.dependencies["my-app"]'

# Find projects that depend on a library
nx graph --print | jq '.graph.dependencies | to_entries[] | select(.value[].target == "shared-ui") | .key'

Troubleshooting
"Cannot find configuration for task X:target"
# Check what targets exist on the project
nx show project X --json | jq '.targets | keys'

# Check if any projects have that target
nx show projects --withTarget target

"The workspace is out of sync"
nx sync
nx reset  # if sync doesn't fix stale cache

Weekly Installs
1.7K
Repository
nrwl/nx-ai-agents-config
GitHub Stars
19
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass