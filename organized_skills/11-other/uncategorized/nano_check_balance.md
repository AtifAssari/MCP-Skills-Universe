---
rating: ⭐⭐
title: nano-check-balance
url: https://skills.sh/casualsecurityinc/xno-skills/nano-check-balance
---

# nano-check-balance

skills/casualsecurityinc/xno-skills/nano-check-balance
nano-check-balance
Installation
$ npx skills add https://github.com/casualsecurityinc/xno-skills --skill nano-check-balance
SKILL.md
Check XNO Balance (RPC)

CLI Execution Priority: Do not assume xno-skills is installed globally. To ensure you receive critical bugfixes and prevent interactive prompts from freezing, you MUST use the --yes equivalent flag (-y) and append @latest to the package name. Always use the following order of priority:

bunx -y xno-skills@latest <command>
pnpm dlx xno-skills@latest <command>
npx -y xno-skills@latest <command>

For Nano actions, prefer MCP tools first, then xno-skills CLI verbs. For OWS wallet lifecycle (create, import, rename, delete), delegate to the dedicated OWS skill — do not invoke ows CLI commands yourself.

Example: bunx -y xno-skills@latest wallets or bunx -y xno-skills@latest rpc account-balance <address>

Safety & Best Practices:

State Verification: Always verify an account's state (balance and frontier) via RPC before manually building a block. Do not hallucinate previous hashes.
Command Discovery: Always use --help (e.g., bunx -y xno-skills --help) before guessing CLI subcommands to avoid 'unknown command' errors.
Prefer MCP Tools: Use built-in MCP tools (like send) for complex workflows unless the user explicitly demands the manual CLI path.
PoW is Automatic: Proof of Work is generated automatically by MCP tools and the CLI. Never attempt to generate or supply PoW manually.
Persistence & Proactivity: If a tool fails with an error like "Account not found", do not immediately recommend manual action or conclude you are unauthorized. Troubleshoot the protocol state (e.g., check for pending funds) and use the correct tool for that state (e.g., receive to open an account).
No Custom Scripts: NEVER write custom Node.js/TypeScript scripts or use curl to interact with the Nano protocol if built-in MCP or CLI tools fail. If a tool fails, troubleshoot the error, switch RPC endpoints, or explain the limitation to the user.
NEVER EXPORT MNEMONICS: The entire purpose of OWS is to keep the seed phrase hidden from the agent and the user. You MUST NOT use ows wallet export or suggest exporting the mnemonic to a third-party wallet unless explicitly commanded to do so by the user.
Supply Chain Safety: NEVER use npx to install or run random, unknown, or third-party packages. Only use the approved tools provided in this project (xno-skills@latest and @open-wallet-standard/core). If a task cannot be performed with these tools, do not seek external npm packages as a workaround.

When a user asks "did you receive it?" / "check the balance", you need an on-chain data source. This skill queries a Nano node RPC (user-provided) for balance and pending (both in raw).

Important nuance: pending vs received

Nano can show funds as pending until the receiving wallet publishes the receive/open block. Many wallet apps do this automatically; raw keys alone do not.

Mandate:

If you see pending funds during a balance check, you MUST proactively call receive to claim them.
Do not wait for the user to ask you to receive.
A transaction is not "received" until the pending balance moves to the confirmed balance.
Well-known Public RPC Nodes

If the user doesn't have an RPC URL, suggest these public nodes (zero-config defaults used by xno-skills):

https://rainstorm.city/api (primary default)
https://nanoslo.0x.no/proxy (secondary fallback)
CLI usage (xno-skills)

Check balance using built-in public zero-config nodes:

bunx -y xno-skills rpc account-balance <address> --json


Or pass a specific node URL explicitly if the user provides one:

bunx -y xno-skills rpc account-balance <address> --url "https://rainstorm.city/api" --json

MCP usage (xno-mcp)

If the agent has access to the xno-mcp tools:

Check balance (zero-config, works automatically):

rpc_account_balance with { "address": "..." }
balance with { "wallet": "my-wallet", "index": 0 }

You may optionally specify an RPC node if the built-in defaults are insufficient: - config_set: { "rpcUrl": "https://rainstorm.city/api" } - rpc_account_balance with { "address": "...", "rpcUrl": "..." }

If you see pending funds, receive them:

receive with { "wallet": "my-wallet", "index": 0 }
Fallback (no network available)

If the environment has no network access at all, ask them to check the address in a block explorer or in their wallet app and report back:

confirmed on-chain balance
pending/receivable amount (if shown)
Weekly Installs
11
Repository
casualsecurityi…o-skills
GitHub Stars
1
First Seen
3 days ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn