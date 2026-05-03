---
title: axum-rust-template
url: https://skills.sh/eng0ai/eng0-template-skills/axum-rust-template
---

# axum-rust-template

skills/eng0ai/eng0-template-skills/axum-rust-template
axum-rust-template
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill axum-rust-template
SKILL.md
Axum Rust API

A Rust Axum API with Diesel ORM and DDD architecture.

Tech Stack
Framework: Axum
Language: Rust
ORM: Diesel
Architecture: DDD
Database: PostgreSQL
Prerequisites
Rust toolchain installed
PostgreSQL
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/axum-rust-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/axum-rust-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Build Project
cargo build

4. Setup Database

Configure database and run Diesel migrations.

Development
cargo run

Weekly Installs
36
Repository
eng0ai/eng0-tem…e-skills
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass