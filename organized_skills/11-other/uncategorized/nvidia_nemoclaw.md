---
rating: ⭐⭐⭐
title: nvidia-nemoclaw
url: https://skills.sh/aradotso/trending-skills/nvidia-nemoclaw
---

# nvidia-nemoclaw

skills/aradotso/trending-skills/nvidia-nemoclaw
nvidia-nemoclaw
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill nvidia-nemoclaw
SKILL.md
NVIDIA NemoClaw

Skill by ara.so — Daily 2026 Skills collection.

NVIDIA NemoClaw is an open-source TypeScript CLI plugin that simplifies running OpenClaw always-on AI assistants securely. It installs and orchestrates the NVIDIA OpenShell runtime, creates policy-enforced sandboxes, and routes all inference through NVIDIA cloud (Nemotron models). Network egress, filesystem access, syscalls, and model API calls are all governed by declarative policy.

Status: Alpha — interfaces and APIs may change without notice.

Installation
Prerequisites
Linux Ubuntu 22.04 LTS or later
Node.js 20+ and npm 10+ (Node.js 22 recommended)
Docker installed and running
NVIDIA OpenShell installed
One-Line Installer
curl -fsSL https://nvidia.com/nemoclaw.sh | bash


This installs Node.js (if absent), runs the guided onboard wizard, creates a sandbox, configures inference, and applies security policies.

Manual Install (from source)
git clone https://github.com/NVIDIA/NemoClaw.git
cd NemoClaw
npm install
npm run build
npm link  # makes `nemoclaw` available globally

Environment Variables
# Required: NVIDIA cloud API key for Nemotron inference
export NVIDIA_API_KEY="nvapi-xxxxxxxxxxxx"

# Optional: override default model
export NEMOCLAW_MODEL="nvidia/nemotron-3-super-120b-a12b"

# Optional: custom sandbox data directory
export NEMOCLAW_SANDBOX_DIR="/var/nemoclaw/sandboxes"


Get an API key at build.nvidia.com.

Quick Start
1. Onboard a New Agent
nemoclaw onboard


The interactive wizard prompts for:

Sandbox name (e.g. my-assistant)
NVIDIA API key ($NVIDIA_API_KEY)
Inference model selection
Network and filesystem policy configuration

Expected output on success:

──────────────────────────────────────────────────
Sandbox      my-assistant (Landlock + seccomp + netns)
Model        nvidia/nemotron-3-super-120b-a12b (NVIDIA Cloud API)
──────────────────────────────────────────────────
Run:         nemoclaw my-assistant connect
Status:      nemoclaw my-assistant status
Logs:        nemoclaw my-assistant logs --follow
──────────────────────────────────────────────────
[INFO]  === Installation complete ===

2. Connect to the Sandbox
nemoclaw my-assistant connect

3. Chat with the Agent (inside sandbox)

TUI (interactive chat):

sandbox@my-assistant:~$ openclaw tui


CLI (single message):

sandbox@my-assistant:~$ openclaw agent --agent main --local -m "hello" --session-id test

Key CLI Commands
Host Commands (nemoclaw)
Command	Description
nemoclaw onboard	Interactive setup: gateway, providers, sandbox
nemoclaw <name> connect	Open interactive shell inside sandbox
nemoclaw <name> status	Show NemoClaw-level sandbox health
nemoclaw <name> logs --follow	Stream sandbox logs
nemoclaw start	Start auxiliary services (Telegram bridge, tunnel)
nemoclaw stop	Stop auxiliary services
nemoclaw deploy <instance>	Deploy to remote GPU instance via Brev
openshell term	Launch OpenShell TUI for monitoring and approvals
Plugin Commands (openclaw nemoclaw, run inside sandbox)

Note: These are under active development — use nemoclaw host CLI as the primary interface.

Command	Description
openclaw nemoclaw launch [--profile ...]	Bootstrap OpenClaw inside OpenShell sandbox
openclaw nemoclaw status	Show sandbox health, blueprint state, and inference
openclaw nemoclaw logs [-f]	Stream blueprint execution and sandbox logs
OpenShell Inspection
# List all sandboxes at the OpenShell layer
openshell sandbox list

# Check specific sandbox
openshell sandbox inspect my-assistant

Architecture

NemoClaw orchestrates four components:

Component	Role
Plugin	TypeScript CLI: launch, connect, status, logs
Blueprint	Versioned Python artifact: sandbox creation, policy, inference setup
Sandbox	Isolated OpenShell container running OpenClaw with policy-enforced egress/filesystem
Inference	NVIDIA cloud model calls routed through OpenShell gateway

Blueprint lifecycle:

Resolve artifact
Verify digest
Plan resources
Apply through OpenShell CLI
TypeScript Plugin Usage

NemoClaw exposes a programmatic TypeScript API for building custom integrations.

Import and Initialize
import { NemoClawClient } from '@nvidia/nemoclaw';

const client = new NemoClawClient({
  apiKey: process.env.NVIDIA_API_KEY!,
  model: process.env.NEMOCLAW_MODEL ?? 'nvidia/nemotron-3-super-120b-a12b',
});

Create a Sandbox Programmatically
import { NemoClawClient, SandboxConfig } from '@nvidia/nemoclaw';

async function createSandbox() {
  const client = new NemoClawClient({
    apiKey: process.env.NVIDIA_API_KEY!,
  });

  const config: SandboxConfig = {
    name: 'my-assistant',
    model: 'nvidia/nemotron-3-super-120b-a12b',
    policy: {
      network: {
        allowedEgressHosts: ['build.nvidia.com'],
        blockUnlisted: true,
      },
      filesystem: {
        allowedPaths: ['/sandbox', '/tmp'],
        readOnly: false,
      },
    },
  };

  const sandbox = await client.sandbox.create(config);
  console.log(`Sandbox created: ${sandbox.id}`);
  return sandbox;
}

Connect and Send a Message
import { NemoClawClient } from '@nvidia/nemoclaw';

async function chatWithAgent(sandboxName: string, message: string) {
  const client = new NemoClawClient({
    apiKey: process.env.NVIDIA_API_KEY!,
  });

  const sandbox = await client.sandbox.get(sandboxName);
  const session = await sandbox.connect();

  const response = await session.agent.send({
    agentId: 'main',
    message,
    sessionId: `session-${Date.now()}`,
  });

  console.log('Agent response:', response.content);
  await session.disconnect();
}

chatWithAgent('my-assistant', 'Summarize the latest NVIDIA earnings report.');

Check Sandbox Status
import { NemoClawClient } from '@nvidia/nemoclaw';

async function checkStatus(sandboxName: string) {
  const client = new NemoClawClient({
    apiKey: process.env.NVIDIA_API_KEY!,
  });

  const status = await client.sandbox.status(sandboxName);

  console.log({
    sandbox: status.name,
    healthy: status.healthy,
    blueprint: status.blueprintState,
    inference: status.inferenceProvider,
    policyVersion: status.policyVersion,
  });
}

Stream Logs
import { NemoClawClient } from '@nvidia/nemoclaw';

async function streamLogs(sandboxName: string) {
  const client = new NemoClawClient({
    apiKey: process.env.NVIDIA_API_KEY!,
  });

  const logStream = client.sandbox.logs(sandboxName, { follow: true });

  for await (const entry of logStream) {
    console.log(`[${entry.timestamp}] ${entry.level}: ${entry.message}`);
  }
}

Apply a Network Policy Update (Hot Reload)
import { NemoClawClient, NetworkPolicy } from '@nvidia/nemoclaw';

async function updateNetworkPolicy(sandboxName: string) {
  const client = new NemoClawClient({
    apiKey: process.env.NVIDIA_API_KEY!,
  });

  // Network policies are hot-reloadable at runtime
  const updatedPolicy: NetworkPolicy = {
    allowedEgressHosts: [
      'build.nvidia.com',
      'api.github.com',
    ],
    blockUnlisted: true,
  };

  await client.sandbox.updatePolicy(sandboxName, {
    network: updatedPolicy,
  });

  console.log('Network policy updated (hot reload applied).');
}

Security / Protection Layers
Layer	What it protects	Hot-reloadable?
Network	Blocks unauthorized outbound connections	✅ Yes
Filesystem	Prevents reads/writes outside /sandbox and /tmp	❌ Locked at creation
Process	Blocks privilege escalation and dangerous syscalls	❌ Locked at creation
Inference	Reroutes model API calls to controlled backends	✅ Yes

When the agent attempts to reach an unlisted host, OpenShell blocks the request and surfaces it in the TUI for operator approval.

Common Patterns
Pattern: Minimal Sandbox for Development
const config: SandboxConfig = {
  name: 'dev-sandbox',
  model: 'nvidia/nemotron-3-super-120b-a12b',
  policy: {
    network: { blockUnlisted: false },   // permissive for dev
    filesystem: { allowedPaths: ['/sandbox', '/tmp', '/home/dev'] },
  },
};

Pattern: Production Strict Sandbox
const config: SandboxConfig = {
  name: 'prod-assistant',
  model: 'nvidia/nemotron-3-super-120b-a12b',
  policy: {
    network: {
      allowedEgressHosts: ['build.nvidia.com'],
      blockUnlisted: true,
    },
    filesystem: {
      allowedPaths: ['/sandbox', '/tmp'],
      readOnly: false,
    },
  },
};

Pattern: Deploy to Remote GPU (Brev)
nemoclaw deploy my-gpu-instance --sandbox my-assistant

await client.deploy({
  instance: 'my-gpu-instance',
  sandboxName: 'my-assistant',
  provider: 'brev',
});

Troubleshooting
Error: Sandbox not found
Error: Sandbox 'my-assistant' not found


Fix: Check at the OpenShell layer — NemoClaw errors and OpenShell errors are separate:

openshell sandbox list
nemoclaw my-assistant status

Error: NVIDIA API key missing or invalid
Error: Inference provider authentication failed


Fix:

export NVIDIA_API_KEY="nvapi-xxxxxxxxxxxx"
nemoclaw onboard  # re-run to reconfigure

Error: Docker not running
Error: Cannot connect to Docker daemon


Fix:

sudo systemctl start docker
sudo usermod -aG docker $USER  # add current user to docker group
newgrp docker

Error: OpenShell not installed
Error: 'openshell' command not found


Fix: Install NVIDIA OpenShell first, then re-run the NemoClaw installer.

Agent blocked on outbound request

When you see a blocked request notification in the TUI:

openshell term        # open TUI to approve/deny the request
# OR update policy to allow the host:
nemoclaw my-assistant policy update --allow-host api.example.com

View Full Debug Logs
nemoclaw my-assistant logs --follow
# or with verbose flag
nemoclaw my-assistant logs --follow --level debug

Documentation Links
Overview
How It Works
Architecture
Inference Profiles
Network Policies
CLI Commands
Weekly Installs
1.2K
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn