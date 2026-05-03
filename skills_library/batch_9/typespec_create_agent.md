---
title: typespec-create-agent
url: https://skills.sh/github/awesome-copilot/typespec-create-agent
---

# typespec-create-agent

skills/github/awesome-copilot/typespec-create-agent
typespec-create-agent
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill typespec-create-agent
Summary

Generate a complete TypeSpec declarative agent for Microsoft 365 Copilot with instructions, capabilities, and conversation starters.

Produces a main.tsp file with agent declaration, instructions, conversation starters, and capability definitions following Microsoft's TypeSpec M365 Copilot schema
Supports 10 capability types including WebSearch, OneDriveAndSharePoint, TeamsMessages, Email, People, CodeInterpreter, GraphicArt, GraphConnectors, Dataverse, and Meetings with optional scoping (URLs, folders, sites)
Enforces constraints: agent names under 100 characters, descriptions under 1,000 characters, instructions under 8,000 characters, and 2-4 diverse conversation starters per agent
Guides users through discovery questions about agent purpose, required capabilities, knowledge sources, and typical interactions to inform the generated definition
SKILL.md
Create TypeSpec Declarative Agent

Create a complete TypeSpec declarative agent for Microsoft 365 Copilot with the following structure:

Requirements

Generate a main.tsp file with:

Agent Declaration

Use @agent decorator with a descriptive name and description
Name should be 100 characters or less
Description should be 1,000 characters or less

Instructions

Use @instructions decorator with clear behavioral guidelines
Define the agent's role, expertise, and personality
Specify what the agent should and shouldn't do
Keep under 8,000 characters

Conversation Starters

Include 2-4 @conversationStarter decorators
Each with a title and example query
Make them diverse and showcase different capabilities

Capabilities (based on user needs)

WebSearch - for web content with optional site scoping
OneDriveAndSharePoint - for document access with URL filtering
TeamsMessages - for Teams channel/chat access
Email - for email access with folder filtering
People - for organization people search
CodeInterpreter - for Python code execution
GraphicArt - for image generation
GraphConnectors - for Copilot connector content
Dataverse - for Dataverse data access
Meetings - for meeting content access
Template Structure
import "@typespec/http";
import "@typespec/openapi3";
import "@microsoft/typespec-m365-copilot";

using TypeSpec.Http;
using TypeSpec.M365.Copilot.Agents;

@agent({
  name: "[Agent Name]",
  description: "[Agent Description]"
})
@instructions("""
  [Detailed instructions about agent behavior, role, and guidelines]
""")
@conversationStarter(#{
  title: "[Starter Title 1]",
  text: "[Example query 1]"
})
@conversationStarter(#{
  title: "[Starter Title 2]",
  text: "[Example query 2]"
})
namespace [AgentName] {
  // Add capabilities as operations here
  op capabilityName is AgentCapabilities.[CapabilityType]<[Parameters]>;
}

Best Practices
Use descriptive, role-based agent names (e.g., "Customer Support Assistant", "Research Helper")
Write instructions in second person ("You are...")
Be specific about the agent's expertise and limitations
Include diverse conversation starters that showcase different features
Only include capabilities the agent actually needs
Scope capabilities (URLs, folders, etc.) when possible for better performance
Use triple-quoted strings for multi-line instructions
Examples

Ask the user:

What is the agent's purpose and role?
What capabilities does it need?
What knowledge sources should it access?
What are typical user interactions?

Then generate the complete TypeSpec agent definition.

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
SnykWarn