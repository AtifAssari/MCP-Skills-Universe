---
title: napi-rs-node-bindings
url: https://skills.sh/pmcfadin/cqlite/napi-rs-node-bindings
---

# napi-rs-node-bindings

skills/pmcfadin/cqlite/napi-rs-node-bindings
napi-rs-node-bindings
Installation
$ npx skills add https://github.com/pmcfadin/cqlite --skill napi-rs-node-bindings
SKILL.md
napi-rs Node.js Bindings
Project Structure
my-rust-lib/
├── Cargo.toml          # napi dependency
├── package.json        # npm package config
├── src/
│   ├── lib.rs          # Core Rust library
│   └── node/           # Node binding module
│       ├── mod.rs      # Exports
│       ├── types.rs    # #[napi] structs
│       └── errors.rs   # Error conversions
├── index.js            # JS entry point (generated)
├── index.d.ts          # TypeScript definitions (generated)
└── __test__/
    └── index.spec.ts   # Tests

Core Workflow
1. Expose Rust Types
use napi::bindgen_prelude::*;
use napi_derive::napi;

#[napi]
pub struct MyType {
    inner: RustType,  // Private Rust type
}

#[napi]
impl MyType {
    #[napi(constructor)]
    pub fn new(value: i64) -> Result<Self> {
        Ok(Self { inner: RustType::new(value)? })
    }
    
    #[napi]
    pub fn process(&self) -> Result<String> {
        self.inner.process().map_err(|e| e.into())
    }
}

2. Export Functions
#[napi]
pub fn parse_cql(query: String) -> Result<Statement> {
    cqlite::parse(&query).map_err(|e| e.into())
}

// Async function returns Promise
#[napi]
pub async fn parse_file(path: String) -> Result<Vec<Statement>> {
    let content = tokio::fs::read_to_string(&path).await?;
    cqlite::parse_all(&content).map_err(|e| e.into())
}

3. Build & Test
npm run build          # Build native module
npm run build:debug    # Debug build (faster)
npm test               # Run tests

Reference Guides

Load these as needed based on the task:

Task	Reference
Type mapping between Rust ↔ JavaScript	type-conversions.md
Converting Rust errors to JS exceptions	error-handling.md
Async patterns and Promises	async-patterns.md
Building and publishing to npm	build-publish.md
Testing strategies	testing.md
Debugging common binding issues	debugging.md
CQLite CQL feature parity checklist	cqlite-parity.md
Quick Reference
Cargo.toml Setup
[package]
name = "cqlite"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["cdylib"]

[dependencies]
napi = { version = "2", default-features = false, features = ["napi9", "async", "serde-json"] }
napi-derive = "2"

[build-dependencies]
napi-build = "2"

[profile.release]
lto = true

package.json Setup
{
  "name": "cqlite",
  "version": "0.1.0",
  "main": "index.js",
  "types": "index.d.ts",
  "napi": {
    "name": "cqlite",
    "triples": {
      "defaults": true,
      "additional": ["aarch64-apple-darwin", "aarch64-linux-android"]
    }
  },
  "scripts": {
    "build": "napi build --platform --release",
    "build:debug": "napi build --platform",
    "prepublishOnly": "napi prepublish -t npm",
    "test": "ava"
  },
  "devDependencies": {
    "@napi-rs/cli": "^2.18.0",
    "ava": "^6.0.0"
  }
}

build.rs
extern crate napi_build;

fn main() {
    napi_build::setup();
}

napi-rs Attribute Quick Reference
Attribute	Use
#[napi]	Expose function/struct/impl to JS
#[napi(constructor)]	Class constructor
#[napi(getter)]	Property getter
#[napi(setter)]	Property setter
#[napi(factory)]	Static factory method
#[napi(js_name = "...")]	Rename in JavaScript
#[napi(ts_args_type = "...")]	Custom TypeScript arg types
#[napi(ts_return_type = "...")]	Custom TypeScript return type
#[napi(object)]	Plain JS object (no class)
#[napi(strict)]	Strict type checking
Weekly Installs
13
Repository
pmcfadin/cqlite
First Seen
Feb 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass