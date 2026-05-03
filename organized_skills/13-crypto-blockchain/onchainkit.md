---
rating: ⭐⭐⭐
title: onchainkit
url: https://skills.sh/alsk1992/cloddsbot/onchainkit
---

# onchainkit

skills/alsk1992/cloddsbot/onchainkit
onchainkit
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill onchainkit
SKILL.md
OnchainKit - Build Onchain Apps

Build production-ready onchain applications using Coinbase's React component library.

Overview

OnchainKit provides ready-to-use components that abstract blockchain complexity:

No backend infrastructure required
Works automatically on Base
Cost-effective transactions (< $0.01 fees)
Commands
Project Setup
/onchainkit create <project-name>    Create new onchain app
/onchainkit add <component>          Add component to project

Templates
/onchainkit template wallet          Wallet connection template
/onchainkit template swap            Token swap app template
/onchainkit template nft             NFT minting template
/onchainkit template checkout        Payment processing template

Docs
/onchainkit docs wallet              Wallet integration docs
/onchainkit docs identity            Identity components docs
/onchainkit docs swap                Token swap docs
/onchainkit docs transaction         Transaction building docs

Core Components
Wallet Connection
import { Wallet, ConnectWallet } from '@coinbase/onchainkit/wallet';
<Wallet><ConnectWallet /></Wallet>

Identity Display
import { Identity, Avatar, Name } from '@coinbase/onchainkit/identity';
<Identity address={address}><Avatar /><Name /></Identity>

Token Swap
import { Swap, SwapButton } from '@coinbase/onchainkit/swap';
<Swap><SwapButton /></Swap>

Quick Start
# Create new app
npm create onchain@latest

# Or add to existing project
npm install @coinbase/onchainkit

Configuration
export NEXT_PUBLIC_CDP_API_KEY="..."        # Coinbase API key
export NEXT_PUBLIC_WC_PROJECT_ID="..."      # WalletConnect ID

Resources
Docs: https://onchainkit.xyz
GitHub: https://github.com/coinbase/onchainkit
Weekly Installs
9
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn