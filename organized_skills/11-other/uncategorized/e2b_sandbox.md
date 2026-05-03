---
rating: ⭐⭐⭐
title: e2b-sandbox
url: https://skills.sh/site/smithery.ai/e2b-sandbox
---

# e2b-sandbox

skills/smithery.ai/e2b-sandbox
e2b-sandbox
$ npx skills add https://smithery.ai/skills/padak/e2b-sandbox
SKILL.md
E2B Sandbox Skill

This skill provides comprehensive guidance for using E2B sandboxes - secure, isolated cloud VMs for executing AI-generated code with advanced monitoring, event handling, and integration capabilities.

What is E2B?

E2B provides secure isolated sandboxes (small VMs) in the cloud that start very quickly (~150ms). Each sandbox has:

Isolated filesystem (1GB Hobby tier, 5GB Pro tier)
Full code execution capabilities (Python, JavaScript, TypeScript, Bash)
Default lifetime of 5 minutes (configurable)
Network access capabilities
Real-time metrics monitoring (CPU, memory, disk)
Lifecycle event tracking and webhooks
MCP Gateway for 200+ tool integrations
Core Concepts
Sandbox Lifecycle

Creating a Sandbox:

from e2b_code_interpreter import Sandbox

# Create with default 5 minute timeout
sandbox = Sandbox.create()

# Create with custom timeout (in seconds)
sandbox = Sandbox.create(timeout=60)

# With auto-pause (beta)
sandbox = Sandbox.beta_create(
    auto_pause=True,
    timeout=10 * 60  # 10 minutes
)

# With metadata for tracking
sandbox = Sandbox.create(
    metadata={'userId': '123', 'env': 'dev'}
)

# With environment variables
sandbox = Sandbox.create(
    envs={'API_KEY': 'secret_value'}
)


JavaScript:

import { Sandbox } from '@e2b/code-interpreter'

// Create with metadata and env vars
const sandbox = await Sandbox.create({
  timeout: 60000,  // milliseconds
  metadata: { userId: '123' },
  envs: { API_KEY: 'secret_value' }
})


Changing Timeout During Runtime:

# Reset timeout to 30 seconds from now
sandbox.set_timeout(30)


Getting Sandbox Info:

info = sandbox.get_info()
# Returns: sandboxId, templateId, name, metadata, startedAt, endAt


Shutting Down:

# Terminate sandbox immediately
sandbox.kill()

# Or kill by ID
Sandbox.kill(sandbox_id)

Sandbox Management

List Sandboxes:

# List with pagination
paginator = Sandbox.list()
sandboxes = paginator.next_items()

# Filter by state
paginator = Sandbox.list(query={'state': ['running', 'paused']})

# Filter by metadata
paginator = Sandbox.list(
    query={'metadata': {'userId': '123', 'env': 'dev'}}
)

# Advanced pagination
paginator = Sandbox.list(limit=100, next_token='<token>')
while paginator.has_next:
    items = paginator.next_items()


Connect to Running Sandbox:

# Connect by ID
sandbox = Sandbox.connect(sandbox_id)

# Or reconnect to current
sandbox = sandbox.connect()


JavaScript:

// List and filter
const paginator = Sandbox.list({
  query: {
    state: ['running'],
    metadata: { userId: '123' }
  }
})
const sandboxes = await paginator.nextItems()

// Connect to existing
const sandbox = await Sandbox.connect(sandboxId)

Monitoring & Metrics

Get Sandbox Metrics:

import time

# Wait for metrics to collect (every 5 seconds)
time.sleep(10)

metrics = sandbox.get_metrics()
# Returns: [{timestamp, cpuUsedPct, cpuCount, memUsed, memTotal, diskUsed, diskTotal}]

# Or by ID
metrics = Sandbox.get_metrics(sandbox_id)


JavaScript:

await new Promise(resolve => setTimeout(resolve, 10000))

const metrics = await sandbox.getMetrics()
// Returns array of timestamped metrics


CLI:

e2b sandbox metrics <sandbox_id>
# Shows: CPU, Memory, Disk usage over time


Lifecycle Events (REST API):

import requests

# Get events for specific sandbox
response = requests.get(
    f'https://api.e2b.app/events/sandboxes/{sandbox_id}',
    headers={'X-API-Key': E2B_API_KEY}
)
events = response.json()

# Get latest 10 events for all sandboxes
response = requests.get(
    'https://api.e2b.app/events/sandboxes?limit=10',
    headers={'X-API-Key': E2B_API_KEY}
)


Event types: sandbox.lifecycle.created, sandbox.lifecycle.updated, sandbox.lifecycle.paused, sandbox.lifecycle.resumed, sandbox.lifecycle.killed

See docs/monitoring-and-events.md for webhook configuration.

Running Code

Execute Python Code (Default):

# Run Python code and get results
execution = sandbox.run_code('print("hello world")')

# Access results
print(execution.text)        # Combined output text
print(execution.logs.stdout)  # Standard output
print(execution.logs.stderr)  # Standard error
print(execution.results)      # Execution results (charts, tables, etc.)
print(execution.error)        # Runtime errors if any


Execute JavaScript/TypeScript:

# JavaScript
execution = sandbox.run_code(
    'console.log("Hello from JS")',
    language='javascript'  # or 'js'
)

# TypeScript with top-level await and ESM imports
execution = sandbox.run_code('''
import axios from "axios";
const response = await axios.get("https://api.github.com/status");
response.data;
''', language='typescript')  # or 'ts'


Execute Bash:

execution = sandbox.run_code(
    'ls -la /home/user',
    language='bash'
)


With Environment Variables:

# Scoped to this execution only
execution = sandbox.run_code(
    'import os; print(os.environ.get("MY_VAR"))',
    envs={'MY_VAR': 'my_value'}
)


JavaScript:

// Python (default)
const exec = await sandbox.runCode('print("hello")')

// JavaScript/TypeScript
const exec = await sandbox.runCode('console.log("hello")', {
  language: 'js',
  envs: { MY_VAR: 'value' }
})

Running Commands

Execute Bash Commands:

# Run terminal commands
result = sandbox.commands.run('ls -l')
print(result)

# With environment variables
result = sandbox.commands.run(
    'echo $MY_VAR',
    envs={'MY_VAR': '123'}
)


Streaming Output:

# Stream stdout/stderr in real-time
process = sandbox.commands.run(
    'for i in {1..5}; do echo "Line $i"; sleep 1; done',
    on_stdout=lambda data: print(f"OUT: {data}"),
    on_stderr=lambda data: print(f"ERR: {data}")
)


Background Commands:

# Run in background, returns immediately
command = sandbox.commands.run(
    'echo hello; sleep 10; echo world',
    background=True,
    on_stdout=lambda data: print(data)
)

# Kill later
command.kill()


JavaScript:

// Streaming
await sandbox.commands.run('echo hello', {
  onStdout: (data) => console.log(data),
  onStderr: (data) => console.error(data)
})

// Background
const cmd = await sandbox.commands.run('sleep 100', {
  background: true
})
await cmd.kill()

Environment Variables

Three scoping levels:

Global (sandbox-wide):
sandbox = Sandbox.create(envs={'API_KEY': 'value'})

Code execution scope:
sandbox.run_code(code, envs={'MY_VAR': 'value'})

Command execution scope:
sandbox.commands.run(cmd, envs={'MY_VAR': 'value'})


Default Environment Variables:

E2B_SANDBOX=true - Indicates code is running in E2B
E2B_SANDBOX_ID - Current sandbox ID
E2B_TEAM_ID - Team ID that created sandbox
E2B_TEMPLATE_ID - Template used for sandbox
File Operations

Upload Files:

import fs

# Read local file
content = fs.read_file('local/file.csv')

# Upload to sandbox (absolute path required)
file_info = sandbox.files.write('/home/user/data.csv', content)
print(file_info.path)  # Path in sandbox


Download Files:

# Download file from sandbox
content = sandbox.files.read('/home/user/output.png')

# Save locally
fs.write_file('local/output.png', content)


List Files:

# List files in directory
files = sandbox.files.list('/')
for file in files:
    print(file)


Watch for Changes:

# Monitor filesystem changes
watcher = sandbox.files.watch('/home/user')
watcher.on_change(lambda event: print(f"Changed: {event}"))


See docs/filesystem.md for complete filesystem API.

Sandbox Persistence (Beta)

Pause and Resume:

# Pause sandbox (saves filesystem + memory state)
sandbox.beta_pause()
print(f"Paused sandbox: {sandbox.sandbox_id}")

# Resume later by reconnecting
resumed = sandbox.connect()

# Or connect by ID
resumed = Sandbox.connect(sandbox_id)


List Paused Sandboxes:

# Get paginated list of paused sandboxes
paginator = Sandbox.list(query={'state': ['paused']})
sandboxes = paginator.next_items()


Important Notes:

Pausing takes ~4 seconds per 1 GiB of RAM
Resuming takes ~1 second
Sandbox can be used for up to 30 days
When sandbox resumes, timeout resets to default (5 minutes) or custom value
Advanced Features
MCP Gateway (200+ Tool Integrations)

E2B provides built-in access to 200+ MCP (Model Context Protocol) servers for integrating external tools.

Enable MCP Servers:

# Python (JS SDK)
sandbox = Sandbox.create(
    mcp={
        'browserbase': {
            'apiKey': os.environ['BROWSERBASE_API_KEY'],
            'geminiApiKey': os.environ['GEMINI_API_KEY'],
            'projectId': os.environ['BROWSERBASE_PROJECT_ID']
        },
        'exa': {'apiKey': os.environ['EXA_API_KEY']},
        'notion': {'internalIntegrationToken': os.environ['NOTION_API_KEY']}
    }
)

# Get MCP URL and token
mcp_url = sandbox.get_mcp_url()
mcp_token = sandbox.get_mcp_token()


Connect from Outside Sandbox:

import { Client } from '@modelcontextprotocol/sdk/client/index.js'
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js'

const client = new Client({ name: 'e2b-mcp-client', version: '1.0.0' })

const transport = new StreamableHTTPClientTransport(
    new URL(sandbox.getMcpUrl()),
    {
        requestInit: {
            headers: { 'Authorization': `Bearer ${await sandbox.getMcpToken()}` }
        }
    }
)

await client.connect(transport)
const tools = await client.listTools()


MCP Server Categories:

Data & Databases: MongoDB, PostgreSQL, Redis, Elasticsearch, Astra DB
Cloud: AWS, Azure, Google Cloud, Kubernetes
Web & Content: Firecrawl, Brave Search, Perplexity, DuckDuckGo, Tavily
Business: Slack, Notion, GitHub, Jira, Confluence, HubSpot
Development: GitHub Chat, JetBrains IDE, ast-grep, Semgrep
AI: OpenAI, Browserbase, Hugging Face, ElevenLabs
Finance: Stripe, Razorpay, Mercado Pago

See docs/mcp-gateway.md for complete list and configuration.

Custom Templates

Build custom sandbox environments with specific dependencies:

# Using E2B CLI
e2b template build

# Specify CPU/RAM in e2b.toml
cpu_count = 2
memory_mb = 2048

# Add start commands
start_cmd = "python app.py"

# Add readiness checks
ready_cmd = "curl localhost:8000/health"


See docs/custom-templates.md for Build System 2.0 details.

E2B CLI
# Authenticate
e2b auth login

# List sandboxes
e2b sandbox list

# Get metrics
e2b sandbox metrics <sandbox_id>

# Build custom template
e2b template build

# Connect to sandbox
e2b sandbox connect <sandbox_id>

Integration Patterns
Connecting LLMs to E2B

E2B works with any LLM via tool use (function calling). The general pattern:

Define a tool/function for code execution
LLM generates code
Execute code in E2B sandbox
Return results to LLM

Example with Tool Use:

from anthropic import Anthropic
from e2b_code_interpreter import Sandbox

# Define tool
tools = [{
    "name": "execute_python",
    "description": "Execute python code in a Jupyter notebook cell and return result",
    "input_schema": {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "The python code to execute in a single cell"
            }
        },
        "required": ["code"]
    }
}]

# Create Anthropic client
client = Anthropic()

# Send message with tools
message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": "Calculate how many r's are in the word 'strawberry'"
    }],
    tools=tools
)

# Execute tool if called
if message.stop_reason == "tool_use":
    tool_use = next(block for block in message.content if block.type == "tool_use")
    if tool_use.name == "execute_python":
        with Sandbox.create() as sandbox:
            code = tool_use.input['code']
            execution = sandbox.run_code(code)
            result = execution.text
            print(result)

Data Analysis Pattern

For data analysis workflows:

Create sandbox
Upload dataset
LLM generates analysis code
Execute in sandbox
Extract results (charts, tables, data)
# Upload dataset
content = fs.read_file('dataset.csv')
dataset_path = sandbox.files.write('/home/user/dataset.csv', content)

# Run analysis code (generated by LLM)
execution = sandbox.run_code(analysis_code)

# Extract chart if generated
for result in execution.results:
    if result.png:
        # PNG is base64 encoded
        fs.write_file('chart.png', result.png, encoding='base64')

Multi-User Session Management
# Create sandbox per user with metadata
sandbox = Sandbox.create(
    metadata={'userId': user_id, 'sessionId': session_id}
)

# Later: Find user's sandboxes
paginator = Sandbox.list(
    query={'metadata': {'userId': user_id}}
)
user_sandboxes = paginator.next_items()

# Reconnect to existing session
if user_sandboxes:
    sandbox = Sandbox.connect(user_sandboxes[0].sandbox_id)

Best Practices
Resource Management
Always clean up sandboxes:
# Use context manager (recommended)
with Sandbox.create() as sandbox:
    # Your code here
    pass  # Sandbox automatically killed on exit

# Or manually
sandbox = Sandbox.create()
try:
    # Your code here
    pass
finally:
    sandbox.kill()


Set appropriate timeouts:

Short tasks: 60-120 seconds
Long-running analysis: 300-600 seconds
Use auto-pause for interactive sessions

Use persistence wisely:

Pause sandboxes between user interactions
Don't pause for short breaks (<5 minutes)
Kill sandboxes when truly done

Monitor resource usage:

# Check metrics before intensive operations
metrics = sandbox.get_metrics()
if metrics:
    latest = metrics[-1]
    if latest['cpuUsedPct'] > 80:
        print("Warning: High CPU usage")

Code Execution
Handle errors gracefully:
execution = sandbox.run_code(code)

if execution.error:
    print(f"Error: {execution.error.name}")
    print(f"Message: {execution.error.value}")
    print(f"Traceback: {execution.error.traceback}")
else:
    print(execution.text)

Process results by type:
for result in execution.results:
    if result.png:
        # Handle chart/image
        save_image(result.png)
    elif result.text:
        # Handle text output
        print(result.text)

Use appropriate language:
# Python for data analysis
sandbox.run_code('import pandas as pd; df.describe()')

# JavaScript for async API calls
sandbox.run_code('await fetch(url)', language='js')

# Bash for system operations
sandbox.run_code('tar -xzf archive.tar.gz', language='bash')

File Operations
Always use absolute paths:
# Good
sandbox.files.write('/home/user/data.csv', content)

# Bad (relative paths may not work as expected)
sandbox.files.write('data.csv', content)

Upload files before executing code:
# Upload dataset first
sandbox.files.write('/home/user/data.csv', dataset)

# Then run code that uses it
code = "import pandas as pd; df = pd.read_csv('/home/user/data.csv')"
sandbox.run_code(code)

Sandbox Discovery
Use metadata for tracking:
# Tag sandboxes with identifying information
sandbox = Sandbox.create(metadata={
    'userId': '123',
    'purpose': 'data-analysis',
    'created': datetime.now().isoformat()
})

# Find and reconnect
paginator = Sandbox.list(query={'metadata': {'userId': '123'}})

Clean up orphaned sandboxes:
# Find all running sandboxes
paginator = Sandbox.list(query={'state': ['running']})
sandboxes = paginator.next_items()

# Kill old ones
for sbx in sandboxes:
    if should_cleanup(sbx):
        Sandbox.kill(sbx.sandbox_id)

Common Patterns
Pattern 1: One-shot Code Execution
with Sandbox.create() as sandbox:
    result = sandbox.run_code(llm_generated_code)
    return result.text

Pattern 2: Multi-step Analysis
sandbox = Sandbox.create(timeout=300)
try:
    # Step 1: Upload data
    sandbox.files.write('/home/user/data.csv', data)

    # Step 2: Load and explore
    sandbox.run_code("import pandas as pd; df = pd.read_csv('/home/user/data.csv')")

    # Step 3: Analyze (code from LLM)
    result = sandbox.run_code(analysis_code)

    # Step 4: Extract results
    for r in result.results:
        if r.png:
            save_chart(r.png)
finally:
    sandbox.kill()

Pattern 3: Interactive Session with Persistence
# Initial creation
sandbox = Sandbox.beta_create(auto_pause=True, timeout=600)

# Do some work
sandbox.run_code(initial_code)

# Pause when user is inactive
sandbox.beta_pause()
save_sandbox_id(sandbox.sandbox_id)

# Later: Resume when user returns
sandbox = Sandbox.connect(saved_sandbox_id)
sandbox.run_code(next_code)

Pattern 4: MCP Tool Integration
// Create sandbox with MCP servers
const sandbox = await Sandbox.create({
    mcp: {
        github: { githubPersonalAccessToken: process.env.GITHUB_TOKEN },
        slack: { botToken: process.env.SLACK_BOT_TOKEN }
    }
})

// Connect MCP client
const client = new Client({ name: 'app', version: '1.0.0' })
const transport = new StreamableHTTPClientTransport(
    new URL(sandbox.getMcpUrl()),
    { requestInit: { headers: { 'Authorization': `Bearer ${await sandbox.getMcpToken()}` }}}
)
await client.connect(transport)

// List available tools
const tools = await client.listTools()

Environment Variables

Required environment variable:

E2B_API_KEY=e2b_***


Get your API key from: https://e2b.dev/dashboard?tab=keys

SDK Installation
# Python
pip install e2b-code-interpreter

# JavaScript/TypeScript
npm i @e2b/code-interpreter

API Differences: Python vs JavaScript
Operation	Python	JavaScript
Create	Sandbox.create()	await Sandbox.create()
Set timeout	sandbox.set_timeout(60)	await sandbox.setTimeout(60000) (milliseconds)
Get info	sandbox.get_info()	await sandbox.getInfo()
Run code	sandbox.run_code(code)	await sandbox.runCode(code)
Run command	sandbox.commands.run(cmd)	await sandbox.commands.run(cmd)
Get metrics	sandbox.get_metrics()	await sandbox.getMetrics()
List sandboxes	Sandbox.list()	Sandbox.list()
Connect	Sandbox.connect(id)	await Sandbox.connect(id)
Kill	sandbox.kill()	await sandbox.kill()
Pause	sandbox.beta_pause()	await sandbox.betaPause()
Troubleshooting
Sandbox Times Out Too Quickly
Increase timeout on creation: Sandbox.create(timeout=300)
Or reset during runtime: sandbox.set_timeout(300)
Code Execution Fails
Check execution.error for details
Verify file paths are absolute
Ensure required packages are available
Check language parameter matches code type
Files Not Found
Use absolute paths: /home/user/filename
Verify file was uploaded successfully
Check file exists: sandbox.files.list('/home/user')
Persistence Issues
Sandboxes auto-delete after 30 days
Check sandbox still exists before connecting
Handle NotFoundException when connecting
High Resource Usage
Check metrics: sandbox.get_metrics()
Kill unused sandboxes
Use smaller datasets or optimize code
MCP Connection Issues
Verify API keys for MCP servers
Check MCP URL and token are valid
Use MCP Inspector for debugging: npx @modelcontextprotocol/inspector
Reference Documentation

For detailed API documentation and additional examples:

E2B Documentation
Quickstart Guide
Sandbox Lifecycle
Monitoring & Events
Advanced Sandbox Management
File Operations
MCP Gateway
Custom Templates
Persistence Guide
Weekly Installs
44
Source
smithery.ai/ski…-sandbox
First Seen
Mar 6, 2026