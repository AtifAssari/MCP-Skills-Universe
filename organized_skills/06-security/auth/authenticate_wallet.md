---
rating: ⭐⭐⭐
title: authenticate-wallet
url: https://skills.sh/fibrous-finance/fibx-skills/authenticate-wallet
---

# authenticate-wallet

skills/fibrous-finance/fibx-skills/authenticate-wallet
authenticate-wallet
Installation
$ npx skills add https://github.com/fibrous-finance/fibx-skills --skill authenticate-wallet
SKILL.md
Wallet Authentication

Manage the authentication session for the fibx CLI. Supports two methods: email OTP (via Privy server wallets) and private key import (local wallet).

Prerequisites
No active session required — this skill creates one
Rules
For email login, NEVER ask the user for a private key.
For private key import, ALWAYS warn the user first: "Your private key will be stored locally in a plaintext session file. Make sure your machine is secure. Shall I proceed?"
You MUST complete auth login before auth verify. They are sequential steps.
After successful auth verify or auth import, ALWAYS run npx fibx@latest status to confirm the session is active.
NEVER store or log private keys, OTP codes, or session tokens in conversation history.
Commands
Email OTP Login (2-step)
# Step 1: Send OTP to email
npx fibx@latest auth login <email>

# Step 2: Verify OTP code
npx fibx@latest auth verify <email> <code>

Private Key Import
npx fibx@latest auth import


INTERACTIVE COMMAND: This opens a prompt for the user to paste their private key. The agent CANNOT pass the key as a CLI argument. Instruct the user to enter it in the terminal prompt, or run it via the agent's terminal tool and let the user type the key.

Session Management
# Check current session status
npx fibx@latest status

# End session
npx fibx@latest auth logout

Parameters
Parameter	Type	Description	Required
email	string	User's email address	Yes (email OTP)
code	string	One-time password received via email	Yes (verify step)
Session Details
Privy sessions: JWT-based, 7-day expiry. After expiry, the user must re-authenticate via auth login.
Private key sessions: No expiry. Session persists until auth logout.
Storage: Sessions are stored as plaintext JSON in an OS-dependent config directory (e.g. ~/.config/fibx/session.json on Linux, ~/Library/Preferences/fibx-nodejs/session.json on macOS).
Examples

User: "Log me in with user@example.com"

npx fibx@latest auth login user@example.com
# Wait for user to provide the OTP code (e.g. "123456")
npx fibx@latest auth verify user@example.com 123456
npx fibx@latest status


User: "Import my private key"

# Warn user first, then:
npx fibx@latest auth import
npx fibx@latest status


User: "Log me out"

npx fibx@latest auth logout

Error Handling
Error	Action
Invalid code	Ask the user to check their email and retry verify.
Rate limit	Wait 60 seconds before retrying.
Session expired	Privy JWT expired (7 days). Restart from auth login.
Not authenticated	Run the full login flow before other skills.
Related Skills
Use status to verify your session is active before any operation.
Run balance after authentication to see available funds.
Run portfolio after authentication to see a full cross-chain overview with USD values.
Weekly Installs
17
Repository
fibrous-finance…x-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn