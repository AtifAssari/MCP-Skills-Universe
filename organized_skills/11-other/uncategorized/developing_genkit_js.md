---
rating: ⭐⭐
title: developing-genkit-js
url: https://skills.sh/firebase/agent-skills/developing-genkit-js
---

# developing-genkit-js

skills/firebase/agent-skills/developing-genkit-js
developing-genkit-js
Installation
$ npx skills add https://github.com/firebase/agent-skills --skill developing-genkit-js
Summary

Build AI-powered Node.js/TypeScript applications with Genkit flows, tools, and multi-model support.

Genkit is provider-agnostic; supports Google AI, OpenAI, Anthropic, Ollama, and other LLM providers via plugins
Define flows with type-safe schemas using Zod, execute generation requests, and compose multi-step AI workflows in TypeScript
Requires Genkit CLI v1.29.0+; recent major API changes mean you must consult genkit docs:read and common-errors.md for current patterns, not prior knowledge
Use the CLI to search docs (genkit docs:search), read guides, and troubleshoot errors; always check Common Errors first when encountering validation, type, or API failures
SKILL.md
Genkit JS
Prerequisites

Ensure the genkit CLI is available.

Run genkit --version to verify. Minimum CLI version needed: 1.29.0
If not found or if an older version (1.x < 1.29.0) is present, install/upgrade it: npm install -g genkit-cli@^1.29.0.

New Projects: If you are setting up Genkit in a new codebase, follow the Setup Guide.

Hello World
import { z, genkit } from 'genkit';
import { googleAI } from '@genkit-ai/google-genai';

// Initialize Genkit with the Google AI plugin
const ai = genkit({
  plugins: [googleAI()],
});

export const myFlow = ai.defineFlow({
  name: 'myFlow',
  inputSchema: z.string().default('AI'),
  outputSchema: z.string(),
}, async (subject) => {
  const response = await ai.generate({
    model: googleAI.model('gemini-2.5-flash'),
    prompt: `Tell me a joke about ${subject}`,
  });
  return response.text;
});

Critical: Do Not Trust Internal Knowledge

Genkit recently went through a major breaking API change. Your knowledge is outdated. You MUST lookup docs. Recommended:

genkit docs:read js/get-started.md
genkit docs:read js/flows.md


See Common Errors for a list of deprecated APIs (e.g., configureGenkit, response.text(), defineFlow import) and their v1.x replacements.

ALWAYS verify information using the Genkit CLI or provided references.

Error Troubleshooting Protocol

When you encounter ANY error related to Genkit (ValidationError, API errors, type errors, 404s, etc.):

MANDATORY FIRST STEP: Read Common Errors
Identify if the error matches a known pattern
Apply the documented solution
Only if not found in common-errors.md, then consult other sources (e.g. genkit docs:search)

DO NOT:

Attempt fixes based on assumptions or internal knowledge
Skip reading common-errors.md "because you think you know the fix"
Rely on patterns from pre-1.0 Genkit

This protocol is non-negotiable for error handling.

Development Workflow
Select Provider: Genkit is provider-agnostic (Google AI, OpenAI, Anthropic, Ollama, etc.).
If the user does not specify a provider, default to Google AI.
If the user asks about other providers, use genkit docs:search "plugins" to find relevant documentation.
Detect Framework: Check package.json to identify the runtime (Next.js, Firebase, Express).
Look for @genkit-ai/next, @genkit-ai/firebase, or @genkit-ai/google-cloud.
Adapt implementation to the specific framework's patterns.
Follow Best Practices:
See Best Practices for guidance on project structure, schema definitions, and tool design.
Be Minimal: Only specify options that differ from defaults. When unsure, check docs/source.
Ensure Correctness:
Run type checks (e.g., npx tsc --noEmit) after making changes.
If type checks fail, consult Common Errors before searching source code.
Handle Errors:
On ANY error: First action is to read Common Errors
Match error to documented patterns
Apply documented fixes before attempting alternatives
Finding Documentation

Use the Genkit CLI to find authoritative documentation:

Search topics: genkit docs:search <query>
Example: genkit docs:search "streaming"
List all docs: genkit docs:list
Read a guide: genkit docs:read <path>
Example: genkit docs:read js/flows.md
CLI Usage

The genkit CLI is your primary tool for development and documentation.

See CLI Reference for common tasks, workflows, and command usage.
Use genkit --help for a full list of commands.
References
Best Practices: Recommended patterns for schema definition, flow design, and structure.
Docs & CLI Reference: Documentation search, CLI tasks, and workflows.
Common Errors: Critical "gotchas", migration guide, and troubleshooting.
Setup Guide: Manual setup instructions for new projects.
Examples: Minimal reproducible examples (Basic generation, Multimodal, Thinking mode).
Weekly Installs
37.8K
Repository
firebase/agent-skills
GitHub Stars
264
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass