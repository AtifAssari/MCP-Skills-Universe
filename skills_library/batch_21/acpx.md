---
title: acpx
url: https://skills.sh/asm3r96/wave-driven-dev/acpx
---

# acpx

skills/asm3r96/wave-driven-dev/acpx
acpx
Installation
$ npx skills add https://github.com/asm3r96/wave-driven-dev --skill acpx
SKILL.md
acpx
When to use this skill

Use this skill when you need to run coding agents through acpx, manage persistent ACP sessions, queue prompts, or consume structured output from scripts.

Use it especially for Wave-Driven Development execution after wave-planner-acpx is approved.

What acpx is

acpx is a headless, scriptable CLI client for ACP (Agent Client Protocol) designed for agent-to-agent automation without PTY scraping.

Core capabilities:

Persistent multi-turn sessions per repo/cwd
One-shot execution mode (exec)
Named parallel sessions (-s/--session)
Queue-aware prompt submission with optional fire-and-forget (--no-wait)
Cooperative cancel (cancel) for in-flight turns
Session control (set-mode, set <key> <value>)
Session metadata/history inspection (sessions show, sessions history)
Local agent process checks (status)
Structured output formats (text, json, quiet)
--suppress-reads for cleaner orchestration output
--prompt-retries for retrying transient prompt failures
Generic model selection via ACP session/set_model
--model support for Codex sessions
Experimental flows runtime and replay-related tooling in v0.4.0
Install
npm i -g acpx


Prefer global install over npx for stable session reuse.

Command model

prompt is default.

acpx [global_options] [prompt_text...]
acpx [global_options] prompt [prompt_options] [prompt_text...]
acpx [global_options] exec [prompt_options] [prompt_text...]
acpx [global_options] cancel [-s <name>]
acpx [global_options] set-mode <mode> [-s <name>]
acpx [global_options] set <key> <value> [-s <name>]
acpx [global_options] status [-s <name>]
acpx [global_options] sessions [list | new [--name <name>] | close [name] | show [name] | history [name] [--limit <count>]]
acpx [global_options] config [show | init]

acpx [global_options] <agent> [prompt_options] [prompt_text...]
acpx [global_options] <agent> exec [prompt_options] [prompt_text...]

Built-in agent registry

Friendly names:

codex -> npx @zed-industries/codex-acp
claude -> npx @zed-industries/claude-agent-acp
gemini -> gemini
opencode -> npx opencode-ai
pi -> npx pi-acp
qoder -> qodercli --acp
trae -> traecli acp serve

Rules:

Default agent is codex.
Unknown positional agent tokens are treated as raw commands.
--agent <command> is explicit raw command mode.
Do not combine positional agent token with --agent.
Core workflows
Persistent prompt session
acpx codex 'inspect failing tests and propose fix plan'
acpx codex 'apply minimal fix and run tests'

One-shot exec
acpx exec 'summarize this repo'
acpx codex exec 'review changed files'

Sessions
acpx sessions new --name backend
acpx codex -s backend 'fix API pagination bug'
acpx codex sessions history backend --limit 20
acpx codex sessions close backend

Queueing and no-wait
acpx codex 'run full test suite and investigate failures'
acpx codex --no-wait 'after tests, summarize root causes and next steps'

Structured output for orchestration
acpx --format json codex exec 'review changed files' > events.ndjson

Retries and quieter logs
acpx codex --prompt-retries 2 'run targeted tests and summarize failures'
acpx --format json --suppress-reads codex exec 'review changed files'

Wave-Driven orchestration guidance

When running worker agents in waves:

Create one named session per worker (-s <agent-name>).
Send worker prompt with strict ownership boundaries.
Require explicit completion marker in each response.
Wait for marker before merge.
Merge per wave order.
Run integration checks before next wave.

Recommended completion marker: WAVE {WAVE_ID} / {AGENT_NAME} DONE

Recommended worker handoff format:

Summary
Files changed
Patch/diffs
How to test (commands + expected results)
Risks/TODOs/Dependency Notes
Global options
--agent <command> raw ACP adapter command
--cwd <dir> session scope directory
--approve-all auto-approve all requests
--approve-reads approve reads/searches, prompt for writes
--deny-all deny all requests
--model <id> request a model when supported by the target agent/session
--format <fmt> output: text, json, quiet
--suppress-reads hide raw read/search output when cleaner logs are useful
--prompt-retries <count> retry transient prompt failures automatically
--timeout <seconds> max wait
--ttl <seconds> queue owner idle TTL
--verbose debug logs

Permission flags are mutually exclusive.

Session behavior

Persistent prompt sessions are scoped by:

agentCommand
absolute cwd
optional session name

Tips:

Use named sessions for parallel streams in one repo.
Use --cwd carefully; changing cwd changes session scope.
Use status and sessions show/history to debug state.
Practical examples

Parallel named streams:

acpx codex -s backend 'implement contract types for Wave 0'
acpx claude -s docs 'draft migration notes for Wave 0'


Repo-scoped review with permissive mode:

acpx --cwd ~/repos/shop --approve-all codex -s pr-842 \
  'review PR #842 for regressions and propose minimal patch'

Weekly Installs
35
Repository
asm3r96/wave-driven-dev
GitHub Stars
1
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn