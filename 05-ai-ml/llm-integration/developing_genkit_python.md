---
rating: ⭐⭐
title: developing-genkit-python
url: https://skills.sh/firebase/agent-skills/developing-genkit-python
---

# developing-genkit-python

skills/firebase/agent-skills/developing-genkit-python
developing-genkit-python
Installation
$ npx skills add https://github.com/firebase/agent-skills --skill developing-genkit-python
SKILL.md
Genkit Python
Prerequisites
Runtime: Python 3.14+, uv for deps (install).
CLI: genkit --version — install via npm install -g genkit-cli if missing.

New projects: Setup (bootstrap + env). Patterns and code samples: Examples.

Hello World
from genkit import Genkit
from genkit.plugins.google_genai import GoogleAI

ai = Genkit(
    plugins=[GoogleAI()],
    model='googleai/gemini-flash-latest',
)

async def main():
    response = await ai.generate(prompt='Tell me a joke about Python.')
    print(response.text)

if __name__ == '__main__':
    ai.run_main(main())

Critical: Do Not Trust Internal Knowledge

The Python SDK changes often — verify imports and APIs against the references here or upstream docs. On any error, read Common Errors first.

Development Workflow
Default provider: Google AI (GoogleAI()), GEMINI_API_KEY in the environment.
Model IDs: always prefixed, e.g. googleai/gemini-flash-latest (always-on-latest Flash alias; same pattern as other skills).
Entrypoint: ai.run_main(main()) for Genkit-driven apps (not asyncio.run() for long-lived servers started with genkit start — see Common Errors).
After generating code, follow Dev Workflow for genkit start and the Dev UI.
On errors: step 1 is always Common Errors.
References
Examples: Structured output, streaming, flows, tools, embeddings.
Setup: New project bootstrap and plugins.
Common Errors: Read first when something breaks.
FastAPI: HTTP, genkit_fastapi_handler, parallel flows.
Dotprompt: .prompt files and helpers.
Evals: Evaluators and datasets.
Dev Workflow: genkit start, Dev UI, checklist.
Weekly Installs
9.2K
Repository
firebase/agent-skills
GitHub Stars
264
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass