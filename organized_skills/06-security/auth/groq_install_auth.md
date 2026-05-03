---
rating: ⭐⭐⭐
title: groq-install-auth
url: https://skills.sh/jeremylongshore/claude-code-plugins-plus-skills/groq-install-auth
---

# groq-install-auth

skills/jeremylongshore/claude-code-plugins-plus-skills/groq-install-auth
groq-install-auth
Installation
$ npx skills add https://github.com/jeremylongshore/claude-code-plugins-plus-skills --skill groq-install-auth
SKILL.md
Groq Install & Auth
Overview

Install the official Groq SDK and configure API key authentication. Groq provides ultra-fast LLM inference on custom LPU hardware through an OpenAI-compatible REST API at api.groq.com/openai/v1/.

Prerequisites
Node.js 18+ or Python 3.8+
Package manager (npm, pnpm, or pip)
Groq account at console.groq.com
API key from GroqCloud console (Settings > API Keys)
Instructions
Step 1: Install the SDK
set -euo pipefail
# TypeScript / JavaScript
npm install groq-sdk

# Python
pip install groq

Step 2: Get Your API Key
Go to console.groq.com/keys
Click "Create API Key"
Copy the key (starts with gsk_)
Store it securely -- you cannot view it again
Step 3: Configure Environment
# Set environment variable (recommended)
export GROQ_API_KEY="gsk_your_key_here"

# Or create .env file (add .env to .gitignore first)
echo 'GROQ_API_KEY=gsk_your_key_here' >> .env

Step 4: Verify Connection (TypeScript)
import Groq from "groq-sdk";

const groq = new Groq({
  apiKey: process.env.GROQ_API_KEY,
});

async function verify() {
  const models = await groq.models.list();
  console.log("Connected! Available models:");
  for (const model of models.data) {
    console.log(`  ${model.id} (owned by ${model.owned_by})`);
  }
}

verify().catch(console.error);

Step 5: Verify Connection (Python)
import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

models = client.models.list()
print("Connected! Available models:")
for model in models.data:
    print(f"  {model.id} (owned by {model.owned_by})")

SDK Defaults

The Groq SDK auto-reads GROQ_API_KEY from environment if no apiKey is passed to the constructor. Additional constructor options:

const groq = new Groq({
  apiKey: process.env.GROQ_API_KEY,  // Optional if env var set
  baseURL: "https://api.groq.com/openai/v1",  // Default
  maxRetries: 2,      // Default retry count
  timeout: 60_000,    // 60 second timeout (ms)
});

API Key Formats
Prefix	Type	Usage
gsk_	Standard API key	All API endpoints

Groq uses a single key type. There are no separate read/write scopes -- all keys have full API access. Restrict access through organizational controls in the console.

Error Handling
Error	Cause	Solution
401 Invalid API Key	Key missing, revoked, or mistyped	Verify key at console.groq.com/keys
MODULE_NOT_FOUND groq-sdk	SDK not installed	Run npm install groq-sdk
ModuleNotFoundError: No module named 'groq'	Python SDK missing	Run pip install groq
ENOTFOUND api.groq.com	Network/DNS issue	Check internet connectivity and firewall
.gitignore Template
# Groq secrets
.env
.env.local
.env.*.local

Resources
Groq Quickstart
Groq API Reference
groq-sdk on npm
groq-typescript on GitHub
Next Steps

After successful auth, proceed to groq-hello-world for your first chat completion.

Weekly Installs
27
Repository
jeremylongshore…s-skills
GitHub Stars
2.1K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass