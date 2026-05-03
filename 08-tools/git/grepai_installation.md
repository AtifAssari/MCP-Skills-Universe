---
title: grepai-installation
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-installation
---

# grepai-installation

skills/yoanbernabeu/grepai-skills/grepai-installation
grepai-installation
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-installation
SKILL.md
GrepAI Installation

This skill covers all methods to install GrepAI on any platform.

When to Use This Skill
Installing GrepAI for the first time
Upgrading an existing GrepAI installation
Building GrepAI from source
Verifying a successful installation
Prerequisites
macOS/Linux: Terminal access
Windows: PowerShell
From source: Go 1.24+ installed
Installation Methods
Method 1: Homebrew (macOS - Recommended)

The easiest way to install on macOS:

# Add the tap and install
brew install yoanbernabeu/tap/grepai

# Verify installation
grepai version


Advantages:

Automatic updates with brew upgrade grepai
Clean uninstall with brew uninstall grepai
Manages dependencies automatically
Method 2: Shell Script (Linux/macOS)

Universal installation script:

# Download and run the installer
curl -sSL https://raw.githubusercontent.com/yoanbernabeu/grepai/main/install.sh | sh

# Verify installation
grepai version


What the script does:

Detects your OS and architecture
Downloads the appropriate binary
Installs to /usr/local/bin/
Sets executable permissions
Method 3: PowerShell (Windows)

Native Windows installation:

# Run in PowerShell (Admin recommended)
irm https://raw.githubusercontent.com/yoanbernabeu/grepai/main/install.ps1 | iex

# Verify installation
grepai version


Note: You may need to adjust execution policy:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Method 4: Build from Source

For developers or custom builds:

# Clone the repository
git clone https://github.com/yoanbernabeu/grepai.git
cd grepai

# Build the binary
make build

# Install globally
sudo mv ./bin/grepai /usr/local/bin/

# Verify installation
grepai version


Requirements:

Go 1.24 or later
Make (optional, can use go build directly)
Verifying Installation

After installation, verify everything works:

# Check version
grepai version
# Output: grepai version 0.24.0

# Check available commands
grepai --help

Updating GrepAI
Check for Updates
grepai update --check

Perform Update
# Auto-update (downloads and installs latest)
grepai update

# Or via Homebrew
brew upgrade grepai

Uninstalling
Homebrew
brew uninstall grepai

Manual
# Remove binary
sudo rm /usr/local/bin/grepai

# Optionally remove config directories
rm -rf ~/.grepai

Next Steps

After installation:

Install Ollama for local embeddings (see grepai-ollama-setup skill)
Initialize a project with grepai init
Start indexing with grepai watch
Common Installation Issues

❌ Problem: command not found: grepai ✅ Solution: Ensure /usr/local/bin is in your PATH:

export PATH="$PATH:/usr/local/bin"


❌ Problem: Permission denied during installation ✅ Solution: Use sudo for the installation command or install to a user directory

❌ Problem: Homebrew tap not found ✅ Solution: Add the tap first:

brew tap yoanbernabeu/tap
brew install grepai

Output Format

After successful installation:

✅ GrepAI installed successfully
   Version: 0.24.0
   Location: /usr/local/bin/grepai

Next steps:
1. Install Ollama: brew install ollama
2. Initialize project: grepai init
3. Start indexing: grepai watch

Weekly Installs
389
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail