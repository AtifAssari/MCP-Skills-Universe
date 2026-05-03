---
title: pydanticai-docs
url: https://skills.sh/dougtrajano/pydantic-ai-skills/pydanticai-docs
---

# pydanticai-docs

skills/dougtrajano/pydantic-ai-skills/pydanticai-docs
pydanticai-docs
Installation
$ npx skills add https://github.com/dougtrajano/pydantic-ai-skills --skill pydanticai-docs
SKILL.md
Pydantic AI Documentation Skill
What is Pydantic AI?

Pydantic AI is a production-grade Python agent framework for building type-safe, dependency-injected Generative AI applications. It supports multiple LLM providers, structured outputs via Pydantic models, and composable multi-agent patterns.

Doc: https://ai.pydantic.dev/index.md

Core Concepts
1. Agent Instantiation
from pydantic_ai import Agent

agent = Agent(
    'openai:gpt-4o',          # model string: provider:model-name
    system_prompt='Be helpful.',
)
result = agent.run_sync('What is the capital of France?')
print(result.output)


For full constructor parameters, run methods, and streaming: load references/AGENT.md.

2. Function Tools (@agent.tool)
from pydantic_ai import Agent, RunContext

agent = Agent('openai:gpt-4o', deps_type=str)

@agent.tool
def get_user_name(ctx: RunContext[str]) -> str:
    """Return the current user's name."""
    return ctx.deps

result = agent.run_sync('What is my name?', deps='Alice')


Use @agent.tool_plain when you don't need RunContext. For tool registration, return types, and retries: load references/FUNCTION_TOOLS.md.

3. Dependency Injection (RunContext)
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext

@dataclass
class MyDeps:
    api_key: str
    user_id: int

agent = Agent('openai:gpt-4o', deps_type=MyDeps)

@agent.tool
async def fetch_data(ctx: RunContext[MyDeps]) -> str:
    return f'User {ctx.deps.user_id}'


For RunContext fields, injection into system prompts and output validators: load references/DEPENDENCIES.md.

4. Structured Output
from pydantic import BaseModel
from pydantic_ai import Agent

class CityInfo(BaseModel):
    city: str
    country: str

agent = Agent('openai:gpt-4o', output_type=CityInfo)
result = agent.run_sync('Where were the 2012 Olympics held?')
print(result.output)  # CityInfo(city='London', country='United Kingdom')


For union types, plain scalars, output_validator, and partial validation: load references/OUTPUT.md.

Additional Topics

For these topics, load the named reference file or follow the doc link — no implementation code is provided here.

Topic	Reference file	Doc link
Message history / multi-turn conversations	references/MESSAGES.md	https://ai.pydantic.dev/message-history/index.md
Model / provider setup (all providers)	references/MODELS.md	https://ai.pydantic.dev/models/overview/index.md
Toolsets (FunctionToolset, composition)	references/TOOLS_AND_TOOLSETS.md	https://ai.pydantic.dev/toolsets/index.md
MCP server integration	references/MCP.md	https://ai.pydantic.dev/mcp/client/index.md
Multi-agent applications	doc link only	https://ai.pydantic.dev/multi-agent-applications/index.md
Graphs (pydantic-graph)	doc link only	https://ai.pydantic.dev/graph/index.md
Evals (pydantic-evals)	doc link only	https://ai.pydantic.dev/evals/index.md
Durable execution	doc link only	https://ai.pydantic.dev/durable_execution/overview/index.md
Retries	doc link only	https://ai.pydantic.dev/retries/index.md
Testing (TestModel, override)	doc link only	https://ai.pydantic.dev/testing/index.md
Logfire integration	doc link only	https://ai.pydantic.dev/logfire/index.md
Builtin tools	doc link only	https://ai.pydantic.dev/builtin-tools/index.md
Streaming	doc link only	https://ai.pydantic.dev/agent/index.md
Agent Behavior Rules
Default to this file — answer from core concepts first; load only the specific references/<CONCEPT>.md relevant to the user's question when more depth is needed.
Never fabricate API details — always end with "For details, see: <URL>" using a link from the official index above.
No implementation code for non-core topics — return a doc link only for topics listed in the Additional Topics table.
Prefer specificity — route to the most specific page (e.g., models/anthropic/index.md) when the user's question targets a specific provider, not the overview.
Out of scope — do not debug user code passively, do not generate full production agent implementations, do not answer questions unrelated to the Pydantic AI ecosystem.
Weekly Installs
86
Repository
dougtrajano/pyd…i-skills
GitHub Stars
260
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn