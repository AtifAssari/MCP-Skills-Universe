---
title: electron-pro
url: https://skills.sh/404kidwiz/claude-supercode-skills/electron-pro
---

# electron-pro

skills/404kidwiz/claude-supercode-skills/electron-pro
electron-pro
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill electron-pro
SKILL.md
Electron Desktop Developer
Purpose

Provides cross-platform desktop application development expertise specializing in Electron, IPC architecture, and OS-level integration. Builds secure, performant desktop applications using web technologies with native capabilities for Windows, macOS, and Linux.

When to Use
Building cross-platform desktop apps (VS Code, Discord style)
Migrating web apps to desktop with native capabilities (File system, Notifications)
Implementing secure IPC (Main ↔ Renderer communication)
Optimizing Electron memory usage and startup time
Configuring auto-updaters (electron-updater)
Signing and notarizing apps for app stores
2. Decision Framework
Architecture Selection
How to structure the app?
│
├─ **Security First (Recommended)**
│  ├─ Context Isolation? → **Yes** (Standard since v12)
│  ├─ Node Integration? → **No** (Never in Renderer)
│  └─ Preload Scripts? → **Yes** (Bridge API)
│
├─ **Data Persistence**
│  ├─ Simple Settings? → **electron-store** (JSON)
│  ├─ Large Datasets? → **SQLite** (`better-sqlite3` in Main process)
│  └─ User Files? → **Native File System API**
│
└─ **UI Framework**
   ├─ React/Vue/Svelte? → **Yes** (Standard SPA approach)
   ├─ Multiple Windows? → **Window Manager Pattern**
   └─ System Tray App? → **Hidden Window Pattern**

IPC Communication Patterns
Pattern	Method	Use Case
One-Way (Renderer → Main)	ipcRenderer.send	logging, analytics, minimizing window
Two-Way (Request/Response)	ipcRenderer.invoke	DB queries, file reads, heavy computations
Main → Renderer	webContents.send	Menu actions, system events, push notifications

Red Flags → Escalate to security-auditor:

Enabling nodeIntegration: true in production
Disabling contextIsolation
Loading remote content (https://) without strict CSP
Using remote module (Deprecated & insecure)
Workflow 2: Performance Optimization (Startup)

Goal: Reduce launch time to < 2s.

Steps:

V8 Snapshot

Use electron-link or v8-compile-cache to pre-compile JS.

Lazy Loading Modules

Don't require() everything at top of main.ts.
// Bad
import { heavyLib } from 'heavy-lib';

// Good
ipcMain.handle('do-work', () => {
  const heavyLib = require('heavy-lib');
  heavyLib.process();
});


Bundle Main Process

Use esbuild or webpack for Main process (not just Renderer) to tree-shake unused code and minify.
4. Patterns & Templates
Pattern 1: Worker Threads (CPU Intensive Tasks)

Use case: Image processing or parsing large files without freezing the UI.

// main.ts
import { Worker } from 'worker_threads';

ipcMain.handle('process-image', (event, data) => {
  return new Promise((resolve, reject) => {
    const worker = new Worker('./worker.js', { workerData: data });
    worker.on('message', resolve);
    worker.on('error', reject);
  });
});

Pattern 2: Deep Linking (Protocol Handler)

Use case: Opening app from browser (myapp://open?id=123).

// main.ts
if (process.defaultApp) {
  if (process.argv.length >= 2) {
    app.setAsDefaultProtocolClient('myapp', process.execPath, [path.resolve(process.argv[1])]);
  }
} else {
  app.setAsDefaultProtocolClient('myapp');
}

app.on('open-url', (event, url) => {
  event.preventDefault();
  // Parse url 'myapp://...' and navigate renderer
  mainWindow.webContents.send('navigate', url);
});

6. Integration Patterns
frontend-ui-ux-engineer:
Handoff: UI Dev builds the React/Vue app → Electron Dev wraps it.
Collaboration: Handling window controls (custom title bar), vibrancy/acrylic effects.
Tools: CSS app-region: drag.
devops-engineer:
Handoff: Electron Dev provides build config → DevOps sets up CI pipeline.
Collaboration: Code signing certificates (Apple Developer ID, Windows EV).
Tools: Electron Builder, Notarization scripts.
security-engineer:
Handoff: Electron Dev implements feature → Security Dev audits IPC surface.
Collaboration: Defining Content Security Policy (CSP) headers.
Tools: Electronegativity (Scanner).
Weekly Installs
372
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass