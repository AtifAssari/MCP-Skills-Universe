---
title: agentmail-toolkit
url: https://skills.sh/agentmail-to/agentmail-skills/agentmail-toolkit
---

# agentmail-toolkit

skills/agentmail-to/agentmail-skills/agentmail-toolkit
agentmail-toolkit
Installation
$ npx skills add https://github.com/agentmail-to/agentmail-skills --skill agentmail-toolkit
SKILL.md
AgentMail Toolkit

Pre-built email tools for popular agent frameworks. Instantly add inbox management, sending, receiving, and email automation to your agents.

Installation
# TypeScript/Node
npm install agentmail-toolkit

# Python
pip install agentmail-toolkit

Configuration

Set your API key as an environment variable:

export AGENTMAIL_API_KEY=your-api-key


Get your API key from console.agentmail.to.

TypeScript Frameworks
Vercel AI SDK
import { AgentMailToolkit } from "agentmail-toolkit/ai-sdk";
import { streamText } from "ai";
import { openai } from "@ai-sdk/openai";

const toolkit = new AgentMailToolkit();

const result = await streamText({
  model: openai("gpt-4o"),
  messages,
  system: "You are an email agent that can send and receive emails.",
  tools: toolkit.getTools(),
});

LangChain
import { createAgent, HumanMessage, AIMessage } from "langchain";
import { AgentMailToolkit } from "agentmail-toolkit/langchain";

const agent = createAgent({
  model: "openai:gpt-4o",
  tools: new AgentMailToolkit().getTools(),
  systemPrompt: "You are an email agent that can send and receive emails.",
});

const result = await agent.stream({ messages }, { streamMode: "messages" });

Clawdbot (Pi Agent)

For Clawdbot/Pi Agent integration.

import { AgentMailToolkit } from "agentmail-toolkit/clawdbot";

const toolkit = new AgentMailToolkit();
const tools = toolkit.getTools();

// Each tool has: name, label, description, parameters, execute
for (const tool of tools) {
  agent.registerTool(tool);
}

Python Frameworks
OpenAI Agents SDK
from agentmail_toolkit.openai import AgentMailToolkit
from agents import Agent

agent = Agent(
    name="Email Agent",
    instructions="You can send, receive, and manage emails.",
    tools=AgentMailToolkit().get_tools(),
)

LangChain
from langchain.agents import create_agent
from agentmail_toolkit.langchain import AgentMailToolkit

agent = create_agent(
    model="gpt-4o",
    system_prompt="You are an email agent that can send and receive emails.",
    tools=AgentMailToolkit().get_tools(),
)

result = agent.stream({"messages": messages}, stream_mode="messages")

LiveKit Agents

For voice AI agents with email capabilities.

from livekit.agents import Agent
from agentmail_toolkit.livekit import AgentMailToolkit

agent = Agent(
    name="Voice Email Agent",
    tools=AgentMailToolkit().get_tools(),
)

Available Tools

The Node and Python toolkits ship different tool sets. The Node toolkit includes drafts; the Python toolkit does not.

Tool	Description	Node	Python
create_inbox	Create a new email inbox	✓	✓
list_inboxes	List all inboxes	✓	✓
get_inbox	Get inbox details	✓	✓
delete_inbox	Delete an inbox	✓	✓
send_message	Send an email	✓	✓
reply_to_message	Reply to an email	✓	✓
forward_message	Forward an email	✓	✓
update_message	Update message labels	✓	✓
list_threads	List email threads	✓	✓
get_thread	Get thread details	✓	✓
get_attachment	Download an attachment	✓	✓
create_draft	Create a draft message	✓	—
list_drafts	List drafts in an inbox	✓	—
get_draft	Get a draft by ID	✓	—
update_draft	Update a draft	✓	—
send_draft	Send a previously-created draft	✓	—
delete_draft	Delete a draft without sending	✓	—

Node toolkit: 17 tools. Python toolkit: 11 tools. If you need draft support from Python, call client.inboxes.drafts.* directly on the AgentMail SDK client.

Custom Configuration

Both toolkits take an existing SDK client as their only constructor argument — they do NOT accept apiKey / api_key directly. If you need a custom API key, construct the SDK client with the key first, then pass the client to the toolkit.

TypeScript
import { AgentMailClient } from "agentmail";
import { AgentMailToolkit } from "agentmail-toolkit/ai-sdk";

// With a custom API key
const client = new AgentMailClient({ apiKey: "your-api-key" });
const toolkit = new AgentMailToolkit(client);

// Or omit the argument to auto-read AGENTMAIL_API_KEY from env
const defaultToolkit = new AgentMailToolkit();

Python
from agentmail import AgentMail
from agentmail_toolkit.openai import AgentMailToolkit

# With a custom API key
client = AgentMail(api_key="your-api-key")
toolkit = AgentMailToolkit(client=client)

# Or omit the argument to auto-read AGENTMAIL_API_KEY from env
default_toolkit = AgentMailToolkit()

Framework Summary
Framework	TypeScript Import	Python Import
Vercel AI SDK	from 'agentmail-toolkit/ai-sdk'	-
LangChain	from 'agentmail-toolkit/langchain'	from agentmail_toolkit.langchain import AgentMailToolkit
Clawdbot	from 'agentmail-toolkit/clawdbot'	-
OpenAI Agents SDK	-	from agentmail_toolkit.openai import AgentMailToolkit
LiveKit Agents	-	from agentmail_toolkit.livekit import AgentMailToolkit
Weekly Installs
253
Repository
agentmail-to/ag…l-skills
GitHub Stars
10
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn