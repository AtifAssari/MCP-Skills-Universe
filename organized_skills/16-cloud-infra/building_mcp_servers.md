---
rating: ⭐⭐⭐
title: building-mcp-servers
url: https://skills.sh/bilalmk/todo_correct/building-mcp-servers
---

# building-mcp-servers

skills/bilalmk/todo_correct/building-mcp-servers
building-mcp-servers
Installation
$ npx skills add https://github.com/bilalmk/todo_correct --skill building-mcp-servers
SKILL.md
MCP Server Development Guide
Overview

Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality of an MCP server is measured by how well it enables LLMs to accomplish real-world tasks.

High-Level Workflow

Creating a high-quality MCP server involves four main phases:

Phase 1: Deep Research and Planning
1.1 Understand Modern MCP Design

API Coverage vs. Workflow Tools: Balance comprehensive API endpoint coverage with specialized workflow tools. When uncertain, prioritize comprehensive API coverage.

Tool Naming and Discoverability: Use consistent prefixes (e.g., github_create_issue, github_list_repos) and action-oriented naming.

Context Management: Design tools that return focused, relevant data. Support filtering/pagination.

Actionable Error Messages: Error messages should guide agents toward solutions with specific suggestions.

1.2 Study MCP Protocol Documentation

Start with the sitemap: https://modelcontextprotocol.io/sitemap.xml

Fetch pages with .md suffix (e.g., https://modelcontextprotocol.io/specification/draft.md).

Key pages: Specification overview, transport mechanisms, tool/resource/prompt definitions.

1.3 Study Framework Documentation

Recommended stack:

Language: TypeScript (high-quality SDK, good AI code generation)
Transport: Streamable HTTP for remote servers, stdio for local servers

Load framework documentation:

MCP Best Practices - Core guidelines
TypeScript Guide - TypeScript patterns
Python Guide - Python/FastMCP patterns

SDK Documentation:

TypeScript: https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md
Python: https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md
1.4 Plan Your Implementation

Review the service's API documentation. List endpoints to implement, starting with most common operations.

Phase 2: Implementation
2.1 Set Up Project Structure

See language-specific guides:

TypeScript Guide - Project structure, package.json, tsconfig.json
Python Guide - Module organization, dependencies
2.2 Implement Core Infrastructure

Create shared utilities:

API client with authentication
Error handling helpers
Response formatting (JSON/Markdown)
Pagination support
2.3 Implement Tools

For each tool:

Input Schema:

Use Zod (TypeScript) or Pydantic (Python)
Include constraints and clear descriptions

Output Schema:

Define outputSchema where possible
Use structuredContent in responses

Tool Description:

Concise summary, parameter descriptions, return type

Annotations:

readOnlyHint, destructiveHint, idempotentHint, openWorldHint
Phase 3: Review and Test
3.1 Code Quality

Review for: DRY principle, consistent error handling, full type coverage, clear descriptions.

3.2 Build and Test

TypeScript:

npm run build
npx @modelcontextprotocol/inspector


Python:

python -m py_compile your_server.py
# Test with MCP Inspector

Phase 4: Create Evaluations

Create 10 evaluation questions to test LLM effectiveness with your server.

Requirements for each question:

Independent, read-only, complex, realistic, verifiable, stable

Output Format:

<evaluation>
  <qa_pair>
    <question>Your question here</question>
    <answer>Expected answer</answer>
  </qa_pair>
</evaluation>


See Evaluation Guide for complete guidelines.

Docker/Containerization
Transport Security (allowed_hosts)

FastMCP validates Host headers. For Docker, configure:

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

transport_security = TransportSecuritySettings(
    allowed_hosts=[
        "127.0.0.1:*", "localhost:*", "[::1]:*",
        "mcp-server:*",  # Docker container name
        "0.0.0.0:*",
    ],
)
mcp = FastMCP("my_server", transport_security=transport_security)

Health Check Endpoint

Add /health endpoint via middleware (see references for full example).

Verification

Run: python3 scripts/verify.py

Expected: ✓ building-mcp-servers skill ready

If Verification Fails
Run diagnostic: Check references/ folder exists
Check: All reference files present
Stop and report if still failing
References
MCP Best Practices - Universal guidelines
Python Guide - Python/FastMCP patterns
TypeScript Guide - TypeScript patterns
TaskFlow Patterns - Internal server patterns
Evaluation Guide - Creating evaluations
Weekly Installs
15
Repository
bilalmk/todo_correct
GitHub Stars
1
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn