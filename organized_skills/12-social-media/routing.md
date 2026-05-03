---
rating: ⭐⭐
title: routing
url: https://skills.sh/alsk1992/cloddsbot/routing
---

# routing

skills/alsk1992/cloddsbot/routing
routing
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill routing
SKILL.md
Routing - Complete API Reference

Route messages to specialized agents, configure channel bindings, and manage tool access policies.

Chat Commands
Agent Management
/agents                                     List available agents
/agent trading                              Switch to trading agent
/agent research                             Switch to research agent
/agent main                                 Switch to main agent
/agent status                               Current agent info

Channel Bindings
/bind trading                               Bind channel to trading agent
/bind research                              Bind channel to research agent
/unbind                                     Remove channel binding
/bindings                                   List all bindings

Tool Policies (Admin)
/tools                                      List available tools
/tools allow <agent> <tool>                 Allow tool for agent
/tools deny <agent> <tool>                  Deny tool for agent
/tools policy <agent>                       View agent's tool policy

TypeScript API Reference
Create Routing Service
import { createRoutingService } from 'clodds/routing';

const routing = createRoutingService({
  // Default agent
  defaultAgent: 'main',

  // Agent definitions
  agents: {
    main: {
      name: 'Main',
      description: 'General assistant',
      model: 'claude-3-sonnet',
      systemPrompt: 'You are a helpful trading assistant...',
      allowedTools: ['*'],  // All tools
    },
    trading: {
      name: 'Trading',
      description: 'Order execution specialist',
      model: 'claude-3-haiku',
      systemPrompt: 'You execute trades efficiently...',
      allowedTools: ['execute', 'portfolio', 'markets', 'feeds'],
    },
    research: {
      name: 'Research',
      description: 'Market analysis expert',
      model: 'claude-3-opus',
      systemPrompt: 'You provide deep market analysis...',
      allowedTools: ['web-search', 'web-fetch', 'markets', 'news'],
    },
    alerts: {
      name: 'Alerts',
      description: 'Notification handler',
      model: 'claude-3-haiku',
      systemPrompt: 'You manage price alerts...',
      allowedTools: ['alerts', 'feeds'],
    },
  },

  // Storage
  storage: 'sqlite',
  dbPath: './routing.db',
});

Route Message
// Route determines best agent
const route = await routing.route({
  message: 'Buy 100 shares of Trump YES',
  channelId: 'telegram-123',
  userId: 'user-456',
});

console.log(`Routed to: ${route.agent}`);
console.log(`Confidence: ${route.confidence}`);
console.log(`Reason: ${route.reason}`);

Get Available Agents
const agents = routing.getAgents();

for (const [id, agent] of Object.entries(agents)) {
  console.log(`${id}: ${agent.name}`);
  console.log(`  ${agent.description}`);
  console.log(`  Model: ${agent.model}`);
  console.log(`  Tools: ${agent.allowedTools.join(', ')}`);
}

Add Custom Agent
routing.addAgent({
  id: 'defi',
  name: 'DeFi Specialist',
  description: 'Solana and EVM DeFi expert',
  model: 'claude-3-sonnet',
  systemPrompt: 'You are an expert in DeFi protocols...',
  allowedTools: ['solana', 'evm', 'bridge', 'portfolio'],
  patterns: [
    /swap|dex|liquidity|pool/i,
    /solana|jupiter|raydium/i,
    /uniswap|1inch|bridge/i,
  ],
});

Update Agent
routing.updateAgent('trading', {
  model: 'claude-3-sonnet',  // Upgrade model
  allowedTools: [...currentTools, 'futures'],
});

Channel Bindings
// Bind channel to specific agent
await routing.addBinding({
  channelId: 'telegram-trading-group',
  agentId: 'trading',
});

// Get binding for channel
const binding = await routing.getBinding('telegram-trading-group');
console.log(`Channel bound to: ${binding?.agentId || 'default'}`);

// List all bindings
const bindings = await routing.getBindings();
for (const b of bindings) {
  console.log(`${b.channelId} → ${b.agentId}`);
}

// Remove binding
await routing.removeBinding('telegram-trading-group');

Tool Policies
// Check if tool is allowed for agent
const allowed = routing.isToolAllowed('trading', 'web-search');
console.log(`web-search allowed for trading: ${allowed}`);

// Get allowed tools for agent
const tools = routing.getAllowedTools('trading');
console.log(`Trading agent tools: ${tools.join(', ')}`);

// Update tool policy
routing.setToolPolicy('trading', {
  allow: ['execute', 'portfolio', 'futures'],
  deny: ['web-search', 'browser'],
});

Built-in Agents
Agent	Model	Purpose	Tools
main	Sonnet	General assistant	All
trading	Haiku	Fast order execution	Execute, Portfolio
research	Opus	Deep analysis	Search, Fetch, News
alerts	Haiku	Notifications	Alerts, Feeds
Routing Rules

Messages are routed based on:

Channel binding — If channel is bound, use that agent
Pattern matching — Match against agent patterns
Keyword detection — Trading terms → trading agent
Default fallback — Use main agent
Pattern Examples
{
  trading: [/buy|sell|order|position|close/i],
  research: [/analyze|research|explain|why/i],
  alerts: [/alert|notify|when|watch/i],
}

Tool Categories
Category	Tools
Execution	execute, portfolio, markets
Data	feeds, news, web-search, web-fetch
Crypto	solana, evm, bridge
System	files, browser, docker
Workspace Isolation

Each agent can have isolated workspace:

routing.addAgent({
  id: 'research',
  workspace: {
    directory: '/tmp/research',
    allowedPaths: ['/tmp/research/**'],
    sandboxed: true,
  },
});

Best Practices
Use fast models for trading — Haiku for time-sensitive operations
Restrict tools appropriately — Trading agent doesn't need browser
Channel bindings — Dedicated channels for specific workflows
Custom agents — Create specialized agents for your use case
Monitor routing — Check logs to see routing decisions
Weekly Installs
9
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn