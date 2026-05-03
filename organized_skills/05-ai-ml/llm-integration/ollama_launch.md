---
rating: ⭐⭐⭐
title: ollama-launch
url: https://skills.sh/richfrem/agent-plugins-skills/ollama-launch
---

# ollama-launch

skills/richfrem/agent-plugins-skills/ollama-launch
ollama-launch
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill ollama-launch
SKILL.md
Dependencies

This skill requires Python 3.8+ and standard library only. No external packages needed.

To install this skill's dependencies:

pip-compile ./requirements.in
pip install -r ./requirements.txt


See ./requirements.txt for the dependency lockfile (currently empty — standard library only).

Ollama Launch

Ollama provides local LLM inference for RLM distillation (seal phase summarization) and embeddings.

When You Need This
Seal fails with Connection refused to 127.0.0.1:11434
RLM distillation shows [DISTILLATION FAILED] for new files
Any tool that calls the Ollama API locally
Pre-Flight Check
# Check if Ollama is already running
curl -sf http://127.0.0.1:11434/api/tags > /dev/null && echo "✅ Ollama running" || echo "❌ Ollama not running"


If running, you're done. If not, proceed.

Start Ollama
# Start Ollama in the background
ollama serve &>/dev/null &

# Wait and verify (2-3 seconds)
sleep 3
curl -sf http://127.0.0.1:11434/api/tags > /dev/null && echo "✅ Ollama ready" || echo "❌ Ollama failed to start"

Verify Model Available

For RLM distillation, the project uses model you define in .env

# List available models
ollama list

# If the model is missing, pull it
ollama pull qwen2:7b

Troubleshooting
Symptom	Fix
Connection refused after start	Wait longer (sleep 5), model may be loading
ollama: command not found	Ollama not installed — ask user to install from https://ollama.com
Port 11434 already in use	Another process on that port — lsof -i :11434 to identify
Integration Points
Learning Loop Seal Phase: RLM synthesis calls Ollama for distillation
RLM Factory: /rlm-factory:distill requires Ollama for batch summarization
Embeddings: Any tool that needs local vector embeddings
Weekly Installs
26
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn