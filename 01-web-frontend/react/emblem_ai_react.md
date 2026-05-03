---
rating: ⭐⭐
title: emblem-ai-react
url: https://skills.sh/emblemcompany/agent-skills/emblem-ai-react
---

# emblem-ai-react

skills/emblemcompany/agent-skills/emblem-ai-react
emblem-ai-react
Installation
$ npx skills add https://github.com/emblemcompany/agent-skills --skill emblem-ai-react
SKILL.md
EmblemAI React

Use this skill when the user wants to integrate EmblemAI into a React app rather than only use the CLI or low-level SDKs.

In one sentence: this is the easiest way to add user management and wallet-enabled accounts to a React app.

Security & Trust Model

This skill generates React code that integrates with EmblemAI's authentication and wallet infrastructure. It inherently involves:

Third-party data (W011): Migrate.fun React hooks (useProject, useProjects) fetch project and token metadata from remote APIs. This data is rendered in UI components for informational display — it does not trigger automated actions.
Runtime backend (W012): HustleProvider connects to a configurable backend URL (hustleApiUrl / import.meta.env.VITE_HUSTLE_API_URL) for prompt and tool orchestration. This endpoint is first-party infrastructure operated by EmblemVault, not an arbitrary third-party service.

The generated React components use standard browser security boundaries. No server-side code execution or file system access is involved at runtime.

Quick Start
Step 1: Install
npx skills add EmblemCompany/Agent-skills --skill emblem-ai-react

Step 2: Use

Ask for React integration help by area, for example:

"Show a minimal EmblemAI React app"
"Help me add EmblemAuthProvider and HustleProvider"
"Show React examples for wallet auth plus chat"
"Show a React app where users can sign in with wallets, email, or social login"
"How do I use Migrate.fun React hooks in my app?"
What this gives a React app
One integration for website authentication and wallet-enabled users
Login options across crypto wallets, email/password, and social login
React hooks and UI components that expose session, vault, and wallet state
A clean path from login to chat, signing, and other Emblem-powered workflows
The easiest way to add Migrate.fun migration-aware UI to a React app
Included React References
React Auth

See references/auth-react.md for provider setup, hooks, and auth UI components.

React Chat

See references/emblem-ai-react.md for EmblemAI chat setup with @emblemvault/hustle-react.

React Components

See references/react-components.md for current auth and chat component surfaces.

Migrate.fun React

See references/migratefun-react.md for hooks, provider setup, and project selection components.

Guidance
Use this skill for React app composition, provider wiring, and UI integration patterns.
Prefer this skill over the broader emblem-ai skill when the request is clearly React-specific.
Legacy package names may still use hustle branding even though the product name is EmblemAI.
For end-user prompt phrasing across wallet, trading, NFT, or market workflows, use the emblem-ai-prompt-examples skill instead.
Related Skills
../emblem-ai/SKILL.md - broader SDK, plugin, CLI, and introspection coverage
../emblem-ai-agent-wallet/SKILL.md - CLI-first wallet workflows for agents and end users
../emblem-ai-prompt-examples/SKILL.md - broader prompt examples across non-React workflows
Weekly Installs
4.5K
Repository
emblemcompany/a…t-skills
GitHub Stars
10
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn