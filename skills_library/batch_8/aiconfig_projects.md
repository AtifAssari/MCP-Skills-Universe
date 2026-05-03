---
title: aiconfig-projects
url: https://skills.sh/launchdarkly/agent-skills/aiconfig-projects
---

# aiconfig-projects

skills/launchdarkly/agent-skills/aiconfig-projects
aiconfig-projects
Installation
$ npx skills add https://github.com/launchdarkly/agent-skills --skill aiconfig-projects
SKILL.md
LaunchDarkly Projects Setup

You're using a skill that will guide you through setting up LaunchDarkly project management in a codebase. Your job is to explore the codebase to understand the stack and patterns, assess what approach makes sense, choose the right implementation path from the references, execute the setup, and verify it works.

Prerequisites

Choose one:

LaunchDarkly API access token with projects:write permission
LaunchDarkly MCP server configured in your environment
Core Principles
Understand First: Explore the codebase to understand the stack and patterns.
Choose the Right Fit: Select an approach that matches your architecture.
Follow Conventions: Respect existing code style and structure.
Verify Integration: Confirm the setup works: the agent performs checks and reports results.
API Key Detection

Before prompting the user for an API key, try to detect it automatically:

Check environment variables: Look for LAUNCHDARKLY_API_KEY, LAUNCHDARKLY_API_TOKEN, or LD_API_KEY
Check MCP config: If using Claude, read ~/.claude/config.json for mcpServers.launchdarkly.env.LAUNCHDARKLY_API_KEY
Prompt user: Only if detection fails, ask the user for their API key

See Quick Start for API usage patterns.

What Are Projects?

Projects are LaunchDarkly's top-level organizational containers that hold:

All your AI Configs
Feature flags and segments
Multiple environments (Production and Test created by default)

Think of projects as separate applications, services, or teams that need their own isolated set of configurations.

Project Setup Workflow
Step 1: Explore the Codebase

Before implementing anything, understand the existing architecture:

Identify the tech stack:

What language(s)? (Python, Node.js, Go, Java, etc.)
What framework(s)? (FastAPI, Express, Spring Boot, etc.)
Is there an existing LaunchDarkly integration?

Check environment management:

How are environment variables stored? (.env files, secrets manager, config files)
Where is configuration loaded? (startup scripts, config modules)
Are there existing LaunchDarkly SDK keys?

Look for patterns:

Are there existing API clients or service modules?
How is external API integration typically done?
Is there a CLI, scripts directory, or admin tooling?

Understand the use case:

Is this a new project being set up?
Adding to an existing LaunchDarkly integration?
Part of a multi-service architecture?
Need for project cloning across regions/teams?
Step 2: Assess the Situation

Based on your exploration, determine the right approach:

Scenario	Recommended Path
New project, no LaunchDarkly integration	Quick Setup - Create project and save SDK keys
Existing LaunchDarkly usage	Add to Existing - Create new project or use existing
Multiple services/microservices	Multi-Project - Create projects per service
Multi-region or multi-tenant	Project Cloning - Clone template project
Infrastructure-as-Code (IaC) setup	Automated Setup - Script-based creation
Need project management tooling	CLI/Admin Tools - Build project management utilities
Step 3: Choose Your Implementation Path

Select the reference guide that matches your stack and use case:

By Language/Stack:

Python Implementation - For Python applications (FastAPI, Django, Flask)
Node.js/TypeScript Implementation - For Node.js/Express/NestJS applications
Go Implementation - For Go services
Multi-Language Setup - For polyglot architectures

By Use Case:

Quick Start - Create first project and get SDK keys
Environment Configuration - Save SDK keys to .env, secrets, or config
Project Cloning - Clone projects for regions/teams
IaC/Automation - Terraform, scripts, CI/CD integration
Admin Tooling - Build CLI or admin utilities
Step 4: Implement the Integration

Follow the chosen reference guide to implement project management. Key considerations:

API Authentication:

Store API token securely
Follow existing secrets management patterns
Never commit tokens to version control

Project Naming:

Use consistent, descriptive names
Follow existing naming conventions
Project keys: lowercase, hyphens, start with letter

SDK Key Management:

Extract and store SDK keys for each environment
Use the same pattern as other secrets in your codebase
Consider separate keys for test/staging/production

Error Handling:

Handle existing projects gracefully (409 conflict)
Provide clear error messages
Don't fail silently
Step 5: Verify the Setup

After creating the project, verify it works:

Fetch to confirm it exists. Prefer the MCP get-project tool over raw curl — it returns a typed object you can inspect directly. If you must call the REST API:

curl -X GET "https://app.launchdarkly.com/api/v2/projects/{projectKey}?expand=environments" \
  -H "Authorization: {api_token}"


Do not pipe the response straight into a .environments.items[]-style jq filter. The shape of environments varies by expand parameter — sometimes it's {items: [...]}, sometimes a bare array — and a hand-rolled filter will fail with Cannot index array with string "items". Run jq -e . first to inspect the actual shape, or use jq '.environments | if type == "object" then .items else . end' to handle both.

Test SDK integration: Run a quick verification to ensure the SDK key works:

import ldclient
from ldclient.config import Config

ldclient.set_config(Config("{sdk_key}"))
# SDK initializes successfully

# Always flush events before closing — trailing events are at risk of being
# lost otherwise, in short-lived scripts and long-running services alike.
ldclient.get().flush()
ldclient.get().close()


Report results:

✓ Project exists and has environments
✓ SDK keys are present and valid
✓ SDK can initialize (or flag any issues)
Project Key Best Practices

Project keys must follow these rules:

✓ Good examples:
  - "support-ai"
  - "chat-bot-v2"
  - "internal-tools"

✗ Bad examples:
  - "Support_AI"     # No uppercase or underscores
  - "123-project"    # Must start with letter  
  - "my.project"     # No dots allowed


Naming Recommendations:

Keep keys short but descriptive
Use team/service/purpose as naming scheme
Be consistent across your organization
Common Organization Patterns
By Team
platform-ai       → Platform Team AI
customer-ai       → Customer Success Team AI
internal-ai       → Internal Tools Team AI

By Application/Service
mobile-ai         → Mobile App AI Configs
web-ai            → Web App AI Configs
api-ai            → API Service AI Configs

By Region/Deployment
ai-us             → US Region
ai-eu             → Europe Region
ai-apac           → Asia-Pacific Region

Edge Cases
Situation	Action
Project already exists	Check if it's the right one; use it or create with different key
Need multiple projects	Create separately for each service/region/team
Shared configs across services	Use same project, separate by SDK context
Token lacks permissions	Request projects:write or use MCP server
Project name conflict	Keys must be unique, names can be similar
What NOT to Do
Don't create projects without understanding the use case first
Don't commit API tokens or SDK keys to version control
Don't use production SDK keys in test/development environments
Don't create duplicate projects unnecessarily
Don't skip the exploration phase
Next Steps

After setting up projects:

Create AI Configs - Use the aiconfig-create skill
Set up SDK Integration - Use the aiconfig-sdk skill
Configure Targeting - Use the aiconfig-targeting skill
Related Skills
aiconfig-create - Create AI Configs in projects
aiconfig-sdk - Integrate SDK in your application
aiconfig-targeting - Configure AI Config targeting
aiconfig-variations - Manage config variations
References
Python Implementation
Node.js Implementation
Go Implementation
Quick Start Guide
Environment Configuration
Project Cloning
IaC/Automation
Admin Tooling
Weekly Installs
316
Repository
launchdarkly/ag…t-skills
GitHub Stars
7
First Seen
Feb 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail