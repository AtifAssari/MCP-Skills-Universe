---
rating: ⭐⭐
title: cargo-lock-manager
url: https://skills.sh/different-ai/openwork/cargo-lock-manager
---

# cargo-lock-manager

skills/different-ai/openwork/cargo-lock-manager
cargo-lock-manager
Installation
$ npx skills add https://github.com/different-ai/openwork --skill cargo-lock-manager
SKILL.md
Quick Usage (Already Configured)
Check Cargo.lock status
cd packages/desktop/src-tauri
cargo check --locked 2>&1 | head -20

Update Cargo.lock locally
cd packages/desktop/src-tauri
cargo update --workspace

Test with --locked after update
cd packages/desktop/src-tauri
cargo test --locked

Common Gotchas
The --locked flag prevents automatic updates to Cargo.lock, which is good for reproducible builds but fails when dependencies change.
PRs often fail because the lock file wasn't committed after dependency updates.
Running cargo update without --workspace may not update all workspace members.
When CI Fails with --locked
Option 1: Update lock file and commit (Recommended)
cd packages/desktop/src-tauri
cargo update --workspace
git add Cargo.lock
git commit -m "chore: update Cargo.lock"
git push

Option 2: Use --offline flag (for air-gapped environments)
cargo test --manifest-path packages/desktop/src-tauri/Cargo.toml --offline

First-Time Setup (If Not Configured)

No setup required. This skill assumes:

Rust/Cargo is installed
You're in the openwork repository
The Tauri app is in packages/desktop/src-tauri/
Prevention Tips
Always run cargo check or cargo build after modifying Cargo.toml files
Include Cargo.lock changes in the same commit as dependency updates
Consider adding a pre-commit hook to verify lock file is up to date
Weekly Installs
90
Repository
different-ai/openwork
GitHub Stars
14.6K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass