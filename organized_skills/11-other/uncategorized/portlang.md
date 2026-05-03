---
rating: ⭐⭐⭐
title: portlang
url: https://skills.sh/portofcontext/skills/portlang
---

# portlang

skills/portofcontext/skills/portlang
portlang
Installation
$ npx skills add https://github.com/portofcontext/skills --skill portlang
SKILL.md
portlang Skill
Core Concept

portlang treats agent behavior as search through a conditioned space. You don't script loops—you declare the search space:

Boundaries: What the agent cannot do (enforced by sandbox)
Verifiers: What success looks like (deterministic pass/fail signals, not walls of output)
Context budget: Hard token ceiling
Environment: What the agent can observe

The runtime executes the search. Every run produces a trajectory (complete event log).

The instruction budget problem: Models follow roughly 150–200 instructions reliably. A large system prompt, many tool definitions, growing conversation history, and re-observations all compete for that budget. portlang keeps budget usage low by design: each field is scoped narrowly, context is bounded by a hard ceiling, and re-observations inject only current state rather than accumulating history.

Prerequisites

portlang currently only runs on apple devices. Before running portlang fields:

Install portlang:
brew tap portofcontext/homebrew-tap
brew install portlang

Set API key (choose one):
export ANTHROPIC_API_KEY=sk-ant-...
export OPENROUTER_API_KEY=sk-or-v1-...

Verify installation:
portlang init  # Check container support

Install the VS Code extension (recommended): Search for "portlang" in the VS Code extension marketplace and install it. Provides LSP support — syntax highlighting, validation, and autocompletion for .field files.

Model naming by provider:

Anthropic API: anthropic/claude-sonnet-4.6, anthropic/claude-opus-4.5
OpenRouter: anthropic/claude-3.5-sonnet, anthropic/claude-3-opus, anything on openrouter that support tool calling
Provider auto-detected from API key
Field File Structure

Fields use the .field extension (preferred) or .toml — both are supported. All sections are optional unless marked (required). Fields marked "inherit" pull their value from a parent field one directory up (auto-detected from ../*.field).

name = "my-task"        # (required) identifier, used in trajectory storage
description = "..."     # human-readable summary

[vars]                  # optional; declare {{ var_name }} template variables
# customer_id = { required = true, description = "Salesforce account ID" }
# region = { required = false, default = "us-east-1", description = "AWS region" }

[model]                 # (required), or: model = "inherit"
name = "anthropic/claude-sonnet-4.6"  # (required)
temperature = 0.5       # default: 0.5

[prompt]                # (required)
goal = "..."            # (required) initial task; supports {{ var }} templates
system = "..."          # optional system prompt; supports {{ var }} templates
re_observation = ["echo '=== workspace ===' && ls -1", ...]  # refresh context each step

[environment]           # optional; all fields have defaults
root = "./workspace"    # working dir (maps to /workspace in container)
packages = ["nodejs"]   # apt packages to install; list "uv" to get uv/pip
dockerfile = "./Dockerfile"  # custom Dockerfile (overrides packages)
image = "custom:tag"    # pre-built image (overrides dockerfile)

[boundary]              # optional, or: boundary = "inherit"
allow_write = ["*.py"]  # glob patterns for writable paths; default: none
collect = ["report.md"] # files to deliver after run (subset of allow_write); default: all allow_write
network = "deny"        # "deny" | "allow"; default: allow
max_tokens = 150000     # hard ceiling on total context tokens
max_cost = "$2.00"      # hard ceiling on total cost (must be quoted string with $)
max_steps = 30          # hard ceiling on agent steps
bash = true             # enable built-in bash tool; default: true
output_schema = """{ ... }"""  # optional; JSON schema string for structured output via submit_output

tools = "inherit"       # optional; inherit [[tool]] list from parent instead of defining inline

[[skill]]               # repeatable; load a Claude Code skill into the agent's context
slug = "skill-name"     # (required) skill slug identifier

[[tool]]                # repeatable; type = "python" | "shell" | "mcp"; bash/glob/write are built-in defaults

# Shell verifier (default when type is omitted):
[[verifier]]
type = "shell"          # default; type can be omitted for shell verifiers
name = "..."            # (required)
command = "..."         # shell command; exit 0 = pass, nonzero = fail; supports {{ var }} templates
trigger = "on_stop"     # "on_stop" | "always" | "on_tool:<tool_name>"; default: on_stop
description = "..."     # injected into context on failure
eval_only = false       # if true, skipped during `portlang run`; only runs during `portlang eval run`

# Levenshtein verifier (normalized edit distance):
[[verifier]]
type = "levenshtein"
name = "..."
file = "output.txt"     # optional; omit to use output_schema structured output
expected = "..."        # reference string; supports {{ var }} templates
threshold = 0.9         # similarity [0.0–1.0] required to pass; default: 1.0

# Semantic similarity verifier (cosine via embeddings):
[[verifier]]
type = "semantic"
name = "..."
file = "output.txt"     # optional; omit to use output_schema structured output
expected = "..."        # reference string to embed and compare; supports {{ var }} templates
threshold = 0.85        # cosine similarity [0.0–1.0]; default: 0.8
embedding_model = "bge-small-en-v1.5"  # local model (~67 MB, downloaded once)
# embedding_url = "https://..."  # use OpenAI-compatible endpoint instead

# Tool call verifier (inspect or require a specific tool call):
[[verifier]]
type = "tool_call"
name = "..."
tool = "bash"           # (required for on_stop) assert this tool was called
field = "/input/path"   # optional; JSON pointer into {input: {...}, output: "..."}
matches = "^[a-z]+"    # optional; regex the field value must match
not_matches = "^/etc"  # optional; regex the field value must NOT match

Minimal Field File
name = "my-task"

[model]
name = "anthropic/claude-sonnet-4.6"

[prompt]
goal = "Create hello.py that prints 'Hello, World!'"

[environment]
root = "./workspace"

[boundary]
allow_write = ["hello.py"]
max_tokens = 80000
max_cost = "$1.00"
max_steps = 10

[[verifier]]
name = "works"
command = "python hello.py 2>&1 | grep -q 'Hello, World!'"
trigger = "on_stop"
description = "Must print 'Hello, World!'"

Essential Commands
portlang new task.field             # Scaffold a new field file (.field preferred; .toml also supported)
portlang new -i                      # Interactive step-by-step field creation
portlang run task.field             # Execute once (native runner, default)
portlang run task.field --dry-run   # Validate field without running (parse, check vars, show config)
portlang run task.field -n 10       # Run N times and report convergence reliability
portlang run task.field --runner claude-code  # Use Claude Code as agent loop
portlang run task.field --auto-reflect       # Run and immediately reflect on the trajectory
portlang run task.field --output-dir ./out  # Copy collected output files to ./out after run
portlang run task.field --json              # Emit run result as JSON (artifacts + structured_output + metadata)
portlang run task.field --var k=v   # Pass a template variable (repeatable)
portlang run task.field --vars p.json  # Pass variables from a JSON file
portlang run task.field --input ./data.csv   # Stage a file into the workspace before the agent starts
portlang run task.field --input '{"id":"123"}'  # Stage inline JSON as portlang_input.json
portlang list [field-name]           # List trajectories (--converged, --failed, --limit)
portlang eval run ./examples/        # Run all fields in a directory
portlang eval run ./examples/ --runner claude-code  # Eval suite using Claude Code runner
portlang eval run ./examples/ --resume <id>   # Resume a previous eval, skipping fields that already passed
portlang eval list [dir]             # List eval runs (--limit)
portlang eval view <id-or-dir>       # Open eval results dashboard (by run ID or directory)
portlang view trajectory <id>        # Open trajectory as interactive HTML
portlang view trajectory <id> --format text  # Replay trajectory step-by-step in terminal
portlang view diff <id-a> <id-b>     # Open trajectory comparison HTML
portlang view field <field-name>     # Open field adaptation report HTML
portlang reflect --field <field-name>           # Analyze trajectories and surface insights (AI-powered)
portlang reflect --field <field-name> -n 10     # Analyze N most recent trajectories
portlang reflect --trajectory-id <id>                       # Analyze a specific trajectory (--field auto-detected)
portlang docs                        # Print CLI reference as Markdown


Add --no-open to any view command to skip opening the browser. See reference/CLI.md for full flag details.

Key Patterns
1. Field Inheritance (shared model/boundary/tools across a suite)

If a *.field file exists one directory up, a child field can inherit from it automatically:

# parent/parent.field — shared config for all child fields
name = "parent"

[model]
name = "anthropic/claude-sonnet-4.6"
temperature = 0.5

[boundary]
network = "deny"
max_tokens = 100000
max_cost = "$1.00"
max_steps = 20

[[tool]]
type = "python"
file = "./tools/shared_utils.py"

# parent/task-a/task.field — child; inherits from ../parent.field
name = "task-a"
model = "inherit"
boundary = "inherit"
tools = "inherit"

[prompt]
goal = "Do task A using the shared tools."


Inheritance eliminates duplication across eval suites. Override any section by defining it inline.

2. Template Variables (parameterize a field for reuse)

Declare variables in [vars], use {{ name }} anywhere in goal/system/re_observation/verifier commands, supply at runtime with --var:

[vars]
currency = { required = false, default = "usd", description = "Currency to report" }

[prompt]
goal = "Get the account balance and return amounts in {{ currency }}."

[[verifier]]
name = "correct-currency"
type = "tool_call"
tool = "bash"
trigger = "on_stop"
description = "Agent must have run bash"

portlang run task.field --var currency=gbp
portlang run task.field --vars params.json   # bulk vars from file
portlang run task.field --input ./data.csv   # stage input file into workspace


--input with a file copies it to the workspace root. --input '{"key":"val"}' writes portlang_input.json. Use re_observation to surface the file contents to the agent each step.

3. Output: Files and Structured Data

portlang has two output mechanisms.

Mechanism	How it works	Best for
collect + file artifacts	Files the agent writes to the workspace, delivered after the run via --output-dir or --json	Documents, code, reports — anything that lives as a file
output_schema + submit_output	Agent calls a built-in tool with a JSON payload matching the declared schema	Typed structured payloads the agent constructs — summaries, verdicts, scores, extracted data

File artifacts — collect:

[boundary]
allow_write = ["report.md", "results/*.json"]
collect = ["report.md", "results/*.json"]  # subset to deliver; default: all allow_write

portlang run task.field --output-dir ./out   # copies report.md, results/*.json into ./out/
portlang run task.field --json               # embeds file contents in JSON stdout
portlang run task.field --json | jq '.artifacts[0].content'


If collect is omitted, all allow_write files are delivered. Set collect = [] to deliver nothing.

Structured output — output_schema:

Define output_schema in [boundary] as a JSON Schema string. The agent calls submit_output with a matching payload; portlang validates it automatically — no verifier needed for schema conformance:

[boundary]
output_schema = '''
{
  "type": "object",
  "required": ["status", "count"],
  "properties": {
    "status": {"type": "string", "enum": ["success", "failure"]},
    "count": {"type": "integer", "minimum": 0}
  }
}
'''


To assert specific field values in structured output, use a tool_call verifier:

[[verifier]]
type = "tool_call"
name = "status-ok"
tool = "submit_output"
field = "/input/status"
matches = "^success$"
trigger = "on_stop"
description = "status must be success"


--json output combines both:

{
  "run_id": "...",
  "field": "my-task",
  "outcome": "converged",
  "structured_output": { "status": "success", "count": 3 },
  "artifacts": [
    { "path": "report.md", "size": 4231, "content": "# Report\n..." }
  ],
  "cost": "0.023",
  "tokens": 18420,
  "steps": 8,
  "duration_ms": 34201,
  "trajectory_id": "..."
}

4. Multi-Layer Verifiers (fail fast with precise feedback)

Layer verifiers from coarse to fine — each one assumes the previous passed:

[[verifier]]
name = "compiled"
command = "python script.py 2>/dev/null"
trigger = "on_stop"
description = "script.py must run without errors"

[[verifier]]
name = "correct-output"
type = "levenshtein"
file = "output.txt"
expected = "42"
threshold = 1.0
trigger = "on_stop"
description = "output.txt must contain exactly '42'"


Verifiers run in order, stop on first failure. Use output_schema when the agent produces structured JSON output — schema validation is built-in, no verifier needed.

5. Smart Verifier Types

Prefer typed verifiers. They run in the portlang runtime — no packages required, no container dependencies. Fall back to shell verifiers only for logic that can't be expressed with a typed verifier, and only use tools guaranteed in the container baseline (see section 8).

Trigger modes: on_stop (default) runs after the agent finishes. always runs after every step. on_tool:<tool_name> runs after each call to a specific tool — useful for incremental checks, e.g. trigger = "on_tool:write" to validate files as they're written.

eval_only: Set eval_only = true to exclude a verifier from regular portlang run but include it in portlang eval run. Use this for ground-truth comparisons (levenshtein, semantic) where the expected value is known but shouldn't affect development runs or steer agent behavior.

# Fuzzy text match (tolerates minor differences)
[[verifier]]
type = "levenshtein"
name = "close-enough"
file = "output.txt"
expected = "The answer is 42."
threshold = 0.9
trigger = "on_stop"
description = "Output must be at least 90% similar to expected"

# Semantic match (meaning, not exact text)
[[verifier]]
type = "semantic"
name = "right-idea"
file = "summary.txt"
expected = "The model achieved high accuracy on the test set."
threshold = 0.85
trigger = "on_stop"
description = "Summary must convey the correct conclusion"


Local embedding model downloaded automatically (~67 MB, no API key required).

6. Scoped Boundaries
[boundary]
allow_write = ["output.json", "logs/*.txt"]
network = "deny"
max_tokens = 100000
max_cost = "$1.00"
max_steps = 20

7. Re-observation (prevent context rot)
[prompt]
goal = "..."
re_observation = [
  "echo '=== workspace ===' && ls -1 *.py *.txt 2>/dev/null | cat",
  "echo '=== tests ===' && python -m pytest --tb=no -q 2>&1 | tail -5",
]


Commands run before each agent step, injecting fresh state without accumulating history. This is the principled alternative to the Ralph loop — instead of periodically restarting the session to clear context rot, you push only what the agent needs to know right now. The context window stays bounded; the agent always knows current state.

8. Custom Environment
[environment]
root = "./workspace"
packages = ["nodejs", "npm"]    # Install apt packages

# Or use a custom Dockerfile:
dockerfile = "./Dockerfile"

# Or a pre-built image:
image = "myregistry/myimage:latest"


Default container baseline: The container is minimal. Available by default: standard POSIX shell builtins, bash, curl, wc, grep, cat, ls, find. Not available unless added to packages or a custom image: python3, node, jq, git, and most other tools.

Shell verifiers run inside the container and are subject to the same constraints. Prefer typed verifiers ("levenshtein", "semantic", "tool_call") or output_schema over shell verifiers whenever possible — they run natively in the portlang runtime and require nothing installed. Only use shell verifiers for checks that require container-side execution, and only invoke tools you've declared in packages.

9. Custom Tools

Default tools (always available, no [[tool]] entry needed):

bash — run shell commands in the container
glob — find files by pattern
write — write files to allowed paths

Define [[tool]] entries only to add capabilities beyond these three.

Python tools are the default choice. Use shell tools only for trivial single-command wrappers (e.g. wc, cp). Anything that parses output, handles errors, calls an API, or processes data belongs in a Python tool.

portlang auto-extracts everything the agent uses from the Python function — the quality of these annotations directly determines how well the agent uses the tool:

Python source	Agent sees
Function name	Tool name
Docstring	Tool description (how agent decides when to call it)
Parameter type hints	Input schema (validated before call)
Literal["a", "b"]	Enum constraints
Pydantic BaseModel return	Output schema (agent knows exactly what it gets back)

Use -> dict and the agent gets no output schema. Use -> MyModel(BaseModel) and the agent sees typed fields it can reason about.

Anti-pattern — don't do this:

# Bad: brittle, untyped, hard to debug
[[tool]]
type = "shell"
name = "fetch_data"
command = "curl -s {url} | jq '.results' > /workspace/data.json && echo '{\"ok\": true}'"
input_schema = '{"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}'


Do this instead — Python tool:

# tools/fetch_data.py
# /// script
# dependencies = ["requests", "pydantic"]
# ///

import json, pathlib
import requests
from pydantic import BaseModel

class FetchResult(BaseModel):
    ok: bool
    count: int
    output_path: str

def fetch_data(url: str, output_path: str) -> FetchResult:
    """Fetch JSON from a URL and write results to output_path."""
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json().get("results", [])
    pathlib.Path(output_path).write_text(json.dumps(data, indent=2))
    return FetchResult(ok=True, count=len(data), output_path=output_path)

[[tool]]
type = "python"
file = "./tools/fetch_data.py"
function = "fetch_data"  # schema auto-extracted from type hints


Python tool rules:

Use Pydantic models as return types. portlang auto-extracts the JSON schema — no manual schema needed. Raise exceptions on errors rather than returning error dicts.
Each tool file runs in isolation — tool files cannot import each other. Put all related logic in one file.
Declare third-party dependencies with a # /// script PEP 723 block at the top; uv installs them automatically — no need to add packages to [environment].
File paths in file = are relative to the field file, not the workspace root.

Shell tool (for simple wrappers only):

[[tool]]
type = "shell"
name = "word_count"
description = "Count words in a file"
command = "wc -w {path}"
input_schema = '{"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}'


Tool-first design: Write Python tools before writing the field. The agent's goal should be: call the tool, write the output. This keeps steps under 5, cost under $0.05, and boundaries naturally minimal. Agents that try to do complex work through raw bash (curl pipes, temp files, awk scripts) burn budget and fail more often.

MCP server (stdio):

[[tool]]
type = "mcp"
name = "filesystem"
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "/workspace"]
transport = "stdio"


MCP server (HTTP/SSE):

[[tool]]
type = "mcp"
name = "stripe"
url = "https://mcp.stripe.com"
transport = "http"
headers = { Authorization = "Bearer ${STRIPE_KEY}" }

10. Agent Skills

Load Claude Code skills into the agent's context using [[skill]] entries. Skills inject specialized knowledge or instructions into the agent before it starts.

[[skill]]
slug = "rust-best-practices"

[[skill]]
slug = "portlang"


Skills are loaded in declaration order. Use --runner claude-code — skills are passed via npx skills inject and are available as system prompt context during the run.

11. Claude Code Runner

Use --runner claude-code to run the agent loop through Claude Code instead of the native runner. This gives the agent Edit, Glob, Grep, LSP, WebSearch, and WebFetch — the full Claude Code toolset — inside portlang's sandbox and verifier system.

portlang run example.field --runner claude-code


Auth: if Claude Code is already installed and authenticated, no setup is needed — portlang reads credentials from ~/.claude/.credentials.json automatically. Otherwise run claude setup-token, or set ANTHROPIC_API_KEY.

How field config maps to Claude Code:

Field config	Behavior
model.name	Passed to Claude Code
[[tool]] MCP	Passed directly via --mcp-config
[[tool]] shell/python	Wrapped as MCP stdio servers, run in container
boundary.allow_write	Enforced via PostToolUse hook on Write/Edit
boundary.max_steps/cost/tokens	Monitored from stream; process killed on breach
[[verifier]] shell, on_stop	Run by portlang after agent exits
[[verifier]] shell, always/on_tool	Run as Claude Code PostToolUse hooks
boundary.network	Always enabled (Claude Code requires API access)
boundary.output_schema	Agent receives a submit_output tool; structured output captured from tool call

Limitations vs native runner: tool_call verifiers and boundary context tracing are not supported.

12. Batch Evaluation
portlang eval run ./examples/
portlang eval view ./examples/   # Open interactive HTML dashboard


Useful for regression testing after changes.

Debugging Workflow
Run fails → portlang view trajectory <id> --format text to replay step-by-step
Find failure point → Check which verifier failed and at which step
Non-determinism → portlang view diff <id-a> <id-b> to find divergence
Visual debugging → portlang view trajectory <id> for HTML view
Optimize → portlang run task.field -n 10 to measure reliability
Patterns → portlang view field <field-name> for adaptation analysis
Insights → portlang reflect --field <field-name> to surface AI-powered insights from trajectories
Common Issues

Budget exhausted:

Start conservative: max_cost = "$0.25" for simple tasks, $1.00 for network-heavy tasks; increase after profiling
Increase max_tokens or reduce max_steps in [boundary]
Simplify re_observation commands — context rot (early history crowding out current state) often masquerades as budget exhaustion; inject minimal, current-state signals only
Check for tool error loops
Move complex logic into Python tools so the agent does orchestration, not implementation

Low convergence rate (<70%):

Strengthen verifiers (make expectations explicit)
Tighten boundaries (restrict file access)
Clarify goal in [prompt]
Lower temperature (e.g., temperature = 0.0)

Verifier always passes/fails:

Weak signal (>95% or <10% pass rate) — adjust verifier command

Structured output not valid:

Add an explicit [[verifier]] to check output.json
Ensure [prompt].goal names the required fields explicitly
Use temperature = 0.0 for consistent JSON output
Reference Documentation
reference/CLI.md - Full CLI reference (all commands and flags)
reference/verifier_patterns.md - 20 real-world verifier examples
reference/custom_tools.md - Shell, Python, MCP guides
reference/trajectory_analysis.md - Advanced debugging
reference/field_recipes.md - 8 complete field examples
Core Principles
Boundaries are topology, not policy - Make bad actions impossible, not discouraged
Verifiers give deterministic signals - Not post-hoc checks; they steer behavior by giving the agent precise feedback instead of raw output to interpret
Context is finite and attention degrades - Smaller context windows produce better results; hard ceilings are quality controls, not just cost controls
Trajectories are data - Replay, diff, analyze distributions; measure convergence rate before shipping
Engineer the environment, not the prompt - Agent policy is opaque; the environment is yours. Use actual control flow for control flow, not prompt instructions

GitHub: https://github.com/portofcontext/portlang

Weekly Installs
15
Repository
portofcontext/skills
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn