---
rating: ⭐⭐
title: uniswap-pay-with-any-token
url: https://skills.sh/okx/plugin-store/uniswap-pay-with-any-token
---

# uniswap-pay-with-any-token

skills/okx/plugin-store/uniswap-pay-with-any-token
uniswap-pay-with-any-token
Installation
$ npx skills add https://github.com/okx/plugin-store --skill uniswap-pay-with-any-token
SKILL.md
Pre-flight Dependencies (auto-injected by Plugin Store CI)

Run once per session before first use. These checks ensure required tools are installed.

Version check (auto-injected)

AI Agent Instruction: Run this version check before executing any commands from this skill. If an update is applied, re-read this SKILL.md before proceeding — the instructions may have changed.

# Check for skill updates (1-hour cache)
UPDATE_CACHE="$HOME/.plugin-store/update-cache/uniswap-pay-with-any-token"
CACHE_MAX=3600
LOCAL_VER="2.0.0"
DO_CHECK=true

if [ -f "$UPDATE_CACHE" ]; then
  CACHE_MOD=$(stat -f %m "$UPDATE_CACHE" 2>/dev/null || stat -c %Y "$UPDATE_CACHE" 2>/dev/null || echo 0)
  NOW=$(date +%s)
  AGE=$(( NOW - CACHE_MOD ))
  [ "$AGE" -lt "$CACHE_MAX" ] && DO_CHECK=false
fi

if [ "$DO_CHECK" = true ]; then
  REMOTE_VER=$(curl -sf --max-time 3 "https://raw.githubusercontent.com/okx/plugin-store/main/skills/uniswap-pay-with-any-token/plugin.yaml" | grep '^version' | head -1 | tr -d '"' | awk '{print $2}')
  if [ -n "$REMOTE_VER" ]; then
    mkdir -p "$HOME/.plugin-store/update-cache"
    echo "$REMOTE_VER" > "$UPDATE_CACHE"
  fi
fi

REMOTE_VER=$(cat "$UPDATE_CACHE" 2>/dev/null || echo "$LOCAL_VER")
if [ "$REMOTE_VER" != "$LOCAL_VER" ]; then
  echo "Update available: uniswap-pay-with-any-token v$LOCAL_VER -> v$REMOTE_VER. Updating..."
  npx skills add okx/plugin-store --skill uniswap-pay-with-any-token --yes --global 2>/dev/null || true
  echo "Updated uniswap-pay-with-any-token to v$REMOTE_VER. Please re-read this SKILL.md."
fi

uniswap-pay-with-any-token

This skill is maintained by Uniswap Labs. Install the full version:

npx skills add Uniswap/uniswap-ai


Or install just this plugin:

claude plugin add @uniswap/uniswap-trading


Source: uniswap-ai/packages/plugins/uniswap-trading/skills/pay-with-any-token

Weekly Installs
26
Repository
okx/plugin-store
GitHub Stars
9
First Seen
10 days ago
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykFail