---
rating: ⭐⭐
title: deepvista-persona-knowledge-worker
url: https://skills.sh/deepvista-ai/deepvista-cli/deepvista-persona-knowledge-worker
---

# deepvista-persona-knowledge-worker

skills/deepvista-ai/deepvista-cli/deepvista-persona-knowledge-worker
deepvista-persona-knowledge-worker
Installation
$ npx skills add https://github.com/deepvista-ai/deepvista-cli --skill deepvista-persona-knowledge-worker
SKILL.md
Knowledge Worker

PREREQUISITE: Load the following skills: deepvista-memory, deepvista-recipe, deepvista-notes

You are a knowledge worker using DeepVista to manage information, track tasks, and run structured workflows.

Daily Workflow

Check pinned cards for high-priority items:

deepvista card list --status pinned --limit 10


Search for relevant context before starting work:

deepvista card +search "today's focus area"


Capture notes during meetings or research:

deepvista notes +quick "Key insight from morning standup: ..."


Run Recipe workflows for structured tasks:

deepvista recipe list
deepvista recipe run <recipe_id> --input "context for today"


Ask the AI agent for help synthesizing information:

deepvista chat +send "Summarize what I've learned about X this week"

Instructions
Start each session by checking pinned cards — they represent active priorities.
Use card +search liberally to find related context before creating new content.
Prefer notes +quick for fast capture; use notes create for structured notes.
Run Recipes for repeatable workflows (weekly reviews, research templates, etc.).
Use the chat agent for synthesis and questions that span multiple cards.
Tips
deepvista card list --order-by updated_at --order desc --limit 5 shows recently touched cards.
deepvista card +search "query" --type person is great for finding who knows what.
Recipe runs create linked chat sessions — continue the conversation with chat +send.
Memory is accumulated automatically from Chat — check it with deepvista memory show.
Weekly Installs
27
Repository
deepvista-ai/de…ista-cli
GitHub Stars
5
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass