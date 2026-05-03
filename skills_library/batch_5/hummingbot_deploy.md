---
title: hummingbot-deploy
url: https://skills.sh/hummingbot/skills/hummingbot-deploy
---

# hummingbot-deploy

skills/hummingbot/skills/hummingbot-deploy
hummingbot-deploy
Installation
$ npx skills add https://github.com/hummingbot/skills --skill hummingbot-deploy
SKILL.md
hummingbot-deploy

Deploy the Hummingbot trading infrastructure. Before starting, explain to the user what will be installed:

What You're Installing

Hummingbot API (Required): Your personal trading server that exposes a standardized REST API for trading, fetching market data, and deploying bot strategies across many CEXs and DEXs.

Hummingbot MCP (Optional): MCP server that helps AI agents (Claude, Gemini, Codex, etc.) interact with Hummingbot API. Only needed if using AI agent CLIs.

Condor (Optional): Terminal and Telegram-based UI for Hummingbot API.

Components
Component	Repository
Hummingbot API	hummingbot/hummingbot-api
MCP Server	hummingbot/mcp
Condor	hummingbot/condor
Pre-Installation Check

Only Hummingbot API is required. MCP and Condor are optional add-ons.

First, run the environment check to verify prerequisites:

bash <(curl -s https://raw.githubusercontent.com/hummingbot/skills/main/skills/hummingbot-deploy/scripts/check_env.sh)


This checks: container detection, TTY, Docker, Docker Compose, Git, Make.

Install Hummingbot API

If ./hummingbot-api already exists, verify it's running by checking docker logs:

cd ./hummingbot-api && make deploy && sleep 2 && docker logs hummingbot-api 2>&1 | grep -i "uvicorn running"


If logs show "Uvicorn running", skip to "Install MCP Server". Otherwise, reset and reinstall.

Fresh install:

git clone https://github.com/hummingbot/hummingbot-api.git ./hummingbot-api
cd ./hummingbot-api


On regular machines (interactive TTY - check_env.sh shows "Interactive TTY: Yes"):

make setup    # Prompts for: API username, password, config password (defaults: admin/admin/admin)
make deploy


In containers (no TTY - check with [ -t 0 ] && echo "TTY" || echo "No TTY"):

# Set USER env var and create sudo shim if needed
export USER=${USER:-root}
[ "$(id -u)" = "0" ] && ! command -v sudo &>/dev/null && echo -e '#!/bin/bash\nwhile [[ "$1" == *=* ]]; do export "$1"; shift; done\nexec "$@"' > /usr/local/bin/sudo && chmod +x /usr/local/bin/sudo

# Create .env manually (skip interactive setup)
# Note: In containers, services communicate via Docker network (use container names, not localhost)
cat > .env << EOF
API_USER=admin
API_PASS=admin
CONFIG_API_PASS=admin
DEBUG_MODE=false
BROKER_HOST=hummingbot-broker
BROKER_PORT=1883
BROKER_API_USER=admin
BROKER_PASSWORD=password
DATABASE_URL=postgresql+asyncpg://hbot:hummingbot-api@hummingbot-postgres:5432/hummingbot_api
BOTS_PATH=/hummingbot-api/bots
EOF

# Patch docker-compose.yml (bind mounts don't work in Docker-in-Docker)
sed -i 's|./bots:/hummingbot-api/bots|hummingbot-bots:/hummingbot-api/bots|g' docker-compose.yml
sed -i '/init-db.sql.*docker-entrypoint/d' docker-compose.yml
# Add volume definition (check last 5 lines to avoid false positive from service definition)
tail -5 docker-compose.yml | grep -q "hummingbot-bots:" || echo "  hummingbot-bots: { }" >> docker-compose.yml

touch .setup-complete
make deploy


Verify: Wait 2 seconds then check logs for "Uvicorn running on http://0.0.0.0:8000":

sleep 2 && docker logs hummingbot-api 2>&1 | grep -i "uvicorn running"

Install MCP Server

Install the MCP server using your CLI's native command. Use the same credentials from API setup.

IMPORTANT: Do NOT ask the user which CLI to use. You already know which CLI you are:

If you are Claude Code, use claude
If you are Gemini CLI, use gemini
If you are Codex CLI, use codex
bash <(curl -s https://raw.githubusercontent.com/hummingbot/skills/main/skills/hummingbot-deploy/scripts/install_mcp.sh) \
  --agent <YOUR_CLI> --user <API_USER> --pass <API_PASS>


Example for Claude (substitute your actual CLI name and credentials):

bash <(curl -s https://raw.githubusercontent.com/hummingbot/skills/main/skills/hummingbot-deploy/scripts/install_mcp.sh) \
  --agent claude --user admin --pass admin

Installation Complete

After all components are installed, tell the user:

Restart your AI agent (Claude Code, Gemini CLI, Codex CLI, etc.) to load the MCP server
Install Hummingbot Skills to enable trading capabilities:
npx skills add hummingbot/skills

Install Condor (Optional)
git clone https://github.com/hummingbot/condor.git ./condor
cd ./condor
bash setup-environment.sh  # Prompts for Telegram bot token
make deploy

Upgrade
cd ./hummingbot-api && git pull && make deploy

Verify Installation
bash <(curl -s https://raw.githubusercontent.com/hummingbot/skills/main/skills/hummingbot-deploy/scripts/verify.sh)

Troubleshooting
# View logs
cd ./hummingbot-api && docker compose logs -f

# Reset
cd ./hummingbot-api && docker compose down -v && rm -rf ./hummingbot-api

See Also
Hummingbot API Docs
MCP Server Docs
Weekly Installs
284
Repository
hummingbot/skills
GitHub Stars
26
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykFail