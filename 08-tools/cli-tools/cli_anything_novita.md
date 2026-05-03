---
title: cli-anything-novita
url: https://skills.sh/hkuds/cli-anything/cli-anything-novita
---

# cli-anything-novita

skills/hkuds/cli-anything/cli-anything-novita
cli-anything-novita
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-novita
SKILL.md
cli-anything-novita

A CLI harness for Novita AI - an OpenAI-compatible API service for AI models like DeepSeek, GLM, and others.

Installation

This CLI is installed as part of the cli-anything-novita package:

pip install cli-anything-novita


Prerequisites:

Python 3.10+
Novita API key from novita.ai
Usage
Basic Commands
# Show help
cli-anything-novita --help

# Start interactive REPL mode
cli-anything-novita

# Chat with model
cli-anything-novita chat --prompt "What is AI?" --model deepseek/deepseek-v3.2

# Streaming chat
cli-anything-novita stream --prompt "Write a poem about code"

# List available models
cli-anything-novita models

# JSON output (for agent consumption)
cli-anything-novita --json chat --prompt "Hello"

REPL Mode

When invoked without a subcommand, the CLI enters an interactive REPL session:

cli-anything-novita
# Enter commands interactively with tab-completion and history

Command Groups
Chat

Chat with AI models through the Novita API.

Command	Description
chat	Chat with the Novita API
stream	Stream chat completion
Session

Session management for chat history.

Command	Description
status	Show session status
clear	Clear session history
history	Show command history
Config

Configuration management.

Command	Description
set	Set a configuration value
get	Get a configuration value (or show all)
delete	Delete a configuration value
path	Show the config file path
Utility
Command	Description
test	Test API connectivity
models	List available models
Examples
Configure API Key
# Set API key via config file (recommended)
cli-anything-novita config set api_key "sk-xxx"

# Or use environment variable
export NOVITA_API_KEY="sk-xxx"

Chat with DeepSeek
# Simple chat
cli-anything-novita chat --prompt "Explain quantum computing" --model deepseek/deepseek-v3.2

# Streaming chat
cli-anything-novita stream --prompt "Write a Python function to calculate factorial"

Test Connectivity
# Verify API key and connectivity
cli-anything-novita test --model deepseek/deepseek-v3.2

# List all available models
cli-anything-novita models

Default Models

The Novita API supports multiple model providers:

Model ID	Provider	Description
deepseek/deepseek-v3.2	DeepSeek	DeepSeek V3.2 model (default)
zai-org/glm-5	Zhipu AI	GLM-5 model
minimax/minimax-m2.5	MiniMax	MiniMax M2.5 model
Output Formats

All commands support dual output modes:

Human-readable (default): Tables, colors, formatted text
Machine-readable (--json flag): Structured JSON for agent consumption
# Human output
cli-anything-novita chat --prompt "Hello"

# JSON output for agents
cli-anything-novita --json chat --prompt "Hello"

For AI Agents

When using this CLI programmatically:

Always use --json flag for parseable output
Check return codes - 0 for success, non-zero for errors
Parse stderr for error messages on failure
Use absolute paths for all file operations
Verify outputs exist after export operations
More Information
Full documentation: See README.md in the package
Test coverage: See TEST.md in the package
Methodology: See HARNESS.md in the cli-anything-plugin
Version

1.0.0

Weekly Installs
88
Repository
hkuds/cli-anything
GitHub Stars
33.2K
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail