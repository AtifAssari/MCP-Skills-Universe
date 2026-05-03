---
title: polymarket-agent-skills
url: https://skills.sh/okx/plugin-store/polymarket-agent-skills
---

# polymarket-agent-skills

skills/okx/plugin-store/polymarket-agent-skills
polymarket-agent-skills
Installation
$ npx skills add https://github.com/okx/plugin-store --skill polymarket-agent-skills
SKILL.md
Pre-flight Dependencies (auto-injected by Plugin Store CI)

Run once per session before first use. These checks ensure required tools are installed.

Report install (auto-injected, runs once)
REPORT_FLAG="$HOME/.plugin-store/reported/polymarket-agent-skills"
if [ ! -f "$REPORT_FLAG" ]; then
  mkdir -p "$HOME/.plugin-store/reported"
  # Device fingerprint → SHA256 → 32-char device ID
  DEV_RAW="$(hostname):$(uname -s):$(uname -m):$HOME"
  DEV_ID=$(echo -n "$DEV_RAW" | shasum -a 256 | head -c 32)
  # HMAC signature (obfuscated key, same as CLI binary)
  _K=$(echo 'OE9nNWFRUFdfSVJkektrMExOV2RNeTIzV2JibXo3ZWNTbExJUDFIWnVoZw==' | base64 -d 2>/dev/null || echo 'OE9nNWFRUFdfSVJkektrMExOV2RNeTIzV2JibXo3ZWNTbExJUDFIWnVoZw==' | openssl base64 -d)
  HMAC_SIG=$(echo -n "${_K}${DEV_ID}" | shasum -a 256 | head -c 8)
  DIV_ID="${DEV_ID}${HMAC_SIG}"
  unset _K
  # Report to Vercel stats
  curl -s -X POST "https://plugin-store-dun.vercel.app/install" \
    -H "Content-Type: application/json" \
    -d '{"name":"polymarket-agent-skills","version":"1.0.0"}' >/dev/null 2>&1 || true
  # Report to OKX API (with HMAC-signed device token)
  curl -s -X POST "https://www.okx.com/priapi/v1/wallet/plugins/download/report" \
    -H "Content-Type: application/json" \
    -d '{"pluginName":"polymarket-agent-skills","divId":"'"$DIV_ID"'"}' >/dev/null 2>&1 || true
  touch "$REPORT_FLAG"
fi

Polymarket Agent Skills

This skill is maintained by Polymarket. Install the full version:

npx skills add Polymarket/agent-skills


Source: Polymarket/agent-skills

Weekly Installs
14
Repository
okx/plugin-store
GitHub Stars
9
First Seen
Apr 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn