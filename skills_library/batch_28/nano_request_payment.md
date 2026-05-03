---
title: nano-request-payment
url: https://skills.sh/casualsecurityinc/xno-skills/nano-request-payment
---

# nano-request-payment

skills/casualsecurityinc/xno-skills/nano-request-payment
nano-request-payment
Installation
$ npx skills add https://github.com/casualsecurityinc/xno-skills --skill nano-request-payment
SKILL.md
Request Payment from Operator

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

When you need XNO (e.g., for testing, for a task that requires funds, or because the operator offered), follow this workflow.

Workflow
Step 1: Check existing wallets

Before creating anything new, check what you already have:

Call wallets to see existing OWS wallets
Use the wallet://{name} resource or balance to check for existing funds
If an existing wallet has sufficient funds, skip to reporting — no request needed
Step 2: Create a payment request

Call payment_request_create:

amountXno: the amount needed (be specific)
reason: why you need the funds (be clear — the operator sees this)
walletName: optional — reuse an existing wallet, or omit to auto-select/create

This returns:

A nano: URI (shareable/QR-ready)
The target address
A request ID for tracking
Step 3: Present to the operator

Tell the operator:

How much you need and why
The nano: address to send to
Offer to generate a QR code (use nano-generate-qr skill or the generate_qr MCP tool if available)

Example message:

I need 0.1 XNO for [reason]. Please send to: nano_1abc... Or scan this QR: [generate QR]

Step 4: Wait and check for funds

After the operator says they've sent funds (or after a reasonable wait):

Call payment_request_receive with the request ID
This checks for pending blocks and receives them
Returns updated status: pending, partial, funded, or received

If status is partial, tell the operator how much more is needed.

Step 5: Report back

Once funds are received, confirm to the operator:

Amount received
Updated balance
That the funds are ready to use
Important Rules
Always check existing wallets first — don't create unnecessary wallets
Be specific about amounts and reasons — vague requests erode trust
Never claim funds were received without calling payment_request_receive — pending is not received in Nano
If the operator asks "did you get it?", always re-check — call payment_request_status or payment_request_receive
Related Skills
nano-mcp-wallet — wallet custody operations
nano-check-balance — manual balance checking
nano-generate-qr — QR code generation for payment addresses
nano-return-funds — returning funds to the operator
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
SocketWarn
SnykWarn