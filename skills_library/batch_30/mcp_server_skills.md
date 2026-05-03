---
title: mcp-server-skills
url: https://skills.sh/gocallum/nextjs16-agent-skills/mcp-server-skills
---

# mcp-server-skills

skills/gocallum/nextjs16-agent-skills/mcp-server-skills
mcp-server-skills
Installation
$ npx skills add https://github.com/gocallum/nextjs16-agent-skills --skill mcp-server-skills
SKILL.md
Links
Model Context Protocol: https://modelcontextprotocol.io/
mcp-handler (HTTP): https://www.npmjs.com/package/mcp-handler
Reference implementation (Roll Dice): https://github.com/gocallum/rolldice-mcpserver
Claude Desktop + mcp-remote bridge: https://www.npmjs.com/package/mcp-remote
Folder Structure (Next.js App Router)
app/
  api/[transport]/route.ts   # One handler for all transports (e.g., /api/mcp)
  actions/mcp-actions.ts     # Server actions reusing the same logic/schemas
lib/
  dice.ts | tools.ts         # Zod schemas, tool definitions, pure logic
components/                  # UI that calls server actions for web testing


Goal: Keep route.ts minimal. Put logic + Zod schemas in lib/* so both the MCP handler and server actions share a single source of truth.

Shared Zod Schema + Tool Definition
// lib/dice.ts
import { z } from "zod";

export const diceSchema = z.number().int().min(2);

export function rollDice(sides: number) {
  const validated = diceSchema.parse(sides);
  const value = 1 + Math.floor(Math.random() * validated);
  return { type: "text" as const, text: `🎲 You rolled a ${value}!` };
}

export const rollDiceTool = {
  name: "roll_dice",
  description: "Rolls an N-sided die",
  schema: { sides: diceSchema },
} as const;

Reusable Server Actions (Web UI + Tests)
// app/actions/mcp-actions.ts
"use server";
import { rollDice as rollDiceCore, rollDiceTool } from "@/lib/dice";

export async function rollDice(sides: number) {
  try {
    const result = rollDiceCore(sides);
    return { success: true, result: { content: [result] } };
  } catch {
    return {
      success: false,
      error: { code: -32602, message: "Invalid parameters: sides must be >= 2" },
    };
  }
}

export async function listTools() {
  return {
    success: true,
    result: {
      tools: [
        {
          name: rollDiceTool.name,
          description: rollDiceTool.description,
          inputSchema: {
            type: "object",
            properties: { sides: { type: "number", minimum: 2 } },
            required: ["sides"],
          },
        },
      ],
    },
  };
}


Server actions call the same logic as the MCP handler and power the web UI, keeping responses aligned.

Lightweight MCP Route
// app/api/[transport]/route.ts
import { createMcpHandler } from "mcp-handler";
import { rollDice, rollDiceTool } from "@/lib/dice";

const handler = createMcpHandler(
  (server) => {
    server.tool(
      rollDiceTool.name,
      rollDiceTool.description,
      rollDiceTool.schema,
      async ({ sides }) => ({ content: [rollDice(sides)] }),
    );
  },
  {}, // server options
  {
    basePath: "/api",     // must match folder path
    maxDuration: 60,
    verboseLogs: true,
  },
);

export { handler as GET, handler as POST };


Pattern highlights

Route only wires createMcpHandler; no business logic inline.
server.tool consumes the shared tool schema/description and calls shared logic.
basePath should align with the folder (e.g., /api/[transport]).
Works for SSE/HTTP transports; stdio can be added separately if needed.
Claude Desktop Config (mcp-remote)
{
  "mcpServers": {
    "rolldice": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://localhost:3000/api/mcp"]
    }
  }
}

Best Practices
Single source of truth — schemas + logic in lib/*; both MCP tools and server actions import them.
Validation first — use Zod for inputs and reuse the same schema for UI + MCP.
Keep route.ts light — only handler wiring, logging, and transport config.
Shared responses — standardize { success, result | error } shapes for tools and UI.
Vercel-friendly — avoid stateful globals; configure maxDuration and runtime if needed.
Multiple transports — expose /api/[transport] for HTTP/SSE; add stdio entrypoint when required.
Local testing — hit server actions from the web UI to ensure MCP responses stay in sync.
Weekly Installs
219
Repository
gocallum/nextjs…t-skills
GitHub Stars
19
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass