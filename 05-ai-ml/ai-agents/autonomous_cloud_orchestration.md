---
title: autonomous-cloud-orchestration
url: https://skills.sh/qodex-ai/ai-agent-skills/autonomous-cloud-orchestration
---

# autonomous-cloud-orchestration

skills/qodex-ai/ai-agent-skills/autonomous-cloud-orchestration
autonomous-cloud-orchestration
Installation
$ npx skills add https://github.com/qodex-ai/ai-agent-skills --skill autonomous-cloud-orchestration
SKILL.md
AWS Bedrock AgentCore

AWS Bedrock AgentCore provides a complete platform for deploying and scaling AI agents with seven core services. This skill guides you through service selection, deployment patterns, and integration workflows using AWS CLI.

AWS Documentation Requirement

CRITICAL: This skill requires AWS MCP tools for accurate, up-to-date AWS information.

Before Answering AWS Questions

Always verify using AWS MCP tools (if available):

mcp__aws-mcp__aws___search_documentation or mcp__*awsdocs*__aws___search_documentation - Search AWS docs
mcp__aws-mcp__aws___read_documentation or mcp__*awsdocs*__aws___read_documentation - Read specific pages
mcp__aws-mcp__aws___get_regional_availability - Check service availability

If AWS MCP tools are unavailable:

Guide user to configure AWS MCP: See AWS MCP Setup Guide
Help determine which option fits their environment:
Has uvx + AWS credentials → Full AWS MCP Server
No Python/credentials → AWS Documentation MCP (no auth)
If cannot determine → Ask user which option to use
When to Use This Skill

Use this skill when you need to:

Deploy REST APIs as MCP tools for AI agents (Gateway)
Execute agents in serverless runtime (Runtime)
Add conversation memory to agents (Memory)
Manage API credentials and authentication (Identity)
Enable agents to execute code securely (Code Interpreter)
Allow agents to interact with websites (Browser)
Monitor and trace agent performance (Observability)
Available Services
Service	Use For	Documentation
Gateway	Converting REST APIs to MCP tools	services/gateway/README.md
Runtime	Deploying and scaling agents	services/runtime/README.md
Memory	Managing conversation state	services/memory/README.md
Identity	Credential and access management	services/identity/README.md
Code Interpreter	Secure code execution in sandboxes	services/code-interpreter/README.md
Browser	Web automation and scraping	services/browser/README.md
Observability	Tracing and monitoring	services/observability/README.md
Common Workflows
Deploying a Gateway Target

MANDATORY - READ DETAILED DOCUMENTATION: See services/gateway/README.md for complete Gateway setup guide including deployment strategies, troubleshooting, and IAM configuration.

Quick Workflow:

Upload OpenAPI schema to S3
(API Key auth only) Create credential provider and store API key
Create gateway target linking schema (and credentials if using API key)
Verify target status and test connectivity

Note: Credential provider is only needed for API key authentication. Lambda targets use IAM roles, and MCP servers use OAuth.

Managing Credentials

MANDATORY - READ DETAILED DOCUMENTATION: See cross-service/credential-management.md for unified credential management patterns across all services.

Quick Workflow:

Use Identity service credential providers for all API keys
Link providers to gateway targets via ARN references
Rotate credentials quarterly through credential provider updates
Monitor usage with CloudWatch metrics
Monitoring Agents

MANDATORY - READ DETAILED DOCUMENTATION: See services/observability/README.md for comprehensive monitoring setup.

Quick Workflow:

Enable observability for agents
Configure CloudWatch dashboards for metrics
Set up alarms for error rates and latency
Use X-Ray for distributed tracing
Service-Specific Documentation

For detailed documentation on each AgentCore service, see the following resources:

Gateway Service
Overview: services/gateway/README.md
Deployment Strategies: services/gateway/deployment-strategies.md
Troubleshooting: services/gateway/troubleshooting-guide.md
Runtime, Memory, Identity, Code Interpreter, Browser, Observability

Each service has comprehensive documentation in its respective directory:

services/runtime/README.md
services/memory/README.md
services/identity/README.md
services/code-interpreter/README.md
services/browser/README.md
services/observability/README.md
Cross-Service Resources

For patterns and best practices that span multiple AgentCore services:

Credential Management: cross-service/credential-management.md - Unified credential patterns, security practices, rotation procedures
Additional Resources
AWS Documentation: Amazon Bedrock AgentCore
API Reference: Bedrock AgentCore Control Plane API
AWS CLI Reference: bedrock-agentcore-control commands
Weekly Installs
71
Repository
qodex-ai/ai-agent-skills
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn