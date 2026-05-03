---
rating: ⭐⭐⭐
title: tauri-scaffold
url: https://skills.sh/0xraduan/raduan-plugins/tauri-scaffold
---

# tauri-scaffold

skills/0xraduan/raduan-plugins/tauri-scaffold
tauri-scaffold
Installation
$ npx skills add https://github.com/0xraduan/raduan-plugins --skill tauri-scaffold
SKILL.md
Scaffold a Tauri + React App

Generate a production-ready Tauri + React desktop application with best practices baked in.

What Gets Created
my-app/
├── src/                      # React frontend
│   ├── ui/
│   │   ├── components/       # React components
│   │   ├── hooks/            # Custom hooks
│   │   └── providers/        # Context providers
│   ├── core/                 # Business logic
│   │   ├── api/              # TanStack Query queries/mutations
│   │   └── db/               # Database access layer
│   ├── App.tsx
│   └── main.tsx
├── src-tauri/                # Rust backend
│   └── src/
│       ├── lib.rs            # Tauri setup
│       ├── commands.rs       # Tauri commands
│       └── migrations.rs     # SQLite migrations
├── package.json
├── tsconfig.json
├── tailwind.config.js
└── vite.config.ts

Stack Included
Tauri 2.x - Native desktop shell
React 18 - UI framework
TypeScript - Strict mode enabled
TanStack Query - Server state management
SQLite - Local database (via tauri-plugin-sql)
Tailwind CSS - Styling
Radix UI - Accessible components
Vite - Build tool
Instructions
Step 1: Get App Details

Ask the user for:

App name (kebab-case, e.g., my-cool-app)
App display name (e.g., "My Cool App")
Bundle identifier (e.g., com.yourname.mycoolapp)
Whether to include AI provider patterns (optional)
Step 2: Create the Project

Run the scaffold script:

uv run /path/to/plugin/scripts/scaffold.py \
  --name "app-name" \
  --display-name "App Display Name" \
  --bundle-id "com.example.appname" \
  --output-dir "./app-name"


If --with-ai flag was provided, add:

  --with-ai

Step 3: Initialize the Project

After scaffolding:

cd app-name
pnpm install

Step 4: Run Development Server
pnpm tauri dev

Step 5: Guide Next Steps

Tell the user:

Database: Add tables in src-tauri/src/migrations.rs
API Layer: Create queries in src/core/api/
Components: Build UI in src/ui/components/
Tauri Commands: Add Rust commands in src-tauri/src/commands.rs

Point them to /tauri-react-starter:guide for architecture deep-dive.

Example
User: Create a new Tauri app for a note-taking application

Weekly Installs
10
Repository
0xraduan/raduan-plugins
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass