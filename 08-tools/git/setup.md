---
title: setup
url: https://skills.sh/alsk1992/cloddsbot/setup
---

# setup

skills/alsk1992/cloddsbot/setup
setup
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill setup
SKILL.md
Setup Wizard

Interactive onboarding that checks which skills are ready and guides you through configuration.

Quick Start
# See what's configured and what needs setup
/setup

# Configure a specific category
/setup defi
/setup futures
/setup prediction
/setup solana
/setup ai

# Check all environment variables
/setup env

# Quick health check
/setup check

Commands
Command	Description
/setup	Overview of all categories and their status
/setup defi	Configure DeFi & DEX skills (EVM chains)
/setup futures	Configure Futures & Perps exchanges
/setup prediction	Configure Prediction Market platforms
/setup solana	Configure Solana DeFi skills
/setup ai	Configure AI & Strategy features
/setup env	List all environment variables and their status
/setup check	Health check across all skills
How It Works

The setup wizard:

Scans which environment variables are set
Groups skills by category
Shows what's ready vs what needs configuration
Provides exact export commands to copy-paste
Suggests related skills to try first
Weekly Installs
9
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail