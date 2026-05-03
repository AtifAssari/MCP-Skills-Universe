---
title: tauri-solidjs
url: https://skills.sh/different-ai/openwork/tauri-solidjs
---

# tauri-solidjs

skills/different-ai/openwork/tauri-solidjs
tauri-solidjs
Installation
$ npx skills add https://github.com/different-ai/openwork --skill tauri-solidjs
SKILL.md
Quick Usage (Already Configured)
Create new Tauri + SolidJS project
pnpm create tauri-app openwork --template solid-ts

Development
pnpm tauri dev

Build for production
pnpm tauri build

Build for mobile
# iOS
pnpm tauri ios dev
pnpm tauri ios build

# Android
pnpm tauri android dev
pnpm tauri android build

Project Structure
openwork/
  packages/
    desktop/
      src-tauri/
        src/
          main.rs           # Rust entry point
          lib.rs            # Tauri commands and state
        Cargo.toml          # Rust dependencies
        tauri.conf.json     # Tauri configuration
        capabilities/       # Permission capabilities
      src/
        App.tsx             # SolidJS root component
        index.tsx           # Entry point
      components/           # UI components
      stores/               # Solid stores for state
      lib/                  # Utilities and OpenCode bridge
      index.html            # HTML template
      package.json          # Frontend dependencies
      vite.config.ts        # Vite configuration

Key Dependencies
Frontend (package.json)
{
  "dependencies": {
    "solid-js": "^1.8.0",
    "@tauri-apps/api": "^2.0.0",
    "@tauri-apps/plugin-shell": "^2.0.0",
    "@tauri-apps/plugin-fs": "^2.0.0",
    "@tauri-apps/plugin-sql": "^2.0.0"
  },
  "devDependencies": {
    "@tauri-apps/cli": "^2.0.0",
    "vite": "^5.0.0",
    "vite-plugin-solid": "^2.8.0",
    "tailwindcss": "^3.4.0"
  }
}

Backend (Cargo.toml)
[dependencies]
tauri = { version = "2", features = ["shell-open"] }
tauri-plugin-shell = "2"
tauri-plugin-fs = "2"
tauri-plugin-sql = { version = "2", features = ["sqlite"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"

Tauri Commands (Rust -> JS)
// packages/desktop/src-tauri/src/lib.rs
use tauri::Manager;

#[tauri::command]
async fn spawn_opencode(prompt: String) -> Result<String, String> {
    use std::process::Command;
    
    let output = Command::new("opencode")
        .args(["-p", &prompt, "-f", "json", "-q"])
        .output()
        .map_err(|e| e.to_string())?;
    
    String::from_utf8(output.stdout)
        .map_err(|e| e.to_string())
}

#[tauri::command]
fn get_opencode_db_path() -> String {
    // Return path to .opencode/opencode.db
    dirs::home_dir()
        .map(|p| p.join(".opencode/opencode.db").to_string_lossy().to_string())
        .unwrap_or_default()
}

Invoking Commands from SolidJS
import { invoke } from "@tauri-apps/api/core";

async function runTask(prompt: string) {
  const result = await invoke<string>("spawn_opencode", { prompt });
  return JSON.parse(result);
}

Common Gotchas
Tauri 2.x uses @tauri-apps/api/core instead of @tauri-apps/api/tauri.
Mobile builds require Xcode (iOS) or Android Studio (Android).
File access requires tauri-plugin-fs and capability configuration.
SQLite access requires tauri-plugin-sql.
First-Time Setup (If Not Configured)
Install Tauri CLI
pnpm add -D @tauri-apps/cli

Initialize Tauri in existing project
pnpm tauri init

Add mobile targets
pnpm tauri ios init
pnpm tauri android init

References
Tauri 2.0 Docs
SolidJS Docs
Tauri Mobile
Weekly Installs
436
Repository
different-ai/openwork
GitHub Stars
14.6K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass