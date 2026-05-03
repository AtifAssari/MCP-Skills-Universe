---
rating: ⭐⭐⭐
title: nano-convert-units
url: https://skills.sh/casualsecurityinc/xno-skills/nano-convert-units
---

# nano-convert-units

skills/casualsecurityinc/xno-skills/nano-convert-units
nano-convert-units
Installation
$ npx skills add https://github.com/casualsecurityinc/xno-skills --skill nano-convert-units
SKILL.md
Convert XNO Units

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

Convert between different XNO cryptocurrency units with BigInt precision. XNO uses 30 decimal places, making floating-point arithmetic unsafe. Always use this skill for accurate conversions.

Unit Reference
Unit	Raw Value	Decimal Places	Description
raw	1	0	Smallest unit (base unit)
mnano	10^24	24	Mega-nano (0.000001 XNO)
knano	10^27	27	Kilonano (0.001 XNO)
XNO	10^30	30	Base unit (1 XNO)
Conversion Factors
1 XNO    = 1,000 knano = 1,000,000 mnano = 10^30 raw
1 knano  = 1,000 mnano = 10^27 raw
1 mnano  = 10^24 raw

CLI Usage
Basic Syntax
bunx -y xno-skills convert <amount> <from-unit>


The command outputs the value in all supported units (raw, xno, knano, mnano). Use --json for machine-readable output.

Examples
# Convert 1 XNO — shows value in all units
bunx -y xno-skills convert 1 xno

# Convert raw to human-readable
bunx -y xno-skills convert 1000000000000000000000000000000 raw

# Convert 0.5 XNO
bunx -y xno-skills convert 0.5 xno

# Smaller units
bunx -y xno-skills convert 1 knano
bunx -y xno-skills convert 1 mnano

# JSON output (for scripts)
bunx -y xno-skills convert 1 xno --json

MCP Usage

If you have access to xno-mcp tools, use convert_units:

{
  "name": "convert_units",
  "arguments": { "amount": "1.5", "from": "xno", "to": "raw" }
}

Precision Handling
Why BigInt?

XNO uses 30 decimal places, which exceeds JavaScript's safe integer limit (15-17 digits). Floating-point arithmetic causes precision loss:

// WRONG - Floating point loses precision
const wrong = 0.1 + 0.2; // 0.30000000000000004

// RIGHT - BigInt maintains precision
const correct = BigInt("1000000000000000000000000000000");

Implementation Notes
All conversions use BigInt internally - No floating-point operations
Input parsing - Decimal strings converted to BigInt raw units
Output formatting - BigInt raw units converted to requested unit
No precision loss - Exact conversions for any amount
Common Precision Pitfalls
// DON'T use Number for XNO amounts
const wrong = 1.5; // Loses precision at 30 decimals

// DO use string input for CLI
// bunx -y xno-skills convert "1.5" xno

Quick Reference
bunx -y xno-skills convert 1 xno        # shows raw, knano, mnano equivalents
bunx -y xno-skills convert 1 knano      # 0.001 XNO
bunx -y xno-skills convert 1 mnano      # 0.000001 XNO
bunx -y xno-skills convert 1 raw        # 0.000000000000000000000000000001 XNO

Related Skills
nano-create-wallet - Generate XNO wallet with seed phrase
nano-validate-address - Validate XNO addresses (BIP-44, legacy)
Weekly Installs
11
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