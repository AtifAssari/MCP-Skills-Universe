---
title: pubmed
url: https://skills.sh/manojbajaj95/mcp-skill/pubmed
---

# pubmed

skills/manojbajaj95/mcp-skill/pubmed
pubmed
Installation
$ npx skills add https://github.com/manojbajaj95/mcp-skill --skill pubmed
SKILL.md
pubmed

Use this skill when you need to work with pubmed through its generated async Python app, call its MCP-backed functions from code, or inspect available functions with the mcp-skill CLI.

Authentication

No authentication required.

app = PubmedApp()


Passing an auth argument is accepted but has no effect and will emit a warning.

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
from pubmed.app import PubmedApp


async def main():
    app = PubmedApp()
    result = await app.search_articles(query="example", max_results=1, sort="example")
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
uvx mcp-skill list-functions pubmed
uvx mcp-skill inspect pubmed search_articles


Important: Add .agents/skills to your Python path so imports resolve correctly:

import sys
sys.path.insert(0, ".agents/skills")
from pubmed.app import PubmedApp


Or set the PYTHONPATH environment variable:

export PYTHONPATH=".agents/skills:$PYTHONPATH"


Preferred: use uv run (handles dependencies automatically):

PYTHONPATH=.agents/skills uv run --with mcp-skill python -c "
import asyncio
from pubmed.app import PubmedApp

async def main():
    app = PubmedApp()
    result = await app.search_articles(query="example", max_results=1, sort="example")
    print(result)

asyncio.run(main())
"


Alternative: use python directly (install dependencies first):

pip install mcp-skill
PYTHONPATH=.agents/skills python -c "
import asyncio
from pubmed.app import PubmedApp

async def main():
    app = PubmedApp()
    result = await app.search_articles(query="example", max_results=1, sort="example")
    print(result)

asyncio.run(main())
"

Weekly Installs
13
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