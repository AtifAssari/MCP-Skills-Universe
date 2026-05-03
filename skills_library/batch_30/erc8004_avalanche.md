---
title: erc8004-avalanche
url: https://skills.sh/colombia-blockchain/agent-skills/erc8004-avalanche
---

# erc8004-avalanche

skills/colombia-blockchain/agent-skills/erc8004-avalanche
erc8004-avalanche
Installation
$ npx skills add https://github.com/colombia-blockchain/agent-skills --skill erc8004-avalanche
SKILL.md
ERC-8004: Trustless Agents

Register your AI agent on-chain with a verifiable identity, making it discoverable and enabling trust signals through reputation and validation. ERC-8004 works on any EVM-compatible chain — currently deployed on Avalanche.

Starter Kit — Create an Agent in 5 Minutes

The fastest way to get started. Copy the template, install, and run:

# 1. Copy the starter template
cp -r assets/starter/ my-agent/
cd my-agent/

# 2. Install dependencies
npm install

# 3. Run locally
npm run dev

# 4. Open in browser
open http://localhost:3000


Your agent is running! You'll see a dashboard with your agent's info and MCP tools.

What's included:

src/server.ts — Complete server with dashboard, health check, MCP server (2 sample tools)
registration.json — ERC-8004 metadata template (edit name, description, capabilities)
dashboard.html — Visual page for browsers and scanners
Dockerfile + railway.toml — Ready to deploy on Railway
README.md — Step-by-step guide from local to deployed and registered on-chain

Next steps:

Edit registration.json with your agent's name and description
Add your own MCP tools in src/server.ts
Deploy to Railway and register on-chain (see assets/starter/README.md)
What is ERC-8004?

ERC-8004 is an Ethereum standard for trustless agent identity and reputation on any EVM chain:

Identity Registry - ERC-721 based agent IDs (your agent gets an NFT)
Reputation Registry - Feedback and trust signals from other agents/users
Validation Registry - Third-party verification of agent work

Website: https://www.8004.org | Spec: https://eips.ethereum.org/EIPS/eip-8004

Contract Addresses (Avalanche)

ERC-8004 can be deployed on any EVM chain. Below are the current official deployments:

Chain	Identity Registry	Reputation Registry
Avalanche Mainnet (43114)	0x8004A169FB4a3325136EB29fA0ceB6D2e539a432	0x8004BAa17C55a88189AE136b182e5fdA19dE9b63
Avalanche Fuji (43113)	0x8004A818BFB912233c491871b3d84c89A494BD9e	0x8004B663056A597Dffe9eCcC1965A193B7388713

Explorer links:

Mainnet: https://snowtrace.io/address/0x8004A169FB4a3325136EB29fA0ceB6D2e539a432
Fuji: https://testnet.snowtrace.io/address/0x8004A818BFB912233c491871b3d84c89A494BD9e
Quick Start
1. Register Your Agent
# Set environment variables
export AVALANCHE_RPC_URL="https://api.avax.network/ext/bc/C/rpc"
export PRIVATE_KEY="your-private-key"

# Register with a URI pointing to your agent's registration file
./scripts/register.sh "https://myagent.xyz/agent.json"

# Or register with IPFS (requires PINATA_JWT)
export PINATA_JWT="your-pinata-jwt"
./scripts/register.sh "ipfs"

2. Check Agent Registration
# Check if an agent is registered and get its info
./scripts/check-agent.sh <agent-id>

3. Update Agent Metadata
# Update on-chain URI to force Snowtrace/scanners to refresh metadata
./scripts/update-uri.sh <agent-id> "https://your-agent.com/registration.json"

4. Give Feedback
# Give reputation feedback to an agent
./scripts/give-feedback.sh <agent-id> <value> <tag1> <tag2>

Registration File Format

Your agent's registration file (see assets/templates/registration.json):

{
  "type": "https://eips.ethereum.org/EIPS/eip-8004#registration-v1",
  "name": "My Agent",
  "description": "An AI agent with on-chain identity via ERC-8004",
  "image": "https://example.com/avatar.png",
  "services": [
    { "name": "web", "endpoint": "https://myagent.xyz/" },
    { "name": "A2A", "endpoint": "https://myagent.xyz/.well-known/agent-card.json", "version": "0.3.0" },
    { "name": "MCP", "endpoint": "https://mcp.myagent.xyz/", "version": "2025-06-18" }
  ],
  "x402Support": false,
  "active": true,
  "registrations": [
    {
      "agentId": 1,
      "agentRegistry": "eip155:43114:0x8004A169FB4a3325136EB29fA0ceB6D2e539a432"
    }
  ],
  "supportedTrust": ["reputation"]
}

Key Concepts
Agent Identity (ERC-721 NFT)
Each agent gets a unique agentId (tokenId) on registration
The NFT owner controls the agent's profile and metadata
Agents are globally identified by eip155:43114:0x8004A169FB4a3325136EB29fA0ceB6D2e539a432 + agentId
Reputation System
Anyone can give feedback (except the agent owner themselves)
Feedback includes a value (int128) with decimals (0-18) plus optional tags
Common tags: starred (quality 0-100), reachable (binary), uptime (percentage)
Feedback can be revoked by the original submitter
Agents can append responses to feedback
Validation
Agents request validation from validator contracts
Validators respond with a score (0-100)
Supports stake-secured re-execution, zkML, TEE attestation
Environment Variables
Variable	Description	Required
RPC_URL	EVM chain RPC endpoint (defaults to Avalanche public RPC)	Yes
PRIVATE_KEY	Wallet private key for signing transactions	Yes
PINATA_JWT	Pinata API JWT for IPFS uploads	No (only for IPFS registration)
AGENT_NAME	Agent display name	No
AGENT_DESCRIPTION	Agent description	No
AGENT_IMAGE	Avatar URL	No
SNOWTRACE_API_KEY	Snowtrace API key for verification	No
Network Details (Avalanche)
Parameter	Mainnet	Fuji Testnet
Chain ID	43114	43113
RPC URL	https://api.avax.network/ext/bc/C/rpc	https://api.avax-test.network/ext/bc/C/rpc
Explorer	https://snowtrace.io	https://testnet.snowtrace.io
Currency	AVAX	AVAX (test)
Faucet	-	https://faucet.avax.network
Workflow
Get native tokens - You need gas fees for registration (~0.01-0.05 AVAX on Avalanche)
Create Registration File - Generate a JSON following the registration format
Upload to IPFS (optional) - Pin via Pinata or host at any URL
Register On-Chain - Call register(agentURI) on the Identity Registry
Set Metadata - Optionally set on-chain metadata and agent wallet
Receive Feedback - Other agents/users can give reputation signals
Request Validation - Optionally request third-party verification
Using with cast (Foundry)
# Register an agent with a URI
cast send 0x8004A169FB4a3325136EB29fA0ceB6D2e539a432 \
  "register(string)" "https://myagent.xyz/agent.json" \
  --rpc-url https://api.avax.network/ext/bc/C/rpc \
  --private-key $PRIVATE_KEY

# Read agent URI
cast call 0x8004A169FB4a3325136EB29fA0ceB6D2e539a432 \
  "tokenURI(uint256)" 1 \
  --rpc-url https://api.avax.network/ext/bc/C/rpc

# Give feedback (value=85, decimals=0, tag1="starred")
cast send 0x8004BAa17C55a88189AE136b182e5fdA19dE9b63 \
  "giveFeedback(uint256,int128,uint8,string,string,string,string,bytes32)" \
  1 85 0 "starred" "" "" "" 0x0000000000000000000000000000000000000000000000000000000000000000 \
  --rpc-url https://api.avax.network/ext/bc/C/rpc \
  --private-key $PRIVATE_KEY

# Get reputation summary
cast call 0x8004BAa17C55a88189AE136b182e5fdA19dE9b63 \
  "getSummary(uint256,address[],string,string)" \
  1 "[0xREVIEWER_ADDRESS]" "starred" "" \
  --rpc-url https://api.avax.network/ext/bc/C/rpc

Using with viem/ethers.js

See references/api-reference.md for complete TypeScript examples.

Interoperability Protocols
A2A (Agent-to-Agent)

See references/a2a-guide.md for:

Complete A2A communication flow with diagrams
Server side: agent-card.json structure, A2A endpoints
Client side: discovering, understanding, and talking to other agents
Multi-agent workflow examples (chaining agents together)
Agent card specification (v0.3.0)
Reputation feedback after A2A interactions
MCP (Model Context Protocol)

See references/mcp-guide.md for:

Complete MCP JSON-RPC implementation (initialize, tools/list, tools/call)
Server side: 10-tool reference implementation with full JSON Schemas
Client side: automated tool discovery and invocation
Tool design best practices (naming, schemas, responses)
Testing with curl commands
JSON-RPC error codes and handling
MCP + x402 integration (free and paid tools)
x402 (Micropayments)

See references/x402-guide.md for:

Complete x402 payment flow with diagrams
Server side: 402 responses, payment verification via facilitator
Client side: EIP-712 signing, creating payment proofs
Agent-to-agent payment discovery (automated)
USDC setup for Mainnet and Fuji testnet
Pricing best practices and security checklist
Best Practices

See references/best-practices.md for:

Structuring registration.json metadata for maximum scanner score
Image/NFT requirements and hosting
Service exposure (web, A2A, MCP) — only declare what works
Capability definition — honest, real, backed by code
Avoiding scanner warnings (WA080 and others)
On-chain vs off-chain metadata consistency
Agent type classification (agentic, hybrid, informational)
Scanner score optimization (Engagement 30%, Service 25%, Publisher 20%, Compliance 15%, Momentum 10%)
Common mistakes to avoid (with real examples)
Deployment & Infrastructure

See references/deployment-guide.md for:

Complete architecture diagram (ASCII)
Step-by-step creation flow (7 phases from zero to live agent)
Railway deployment guide with configuration
Infrastructure requirements and cost estimation
Backend code structure and patterns (caching, timeouts, parallel calls)
On-chain registration flow with commands
Monitoring, maintenance, and security checklist
Troubleshooting

See references/troubleshooting.md for:

Real production issues and their solutions
Scanner warning fixes (WA080, unreachable services)
Railway deployment issues (502, build fails, crashes)
API integration problems (rate limits, timeouts, memory leaks)
On-chain registration debugging
Diagnostic commands and resolution flowchart
Reference Documents
Document	Description
references/api-reference.md	TypeScript/JavaScript API examples (viem + ethers.js)
references/registration-format.md	Complete registration.json specification
references/contract-addresses.md	All contract addresses and RPC endpoints
references/a2a-guide.md	A2A protocol implementation guide
references/mcp-guide.md	MCP server/client implementation guide
references/x402-guide.md	x402 micropayment protocol guide
references/best-practices.md	Metadata, scoring, and agent design best practices
references/deployment-guide.md	Architecture, Railway deployment, infrastructure
references/troubleshooting.md	Real-world issues and solutions
Links
ERC-8004 Spec
8004.org
8004scan.io - Agent scanner and scoring
erc-8004scan.xyz - Agent scanner and metadata validation
GitHub: erc-8004-contracts
Snowtrace Explorer
Railway - Recommended hosting platform
Weekly Installs
8
Repository
colombia-blockc…t-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn