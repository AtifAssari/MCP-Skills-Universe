---
title: mcp-skill
url: https://skills.sh/manojbajaj95/mcp-skill/mcp-skill
---

# mcp-skill

skills/manojbajaj95/mcp-skill/mcp-skill
mcp-skill
Installation
$ npx skills add https://github.com/manojbajaj95/mcp-skill --skill mcp-skill
SKILL.md
mcp-skill

Use this skill when you need to work with the mcp-skill CLI or use a generated MCP-backed app from Python.

What It Does

This skill helps with:

Creating a new generated app wrapper from an MCP server
Listing generated apps available locally
Listing functions for a specific generated app
Inspecting a function before calling it
Using the generated app from async Python
Dependencies

CLI usage depends on:

uv
mcp-skill

Python usage depends on:

mcp-skill
Core Commands
# Create a new generated app wrapper
uvx mcp-skill create --url https://example.com/mcp --name example --non-interactive

# List generated apps
uvx mcp-skill list-apps

# List functions for one app
uvx mcp-skill list-functions notion

# Inspect one function
uvx mcp-skill inspect notion notion_search

Example

Find a generated app, inspect the function you need, then call it from async Python:

import asyncio
from sentry.app import SentryApp


async def main():
    sentry = SentryApp()
    user = await sentry.whoami()
    print(user)


asyncio.run(main())

Async Usage Notes
Generated app methods are async and should be called with await.
Use them inside async def, then run that function with asyncio.run(...) in a normal script.
If you skip await, you will get a coroutine object instead of the real result.
Be careful in environments that already manage an event loop.
Recommended Workflow
Run uvx mcp-skill list-apps to find the generated app name.
Run uvx mcp-skill list-functions <app> to see available functions.
Run uvx mcp-skill inspect <app> <function> to confirm the exact signature and docstring.
Import the app class from <app>.app and call the async method you found.
Weekly Installs
12
Repository
manojbajaj95/mcp-skill
GitHub Stars
6
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn