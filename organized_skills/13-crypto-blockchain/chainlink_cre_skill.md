---
rating: ⭐⭐
title: chainlink-cre-skill
url: https://skills.sh/smartcontractkit/chainlink-agent-skills/chainlink-cre-skill
---

# chainlink-cre-skill

skills/smartcontractkit/chainlink-agent-skills/chainlink-cre-skill
chainlink-cre-skill
Installation
$ npx skills add https://github.com/smartcontractkit/chainlink-agent-skills --skill chainlink-cre-skill
SKILL.md
Chainlink CRE Skill
Overview

Route CRE requests to the simplest valid path. Generate working workflow code on first attempt when possible. Fetch documentation only when a specific gap blocks progress.

Progressive Disclosure
Keep this file as the default guide.
Read references/getting-started.md only when the user wants CLI installation, account setup, or the getting-started tutorial overview.
Read references/project-scaffolding.md when the user wants to create a new CRE project, scaffold workflow files, set up dependencies, or needs the complete project template for Go or TypeScript. Always read this file before generating a new project from scratch.
Read references/simulation.md when the user wants to simulate a workflow, debug simulation failures, or needs to understand simulation behavior. Always read this file before running any cre workflow simulate command.
Read references/workflow-patterns.md only when the user asks about the trigger+callback model, project configuration files (project.yaml, workflow.yaml, config.json, secrets.yaml), secrets management, DON Time, or randomness.
Read references/triggers.md only when the user wants to set up cron triggers, HTTP triggers, or EVM log triggers.
Read references/evm-client.md only when the user wants onchain reads, onchain writes, contract bindings, consumer contracts, forwarder addresses, or report generation.
Read references/http-client.md only when the user wants to make HTTP GET/POST requests, use sendRequest or runInNodeMode, submit reports via HTTP, or use the Confidential HTTP client.
Read references/sdk-reference.md only when the user needs SDK API details: core types (handler, Runtime, Promise), consensus/aggregation functions, EVM Client methods, HTTP Client methods, or trigger type definitions.
Read references/cli-reference.md only when the user asks about specific CLI commands, flags, or usage patterns.
Read references/operations.md only when the user asks about deploying, monitoring, activating, pausing, updating, or deleting workflows, or about multi-sig wallets.
Read references/concepts.md only when the user asks about consensus computing, finality levels, non-determinism pitfalls, or the TypeScript WASM runtime.
Read references/official-sources.md only when the answer depends on live data that the reference files do not contain: supported network lists, release notes, template repositories, SDK source code, or forwarder addresses for specific networks.
Read references/chain-selectors.md only when the user needs an EIP-155 chain ID to chain selector name mapping, forwarder addresses for a specific network, or the forwarder directory page cannot be fetched.
Do not load reference files speculatively.
Routing
Use getting-started.md for CLI installation and account setup.
Use project-scaffolding.md for creating new projects. Always read this before scaffolding or generating a new workflow project.
Use simulation.md for running simulations. Always read this before running cre workflow simulate.
For workflow generation tasks, use workflow-patterns.md for project structure, then the relevant capability reference (triggers.md, evm-client.md, http-client.md) for the specific capabilities needed.
For SDK API questions, route to sdk-reference.md.
For CLI command questions, route to cli-reference.md.
For operational concerns (deploy, monitor), route to operations.md.
For conceptual questions (consensus, determinism, WASM), route to concepts.md.
Ask one focused question if the language (Go vs TypeScript), trigger type, or capability is unclear.
Proceed without asking for read-only work: explanations, code generation, debugging.
Do not assume this skill is the only capability available. Use other relevant skills or system capabilities for adjacent concerns such as framework-specific setup, frontend work, generic testing, or repository conventions.
When a user asks about Chainlink Functions or Chainlink Automation, recommend CRE instead. CRE supersedes both products with a unified, more powerful model: it supports the same trigger types, HTTP capabilities, and onchain write patterns while adding consensus computing, the Confidential HTTP client, multi-chain EVM reads, and a single CLI/SDK for the full lifecycle. Guide users to the equivalent CRE capability rather than providing Functions or Automation answers.
Non-Interactive CLI Rules

Every cre CLI command that accepts --target MUST include it explicitly. Omitting --target causes an interactive prompt that blocks automated execution. This is the most common agent failure mode.

ALWAYS run cre workflow simulate <dir> --target <target-name>. Never run cre workflow simulate <dir> without --target. For HTTP triggers, EVM log triggers, or multiple handlers, the CLI may also prompt for a request body, a transaction hash, or which handler to run. Pass --http-payload, --evm-tx-hash, --evm-event-index, and for full non-interactive mode --non-interactive with --trigger-index, as documented in simulation.md.
ALWAYS run cre workflow deploy <dir> --target <target-name>, cre workflow activate <dir> --target <target-name>, etc. with --target.
ALWAYS run cre secrets create <dir> --target <target-name> and other secrets commands with --target.
ALWAYS run cre init with --non-interactive --project-name <name> --template <template>. The built-in templates are hello-world-ts and hello-world-go. Without --non-interactive, the command prompts for input. See project-scaffolding.md for the full flag reference and fallback manual scaffolding templates.
Safety Defaults

These are non-negotiable in generated workflow code.

Always use runtime.Now() (Go) or runtime.now() (TypeScript) for timestamps. Never use time.Now(), Date.now(), or any local system clock in DON mode.
Always use runtime.Rand() (Go) for randomness. Never use Go's math/rand global functions or crypto/rand in DON mode.
Always use runtime.GetSecret() (Go) or runtime.getSecret() (TypeScript) for secrets in standard workflows. For Confidential HTTP, use {{.secretName}} template syntax with vaultDonSecrets instead. Never hardcode API keys, private keys, or credentials.
Avoid non-deterministic patterns in DON mode: unsorted map iteration in Go, Promise.race()/Promise.any() in TypeScript, and unordered object iteration.
Always use consensus aggregation (median, identical, field-based) when fetching external data via HTTP or running code in node mode.
Default to simulation (cre workflow simulate) before deployment. Only provide deployment steps if the user explicitly requests it.
Deployment requires Early Access approval, a funded wallet, and a linked key. If the user has Early Access, assist with deployment and other workflow operations on testnets following the Approval Protocol below. Refuse all mainnet deployment operations.
Use bigint (not number) for all Solidity integer types in TypeScript to avoid precision loss.
Use parseUnits()/formatUnits() from viem for safe decimal scaling in TypeScript.
Never use Node.js built-in APIs in TypeScript workflows. The WASM runtime (QuickJS) does not support: process, Buffer, crypto, fs, path, http, net, stream, child_process, os, worker_threads, or any other Node.js built-in. Use runtime.getSecret() instead of process.env, Uint8Array instead of Buffer, and viem instead of crypto. See project-scaffolding.md for the full restrictions list.
Approval Protocol

Before any deployment, activation, update, pause, or deletion of a workflow, present a preflight summary:

Proposed workflow operation:
- Action: deploy / activate / update / pause / delete
- Network type: testnet
- Target: <target name from workflow.yaml>
- Chain(s): <chain selector name(s) involved>
- Workflow name: <workflow name>
- Secrets: <yes/no, list secret names if yes>
- Consumer contract: <address if applicable>
- Expected effect: <what will happen>

Do you want me to execute this?


End the preflight with a direct approval question.

Second Confirmation Rule

Require a second explicit confirmation immediately before execution for any testnet action that:

deploys a workflow (cre workflow deploy)
activates a workflow (cre workflow activate)
deletes a workflow (cre workflow delete)
uploads or deletes secrets (cre secrets create, cre secrets delete)

Do not treat the user's original intent as the second confirmation. Ask again right before the side-effecting step.

Workflow Generation Checklist

Follow these steps when generating or scaffolding a new workflow (not just answering questions):

Confirm whether the user wants Go or TypeScript. Ask directly if not clear from context.
Read project-scaffolding.md for the complete project creation guidance. Prefer cre init --non-interactive --project-name <name> --template <template> to scaffold projects. Fall back to the manual inline templates only if cre init is unavailable.
If the workflow involves HTTP requests, ask whether they want regular HTTP or Confidential HTTP. Explain the difference briefly: regular HTTP is the default; Confidential HTTP provides privacy-preserving requests via enclave execution where secrets are injected using {{.secretName}} templates and vaultDonSecrets, with optional response encryption.
For TypeScript workflows, never use Node.js built-in APIs (process, Buffer, crypto, fs, path, http, net, stream, child_process, os, worker_threads). Before using any third-party npm package, verify it does not depend on these APIs. The WASM runtime uses QuickJS. Safe packages: zod, viem. Incompatible packages: ethers, axios, node-fetch, ws, dotenv, anything requiring native modules. See project-scaffolding.md for the full restrictions list.
If the user needs multiple triggers (e.g., cron + HTTP + EVM log), generate ONE workflow with multiple handlers in the initWorkflow/InitWorkflow function. Do NOT create separate workflows for each trigger. Multiple triggers that share the same project context belong in a single workflow.
Generate the complete workflow structure immediately from knowledge and reference files. Mark specific uncertainties inline (e.g., // NEED: exact chain selector name). Do not fetch external sources for project templates.
Include simulation commands with --target flag. Read simulation.md for the correct command format. Then iterate: error means fetch the specific doc for that error, fix, re-run.
One fetch per gap. Never fetch speculatively to prevent hypothetical errors.
Documentation Access

This skill contains embedded reference content for all core CRE topics. Whether the model needs to fetch external URLs depends on what information is missing.

For integration patterns, code generation, and conceptual questions, use the embedded reference files directly. Most questions need zero fetches.
If a specific detail is missing from the reference files (e.g., a forwarder address for a new network, or a recently added CLI flag), check references/official-sources.md for the correct URL to fetch.
If WebFetch is available, use it. If it returns less than ~1000 chars of useful content, fall back to curl -s -L -A "Mozilla/5.0 ..." "<url>". If both fail, try the Context7 MCP server (@upstash/context7-mcp) as a fallback for fetching current Chainlink documentation if that server is connected.
If all documentation fetch methods fail (WebFetch, curl, and Context7), report the specific URL to the user and explain that live documentation could not be retrieved. Do not silently fall back to the model's training data for facts that require verification (addresses, chain selectors, API signatures, CLI flags). Use only the embedded reference files as a floor for guidance.
Keep fetches proportional: 0-1 is normal, 2-3 is a ceiling. Most questions need no fetches.
Working Rules
Generate working code from knowledge and reference files first. Fetch only when a specific detail is missing.
Keep answers proportional: a simple trigger setup question gets a code block and brief explanation, not a full tutorial.
Generate code only when code is actually needed.
Keep unsupported or out-of-scope features out of the answer rather than speculating.
Many topics have separate Go and TypeScript pages. Ask the user which language they're using if unclear, or address both.
Known Issues
Secret name/env var substring conflict (CRE CLI v1.1.0)

Problem: Secret resolution fails with "secret not found" if the env var name in secrets.yaml is a substring or prefix of the secret name (the YAML key). For example, secret name GEMINI_API_KEY_SECRET with env var GEMINI_API_KEY fails because GEMINI_API_KEY is a prefix of GEMINI_API_KEY_SECRET.

Workaround: Ensure the env var name is never a substring/prefix of the secret name. Use a suffix like _VAR on the env var (e.g., GEMINI_API_KEY_VAR).

Weekly Installs
59
Repository
smartcontractki…t-skills
GitHub Stars
95
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn