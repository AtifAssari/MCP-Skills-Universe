---
rating: ⭐⭐⭐
title: isol8
url: https://skills.sh/illusion47586/isol8/isol8
---

# isol8

skills/illusion47586/isol8/isol8
isol8
Installation
$ npx skills add https://github.com/illusion47586/isol8 --skill isol8
SKILL.md
Isol8 Skill

Isol8 is a secure execution engine for running untrusted code inside Docker containers with strict resource limits, network controls, and output sanitization. Use this skill when you need to execute code, scripts, system commands, or AI coding agents in a safe, isolated environment.

For full documentation, see the isol8 docs. This file is a quick-reference for AI agents — it covers the most common operations and links to detailed docs for everything else.

Quick Reference
CLI Commands
Command	Purpose	Full Docs
isol8 run [file]	Execute code in an isolated container	CLI: run
isol8 setup	Build Docker images, optionally bake in packages	CLI: setup
isol8 build --base <runtime> --install <pkg>	Build a custom runtime image with pre-baked dependencies and/or setup scripts	CLI: build
isol8 cleanup	Remove orphaned isol8 containers	CLI: cleanup
isol8 serve	Start HTTP server for remote execution (downloads binary on first use)	CLI: serve
isol8 config	Display resolved configuration	CLI: config
Input Resolution (isol8 run)
--eval flag (inline code, defaults to python runtime)
File argument (runtime auto-detected from extension, or forced with --runtime)
Stdin (defaults to python runtime)

Extension mapping: .py → python, .js/.mjs/.cjs → node, .ts → bun, .mts → deno, .sh → bash. The agent runtime has no file extension mapping and must be specified explicitly with --runtime agent.

Most-Used Flags (isol8 run)
Flag	Default	Description
-e, --eval <code>	—	Execute inline code
-r, --runtime <name>	auto-detect	Force: python, node, bun, deno, bash, agent
--no-stream	false	Disable real-time output streaming
--persistent	false	Keep container alive between runs
--persist	false	Keep container after execution for debugging
--debug	false	Enable internal debug logging
--install <package>	—	Install package before execution (repeatable)
--setup <command>	—	Setup script/command run before execution (repeatable; reads file if path exists)
--workdir <path>	/sandbox	Working directory for code execution (must be inside /sandbox)
--net <mode>	none	Network: none, host, filtered
--timeout <ms>	30000	Execution timeout
--memory <limit>	512m	Memory limit
--secret <KEY=VALUE>	—	Secret env var, value masked in output (repeatable)
--stdin <data>	—	Pipe data to stdin

For the complete flag reference (20 flags total), see CLI: run.

CLI Examples
# Python inline
isol8 run -e "print('Hello!')" --runtime python

# Run a file (runtime auto-detected)
isol8 run script.py

# With package installation
isol8 run -e "import numpy; print(numpy.__version__)" --runtime python --install numpy

# Pipe via stdin
echo "console.log(42)" | isol8 run --runtime node

# Secrets (masked as *** in output)
isol8 run -e "import os; print(os.environ['KEY'])" --runtime python --secret KEY=sk-1234

# Remote execution
isol8 run script.py --host http://server:3000 --key my-api-key

# AI coding agent (sandboxed)
isol8 run -e "refactor this to use async/await" --runtime agent \
  --net filtered --allow "api.anthropic.com" \
  --secret "ANTHROPIC_API_KEY=sk-..." \
  --files ./my-project --workdir /sandbox/my-project --timeout 600000

# Cleanup orphaned containers
isol8 cleanup               # Interactive (prompts for confirmation)
isol8 cleanup --force       # Skip confirmation

Library API (Quick Reference)

For full library documentation, see Library Overview.

DockerIsol8
import { DockerIsol8 } from "isol8";

const isol8 = new DockerIsol8({
  mode: "ephemeral",     // or "persistent"
  network: "none",       // or "host" or "filtered"
  memoryLimit: "512m",
  cpuLimit: 1.0,
  timeoutMs: 30000,
  secrets: {},           // values masked in output
  persist: false,        // keep container after execution for debugging
  debug: false,          // enable internal debug logging
});

await isol8.start();

const result = await isol8.execute({
  code: 'print("hello")',
  runtime: "python",
  installPackages: ["numpy"],  // optional
  setupScript: "echo setup",   // optional — runs before main code
  workdir: "/sandbox/project",  // optional — defaults to /sandbox
});

console.log(result.stdout);    // captured output
console.log(result.exitCode);  // 0 = success
console.log(result.durationMs);

await isol8.stop();


Full options reference: Execution Options

RemoteIsol8
import { RemoteIsol8 } from "isol8";

const isol8 = new RemoteIsol8(
  { host: "http://localhost:3000", apiKey: "secret" },
  { network: "none" }
);
await isol8.start();
const result = await isol8.execute({ code: "print(1)", runtime: "python" });
await isol8.stop();

Streaming
for await (const event of isol8.executeStream({
  code: 'for i in range(5): print(i)',
  runtime: "python",
})) {
  if (event.type === "stdout") process.stdout.write(event.data);
  if (event.type === "exit") console.log("Exit code:", event.data);
}


Full streaming docs: Streaming

File I/O (Persistent Mode)
await isol8.putFile("/sandbox/data.csv", "col1,col2\n1,2");
const buf = await isol8.getFile("/sandbox/output.txt");


Full file I/O docs: File I/O

HTTP Server API

Full endpoint reference: Server Endpoints

Method	Path	Auth	Description
GET	/health	No	Health check
POST	/execute	Yes	Execute code, return result
POST	/execute/stream	Yes	Execute code, SSE stream
POST	/file	Yes	Upload file (base64)
GET	/file	Yes	Download file (base64)
DELETE	/session/:id	Yes	Destroy persistent session
Configuration

Config is loaded from (first found): ./isol8.config.json or ~/.isol8/config.json. Partial configs are deep-merged with defaults.

Full configuration reference: Configuration

Security Defaults
Layer	Default
Filesystem	Read-only root, /sandbox tmpfs 512MB (exec allowed), /tmp tmpfs 256MB (noexec)
User isolation	Non-root sandbox user (uid 100), processes killed between pool reuses
Processes	PID limit 64, no-new-privileges
Resources	1 CPU, 512MB memory, 30s timeout
Network	Disabled (none), iptables enforcement in filtered mode
Output	Truncated at 1MB, secrets masked
Seccomp	"safety" (blocks mount, swap, ptrace, etc.)

Container Filesystem:

/sandbox (512MB): Working directory, packages installed here, execution allowed for .so files
/tmp (256MB): Temporary files, no execution allowed for security

Full security model: Security

Troubleshooting
"Docker not running": Run isol8 setup to check.
Timeouts: Increase --timeout. Process is killed on timeout.
OOM Killed: Increase --memory.
"No space left on device": Increase --sandbox-size (default 512MB) or --tmp-size (default 256MB).
"Operation not permitted" with numpy/packages: Packages need --sandbox-size large enough for installation (512MB+ recommended).
.ts files running with Bun instead of Deno: .ts defaults to Bun. Use --runtime deno or .mts extension.
Serve command failing: Ensure the server binary can be downloaded from GitHub Releases. Use isol8 serve --update to force a fresh download. Use isol8 serve --debug to see detailed server logs. For listen port selection, precedence is --port > ISOL8_PORT > PORT > 3000; if the port is busy, serve can prompt for another port or auto-pick an available one.
Agent runtime requires filtered network: The agent runtime enforces --net filtered with at least one --allow entry. Pass --allow "api.anthropic.com" (or your LLM provider's domain).
Agent runtime needs API key: Pass the LLM provider key via --secret "ANTHROPIC_API_KEY=sk-...". The value is masked in output.
Agent runtime out of space: The agent runtime defaults to --sandbox-size 2g. For large repos, increase with --sandbox-size 4g.
Weekly Installs
26
Repository
illusion47586/isol8
GitHub Stars
4
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykFail