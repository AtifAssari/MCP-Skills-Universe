---
title: openai-docs
url: https://skills.sh/boshu2/agentops/openai-docs
---

# openai-docs

skills/boshu2/agentops/openai-docs
openai-docs
Originally fromopenai/skills
Installation
$ npx skills add https://github.com/boshu2/agentops --skill openai-docs
SKILL.md
OpenAI Docs

Provide authoritative, current guidance from OpenAI developer docs using the developers.openai.com MCP server. Always prioritize the developer docs MCP tools over web.run for OpenAI-related questions. Only if the MCP server is installed and returns no meaningful results should you fall back to web search.

Quick start
Use mcp__openaiDeveloperDocs__search_openai_docs to find the most relevant doc pages.
Use mcp__openaiDeveloperDocs__fetch_openai_doc to pull exact sections and quote/paraphrase accurately.
Use mcp__openaiDeveloperDocs__list_openai_docs only when you need to browse or discover pages without a clear query.
OpenAI product snapshots
Apps SDK: Build ChatGPT apps by providing a web component UI and an MCP server that exposes your app's tools to ChatGPT.
Responses API: A unified endpoint designed for stateful, multimodal, tool-using interactions in agentic workflows.
Chat Completions API: Generate a model response from a list of messages comprising a conversation.
Codex: OpenAI's coding agent for software development that can write, understand, review, and debug code.
gpt-oss: Open-weight OpenAI reasoning models (gpt-oss-120b and gpt-oss-20b) released under the Apache 2.0 license.
Realtime API: Build low-latency, multimodal experiences including natural speech-to-speech conversations.
Agents SDK: A toolkit for building agentic apps where a model can use tools and context, hand off to other agents, stream partial results, and keep a full trace.
If MCP server is missing

If MCP tools fail or no OpenAI docs resources are available:

In Codex:

Run: codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
If it fails due to permissions/sandboxing, retry with escalated permissions.
Ask the user to restart Codex, then re-run doc search/fetch.

In Claude Code:

Add the MCP server to ~/.claude/settings.json under "mcpServers":
{
  "mcpServers": {
    "openaiDeveloperDocs": {
      "type": "url",
      "url": "https://developers.openai.com/mcp"
    }
  }
}

Restart Claude Code, then re-run doc search/fetch.

In other agents: Ask the user to configure the MCP server per their agent's documentation.

Workflow
Clarify the product scope (Codex, OpenAI API, or ChatGPT Apps SDK) and the task.
Search docs with a precise query.
Fetch the best page and the specific section needed (use anchor when possible).
Answer with concise guidance and cite the doc source.
Provide code snippets only when the docs support them.
Quality rules
Treat OpenAI docs as the source of truth; avoid speculation.
Keep quotes short and within policy limits; prefer paraphrase with citations.
If multiple pages differ, call out the difference and cite both.
If docs do not cover the user’s need, say so and offer next steps.
Tooling notes
Always use MCP doc tools before any web search for OpenAI-related questions.
If the MCP server is installed but returns no meaningful results, then use web search as a fallback.
When falling back to web search, restrict to official OpenAI domains (developers.openai.com, platform.openai.com) and cite sources.
Examples
OpenAI API Guidance

User says: "How do I use tool calls with the Responses API?"

What happens:

Search OpenAI docs MCP for "Responses API tools".
Fetch the most relevant section.
Return implementation guidance with citations.
Codex Capability Check

User says: "Does Codex support read-only review workflows?"

What happens:

Query Codex docs via MCP.
Fetch flag/sandbox references.
Answer with source-backed guidance and constraints.
Troubleshooting
Problem	Cause	Solution
MCP docs search returns nothing	MCP server not installed	Install openaiDeveloperDocs MCP, restart Codex, retry search
Results are stale/unclear	Query too broad	Narrow query by product + feature, then fetch exact page section
Need citation-ready answer	Source not fetched	Fetch specific doc section before answering
Docs do not cover question	Gap in official docs	State gap explicitly and provide safe best-effort guidance
Weekly Installs
398
Repository
boshu2/agentops
GitHub Stars
323
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn