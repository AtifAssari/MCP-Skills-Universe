---
title: openai-agents-sdk
url: https://skills.sh/naimalarain13/hackathon-ii_the-evolution-of-todo/openai-agents-sdk
---

# openai-agents-sdk

skills/naimalarain13/hackathon-ii_the-evolution-of-todo/openai-agents-sdk
openai-agents-sdk
Installation
$ npx skills add https://github.com/naimalarain13/hackathon-ii_the-evolution-of-todo --skill openai-agents-sdk
SKILL.md
OpenAI Agents SDK Skill

Build AI agents using OpenAI Agents SDK with support for Gemini and other LLMs via direct integration or OpenRouter.

Architecture
┌─────────────────────────────────────────────────────────────────────────┐
│                        OpenAI Agents SDK                                │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                         Agent                                     │   │
│  │  model: OpenAIChatCompletionsModel                               │   │
│  │    (via AsyncOpenAI with Gemini base_url)                        │   │
│  │  tools: [function_tool, ...]                                      │   │
│  │  mcp_servers: [MCPServerStreamableHttp(...)]                      │   │
│  │  handoffs: [specialized_agent, ...]                               │   │
│  └──────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
                              │
                              │ MCP Protocol
                              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    MCP Server (FastMCP)                                 │
│              @mcp.tool() for task operations                            │
└─────────────────────────────────────────────────────────────────────────┘

Quick Start
Installation
# Base installation
pip install openai-agents

# Or with uv
uv add openai-agents

Environment Variables
# For Direct Gemini Integration (Recommended)
GOOGLE_API_KEY=your-gemini-api-key

# OR for OpenRouter (Alternative)
OPENROUTER_API_KEY=your-openrouter-api-key

# For OpenAI (optional, for tracing)
OPENAI_API_KEY=your-openai-api-key

Using Gemini via Direct Integration (Recommended)

The recommended approach is to use AsyncOpenAI with Gemini's OpenAI-compatible endpoint. This avoids quota issues with LiteLLM.

import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner
from agents.run import RunConfig
from dotenv import load_dotenv

load_dotenv()

# Create custom OpenAI client pointing to Gemini
gemini_api_key = os.getenv("GOOGLE_API_KEY")
external_provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Create model using the custom client
model = OpenAIChatCompletionsModel(
    openai_client=external_provider,
    model="gemini-2.0-flash-exp",
)

# Configure agent with model
config = RunConfig(
    model=model,
    model_provider=external_provider,
    tracing_disabled=True
)

# Create agent
agent = Agent(
    name="Todo Assistant",
    instructions="You are a helpful task management assistant.",
)

# Run the agent with config
result = await Runner.run(agent, "Help me organize my tasks", config=config)
print(result.final_output)

Alternative: Using OpenRouter

OpenRouter provides access to multiple models through a single API, including free options.

import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner
from agents.run import RunConfig
from dotenv import load_dotenv

load_dotenv()

# Create OpenRouter client
openrouter_key = os.getenv("OPENROUTER_API_KEY")
external_provider = AsyncOpenAI(
    api_key=openrouter_key,
    base_url="https://openrouter.ai/api/v1",
)

# Use a free model (powered by Gemini or other providers)
model = OpenAIChatCompletionsModel(
    openai_client=external_provider,
    model="openai/gpt-oss-20b:free",
)

config = RunConfig(
    model=model,
    model_provider=external_provider,
    tracing_disabled=True
)

# Create and run agent
agent = Agent(
    name="Todo Assistant",
    instructions="You are a helpful task management assistant.",
)

result = await Runner.run(agent, "Help me organize my tasks", config=config)
print(result.final_output)

Reference
Pattern	Guide
Agent Creation	reference/agents.md
Function Tools	reference/function-tools.md
MCP Integration	reference/mcp-integration.md
Handoffs	reference/handoffs.md
Examples
Example	Description
examples/todo-agent.md	Complete todo agent with MCP tools
Templates
Template	Purpose
templates/agent_gemini.py	Basic Gemini agent template with direct integration
templates/agent_mcp.py	Agent with MCP server integration
Basic Agent with Function Tools
import asyncio
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, function_tool
from agents.run import RunConfig
import os

@function_tool
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    return f"The weather in {city} is sunny."

async def main():
    # Setup Gemini client
    external_provider = AsyncOpenAI(
        api_key=os.getenv("GOOGLE_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai",
    )

    model = OpenAIChatCompletionsModel(
        openai_client=external_provider,
        model="gemini-2.0-flash-exp",
    )

    config = RunConfig(
        model=model,
        model_provider=external_provider,
        tracing_disabled=True
    )

    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        tools=[get_weather],
    )

    result = await Runner.run(agent, "What's the weather in Tokyo?", config=config)
    print(result.final_output)

asyncio.run(main())

Agent with MCP Server

Connect your agent to an MCP server to access tools, resources, and prompts.

import asyncio
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner
from agents.mcp import MCPServerStreamableHttp
from agents.run import RunConfig

async def main():
    # Setup Gemini client
    external_provider = AsyncOpenAI(
        api_key=os.getenv("GOOGLE_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai",
    )

    model = OpenAIChatCompletionsModel(
        openai_client=external_provider,
        model="gemini-2.0-flash-exp",
    )

    config = RunConfig(
        model=model,
        model_provider=external_provider,
        tracing_disabled=True
    )

    async with MCPServerStreamableHttp(
        name="Todo MCP Server",
        params={
            "url": "http://localhost:8000/api/mcp",
            "timeout": 30,
        },
        cache_tools_list=True,
    ) as mcp_server:
        agent = Agent(
            name="Todo Assistant",
            instructions="""You are a task management assistant.
Use the MCP tools to help users manage their tasks:
- add_task: Create new tasks
- list_tasks: View existing tasks
- complete_task: Mark tasks as done
- delete_task: Remove tasks
- update_task: Modify tasks""",
            mcp_servers=[mcp_server],
        )

        result = await Runner.run(
            agent,
            "Show me my pending tasks",
            config=config
        )
        print(result.final_output)

asyncio.run(main())

Agent Handoffs

Create specialized agents that hand off conversations. Note: When using handoffs, all agents share the same RunConfig.

from agents import Agent, handoff, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from agents.run import RunConfig
from agents.extensions.handoff_prompt import prompt_with_handoff_instructions
import os

# Setup shared configuration
external_provider = AsyncOpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    openai_client=external_provider,
    model="gemini-2.0-flash-exp",
)

config = RunConfig(
    model=model,
    model_provider=external_provider,
    tracing_disabled=True
)

# Specialized agents (no model specified - uses config)
task_agent = Agent(
    name="Task Agent",
    instructions=prompt_with_handoff_instructions(
        "You specialize in task management. Help users create, update, and complete tasks."
    ),
)

help_agent = Agent(
    name="Help Agent",
    instructions=prompt_with_handoff_instructions(
        "You provide help and instructions about using the todo app."
    ),
)

# Triage agent
triage_agent = Agent(
    name="Triage Agent",
    instructions=prompt_with_handoff_instructions(
        """Route users to the appropriate agent:
- Task Agent: for creating, viewing, or managing tasks
- Help Agent: for questions about how to use the app"""
    ),
    handoffs=[task_agent, help_agent],
)

# Run with config
result = await Runner.run(triage_agent, "How do I add a task?", config=config)

Streaming Responses
from agents import Runner

result = Runner.run_streamed(agent, "List my tasks", config=config)

async for event in result.stream_events():
    if event.type == "run_item_stream_event":
        print(event.item, end="", flush=True)

print(result.final_output)

Model Settings
from agents import Agent, ModelSettings, Runner

agent = Agent(
    name="Assistant",
    model_settings=ModelSettings(
        include_usage=True,  # Track token usage
        tool_choice="auto",  # or "required", "none"
    ),
)

result = await Runner.run(agent, "Hello!", config=config)
print(f"Tokens used: {result.context_wrapper.usage.total_tokens}")

Tracing Control

Disable tracing when not using OpenAI:

from agents.run import RunConfig

# Tracing disabled in config
config = RunConfig(
    model=model,
    model_provider=external_provider,
    tracing_disabled=True  # Disable tracing
)

Supported Model Providers
Provider	Base URL	Model Examples
Gemini	https://generativelanguage.googleapis.com/v1beta/openai	gemini-2.0-flash-exp, gemini-1.5-pro
OpenRouter	https://openrouter.ai/api/v1	openai/gpt-oss-20b:free, google/gemini-2.0-flash-exp:free
MCP Connection Types
Type	Use Case	Class
Streamable HTTP	Production, low-latency	MCPServerStreamableHttp
SSE	Web clients, real-time	MCPServerSse
Stdio	Local processes	MCPServerStdio
Hosted	OpenAI-hosted MCP	HostedMCPTool
Error Handling
from agents import Runner, AgentError

try:
    result = await Runner.run(agent, "Hello")
    print(result.final_output)
except AgentError as e:
    print(f"Agent error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

Best Practices
Use Direct Integration - Use AsyncOpenAI with custom base_url instead of LiteLLM to avoid quota issues
Pass RunConfig - Always pass RunConfig to Runner.run() for non-OpenAI providers
Cache MCP tools - Use cache_tools_list=True for performance
Use handoffs - Create specialized agents for different functionality
Enable usage tracking - Set include_usage=True in ModelSettings to monitor costs
Disable tracing - Set tracing_disabled=True in RunConfig when not using OpenAI
Handle errors gracefully - Use try/except for agent execution
Use streaming - Implement streaming for better user experience
Share configuration - When using handoffs, all agents share the same RunConfig
Troubleshooting
Quota Exceeded Error on First Request

Problem: Getting quota exceeded error even on first request when using LiteLLM.

Solution: Switch to direct integration using AsyncOpenAI:

from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

external_provider = AsyncOpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    openai_client=external_provider,
    model="gemini-2.0-flash-exp",
)

config = RunConfig(
    model=model,
    model_provider=external_provider,
    tracing_disabled=True
)

result = await Runner.run(agent, "Hello", config=config)

MCP connection fails
Check MCP server is running
Verify URL is correct
Check timeout settings
Ensure cache_tools_list=True for performance
Gemini API errors
Verify GOOGLE_API_KEY is set correctly
Check model name: gemini-2.0-flash-exp or gemini-1.5-pro
Verify base_url is correct: https://generativelanguage.googleapis.com/v1beta/openai
Ensure API quota is not exceeded
Agent not using provided model

Problem: Agent ignores model configuration.

Solution: Always pass RunConfig to Runner.run():

result = await Runner.run(agent, message, config=config)

Weekly Installs
19
Repository
naimalarain13/h…-of-todo
GitHub Stars
2
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn