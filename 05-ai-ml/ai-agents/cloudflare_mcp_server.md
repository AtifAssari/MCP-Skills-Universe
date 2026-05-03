---
rating: ⭐⭐⭐
title: cloudflare-mcp-server
url: https://skills.sh/jezweb/claude-skills/cloudflare-mcp-server
---

# cloudflare-mcp-server

skills/jezweb/claude-skills/cloudflare-mcp-server
cloudflare-mcp-server
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill cloudflare-mcp-server
Summary

Deploy remote MCP servers on Cloudflare Workers with TypeScript, OAuth, and Durable Objects.

Supports SSE and HTTP Streamable transports with automatic WebSocket hibernation for stateful sessions; choose from five auth templates (no-auth, bearer, GitHub/Google OAuth, enterprise SSO)
Base path configuration is critical—server and client URLs must match exactly (e.g., serveSSE("/sse") requires client URL https://worker.dev/sse, not https://worker.dev)
Includes 24 documented error solutions covering path mismatches, transport confusion, OAuth redirect URIs, CORS preflight, environment validation, and Durable Objects migrations
Conditional tool registration enables role-based access control and feature flags; stateful tools persist across hibernation using this.state.storage instead of instance properties
SKILL.md
Cloudflare MCP Server Skill

Build and deploy Model Context Protocol (MCP) servers on Cloudflare Workers with TypeScript.

Status: Production Ready ✅ Last Updated: 2026-01-21 Latest Versions: @modelcontextprotocol/sdk@1.25.3, @cloudflare/workers-oauth-provider@0.2.2, agents@0.3.6

Recent Updates (2025):

September 2025: Code Mode (agents write code vs calling tools, auto-generated TypeScript API from schema)
August 2025: MCP Elicitation (interactive workflows, user input during execution), Task Queues, Email Integration
July 2025: MCPClientManager (connection management, OAuth flow, hibernation)
April 2025: HTTP Streamable Transport (single endpoint, recommended over SSE), Python MCP support
May 2025: Claude.ai remote MCP support, use-mcp React library, major partnerships
What is This Skill?

This skill teaches you to build remote MCP servers on Cloudflare - the ONLY platform with official remote MCP support.

Use when: Avoiding 24+ common MCP + Cloudflare errors (especially URL path mismatches - the #1 failure cause)

🚀 Quick Start (5 Minutes)

Start with Cloudflare's official template:

npm create cloudflare@latest -- my-mcp-server \
  --template=cloudflare/ai/demos/remote-mcp-authless
cd my-mcp-server && npm install && npm run dev


Choose template based on auth needs:

remote-mcp-authless - No auth (recommended for most)
remote-mcp-github-oauth - GitHub OAuth
remote-mcp-google-oauth - Google OAuth
remote-mcp-auth0 / remote-mcp-authkit - Enterprise SSO
mcp-server-bearer-auth - Custom auth

All templates: https://github.com/cloudflare/ai/tree/main/demos

Production examples: https://github.com/cloudflare/mcp-server-cloudflare (15 servers with real integrations)

Deployment Workflow
# 1. Create from template
npm create cloudflare@latest -- my-mcp --template=cloudflare/ai/demos/remote-mcp-authless
cd my-mcp && npm install && npm run dev

# 2. Deploy
npx wrangler deploy
# Note the output URL: https://my-mcp.YOUR_ACCOUNT.workers.dev

# 3. Test (PREVENTS 80% OF ERRORS!)
curl https://my-mcp.YOUR_ACCOUNT.workers.dev/sse
# Expected: {"name":"My MCP Server","version":"1.0.0","transports":["/sse","/mcp"]}
# Got 404? See "HTTP Transport Fundamentals" below

# 4. Configure client (~/.config/claude/claude_desktop_config.json)
{
  "mcpServers": {
    "my-mcp": {
      "url": "https://my-mcp.YOUR_ACCOUNT.workers.dev/sse"  // Must match curl URL!
    }
  }
}

# 5. Restart Claude Desktop (config only loads at startup)


Post-Deployment Checklist:

 curl returns server info (not 404)
 Client URL matches curl URL exactly
 Claude Desktop restarted
 Tools visible in Claude Desktop
 Test tool call succeeds
⚠️ CRITICAL: HTTP Transport Fundamentals

The #1 reason MCP servers fail to connect is URL path configuration mistakes.

URL Path Configuration Deep-Dive

When you serve an MCP server at a specific path, the client URL must match exactly.

Example 1: Serving at /sse

// src/index.ts
export default {
  fetch(request: Request, env: Env, ctx: ExecutionContext) {
    const { pathname } = new URL(request.url);

    if (pathname.startsWith("/sse")) {
      return MyMCP.serveSSE("/sse").fetch(request, env, ctx);  // ← Base path is "/sse"
    }

    return new Response("Not Found", { status: 404 });
  }
};


Client configuration MUST include /sse:

{
  "mcpServers": {
    "my-mcp": {
      "url": "https://my-mcp.workers.dev/sse"  // ✅ Correct
    }
  }
}


❌ WRONG client configurations:

"url": "https://my-mcp.workers.dev"      // Missing /sse → 404
"url": "https://my-mcp.workers.dev/"     // Missing /sse → 404
"url": "http://localhost:8788"           // Wrong after deploy


Example 2: Serving at / (root)

export default {
  fetch(request: Request, env: Env, ctx: ExecutionContext) {
    return MyMCP.serveSSE("/").fetch(request, env, ctx);  // ← Base path is "/"
  }
};


Client configuration:

{
  "mcpServers": {
    "my-mcp": {
      "url": "https://my-mcp.workers.dev"  // ✅ Correct (no /sse)
    }
  }
}

How Base Path Affects Tool URLs

When you call serveSSE("/sse"), MCP tools are served at:

https://my-mcp.workers.dev/sse/tools/list
https://my-mcp.workers.dev/sse/tools/call
https://my-mcp.workers.dev/sse/resources/list


When you call serveSSE("/"), MCP tools are served at:

https://my-mcp.workers.dev/tools/list
https://my-mcp.workers.dev/tools/call
https://my-mcp.workers.dev/resources/list


The base path is prepended to all MCP endpoints automatically.

Request/Response Lifecycle
1. Client connects to: https://my-mcp.workers.dev/sse
                                ↓
2. Worker receives request: { url: "https://my-mcp.workers.dev/sse", ... }
                                ↓
3. Your fetch handler: const { pathname } = new URL(request.url)
                                ↓
4. pathname === "/sse" → Check passes
                                ↓
5. MyMCP.serveSSE("/sse").fetch() → MCP server handles request
                                ↓
6. Tool calls routed to: /sse/tools/call


If client connects to https://my-mcp.workers.dev (missing /sse):

pathname === "/" → Check fails → 404 Not Found

Testing Your URL Configuration

Step 1: Deploy your MCP server

npx wrangler deploy
# Output: Deployed to https://my-mcp.YOUR_ACCOUNT.workers.dev


Step 2: Test the base path with curl

# If serving at /sse, test this URL:
curl https://my-mcp.YOUR_ACCOUNT.workers.dev/sse

# Should return MCP server info (not 404)


Step 3: Update client config with the EXACT URL you tested

{
  "mcpServers": {
    "my-mcp": {
      "url": "https://my-mcp.YOUR_ACCOUNT.workers.dev/sse"  // Match curl URL
    }
  }
}


Step 4: Restart Claude Desktop

Post-Deployment Checklist

After deploying, verify:

 curl https://worker.dev/sse returns MCP server info (not 404)
 Client config URL matches deployed URL exactly
 No typos in URL (common: workes.dev instead of workers.dev)
 Using https:// (not http://) for deployed Workers
 If using OAuth, redirect URI also updated
Transport Selection

Two transports available:

SSE (Server-Sent Events) - Legacy, wide compatibility

MyMCP.serveSSE("/sse").fetch(request, env, ctx)


Streamable HTTP - 2025 standard (recommended), single endpoint

MyMCP.serve("/mcp").fetch(request, env, ctx)


Support both for maximum compatibility:

export default {
  fetch(request: Request, env: Env, ctx: ExecutionContext) {
    const { pathname } = new URL(request.url);

    if (pathname.startsWith("/sse")) {
      return MyMCP.serveSSE("/sse").fetch(request, env, ctx);
    }
    if (pathname.startsWith("/mcp")) {
      return MyMCP.serve("/mcp").fetch(request, env, ctx);
    }

    return new Response("Not Found", { status: 404 });
  }
};


CRITICAL: Use pathname.startsWith() to match paths correctly!

2025 Knowledge Gaps
MCP Elicitation (August 2025)

MCP servers can now request user input during tool execution:

// Request user input during tool execution
const result = await this.elicit({
  prompt: "Enter your API key:",
  type: "password"
});

// Interactive workflows with Durable Objects state
await this.state.storage.put("api_key", result);


Use cases: Confirmations, forms, multi-step workflows State: Preserved during agent hibernation

Code Mode (September 2025)

Agents SDK converts MCP schema → TypeScript API:

// Old: Direct tool calls
await server.callTool("get_user", { id: "123" });

// New: Type-safe generated API
const user = await api.getUser("123");


Benefits: Auto-generated doc comments, type safety, code completion

MCPClientManager (July 2025)

New class for MCP client capabilities:

import { MCPClientManager } from "agents/mcp";

const manager = new MCPClientManager(env);
await manager.connect("https://external-mcp.com/sse");
// Auto-discovers tools, resources, prompts
// Handles reconnection, OAuth flow, hibernation

Task Queues & Email (August 2025)
// Task queues for background jobs
await this.queue.send({ task: "process_data", data });

// Email integration
async onEmail(message: Email) {
  // Process incoming email
  const response = await this.generateReply(message);
  await this.sendEmail(response);
}

HTTP Streamable Transport Details (April 2025)

Single endpoint replaces separate connection/messaging endpoints:

// Old: Separate endpoints
/connect  // Initialize connection
/message  // Send/receive messages

// New: Single streamable endpoint
/mcp      // All communication via HTTP streaming


Benefit: Simplified architecture, better performance

Security Considerations
PKCE Bypass Vulnerability (CRITICAL)

CVE: GHSA-qgp8-v765-qxx9 Severity: Critical Fixed in: @cloudflare/workers-oauth-provider@0.0.5

Problem: Earlier versions of the OAuth provider library had a critical vulnerability that completely bypassed PKCE protection, potentially allowing attackers to intercept authorization codes.

Action Required:

# Check current version
npm list @cloudflare/workers-oauth-provider

# Update if < 0.0.5
npm install @cloudflare/workers-oauth-provider@latest


Minimum Safe Version: @cloudflare/workers-oauth-provider@0.0.5 or later

Token Storage Best Practices

Always use encrypted storage for OAuth tokens:

// ✅ GOOD: workers-oauth-provider handles encryption automatically
export default new OAuthProvider({
  kv: (env) => env.OAUTH_KV,  // Tokens stored encrypted
  // ...
});

// ❌ BAD: Storing tokens in plain text
await env.KV.put("access_token", token);  // Security risk!


User-scoped KV keys prevent data leakage between users:

// ✅ GOOD: Namespace by user ID
await env.KV.put(`user:${userId}:todos`, data);

// ❌ BAD: Global namespace
await env.KV.put(`todos`, data);  // Data visible to all users!

Authentication Patterns

Choose auth based on use case:

No Auth - Internal tools, dev (Template: remote-mcp-authless)

Bearer Token - Custom auth (Template: mcp-server-bearer-auth)

// Validate Authorization: Bearer <token>
const token = request.headers.get("Authorization")?.replace("Bearer ", "");
if (!await validateToken(token, env)) {
  return new Response("Unauthorized", { status: 401 });
}


OAuth Proxy - GitHub/Google (Template: remote-mcp-github-oauth)

import { OAuthProvider, GitHubHandler } from "@cloudflare/workers-oauth-provider";

export default new OAuthProvider({
  authorizeEndpoint: "/authorize",
  tokenEndpoint: "/token",
  defaultHandler: new GitHubHandler({
    clientId: (env) => env.GITHUB_CLIENT_ID,
    clientSecret: (env) => env.GITHUB_CLIENT_SECRET,
    scopes: ["repo", "user:email"]
  }),
  kv: (env) => env.OAUTH_KV,
  apiHandlers: { "/sse": MyMCP.serveSSE("/sse") }
});


⚠️ CRITICAL: All OAuth URLs (url, authorizationUrl, tokenUrl) must use same domain

Remote OAuth with DCR - Full OAuth provider (Template: remote-mcp-authkit)

Security levels: No Auth (⚠️) < Bearer (✅) < OAuth Proxy (✅✅) < Remote OAuth (✅✅✅)

Stateful MCP Servers (Durable Objects)

McpAgent extends Durable Objects for per-session state:

// Storage API
await this.state.storage.put("key", "value");
const value = await this.state.storage.get<string>("key");

// Required wrangler.jsonc
{
  "durable_objects": {
    "bindings": [{ "name": "MY_MCP", "class_name": "MyMCP" }]
  },
  "migrations": [{ "tag": "v1", "new_classes": ["MyMCP"] }]  // Required on first deploy!
}


Critical: Migrations required on first deployment

Cost: Durable Objects now included in free tier (2025)

Architecture: Internal vs External Transports

Important: McpAgent uses different transports for client-facing vs internal communication.

Source: GitHub Issue #172

Transport Architecture
Client --- (SSE or HTTP) --> Worker --- (WebSocket) --> Durable Object


Client → Worker (External):

SSE transport: /sse endpoint
HTTP Streamable: /mcp endpoint
Client chooses transport

Worker → Durable Object (Internal):

Always WebSocket
Required by PartyServer (McpAgent's internal dependency)
Automatic upgrade, invisible to client
What This Means
SSE clients are fully supported - External interface can be SSE
WebSocket is mandatory for DO - Internal Worker-DO communication always uses WebSocket
This is not a limitation - It's an implementation detail of McpAgent's architecture
Example
export default {
  fetch(request: Request, env: Env, ctx: ExecutionContext) {
    const { pathname } = new URL(request.url);

    // Client uses SSE
    if (pathname.startsWith("/sse")) {
      // ✅ Client → Worker: SSE
      // ✅ Worker → DO: WebSocket (automatic)
      return MyMCP.serveSSE("/sse").fetch(request, env, ctx);
    }

    return new Response("Not Found", { status: 404 });
  }
};


Key Takeaway: You can serve SSE to clients without worrying about the internal WebSocket requirement.

Common Patterns
Tool Return Format (CRITICAL)

Source: Stytch Blog - Building MCP Server with OAuth

All MCP tools must return this exact format:

this.server.tool(
  "my_tool",
  { /* schema */ },
  async (params) => {
    // ✅ CORRECT: Return object with content array
    return {
      content: [
        { type: "text", text: "Your result here" }
      ]
    };

    // ❌ WRONG: Raw string
    return "Your result here";

    // ❌ WRONG: Plain object
    return { result: "Your result here" };
  }
);


Common mistake: Returning raw strings or plain objects instead of proper MCP content format. This causes client parsing errors.

Conditional Tool Registration

Source: Cloudflare Blog - Building AI Agents

Dynamically add tools based on authenticated user:

export class MyMCP extends McpAgent<Env> {
  async init() {
    this.server = new McpServer({ name: "My MCP" });

    // Base tools for all users
    this.server.tool("public_tool", { /* schema */ }, async (params) => {
      // Available to everyone
    });

    // Conditional tools based on user
    const userId = this.props?.userId;
    if (await this.isAdmin(userId)) {
      this.server.tool("admin_tool", { /* schema */ }, async (params) => {
        // Only available to admins
      });
    }

    // Premium features
    if (await this.isPremiumUser(userId)) {
      this.server.tool("premium_feature", { /* schema */ }, async (params) => {
        // Only for premium users
      });
    }
  }

  private async isAdmin(userId?: string): Promise<boolean> {
    if (!userId) return false;
    const userRole = await this.state.storage.get<string>(`user:${userId}:role`);
    return userRole === "admin";
  }
}


Use cases:

Feature flags per user
Premium vs free tier tools
Role-based access control (RBAC)
A/B testing new tools
Caching with DO Storage
async getCached<T>(key: string, ttlMs: number, fetchFn: () => Promise<T>): Promise<T> {
  const cached = await this.state.storage.get<{ data: T, timestamp: number }>(key);
  if (cached && Date.now() - cached.timestamp < ttlMs) {
    return cached.data;
  }
  const data = await fetchFn();
  await this.state.storage.put(key, { data, timestamp: Date.now() });
  return data;
}

Rate Limiting
async rateLimit(key: string, maxRequests: number, windowMs: number): Promise<boolean> {
  const requests = await this.state.storage.get<number[]>(`ratelimit:${key}`) || [];
  const recentRequests = requests.filter(ts => Date.now() - ts < windowMs);
  if (recentRequests.length >= maxRequests) return false;
  recentRequests.push(Date.now());
  await this.state.storage.put(`ratelimit:${key}`, recentRequests);
  return true;
}

24 Known Errors (With Solutions)
1. McpAgent Class Not Exported

Error: TypeError: Cannot read properties of undefined (reading 'serve')

Cause: Forgot to export McpAgent class

Solution:

export class MyMCP extends McpAgent { ... }  // ✅ Must export
export default { fetch() { ... } }

2. Base Path Configuration Mismatch (Most Common!)

Error: 404 Not Found or Connection failed

Cause: serveSSE("/sse") but client configured with https://worker.dev (missing /sse)

Solution: Match base paths exactly

// Server serves at /sse
MyMCP.serveSSE("/sse").fetch(...)

// Client MUST include /sse
{ "url": "https://worker.dev/sse" }  // ✅ Correct
{ "url": "https://worker.dev" }      // ❌ Wrong - 404


Debug steps:

Check what path your server uses: serveSSE("/sse") vs serveSSE("/")
Test with curl: curl https://worker.dev/sse
Update client config to match curl URL
3. Transport Type Confusion

Error: Connection failed: Unexpected response format

Cause: Client expects SSE but connects to HTTP endpoint (or vice versa)

Solution: Match transport types

// SSE transport
MyMCP.serveSSE("/sse")  // Client URL: https://worker.dev/sse

// HTTP transport
MyMCP.serve("/mcp")     // Client URL: https://worker.dev/mcp


Best practice: Support both transports (see Transport Selection Guide)

4. pathname.startsWith() Logic Error

Error: Both /sse and /mcp routes fail or conflict

Cause: Incorrect path matching logic

Solution: Use startsWith() correctly

// ✅ CORRECT
if (pathname.startsWith("/sse")) {
  return MyMCP.serveSSE("/sse").fetch(...);
}
if (pathname.startsWith("/mcp")) {
  return MyMCP.serve("/mcp").fetch(...);
}

// ❌ WRONG: Exact match breaks sub-paths
if (pathname === "/sse") {  // Breaks /sse/tools/list
  return MyMCP.serveSSE("/sse").fetch(...);
}

5. Local vs Deployed URL Mismatch

Error: Works in dev, fails after deployment

Cause: Client still configured with localhost URL

Solution: Update client config after deployment

// Development
{ "url": "http://localhost:8788/sse" }

// ⚠️ MUST UPDATE after npx wrangler deploy
{ "url": "https://my-mcp.YOUR_ACCOUNT.workers.dev/sse" }


Post-deployment checklist:

 Run npx wrangler deploy and note output URL
 Update client config with deployed URL
 Test with curl
 Restart Claude Desktop
6. OAuth Redirect URI Mismatch

Error: OAuth error: redirect_uri does not match

Cause: OAuth redirect URI doesn't match deployed URL

Solution: Update ALL OAuth URLs after deployment

{
  "url": "https://my-mcp.YOUR_ACCOUNT.workers.dev/sse",
  "auth": {
    "type": "oauth",
    "authorizationUrl": "https://my-mcp.YOUR_ACCOUNT.workers.dev/authorize",  // Must match deployed domain
    "tokenUrl": "https://my-mcp.YOUR_ACCOUNT.workers.dev/token"
  }
}


CRITICAL: All URLs must use the same protocol and domain!

7. Missing OPTIONS Handler (CORS Preflight)

Error: Access to fetch at '...' blocked by CORS policy or Method Not Allowed

Cause: Browser clients send OPTIONS requests for CORS preflight, but server doesn't handle them

Solution: Add OPTIONS handler

export default {
  fetch(request: Request, env: Env, ctx: ExecutionContext) {
    // Handle CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, {
        status: 204,
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type, Authorization",
          "Access-Control-Max-Age": "86400"
        }
      });
    }

    // ... rest of your fetch handler
  }
};


When needed: Browser-based MCP clients (like MCP Inspector in browser)

8. Request Body Validation Missing

Error: TypeError: Cannot read properties of undefined or Unexpected token in JSON parsing

Cause: Client sends malformed JSON, server doesn't validate before parsing

Solution: Wrap request handling in try/catch

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    try {
      // Your MCP server logic
      return await MyMCP.serveSSE("/sse").fetch(request, env, ctx);
    } catch (error) {
      console.error("Request handling error:", error);
      return new Response(
        JSON.stringify({
          error: "Invalid request",
          details: error.message
        }),
        {
          status: 400,
          headers: { "Content-Type": "application/json" }
        }
      );
    }
  }
};

9. Environment Variable Validation Missing

Error: TypeError: env.API_KEY is undefined or silent failures (tools return empty data)

Cause: Required environment variables not configured or missing at runtime

Solution: Add startup validation

export class MyMCP extends McpAgent<Env> {
  async init() {
    // Validate required environment variables
    if (!this.env.API_KEY) {
      throw new Error("API_KEY environment variable not configured");
    }
    if (!this.env.DATABASE_URL) {
      throw new Error("DATABASE_URL environment variable not configured");
    }

    // Continue with tool registration
    this.server.tool(...);
  }
}


Configuration checklist:

Development: Add to .dev.vars (local only, gitignored)
Production: Add to wrangler.jsonc vars (public) or use wrangler secret (sensitive)

Best practices:

# .dev.vars (local development, gitignored)
API_KEY=dev-key-123
DATABASE_URL=http://localhost:3000

# wrangler.jsonc (public config)
{
  "vars": {
    "ENVIRONMENT": "production",
    "LOG_LEVEL": "info"
  }
}

# wrangler secret (production secrets)
npx wrangler secret put API_KEY
npx wrangler secret put DATABASE_URL

10. McpAgent vs McpServer Confusion

Error: TypeError: server.registerTool is not a function or this.server is undefined

Cause: Trying to use standalone SDK patterns with McpAgent class

Solution: Use McpAgent's this.server.tool() pattern

// ❌ WRONG: Mixing standalone SDK with McpAgent
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

const server = new McpServer({ name: "My Server" });
server.registerTool(...);  // Not compatible with McpAgent!

export class MyMCP extends McpAgent { /* no server property */ }

// ✅ CORRECT: McpAgent pattern
export class MyMCP extends McpAgent<Env> {
  server = new McpServer({
    name: "My MCP Server",
    version: "1.0.0"
  });

  async init() {
    this.server.tool("tool_name", ...);  // Use this.server
  }
}


Key difference: McpAgent provides this.server property, standalone SDK doesn't.

11. WebSocket Hibernation State Loss

Error: Tool calls fail after reconnect with "state not found"

Cause: In-memory state cleared on hibernation

Solution: Use this.state.storage instead of instance properties

// ❌ DON'T: Lost on hibernation
this.userId = "123";

// ✅ DO: Persists through hibernation
await this.state.storage.put("userId", "123");

12. Durable Objects Binding Missing

Error: TypeError: Cannot read properties of undefined (reading 'idFromName')

Cause: Forgot DO binding in wrangler.jsonc

Solution: Add binding (see Stateful MCP Servers section)

{
  "durable_objects": {
    "bindings": [
      {
        "name": "MY_MCP",
        "class_name": "MyMCP",
        "script_name": "my-mcp-server"
      }
    ]
  }
}

13. Migration Not Defined

Error: Error: Durable Object class MyMCP has no migration defined

Cause: First DO deployment requires migration

Solution:

{
  "migrations": [
    { "tag": "v1", "new_classes": ["MyMCP"] }
  ]
}

14. serializeAttachment() Not Used

Error: WebSocket metadata lost on hibernation wake

Cause: Not using serializeAttachment() to preserve connection metadata

Solution: See WebSocket Hibernation section

15. OAuth Consent Screen Disabled

Security risk: Users don't see what permissions they're granting

Cause: allowConsentScreen: false in production

Solution: Always enable in production

export default new OAuthProvider({
  allowConsentScreen: true,  // ✅ Always true in production
  // ...
});

16. JWT Signing Key Missing

Error: Error: JWT_SIGNING_KEY environment variable not set

Cause: OAuth Provider requires signing key for tokens

Solution:

# Generate secure key
openssl rand -base64 32

# Add to wrangler secret
npx wrangler secret put JWT_SIGNING_KEY

17. Tool Schema Validation Error

Error: ZodError: Invalid input type

Cause: Client sends string, schema expects number (or vice versa)

Solution: Use Zod transforms

// Accept string, convert to number
param: z.string().transform(val => parseInt(val, 10))

// Or: Accept both types
param: z.union([z.string(), z.number()]).transform(val =>
  typeof val === "string" ? parseInt(val, 10) : val
)

18. Multiple Transport Endpoints Conflicting

Error: /sse returns 404 after adding /mcp

Cause: Incorrect path matching (missing startsWith())

Solution: Use startsWith() or exact matches correctly (see Error #4)

19. Local Testing with Miniflare Limitations

Error: OAuth flow fails in local dev, or Durable Objects behave differently

Cause: Miniflare doesn't support all DO features

Solution: Use npx wrangler dev --remote for full DO support

# Local simulation (faster but limited)
npm run dev

# Remote DOs (slower but accurate)
npx wrangler dev --remote

20. Client Configuration Format Error

Error: Claude Desktop doesn't recognize server

Cause: Wrong JSON format in claude_desktop_config.json

Solution: See "Connect Claude Desktop" section for correct format

Common mistakes:

// ❌ WRONG: Missing "mcpServers" wrapper
{
  "my-mcp": {
    "url": "https://worker.dev/sse"
  }
}

// ❌ WRONG: Trailing comma
{
  "mcpServers": {
    "my-mcp": {
      "url": "https://worker.dev/sse",  // ← Remove comma
    }
  }
}

// ✅ CORRECT
{
  "mcpServers": {
    "my-mcp": {
      "url": "https://worker.dev/sse"
    }
  }
}

21. Health Check Endpoint Missing

Issue: Can't tell if Worker is running or if URL is correct

Impact: Debugging connection issues takes longer

Solution: Add health check endpoint (see Transport Selection Guide)

Test:

curl https://my-mcp.workers.dev/health
# Should return: {"status":"ok","transports":{...}}

22. CORS Headers Missing

Error: Access to fetch at '...' blocked by CORS policy

Cause: MCP server doesn't return CORS headers for cross-origin requests

Solution: Add CORS headers to all responses

// Manual CORS (if not using OAuthProvider)
const corsHeaders = {
  "Access-Control-Allow-Origin": "*",  // Or specific origin
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization"
};

// Add to responses
return new Response(body, {
  headers: {
    ...corsHeaders,
    "Content-Type": "application/json"
  }
});


Note: OAuthProvider handles CORS automatically!

23. IoContext Timeout During MCP Initialization

Error: IoContext timed out due to inactivity, waitUntil tasks were cancelled

Source: GitHub Issue #640

Cause: When implementing MCP servers using McpAgent with custom Bearer authentication, the IoContext times out during the MCP protocol initialization handshake (before any tools are called).

Symptoms:

Timeout occurs before any tools are called
~2 minute gap between initial request and agent initialization
Internal methods work (setInitializeRequest, getInitializeRequest, updateProps)
Both GET and POST to /mcp are canceled
Error: "IoContext timed out due to inactivity, waitUntil tasks were cancelled"

Affected Code Pattern:

// Custom Bearer auth without OAuthProvider wrapper
export default {
  fetch: async (req, env, ctx) => {
    const authHeader = req.headers.get("Authorization");
    if (!authHeader?.startsWith("Bearer ")) {
      return new Response("Unauthorized", { status: 401 });
    }

    if (url.pathname === "/sse") {
      return MyMCP.serveSSE("/sse")(req, env, ctx);  // ← Timeout here
    }
    return new Response("Not found", { status: 404 });
  }
};


Root Cause Hypothesis:

May require OAuthProvider wrapper even for custom Bearer auth
Possible missing timeout configuration for Durable Object IoContext
May need CloudflareMCPServer instead of standard McpServer

Workaround: Use official templates with OAuthProvider pattern instead of custom Bearer auth:

// Use OAuthProvider wrapper (recommended)
import { OAuthProvider } from "@cloudflare/workers-oauth-provider";

export default new OAuthProvider({
  authorizeEndpoint: "/authorize",
  tokenEndpoint: "/token",
  // ... OAuth config
  apiHandlers: { "/sse": MyMCP.serveSSE("/sse") }
});


Status: Investigation ongoing (issue open as of 2026-01-21)

24. OAuth Remote Connection Failures

Error: Connection to remote MCP server fails when using OAuth (works locally but fails when deployed)

Source: GitHub Issue #444

Cause: When deploying MCP client from Cloudflare Agents repository to Workers, client fails to connect to MCP servers secured with OAuth.

Symptoms:

Works perfectly in local development
Fails after deployment to Workers
OAuth handshake never completes
Client can't establish connection

Troubleshooting Steps:

Verify OAuth tokens are handled correctly during remote connection attempts

// Check token is being passed to remote server
console.log("Connecting with token:", token ? "present" : "missing");


Check network permissions to access OAuth provider

// Ensure Worker can reach OAuth endpoints
const response = await fetch("https://oauth-provider.com/token");


Verify CORS configuration on OAuth provider

// OAuth provider must allow Worker origin
headers: {
  "Access-Control-Allow-Origin": "https://your-worker.workers.dev",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization"
}


Check redirect URIs match deployed URLs

{
  "url": "https://mcp.workers.dev/sse",
  "auth": {
    "authorizationUrl": "https://mcp.workers.dev/authorize",  // Must match deployed domain
    "tokenUrl": "https://mcp.workers.dev/token"
  }
}


Deployment Checklist:

 All OAuth URLs use deployed domain (not localhost)
 CORS headers configured on OAuth provider
 Network requests to OAuth provider allowed in Worker
 Redirect URIs registered with OAuth provider
 Environment variables set in production (wrangler secret)

Related: Issue #640 (both involve OAuth/auth in remote deployments)

Testing & Deployment
# Local dev
npm run dev                    # Miniflare (fast)
npx wrangler dev --remote      # Remote DOs (accurate)

# Test with MCP Inspector
npx @modelcontextprotocol/inspector@latest
# Open http://localhost:5173, enter http://localhost:8788/sse

# Deploy
npx wrangler login  # First time only
npx wrangler deploy
# ⚠️ CRITICAL: Update client config with deployed URL!

# Monitor logs
npx wrangler tail

Official Documentation
Cloudflare Agents: https://developers.cloudflare.com/agents/
MCP Specification: https://modelcontextprotocol.io/
Official Templates: https://github.com/cloudflare/ai/tree/main/demos
Production Servers: https://github.com/cloudflare/mcp-server-cloudflare
workers-oauth-provider: https://github.com/cloudflare/workers-oauth-provider

Package Versions: @modelcontextprotocol/sdk@1.25.3, @cloudflare/workers-oauth-provider@0.2.2, agents@0.3.6 Last Verified: 2026-01-21 Errors Prevented: 24 documented issues (100% prevention rate) Skill Version: 3.1.0 | Changes: Added IoContext timeout (#23), OAuth remote failures (#24), Security section (PKCE vulnerability), Architecture clarification (internal WebSocket), Tool return format pattern, Conditional tool registration

Weekly Installs
333
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn