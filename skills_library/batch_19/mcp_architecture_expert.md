---
title: mcp architecture expert
url: https://skills.sh/frankxai/claude-skills-library/mcp-architecture-expert
---

# mcp architecture expert

skills/frankxai/claude-skills-library/MCP Architecture Expert
MCP Architecture Expert
Installation
$ npx skills add https://github.com/frankxai/claude-skills-library --skill 'MCP Architecture Expert'
SKILL.md
MCP Architecture Expert Skill
Purpose

Master the Model Context Protocol (MCP) to build standardized, reusable integrations between AI systems and data sources, eliminating the N×M integration problem.

What is MCP?
Model Context Protocol

Open standard (November 2024, Anthropic) for connecting AI systems to external data sources and tools through a unified protocol.

The Problem: N agents × M tools = N×M custom integrations The Solution: N agents + M MCP servers = N+M integrations (any agent uses any tool)

Architecture
┌─────────────┐
│  MCP Host   │  (Claude Desktop, IDEs, Apps)
│   ┌─────┐   │
│   │Client│──┼──┐
│   └─────┘   │  │
└─────────────┘  │
                 │ JSON-RPC 2.0
                 │
┌────────────────┼─────────────┐
│  MCP Server    ▼             │
│  ┌──────────────────┐        │
│  │  Resources       │        │
│  │  Tools           │        │
│  │  Prompts         │        │
│  └──────────────────┘        │
│         │                    │
│         ▼                    │
│  ┌──────────────────┐        │
│  │ Data Source      │        │
│  │ (DB, API, Files) │        │
│  └──────────────────┘        │
└─────────────────────────────┘

Three Core Capabilities
1. Resources

Purpose: Expose data for AI to read

Examples:

File contents
Database records
API responses
Documentation

Definition:

{
  "resources": [
    {
      "uri": "file:///docs/api-spec.md",
      "name": "API Specification",
      "mimeType": "text/markdown"
    },
    {
      "uri": "db://customers/12345",
      "name": "Customer Record",
      "mimeType": "application/json"
    }
  ]
}

2. Tools

Purpose: Functions AI can invoke

Examples:

Query database
Call external API
Process files
Execute commands

Definition:

{
  "tools": [
    {
      "name": "query_database",
      "description": "Execute SQL query on customer database",
      "inputSchema": {
        "type": "object",
        "properties": {
          "query": {"type": "string"}
        },
        "required": ["query"]
      }
    }
  ]
}

3. Prompts

Purpose: Reusable prompt templates

Examples:

Common task patterns
Domain-specific workflows
Best practice templates

Definition:

{
  "prompts": [
    {
      "name": "analyze_customer",
      "description": "Analyze customer behavior and generate insights",
      "arguments": [
        {
          "name": "customer_id",
          "description": "Customer identifier",
          "required": true
        }
      ]
    }
  ]
}

Building MCP Servers
Python Server Example
from mcp import Server, Tool, Resource

server = Server("customer-data")

@server.resource("customer://")
async def get_customer(uri: str):
    """Expose customer data as resources"""
    customer_id = uri.split("://")[1]
    return {
        "uri": uri,
        "mimeType": "application/json",
        "text": json.dumps(get_customer_data(customer_id))
    }

@server.tool()
async def query_customers(
    filters: dict
) -> list:
    """Query customer database"""
    return database.query("customers", filters)

@server.prompt()
async def customer_analysis(customer_id: str):
    """Generate customer analysis prompt"""
    return {
        "messages": [
            {
                "role": "user",
                "content": f"Analyze customer {customer_id} behavior and provide insights"
            }
        ]
    }

if __name__ == "__main__":
    server.run()

TypeScript Server Example
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({
  name: "github-server",
  version: "1.0.0"
}, {
  capabilities: {
    resources: {},
    tools: {},
    prompts: {}
  }
});

server.setRequestHandler(ListResourcesRequestSchema, async () => {
  return {
    resources: [
      {
        uri: "github://issues",
        name: "GitHub Issues",
        mimeType: "application/json"
      }
    ]
  };
});

server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "create_issue",
        description: "Create a new GitHub issue",
        inputSchema: {
          type: "object",
          properties: {
            title: { type: "string" },
            body: { type: "string" }
          }
        }
      }
    ]
  };
});

const transport = new StdioServerTransport();
await server.connect(transport);

Common MCP Servers
Official Servers (by Anthropic)
GitHub - Issues, PRs, repos
Slack - Messages, channels
Google Drive - Files, docs
PostgreSQL - Database queries
Puppeteer - Web scraping
Git - Repository operations
Stripe - Payment data
Installing Official Servers
# Via npm
npx @modelcontextprotocol/server-github

# Via Docker
docker run mcp-postgres-server

# Via Python
pip install mcp-server-slack
python -m mcp_server_slack

Client Integration
Claude Desktop Configuration
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-token"
      }
    },
    "postgres": {
      "command": "docker",
      "args": ["run", "mcp-postgres-server"],
      "env": {
        "DATABASE_URL": "postgresql://..."
      }
    }
  }
}

Claude SDK Integration
from anthropic import Anthropic

client = Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-5",
    mcp_servers={
        "github": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"]
        }
    },
    messages=[{
        "role": "user",
        "content": "List my GitHub issues"
    }]
)

Security Best Practices
Authentication
# OAuth 2.0 with Resource Indicators (RFC 8707)
server = Server(
    "secure-api",
    auth_type="oauth2",
    scopes=["read:data", "write:data"]
)

@server.tool(required_scope="write:data")
async def update_record(record_id: str, data: dict):
    # Only callable with write permissions
    pass

Input Validation
@server.tool()
async def execute_query(query: str):
    # Validate to prevent injection
    if not is_safe_query(query):
        raise ValueError("Unsafe query detected")

    # Sanitize inputs
    safe_query = sanitize_sql(query)
    return database.execute(safe_query)

Rate Limiting
from functools import lru_cache
from time import time

@server.tool()
@rate_limit(calls=10, period=60)  # 10 calls per minute
async def expensive_operation():
    pass

Audit Logging
@server.tool()
async def sensitive_operation(data: dict):
    audit_log.write({
        "timestamp": datetime.now(),
        "operation": "sensitive_operation",
        "user": current_user(),
        "data": data
    })
    return process(data)

Advanced Patterns
Multi-Source Aggregation
@server.resource("aggregated://customer")
async def aggregate_customer_data(customer_id: str):
    """Combine data from multiple sources"""
    crm_data = await crm_server.get_resource(f"crm://{customer_id}")
    support_data = await support_server.get_resource(f"support://{customer_id}")
    analytics_data = await analytics_server.get_resource(f"analytics://{customer_id}")

    return {
        "uri": f"aggregated://customer/{customer_id}",
        "data": {
            **crm_data,
            **support_data,
            **analytics_data
        }
    }

Caching Layer
from functools import lru_cache

@server.resource("cached://")
@lru_cache(maxsize=1000)
async def cached_resource(uri: str):
    """Cache frequently accessed resources"""
    return await expensive_fetch(uri)

Streaming Large Data
@server.tool()
async def stream_large_dataset(query: str):
    """Stream results for large datasets"""
    async for chunk in database.stream(query):
        yield chunk

Monitoring & Observability
Metrics Collection
from prometheus_client import Counter, Histogram

tool_calls = Counter('mcp_tool_calls', 'Tool invocations', ['tool_name'])
latency = Histogram('mcp_latency', 'Operation latency')

@server.tool()
@latency.time()
async def monitored_tool():
    tool_calls.labels(tool_name='monitored_tool').inc()
    # Tool implementation

Error Tracking
import logging

logger = logging.getLogger("mcp_server")

@server.tool()
async def error_tracked_tool():
    try:
        return await risky_operation()
    except Exception as e:
        logger.error(f"Tool failed: {e}", exc_info=True)
        raise

Testing MCP Servers
Unit Testing
import pytest
from mcp.testing import MockServer

@pytest.mark.asyncio
async def test_customer_tool():
    server = MockServer()
    result = await server.call_tool("get_customer", {"id": "123"})
    assert result["customer_id"] == "123"

Integration Testing
@pytest.mark.asyncio
async def test_full_workflow():
    # Start test server
    async with TestMCPServer() as server:
        # Test resource access
        resource = await server.get_resource("test://data")
        assert resource is not None

        # Test tool execution
        result = await server.call_tool("process_data", {"input": "test"})
        assert result["success"] == True

Decision Framework

Build MCP Server when:

Creating reusable data/tool integration
Want AI agents to access your data
Need standardized interface across frameworks
Building for ecosystem (others can use your server)

Use existing MCP Server when:

Connecting to GitHub, Slack, Drive, Postgres, etc.
Standard data sources with official servers
Prototyping quickly
Resources

Official:

Specification: https://modelcontextprotocol.io/specification
GitHub: https://github.com/modelcontextprotocol
Server Registry: https://github.com/modelcontextprotocol/servers

SDKs:

Python: pip install mcp
TypeScript: npm install @modelcontextprotocol/sdk

MCP is the universal standard for AI-to-data integration in 2025 and beyond.

Weekly Installs
–
Repository
frankxai/claude…-library
GitHub Stars
11
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn