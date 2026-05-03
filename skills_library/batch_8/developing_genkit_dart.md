---
title: developing-genkit-dart
url: https://skills.sh/firebase/agent-skills/developing-genkit-dart
---

# developing-genkit-dart

skills/firebase/agent-skills/developing-genkit-dart
developing-genkit-dart
Installation
$ npx skills add https://github.com/firebase/agent-skills --skill developing-genkit-dart
Summary

Unified AI SDK for Dart enabling code generation, structured outputs, tools, flows, and agents.

Provides core APIs for generation, tool definition, flow orchestration, embeddings, and streaming with a single interface
Includes 8+ plugins for LLM providers (Google Gemini, Anthropic Claude, OpenAI GPT), Firebase AI, Model Context Protocol, Chrome browser integration, and HTTP server hosting via Shelf
Built-in CLI with local development UI for flow execution, tracing, model experimentation, and output evaluation
Requires schemantic library for type-safe schema mapping in tools, flows, and prompts
SKILL.md
Genkit Dart

Genkit Dart is an AI SDK for Dart that provides a unified interface for code generation, structured outputs, tools, flows, and AI agents.

Core Features and Usage

If you need help with initializing Genkit (Genkit()), Generation (ai.generate), Tooling (ai.defineTool), Flows (ai.defineFlow), Embeddings (ai.embedMany), streaming, or calling remote flow endpoints, please load the core framework reference: references/genkit.md

Genkit CLI (recommended)

The Genkit CLI provides a local development UI for running Flow, tracing executions, playing with models, and evaluating outputs.

check if the user has it installed: genkit --version

Installation:

curl -sL cli.genkit.dev | bash # Native CLI
# OR
npm install -g genkit-cli # Via npm


Usage: Wrap your run command with genkit start to attach the Genkit developer UI and tracing:

genkit start -- dart run main.dart

Plugin Ecosystem

Genkit relies on a large suite of plugins to perform generative AI actions, interface with external LLMs, or host web servers.

When asked to use any given plugin, always verify usage by referring to its corresponding reference below. You should load the reference when you need to know the specific initialization arguments, tools, models, and usage patterns for the plugin:

Plugin Name	Reference Link	Description
genkit_google_genai	references/genkit_google_genai.md	Load for Google Gemini plugin interface usage.
genkit_anthropic	references/genkit_anthropic.md	Load for Anthropic plugin interface for Claude models.
genkit_openai	references/genkit_openai.md	Load for OpenAI plugin interface for GPT models, Groq, and custom compatible endpoints.
genkit_middleware	references/genkit_middleware.md	Load for Tooling for specific agentic behavior: filesystem, skills, and toolApproval interrupts.
genkit_mcp	references/genkit_mcp.md	Load for Model Context Protocol integration (Server, Host, and Client capabilities).
genkit_chrome	references/genkit_chrome.md	Load for Running Gemini Nano locally inside the Chrome browser using the Prompt API.
genkit_shelf	references/genkit_shelf.md	Load for Integrating Genkit Flow actions over HTTP using Dart Shelf.
genkit_firebase_ai	references/genkit_firebase_ai.md	Load for Firebase AI plugin interface (Gemini API via Vertex AI).
External Dependencies

Whenever you define schemas mapping inside of Tools, Flows, and Prompts, you must use the schemantic library. To learn how to use schemantic, ensure you read references/schemantic.md for how to implement type safe generated Dart code. This is particularly relevant when you encounter symbols like @Schema(), SchemanticType, or classes with the $ prefix. Genkit Dart uses schemantic for all of its data models so it's a CRITICAL skill to understand for using Genkit Dart.

Best Practices
Always check that code cleanly compiles using dart analyze before generating the final response.
Always use the Genkit CLI for local development and debugging.
Weekly Installs
37.7K
Repository
firebase/agent-skills
GitHub Stars
264
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass