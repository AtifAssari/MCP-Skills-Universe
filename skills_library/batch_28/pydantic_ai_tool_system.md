---
title: pydantic-ai-tool-system
url: https://skills.sh/existential-birds/beagle/pydantic-ai-tool-system
---

# pydantic-ai-tool-system

skills/existential-birds/beagle/pydantic-ai-tool-system
pydantic-ai-tool-system
Installation
$ npx skills add https://github.com/existential-birds/beagle --skill pydantic-ai-tool-system
SKILL.md
PydanticAI Tool System
Tool Registration

Two decorators based on whether you need context:

from pydantic_ai import Agent, RunContext

agent = Agent('openai:gpt-4o')

# @agent.tool - First param MUST be RunContext
@agent.tool
async def get_user_data(ctx: RunContext[MyDeps], user_id: int) -> str:
    """Get user data from database.

    Args:
        ctx: The run context with dependencies.
        user_id: The user's ID.
    """
    return await ctx.deps.db.get_user(user_id)

# @agent.tool_plain - NO context parameter allowed
@agent.tool_plain
def calculate_total(prices: list[float]) -> float:
    """Calculate total price.

    Args:
        prices: List of prices to sum.
    """
    return sum(prices)

Critical Rules
@agent.tool: First parameter MUST be RunContext[DepsType]
@agent.tool_plain: MUST NOT have RunContext parameter
Docstrings: Required for LLM to understand tool purpose
Google-style docstrings: Used for parameter descriptions
Docstring Formats

Google style (default):

@agent.tool_plain
async def search(query: str, limit: int = 10) -> list[str]:
    """Search for items.

    Args:
        query: The search query.
        limit: Maximum results to return.
    """


Sphinx style:

@agent.tool_plain(docstring_format='sphinx')
async def search(query: str) -> list[str]:
    """Search for items.

    :param query: The search query.
    """

Tool Return Types

Tools can return various types:

# String (direct)
@agent.tool_plain
def get_info() -> str:
    return "Some information"

# Pydantic model (serialized to JSON)
@agent.tool_plain
def get_user() -> User:
    return User(name="John", age=30)

# Dict (serialized to JSON)
@agent.tool_plain
def get_data() -> dict[str, Any]:
    return {"key": "value"}

# ToolReturn for custom content types
from pydantic_ai import ToolReturn, ImageUrl

@agent.tool_plain
def get_image() -> ToolReturn:
    return ToolReturn(content=[ImageUrl(url="https://...")])

Accessing Context

RunContext provides:

@agent.tool
async def my_tool(ctx: RunContext[MyDeps]) -> str:
    # Dependencies
    db = ctx.deps.db
    api = ctx.deps.api_client

    # Model info
    model_name = ctx.model.model_name

    # Usage tracking
    tokens_used = ctx.usage.total_tokens

    # Retry info
    attempt = ctx.retry  # Current retry attempt (0-based)
    max_retries = ctx.max_retries

    # Message history
    messages = ctx.messages

    return "result"

Tool Prepare Functions

Dynamically modify tools per-request:

from pydantic_ai.tools import ToolDefinition

async def prepare_tools(
    ctx: RunContext[MyDeps],
    tool_defs: list[ToolDefinition]
) -> list[ToolDefinition]:
    """Filter or modify tools based on context."""
    if ctx.deps.user_role != 'admin':
        # Hide admin tools from non-admins
        return [t for t in tool_defs if not t.name.startswith('admin_')]
    return tool_defs

agent = Agent('openai:gpt-4o', prepare_tools=prepare_tools)

Toolsets

Group and compose tools:

from pydantic_ai import FunctionToolset, CombinedToolset

# Create a toolset
db_tools = FunctionToolset()

@db_tools.tool
def query_users(name: str) -> list[dict]:
    """Query users by name."""
    ...

@db_tools.tool
def update_user(id: int, data: dict) -> bool:
    """Update user data."""
    ...

# Use in agent
agent = Agent('openai:gpt-4o', toolsets=[db_tools])

# Combine toolsets
all_tools = CombinedToolset([db_tools, api_tools])

Common Mistakes
Wrong: Context in tool_plain
@agent.tool_plain
async def bad_tool(ctx: RunContext[MyDeps]) -> str:  # ERROR!
    ...

Wrong: Missing context in tool
@agent.tool
def bad_tool(user_id: int) -> str:  # ERROR!
    ...

Wrong: Context not first parameter
@agent.tool
def bad_tool(user_id: int, ctx: RunContext[MyDeps]) -> str:  # ERROR!
    ...

Async vs Sync

Both work, but async is preferred for I/O:

# Async (preferred for I/O operations)
@agent.tool
async def fetch_data(ctx: RunContext[Deps]) -> str:
    return await ctx.deps.client.get('/data')

# Sync (fine for CPU-bound operations)
@agent.tool_plain
def compute(x: int, y: int) -> int:
    return x * y

Weekly Installs
141
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