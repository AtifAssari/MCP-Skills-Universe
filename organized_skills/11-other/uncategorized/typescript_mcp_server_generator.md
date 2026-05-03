---
rating: ⭐⭐
title: typescript-mcp-server-generator
url: https://skills.sh/github/awesome-copilot/typescript-mcp-server-generator
---

# typescript-mcp-server-generator

skills/github/awesome-copilot/typescript-mcp-server-generator
typescript-mcp-server-generator
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill typescript-mcp-server-generator
Summary

Complete TypeScript MCP server project generator with tools, resources, and transport configuration.

Scaffolds a full Node.js/TypeScript project with @modelcontextprotocol/sdk, zod validation, and choice of HTTP (Express) or stdio transport
Generates at least one production-ready tool with schema validation, error handling, and structured content responses
Includes tsconfig.json with ES modules, proper package.json setup, and dev tooling (tsx/ts-node)
Optionally adds resources with dynamic URI templates and prompts with argument schemas for extensibility
Provides testing guidance via MCP Inspector, example tool invocations, and troubleshooting for common deployment issues
SKILL.md
Generate TypeScript MCP Server

Create a complete Model Context Protocol (MCP) server in TypeScript with the following specifications:

Requirements
Project Structure: Create a new TypeScript/Node.js project with proper directory structure
NPM Packages: Include @modelcontextprotocol/sdk, zod@3, and either express (for HTTP) or stdio support
TypeScript Configuration: Proper tsconfig.json with ES modules support
Server Type: Choose between HTTP (with Streamable HTTP transport) or stdio-based server
Tools: Create at least one useful tool with proper schema validation
Error Handling: Include comprehensive error handling and validation
Implementation Details
Project Setup
Initialize with npm init and create package.json
Install dependencies: @modelcontextprotocol/sdk, zod@3, and transport-specific packages
Configure TypeScript with ES modules: "type": "module" in package.json
Add dev dependencies: tsx or ts-node for development
Create proper .gitignore file
Server Configuration
Use McpServer class for high-level implementation
Set server name and version
Choose appropriate transport (StreamableHTTPServerTransport or StdioServerTransport)
For HTTP: set up Express with proper middleware and error handling
For stdio: use StdioServerTransport directly
Tool Implementation
Use registerTool() method with descriptive names
Define schemas using zod for input and output validation
Provide clear title and description fields
Return both content and structuredContent in results
Implement proper error handling with try-catch blocks
Support async operations where appropriate
Resource/Prompt Setup (Optional)
Add resources using registerResource() with ResourceTemplate for dynamic URIs
Add prompts using registerPrompt() with argument schemas
Consider adding completion support for better UX
Code Quality
Use TypeScript for type safety
Follow async/await patterns consistently
Implement proper cleanup on transport close events
Use environment variables for configuration
Add inline comments for complex logic
Structure code with clear separation of concerns
Example Tool Types to Consider
Data processing and transformation
External API integrations
File system operations (read, search, analyze)
Database queries
Text analysis or summarization (with sampling)
System information retrieval
Configuration Options

For HTTP Servers:

Port configuration via environment variables
CORS setup for browser clients
Session management (stateless vs stateful)
DNS rebinding protection for local servers

For stdio Servers:

Proper stdin/stdout handling
Environment-based configuration
Process lifecycle management
Testing Guidance
Explain how to run the server (npm start or npx tsx server.ts)
Provide MCP Inspector command: npx @modelcontextprotocol/inspector
For HTTP servers, include connection URL: http://localhost:PORT/mcp
Include example tool invocations
Add troubleshooting tips for common issues
Additional Features to Consider
Sampling support for LLM-powered tools
User input elicitation for interactive workflows
Dynamic tool registration with enable/disable capabilities
Notification debouncing for bulk updates
Resource links for efficient data references

Generate a complete, production-ready MCP server with comprehensive documentation, type safety, and error handling.

Weekly Installs
9.5K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass