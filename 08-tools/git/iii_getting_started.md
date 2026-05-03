---
title: iii-getting-started
url: https://skills.sh/iii-hq/iii/iii-getting-started
---

# iii-getting-started

skills/iii-hq/iii/iii-getting-started
iii-getting-started
Installation
$ npx skills add https://github.com/iii-hq/iii --skill iii-getting-started
SKILL.md
Getting Started with iii

iii replaces your API framework, task queue, cron scheduler, pub/sub, state store, and observability pipeline with a single engine and three primitives: Function, Trigger, Worker.

Step 1: Install the Engine
curl -fsSL https://install.iii.dev/iii/main/install.sh | sh


Verify it installed:

iii --version

Step 2: Create a Project
curl -LO https://github.com/iii-hq/cli-tooling/releases/latest/download/quickstart.zip
unzip quickstart.zip
cd quickstart


The quickstart includes TypeScript, Python, and Rust workers. If you don't have all runtimes, the README includes Docker Compose instructions.

Step 3: Start the Engine
iii --config iii-config.yaml


The engine starts and listens for worker connections on ws://localhost:49134. The REST API is available at http://localhost:3111. The console is available at http://localhost:3113.

Step 4: Install the SDK

Pick your language:

# TypeScript / Node.js
npm install iii-sdk

# Python
pip install iii-sdk

# Rust — add to Cargo.toml
# [dependencies]
# iii-sdk = "*"

Step 5: Write Your First Worker
TypeScript
import { registerWorker, Logger, TriggerAction } from 'iii-sdk'

const iii = registerWorker(process.env.III_URL ?? 'ws://localhost:49134')

iii.registerFunction(
  'hello::greet',
  async (input) => {
    const logger = new Logger()
    const name = input?.name ?? 'world'
    logger.info('Greeting user', { name })
    return { message: `Hello, ${name}!` }
  },
  { description: 'Greet a user by name' },
)

iii.registerTrigger({
  type: 'http',
  function_id: 'hello::greet',
  config: { api_path: '/hello', http_method: 'POST' },
})

Python
from iii import register_worker, InitOptions, Logger

iii = register_worker(address="ws://localhost:49134", options=InitOptions(worker_name="hello-worker"))

def greet(data):
    logger = Logger()
    name = data.get("name", "world") if isinstance(data, dict) else "world"
    logger.info("Greeting user", {"name": name})
    return {"message": f"Hello, {name}!"}

iii.register_function({"id": "hello::greet", "description": "Greet a user by name"}, greet)
iii.register_trigger({"type": "http", "function_id": "hello::greet", "config": {"api_path": "/hello", "http_method": "POST"}})

Rust
use iii_sdk::{register_worker, InitOptions, Logger, RegisterFunctionMessage, RegisterTriggerInput};
use serde_json::json;

let iii = register_worker("ws://127.0.0.1:49134", InitOptions::default());

iii.register_function(
    RegisterFunctionMessage::with_id("hello::greet".into()),
    |input: serde_json::Value| async move {
        let logger = Logger::new();
        let name = input["name"].as_str().unwrap_or("world");
        logger.info("Greeting user", Some(&json!({ "name": name })));
        Ok(json!({ "message": format!("Hello, {}!", name) }))
    },
);

iii.register_trigger(RegisterTriggerInput {
    trigger_type: "http".into(),
    function_id: "hello::greet".into(),
    config: json!({ "api_path": "/hello", "http_method": "POST" }),
})?;

Step 6: Test It
curl -X POST http://localhost:3111/hello \
  -H "Content-Type: application/json" \
  -d '{"name": "iii"}'


Expected response:

{"message": "Hello, iii!"}

Install Agent Skills

Get all iii skills for your AI coding agent:

npx skillkit add iii-hq/iii/skills


Skills teach your agent how to use every iii primitive — HTTP endpoints, cron scheduling, queues, state management, streams, channels, and more. Available for Claude Code, Cursor, Codex, Gemini CLI, and 30+ other agents.

Adapting This Pattern
Add more functions to the same worker — each gets its own registerFunction + registerTrigger calls
Use :: separator for function IDs to namespace them: orders::create, orders::validate
Add cron triggers with { type: 'cron', config: { expression: '0 0 9 * * * *' } } (7-field: sec min hour day month weekday year)
Add queue triggers with { type: 'durable:subscriber', config: { topic: 'my-queue' } }
Use iii.trigger() to invoke other functions from within a function
Use state::get / state::set to persist data across function calls
Recommended Next Steps

After getting your first worker running:

Add state — Use iii-state-management skill to persist data
Add a queue — Use iii-queue-processing skill for async job processing
Add a cron job — Use iii-cron-scheduling skill for scheduled tasks
Build an API — Use iii-http-endpoints skill for REST endpoints with CRUD
Add observability — Use iii-observability skill for tracing and metrics
Explore architecture patterns — See iii-agentic-backend, iii-reactive-backend, iii-workflow-orchestration
Key Resources
Quickstart Guide
SDK Reference — Node.js
SDK Reference — Python
SDK Reference — Rust
Engine Configuration
Console Dashboard
Pattern Boundaries
For HTTP endpoint patterns (CRUD, parameterized routes), prefer iii-http-endpoints
For cron/scheduling patterns, prefer iii-cron-scheduling
For queue/async job patterns, prefer iii-queue-processing
For state persistence patterns, prefer iii-state-management
For engine configuration, prefer iii-engine-config
Stay with iii-getting-started for installation, initial setup, and first-worker guidance
When to Use
Use this skill when the task is about installing iii, creating a new project, or writing a first worker.
Triggers when the request asks for setup help, quickstart guidance, or getting started with iii.
Boundaries
Never use this skill as a generic fallback for unrelated tasks.
You must not apply this skill when a more specific iii skill is a better fit.
Always verify environment and safety constraints before applying examples from this skill.
Weekly Installs
10
Repository
iii-hq/iii
GitHub Stars
15.3K
First Seen
Apr 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn