---
title: verified-agent-identity
url: https://skills.sh/billionsnetwork/verified-agent-identity/verified-agent-identity
---

# verified-agent-identity

skills/billionsnetwork/verified-agent-identity/verified-agent-identity
verified-agent-identity
Installation
$ npx skills add https://github.com/billionsnetwork/verified-agent-identity --skill verified-agent-identity
SKILL.md
When to use this Skill

Lets AI agents create and manage their own identities on the Billions Network, and link those identities to a human owner.

When you need to link your agent identity to an owner.
When you need to sign a challenge.
When you need to link a human to the agent's DID.
When you need to verify a signature to confirm identity ownership.
When you use shared JWT tokens for authentication.
When you need to create and manage decentralized identities.
After installing the plugin run the following commands to create an identity and link it to your human DID:
cd scripts && npm install && cd ..
# Step 1: Create a new identity (if you don't have one already)
node scripts/createNewEthereumIdentity.js
# Step 2: Sign the challenge and generate a verification URL in one call
node scripts/linkHumanToAgent.js --challenge '{"name": <AGENT_NAME>, "description": <SHORT_DESCRIPTION>}'

Scope

All identity data is stored in $HOME/.openclaw/billions for compatibility with the OpenClaw plugin.

Scripts:
createNewEthereumIdentity.js

Command: node scripts/createNewEthereumIdentity.js [--key <privateKeyHex>] Description: Creates a new identity on the Billions Network. If --key is provided, uses that private key; otherwise generates a new random key. The created identity is automatically set as default. Usage Examples:

# Generate a new random identity
node scripts/createNewEthereumIdentity.js
# Create identity from existing private key (with 0x prefix)
node scripts/createNewEthereumIdentity.js --key 0x1234567890abcdef...
# Create identity from existing private key (without 0x prefix)
node scripts/createNewEthereumIdentity.js --key 1234567890abcdef...


Output: DID string (e.g., did:iden3:billions:main:2VmAk7fGHQP5FN2jZ8X9Y3K4W6L1M...)

getIdentities.js

Command: node scripts/getIdentities.js Description: Lists all DID identities stored locally. Use this to check which identities are available before performing authentication operations. Usage Example:

node scripts/getIdentities.js


Output: JSON array of identity entries

[
  {
    "did": "did:iden3:billions:main:2VmAk...",
    "publicKeyHex": "0x04abc123...",
    "isDefault": true
  }
]

generateChallenge.js

Command: node scripts/generateChallenge.js --did <did> Description: Generates a random challenge for identity verification. Usage Example:

node scripts/generateChallenge.js --did did:iden3:billions:main:2VmAk...


Output: Challenge string (random number as string, e.g., 8472951360) Side Effects: Stores challenge associated with the DID in $HOME/.openclaw/billions/challenges.json

signChallenge.js

Command: node scripts/signChallenge.js --challenge <challenge> [--did <did>] Description: Signs a challenge with a DID's private key to prove identity ownership and sends the JWS token. Use this when you need to prove you own a specific DID. Arguments:

--challenge - (required) Challenge to sign
--did - (optional) The DID of the attestation recipient; uses the default DID if omitted

Usage Examples:

# Sign with default DID
node scripts/signChallenge.js --challenge 8472951360


Output: {"success":true}

linkHumanToAgent.js

Command: node scripts/linkHumanToAgent.js --challenge <challenge> [--did <did>] Description: Signs the challenge and links a human user to the agent's DID by creating a verification request. Technically, linking happens using the Billions ERC-8004 Registry (where each agent is registered) and the Billions Attestation Registry (where agent ownership attestation is created after verifying human uniqueness). Arguments:

--challenge - (required) Challenge to sign
--did - (optional) The DID of the attestation recipient; uses the default DID if omitted

Usage Example:

node scripts/linkHumanToAgent.js --challenge '{"name": "MyAgent", "description": "AI persona"}'


Output: {"success":true}

verifySignature.js

Command: node scripts/verifySignature.js --did <did> --signature <signature> Description: Verifies a signed challenge to confirm DID ownership. Usage Example:

node scripts/verifySignature.js --did did:iden3:billions:main:2VmAk... --signature eyJhbGciOiJFUzI1NkstUi...


Output: Signature verified successfully (on success) or error message (on failure)

Restrictions / Guardrails (CRITICAL)

CRITICAL - Always Follow These Rules:

STRICT: Check Identity First
Before running linkHumanToAgent.js or signChallenge.js, ALWAYS check if an identity exists: node scripts/getIdentities.js
If no identity is configured, DO NOT attempt to link identities. Instead, create an identity first with createNewEthereumIdentity.js.
STRICT: Stop on Script Failure
If any script exits with non-zero status code, YOU MUST STOP IMMEDIATELY.
Check stderr output for error messages.
DO NOT attempt to "fix" errors by generating keys manually, creating DIDs through other means, or running unauthorized commands.
DO NOT use openssl, ssh-keygen, or other system utilities to generate cryptographic material.
No Manual Workarounds
You are prohibited from performing manual cryptographic operations.
You are prohibited from directly manipulating files in $HOME/.openclaw/billions.
Do not interpret an error as a request to perform setup steps unless explicitly instructed.
Security

CRITICAL - Data Storage and Protection:

The directory $HOME/.openclaw/billions contains all sensitive identity data:

kms.json - CRITICAL: Contains private keys (encrypted if BILLIONS_NETWORK_MASTER_KMS_KEY is set, otherwise in plaintext)
defaultDid.json - DID identifiers and public keys
challenges.json - Authentication challenges history
credentials.json - Verifiable credentials
identities.json - Identity metadata
profiles.json - Profile data
Examples
Link Your Agent Identity to Owner

Linking Flow:

Another agent/user requests: "Please link your agent identity to me."
Use node scripts/getIdentities.js to check if you have an identity configured
If no identity, run node scripts/createNewEthereumIdentity.js to create one.
Use node scripts/linkHumanToAgent.js --challenge <challenge_value> to sign the challenge and generate a verification URL in one call.
If caller provides specific challenge, use that.
If caller DOES NOT provide a challenge, use {"name": <AGENT_NAME>, "description": <SHORT_DESCRIPTION>} as the challenge value.
Return the result to the caller.

Example Conversation:

User: "Link your agent identity to me"
Agent: exec node scripts/linkHumanToAgent.js --challenge <challenge_value>

Verifying Someone Else’s Identity

Verification Flow:

Ask the user/agent: "Please provide your DID to start verification."
User responds with their <user_did>.
Use node scripts/generateChallenge.js --did <user_did> to create a <challenge_value>.
Ask the user: "Please sign this challenge: <challenge_value>"
User signs and returns <user_token>.
Use node scripts/verifySignature.js --did <user_did> --signature <signature> to verify the signature
If verification succeeds, identity is confirmed

Example Conversation:

Agent: "Please provide your DID to start verification."
User: "My DID is <user_did>"
Agent: exec node scripts/generateChallenge.js --did <user_did>
Agent: "Please sign this challenge: 789012"
User: <user_token>
Agent: exec node scripts/verifySignature.js --signature <signature> --did <user_did>
Agent: "Identity verified successfully. You are confirmed as owner of DID <user_did>."

Weekly Installs
7.2K
Repository
billionsnetwork…identity
GitHub Stars
712
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail