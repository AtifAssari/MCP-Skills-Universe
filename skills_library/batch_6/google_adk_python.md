---
title: google-adk-python
url: https://skills.sh/cnemri/google-genai-skills/google-adk-python
---

# google-adk-python

skills/cnemri/google-genai-skills/google-adk-python
google-adk-python
Installation
$ npx skills add https://github.com/cnemri/google-genai-skills --skill google-adk-python
SKILL.md
Google ADK (Python) Skill

This skill provides comprehensive documentation and Python examples for the Google Agent Development Kit (ADK). It maps documentation topics to their corresponding Python code snippets.

How to Use

Identify the user's specific interest or task and refer to the relevant reference file below. Each reference file contains links to the official documentation (Markdown) and the corresponding Python examples (raw code).

Topics
1. Getting Started

For installation, quickstarts, and basic agent setup.

Reference: references/get-started.md
2. Agents & Models

For creating different types of agents (LLM, Workflow, Loop, Parallel, Sequential) and configuring specific models (Gemini, Anthropic, etc.).

Agents Reference: references/agents.md
Models Reference: references/models.md
3. Tools (Basic & Advanced)

For integrating tools like Google Search, Code Execution, BigQuery, third-party services (GitHub, Jira, etc.), MCP, and Grounding.

Basic Tools Reference: references/tools.md
Advanced Tools Reference: references/advanced-tools.md
4. Streaming

For building real-time, low-latency streaming agents (audio/video).

Reference: references/streaming.md
5. Callbacks

For hooking into agent lifecycle events (before/after agent, model, tool execution).

Reference: references/callbacks.md
6. Runtime & Architecture

For deep dives into the Runtime, Sessions, Memory, Context, Events, Artifacts, and Plugins.

Reference: references/runtime-arch.md
7. Deployment & Operations

For deploying agents (Cloud Run, GKE) and observability (Logging, Tracing, Evaluation).

Reference: references/deploy-ops.md
8. Tutorials & Samples

For end-to-end tutorials and complete agent samples (e.g., YouTube Shorts Assistant, Weather Agent).

Reference: references/tutorials.md
9. API Reference

For REST API details.

Reference: references/api.md
10. General Information

For project info, community, release notes, and limitations.

Reference: references/general.md
Instructions
When a user asks about a specific topic, load the corresponding reference file to get the URLs for the documentation and code.
You can read the content of the linked files using web_fetch or run_shell_command with curl if you need to provide the actual content to the user.
Always prefer providing the Python example code when explaining a concept.
Weekly Installs
269
Repository
cnemri/google-g…i-skills
GitHub Stars
119
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn