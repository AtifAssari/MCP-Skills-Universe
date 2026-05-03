---
title: openai-docs
url: https://skills.sh/openai/skills/openai-docs
---

# openai-docs

skills/openai/skills/openai-docs
openai-docs
Installation
$ npx skills add https://github.com/openai/skills --skill openai-docs
Summary

Access current OpenAI developer documentation with MCP tools and model-selection guidance.

Prioritizes the OpenAI Developer Docs MCP server for all queries; falls back to web search only on official OpenAI domains if MCP returns no results
Includes reference files for model selection, GPT-5.4 upgrade planning, and prompting guidance; always verifies recommendations against live docs before answering
Covers seven core OpenAI products: Apps SDK, Responses API, Chat Completions, Codex, gpt-oss, Realtime API, and Agents SDK
Handles MCP server installation and escalation if tools are unavailable, with clear workflow for clarifying product scope and upgrade needs
SKILL.md
OpenAI Docs

Provide authoritative, current guidance from OpenAI developer docs using the developers.openai.com MCP server. Always prioritize the developer docs MCP tools over web.run for OpenAI-related questions. This skill also owns model selection, API model migration, and prompt-upgrade guidance. Only if the MCP server is installed and returns no meaningful results should you fall back to web search.

Quick start
Use mcp__openaiDeveloperDocs__search_openai_docs to find the most relevant doc pages.
Use mcp__openaiDeveloperDocs__fetch_openai_doc to pull exact sections and quote/paraphrase accurately.
Use mcp__openaiDeveloperDocs__list_openai_docs only when you need to browse or discover pages without a clear query.
For model-selection, "latest model", or default-model questions, fetch https://developers.openai.com/api/docs/guides/latest-model.md first. If that is unavailable, load references/latest-model.md.
For model upgrades or prompt upgrades, run node scripts/resolve-latest-model-info.js only when the target is latest/current/default or otherwise unspecified; otherwise preserve the explicitly requested target.
Preserve explicit target requests: if the user names a target model like "migrate to GPT-5.4", keep that requested target even if latest-model.md names a newer model. Mention newer guidance only as optional.
If current remote guidance is needed, fetch both the returned migration and prompting guide URLs directly. If direct fetch fails, use MCP/search fallback; if that also fails, use bundled fallback references and disclose the fallback.
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

Run the install command yourself: codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
If it fails due to permissions/sandboxing, immediately retry the same command with escalated permissions and include a 1-sentence justification for approval. Do not ask the user to run it yet.
Only if the escalated attempt fails, ask the user to run the install command.
Ask the user to restart Codex.
Re-run the doc search/fetch after restart.
Workflow
Clarify whether the request is general docs lookup, model selection, a model-string upgrade, prompt-upgrade guidance, or broader API/provider migration.
For model-selection or upgrade requests, prefer current remote docs over bundled references when the user asks for latest/current/default guidance.
Fetch https://developers.openai.com/api/docs/guides/latest-model.md.
Find the latest model ID and explicit migration or prompt-guidance links.
Prefer explicit links from the latest-model page over derived URLs.
For explicit named-model requests, preserve the requested model target and do not silently retarget to the latest model. Mention newer remote guidance only as optional.
For dynamic latest/current/default upgrades, run node scripts/resolve-latest-model-info.js, then fetch both returned guide URLs directly when possible.
If direct guide fetch fails, use the developer-docs MCP tools or official OpenAI-domain search to find the same guide content.
If remote docs are unavailable, use bundled fallback references and say that fallback guidance was used.
For model upgrades, keep changes narrow: update active OpenAI API model defaults and directly related prompts only when safe.
Leave historical docs, examples, eval baselines, fixtures, provider comparisons, provider registries, pricing tables, alias defaults, low-cost fallback paths, and ambiguous older model usage unchanged unless the user explicitly asks to upgrade them.
Do not perform SDK, tooling, IDE, plugin, shell, auth, or provider-environment migrations as part of a model-and-prompt upgrade.
If an upgrade needs API-surface changes, schema rewiring, tool-handler changes, or implementation work beyond a literal model-string replacement and prompt edits, report it as blocked or confirmation-needed.
For general docs lookup, search docs with a precise query, fetch the best page and exact section needed, and answer with concise citations.
Reference map

Read only what you need:

https://developers.openai.com/api/docs/guides/latest-model.md -> current model-selection and "best/latest/current model" questions.
references/latest-model.md -> bundled fallback for model-selection and "best/latest/current model" questions.
references/upgrade-guide.md -> bundled fallback for model upgrade and upgrade-planning requests.
references/prompting-guide.md -> bundled fallback for prompt rewrites and prompt-behavior upgrades.
Quality rules
Treat OpenAI docs as the source of truth; avoid speculation.
Keep migration changes narrow and behavior-preserving.
Prefer prompt-only upgrades when possible.
Do not invent pricing, availability, parameters, API changes, or breaking changes.
Keep quotes short and within policy limits; prefer paraphrase with citations.
If multiple pages differ, call out the difference and cite both.
If official docs and repo behavior disagree, state the conflict and stop before making broad edits.
If docs do not cover the user’s need, say so and offer next steps.
Tooling notes
Always use MCP doc tools before any web search for OpenAI-related questions.
If the MCP server is installed but returns no meaningful results, then use web search as a fallback.
When falling back to web search, restrict to official OpenAI domains (developers.openai.com, platform.openai.com) and cite sources.
Weekly Installs
1.5K
Repository
openai/skills
GitHub Stars
18.0K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail