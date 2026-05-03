---
rating: ⭐⭐⭐
title: google-agents-cli-adk-code
url: https://skills.sh/google/agents-cli/google-agents-cli-adk-code
---

# google-agents-cli-adk-code

skills/google/agents-cli/google-agents-cli-adk-code
google-agents-cli-adk-code
Installation
$ npx skills add https://github.com/google/agents-cli --skill google-agents-cli-adk-code
SKILL.md
ADK Cheatsheet

Before using this skill, activate /google-agents-cli-workflow first — it contains the required development phases and scaffolding steps.

Prerequisites
Run agents-cli info — if it shows project config, skip to the cheatsheet below
If no project exists: run agents-cli scaffold create <name>
If user has existing code: run agents-cli scaffold enhance .

Do NOT write agent code until a project is scaffolded.

Python only for now. This cheatsheet currently covers the Python ADK SDK. Support for other languages is coming soon.

Quick Reference — Most Common Patterns
Agent Creation
from google.adk.agents import Agent

root_agent = Agent(
    name="my_agent",
    model="gemini-flash-latest",
    instruction="You are a helpful assistant that ...",
    tools=[my_tool],
)


NEVER change an existing agent's model= value unless the user explicitly asks. If a Gemini model returns a 404, it's almost always a GOOGLE_CLOUD_LOCATION issue — run the listing command to verify availability before changing anything. For model docs, fetch https://adk.dev/agents/models/google-gemini/index.md.

uv run --with google-genai python -c "
from google import genai
client = genai.Client(vertexai=True, location='global')
for m in client.models.list(): print(m.name)
"

Basic Tool
from google.adk.tools import FunctionTool

def get_weather(city: str) -> dict:
    """Get current weather for a city."""
    return {"city": city, "temp": "22°C", "condition": "sunny"}

weather_tool = FunctionTool(func=get_weather)


ADK built-in tool imports: Import the tool instance, not the module.

from google.adk.tools.load_web_page import load_web_page  # CORRECT
from google.adk.tools import load_web_page                 # WRONG

Simple Callback
from google.adk.agents.callback_context import CallbackContext

async def initialize_state(callback_context: CallbackContext) -> None:
    state = callback_context.state
    if "history" not in state:
        state["history"] = []

root_agent = Agent(
    name="my_agent",
    model="gemini-flash-latest",
    instruction="...",
    before_agent_callback=initialize_state,
)

Reference Files
File	When to read
references/adk-python.md	ADK Python API — agents, tools, callbacks, plugins, state, artifacts, context caching, session rewind
references/adk-2.0.md	ADK 2.0 Workflow API (experimental pre-GA, opt-in) — graph-based workflows, nodes, edges, HITL, parallel processing
ADK 2.0 Workflows — Opt-in

The Workflow API is experimental, pre-GA (ADK 2.0). Do NOT recommend it by default.

Before suggesting workflow patterns, explain the following to the user and ask if they want to proceed:

What it is: ADK 2.0 introduces a graph-based Workflow API — nodes (functions, LLM agents, tools) connected by edges with conditional routing, fan-out/fan-in parallelism, and human-in-the-loop interrupts.
When it helps: Complex multi-step pipelines needing deterministic control flow, parallel processing of list items, structured approval gates, or retry logic — cases where SequentialAgent/ParallelAgent/LoopAgent feel limiting.
Risks: Pre-GA — APIs may change before GA. Requires google-adk >= 2.0.0 and Python >= 3.11. Incompatible with Live Streaming. Scaffolded projects need pyproject.toml changes before upgrade — see the reference file for step-by-step instructions.

Only read references/adk-2.0.md after the user explicitly opts in. If they decline or are unsure, use the standard ADK 1.x orchestration patterns from references/adk-python.md (SequentialAgent, ParallelAgent, LoopAgent, BaseAgent).

ADK Documentation

For the ADK docs index (titles and URLs for fetching documentation pages), use curl https://adk.dev/llms.txt.

Related Skills
/google-agents-cli-workflow — Development workflow, coding guidelines, and operational rules
/google-agents-cli-scaffold — Project creation and enhancement with agents-cli scaffold create / scaffold enhance
/google-agents-cli-eval — Evaluation methodology, evalset schema, and the eval-fix loop
/google-agents-cli-deploy — Deployment targets, CI/CD pipelines, and production workflows
Weekly Installs
3.5K
Repository
google/agents-cli
GitHub Stars
1.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn