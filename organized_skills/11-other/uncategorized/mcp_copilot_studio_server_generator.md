---
rating: ⭐⭐
title: mcp-copilot-studio-server-generator
url: https://skills.sh/github/awesome-copilot/mcp-copilot-studio-server-generator
---

# mcp-copilot-studio-server-generator

skills/github/awesome-copilot/mcp-copilot-studio-server-generator
mcp-copilot-studio-server-generator
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill mcp-copilot-studio-server-generator
Summary

Generate complete MCP server implementations optimized for Copilot Studio with Power Platform connector standards.

Produces all required files (apiDefinition.swagger.json, apiProperties.json, script.csx, and MCP server code) following Power Platform connector structure with x-ms-agentic-protocol: mcp-streamable-1.0 support
Enforces Copilot Studio schema constraints: no reference types, single-type fields only, primitive types, and full URI endpoints to ensure compatibility
Generates JSON-RPC 2.0 compliant tools, resources (as tool outputs), and streamable HTTP endpoints at /mcp with proper error handling
Includes validation checklist and deployment configuration for Power Platform environments and Copilot Studio agent integration
SKILL.md
Power Platform MCP Connector Generator

Generate a complete Power Platform custom connector with Model Context Protocol (MCP) integration for Microsoft Copilot Studio. This prompt creates all necessary files following Power Platform connector standards with MCP streamable HTTP support.

Instructions

Create a complete MCP server implementation that:

Uses Copilot Studio MCP Pattern:

Implement x-ms-agentic-protocol: mcp-streamable-1.0
Support JSON-RPC 2.0 communication protocol
Provide streamable HTTP endpoint at /mcp
Follow Power Platform connector structure

Schema Compliance Requirements:

NO reference types in tool inputs/outputs (filtered by Copilot Studio)
Single type values only (not arrays of multiple types)
Avoid enum inputs (interpreted as string, not enum)
Use primitive types: string, number, integer, boolean, array, object
Ensure all endpoints return full URIs

MCP Components to Include:

Tools: Functions for the language model to call (✅ Supported in Copilot Studio)
Resources: File-like data outputs from tools (✅ Supported in Copilot Studio - must be tool outputs to be accessible)
Prompts: Predefined templates for specific tasks (❌ Not yet supported in Copilot Studio)

Implementation Structure:

/apiDefinition.swagger.json  (Power Platform connector schema)
/apiProperties.json         (Connector metadata and configuration)
/script.csx                 (Custom code transformations and logic)
/server/                    (MCP server implementation)
/tools/                     (Individual MCP tools)
/resources/                 (MCP resource handlers)

Context Variables
Server Purpose: [Describe what the MCP server should accomplish]
Tools Needed: [List of specific tools to implement]
Resources: [Types of resources to provide]
Authentication: [Auth method: none, api-key, oauth2]
Host Environment: [Azure Function, Express.js, FastAPI, etc.]
Target APIs: [External APIs to integrate with]
Expected Output

Generate:

apiDefinition.swagger.json with:

Proper x-ms-agentic-protocol: mcp-streamable-1.0
MCP endpoint at POST /mcp
Compliant schema definitions (no reference types)
McpResponse and McpErrorResponse definitions

apiProperties.json with:

Connector metadata and branding
Authentication configuration
Policy templates if needed

script.csx with:

Custom C# code for request/response transformations
MCP JSON-RPC message handling logic
Data validation and processing functions
Error handling and logging capabilities

MCP Server Code with:

JSON-RPC 2.0 request handler
Tool registration and execution
Resource management (as tool outputs)
Proper error handling
Copilot Studio compatibility checks

Individual Tools that:

Accept only primitive type inputs
Return structured outputs
Include resources as outputs when needed
Provide clear descriptions for Copilot Studio

Deployment Configuration for:

Power Platform environment
Copilot Studio agent integration
Testing and validation
Validation Checklist

Ensure generated code:

 No reference types in schemas
 All type fields are single types
 Enum handling via string with validation
 Resources available through tool outputs
 Full URI endpoints
 JSON-RPC 2.0 compliance
 Proper x-ms-agentic-protocol header
 McpResponse/McpErrorResponse schemas
 Clear tool descriptions for Copilot Studio
 Generative Orchestration compatible
Example Usage
Server Purpose: Customer data management and analysis
Tools Needed: 
  - searchCustomers
  - getCustomerDetails
  - analyzeCustomerTrends
Resources:
  - Customer profiles
  - Analysis reports
Authentication: oauth2
Host Environment: Azure Function
Target APIs: CRM System REST API

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