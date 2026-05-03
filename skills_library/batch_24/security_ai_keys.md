---
title: security-ai-keys
url: https://skills.sh/igorwarzocha/opencode-workflows/security-ai-keys
---

# security-ai-keys

skills/igorwarzocha/opencode-workflows/security-ai-keys
security-ai-keys
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill security-ai-keys
SKILL.md

Security audit patterns for AI API key leakage in applications integrating AI providers.

Core Principles
MUST treat AI API keys as secrets and keep them server-side.
MUST NOT ship keys to browsers or mobile clients.
SHOULD avoid logging keys; redact before logging or error reporting.
MUST rotate keys immediately if exposure is suspected.
Common Leak Paths
1) Client-Side Exposure
NEXT_PUBLIC_* / VITE_* env vars containing AI keys
Direct calls to AI provider endpoints from browser code
2) Build Artifacts
Keys embedded in bundles (dist/, build/, .next/)
Source maps exposing server code containing keys
3) Logs and Telemetry
console.log / logger statements that include key values
Error tracking payloads (Sentry, Datadog) with headers included
Quick Audit Commands
# Env files: AI keys accidentally exposed to client
rg -n "(NEXT_PUBLIC_|VITE_).*(OPENAI|OPENROUTER|ANTHROPIC|GEMINI|GOOGLE|VERTEX|BEDROCK|AWS|AZURE|MISTRAL|COHERE|GROQ|PERPLEXITY|TOGETHER|REPLICATE|FIREWORKS|HUGGINGFACE|HF_)" . -g "*.env*"

# Client code calling AI APIs directly (check for browser use)
rg -n "api\.openai\.com|openrouter\.ai|api\.anthropic\.com|generativelanguage\.googleapis\.com|aiplatform\.googleapis\.com|bedrock.*amazonaws\.com|api\.mistral\.ai|api\.cohere\.ai|api\.groq\.com|api\.together\.xyz|api\.perplexity\.ai|api\.replicate\.com|api\.fireworks\.ai|openai\.azure\.com" . -g "*.js" -g "*.ts" -g "*.jsx" -g "*.tsx" -g "*.vue"

# Scan build outputs for likely keys (heuristic)
rg -a "sk-[A-Za-z0-9]{20,}|sk-ant-[A-Za-z0-9-]{20,}|sk-or-[A-Za-z0-9-]{20,}|AIza[0-9A-Za-z_-]{35}|hf_[A-Za-z0-9]{20,}" dist/ build/ .next/ 2>/dev/null

# Service account credentials and cloud auth files
rg -n "\"type\"\s*:\s*\"service_account\"|GOOGLE_APPLICATION_CREDENTIALS|AWS_ACCESS_KEY_ID|AWS_SECRET_ACCESS_KEY|AZURE_OPENAI_API_KEY" . -g "*.env*" -g "*.json"

Hardening Checklist
 AI provider keys only in server runtime (never in browser)
 .env.local and .env.*.local are gitignored
 Logs redact or omit secrets (request headers, env values)
 Build artifacts scanned before deploy
 Keys rotated if exposure suspected
Scripts
scripts/scan.sh - First-pass AI key leakage scan
Weekly Installs
45
Repository
igorwarzocha/op…orkflows
GitHub Stars
111
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass