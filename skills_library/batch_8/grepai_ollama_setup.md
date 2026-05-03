---
title: grepai-ollama-setup
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-ollama-setup
---

# grepai-ollama-setup

skills/yoanbernabeu/grepai-skills/grepai-ollama-setup
grepai-ollama-setup
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-ollama-setup
SKILL.md
Ollama Setup for GrepAI

This skill covers installing and configuring Ollama as the local embedding provider for GrepAI. Ollama enables 100% private code search where your code never leaves your machine.

When to Use This Skill
Setting up GrepAI with local, private embeddings
Installing Ollama for the first time
Choosing and downloading embedding models
Troubleshooting Ollama connection issues
Why Ollama?
Benefit	Description
🔒 Privacy	Code never leaves your machine
💰 Free	No API costs
⚡ Fast	Local processing, no network latency
🔌 Offline	Works without internet
Installation
macOS (Homebrew)
# Install Ollama
brew install ollama

# Start the Ollama service
ollama serve

macOS (Direct Download)
Download from ollama.com
Open the .dmg and drag to Applications
Launch Ollama from Applications
Linux
# One-line installer
curl -fsSL https://ollama.com/install.sh | sh

# Start the service
ollama serve

Windows
Download installer from ollama.com
Run the installer
Ollama starts automatically as a service
Downloading Embedding Models

GrepAI requires an embedding model to convert code into vectors.

Recommended Model: nomic-embed-text
# Download the recommended model (768 dimensions)
ollama pull nomic-embed-text


Specifications:

Dimensions: 768
Size: ~274 MB
Performance: Excellent for code search
Language: English-optimized
Alternative Models
# Multilingual support (better for non-English code/comments)
ollama pull nomic-embed-text-v2-moe

# Larger, more accurate
ollama pull bge-m3

# Maximum quality
ollama pull mxbai-embed-large

Model	Dimensions	Size	Best For
nomic-embed-text	768	274 MB	General code search
nomic-embed-text-v2-moe	768	500 MB	Multilingual codebases
bge-m3	1024	1.2 GB	Large codebases
mxbai-embed-large	1024	670 MB	Maximum accuracy
Verifying Installation
Check Ollama is Running
# Check if Ollama server is responding
curl http://localhost:11434/api/tags

# Expected output: JSON with available models

List Downloaded Models
ollama list

# Output:
# NAME                     ID           SIZE    MODIFIED
# nomic-embed-text:latest  abc123...    274 MB  2 hours ago

Test Embedding Generation
# Quick test (should return embedding vector)
curl http://localhost:11434/api/embeddings -d '{
  "model": "nomic-embed-text",
  "prompt": "function hello() { return world; }"
}'

Configuring GrepAI for Ollama

After installing Ollama, configure GrepAI to use it:

# .grepai/config.yaml
embedder:
  provider: ollama
  model: nomic-embed-text
  endpoint: http://localhost:11434


This is the default configuration when you run grepai init, so no changes are needed if using nomic-embed-text.

Running Ollama
Foreground (Development)
# Run in current terminal (see logs)
ollama serve

Background (macOS/Linux)
# Using nohup
nohup ollama serve &

# Or as a systemd service (Linux)
sudo systemctl enable ollama
sudo systemctl start ollama

Check Status
# Check if running
pgrep -f ollama

# Or test the API
curl -s http://localhost:11434/api/tags | head -1

Resource Considerations
Memory Usage

Embedding models load into RAM:

nomic-embed-text: ~500 MB RAM
bge-m3: ~1.5 GB RAM
mxbai-embed-large: ~1 GB RAM
CPU vs GPU

Ollama uses CPU by default. For faster embeddings:

macOS: Uses Metal (Apple Silicon) automatically
Linux/Windows: Install CUDA for NVIDIA GPU support
Common Issues

❌ Problem: connection refused to localhost:11434 ✅ Solution: Start Ollama:

ollama serve


❌ Problem: Model not found ✅ Solution: Pull the model first:

ollama pull nomic-embed-text


❌ Problem: Slow embedding generation ✅ Solution:

Use a smaller model
Ensure Ollama is using GPU (check ollama ps)
Close other memory-intensive applications

❌ Problem: Out of memory ✅ Solution: Use a smaller model or increase system RAM

Best Practices
Start Ollama before GrepAI: Ensure ollama serve is running
Use recommended model: nomic-embed-text offers best balance
Keep Ollama running: Leave it as a background service
Update periodically: ollama pull nomic-embed-text for updates
Output Format

After successful setup:

✅ Ollama Setup Complete

   Ollama Version: 0.1.x
   Endpoint: http://localhost:11434
   Model: nomic-embed-text (768 dimensions)
   Status: Running

   GrepAI is ready to use with local embeddings.
   Your code will never leave your machine.

Weekly Installs
499
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn