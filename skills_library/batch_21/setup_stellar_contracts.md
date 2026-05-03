---
title: setup-stellar-contracts
url: https://skills.sh/openzeppelin/openzeppelin-skills/setup-stellar-contracts
---

# setup-stellar-contracts

skills/openzeppelin/openzeppelin-skills/setup-stellar-contracts
setup-stellar-contracts
Installation
$ npx skills add https://github.com/openzeppelin/openzeppelin-skills --skill setup-stellar-contracts
SKILL.md
Stellar Setup
Soroban/Stellar Development Setup

Install the Rust toolchain (v1.84.0+) and the Soroban WASM target:

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup target add wasm32v1-none


Install the Stellar CLI:

curl -fsSL https://github.com/stellar/stellar-cli/raw/main/install.sh | sh


Create a new Soroban project:

stellar contract init my_project


This creates a Cargo workspace with contracts in contracts/*/.

OpenZeppelin Dependencies

Look up the current version from the stellar-contracts repo before adding. Pin exact versions with = as the library is under active development.

Add OpenZeppelin crates to the root Cargo.toml under [workspace.dependencies]:

[workspace.dependencies]
stellar-tokens = "=<VERSION>"
stellar-access = "=<VERSION>"
stellar-contract-utils = "=<VERSION>"
stellar-macros = "=<VERSION>"


Then reference them in the per-contract contracts/*/Cargo.toml:

[dependencies]
soroban-sdk = { workspace = true }
stellar-tokens = { workspace = true }
stellar-access = { workspace = true }
stellar-contract-utils = { workspace = true }
stellar-macros = { workspace = true }


Available crates: stellar-access, stellar-accounts, stellar-contract-utils, stellar-fee-abstraction, stellar-governance, stellar-macros, stellar-tokens.

Only add the crates the contract actually uses. stellar-macros provides proc-macro attributes (for example, #[when_not_paused], #[only_owner], #[derive(Upgradeable)]) and is needed in most contracts.

Code Patterns

Imports use underscores as the crate root (Rust convention):

use stellar_tokens::fungible::{Base, FungibleToken};
use stellar_tokens::fungible::burnable::FungibleBurnable;
use stellar_access::ownable::Ownable;
use stellar_contract_utils::pausable::Pausable;
use stellar_macros::when_not_paused;


Contracts use #[contract] on the struct and #[contractimpl] on the impl block (from soroban_sdk):

use soroban_sdk::{contract, contractimpl, Env};

#[contract]
pub struct MyToken;

#[contractimpl]
impl MyToken {
    // Implement trait methods here
}


Trait implementations are separate impl blocks per trait (e.g., FungibleToken, Pausable). Guard macros like #[when_not_paused] and #[only_owner] decorate individual functions.

Platform Notes
Read operations are free in Stellar. Optimize for minimizing writes; reads and computation are cheap. Prefer clean, readable code over micro-optimizations.
Instance storage TTL extension is the developer's responsibility. The OpenZeppelin library handles TTL extension for other storage entries, but contracts must extend their own instance storage entries to prevent expiration.
Build & Test

Build the contract to WASM:

stellar contract build


This is a shortcut for cargo build --target wasm32v1-none --release. Output appears in target/wasm32v1-none/release/.

Run tests:

cargo test


soroban-sdk testutils are automatically enabled for in-crate unit tests.

Weekly Installs
107
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