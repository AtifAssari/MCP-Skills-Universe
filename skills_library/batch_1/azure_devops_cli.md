---
title: azure-devops-cli
url: https://skills.sh/github/awesome-copilot/azure-devops-cli
---

# azure-devops-cli

skills/github/awesome-copilot/azure-devops-cli
azure-devops-cli
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill azure-devops-cli
Summary

Manage Azure DevOps resources including projects, repos, pipelines, builds, work items, and service endpoints via CLI.

Covers six major domains: Repos and PRs, Pipelines and Builds, Boards and Work Items, Variables and Agents, Organization and Security, and Advanced Usage patterns
Requires Azure CLI 2.81.0+ with the azure-devops extension; authenticate using PAT tokens and configure default organization/project to avoid repeating flags
Supports output formatting with JMESPath queries, global arguments, and scripting patterns for automation workflows
Includes reference documentation for each domain with complete command syntax, examples, and best practices for CI/CD and DevOps automation
SKILL.md
Azure DevOps CLI

Manage Azure DevOps resources using the Azure CLI with the Azure DevOps extension.

CLI Version: 2.81.0 (current as of 2025)

Prerequisites
# Install Azure CLI
brew install azure-cli  # macOS
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash  # Linux

# Install Azure DevOps extension
az extension add --name azure-devops

Authentication
# Login with PAT token
az devops login --organization https://dev.azure.com/{org} --token YOUR_PAT_TOKEN

# Set default organization and project (avoids repeating --org/--project)
# Note: Legacy URL https://{org}.visualstudio.com should be replaced with https://dev.azure.com/{org}
az devops configure --defaults organization=https://dev.azure.com/{org} project={project}

# List current configuration
az devops configure --list

CLI Structure
az devops          # Main DevOps commands
├── admin          # Administration (banner)
├── extension      # Extension management
├── project        # Team projects
├── security       # Security operations
│   ├── group      # Security groups
│   └── permission # Security permissions
├── service-endpoint # Service connections
├── team           # Teams
├── user           # Users
├── wiki           # Wikis
├── configure      # Set defaults
├── invoke         # Invoke REST API
├── login          # Authenticate
└── logout         # Clear credentials

az pipelines       # Azure Pipelines
├── agent          # Agents
├── build          # Builds
├── folder         # Pipeline folders
├── pool           # Agent pools
├── queue          # Agent queues
├── release        # Releases
├── runs           # Pipeline runs
├── variable       # Pipeline variables
└── variable-group # Variable groups

az boards          # Azure Boards
├── area           # Area paths
├── iteration      # Iterations
└── work-item      # Work items

az repos           # Azure Repos
├── import         # Git imports
├── policy         # Branch policies
├── pr             # Pull requests
└── ref            # Git references

az artifacts       # Azure Artifacts
└── universal      # Universal Packages

Reference Files

Read the relevant reference file based on the user's task. Each file contains complete command syntax and examples for its domain.

File	When to read	Covers
references/repos-and-prs.md	Repos, branches, pull requests, branch policies	Repositories, Import, PRs (create/list/vote/reviewers/policies), Git refs, Branch policies
references/pipelines-and-builds.md	Pipelines, builds, releases, artifacts	Pipelines CRUD, runs, builds, releases, artifacts download/upload
references/boards-and-iterations.md	Work items, sprints, area paths	Work items (WIQL/create/update/relations), Area paths, Iterations, Team iterations
references/variables-and-agents.md	Pipeline variables, agent pools	Pipeline variables, Variable groups, Pipeline folders, Agent pools/queues
references/org-and-security.md	Projects, teams, users, permissions, wikis	Projects, Extensions, Teams, Users, Security groups/permissions, Service endpoints, Wikis, Admin
references/advanced-usage.md	Output formatting, JMESPath queries	Output formats, JMESPath queries (basic + advanced), Global args, Common params, Git aliases
references/workflows-and-patterns.md	Automation scripts, best practices, error handling	Common workflows, Best practices, Error handling, Scripting patterns, Real-world examples
Weekly Installs
10.2K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail