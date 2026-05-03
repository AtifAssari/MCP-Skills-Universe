---
rating: ⭐⭐
title: sanitize
url: https://skills.sh/vxcozy/sanitize/sanitize
---

# sanitize

skills/vxcozy/sanitize/sanitize
sanitize
Installation
$ npx skills add https://github.com/vxcozy/sanitize --skill sanitize
SKILL.md

Run a comprehensive 12-point security sanitization audit on the current repository. This checks for secrets, credentials, and sensitive data that should never be committed.

Checks

For each repository in the project, scan all tracked and staged files:

Full file audit — Run git status to list all modified/untracked files. Review what's about to be committed.
Private keys / mnemonics — Grep for 64-char hex strings (0x + 64 hex), BEGIN PRIVATE KEY, mnemonic =, seed phrase
API keys / tokens / secrets — Grep for sk-*, AKIA*, ghp_*, glpat-*, xox[bpsa]-*, Bearer tokens, api_key=, api_secret=
.env files — Check if any .env* files (except .env.example) are tracked by git with git ls-files '*.env*'
.mcp.json — Check if .mcp.json is tracked (often contains plaintext private keys)
config.json / config files — Check tracked config.json, settings.json, credentials.* files for secret-like values (private_key, secret, password, token)
Plaintext passwords — Grep for password=, passwd=, pwd= with literal (non-env-var) values
RPC URLs with embedded keys — Grep for Infura/Alchemy/QuickNode/Moralis URLs containing inline API keys
Real wallet addresses — Flag Ethereum addresses (0x + 40 hex) in non-test source files for manual review. Ignore dummy addresses (0x0000..., 0xaAaA..., 0xdead..., 0xbeef...)
console.log leaking data — Grep for console.log/debug/info statements referencing key/secret/token/password/mnemonic/credential
.gitignore coverage — Verify .gitignore includes: .env, .env.local, .mcp.json, config.json, .claude/, node_modules
Test files with real credentials — Scan .test.* / .spec.* files for production API keys or tokens (sk-, AKIA, ghp_*)
Pre-commit hook

This skill includes a bash pre-commit hook (scripts/pre-commit-sanitize) that runs the same 12 checks automatically on every git commit. Install it with:

./scripts/install-hooks.sh /path/to/your/repo

Output

Report each check as PASS, WARN, or FAIL with specific file:line references for any findings. Summarize at the end with total pass/warn/fail counts.

Rules
Dummy/test addresses (0xaAaA..., 0xdead..., 0x0000...) are OK — don't flag
.env.example with placeholders is OK
Variable names and type definitions mentioning "key" or "secret" are OK — only flag actual literal values
Focus on git diff and staged content when possible, not entire file history
If the repository has a pre-commit hook installed, note that and still run the full audit independently
Weekly Installs
12
Repository
vxcozy/sanitize
GitHub Stars
19
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass