---
title: clickup
url: https://skills.sh/manojbajaj95/mcp-skill/clickup
---

# clickup

skills/manojbajaj95/mcp-skill/clickup
clickup
Installation
$ npx skills add https://github.com/manojbajaj95/mcp-skill --skill clickup
SKILL.md
clickup

Use this skill when you need to work with clickup through its generated async Python app, call its MCP-backed functions from code, or inspect available functions with the mcp-skill CLI.

Authentication

This app can use the MCP client's built-in OAuth flow when the server requires it. In most cases, the default constructor is enough. Tokens are persisted to ~/.mcp-skill/auth/ so subsequent runs reuse the same credentials automatically.

app = ClickupApp()


If you need a custom OAuth provider, pass it via the auth argument:

app = ClickupApp(auth=my_oauth_provider)

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
from clickup.app import ClickupApp


async def main():
    app = ClickupApp()
    result = await app.clickup_search(keywords="example", sort="value", filters="value")
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
uvx mcp-skill list-functions clickup
uvx mcp-skill inspect clickup clickup_search


Important: Add .agents/skills to your Python path so imports resolve correctly:

import sys
sys.path.insert(0, ".agents/skills")
from clickup.app import ClickupApp


Or set the PYTHONPATH environment variable:

export PYTHONPATH=".agents/skills:$PYTHONPATH"


Preferred: use uv run (handles dependencies automatically):

PYTHONPATH=.agents/skills uv run --with mcp-skill python -c "
import asyncio
from clickup.app import ClickupApp

async def main():
    app = ClickupApp()
    result = await app.clickup_search(keywords="example", sort="value", filters="value")
    print(result)

asyncio.run(main())
"


Alternative: use python directly (install dependencies first):

pip install mcp-skill
PYTHONPATH=.agents/skills python -c "
import asyncio
from clickup.app import ClickupApp

async def main():
    app = ClickupApp()
    result = await app.clickup_search(keywords="example", sort="value", filters="value")
    print(result)

asyncio.run(main())
"

Weekly Installs
16
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