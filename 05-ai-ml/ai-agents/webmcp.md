---
title: webmcp
url: https://skills.sh/pillarhq/pillar-skills/webmcp
---

# webmcp

skills/pillarhq/pillar-skills/webmcp
webmcp
Installation
$ npx skills add https://github.com/pillarhq/pillar-skills --skill webmcp
SKILL.md
WebMCP Tools

Implement tools using the W3C WebMCP API (navigator.modelContext) so AI agents, browser assistants, and assistive technologies can call structured JavaScript functions on your page.

When to Apply

Reference these guidelines when:

Adding tools to a web page for browser AI agents
Registering callable functions via navigator.modelContext
Exposing existing page functionality to agents
Building cooperative human-in-the-loop agent workflows
Essential Rules
Priority	Rule	Description
CRITICAL	tool-definition	Every tool needs name, description, inputSchema, and execute
CRITICAL	security	Validate params, confirm destructive actions, don't leak sensitive data
HIGH	descriptions	Write specific descriptions — this is what the LLM reads to pick the tool
HIGH	dynamic-registration	Register/unregister tools as SPA state changes
MEDIUM	user-interaction	Use agent.requestUserInteraction() for purchases, deletions, and sends
Quick Reference
1. Register a Tool (CRITICAL)
navigator.modelContext.registerTool({
  name: "add-to-cart",
  description: "Add a product to the shopping cart by ID",
  inputSchema: {
    type: "object",
    properties: {
      productId: { type: "string", description: "Product ID" },
      quantity: { type: "number", description: "How many to add (1-100)" }
    },
    required: ["productId"]
  },
  execute: async ({ productId, quantity }) => {
    await cartApi.add(productId, quantity ?? 1);
    return { content: [{ type: "text", text: `Added ${quantity ?? 1} to cart` }] };
  }
});

2. Feature Detection (CRITICAL)
if ("modelContext" in navigator) {
  navigator.modelContext.registerTool({...});
}

3. Tool Descriptions (HIGH)
// Good — specific, includes what it returns
description: "Search available flights. Returns {id, airline, price, departure, arrival}. Does not book — use book-flight to complete."

// Bad — vague
description: "Search flights"

4. User Confirmation (MEDIUM)
execute: async ({ productId }, agent) => {
  const ok = await agent.requestUserInteraction(() =>
    confirm(`Buy product ${productId}?`)
  );
  if (!ok) throw new Error("Cancelled");
  await purchase(productId);
  return { content: [{ type: "text", text: "Purchased" }] };
}

5. Dynamic Registration for SPAs (HIGH)
// React — register on mount, unregister on unmount
useEffect(() => {
  if (!("modelContext" in navigator)) return;
  navigator.modelContext.registerTool({ name: "edit-doc", ... });
  return () => navigator.modelContext.unregisterTool("edit-doc");
}, [doc.id]);

How to Use

Read individual rule files for detailed explanations and code examples:

rules/tool-definition.md
rules/descriptions.md
rules/security.md
rules/dynamic-registration.md
rules/user-interaction.md


For the complete guide with all patterns expanded: AGENTS.md

Weekly Installs
66
Repository
pillarhq/pillar-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass