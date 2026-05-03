---
title: gh-aw-mcp-gateway
url: https://skills.sh/hack23/riksdagsmonitor/gh-aw-mcp-gateway
---

# gh-aw-mcp-gateway

skills/hack23/riksdagsmonitor/gh-aw-mcp-gateway
gh-aw-mcp-gateway
Installation
$ npx skills add https://github.com/hack23/riksdagsmonitor --skill gh-aw-mcp-gateway
SKILL.md
🌐 GitHub Agentic Workflows - MCP Gateway Skill
📋 Purpose

Master the MCP Gateway for GitHub Agentic Workflows - the foundational infrastructure component that enables AI agents to access Model Context Protocol (MCP) servers safely and efficiently. This skill provides comprehensive expertise in configuring, deploying, and operating the MCP Gateway for production AI automation.

🎯 Core Concept
What Is the MCP Gateway?

The MCP Gateway is a proxy server that routes Model Context Protocol (MCP) requests from AI agents to backend MCP servers. It provides centralized configuration, Docker container management, and secure access to multiple MCP servers through a unified HTTP API.

Key Principles:

🔒 Secure Routing: Proxies MCP requests with authentication and validation
🐳 Docker Integration: Launches MCP servers as isolated Docker containers
📡 Protocol Translation: Handles stdio ↔ HTTP transport for MCP servers
🔌 Multi-Server: Routes to multiple backend MCP servers (GitHub, Serena, custom)
📊 Observable: Comprehensive logging and per-server log files
🛡️ Containerized: Runs in GitHub Actions with security enforcement

Architecture:

┌──────────────────────────────────────────────────────────┐
│                    GitHub Actions Workflow                │
│                                                            │
│  ┌───────────────────────────────────────────────────┐  │
│  │                    AI Agent                        │  │
│  │  - Reads: MCP tools (GitHub, Serena, etc.)       │  │
│  │  - Calls: tools/list, tools/call                  │  │
│  │  - HTTP requests to MCP Gateway                   │  │
│  └──────────────┬────────────────────────────────────┘  │
│                 │                                         │
│                 ▼ HTTP (JSON-RPC)                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │              MCP Gateway (awmg)                   │  │
│  │  - Routes: /mcp/{serverID} (routed mode)        │  │
│  │  - Auth: API key validation (MCP 7.1)           │  │
│  │  - Spawns: Docker containers                     │  │
│  │  - Logs: Per-server + unified logs               │  │
│  └──┬───────────┬────────────────┬──────────────────┘  │
│     │ stdio     │ stdio          │ stdio                │
│     ▼           ▼                ▼                       │
│  ┌─────┐   ┌─────────┐   ┌──────────────┐             │
│  │GitHub│   │ Serena  │   │  Custom MCP  │             │
│  │ MCP │   │   MCP   │   │    Server    │             │
│  └─────┘   └─────────┘   └──────────────┘             │
│  (Container)  (Container)    (Container)                │
└──────────────────────────────────────────────────────────┘

🏗️ MCP Gateway Core

A gateway for Model Context Protocol (MCP) servers.

This gateway is used with GitHub Agentic Workflows via the sandbox.mcp configuration to provide MCP server access to AI agents running in sandboxed environments.

📖 Full Configuration Specification - Complete reference for all configuration options and validation rules.

Features
Configuration Modes: Supports both TOML files and JSON stdin configuration
Spec-Compliant Validation: Fail-fast validation with detailed error messages
Variable Expansion: Environment variable substitution with ${VAR_NAME} syntax
Type Normalization: Automatic conversion of legacy "local" type to "stdio"
Schema Normalization: Automatic fixing of malformed JSON schemas from backend MCP servers
Adds missing properties field to object schemas
Prevents downstream validation errors
Transparent to both backends and clients
Routing Modes:
Routed: Each backend server accessible at /mcp/{serverID}
Unified: Single endpoint /mcp that routes to configured servers
Docker Support: Launch backend MCP servers as Docker containers
Stdio Transport: JSON-RPC 2.0 over stdin/stdout for MCP communication
Container Detection: Automatic detection of containerized environments with security warnings
Enhanced Debugging: Detailed error context and troubleshooting suggestions for command failures
Per-ServerID Logs: Separate log files for each backend MCP server ({serverID}.log) for easier troubleshooting
Getting Started

For detailed setup instructions, building from source, and local development, see CONTRIBUTING.md.

Quick Start with Docker

Pull the Docker image (when available):

docker pull ghcr.io/github/gh-aw-mcpg:latest


Create a configuration file (config.json):

{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "container": "ghcr.io/github/github-mcp-server:latest",
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": ""
      }
    }
  }
}


Run the container:

docker run --rm -i \
  -e MCP_GATEWAY_PORT=8000 \
  -e MCP_GATEWAY_DOMAIN=localhost \
  -e MCP_GATEWAY_API_KEY=your-secret-key \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /path/to/logs:/tmp/gh-aw/mcp-logs \
  -p 8000:8000 \
  ghcr.io/github/gh-aw-mcpg:latest < config.json


Required flags:

-i: Enables stdin for passing JSON configuration
-e MCP_GATEWAY_*: Required environment variables
-v /var/run/docker.sock: Required for spawning backend MCP servers
-v /path/to/logs:/tmp/gh-aw/mcp-logs: Mount for persistent gateway logs (or use -e MCP_GATEWAY_LOG_DIR=/custom/path with matching volume mount)
mcp-gateway.log: Unified log with all messages
{serverID}.log: Per-server logs for easier troubleshooting
gateway.md: Markdown-formatted logs for GitHub workflow previews
rpc-messages.jsonl: Machine-readable RPC message logs
tools.json: Available tools from all backend MCP servers
-p 8000:8000: Port mapping must match MCP_GATEWAY_PORT

MCPG will start in routed mode on http://0.0.0.0:8000 (using MCP_GATEWAY_PORT), proxying MCP requests to your configured backend servers.

Configuration

MCP Gateway supports two configuration formats:

TOML format - Use with --config flag for file-based configuration
JSON stdin format - Use with --config-stdin flag for dynamic configuration
TOML Format (config.toml)

TOML configuration uses command and args fields directly for maximum flexibility:

[servers]

[servers.github]
command = "docker"
args = ["run", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "-i", "ghcr.io/github/github-mcp-server:latest"]

[servers.filesystem]
command = "node"
args = ["/path/to/filesystem-server.js"]


Note: In TOML format, you specify the command and args directly. This allows you to use any command (docker, node, python, etc.).

JSON Stdin Format

For the complete JSON configuration specification with all validation rules, see the MCP Gateway Configuration Reference.

{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "container": "ghcr.io/github/github-mcp-server:latest",
      "entrypoint": "/custom/entrypoint.sh",
      "entrypointArgs": ["--verbose"],
      "mounts": [
        "/host/config:/app/config:ro",
        "/host/data:/app/data:rw"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "",
        "EXPANDED_VAR": "${MY_HOME}/config"
      }
    }
  },
  "gateway": {
    "port": 8080,
    "apiKey": "your-api-key",
    "domain": "localhost",
    "startupTimeout": 30,
    "toolTimeout": 60,
    "payloadDir": "/tmp/jq-payloads"
  }
}

Server Configuration Fields

type (optional): Server transport type

"stdio" - Standard input/output transport (default)
"http" - HTTP transport (fully supported)
"local" - Alias for "stdio" (backward compatibility)

container (required for stdio in JSON format): Docker container image (e.g., "ghcr.io/github/github-mcp-server:latest")

Automatically wraps as docker run --rm -i <container>
Note: The command field is NOT supported in JSON stdin format (stdio servers must use container instead)
TOML format uses command and args fields directly

entrypoint (optional): Custom entrypoint for the container

Overrides the default container entrypoint
Applied as --entrypoint flag to Docker

entrypointArgs (optional): Arguments passed to container entrypoint

Array of strings passed after the container image

mounts (optional): Volume mounts for the container

Array of strings in format "source:dest:mode"
source - Host path to mount (can use environment variables with ${VAR} syntax)
dest - Container path where the volume is mounted
mode - Either "ro" (read-only) or "rw" (read-write)
Example: ["/host/config:/app/config:ro", "/host/data:/app/data:rw"]

env (optional): Environment variables

Set to "" (empty string) for passthrough from host environment
Set to "value" for explicit value
Use "${VAR_NAME}" for environment variable expansion (fails if undefined)

url (required for http): HTTP endpoint URL for type: "http" servers

Validation Rules:

JSON stdin format:
Stdio servers must specify container (required)
HTTP servers must specify url (required)
The command field is not supported - stdio servers must use container
TOML format:
Uses command and args fields directly (e.g., command = "docker")
Common rules (both formats):
Empty/"local" type automatically normalized to "stdio"
Variable expansion with ${VAR_NAME} fails fast on undefined variables
All validation errors include JSONPath and helpful suggestions
Mount specifications must follow "source:dest:mode" format
mode must be either "ro" or "rw"
Both source and destination paths are required (cannot be empty)

See Configuration Specification for complete validation rules.

Gateway Configuration Fields (Reserved)
port (optional): Gateway HTTP port (default: from --listen flag)
Valid range: 1-65535
apiKey (optional): API key for authentication
domain (optional): Domain name for the gateway
Allowed values: "localhost", "host.docker.internal"
startupTimeout (optional): Seconds to wait for backend startup (default: 60)
Must be positive integer
toolTimeout (optional): Seconds to wait for tool execution (default: 120)
Must be positive integer
payloadDir (optional): Directory for storing large payload files (default: /tmp/jq-payloads)
Payloads are organized by session: {payloadDir}/{sessionID}/{queryID}/payload.json

Note: Gateway configuration fields are validated and parsed but not yet fully implemented.

Configuration Alternatives:

payloadSizeThreshold is not supported in JSON stdin format. Use:
CLI flag: --payload-size-threshold <bytes> (default: 10240)
Environment variable: MCP_GATEWAY_PAYLOAD_SIZE_THRESHOLD=<bytes>
Payloads larger than this threshold are stored to disk and return metadata
Payloads smaller than or equal to this threshold are returned inline

Environment Variable Features:

Passthrough: Set value to empty string ("") to pass through from host
Expansion: Use ${VAR_NAME} syntax for dynamic substitution (fails if undefined)
Configuration Validation and Error Handling

MCP Gateway provides detailed error messages and validation to help catch configuration issues early:

Parse Errors with Precise Location

When there's a syntax error in your TOML configuration, the gateway reports the exact line and column:

$ awmg --config config.toml
Error: failed to parse TOML at line 2, column 6: expected '.' or '=', but got '3' instead


This helps you quickly identify and fix syntax issues.

Unknown Key Detection (Typo Detection)

The gateway detects and warns about unknown configuration keys, helping catch typos and deprecated options:

[gateway]
prot = 3000              # Typo: should be 'port'
startup_timout = 30      # Typo: should be 'startup_timeout'


When you run the gateway with these typos, you'll see warnings in the log file:

[2026-02-07T17:46:51Z] [WARN] [config] Unknown configuration key 'gateway.prot' - check for typos or deprecated options
[2026-02-07T17:46:51Z] [WARN] [config] Unknown configuration key 'gateway.startup_timout' - check for typos or deprecated options


The gateway will use default values for unrecognized keys, so it will still start, but the warnings help you identify and fix configuration issues.

Memory-Efficient Parsing

The gateway uses streaming parsing for configuration files, making it efficient even with large configuration files containing many servers.

Best Practices
Check logs for warnings: After starting the gateway, check the log file for any warnings about unknown keys
Use precise error messages: When you see a parse error, the line and column numbers point exactly to the problem
Validate configuration: Test your configuration changes by running the gateway and checking for warnings
Keep configuration clean: Remove any deprecated or unused configuration options
Usage
MCPG is a proxy server for Model Context Protocol (MCP) servers.
It provides routing, aggregation, and management of multiple MCP backend servers.

Usage:
  awmg [flags]
  awmg [command]

Available Commands:
  completion  Generate completion script
  help        Help about any command

Flags:
  -c, --config string                Path to config file
      --config-stdin                 Read MCP server configuration from stdin (JSON format). When enabled, overrides --config
      --env string                   Path to .env file to load environment variables
  -h, --help                         help for awmg
  -l, --listen string                HTTP server listen address (default "127.0.0.1:3000")
      --log-dir string               Directory for log files (falls back to stdout if directory cannot be created) (default "/tmp/gh-aw/mcp-logs")
      --payload-dir string           Directory for storing large payload files (segmented by session ID) (default "/tmp/jq-payloads")
      --payload-size-threshold int   Size threshold (in bytes) for storing payloads to disk. Payloads larger than this are stored, smaller ones returned inline (default 10240)
      --routed                       Run in routed mode (each backend at /mcp/<server>)
      --sequential-launch   Launch MCP servers sequentially during startup (parallel launch is default)
      --unified             Run in unified mode (all backends at /mcp)
      --validate-env        Validate execution environment (Docker, env vars) before starting
  -v, --verbose count       Increase verbosity level (use -v for info, -vv for debug, -vvv for trace)
      --version             version for awmg

Use "awmg [command] --help" for more information about a command.

Environment Variables

The following environment variables are used by the MCP Gateway:

Required for Production (Containerized Mode)

When running in a container (run_containerized.sh), these variables must be set:

Variable	Description	Example
MCP_GATEWAY_PORT	The port the gateway listens on (used for --listen address)	8080
MCP_GATEWAY_DOMAIN	The domain name for the gateway	localhost
MCP_GATEWAY_API_KEY	API key for authentication	your-secret-key
Optional (Non-Containerized Mode)

When running locally (run.sh), these variables are optional (warnings shown if missing):

Variable	Description	Default
MCP_GATEWAY_PORT	Gateway listening port	8000
MCP_GATEWAY_DOMAIN	Gateway domain	localhost
MCP_GATEWAY_API_KEY	API authentication key	(disabled)
MCP_GATEWAY_LOG_DIR	Log file directory (sets default for --log-dir flag)	/tmp/gh-aw/mcp-logs
MCP_GATEWAY_PAYLOAD_DIR	Large payload storage directory (sets default for --payload-dir flag)	/tmp/jq-payloads
MCP_GATEWAY_PAYLOAD_SIZE_THRESHOLD	Size threshold in bytes for payload storage (sets default for --payload-size-threshold flag)	10240
DEBUG	Enable debug logging with pattern matching (e.g., *, server:*,launcher:*)	(disabled)
DEBUG_COLORS	Control colored debug output (0 to disable, auto-disabled when piping)	Auto-detect

Note: The HOST and MODE environment variables are not used by the gateway application. Use the --listen flag to set the bind address (default: 127.0.0.1:3000) and the --routed or --unified flags to set the gateway mode.

Docker Configuration
Variable	Description	Default
DOCKER_HOST	Docker daemon socket path	/var/run/docker.sock
DOCKER_API_VERSION	Docker API version (set by helper scripts, Docker client auto-negotiates)	Set by run.sh based on architecture
Containerized Mode
Running in Docker

For production deployments in Docker containers, use run_containerized.sh which:

Validates the container environment before starting
Requires all essential environment variables
Requires stdin input (-i flag) for JSON configuration
Validates Docker socket accessibility
Validates port mapping configuration
# Correct way to run the gateway in a container:
docker run -i \
  -e MCP_GATEWAY_PORT=8080 \
  -e MCP_GATEWAY_DOMAIN=localhost \
  -e MCP_GATEWAY_API_KEY=your-key \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /path/to/logs:/tmp/gh-aw/mcp-logs \
  -p 8080:8080 \
  ghcr.io/github/gh-aw-mcpg:latest < config.json


Important flags:

-i: Required for passing configuration via stdin
-v /var/run/docker.sock:/var/run/docker.sock: Required for spawning backend MCP servers
-v /path/to/logs:/tmp/gh-aw/mcp-logs: Optional but recommended for persistent logs (path matches default or MCP_GATEWAY_LOG_DIR)
-p <host>:<container>: Port mapping must match MCP_GATEWAY_PORT
Validation Checks

The containerized startup script performs these validations:

Check	Description	Action on Failure
Docker Socket	Verifies Docker daemon is accessible	Exit with error
Environment Variables	Checks required env vars are set	Exit with error
Port Mapping	Verifies container port is mapped to host	Exit with error
Stdin Interactive	Ensures -i flag was used	Exit with error
Log Directory Mount	Verifies log directory is mounted to host	Warning (logs won't persist)
Non-Containerized Mode

For local development, use run.sh which:

Warns about missing environment variables (but continues)
Provides default configuration if no config file specified
Auto-detects containerized environments and redirects to run_containerized.sh
# Run locally with defaults:
./run.sh

# Run with custom config:
CONFIG=my-config.toml ./run.sh

# Run with environment variables:
MCP_GATEWAY_PORT=3000 ./run.sh

Logging

MCPG provides comprehensive logging of all gateway operations to help diagnose issues and monitor activity.

Log Files

The gateway creates multiple log files for different purposes:

mcp-gateway.log - Unified log with all gateway messages
{serverID}.log - Per-server logs (e.g., github.log, slack.log) for easier troubleshooting of specific backend servers
gateway.md - Markdown-formatted logs for GitHub workflow previews
rpc-messages.jsonl - Machine-readable JSONL format for RPC message analysis
tools.json - Available tools from all backend MCP servers (mapping server IDs to their tool names and descriptions)
Log File Location

By default, logs are written to /tmp/gh-aw/mcp-logs/. This location can be configured using either:

MCP_GATEWAY_LOG_DIR environment variable - Sets the default log directory
--log-dir flag - Overrides the environment variable and default

The precedence order is: --log-dir flag → MCP_GATEWAY_LOG_DIR env var → default (/tmp/gh-aw/mcp-logs)

Per-ServerID Logs

Each backend MCP server gets its own log file (e.g., github.log, slack.log) in addition to the unified mcp-gateway.log. This makes it much easier to:

Debug issues with a specific backend server
View all activity for one server without filtering
Identify which server is causing problems
Troubleshoot server-specific configuration issues

Example log directory structure:

/tmp/gh-aw/mcp-logs/
├── mcp-gateway.log    # All messages
├── github.log         # Only GitHub server logs
├── slack.log          # Only Slack server logs
├── notion.log         # Only Notion server logs
├── gateway.md         # Markdown format
├── rpc-messages.jsonl # RPC messages
└── tools.json         # Available tools


Using the environment variable:

export MCP_GATEWAY_LOG_DIR=/var/log/mcp-gateway
./awmg --config config.toml


Using the command-line flag:

./awmg --config config.toml --log-dir /var/log/mcp-gateway


Important for containerized mode: Mount the log directory to persist logs outside the container:

docker run -v /path/on/host:/tmp/gh-aw/mcp-logs ...


If the log directory cannot be created or accessed, MCPG automatically falls back to logging to stdout.

What Gets Logged

MCPG logs all important gateway events including:

Startup and Shutdown: Gateway initialization, configuration loading, and graceful shutdown
MCP Client Interactions: Client connection events, request/response details, session management
Backend Server Interactions: Backend server launches, connection establishment, communication events
Authentication Events: Successful authentications and authentication failures (missing/invalid tokens)
Connectivity Errors: Connection failures, timeouts, protocol errors, and command execution issues
Debug Information: Optional detailed debugging via the DEBUG environment variable
Log Format

Each log entry includes:

Timestamp (RFC3339 format)
Log Level (INFO, WARN, ERROR, DEBUG)
Category (startup, client, backend, auth, shutdown)
Message with contextual details

Example log entries:

[2026-01-08T23:00:00Z] [INFO] [startup] Starting MCPG with config: config.toml, listen: 127.0.0.1:3000, log-dir: /tmp/gh-aw/mcp-logs
[2026-01-08T23:00:01Z] [INFO] [backend] Launching MCP backend server: github, command=docker, args=[run --rm -i ghcr.io/github/github-mcp-server:latest]
[2026-01-08T23:00:02Z] [INFO] [client] New MCP client connection, remote=127.0.0.1:54321, method=POST, path=/mcp/github, backend=github, session=abc123
[2026-01-08T23:00:03Z] [ERROR] [auth] Authentication failed: invalid API key, remote=127.0.0.1:54322, path=/mcp/github

Debug Logging

For development and troubleshooting, enable debug logging using the DEBUG environment variable:

# Enable all debug logs
DEBUG=* ./awmg --config config.toml

# Enable specific categories
DEBUG=server:*,launcher:* ./awmg --config config.toml


Debug logs are written to stderr and follow the same pattern-matching syntax as the file logger.

API Endpoints
Routed Mode (default)
POST /mcp/{serverID} - Send JSON-RPC request to specific server
Example: POST /mcp/github with body {"jsonrpc": "2.0", "method": "tools/list", "id": 1}
Unified Mode
POST /mcp - Send JSON-RPC request (routed to first configured server)
Health Check
GET /health - Returns OK
MCP Methods

Supported JSON-RPC 2.0 methods:

tools/list - List available tools
tools/call - Call a tool with parameters
Any other MCP method (forwarded as-is)
Security Features
Authentication

MCPG implements MCP specification 7.1 for API key authentication.

Authentication Header Format:

Per MCP spec 7.1: Authorization header MUST contain the API key directly
Format: Authorization: <api-key> (plain API key, NOT Bearer scheme)
Example: Authorization: my-secret-api-key-123

Configuration:

Set via MCP_GATEWAY_API_KEY environment variable
When configured, all endpoints except /health require authentication
When not configured, authentication is disabled

Implementation:

The internal/auth package provides centralized authentication logic
auth.ParseAuthHeader() - Parses Authorization headers per MCP spec 7.1
auth.ValidateAPIKey() - Validates provided API keys
Backward compatibility for Bearer tokens is maintained

Example Request:

curl -X POST http://localhost:8000/mcp/github \
  -H "Authorization: my-api-key" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "method": "tools/list", "id": 1}'

Enhanced Error Debugging

Command failures now include extensive debugging information:

Full command, arguments, and environment variables
Context-specific troubleshooting suggestions:
Docker daemon connectivity checks
Container image availability
Network connectivity issues
MCP protocol compatibility checks
Architecture

This Go port focuses on core MCP proxy functionality with optional security features:

Core Features (Enabled)
✅ TOML and JSON stdin configuration with spec-compliant validation
✅ Environment variable expansion (${VAR_NAME}) with fail-fast behavior
✅ Stdio transport for backend servers (containerized execution only)
✅ Docker container launching
✅ Routed and unified modes
✅ Basic request/response proxying
✅ Enhanced error debugging and troubleshooting
MCP Server Compatibility

The gateway supports MCP servers via stdio transport using Docker containers. All properly configured MCP servers work through direct stdio connections.

Test Results

Both GitHub MCP and Serena MCP servers pass comprehensive test suites including gateway tests:

Server	Transport	Direct Tests	Gateway Tests	Status
GitHub MCP	Stdio (Docker)	✅ All passed	✅ All passed	Production ready
Serena MCP	Stdio (Docker)	✅ 68/68 passed (100%)	✅ All passed	Production ready

Configuration:

# Both servers use stdio transport via Docker containers
docker run -i ghcr.io/github/github-mcp-server          # GitHub MCP
docker run -i ghcr.io/github/serena-mcp-server     # Serena MCP

Using MCP Servers with the Gateway

Direct Connection (Recommended): Configure MCP servers to connect directly via stdio transport for optimal performance and full feature support:

{
  "mcpServers": {
    "serena": {
      "type": "stdio",
      "container": "ghcr.io/github/serena-mcp-server:latest"
    },
    "github": {
      "type": "stdio",
      "container": "ghcr.io/github/github-mcp-server:latest"
    }
  }
}


Architecture Considerations:

The gateway manages backend MCP servers using stdio transport via Docker containers
Session connection pooling ensures efficient resource usage
Backend processes are reused across multiple requests per session
All MCP protocol features are fully supported
Test Coverage

Serena MCP Server Testing:

✅ Direct Connection Tests: 68/68 tests passed (100%)
✅ Gateway Tests: All tests passed via make test-serena-gateway
✅ Multi-language support (Go, Java, JavaScript, Python)
✅ File operations, symbol operations, memory management
✅ Error handling and protocol compliance
✅ See SERENA_TEST_RESULTS.md for detailed results

GitHub MCP Server Testing:

✅ Full test suite validation (direct and gateway)
✅ Repository operations, issue management, search functionality
✅ Production deployment validated
Contributing

For development setup, build instructions, testing guidelines, and project architecture details, see CONTRIBUTING.md.

License

MIT License

📖 References
Official Documentation
MCP Gateway Configuration Reference - Complete configuration specification
GitHub Agentic Workflows - Main repository
Model Context Protocol Specification - MCP protocol spec
MCP Gateway Repository - Gateway source code
Related Skills
gh-aw-safe-outputs - Safe outputs pattern for controlled AI writes
gh-aw-firewall - Network firewall for Agentic Workflows
github-agentic-workflows - Complete GitHub Agentic Workflows guide
Docker Resources
Docker Run Reference - Docker command reference
Docker Socket Security - Docker security best practices
Security
Agentic Workflows Security Model - Security architecture
MCP Authentication - MCP 7.1 auth spec
🎓 Learning Path
Beginner (Weeks 1-2)
Understand MCP protocol basics
Configure single backend (GitHub MCP)
Test with TOML configuration locally
Learn routed vs unified modes
Enable basic authentication
Intermediate (Weeks 3-4)
Multi-server configuration
Docker volume mounts and environment variables
Production deployment with JSON stdin
Log analysis and troubleshooting
GitHub Actions integration
Advanced (Weeks 5-8)
Custom MCP server development
HTTP backend integration
Advanced debugging techniques
Performance optimization
Security hardening
Production monitoring

Last Updated: 2026-02-16
Version: 1.0.0
Maintained by: Hack23 AB
License: MIT

🔐 Advanced Security Topics
Security Model (GitHub Agentic Workflows)

The MCP Gateway operates as a Layer 1 trusted component in the GitHub Agentic Workflows security model.

Threat Model

GitHub Agentic Workflows considers an adversary that may compromise untrusted user-level components (containers) and cause them to behave arbitrarily within granted privileges. The adversary may attempt to:

Access or corrupt memory or state of other components
Communicate over unintended channels
Abuse legitimate channels to perform unintended actions
Confuse higher-level control logic by deviating from expected workflows

Assumptions:

Adversary does NOT compromise hardware or cryptographic primitives
Side-channel and covert-channel attacks are out of scope
Layer 1: Substrate-Level Trust

Trusted components:

GitHub Actions runner VM
Hardware (CPU, MMU)
Kernel and container runtime
Network firewall (configures connectivity via iptables)
MCP Gateway (configures and spawns isolated containers)

Security guarantees:

Memory isolation between components
CPU and resource isolation
Mediation of privileged operations and system calls
Explicit, kernel-enforced communication boundaries

These guarantees hold even if untrusted user-level components are fully compromised.

Trust violations require:

Vulnerabilities in firewall or MCP Gateway
Container runtime exploits
Kernel, hypervisor, or hardware compromises

If Layer 1 fails, higher-level security guarantees may not hold.

Layer 2: Configuration-Level Trust

Trusted artifacts:

Action steps
Network firewall policies
MCP server configurations
Toolchains that interpret configurations

Configuration controls:

Which components are loaded
How components are connected
Which communication channels are permitted
What component privileges are assigned

Authentication tokens:

Agent API keys
GitHub access tokens
Treated as imported capabilities that bound components' external effects
Distribution controlled declaratively

Security violations arise from:

Misconfigurations
Overly permissive specifications
Limitations of declarative model

This layer defines what components exist and how they communicate, but NOT how they use those channels over time.

Layer 3: Plan-Level Trust

Trusted compiler decomposes workflow into stages.

For each stage, the plan specifies:

Which components are active and their permissions
Data produced by the stage
How that data may be consumed by subsequent stages

Key instantiation: SafeOutputs subsystem

Agent can interact with read-only MCP servers (e.g., GitHub MCP server)
Externalized writes (creating PRs) are buffered as artifacts by SafeOutputs
When agent finishes, buffered artifacts processed by deterministic filters
Checks include: structural constraints, policy enforcement, automated sanitization
Filtered artifacts passed to subsequent stage for externalization

Security violations at planning layer:

Incorrect plan construction
Incomplete or overly permissive stage definitions
Errors in enforcement of plan transitions

This layer limits blast radius of compromised component to:

The stage in which it is active
Its influence on artifacts passed to next stage
🧪 MCP Server Compatibility
Verified MCP Servers

The MCP Gateway supports MCP servers via stdio transport using Docker containers. All properly configured MCP servers work with the gateway.

GitHub MCP Server

Transport: Stdio (Docker)
Status: ✅ Production ready
Direct Tests: ✅ All passed
Gateway Tests: ✅ All passed

Configuration (JSON):

{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "container": "ghcr.io/github/github-mcp-server:latest",
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": ""
      }
    }
  }
}


Configuration (TOML):

[servers.github]
command = "docker"
args = ["run", "--rm", "-i", "ghcr.io/github/github-mcp-server:latest"]

Serena MCP Server

Transport: Stdio (Docker)
Status: ✅ Production ready
Direct Tests: ✅ 68/68 passed (100%)
Gateway Tests: ✅ All passed

Configuration (JSON):

{
  "mcpServers": {
    "serena": {
      "type": "stdio",
      "container": "ghcr.io/github/serena-mcp-server:latest",
      "env": {
        "SERENA_CONFIG": "/path/to/config"
      }
    }
  }
}


Configuration (TOML):

[servers.serena]
command = "docker"
args = ["run", "--rm", "-i", "ghcr.io/github/serena-mcp-server:latest"]

Backend Connection Management

Architecture:

Gateway launches MCP servers as Docker containers
Each session maintains a persistent connection pool
Backend processes are reused across multiple requests
Stdio pipes remain open for the lifetime of the session

Example Flow:

Client Request 1 (session abc):
  → Gateway launches: docker run -i github-mcp-server
  → Stores connection in pool["github"]["abc"]
  → Sends initialize via stdio
  → Returns response

Client Request 2 (session abc):
  → Gateway retrieves existing connection from pool
  → SAME Docker process, SAME stdio connection
  → Sends tools/list via same connection
  → Returns response

Test Results

GitHub MCP Server:

✅ Full test suite validation (direct and gateway)
✅ Repository operations tested
✅ Issue management validated
✅ Production deployment confirmed

Serena MCP Server:

✅ Direct Connection: 68 comprehensive tests (100% pass rate)
✅ Gateway Connection: All integration tests passed
✅ Multi-language support (Go, Java, JavaScript, Python)
✅ All 29 tools tested and validated
✅ File operations, symbol operations, memory management

Key capabilities tested:

File operations (list, read, write)
Symbol operations (find, analyze)
Memory management
Error handling
Protocol compliance
📡 HTTP Backend Support
HTTP Transport

The MCP Gateway supports HTTP backend servers in addition to stdio backends.

Transport types:

stdio - Standard input/output via Docker containers (default)
http - HTTP endpoints (external MCP servers)
Session ID Handling for HTTP Backends
Overview

HTTP MCP servers may require the Mcp-Session-Id header to be present in all requests, including initialization requests like tools/list.

Problem: When the gateway initializes, it calls tools/list on each backend to discover tools. For HTTP backends, these initialization calls were made without a session ID, causing servers that require the header to reject the request.

Solution: The gateway now creates a context with a session ID for all HTTP backend calls:

During initialization: gateway-init-{serverID}
During client requests: Session ID from client's Authorization header
Session ID Flow

Initialization Flow:

Gateway starts up
NewUnified creates the unified server
registerAllTools is called
For each backend, registerToolsFromBackend is called
Context is created with session ID: gateway-init-{serverID}
SendRequestWithServerID(ctx, "tools/list", ...) is called
For HTTP backends, sendHTTPRequest adds Mcp-Session-Id header
HTTP backend receives request with header and responds successfully

Client Request Flow (Routed Mode):

Client sends request to /mcp/{serverID} with Authorization header
Gateway extracts session ID from Authorization header
Session ID is stored in request context
Tool handler is called with context containing session ID
SendRequestWithServerID(ctx, "tools/call", ...) is called
For HTTP backends, sendHTTPRequest adds Mcp-Session-Id header with client's session ID
HTTP backend receives request with client's session ID
Configuration

No configuration changes required. The fix works automatically for all HTTP backends:

TOML:

[servers.my-http-backend]
type = "http"
url = "https://example.com/mcp"


JSON:

{
  "mcpServers": {
    "my-http-backend": {
      "type": "http",
      "url": "https://example.com/mcp"
    }
  }
}

Backward Compatibility

This change is fully backward compatible:

For HTTP backends that don't require the header: They will simply ignore it
For HTTP backends that require the header: They now work correctly
For stdio backends: No change in behavior (they don't use HTTP headers)
Debugging

Enable debug logging to see session ID handling:

DEBUG=mcp:* ./awmg --config config.toml


Log messages:

[mcp:connection] Added Mcp-Session-Id header: gateway-init-safeinputs

📚 Comprehensive Examples
Example 1: Single Backend (GitHub MCP)

Scenario: Local development with GitHub MCP server

TOML Configuration:

[servers.github]
command = "docker"
args = ["run", "--rm", "-i", "ghcr.io/github/github-mcp-server:latest"]

[gateway]
port = 8000
domain = "localhost"
startupTimeout = 30
toolTimeout = 60


Run locally:

export GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token
awmg --config config.toml --listen 127.0.0.1:8000


Test tools/list:

curl -X POST http://localhost:8000/mcp/github \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "method": "tools/list", "id": 1}'


Expected response:

{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "search_code",
        "description": "Search for code across GitHub repositories",
        "inputSchema": { ... }
      },
      {
        "name": "get_file_contents",
        "description": "Get contents of a file from a GitHub repository",
        "inputSchema": { ... }
      }
    ]
  }
}

Example 2: Production Deployment (Multi-Server)

Scenario: Production deployment with GitHub and Serena MCP servers in Docker

JSON Configuration (config.json):

{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "container": "ghcr.io/github/github-mcp-server:latest",
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": ""
      }
    },
    "serena": {
      "type": "stdio",
      "container": "ghcr.io/github/serena-mcp-server:latest",
      "mounts": [
        "${HOME}/workspace:/workspace:rw",
        "${HOME}/.serena:/root/.serena:ro"
      ],
      "env": {
        "SERENA_CONFIG": "${HOME}/.serena/config.json",
        "DEBUG": "false"
      }
    }
  },
  "gateway": {
    "port": 8000,
    "apiKey": "your-production-api-key",
    "domain": "localhost",
    "startupTimeout": 45,
    "toolTimeout": 90,
    "payloadDir": "/var/lib/mcp-payloads"
  }
}


Docker Run:

docker run --rm -i \
  --name mcp-gateway \
  -e MCP_GATEWAY_PORT=8000 \
  -e MCP_GATEWAY_DOMAIN=localhost \
  -e MCP_GATEWAY_API_KEY=your-production-api-key \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=$GITHUB_TOKEN \
  -e HOME=/root \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /var/log/mcp-gateway:/tmp/gh-aw/mcp-logs \
  -v /var/lib/mcp-payloads:/var/lib/mcp-payloads \
  -v $HOME/workspace:/root/workspace \
  -v $HOME/.serena:/root/.serena:ro \
  -p 8000:8000 \
  ghcr.io/github/gh-aw-mcpg:latest < config.json


Test multiple backends:

# GitHub backend
curl -X POST http://localhost:8000/mcp/github \
  -H "Authorization: your-production-api-key" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}'

# Serena backend
curl -X POST http://localhost:8000/mcp/serena \
  -H "Authorization: your-production-api-key" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"list_files","arguments":{"path":"/workspace"}},"id":2}'

Example 3: GitHub Actions Workflow

Scenario: AI agent with MCP Gateway in GitHub Actions

Workflow (.github/workflows/ai-agent.yml):

name: AI Agent with MCP Gateway

on:
  workflow_dispatch:
    inputs:
      task:
        description: 'Task for AI agent'
        required: true
        default: 'Analyze codebase and suggest improvements'

permissions:
  contents: write
  pull-requests: write
  issues: write

jobs:
  run-agent:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      
      - name: Create MCP Gateway configuration
        run: |
          cat > mcp-config.json <<EOF
          {
            "mcpServers": {
              "github": {
                "type": "stdio",
                "container": "ghcr.io/github/github-mcp-server:latest",
                "env": {
                  "GITHUB_PERSONAL_ACCESS_TOKEN": ""
                }
              },
              "serena": {
                "type": "stdio",
                "container": "ghcr.io/github/serena-mcp-server:latest",
                "mounts": [
                  "${{ github.workspace }}:/workspace:rw"
                ],
                "env": {
                  "WORKSPACE": "/workspace"
                }
              }
            },
            "gateway": {
              "port": 8000,
              "apiKey": "${{ secrets.MCP_GATEWAY_API_KEY }}",
              "domain": "localhost",
              "startupTimeout": 60,
              "toolTimeout": 120
            }
          }
          EOF
      
      - name: Start MCP Gateway
        run: |
          docker run -d --name mcp-gateway \
            -e MCP_GATEWAY_PORT=8000 \
            -e MCP_GATEWAY_DOMAIN=localhost \
            -e MCP_GATEWAY_API_KEY=${{ secrets.MCP_GATEWAY_API_KEY }} \
            -e GITHUB_PERSONAL_ACCESS_TOKEN=${{ secrets.GITHUB_TOKEN }} \
            -v /var/run/docker.sock:/var/run/docker.sock \
            -v ${{ github.workspace }}:/workspace \
            -v ${{ github.workspace }}/logs:/tmp/gh-aw/mcp-logs \
            -p 8000:8000 \
            ghcr.io/github/gh-aw-mcpg:latest < mcp-config.json
      
      - name: Wait for gateway to be ready
        run: |
          echo "Waiting for MCP Gateway to start..."
          timeout 60 bash -c 'until curl -f http://localhost:8000/health; do sleep 2; done'
          echo "MCP Gateway is ready!"
      
      - name: Verify MCP servers
        run: |
          echo "Testing GitHub MCP server..."
          curl -X POST http://localhost:8000/mcp/github \
            -H "Authorization: ${{ secrets.MCP_GATEWAY_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d '{"jsonrpc":"2.0","method":"tools/list","id":1}' | jq .
          
          echo "Testing Serena MCP server..."
          curl -X POST http://localhost:8000/mcp/serena \
            -H "Authorization: ${{ secrets.MCP_GATEWAY_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d '{"jsonrpc":"2.0","method":"tools/list","id":2}' | jq .
      
      - name: Run AI agent
        env:
          MCP_GATEWAY_URL: http://localhost:8000
          MCP_GATEWAY_API_KEY: ${{ secrets.MCP_GATEWAY_API_KEY }}
          TASK: ${{ github.event.inputs.task }}
        run: |
          # Run your AI agent here
          # Agent should call MCP Gateway at $MCP_GATEWAY_URL
          # with Authorization header containing $MCP_GATEWAY_API_KEY
          echo "Running AI agent with task: $TASK"
          # ./run-agent.sh
      
      - name: Stop MCP Gateway
        if: always()
        run: |
          docker stop mcp-gateway || true
          docker rm mcp-gateway || true
      
      - name: Upload MCP Gateway logs
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: mcp-gateway-logs
          path: logs/
          retention-days: 7
      
      - name: Display log summary
        if: always()
        run: |
          echo "## MCP Gateway Log Summary" >> $GITHUB_STEP_SUMMARY
          echo "" >> $GITHUB_STEP_SUMMARY
          if [ -f logs/gateway.md ]; then
            cat logs/gateway.md >> $GITHUB_STEP_SUMMARY
          else
            echo "No gateway logs found" >> $GITHUB_STEP_SUMMARY
          fi

Example 4: Custom MCP Server

Scenario: Custom MCP server with custom entrypoint and environment

JSON Configuration:

{
  "mcpServers": {
    "custom": {
      "type": "stdio",
      "container": "myorg/custom-mcp-server:v1.2.3",
      "entrypoint": "/app/custom-entrypoint.sh",
      "entrypointArgs": ["--verbose", "--log-level=debug"],
      "mounts": [
        "${HOME}/custom-config:/app/config:ro",
        "${HOME}/custom-data:/app/data:rw",
        "/tmp/custom-cache:/app/cache:rw"
      ],
      "env": {
        "API_KEY": "",
        "API_URL": "https://api.example.com",
        "CONFIG_PATH": "/app/config/settings.yaml",
        "DATA_DIR": "/app/data",
        "CACHE_DIR": "/app/cache",
        "LOG_LEVEL": "debug",
        "FEATURE_FLAG_X": "true"
      }
    }
  },
  "gateway": {
    "port": 8000,
    "apiKey": "custom-server-api-key"
  }
}


Docker command (auto-generated by gateway):

docker run --rm -i \
  --entrypoint /app/custom-entrypoint.sh \
  -v /home/user/custom-config:/app/config:ro \
  -v /home/user/custom-data:/app/data:rw \
  -v /tmp/custom-cache:/app/cache:rw \
  -e API_KEY \
  -e API_URL=https://api.example.com \
  -e CONFIG_PATH=/app/config/settings.yaml \
  -e DATA_DIR=/app/data \
  -e CACHE_DIR=/app/cache \
  -e LOG_LEVEL=debug \
  -e FEATURE_FLAG_X=true \
  myorg/custom-mcp-server:v1.2.3 \
  --verbose --log-level=debug

Example 5: HTTP Backend

Scenario: Remote MCP server over HTTP

JSON Configuration:

{
  "mcpServers": {
    "remote-mcp": {
      "type": "http",
      "url": "https://mcp.example.com/api/v1"
    }
  },
  "gateway": {
    "port": 8000,
    "apiKey": "gateway-api-key"
  }
}


Session ID behavior:

Gateway adds Mcp-Session-Id header automatically
Initialization: gateway-init-remote-mcp
Client requests: Session ID from Authorization header

Test:

curl -X POST http://localhost:8000/mcp/remote-mcp \
  -H "Authorization: gateway-api-key" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}'

Example 6: Unified Mode (Simple)

Scenario: Single backend in unified mode for testing

TOML Configuration:

[servers.github]
command = "docker"
args = ["run", "--rm", "-i", "ghcr.io/github/github-mcp-server:latest"]


Run in unified mode:

export GITHUB_PERSONAL_ACCESS_TOKEN=ghp_token
awmg --config config.toml --unified --listen 127.0.0.1:8000


Test (single endpoint):

curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}'

🛠️ Troubleshooting Guide
Issue: Gateway Fails to Start

Symptom:

Error: failed to parse configuration


Possible causes:

Invalid TOML syntax
Invalid JSON in stdin
Missing required fields
Invalid field values

Solutions:

Check TOML syntax:

# Look for line/column in error message
Error: failed to parse TOML at line 5, column 10


Validate JSON:

cat config.json | jq .
# Should output formatted JSON or show syntax error


Enable validation:

awmg --config config.toml --validate-env


Check unknown keys:

# Look for warnings in logs
grep "Unknown configuration key" /tmp/gh-aw/mcp-logs/mcp-gateway.log

Issue: Backend Container Won't Start

Symptom:

Error: Backend server 'github' failed to start
timeout: startup took longer than 60s


Possible causes:

Docker image doesn't exist
Docker socket not accessible
Missing environment variables
Network issues pulling image
Container crashes on startup

Solutions:

Pull image manually:

docker pull ghcr.io/github/github-mcp-server:latest


Check Docker socket:

docker ps
# Should list running containers


Check backend log:

cat /tmp/gh-aw/mcp-logs/github.log
# Look for error messages


Test container directly:

docker run --rm -i ghcr.io/github/github-mcp-server:latest
# Try sending: {"jsonrpc":"2.0","method":"tools/list","id":1}


Check environment variables:

# Ensure all required vars are set
echo $GITHUB_PERSONAL_ACCESS_TOKEN


Increase startup timeout:

{
  "gateway": {
    "startupTimeout": 120
  }
}

Issue: Authentication Failures

Symptom:

401 Unauthorized: Invalid API key


Possible causes:

API key not configured
Wrong Authorization header format
Typo in API key
API key not matching

Solutions:

Check API key is set:

echo $MCP_GATEWAY_API_KEY
# Should output your API key


Verify Authorization header format (NOT Bearer):

# Correct:
curl -H "Authorization: my-api-key" ...

# Wrong:
curl -H "Authorization: Bearer my-api-key" ...


Check gateway logs:

grep "auth" /tmp/gh-aw/mcp-logs/mcp-gateway.log


Test with correct format:

curl -X POST http://localhost:8000/mcp/github \
  -H "Authorization: $(echo $MCP_GATEWAY_API_KEY)" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}'

Issue: Tools Not Discovered

Symptom:

Error: No tools available from backend 'github'


Possible causes:

Backend didn't start successfully
Backend doesn't respond to tools/list
Invalid tools/list response
Network/connection issues

Solutions:

Check tools registry:

cat /tmp/gh-aw/mcp-logs/tools.json
# Should show tools from all backends


Check backend logs:

cat /tmp/gh-aw/mcp-logs/github.log | grep "tools/list"


Test tools/list directly:

curl -X POST http://localhost:8000/mcp/github \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}' | jq .


Enable debug logging:

DEBUG=* awmg --config config.toml


Check for schema errors:

# Gateway auto-fixes malformed schemas
grep "Normalized schema" /tmp/gh-aw/mcp-logs/mcp-gateway.log

Issue: Volume Mount Errors

Symptom:

Error: Invalid mount specification
Expected format: "source:dest:mode"


Possible causes:

Missing mode (ro/rw)
Empty source or dest
Typo in mount specification
Path doesn't exist

Solutions:

Check mount format:

{
  "mounts": [
    "/host/config:/app/config:ro",
    "/host/data:/app/data:rw"
  ]
}


Verify paths exist:

ls -la /host/config
ls -la /host/data


Use environment variable expansion:

{
  "mounts": [
    "${HOME}/.config:/app/config:ro"
  ]
}


Check error message for JSONPath:

Location: mcpServers.github.mounts[0]

Issue: Environment Variable Expansion Fails

Symptom:

Error: Environment variable expansion failed
Variable: HOME
Reason: Environment variable is not defined


Possible causes:

Variable not set before running
Typo in variable name
Variable not exported

Solutions:

Set variable:

export HOME=/root


Check variable is set:

echo $HOME
# Should output value


Use explicit values instead:

{
  "env": {
    "CONFIG_PATH": "/app/config"
  }
}


Check all referenced variables:

grep '\${' config.json
# Shows all variables that need to be defined

Issue: Port Mapping Problems

Symptom:

Error: Port mapping does not match MCP_GATEWAY_PORT
Expected: 8000, Actual: 3000


Possible causes:

-p flag doesn't match MCP_GATEWAY_PORT
Wrong port in configuration
Port already in use

Solutions:

Match -p to MCP_GATEWAY_PORT:

docker run -i \
  -e MCP_GATEWAY_PORT=8000 \
  -p 8000:8000 \
  ghcr.io/github/gh-aw-mcpg:latest < config.json


Check port availability:

netstat -tuln | grep 8000
# Should show no output if port is free


Use different port:

docker run -i \
  -e MCP_GATEWAY_PORT=9000 \
  -p 9000:9000 \
  ghcr.io/github/gh-aw-mcpg:latest < config.json

Issue: Logs Not Persisting

Symptom: Logs disappear when container stops

Possible causes:

Log directory not mounted to host
Wrong mount path
Permission issues

Solutions:

Mount log directory:

docker run -i \
  -v /var/log/mcp-gateway:/tmp/gh-aw/mcp-logs \
  ghcr.io/github/gh-aw-mcpg:latest < config.json


Check mount is correct:

docker inspect mcp-gateway | jq '.[0].Mounts'


Verify logs after container stops:

ls -la /var/log/mcp-gateway/
# Should show log files


Check permissions:

# Ensure user can write to log directory
chmod 777 /var/log/mcp-gateway

Issue: Docker Socket Permission Denied

Symptom:

Error: Cannot connect to Docker daemon
Permission denied while trying to connect to Docker socket


Possible causes:

Docker socket not mounted
Gateway user doesn't have Docker permissions
Docker daemon not running

Solutions:

Mount Docker socket:

docker run -i \
  -v /var/run/docker.sock:/var/run/docker.sock \
  ghcr.io/github/gh-aw-mcpg:latest < config.json


Check Docker is running:

docker ps


Test Docker access:

docker run hello-world

Issue: Slow Tool Execution

Symptom:

Error: Tool execution timeout (exceeded 120s)


Possible causes:

Tool is computationally expensive
Network latency (HTTP backends)
Backend server overloaded
Default timeout too low

Solutions:

Increase tool timeout:

{
  "gateway": {
    "toolTimeout": 300
  }
}


Check backend performance:

# Look for slow tool calls in logs
jq 'select(.duration > 5000)' /tmp/gh-aw/mcp-logs/rpc-messages.jsonl


Monitor backend resources:

docker stats mcp-gateway


Enable debug logging:

DEBUG=mcp:* awmg --config config.toml

🎯 Best Practices & Patterns
Configuration Management

✅ DO:

Use environment-specific configs
# Development
awmg --config config.dev.toml

# Production
docker run -i ghcr.io/github/gh-aw-mcpg:latest < config.prod.json

Validate before deploying
# Check configuration syntax
awmg --config config.toml --validate-env

# Test in dry-run mode
DEBUG=* awmg --config config.toml

Use environment variables for secrets
{
  "env": {
    "API_KEY": "",
    "SECRET_TOKEN": ""
  }
}

Document your configuration
# GitHub MCP server for repository access
[servers.github]
command = "docker"
args = ["run", "--rm", "-i", "ghcr.io/github/github-mcp-server:latest"]

# Startup timeout increased for slow networks
[gateway]
startupTimeout = 90

Version control non-sensitive configs
git add config.toml.template
git add .env.example
# Never commit actual secrets!


❌ DON'T:

Hardcode secrets
{
  "env": {
    "API_KEY": "ghp_actual_secret_key"  // ❌ DON'T DO THIS
  }
}

Use overly permissive mounts
{
  "mounts": [
    "/:/host:rw"  // ❌ Mounts entire filesystem read-write
  ]
}

Ignore configuration warnings
[WARN] Unknown configuration key 'gateway.prot'
// ❌ Fix typos immediately

Skip validation
# ❌ Don't skip this step
awmg --config config.toml  # without --validate-env

Security Hardening

✅ DO:

Always use API keys in production
export MCP_GATEWAY_API_KEY=$(openssl rand -base64 32)

Rotate API keys regularly
# Monthly rotation
./rotate-api-keys.sh

Use read-only mounts for configs
{
  "mounts": [
    "/host/config:/app/config:ro"
  ]
}

Limit backend permissions
{
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": ""
  }
  // Use token with minimal required scopes
}

Monitor authentication failures
# Alert on failed auth attempts
grep "Authentication failed" /tmp/gh-aw/mcp-logs/mcp-gateway.log | \
  tail -n 10 | \
  mail -s "MCP Gateway Auth Failures" admin@example.com

Use specific image tags
{
  "container": "ghcr.io/github/github-mcp-server:v1.2.3"
}


❌ DON'T:

Disable authentication
# ❌ Don't run without API key in production
unset MCP_GATEWAY_API_KEY

Share API keys across environments
# ❌ Use different keys
export DEV_API_KEY=dev-key
export PROD_API_KEY=prod-key

Use :latest tags
{
  "container": "myserver:latest"  // ❌ Not reproducible
}

Grant unnecessary permissions
# ❌ Don't run privileged
docker run --privileged ...

Logging & Monitoring

✅ DO:

Mount logs to persistent storage
docker run -i \
  -v /var/log/mcp-gateway:/tmp/gh-aw/mcp-logs \
  ghcr.io/github/gh-aw-mcpg:latest < config.json

Use per-server logs for debugging
# Debug specific backend
tail -f /tmp/gh-aw/mcp-logs/github.log

Monitor log file sizes
# Rotate logs when > 100MB
find /var/log/mcp-gateway -name "*.log" -size +100M

Enable debug logging for troubleshooting
DEBUG=mcp:*,server:* awmg --config config.toml

Analyze RPC messages
# Find slow tools
jq 'select(.duration > 5000)' /tmp/gh-aw/mcp-logs/rpc-messages.jsonl

# Count by method
jq -r .method /tmp/gh-aw/mcp-logs/rpc-messages.jsonl | sort | uniq -c

Monitor health endpoint
# Kubernetes liveness probe
livenessProbe:
  httpGet:
    path: /health
    port: 8000
  periodSeconds: 10


❌ DON'T:

Ignore log warnings
# ❌ Always investigate warnings
grep WARN /tmp/gh-aw/mcp-logs/mcp-gateway.log

Let logs grow unbounded
# ❌ Implement log rotation
logrotate /etc/logrotate.d/mcp-gateway

Store logs in container
# ❌ Logs lost when container stops
docker run ghcr.io/github/gh-aw-mcpg:latest

Performance Optimization

✅ DO:

Use parallel backend launch (default)
# Backends start simultaneously
awmg --config config.toml

Tune timeouts for your workload
{
  "gateway": {
    "startupTimeout": 30,  // Fast backends
    "toolTimeout": 300      // Slow AI tools
  }
}

Monitor backend startup times
grep "Launching MCP backend" /tmp/gh-aw/mcp-logs/mcp-gateway.log

Use payload threshold wisely
# Store large payloads to disk
export MCP_GATEWAY_PAYLOAD_SIZE_THRESHOLD=10240

Reuse session connections
# Connection pooling happens automatically
# Same session = same backend process


❌ DON'T:

Use sequential launch unnecessarily
# ❌ Slower startup
awmg --config config.toml --sequential-launch

Set timeouts too low
{
  "gateway": {
    "toolTimeout": 5  // ❌ Too aggressive
  }
}

Docker Best Practices

✅ DO:

Clean up containers automatically
docker run --rm -i ...  // Always use --rm

Limit container resources
docker run -i \
  --memory=2g \
  --cpus=2.0 \
  ghcr.io/github/gh-aw-mcpg:latest < config.json

Use health checks
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/health || exit 1

Monitor Docker socket usage
# Check Docker API calls
docker events --filter type=container

Use multi-stage builds
# Build stage
FROM golang:1.21 AS builder
...

# Runtime stage
FROM gcr.io/distroless/base-debian12
COPY --from=builder /app/awmg /awmg


❌ DON'T:

Leave containers running indefinitely
# ❌ Stop containers when done
docker stop mcp-gateway

Ignore container logs
# ❌ Check for errors
docker logs mcp-gateway

Run as root unnecessarily
# ✅ Use non-root user
USER nobody

💡 Tips & Tricks
Quick Commands

Start gateway with defaults:

awmg --config config.toml


Test configuration:

awmg --config config.toml --validate-env


Debug mode:

DEBUG=* awmg --config config.toml -vvv


Health check:

curl http://localhost:8000/health


View available tools:

cat /tmp/gh-aw/mcp-logs/tools.json | jq .


Watch logs in real-time:

tail -f /tmp/gh-aw/mcp-logs/mcp-gateway.log

Useful Aliases
alias awmg-dev='awmg --config config.dev.toml --listen 127.0.0.1:8000'
alias awmg-logs='tail -f /tmp/gh-aw/mcp-logs/mcp-gateway.log'
alias awmg-health='curl http://localhost:8000/health'
alias awmg-tools='cat /tmp/gh-aw/mcp-logs/tools.json | jq .'

Environment Setup

.env file:

MCP_GATEWAY_PORT=8000
MCP_GATEWAY_DOMAIN=localhost
MCP_GATEWAY_API_KEY=your-dev-api-key
MCP_GATEWAY_LOG_DIR=/var/log/mcp-gateway
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token
DEBUG=mcp:*,server:*


Load environment:

source .env
awmg --config config.toml

Quick Testing

Test tools/list:

curl -X POST http://localhost:8000/mcp/github \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}' | jq .


Test tools/call:

curl -X POST http://localhost:8000/mcp/github \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc":"2.0",
    "method":"tools/call",
    "params":{
      "name":"search_code",
      "arguments":{"query":"repo:github/gh-aw MCP"}
    },
    "id":2
  }' | jq .

Production Checklist
 API key configured and rotated
 Log directory mounted to host
 Docker socket accessible
 Health endpoint responding
 All backends starting successfully
 Tools discovered from all backends
 Authentication working
 Per-server logs available
 Resource limits set
 Monitoring configured
Weekly Installs
21
Repository
hack23/riksdagsmonitor
GitHub Stars
7
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn