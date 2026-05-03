---
rating: ⭐⭐⭐
title: javascript-sdk
url: https://skills.sh/inference-sh/skills/javascript-sdk
---

# javascript-sdk

skills/inference-sh/skills/javascript-sdk
javascript-sdk
Installation
$ npx skills add https://github.com/inference-sh/skills --skill javascript-sdk
SKILL.md
JavaScript SDK

Build AI applications with the inference.sh JavaScript/TypeScript SDK.

Quick Start
npm install @inferencesh/sdk

import { inference } from '@inferencesh/sdk';

const client = inference({ apiKey: 'inf_your_key' });

// Run an AI app
const result = await client.run({
  app: 'infsh/flux-schnell',
  input: { prompt: 'A sunset over mountains' }
});
console.log(result.output);

Installation
npm install @inferencesh/sdk
# or
yarn add @inferencesh/sdk
# or
pnpm add @inferencesh/sdk


Requirements: Node.js 18.0.0+ (or modern browser with fetch)

Authentication
import { inference } from '@inferencesh/sdk';

// Direct API key
const client = inference({ apiKey: 'inf_your_key' });

// From environment variable (recommended)
const client = inference({ apiKey: process.env.INFERENCE_API_KEY });

// For frontend apps (use proxy)
const client = inference({ proxyUrl: '/api/inference/proxy' });


Get your API key: Settings → API Keys → Create API Key

Running Apps
Basic Execution
const result = await client.run({
  app: 'infsh/flux-schnell',
  input: { prompt: 'A cat astronaut' }
});

console.log(result.status);  // "completed"
console.log(result.output);  // Output data

Fire and Forget
const task = await client.run({
  app: 'google/veo-3-1-fast',
  input: { prompt: 'Drone flying over mountains' }
}, { wait: false });

console.log(`Task ID: ${task.id}`);
// Check later with client.getTask(task.id)

Streaming Progress
const stream = await client.run({
  app: 'google/veo-3-1-fast',
  input: { prompt: 'Ocean waves at sunset' }
}, { stream: true });

for await (const update of stream) {
  console.log(`Status: ${update.status}`);
  if (update.logs?.length) {
    console.log(update.logs.at(-1));
  }
}

Run Parameters
Parameter	Type	Description
app	string	App ID (namespace/name@version)
input	object	Input matching app schema
setup	object	Hidden setup configuration
infra	string	'cloud' or 'private'
session	string	Session ID for stateful execution
session_timeout	number	Idle timeout (1-3600 seconds)
File Handling
Automatic Upload
const result = await client.run({
  app: 'image-processor',
  input: {
    image: '/path/to/image.png'  // Auto-uploaded
  }
});

Manual Upload
// Basic upload
const file = await client.uploadFile('/path/to/image.png');

// With options
const file = await client.uploadFile('/path/to/image.png', {
  filename: 'custom_name.png',
  contentType: 'image/png',
  public: true
});

const result = await client.run({
  app: 'image-processor',
  input: { image: file.uri }
});

Browser File Upload
const input = document.querySelector('input[type="file"]');
const file = await client.uploadFile(input.files[0]);

Sessions (Stateful Execution)

Keep workers warm across multiple calls:

// Start new session
const result = await client.run({
  app: 'my-app',
  input: { action: 'init' },
  session: 'new',
  session_timeout: 300  // 5 minutes
});
const sessionId = result.session_id;

// Continue in same session
const result2 = await client.run({
  app: 'my-app',
  input: { action: 'process' },
  session: sessionId
});

Agent SDK
Template Agents

Use pre-built agents from your workspace:

const agent = client.agent('my-team/support-agent@latest');

// Send message
const response = await agent.sendMessage('Hello!');
console.log(response.text);

// Multi-turn conversation
const response2 = await agent.sendMessage('Tell me more');

// Reset conversation
agent.reset();

// Get chat history
const chat = await agent.getChat();

Ad-hoc Agents

Create custom agents programmatically:

import { tool, string, number, appTool } from '@inferencesh/sdk';

// Define tools
const calculator = tool('calculate')
  .describe('Perform a calculation')
  .param('expression', string('Math expression'))
  .build();

const imageGen = appTool('generate_image', 'infsh/flux-schnell@latest')
  .describe('Generate an image')
  .param('prompt', string('Image description'))
  .build();

// Create agent
const agent = client.agent({
  core_app: { ref: 'infsh/claude-sonnet-4@latest' },
  system_prompt: 'You are a helpful assistant.',
  tools: [calculator, imageGen],
  temperature: 0.7,
  max_tokens: 4096
});

const response = await agent.sendMessage('What is 25 * 4?');

Available Core Apps
Model	App Reference
Claude Sonnet 4	infsh/claude-sonnet-4@latest
Claude 3.5 Haiku	infsh/claude-haiku-35@latest
GPT-4o	infsh/gpt-4o@latest
GPT-4o Mini	infsh/gpt-4o-mini@latest
Tool Builder API
Parameter Types
import {
  string, number, integer, boolean,
  enumOf, array, obj, optional
} from '@inferencesh/sdk';

const name = string('User\'s name');
const age = integer('Age in years');
const score = number('Score 0-1');
const active = boolean('Is active');
const priority = enumOf(['low', 'medium', 'high'], 'Priority');
const tags = array(string('Tag'), 'List of tags');
const address = obj({
  street: string('Street'),
  city: string('City'),
  zip: optional(string('ZIP'))
}, 'Address');

Client Tools (Run in Your Code)
const greet = tool('greet')
  .display('Greet User')
  .describe('Greets a user by name')
  .param('name', string('Name to greet'))
  .requireApproval()
  .build();

App Tools (Call AI Apps)
const generate = appTool('generate_image', 'infsh/flux-schnell@latest')
  .describe('Generate an image from text')
  .param('prompt', string('Image description'))
  .setup({ model: 'schnell' })
  .input({ steps: 20 })
  .requireApproval()
  .build();

Agent Tools (Delegate to Sub-agents)
import { agentTool } from '@inferencesh/sdk';

const researcher = agentTool('research', 'my-org/researcher@v1')
  .describe('Research a topic')
  .param('topic', string('Topic to research'))
  .build();

Webhook Tools (Call External APIs)
import { webhookTool } from '@inferencesh/sdk';

const notify = webhookTool('slack', 'https://hooks.slack.com/...')
  .describe('Send Slack notification')
  .secret('SLACK_SECRET')
  .param('channel', string('Channel'))
  .param('message', string('Message'))
  .build();

Internal Tools (Built-in Capabilities)
import { internalTools } from '@inferencesh/sdk';

const config = internalTools()
  .plan()
  .memory()
  .webSearch(true)
  .codeExecution(true)
  .imageGeneration({
    enabled: true,
    appRef: 'infsh/flux@latest'
  })
  .build();

const agent = client.agent({
  core_app: { ref: 'infsh/claude-sonnet-4@latest' },
  internal_tools: config
});

Streaming Agent Responses
const response = await agent.sendMessage('Explain quantum computing', {
  onMessage: (msg) => {
    if (msg.content) {
      process.stdout.write(msg.content);
    }
  },
  onToolCall: async (call) => {
    console.log(`\n[Tool: ${call.name}]`);
    const result = await executeTool(call.name, call.args);
    agent.submitToolResult(call.id, result);
  }
});

File Attachments
// From file path (Node.js)
import { readFileSync } from 'fs';
const response = await agent.sendMessage('What\'s in this image?', {
  files: [readFileSync('image.png')]
});

// From base64
const response = await agent.sendMessage('Analyze this', {
  files: ['data:image/png;base64,iVBORw0KGgo...']
});

// From browser File object
const input = document.querySelector('input[type="file"]');
const response = await agent.sendMessage('Describe this', {
  files: [input.files[0]]
});

Skills (Reusable Context)
const agent = client.agent({
  core_app: { ref: 'infsh/claude-sonnet-4@latest' },
  skills: [
    {
      name: 'code-review',
      description: 'Code review guidelines',
      content: '# Code Review\n\n1. Check security\n2. Check performance...'
    },
    {
      name: 'api-docs',
      description: 'API documentation',
      url: 'https://example.com/skills/api-docs.md'
    }
  ]
});

Server Proxy (Frontend Apps)

For browser apps, proxy through your backend to keep API keys secure:

Client Setup
const client = inference({
  proxyUrl: '/api/inference/proxy'
  // No apiKey needed on frontend
});

Next.js Proxy (App Router)
// app/api/inference/proxy/route.ts
import { createRouteHandler } from '@inferencesh/sdk/proxy/nextjs';

const route = createRouteHandler({
  apiKey: process.env.INFERENCE_API_KEY
});

export const POST = route.POST;

Express Proxy
import express from 'express';
import { createProxyMiddleware } from '@inferencesh/sdk/proxy/express';

const app = express();
app.use('/api/inference/proxy', createProxyMiddleware({
  apiKey: process.env.INFERENCE_API_KEY
}));

Supported Frameworks
Next.js (App Router & Pages Router)
Express
Hono
Remix
SvelteKit
TypeScript Support

Full type definitions included:

import type {
  TaskDTO,
  ChatDTO,
  ChatMessageDTO,
  AgentTool,
  TaskStatusCompleted,
  TaskStatusFailed
} from '@inferencesh/sdk';

if (result.status === TaskStatusCompleted) {
  console.log('Done!');
} else if (result.status === TaskStatusFailed) {
  console.log('Failed:', result.error);
}

Error Handling
import { RequirementsNotMetException, InferenceError } from '@inferencesh/sdk';

try {
  const result = await client.run({ app: 'my-app', input: {...} });
} catch (e) {
  if (e instanceof RequirementsNotMetException) {
    console.log('Missing requirements:');
    for (const err of e.errors) {
      console.log(`  - ${err.type}: ${err.key}`);
    }
  } else if (e instanceof InferenceError) {
    console.log('API error:', e.message);
  }
}

Human Approval Workflows
const response = await agent.sendMessage('Delete all temp files', {
  onToolCall: async (call) => {
    if (call.requiresApproval) {
      const approved = await promptUser(`Allow ${call.name}?`);
      if (approved) {
        const result = await executeTool(call.name, call.args);
        agent.submitToolResult(call.id, result);
      } else {
        agent.submitToolResult(call.id, { error: 'Denied by user' });
      }
    }
  }
});

CommonJS Support
const { inference, tool, string } = require('@inferencesh/sdk');

const client = inference({ apiKey: 'inf_...' });
const result = await client.run({...});

Reference Files
Agent Patterns - Multi-agent, RAG, batch processing patterns
Tool Builder - Complete tool builder API reference
Server Proxy - Next.js, Express, Hono, Remix, SvelteKit setup
Streaming - Real-time progress updates and SSE handling
File Handling - Upload, download, and manage files
Sessions - Stateful execution with warm workers
TypeScript - Type definitions and type-safe patterns
React Integration - Hooks, components, and patterns
Related Skills
# Python SDK
npx skills add inference-sh/skills@python-sdk

# Full platform skill (all 250+ apps via CLI)
npx skills add inference-sh/skills@infsh-cli

# LLM models
npx skills add inference-sh/skills@llm-models

# Image generation
npx skills add inference-sh/skills@ai-image-generation

Documentation
JavaScript SDK Reference - Full API documentation
Agent SDK Overview - Building agents
Tool Builder Reference - Creating tools
Server Proxy Setup - Frontend integration
Authentication - API key setup
Streaming - Real-time updates
File Uploads - File handling
Weekly Installs
342
Repository
inference-sh/skills
GitHub Stars
395
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn