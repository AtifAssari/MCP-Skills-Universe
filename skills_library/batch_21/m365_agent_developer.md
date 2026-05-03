---
title: m365-agent-developer
url: https://skills.sh/sebastienlevert/m365-copilot-skills/m365-agent-developer
---

# m365-agent-developer

skills/sebastienlevert/m365-copilot-skills/m365-agent-developer
m365-agent-developer
Installation
$ npx skills add https://github.com/sebastienlevert/m365-copilot-skills --skill m365-agent-developer
SKILL.md
M365 Agent Developer

This comprehensive skill provides expert guidance on the Microsoft 365 Copilot agent development lifecycle: from architectural design through TypeSpec implementation to deployment and publishing using the Agents Toolkit (ATK) CLI.

⚠️ For creating new projects, use the m365-agent-scaffolder skill first ⚠️

🚨 CRITICAL DEPLOYMENT RULE 🚨 When using this skill to make edits to an agent, you MUST ALWAYS deploy the agent using atk provision before returning to the user. This ensures changes are immediately reflected in M365 Copilot. Never return to the user with undeployed changes.

When to Use This Skill

Use this skill when:

Designing the architecture for a new M365 Copilot agent
Implementing TypeSpec code for agent capabilities and API plugins
Configuring agent instructions and conversation starters
Provisioning and deploying agents using ATK CLI
Managing agent lifecycle across environments (dev, staging, production)
Reviewing existing agent architectures for best practices
Troubleshooting TypeSpec compilation or deployment issues
Adding new capabilities or API plugins to existing agents
Implementing security patterns and compliance requirements
Packaging and publishing agents for sharing

Do NOT use this skill for creating new empty projects - use the m365-agent-scaffolder skill instead.

Key References
TypeSpec Best Practices - Official TypeSpec patterns and best practices for M365 Copilot agents
Architectural Patterns and Frameworks - Design patterns for agent architecture
API Plugins - Integration patterns and best practices for API plugins
Conversation Design - Instruction patterns and conversation starter best practices
Security Guidelines - Security patterns, compliance frameworks, and credential management
Deployment - Complete ATK CLI workflows, environment management, and CI/CD patterns
Common Pitfalls - Anti-patterns and solutions in M365 Copilot agent development
Best Practices - Comprehensive best practices for security, performance, testing, and more
Examples - Common workflow examples and scripts
Instructions

Follow these step-by-step instructions when working with M365 Copilot agents:

Step 1: Understand the Requirements

Action: Gather and analyze the agent requirements:

Identify the agent's primary purpose and target users
Determine required data sources (M365 services, external APIs)
List necessary actions the agent must perform
Identify security and compliance requirements

Why it's important: Clear requirements drive architectural decisions and ensure the agent meets user needs.

Step 2: Design the Agent Architecture

Action: Create a comprehensive architectural design:

Select deployment model (personal or shared)
Choose appropriate M365 capabilities with scoping
Design API plugin integrations if needed
Plan authentication and authorization strategy
Design conversation flow and instructions

Reference: Follow the Architectural Design section and patterns-and-frameworks.md

Step 3: Implement TypeSpec Code

Action: Write type-safe agent code using TypeSpec:

Define agent with @agent decorator
Configure capabilities with appropriate scoping
Implement API plugin actions with authentication
Write clear instructions and conversation starters
Document all models and operations with @doc

Reference: Follow TypeSpec Best Practices and official typespec-decorators.md

⚠️ IMPORTANT: After making any edits to TypeSpec code, you MUST compile and deploy the agent (Steps 4-5) before returning to the user.

Step 4: Compile and Validate

Action: Compile TypeSpec to validate the implementation:

npm run compile


Why it's important: Compilation catches syntax errors and validates decorator usage before deployment.

Step 5: Provision Azure Resources

Action: Provision required Azure resources and register the agent:

npx -p @microsoft/m365agentstoolkit-cli@latest atk provision --env local


Result: Returns a test URL like https://m365.cloud.microsoft/chat/?titleId=U_abc123xyz

Step 6: Test and Iterate

Action: Test the agent in Microsoft 365 Copilot:

Use the provisioned test URL
Test all conversation starters
Verify capability access and scoping
Test error handling and edge cases
Validate security controls
Step 7: Deploy to Environments

Action: Deploy to staging/production environments:

npx -p @microsoft/m365agentstoolkit-cli@latest atk provision --env prod


Reference: Follow deployment.md for environment management and CI/CD patterns

Step 8: Package and Share

Action: Package and share the agent:

# Package the agent
npx -p @microsoft/m365agentstoolkit-cli@latest atk provision --env dev

# Share to tenant (for shared agents)
npx -p @microsoft/m365agentstoolkit-cli@latest atk share --scope tenant --env dev


Reference: See deployment.md for sharing strategies

Critical Workflow Rules
Always Deploy After Edits

RULE: When making any changes to an agent (TypeSpec code, instructions, capabilities, API plugins), you MUST complete the following workflow before returning to the user:

Compile the TypeSpec code: npm run compile
Provision/deploy the agent: npx -p @microsoft/m365agentstoolkit-cli@latest atk provision --env local
Confirm deployment succeeded and provide the test URL

Why this is critical:

Changes are not reflected in M365 Copilot until the agent is redeployed
Users expect to test changes immediately after you make them
Undeployed changes create confusion and waste time
This ensures a complete, testable solution is always delivered

Never skip deployment: Even for minor changes like updating instructions or conversation starters, always redeploy. M365 Copilot only sees the deployed version.

Always Clean Up Unused Files

RULE: Every time you work on an agent project, check for and remove unused or obsolete files:

Check for orphaned files: Look for files not referenced anywhere in the project
Remove generated artifacts: Delete old build outputs, temp files, and stale generated code
Clean unused dependencies: Remove unused imports and dependencies
Delete obsolete documentation: Remove outdated docs that no longer apply

Files to check and potentially remove:

TODO.md or planning files no longer needed
Old backup files (.bak, .old, .orig)
Unused TypeSpec files not imported anywhere
Stale environment files (.env.old, .env.backup)
Empty or placeholder files
Commented-out code blocks that will never be used
Unused model definitions or operations

Why this is critical:

Clean projects are easier to understand and maintain
Unused files create confusion about what's active
Old files may contain outdated patterns or security issues
Smaller projects are faster to compile and deploy

Before returning to the user: Always verify the project contains only necessary, actively-used files.

Best Practices

Follow these best practices for successful M365 Copilot agent development:

Category	Key Focus
Security	Least privilege scoping, credential management, input validation
Performance	Scoped queries, efficient API design, caching strategies
Error Handling	Graceful degradation, clear messages, retry logic
Testing	Conversation starters, edge cases, security testing
Compliance	Data residency, retention policies, RBAC
Maintainability	Documentation, naming conventions, version control
Conversation Design	Clear instructions, actionable starters, appropriate tone
Deployment	Environment strategy, CI/CD, version management

Reference: best-practices.md for detailed guidelines.

Examples

Common workflow examples for M365 Copilot agent development:

Example	Description
Compile and Validate	Local TypeSpec validation before deployment
Development and Provisioning	Full dev workflow with test URL
Provision and Share	Deploy and share agent with tenant users
Package for Distribution	Create distributable package for production

Reference: examples.md for complete workflow scripts.

Weekly Installs
19
Repository
sebastienlevert…t-skills
GitHub Stars
4
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass