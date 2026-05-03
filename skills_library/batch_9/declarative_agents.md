---
title: declarative-agents
url: https://skills.sh/github/awesome-copilot/declarative-agents
---

# declarative-agents

skills/github/awesome-copilot/declarative-agents
declarative-agents
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill declarative-agents
Summary

Complete development kit for building Microsoft 365 Copilot declarative agents with TypeSpec and Agents Toolkit integration.

Three specialized workflows cover basic agent creation, advanced enterprise design, and validation/optimization for existing agents
Supports up to 5 capabilities from 11 options including WebSearch, OneDrive/SharePoint, Graph Connectors, Power Platform, and custom connectors
Enforces v1.5 schema compliance with character limits (name: 100, description: 1000, instructions: 8000) and array constraints
Includes TypeSpec support for type-safe definitions, VS Code extension integration, local debugging via Agents Playground, and environment variable management
SKILL.md
Microsoft 365 Declarative Agents Development Kit

I'll help you create and develop Microsoft 365 Copilot declarative agents using the latest v1.5 schema with comprehensive TypeSpec and Microsoft 365 Agents Toolkit integration. Choose from three specialized workflows:

Workflow 1: Basic Agent Creation

Perfect for: New developers, simple agents, quick prototypes

I'll guide you through:

Agent Planning: Define purpose, target users, and core capabilities
Capability Selection: Choose from 11 available capabilities (WebSearch, OneDriveAndSharePoint, GraphConnectors, etc.)
Basic Schema Creation: Generate compliant JSON manifest with proper constraints
TypeSpec Alternative: Create modern type-safe definitions that compile to JSON
Testing Setup: Configure Agents Playground for local testing
Toolkit Integration: Leverage Microsoft 365 Agents Toolkit for enhanced development
Workflow 2: Advanced Enterprise Agent Design

Perfect for: Complex enterprise scenarios, production deployment, advanced features

I'll help you architect:

Enterprise Requirements Analysis: Multi-tenant considerations, compliance, security
Advanced Capability Configuration: Complex capability combinations and interactions
Behavior Override Implementation: Custom response patterns and specialized behaviors
Localization Strategy: Multi-language support with proper resource management
Conversation Starters: Strategic conversation entry points for user engagement
Production Deployment: Environment management, versioning, and lifecycle planning
Monitoring & Analytics: Implementation of tracking and performance optimization
Workflow 3: Validation & Optimization

Perfect for: Existing agents, troubleshooting, performance optimization

I'll perform:

Schema Compliance Validation: Full v1.5 specification adherence checking
Character Limit Optimization: Name (100), description (1000), instructions (8000)
Capability Audit: Verify proper capability configuration and usage
TypeSpec Migration: Convert existing JSON to modern TypeSpec definitions
Testing Protocol: Comprehensive validation using Agents Playground
Performance Analysis: Identify bottlenecks and optimization opportunities
Best Practices Review: Alignment with Microsoft guidelines and recommendations
Core Features Across All Workflows
Microsoft 365 Agents Toolkit Integration
VS Code Extension: Full integration with teamsdevapp.ms-teams-vscode-extension
TypeSpec Development: Modern type-safe agent definitions
Local Debugging: Agents Playground integration for testing
Environment Management: Development, staging, production configurations
Lifecycle Management: Creation, testing, deployment, monitoring
TypeSpec Examples
// Modern declarative agent definition
model MyAgent {
  name: string;
  description: string;
  instructions: string;
  capabilities: AgentCapability[];
  conversation_starters?: ConversationStarter[];
}

JSON Schema v1.5 Validation
Full compliance with latest Microsoft specification
Character limit enforcement (name: 100, description: 1000, instructions: 8000)
Array constraint validation (conversation_starters: max 4, capabilities: max 5)
Required field validation and type checking
Available Capabilities (Choose up to 5)
WebSearch: Internet search functionality
OneDriveAndSharePoint: File and content access
GraphConnectors: Enterprise data integration
MicrosoftGraph: Microsoft 365 service integration
TeamsAndOutlook: Communication platform access
PowerPlatform: Power Apps and Power Automate integration
BusinessDataProcessing: Enterprise data analysis
WordAndExcel: Document and spreadsheet manipulation
CopilotForMicrosoft365: Advanced Copilot features
EnterpriseApplications: Third-party system integration
CustomConnectors: Custom API and service integration
Environment Variables Support
{
  "name": "${AGENT_NAME}",
  "description": "${AGENT_DESCRIPTION}",
  "instructions": "${AGENT_INSTRUCTIONS}"
}


Which workflow would you like to start with? Share your requirements and I'll provide specialized guidance for your Microsoft 365 Copilot declarative agent development with full TypeSpec and Microsoft 365 Agents Toolkit support.

Weekly Installs
8.3K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass