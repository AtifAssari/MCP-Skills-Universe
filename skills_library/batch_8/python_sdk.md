---
title: python-sdk
url: https://skills.sh/inference-sh/skills/python-sdk
---

# python-sdk

skills/inference-sh/skills/python-sdk
python-sdk
Installation
$ npx skills add https://github.com/inference-sh/skills --skill python-sdk
SKILL.md
Python SDK

Build AI applications with the inference.sh Python SDK.

Quick Start
pip install inferencesh

from inferencesh import inference

client = inference(api_key="inf_your_key")

# Run an AI app
result = client.run({
    "app": "infsh/flux-1-dev",
    "input": {"prompt": "A sunset over mountains"}
})
print(result["output"])

Installation
# Standard installation
pip install inferencesh

# With async support
pip install inferencesh[async]


Requirements: Python 3.8+

Authentication
import os
from inferencesh import inference

# Direct API key
client = inference(api_key="inf_your_key")

# From environment variable (recommended)
client = inference(api_key=os.environ["INFERENCE_API_KEY"])


Get your API key: Settings → API Keys → Create API Key

Running Apps
Basic Execution
result = client.run({
    "app": "infsh/flux-1-dev",
    "input": {"prompt": "A cat astronaut"}
})

print(result["status"])  # "completed"
print(result["output"])  # Output data

Fire and Forget
task = client.run({
    "app": "google/veo-3-1-fast",
    "input": {"prompt": "Drone flying over mountains"}
}, wait=False)

print(f"Task ID: {task['id']}")
# Check later with client.get_task(task['id'])

Streaming Progress
for update in client.run({
    "app": "google/veo-3-1-fast",
    "input": {"prompt": "Ocean waves at sunset"}
}, stream=True):
    print(f"Status: {update['status']}")
    if update.get("logs"):
        print(update["logs"][-1])

Run Parameters
Parameter	Type	Description
app	string	App ID (namespace/name@version)
input	dict	Input matching app schema
setup	dict	Hidden setup configuration
infra	string	'cloud' or 'private'
session	string	Session ID for stateful execution
session_timeout	int	Idle timeout (1-3600 seconds)
File Handling
Automatic Upload
result = client.run({
    "app": "image-processor",
    "input": {
        "image": "/path/to/image.png"  # Auto-uploaded
    }
})

Manual Upload
from inferencesh import UploadFileOptions

# Basic upload
file = client.upload_file("/path/to/image.png")

# With options
file = client.upload_file(
    "/path/to/image.png",
    UploadFileOptions(
        filename="custom_name.png",
        content_type="image/png",
        public=True
    )
)

result = client.run({
    "app": "image-processor",
    "input": {"image": file["uri"]}
})

Sessions (Stateful Execution)

Keep workers warm across multiple calls:

# Start new session
result = client.run({
    "app": "my-app",
    "input": {"action": "init"},
    "session": "new",
    "session_timeout": 300  # 5 minutes
})
session_id = result["session_id"]

# Continue in same session
result = client.run({
    "app": "my-app",
    "input": {"action": "process"},
    "session": session_id
})

Agent SDK
Template Agents

Use pre-built agents from your workspace:

agent = client.agent("my-team/support-agent@latest")

# Send message
response = agent.send_message("Hello!")
print(response.text)

# Multi-turn conversation
response = agent.send_message("Tell me more")

# Reset conversation
agent.reset()

# Get chat history
chat = agent.get_chat()

Ad-hoc Agents

Create custom agents programmatically:

from inferencesh import tool, string, number, app_tool

# Define tools
calculator = (
    tool("calculate")
    .describe("Perform a calculation")
    .param("expression", string("Math expression"))
    .build()
)

image_gen = (
    app_tool("generate_image", "infsh/flux-1-dev@latest")
    .describe("Generate an image")
    .param("prompt", string("Image description"))
    .build()
)

# Create agent
agent = client.agent({
    "core_app": {"ref": "infsh/claude-sonnet-4@latest"},
    "system_prompt": "You are a helpful assistant.",
    "tools": [calculator, image_gen],
    "temperature": 0.7,
    "max_tokens": 4096
})

response = agent.send_message("What is 25 * 4?")

Available Core Apps
Model	App Reference
Claude Sonnet 4	infsh/claude-sonnet-4@latest
Claude 3.5 Haiku	infsh/claude-haiku-35@latest
GPT-4o	infsh/gpt-4o@latest
GPT-4o Mini	infsh/gpt-4o-mini@latest
Tool Builder API
Parameter Types
from inferencesh import (
    string, number, integer, boolean,
    enum_of, array, obj, optional
)

name = string("User's name")
age = integer("Age in years")
score = number("Score 0-1")
active = boolean("Is active")
priority = enum_of(["low", "medium", "high"], "Priority")
tags = array(string("Tag"), "List of tags")
address = obj({
    "street": string("Street"),
    "city": string("City"),
    "zip": optional(string("ZIP"))
}, "Address")

Client Tools (Run in Your Code)
greet = (
    tool("greet")
    .display("Greet User")
    .describe("Greets a user by name")
    .param("name", string("Name to greet"))
    .require_approval()
    .build()
)

App Tools (Call AI Apps)
generate = (
    app_tool("generate_image", "infsh/flux-1-dev@latest")
    .describe("Generate an image from text")
    .param("prompt", string("Image description"))
    .setup({"model": "schnell"})
    .input({"steps": 20})
    .require_approval()
    .build()
)

Agent Tools (Delegate to Sub-agents)
from inferencesh import agent_tool

researcher = (
    agent_tool("research", "my-org/researcher@v1")
    .describe("Research a topic")
    .param("topic", string("Topic to research"))
    .build()
)

Webhook Tools (Call External APIs)
from inferencesh import webhook_tool

notify = (
    webhook_tool("slack", "https://hooks.slack.com/...")
    .describe("Send Slack notification")
    .secret("SLACK_SECRET")
    .param("channel", string("Channel"))
    .param("message", string("Message"))
    .build()
)

Internal Tools (Built-in Capabilities)
from inferencesh import internal_tools

config = (
    internal_tools()
    .plan()
    .memory()
    .web_search(True)
    .code_execution(True)
    .image_generation({
        "enabled": True,
        "app_ref": "infsh/flux@latest"
    })
    .build()
)

agent = client.agent({
    "core_app": {"ref": "infsh/claude-sonnet-4@latest"},
    "internal_tools": config
})

Streaming Agent Responses
def handle_message(msg):
    if msg.get("content"):
        print(msg["content"], end="", flush=True)

def handle_tool(call):
    print(f"\n[Tool: {call.name}]")
    result = execute_tool(call.name, call.args)
    agent.submit_tool_result(call.id, result)

response = agent.send_message(
    "Explain quantum computing",
    on_message=handle_message,
    on_tool_call=handle_tool
)

File Attachments
# From file path
with open("image.png", "rb") as f:
    response = agent.send_message(
        "What's in this image?",
        files=[f.read()]
    )

# From base64
response = agent.send_message(
    "Analyze this",
    files=["data:image/png;base64,iVBORw0KGgo..."]
)

Skills (Reusable Context)
agent = client.agent({
    "core_app": {"ref": "infsh/claude-sonnet-4@latest"},
    "skills": [
        {
            "name": "code-review",
            "description": "Code review guidelines",
            "content": "# Code Review\n\n1. Check security\n2. Check performance..."
        },
        {
            "name": "api-docs",
            "description": "API documentation",
            "url": "https://example.com/skills/api-docs.md"
        }
    ]
})

Async Support
from inferencesh import async_inference
import asyncio

async def main():
    client = async_inference(api_key="inf_...")

    # Async app execution
    result = await client.run({
        "app": "infsh/flux-1-dev",
        "input": {"prompt": "A galaxy"}
    })

    # Async agent
    agent = client.agent("my-org/assistant@latest")
    response = await agent.send_message("Hello!")

    # Async streaming
    async for msg in agent.stream_messages():
        print(msg)

asyncio.run(main())

Error Handling
from inferencesh import RequirementsNotMetException

try:
    result = client.run({"app": "my-app", "input": {...}})
except RequirementsNotMetException as e:
    print(f"Missing requirements:")
    for err in e.errors:
        print(f"  - {err['type']}: {err['key']}")
except RuntimeError as e:
    print(f"Error: {e}")

Human Approval Workflows
def handle_tool(call):
    if call.requires_approval:
        # Show to user, get confirmation
        approved = prompt_user(f"Allow {call.name}?")
        if approved:
            result = execute_tool(call.name, call.args)
            agent.submit_tool_result(call.id, result)
        else:
            agent.submit_tool_result(call.id, {"error": "Denied by user"})

response = agent.send_message(
    "Delete all temp files",
    on_tool_call=handle_tool
)

Reference Files
Agent Patterns - Multi-agent, RAG, human-in-the-loop patterns
Tool Builder - Complete tool builder API reference
Streaming - Real-time progress updates and SSE handling
File Handling - Upload, download, and manage files
Sessions - Stateful execution with warm workers
Async Patterns - Parallel processing and async/await
Related Skills
# JavaScript SDK
npx skills add inference-sh/skills@javascript-sdk

# Full platform skill (all 250+ apps via CLI)
npx skills add inference-sh/skills@infsh-cli

# LLM models
npx skills add inference-sh/skills@llm-models

# Image generation
npx skills add inference-sh/skills@ai-image-generation

Documentation
Python SDK Reference - Full API documentation
Agent SDK Overview - Building agents
Tool Builder Reference - Creating tools
Authentication - API key setup
Streaming - Real-time updates
File Uploads - File handling
Weekly Installs
337
Repository
inference-sh/skills
GitHub Stars
395
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn