---
rating: ⭐⭐⭐
title: veil
url: https://skills.sh/bankrbot/openclaw-skills/veil
---

# veil

skills/bankrbot/openclaw-skills/veil
veil
Installation
$ npx skills add https://github.com/bankrbot/openclaw-skills --skill veil
SKILL.md
Veil

This skill wraps the @veil-cash/sdk CLI to make Veil operations agent-friendly.

Supported Assets
Asset	Decimals	Description
ETH	18	Native ETH (via WETH)
USDC	6	USDC on Base
What it does
Key management: generate and store a Veil keypair locally
Status check: verify configuration, registration, and relay health
Balances: veil balance (queue + private) — supports --pool eth|usdc
Deposits via Bankr: build Bankr-compatible unsigned transactions and ask Bankr to sign & submit (handles ERC20 approve + deposit for USDC)
Private actions: withdraw, transfer, merge for ETH or USDC — executed locally using VEIL_KEY (ZK/proof flow)
File locations (recommended)
Veil keys: ~/.clawdbot/skills/veil/.env.veil (chmod 600)
Bankr API key: ~/.clawdbot/skills/bankr/config.json
Quick start
1) Install the Veil SDK

Option A: Global npm install (recommended)

npm install -g @veil-cash/sdk


Option B: Clone from GitHub

mkdir -p ~/.openclaw/workspace/repos
cd ~/.openclaw/workspace/repos
git clone https://github.com/veildotcash/veildotcash-sdk.git
cd veildotcash-sdk
npm ci && npm run build

2) Configure Base RPC (recommended)

Veil queries a lot of blockchain data (UTXOs, merkle proofs, etc.), so public RPCs will likely hit rate limits. A dedicated RPC from Alchemy, Infura, or similar is recommended.

Put RPC_URL=... in one of these:

~/.clawdbot/skills/veil/.env (preferred)
or the SDK repo .env (less ideal)

Example:

mkdir -p ~/.clawdbot/skills/veil
cat > ~/.clawdbot/skills/veil/.env << 'EOF'
RPC_URL=https://base-mainnet.g.alchemy.com/v2/YOUR_KEY
EOF
chmod 600 ~/.clawdbot/skills/veil/.env

3) Make scripts executable
chmod +x scripts/*.sh

4) Generate your Veil keypair
scripts/veil-init.sh
scripts/veil-keypair.sh

5) Check your setup
scripts/veil-status.sh

6) Find your Bankr Base address
scripts/veil-bankr-prompt.sh "What is my Base wallet address? Respond with just the address."

7) Check balances
# ETH pool (default)
scripts/veil-balance.sh --address 0xYOUR_BANKR_ADDRESS

# USDC pool
scripts/veil-balance.sh --address 0xYOUR_BANKR_ADDRESS --pool usdc

8) Deposit via Bankr (sign & submit)
# Deposit ETH
scripts/veil-deposit-via-bankr.sh ETH 0.011 --address 0xYOUR_BANKR_ADDRESS

# Deposit USDC (auto-handles approve + deposit)
scripts/veil-deposit-via-bankr.sh USDC 100 --address 0xYOUR_BANKR_ADDRESS

9) Withdraw (private to public)
scripts/veil-withdraw.sh ETH 0.007 0xYOUR_BANKR_ADDRESS
scripts/veil-withdraw.sh USDC 50 0xRECIPIENT

10) Transfer privately
scripts/veil-transfer.sh ETH 0.01 0xRECIPIENT
scripts/veil-transfer.sh USDC 25 0xRECIPIENT

11) Merge UTXOs
scripts/veil-merge.sh ETH 0.1
scripts/veil-merge.sh USDC 100

References
SDK Reference — CLI commands, environment variables, error codes
Troubleshooting — Common issues and debugging tips
Notes
For Bankr signing, this skill uses Bankr's Agent API via your local ~/.clawdbot/skills/bankr/config.json.
For USDC deposits via Bankr, the skill automatically submits the ERC20 approval transaction first, then the deposit transaction.
For privacy safety: never commit .env.veil or .env files to git.
Weekly Installs
101
Repository
bankrbot/openclaw-skills
GitHub Stars
1.1K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn