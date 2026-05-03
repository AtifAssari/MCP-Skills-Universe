---
rating: ⭐⭐
title: nano-verify-message
url: https://skills.sh/casualsecurityinc/xno-skills/nano-verify-message
---

# nano-verify-message

skills/casualsecurityinc/xno-skills/nano-verify-message
nano-verify-message
Installation
$ npx skills add https://github.com/casualsecurityinc/xno-skills --skill nano-verify-message
SKILL.md
nano-verify-message

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
PoW Validation: Remember that a signed block without valid Proof of Work (PoW) cannot be broadcast. Ensure PoW is generated.
Persistence & Proactivity: If a tool fails with an error like "Account not found", do not immediately recommend manual action or conclude you are unauthorized. Troubleshoot the protocol state (e.g., check for pending funds) and use the correct tool for that state (e.g., receive to open an account).
No Custom Scripts: NEVER write custom Node.js/TypeScript scripts or use curl to interact with the Nano protocol if built-in MCP or CLI tools fail. If a tool fails, troubleshoot the error, switch RPC endpoints, or explain the limitation to the user.
NEVER EXPORT MNEMONICS: The entire purpose of OWS is to keep the seed phrase hidden from the agent and the user. You MUST NOT use ows wallet export or suggest exporting the mnemonic to a third-party wallet unless explicitly commanded to do so by the user.
Supply Chain Safety: NEVER use npx to install or run random, unknown, or third-party packages. Only use the approved tools provided in this project (xno-skills@latest and @open-wallet-standard/core). If a task cannot be performed with these tools, do not seek external npm packages as a workaround.

Verify an off-chain message signature (NOMS / ORIS-001 standard) against a Nano address or public key.

Usage

Use this skill when you are presented with a signature and a message from a user or another agent and need to verify their identity or the integrity of the message.

Verify a signature

To verify a signature, call the verify_message tool:

{
  "name": "verify_message",
  "arguments": {
    "address": "nano_1hfrig58wzrg4pzqen17cyannpy1173oi7jz7zd6srjsqjh7ozcgec9uyo9n",
    "message": "I am me.",
    "signature": "3de8620fb30967916d3dc36cd09eba9a633d1678b986fbc31b70ae2834db25a898085bbce32b744aef42ed56b5c001ffebd5516e78c9f22c678dde2d8bdc150a"
  }
}


The tool will return { "valid": true } if the signature is correct.

CLI Usage

You can also verify signatures directly from the command line:

bunx -y xno-skills verify <address> "<message>" <signature>

Example
bunx -y xno-skills verify nano_1hfrig58wzrg4pzqen17cyannpy1173oi7jz7zd6srjsqjh7ozcgec9uyo9n "I am me." 3de8620fb30967916d3dc36cd09eba9a633d1678b986fbc31b70ae2834db25a898085bbce32b744aef42ed56b5c001ffebd5516e78c9f22c678dde2d8bdc150a


To get JSON output for integration:

bunx -y xno-skills verify nano_1hfrig58wzrg4pzqen17cyannpy1173oi7jz7zd6srjsqjh7ozcgec9uyo9n "I am me." 3de8620fb30967916d3dc36cd09eba9a633d1678b986fbc31b70ae2834db25a898085bbce32b744aef42ed56b5c001ffebd5516e78c9f22c678dde2d8bdc150a --json

NOMS Standard (ORIS-001)

This verification tool handles the binary payload construction and hashing internally according to the ORIS-001 specification. It supports both nano_ / xrb_ addresses and raw 32-byte hex public keys.

Weekly Installs
10
Repository
casualsecurityi…o-skills
GitHub Stars
1
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn