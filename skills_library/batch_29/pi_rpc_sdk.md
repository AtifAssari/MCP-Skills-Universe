---
title: pi-rpc-sdk
url: https://skills.sh/romiluz13/pi-agent-skills/pi-rpc-sdk
---

# pi-rpc-sdk

skills/romiluz13/pi-agent-skills/pi-rpc-sdk
pi-rpc-sdk
Installation
$ npx skills add https://github.com/romiluz13/pi-agent-skills --skill pi-rpc-sdk
SKILL.md
Pi RPC and SDK integration
Grounding
pi-mono/packages/coding-agent/docs/rpc.md — Framing section (LF-only record delimiter; readline incompatibility with U+2028/U+2029).
pi-mono/packages/coding-agent/docs/sdk.md — programmatic session patterns plus createAgentSession, AgentSession, createAgentSessionRuntime, ModelRegistry.create(), AuthStorage.create(), and SessionManager.inMemory().
pi-mono/packages/coding-agent/docs/json.md — --mode json event stream: session header, agent_*/turn_*/message_*/tool_execution_* events, jq filtering examples.
pi-mono/packages/coding-agent/src/modes/rpc/rpc-client.ts — reference TypeScript client mentioned from rpc.md intro when applicable.
pi-mono/packages/coding-agent/src/core/agent-session.ts — API surface for in-process embedding (per rpc.md note to TypeScript users).
Invariants
Framing rules are normative text in pi-mono/packages/coding-agent/docs/rpc.md; quote or paraphrase strictly from that file when advising client implementers.
Skill commands and prompt templates are expanded for RPC prompts per rpc.md Input expansion bullet under prompt command.
--mode json is read-only observation (stdout events); --mode rpc is bidirectional control (stdin commands + stdout responses). Different use cases, same framing caveats for U+2028/U+2029.
For TypeScript/Node embedding, createAgentSession() is the primary factory; it requires sessionManager, authStorage, and modelRegistry. For advanced multi-session hosting, use createAgentSessionRuntime() which returns AgentSessionRuntime with lower-level access to agent, sessionManager, settingsManager, modelRegistry, extensions, bashExecutor, resourceLoader — pi-mono/packages/coding-agent/docs/sdk.md.
Workflows
Choose integration: If user is on Node/TS, point to rpc.md recommendation to prefer AgentSession vs subprocess; cite the file’s opening Note for Node.js/TypeScript users.
Debug framing: Re-read Framing section; do not suggest generic line readers as compliant.
JSON event stream: For read-only observation of agent activity, point to json.md (--mode json); for bidirectional control, point to rpc.md (--mode rpc).
In-process embedding: For TypeScript/Node users who don't need subprocess isolation, prefer createAgentSession() over --mode rpc. Import from @mariozechner/pi-coding-agent. See pi-mono/packages/coding-agent/docs/sdk.md and pi-mono/packages/coding-agent/examples/sdk/.
Anti-patterns
Do not describe delimiter behavior contradicting rpc.md (only \n as record delimiter; optional \r strip on input).
Weekly Installs
15
Repository
romiluz13/pi-ag…t-skills
GitHub Stars
11
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass