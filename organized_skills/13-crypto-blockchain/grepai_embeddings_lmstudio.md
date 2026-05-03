---
rating: ⭐⭐⭐
title: grepai-embeddings-lmstudio
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-embeddings-lmstudio
---

# grepai-embeddings-lmstudio

skills/yoanbernabeu/grepai-skills/grepai-embeddings-lmstudio
grepai-embeddings-lmstudio
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-embeddings-lmstudio
SKILL.md
GrepAI Embeddings with LM Studio

This skill covers using LM Studio as the embedding provider for GrepAI, offering a user-friendly GUI for managing local models.

When to Use This Skill
Want local embeddings with a graphical interface
Already using LM Studio for other AI tasks
Prefer visual model management over CLI
Need to easily switch between models
What is LM Studio?

LM Studio is a desktop application for running local LLMs with:

🖥️ Graphical user interface
📦 Easy model downloading
🔌 OpenAI-compatible API
🔒 100% private, local processing
Prerequisites
Download LM Studio from lmstudio.ai
Install and launch the application
Download an embedding model
Installation
Step 1: Download LM Studio

Visit lmstudio.ai and download for your platform:

macOS (Intel or Apple Silicon)
Windows
Linux
Step 2: Launch and Download a Model
Open LM Studio
Go to the Search tab
Search for an embedding model:
nomic-embed-text-v1.5
bge-small-en-v1.5
bge-large-en-v1.5
Click Download
Step 3: Start the Local Server
Go to the Local Server tab
Select your embedding model
Click Start Server
Note the endpoint (default: http://localhost:1234)
Configuration
Basic Configuration
# .grepai/config.yaml
embedder:
  provider: lmstudio
  model: nomic-embed-text-v1.5
  endpoint: http://localhost:1234

With Custom Port
embedder:
  provider: lmstudio
  model: nomic-embed-text-v1.5
  endpoint: http://localhost:8080

With Explicit Dimensions
embedder:
  provider: lmstudio
  model: nomic-embed-text-v1.5
  endpoint: http://localhost:1234
  dimensions: 768

Available Models
nomic-embed-text-v1.5 (Recommended)
Property	Value
Dimensions	768
Size	~260 MB
Quality	Excellent
Speed	Fast
embedder:
  provider: lmstudio
  model: nomic-embed-text-v1.5

bge-small-en-v1.5
Property	Value
Dimensions	384
Size	~130 MB
Quality	Good
Speed	Very fast

Best for: Smaller codebases, faster indexing.

embedder:
  provider: lmstudio
  model: bge-small-en-v1.5
  dimensions: 384

bge-large-en-v1.5
Property	Value
Dimensions	1024
Size	~1.3 GB
Quality	Very high
Speed	Slower

Best for: Maximum accuracy.

embedder:
  provider: lmstudio
  model: bge-large-en-v1.5
  dimensions: 1024

Model Comparison
Model	Dims	Size	Speed	Quality
bge-small-en-v1.5	384	130MB	⚡⚡⚡	⭐⭐⭐
nomic-embed-text-v1.5	768	260MB	⚡⚡	⭐⭐⭐⭐
bge-large-en-v1.5	1024	1.3GB	⚡	⭐⭐⭐⭐⭐
LM Studio Server Setup
Starting the Server
Open LM Studio
Navigate to Local Server tab (left sidebar)
Select an embedding model from the dropdown
Configure settings:
Port: 1234 (default)
Enable Embedding Endpoint
Click Start Server
Server Status

Look for the green indicator showing the server is running.

Verifying the Server
# Check server is responding
curl http://localhost:1234/v1/models

# Test embedding
curl http://localhost:1234/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nomic-embed-text-v1.5",
    "input": "function authenticate(user)"
  }'

LM Studio Settings
Recommended Settings

In LM Studio's Local Server tab:

Setting	Recommended Value
Port	1234
Enable CORS	Yes
Context Length	Auto
GPU Layers	Max (for speed)
GPU Acceleration

LM Studio automatically uses:

macOS: Metal (Apple Silicon)
Windows/Linux: CUDA (NVIDIA)

Adjust GPU layers in settings for memory/speed balance.

Running LM Studio Headless

For server environments, LM Studio supports CLI mode:

# Start server without GUI (check LM Studio docs for exact syntax)
lmstudio server start --model nomic-embed-text-v1.5 --port 1234

Common Issues

❌ Problem: Connection refused ✅ Solution: Ensure LM Studio server is running:

Open LM Studio
Go to Local Server tab
Click Start Server

❌ Problem: Model not found ✅ Solution:

Download the model in LM Studio's Search tab
Select it in the Local Server dropdown

❌ Problem: Slow embedding generation ✅ Solutions:

Enable GPU acceleration in LM Studio settings
Use a smaller model (bge-small-en-v1.5)
Close other GPU-intensive applications

❌ Problem: Port already in use ✅ Solution: Change port in LM Studio settings:

embedder:
  endpoint: http://localhost:8080  # Different port


❌ Problem: LM Studio closes and server stops ✅ Solution: Keep LM Studio running in the background, or consider using Ollama which runs as a system service

LM Studio vs Ollama
Feature	LM Studio	Ollama
GUI	✅ Yes	❌ CLI only
System service	❌ App must run	✅ Background service
Model management	✅ Visual	✅ CLI
Ease of use	⭐⭐⭐⭐⭐	⭐⭐⭐⭐
Server reliability	⭐⭐⭐	⭐⭐⭐⭐⭐

Recommendation: Use LM Studio if you prefer a GUI, Ollama for always-on background service.

Migrating from LM Studio to Ollama

If you need a more reliable background service:

Install Ollama:
brew install ollama
ollama serve &
ollama pull nomic-embed-text

Update config:
embedder:
  provider: ollama
  model: nomic-embed-text
  endpoint: http://localhost:11434

Re-index:
rm .grepai/index.gob
grepai watch

Best Practices
Keep LM Studio running: Server stops when app closes
Use recommended model: nomic-embed-text-v1.5 for best balance
Enable GPU: Faster embeddings with hardware acceleration
Check server before indexing: Ensure green status indicator
Consider Ollama for production: More reliable as background service
Output Format

Successful LM Studio configuration:

✅ LM Studio Embedding Provider Configured

   Provider: LM Studio
   Model: nomic-embed-text-v1.5
   Endpoint: http://localhost:1234
   Dimensions: 768 (auto-detected)
   Status: Connected

   Note: Keep LM Studio running for embeddings to work.

Weekly Installs
356
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass