---
title: mcp
url: https://skills.sh/vercel-labs/json-render/mcp
---

# mcp

skills/vercel-labs/json-render/mcp
mcp
Installation
$ npx skills add https://github.com/vercel-labs/json-render --skill mcp
SKILL.md
@json-render/mcp

MCP Apps integration that serves json-render UIs as interactive MCP Apps inside Claude, ChatGPT, Cursor, VS Code, and other MCP-capable clients.

Quick Start
Server (Node.js)
import { createMcpApp } from "@json-render/mcp";
import { defineCatalog } from "@json-render/core";
import { schema } from "@json-render/react/schema";
import { shadcnComponentDefinitions } from "@json-render/shadcn/catalog";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import fs from "node:fs";

const catalog = defineCatalog(schema, {
  components: { ...shadcnComponentDefinitions },
  actions: {},
});

const server = createMcpApp({
  name: "My App",
  version: "1.0.0",
  catalog,
  html: fs.readFileSync("dist/index.html", "utf-8"),
});

await server.connect(new StdioServerTransport());

Client (React, inside iframe)
import { useJsonRenderApp } from "@json-render/mcp/app";
import { JSONUIProvider, Renderer } from "@json-render/react";

function McpAppView({ registry }) {
  const { spec, loading, error } = useJsonRenderApp();
  if (error) return <div>Error: {error.message}</div>;
  if (!spec) return <div>Waiting...</div>;
  return (
    <JSONUIProvider registry={registry} initialState={spec.state ?? {}}>
      <Renderer spec={spec} registry={registry} loading={loading} />
    </JSONUIProvider>
  );
}

Architecture
createMcpApp() creates an McpServer that registers a render-ui tool and a ui:// HTML resource
The tool description includes the catalog prompt so the LLM knows how to generate valid specs
The HTML resource is a Vite-bundled single-file React app with json-render renderers
Inside the iframe, useJsonRenderApp() connects to the host via postMessage and renders specs
Server API
createMcpApp(options) - main entry, creates a full MCP server
registerJsonRenderTool(server, options) - register a json-render tool on an existing server
registerJsonRenderResource(server, options) - register the UI resource
Client API (@json-render/mcp/app)
useJsonRenderApp(options?) - React hook, returns { spec, loading, connected, error, callServerTool }
buildAppHtml(options) - generate HTML from bundled JS/CSS
Building the iframe HTML

Bundle the React app into a single self-contained HTML file using Vite + vite-plugin-singlefile:

// vite.config.ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { viteSingleFile } from "vite-plugin-singlefile";

export default defineConfig({
  plugins: [react(), viteSingleFile()],
  build: { outDir: "dist" },
});

Client Configuration
Cursor (.cursor/mcp.json)
{
  "mcpServers": {
    "my-app": {
      "command": "npx",
      "args": ["tsx", "server.ts", "--stdio"]
    }
  }
}

Claude Desktop
{
  "mcpServers": {
    "my-app": {
      "command": "npx",
      "args": ["tsx", "/path/to/server.ts", "--stdio"]
    }
  }
}

Dependencies
# Server
npm install @json-render/mcp @json-render/core @modelcontextprotocol/sdk

# Client (iframe)
npm install @json-render/react @json-render/shadcn react react-dom

# Build tools
npm install -D vite @vitejs/plugin-react vite-plugin-singlefile

Weekly Installs
566
Repository
vercel-labs/json-render
GitHub Stars
14.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass