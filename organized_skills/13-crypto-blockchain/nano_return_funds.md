---
rating: ⭐⭐
title: nano-return-funds
url: https://skills.sh/casualsecurityinc/xno-skills/nano-return-funds
---

# nano-return-funds

skills/casualsecurityinc/xno-skills/nano-return-funds
nano-return-funds
Installation
$ npx skills add https://github.com/casualsecurityinc/xno-skills --skill nano-return-funds
SKILL.md
Return Funds to Sender

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

When the operator asks you to return funds (e.g., "send it back", "return the XNO", "refund"), follow this workflow carefully.

Core Safety Rule

NEVER guess the refund destination. If there is any ambiguity about where to send funds, ALWAYS ask the operator to confirm.

Workflow
Step 1: Identify what to return

If the request is linked to a payment request:

Call payment_request_refund with the request ID and execute: false
This returns source addresses from received blocks

If no payment request exists:

Call history to see recent transactions
Identify receive transactions and their source addresses
Step 2: Evaluate ambiguity

The system will tell you if the refund target is clear or ambiguous:

Single source (clear):

One address sent all the funds
Present the address and amount to the operator for confirmation
Example: "I received 0.1 XNO from nano_1abc.... Shall I return it there?"

Multiple sources (ambiguous):

Different addresses sent funds
List ALL candidates with amounts
Ask the operator which address to refund to
Example: "I received funds from multiple addresses:
nano_1abc... — 0.05 XNO
nano_3def... — 0.05 XNO Which address should I return funds to?"

No sources found:

No received funds to return
Tell the operator: "No incoming transactions found to refund."
Step 3: Confirm and execute

After the operator confirms the destination:

Call payment_request_refund with execute: true and confirmAddress: "<confirmed address>"
Or use send directly if not linked to a payment request
Report the send hash and updated balance
Important Rules
Always confirm before sending — even if there's only one source
Show the full address — don't abbreviate, let the operator verify
If the operator says "send it back" without context, check payment_request_list for recent requests, then history for recent receives
Partial refunds are OK — if the operator asks to return only part of the funds, respect that
Check allowance limits — if spending limits are set, the refund may need operator approval to increase limits first
Log everything — all refund operations are tracked in transaction history
Edge Cases
"Return everything"
Check total balance across all wallet accounts
List all accounts with balances
Confirm with operator before draining accounts
"Return to [specific address]"
Validate the address first (validate_address)
Confirm amount
Send directly — no need to match against sources
Allowance blocks the refund

If spending limits prevent the refund:

Tell the operator: "The current spending limit prevents this send. Please increase the limit via config_set({ maxSendXno: \"...\" }) or confirm you'd like to proceed."
Related Skills
nano-request-payment — the inbound counterpart
nano-mcp-wallet — wallet operations
nano-validate-address — verify addresses before sending
Weekly Installs
10
Repository
casualsecurityi…o-skills
GitHub Stars
1
First Seen
3 days ago
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn