---
rating: ⭐⭐
title: local-llm-ops
url: https://skills.sh/bobmatnyc/claude-mpm-skills/local-llm-ops
---

# local-llm-ops

skills/bobmatnyc/claude-mpm-skills/local-llm-ops
local-llm-ops
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill local-llm-ops
SKILL.md
Local LLM Ops (Ollama)
Overview

Your localLLM repo provides a full local LLM toolchain on Apple Silicon: setup scripts, a rich CLI chat launcher, benchmarks, and diagnostics. The operational path is: install Ollama, ensure the service is running, initialize the venv, pull models, then launch chat or benchmarks.

Quick Start
./setup_chatbot.sh
./chatllm


If no models are present:

ollama pull mistral

Setup Checklist
Install Ollama: brew install ollama
Start the service: brew services start ollama
Run setup: ./setup_chatbot.sh
Verify service: curl http://localhost:11434/api/version
Chat Launchers
./chatllm (primary launcher)
./chat or ./chat.py (alternate launchers)
Aliases: ./install_aliases.sh then llm, llm-code, llm-fast

Task modes:

./chat -t coding -m codellama:70b
./chat -t creative -m llama3.1:70b
./chat -t analytical

Benchmark Workflow

Benchmarks are scripted in scripts/run_benchmarks.sh:

./scripts/run_benchmarks.sh


This runs bench_ollama.py with:

benchmarks/prompts.yaml
benchmarks/models.yaml
Multiple runs and max token limits
Diagnostics

Run the built-in diagnostic script when setup fails:

./diagnose.sh


Common fixes:

Re-run ./setup_chatbot.sh
Ensure ollama is in PATH
Pull at least one model: ollama pull mistral
Operational Notes
Virtualenv lives in .venv
Chat configs and sessions live under ~/.localllm/
Ollama API runs at http://localhost:11434
Related Skills
toolchains/universal/infrastructure/docker
Weekly Installs
201
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass