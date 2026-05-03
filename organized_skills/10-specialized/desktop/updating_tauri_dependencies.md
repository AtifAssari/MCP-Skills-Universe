---
rating: ⭐⭐⭐
title: updating-tauri-dependencies
url: https://skills.sh/dchuk/claude-code-tauri-skills/updating-tauri-dependencies
---

# updating-tauri-dependencies

skills/dchuk/claude-code-tauri-skills/updating-tauri-dependencies
updating-tauri-dependencies
Installation
$ npx skills add https://github.com/dchuk/claude-code-tauri-skills --skill updating-tauri-dependencies
SKILL.md
Updating Tauri Dependencies

This skill provides guidance for updating Tauri dependencies across both the JavaScript and Rust ecosystems.

Version Synchronization (Critical)

The JavaScript @tauri-apps/api package and Rust tauri crate must maintain matching minor versions. Adding new features requires upgrading both sides to ensure compatibility.

For Tauri plugins, maintain exact version parity (e.g., both 2.2.1) for the npm package and cargo crate.

Updating JavaScript Dependencies
Using npm

Update Tauri CLI and API packages:

npm install @tauri-apps/cli@latest @tauri-apps/api@latest


Check for outdated packages:

npm outdated @tauri-apps/cli
npm outdated @tauri-apps/api

Using yarn

Update Tauri CLI and API packages:

yarn up @tauri-apps/cli @tauri-apps/api


Check for outdated packages:

yarn outdated @tauri-apps/cli
yarn outdated @tauri-apps/api

Using pnpm

Update Tauri CLI and API packages:

pnpm update @tauri-apps/cli @tauri-apps/api --latest


Check for outdated packages:

pnpm outdated @tauri-apps/cli
pnpm outdated @tauri-apps/api

Updating Rust Dependencies
Manual Update

Check the latest versions on crates.io:

tauri crate versions
tauri-build crate versions

Edit src-tauri/Cargo.toml and update the version numbers:

[build-dependencies]
tauri-build = "2.0"

[dependencies]
tauri = { version = "2.0", features = [] }

Run cargo update from the src-tauri directory:
cd src-tauri && cargo update

Using cargo-edit (Automatic)

Install cargo-edit if not already installed:

cargo install cargo-edit


Upgrade Tauri dependencies automatically:

cd src-tauri && cargo upgrade tauri tauri-build

Checking for Updates
Check All Tauri Dependencies

JavaScript packages:

# npm
npm outdated | grep tauri

# yarn
yarn outdated | grep tauri

# pnpm
pnpm outdated | grep tauri


Rust crates:

cd src-tauri && cargo outdated | grep tauri


Note: cargo outdated requires the cargo-outdated tool:

cargo install cargo-outdated

Updating Tauri Plugins

When updating Tauri plugins, both the npm package and Rust crate must be updated to the same version.

Example for updating a plugin (e.g., shell plugin):

JavaScript side
# npm
npm install @tauri-apps/plugin-shell@latest

# yarn
yarn up @tauri-apps/plugin-shell

# pnpm
pnpm update @tauri-apps/plugin-shell --latest

Rust side

Edit src-tauri/Cargo.toml:

[dependencies]
tauri-plugin-shell = "2.0"


Then update:

cd src-tauri && cargo update

Complete Update Workflow

To update all Tauri dependencies in a project:

Update JavaScript dependencies:
# Using npm (adjust for your package manager)
npm install @tauri-apps/cli@latest @tauri-apps/api@latest

Update any Tauri plugins on the JavaScript side:
npm install @tauri-apps/plugin-shell@latest @tauri-apps/plugin-fs@latest
# Add other plugins as needed


Update Rust dependencies in src-tauri/Cargo.toml

Run cargo update:

cd src-tauri && cargo update

Rebuild the project to verify compatibility:
npm run tauri build
# or
cargo tauri build

Troubleshooting
Version Mismatch Errors

If you encounter version mismatch errors between JavaScript and Rust dependencies:

Verify both sides use matching minor versions
Check package.json for @tauri-apps/api version
Check src-tauri/Cargo.toml for tauri crate version
Ensure they align (e.g., both at 2.x)
Cargo Lock Conflicts

If Cargo.lock has conflicts after updating:

cd src-tauri && rm Cargo.lock && cargo update

Plugin Version Mismatch

For plugin version mismatches, ensure exact version parity between npm and cargo versions of the same plugin.

Weekly Installs
57
Repository
dchuk/claude-co…i-skills
GitHub Stars
18
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass