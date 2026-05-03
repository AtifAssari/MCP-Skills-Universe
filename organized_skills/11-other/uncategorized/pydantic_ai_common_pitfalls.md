---
rating: ⭐⭐⭐
title: pydantic-ai-common-pitfalls
url: https://skills.sh/existential-birds/beagle/pydantic-ai-common-pitfalls
---

# pydantic-ai-common-pitfalls

skills/existential-birds/beagle/pydantic-ai-common-pitfalls
pydantic-ai-common-pitfalls
Installation
$ npx skills add https://github.com/existential-birds/beagle --skill pydantic-ai-common-pitfalls
SKILL.md
PydanticAI Common Pitfalls and Debugging
Tool Decorator Errors
Wrong: RunContext in tool_plain
# ERROR: RunContext not allowed in tool_plain
@agent.tool_plain
async def bad_tool(ctx: RunContext[MyDeps]) -> str:
    return "oops"
# UserError: RunContext annotations can only be used with tools that take context


Fix: Use @agent.tool if you need context:

@agent.tool
async def good_tool(ctx: RunContext[MyDeps]) -> str:
    return "works"

Wrong: Missing RunContext in tool
# ERROR: First param must be RunContext
@agent.tool
def bad_tool(user_id: int) -> str:
    return "oops"
# UserError: First parameter of tools that take context must be annotated with RunContext[...]


Fix: Add RunContext as first parameter:

@agent.tool
def good_tool(ctx: RunContext[MyDeps], user_id: int) -> str:
    return "works"

Wrong: RunContext not first
# ERROR: RunContext must be first parameter
@agent.tool
def bad_tool(user_id: int, ctx: RunContext[MyDeps]) -> str:
    return "oops"


Fix: RunContext must always be the first parameter.

Valid Patterns (Not Errors)
Raw Function Tool Registration

The following pattern IS valid and supported by pydantic-ai:

from pydantic_ai import Agent, RunContext

async def search_db(ctx: RunContext[MyDeps], query: str) -> list[dict]:
    """Search the database."""
    return await ctx.deps.db.search(query)

async def get_user(ctx: RunContext[MyDeps], user_id: int) -> dict:
    """Get user by ID."""
    return await ctx.deps.db.get_user(user_id)

# Valid: Pass raw functions to Agent(tools=[...])
agent = Agent(
    'openai:gpt-4o',
    deps_type=MyDeps,
    tools=[search_db, get_user]  # RunContext detected from signature
)


Why this works: PydanticAI inspects function signatures. If the first parameter is RunContext[T], it's treated as a context-aware tool. No decorator required.

Reference: https://ai.pydantic.dev/agents/#registering-tools-via-the-tools-argument

Do NOT flag code that passes functions with RunContext signatures to Agent(tools=[...]). This is equivalent to using @agent.tool and is explicitly documented.

Dependency Type Mismatches
Wrong: Missing deps at runtime
agent = Agent('openai:gpt-4o', deps_type=MyDeps)

# ERROR: deps required but not provided
result = agent.run_sync('Hello')  # Missing deps!


Fix: Always provide deps when deps_type is set:

result = agent.run_sync('Hello', deps=MyDeps(...))

Wrong: Wrong deps type
@dataclass
class AppDeps:
    db: Database

@dataclass
class WrongDeps:
    api: ApiClient

agent = Agent('openai:gpt-4o', deps_type=AppDeps)

# Type error: WrongDeps != AppDeps
result = agent.run_sync('Hello', deps=WrongDeps(...))

Output Type Issues
Pydantic validation fails
class Response(BaseModel):
    count: int
    items: list[str]

agent = Agent('openai:gpt-4o', output_type=Response)
result = agent.run_sync('List items')
# May fail if LLM returns wrong structure


Fix: Increase retries or improve prompt:

agent = Agent(
    'openai:gpt-4o',
    output_type=Response,
    retries=3,  # More attempts
    instructions='Return JSON with count (int) and items (list of strings).'
)

Complex nested types
# May cause schema issues with some models
class Complex(BaseModel):
    nested: dict[str, list[tuple[int, str]]]


Fix: Simplify or use intermediate models:

class Item(BaseModel):
    id: int
    name: str

class Simple(BaseModel):
    items: list[Item]

Async vs Sync Mistakes
Wrong: Calling async in sync context
# ERROR: Can't await in sync function
def handler():
    result = await agent.run('Hello')  # SyntaxError!


Fix: Use run_sync or make handler async:

def handler():
    result = agent.run_sync('Hello')

# Or
async def handler():
    result = await agent.run('Hello')

Wrong: Blocking in async tools
@agent.tool
async def slow_tool(ctx: RunContext[Deps]) -> str:
    time.sleep(5)  # WRONG: Blocks event loop!
    return "done"


Fix: Use async I/O:

@agent.tool
async def slow_tool(ctx: RunContext[Deps]) -> str:
    await asyncio.sleep(5)  # Correct
    return "done"

Model Configuration Errors
Missing API key
# ERROR: OPENAI_API_KEY not set
agent = Agent('openai:gpt-4o')
result = agent.run_sync('Hello')
# ModelAPIError: Authentication failed


Fix: Set environment variable or use defer_model_check:

# For testing
agent = Agent('openai:gpt-4o', defer_model_check=True)
with agent.override(model=TestModel()):
    result = agent.run_sync('Hello')

Invalid model string
# ERROR: Unknown provider
agent = Agent('unknown:model')
# ValueError: Unknown model provider


Fix: Use valid provider:model format.

Streaming Issues
Wrong: Using result before stream completes
async with agent.run_stream('Hello') as response:
    # DON'T access .output before streaming completes
    print(response.output)  # May be incomplete!

# Correct: access after context manager
print(response.output)  # Complete result

Wrong: Not iterating stream
async with agent.run_stream('Hello') as response:
    pass  # Never consumed!

# Stream was never read - output may be incomplete


Fix: Always consume the stream:

async with agent.run_stream('Hello') as response:
    async for chunk in response.stream_output():
        print(chunk, end='')

Tool Return Issues
Wrong: Returning non-serializable
@agent.tool_plain
def bad_return() -> object:
    return CustomObject()  # Can't serialize!


Fix: Return serializable types (str, dict, Pydantic model):

@agent.tool_plain
def good_return() -> dict:
    return {"key": "value"}

Debugging Tips
Enable tracing
import logfire
logfire.configure()
logfire.instrument_pydantic_ai()

# Or per-agent
agent = Agent('openai:gpt-4o', instrument=True)

Capture messages
from pydantic_ai import capture_run_messages

with capture_run_messages() as messages:
    result = agent.run_sync('Hello')

for msg in messages:
    print(type(msg).__name__, msg)

Check model responses
result = agent.run_sync('Hello')
print(result.all_messages())  # Full message history
print(result.response)  # Last model response
print(result.usage())  # Token usage

Common Error Messages
Error	Cause	Fix
First parameter... RunContext	@agent.tool missing ctx	Add ctx: RunContext[...]
RunContext... only... context	@agent.tool_plain has ctx	Remove ctx or use @agent.tool
Unknown model provider	Invalid model string	Use valid provider:model
ModelAPIError	API auth/quota	Check API key, limits
RetryPromptPart in messages	Validation failed	Check output_type, increase retries
Weekly Installs
198
Repository
existential-birds/beagle
GitHub Stars
56
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass