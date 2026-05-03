---
rating: ⭐⭐
title: gen-paylink-govilo
url: https://skills.sh/hau823823/gen-paylink-govilo/gen-paylink-govilo
---

# gen-paylink-govilo

skills/hau823823/gen-paylink-govilo/gen-paylink-govilo
gen-paylink-govilo
Installation
$ npx skills add https://github.com/hau823823/gen-paylink-govilo --skill gen-paylink-govilo
Summary

Package files into paid unlock links on Govilo with a single command.

Accepts ZIP files, folders, or individual files as input; non-ZIP inputs are automatically packaged into a ZIP (max 20 MB, 20 files per package)
Handles the full Govilo Bot API workflow: presign upload URL, upload to R2 storage, and create monetized item with unlock link
Requires GOVILO_API_KEY and SELLER_ADDRESS environment variables; seller address can also be passed via CLI parameter
Returns JSON output with unlock URL on success; always prompt user for product title, price (USDC), and optional description before execution
SKILL.md
Govilo To Go

Turn any file into a paid unlock link — one command to package, upload, and collect crypto payments. The last mile of automation: from creation to monetization.

Before Running

Always ask the user for these values before executing the CLI — never guess or use placeholders:

title — What is the product name?
price — How much to charge (in USDC)?
description — Short description of the product (optional, but always ask)
CLI Command

Requires uv. See references/setup-guide.md for install instructions.

Run from this skill's base directory. Use a dedicated env file containing only GOVILO_API_KEY (and optionally SELLER_ADDRESS). Never point --env-file at a project .env that contains unrelated secrets.

cd <skill_base_directory>
uv run --env-file <path_to>/.env.govilo create-link \
  --input <path>         \
  --title "Product Name" \
  --price "5.00"         \
  --address "0x..."      \
  --description "optional"


If no .env.govilo exists, create one before running:

GOVILO_API_KEY=sk_live_xxx
SELLER_ADDRESS=0x...


--input accepts ZIP file, folder, or individual files (repeatable). Non-ZIP inputs are auto-packaged.

All output is JSON {"ok": true/false, ...} with exit code 1 on failure.

Parameters
Param	Required	Source	Description
--input	Yes	CLI (repeatable)	ZIP, folder, or file paths
--title	Yes	CLI	Product title
--price	Yes	CLI	Price in USDC
--address	No	CLI > SELLER_ADDRESS env	Seller EVM wallet
--description	No	CLI	Product description
Workflow
Validate config (API Key + seller address)
Package inputs → ZIP (if not already ZIP)
POST /api/v1/bot/uploads/presign → get upload_url + session_id
PUT upload_url → upload ZIP to R2
POST /api/v1/bot/items → get unlock_url
File Limits
Max ZIP size: 20 MB
Max files in ZIP: 20
Setup

Two values are required:

Variable	Required	Description
GOVILO_API_KEY	Yes	Bot API key from govilo.xyz
SELLER_ADDRESS	Yes*	EVM wallet address on Base chain

*SELLER_ADDRESS can also be passed via --address CLI parameter.

See references/setup-guide.md for step-by-step registration and wallet setup instructions.

API Reference

See references/bot-api-quick-ref.md for Bot API endpoints and error codes.

Weekly Installs
3.0K
Repository
hau823823/gen-p…k-govilo
GitHub Stars
1
First Seen
4 days ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn