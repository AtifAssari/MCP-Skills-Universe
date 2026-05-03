---
rating: ⭐⭐⭐
title: setup-solidity-contracts
url: https://skills.sh/openzeppelin/openzeppelin-skills/setup-solidity-contracts
---

# setup-solidity-contracts

skills/openzeppelin/openzeppelin-skills/setup-solidity-contracts
setup-solidity-contracts
Installation
$ npx skills add https://github.com/openzeppelin/openzeppelin-skills --skill setup-solidity-contracts
SKILL.md
Solidity Setup

For existing projects, detect the framework by looking for hardhat.config.* (Hardhat) or foundry.toml (Foundry). For new projects, ask the user which framework they prefer.

Hardhat Setup
Initialize project (only if starting a new project)
npx hardhat init        # Hardhat v2
npx hardhat --init      # Hardhat v3

Install OpenZeppelin Contracts:
npm install @openzeppelin/contracts

If using upgradeable contracts, also install the upgradeable variant:
npm install @openzeppelin/contracts-upgradeable

Foundry Setup
Install Foundry
curl -L https://foundry.paradigm.xyz | bash
foundryup

Initialize project (only if starting a new project)
forge init my-project
cd my-project

Add OpenZeppelin Contracts:
forge install OpenZeppelin/openzeppelin-contracts@v<VERSION>

If using upgradeable contracts, also add the upgradeable variant:
forge install OpenZeppelin/openzeppelin-contracts-upgradeable@v<VERSION>


Look up the current version from https://github.com/OpenZeppelin/openzeppelin-contracts/releases. Pin to a release tag — without one, forge install pulls the default branch, which may be unstable.

remappings.txt (if not using upgradeable contracts)
@openzeppelin/contracts/=lib/openzeppelin-contracts/contracts/

remappings.txt (if using upgradeable contracts)
@openzeppelin/contracts/=lib/openzeppelin-contracts-upgradeable/lib/openzeppelin-contracts/contracts/
@openzeppelin/contracts-upgradeable/=lib/openzeppelin-contracts-upgradeable/contracts/


Note The above remappings mean that both @openzeppelin/contracts/ (including proxy contracts) and @openzeppelin/contracts-upgradeable/ come from the openzeppelin-contracts-upgradeable submodule and its subdirectories, which includes its own transitive copy of openzeppelin-contracts of the same release version number. This format is needed for Etherscan verification to work. Particularly, any copies of openzeppelin-contracts that are installed separately are NOT used.

Import Conventions
Standard: @openzeppelin/contracts/token/ERC20/ERC20.sol
Upgradeable: @openzeppelin/contracts-upgradeable/token/ERC20/ERC20Upgradeable.sol
Use upgradeable variants only when deploying behind proxies; otherwise use standard contracts.
Weekly Installs
221
Repository
openzeppelin/op…n-skills
GitHub Stars
173
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn