---
rating: ⭐⭐
title: pma-rust
url: https://skills.sh/zzci/skills/pma-rust
---

# pma-rust

skills/zzci/skills/pma-rust
pma-rust
Installation
$ npx skills add https://github.com/zzci/skills --skill pma-rust
SKILL.md
Rust Project Implementation Guide

Use this skill together with /pma. /pma controls workflow, approval, and task tracking; this guide defines the implementation baseline after approval.

Keep this entry file small. Load only the reference packs needed for the task.

Scope

For PMA-managed Rust workspace projects, especially services and CLIs built from multiple crates.

Not for ad hoc one-file Rust examples, embedded targets, or non-PMA workflows.

Loading Order
Always load references/baseline.md first.
Load references/toolchain-and-workspace.md for workspace structure, Cargo defaults, toolchain pinning, lint setup, and common crate conventions.
Load references/runtime-and-data.md for error handling, architecture, Axum, Diesel, SQLx, config loading, and signal handling.
Load references/delivery.md for security, logging, observability, testing, CI, and Git workflow.
Quick Routing
New workspace or crate layout: references/toolchain-and-workspace.md
Axum services, config layering, DB access, signal handling: references/runtime-and-data.md
security review, telemetry, testing, CI, release readiness: references/delivery.md
default stack, quality gates, naming, core conventions: references/baseline.md
Reference Packs
references/baseline.md Scope, stack defaults, quality gates, naming, and core code quality expectations.
references/toolchain-and-workspace.md Workspace layout, Cargo.toml, toolchain pinning, compiler flags, and lint configuration.
references/runtime-and-data.md Error handling, architecture patterns, database strategy, config layering, Axum runtime, and shutdown.
references/delivery.md Security, logging, observability, testing, CI, and Git conventions.

If the repository has already chosen a different path, keep that choice explicit and apply it consistently across code, scripts, docs, and CI.

Weekly Installs
84
Repository
zzci/skills
GitHub Stars
2
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn