---
rating: ⭐⭐
title: canva
url: https://skills.sh/manojbajaj95/mcp-skill/canva
---

# canva

skills/manojbajaj95/mcp-skill/canva
canva
Installation
$ npx skills add https://github.com/manojbajaj95/mcp-skill --skill canva
SKILL.md
canva

Use this skill when you need to work with canva through its generated async Python app, call its MCP-backed functions from code, or inspect available functions with the mcp-skill CLI.

Authentication

This app can use the MCP client's built-in OAuth flow when the server requires it. In most cases, the default constructor is enough. Tokens are persisted to ~/.mcp-skill/auth/ so subsequent runs reuse the same credentials automatically.

app = CanvaApp()


If you need a custom OAuth provider, pass it via the auth argument:

app = CanvaApp(auth=my_oauth_provider)

Dependencies

This skill requires the following Python packages:

mcp-skill

Install with uv:

uv pip install mcp-skill


Or with pip:

pip install mcp-skill

Python Usage

Use the generated app directly in async Python code:

import asyncio
from canva.app import CanvaApp


async def main():
    app = CanvaApp()
    result = await app.upload_asset_from_url(url="example", name="example", user_intent="example")
    print(result)


asyncio.run(main())

Async Usage Notes
Every generated tool method is async, so call it with await.
Use these apps inside an async function, then run that function with asyncio.run(...) if you are in a script.
If you forget await, you will get a coroutine object instead of the actual tool result.
Be careful when mixing this with other event-loop environments such as notebooks, web servers, or async frameworks.
Discover Functions with the CLI

Use the CLI to find available apps, list functions on an app, and inspect a function before calling it:

uvx mcp-skill list-apps
uvx mcp-skill list-functions canva
uvx mcp-skill inspect canva upload_asset_from_url


Important: Add .agents/skills to your Python path so imports resolve correctly:

import sys
sys.path.insert(0, ".agents/skills")
from canva.app import CanvaApp


Or set the PYTHONPATH environment variable:

export PYTHONPATH=".agents/skills:$PYTHONPATH"


Preferred: use uv run (handles dependencies automatically):

PYTHONPATH=.agents/skills uv run --with mcp-skill python -c "
import asyncio
from canva.app import CanvaApp

async def main():
    app = CanvaApp()
    result = await app.upload_asset_from_url(url="example", name="example", user_intent="example")
    print(result)

asyncio.run(main())
"


Alternative: use python directly (install dependencies first):

pip install mcp-skill
PYTHONPATH=.agents/skills python -c "
import asyncio
from canva.app import CanvaApp

async def main():
    app = CanvaApp()
    result = await app.upload_asset_from_url(url="example", name="example", user_intent="example")
    print(result)

asyncio.run(main())
"

Weekly Installs
11
Repository
manojbajaj95/mcp-skill
GitHub Stars
6
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn