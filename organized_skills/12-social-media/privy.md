---
rating: ⭐⭐
title: privy
url: https://skills.sh/site/docs.privy.io/privy
---

# privy

skills/docs.privy.io/Privy
Privy
$ npx skills add https://docs.privy.io
SKILL.md
Privy Skill Reference
Product summary

Privy is an authentication and wallet infrastructure platform that enables developers to onboard users with wallets, create self-custodial embedded wallets, and securely sign transactions. It provides three interconnected layers: authentication (email, social, passkeys, wallets), wallets (embedded or external, across 50+ blockchains), and controls (owners, signers, policies).

Key files and entry points:

Dashboard: https://dashboard.privy.io — create apps, manage credentials, configure login methods
App ID & Secret: Required for all API calls; found in Dashboard under app settings
Client SDKs: React (@privy-io/react-auth), React Native, Swift, Android, Flutter, Unity
Server SDKs: Node.js (@privy-io/node), Python, Java, Go, Rust
REST API: https://api.privy.io/v1/ — direct wallet and user management
Webhooks: Subscribe to user, wallet, transaction, and intent events

Primary docs: https://docs.privy.io

When to use

Reach for this skill when:

Building user onboarding: Implementing email, social, passkey, or wallet-based login
Creating wallets: Provisioning embedded wallets for users or application-owned wallets via API
Signing transactions: Requesting signatures from wallets on Ethereum, Solana, or other chains
Managing access control: Setting up owners, signers, and policies to control who can do what with wallets
Handling user state: Creating users, linking accounts, managing custom metadata, or querying user objects
Monitoring activity: Setting up webhooks for user, wallet, transaction, or intent events
Configuring dashboard: Setting up apps, login methods, appearance, team roles, or SSO
Quick reference
SDK initialization
Platform	Code
React	<PrivyProvider appId="..." clientId="..." config={{...}}>
React Native	<PrivyProvider appId="..." clientId="..." config={{...}}>
Node.js	new PrivyClient({appId: '...', appSecret: '...'})
Python	PrivyClient(app_id='...', app_secret='...')
Java	PrivyClient.builder().appId(...).appSecret(...).build()
REST API	Basic auth: -u "app-id:app-secret"
Common API endpoints
Task	Endpoint	Method
Create wallet	POST /v1/wallets	Create embedded or app-owned wallet
Get wallet	GET /v1/wallets/{wallet_id}	Fetch wallet details
Send transaction	POST /v1/wallets/{wallet_id}/rpc	Sign and send via RPC
Create user	POST /v1/users	Create user object
Get user	GET /v1/users/{user_id}	Fetch user by ID
Create policy	POST /v1/policies	Define wallet action rules
Get policy	GET /v1/policies/{policy_id}	Fetch policy details
Create key quorum	POST /v1/key-quorums	Set up multi-sig approval
Configuration options (PrivyProvider)
config={{
  embeddedWallets: {
    ethereum: { createOnLogin: 'users-without-wallets' },
    solana: { createOnLogin: 'users-without-wallets' }
  },
  loginMethods: {
    email: true,
    sms: true,
    wallet: true,
    passkey: true,
    oauth: ['google', 'discord']
  },
  appearance: { theme: 'dark' },
  externalWallets: { ... }
}}

Wallet ownership models
Model	Owner	Use case
User-owned	User only	Self-custodial consumer wallets
User + server	User + authorization key	Automated trading, limit orders
App-owned	Authorization key	Treasury, agents, bots
Custodial	Licensed custodian	FBO banking model
Decision guidance
When to use embedded vs. external wallets
Scenario	Embedded	External
New users, no crypto experience	✓	
Users have existing wallets (MetaMask, Phantom)		✓
Need seamless onboarding UX	✓	
Users want to bring their own keys		✓
Multi-chain support required	✓	✓
Custody and key management needed	✓	
When to use Privy auth vs. JWT-based auth
Scenario	Privy auth	JWT-based
Building from scratch	✓	
Existing auth provider (Auth0, Firebase)		✓
Need email, social, passkey, wallet login	✓	
Want to keep existing auth system		✓
Multi-method login required	✓	✓
When to use policies vs. signers
Scenario	Policies	Signers
Enforce transaction limits	✓	
Restrict recipient addresses	✓	
Grant scoped permissions to server		✓
Require multi-sig approval		✓
Prevent contract interactions	✓	
Delegate specific actions		✓
Workflow
1. Set up your app
Go to https://dashboard.privy.io and create a new app
Copy your App ID and App Secret (keep secret safe)
Configure login methods (email, social, wallet, passkey)
Set allowed domains and redirect URIs
Create app clients for different environments (dev, staging, prod)
2. Initialize Privy in your client
Install SDK: npm install @privy-io/react-auth (or appropriate SDK)
Wrap your app with PrivyProvider at the root
Pass appId and clientId from Dashboard
Configure embeddedWallets to auto-create on login if desired
Wait for ready flag before consuming Privy state
3. Authenticate users
Use usePrivy() hook to access login and logout methods
Call login() to show Privy modal or use direct login methods (loginWithCode, useLoginWithOAuth)
Access authenticated user via user from usePrivy() hook
Verify user identity on backend using identity tokens
4. Create or access wallets

Client-side (React):

Use useWallets() hook to get user's wallets
Call createWallet() from useCreateWallet() to create new wallet
Access wallet address and chain type from wallet object

Server-side (Node.js):

Initialize PrivyClient with app ID and secret
Call privy.wallets().create({chain_type: 'ethereum', owner: {user_id: '...'}}) to create user wallet
Or call with {public_key: '...'} to create app-owned wallet
5. Sign transactions

Client-side (React):

Use useSignTransaction() or chain-specific hooks (useSignEthereumTransaction, useSignSolanaTransaction)
Prepare transaction object with recipient, amount, data
Call sign method; user approves in modal
Transaction is signed and broadcast

Server-side (Node.js):

Create authorization context with authorization key or user JWT
Call privy.wallets().ethereum().sendTransaction(walletId, {...}, authContext)
Include privy-authorization-signature header with signature
6. Set up controls and policies
Create authorization key in Dashboard (for app-owned wallets)
Create policy via API: POST /v1/policies with rules and conditions
Attach policy to wallet at creation: policy_ids: ['policy-id']
Define rules (ALLOW/DENY) with conditions (amount, recipient, method)
Test policy by attempting restricted action
7. Monitor with webhooks
Go to Dashboard > Webhooks and register endpoint
Subscribe to events: user.created, user.authenticated, wallet.funds_deposited, transaction.confirmed
Verify webhook signature using app secret
Parse payload and update your backend state
Implement retry logic for failed deliveries
Common gotchas
Missing ready flag: Don't consume Privy state before ready === true — causes stale data
App secret exposure: Never expose app secret in client code; use only on backend
Authorization signature required: Server-side wallet actions require privy-authorization-signature header; missing it causes 401 errors
Policy not enforced: Policies are evaluated at request time in secure enclaves; ensure policy is attached to wallet at creation
Wallet creation rate limits: Batch wallet creation or implement exponential backoff; hitting 429 errors means you need retry logic
User JWT expiry: User JWTs expire; refresh them before they expire or re-authenticate
Idempotency keys: Use idempotency keys for wallet creation to prevent duplicates; key must be unique per request
Chain type mismatch: Ensure wallet chain type matches the transaction you're signing (Ethereum wallet can't sign Solana transactions)
External wallet not connected: Check user.linkedAccounts to verify external wallet is connected before attempting to use it
Webhook signature verification: Always verify webhook signature using HMAC-SHA256 with app secret; don't trust unsigned payloads
Verification checklist

Before submitting work with Privy:

 App ID and secret are correctly configured (secret not exposed in client code)
 PrivyProvider wraps the entire app and ready flag is checked before using Privy
 Wallet creation includes appropriate owner (user ID for user wallets, authorization key for app wallets)
 Policies are attached to wallets if access control is needed
 Authorization signatures are included in server-side requests
 Idempotency keys are used for wallet creation to prevent duplicates
 Webhook endpoints are registered and signatures are verified
 User identity tokens are verified on backend before trusting user claims
 Error handling covers rate limits (429), authorization failures (401), and invalid requests (400)
 Tested with both embedded and external wallets if applicable
 Tested across target chains (Ethereum, Solana, etc.)
Resources

Comprehensive navigation: https://docs.privy.io/llms.txt — full page-by-page listing for agent reference

Critical docs:

Key Concepts — understand authentication, wallets, controls, and ownership models
React Setup — initialize Privy in React apps
API Reference — REST API endpoints, authentication, webhooks

For additional documentation and navigation, see: https://docs.privy.io/llms.txt

Weekly Installs
140
Source
docs.privy.io
First Seen
Mar 27, 2026