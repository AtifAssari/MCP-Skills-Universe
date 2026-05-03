---
rating: ⭐⭐
title: electron
url: https://skills.sh/teachingai/full-stack-skills/electron
---

# electron

skills/teachingai/full-stack-skills/electron
electron
Installation
$ npx skills add https://github.com/teachingai/full-stack-skills --skill electron
Summary

Comprehensive Electron framework guidance for building cross-platform desktop applications.

Covers main process, renderer process, preload scripts, and IPC communication patterns with code examples
Includes API reference and practical examples for BrowserWindow, Menu, Tray, Dialog, and other core modules
Provides best practices for security (nodeIntegration, preload scripts), process separation, and resource management
Addresses packaging, auto-updates, native module compatibility, and cross-platform testing workflows
SKILL.md
When to use this skill

Use this skill whenever the user wants to:

Build cross-platform desktop applications with Electron
Understand Electron architecture (main process, renderer process, preload)
Implement IPC (Inter-Process Communication) between processes
Create and manage BrowserWindow instances
Implement menus, tray icons, and native features
Package and distribute Electron applications
Use Electron Forge for project scaffolding and building
Debug and test Electron applications
Implement security best practices
Use Electron APIs (app, BrowserWindow, ipcMain, ipcRenderer, etc.)
How to use this skill

This skill is organized to match the Electron official documentation structure (https://www.electronjs.org/zh/docs/latest/, https://www.electronjs.org/zh/docs/latest/api/app). When working with Electron:

Identify the topic from the user's request:

Getting started/快速开始 → examples/getting-started/installation.md or examples/getting-started/quick-start.md
Main process/主进程 → examples/processes/main-process.md
Renderer process/渲染进程 → examples/processes/renderer-process.md
IPC communication/IPC 通信 → examples/processes/ipc-communication.md
BrowserWindow/窗口 → examples/api/browser-window.md
Menu/菜单 → examples/api/menu.md
Packaging/打包 → examples/advanced/packaging.md
Security/安全 → examples/advanced/security.md

Load the appropriate example file from the examples/ directory:

Getting Started (快速开始) - examples/getting-started/:

examples/getting-started/installation.md - Installing Electron and basic setup
examples/getting-started/quick-start.md - Quick start tutorial

Processes (进程) - examples/processes/:

examples/processes/main-process.md - Main process concepts and usage
examples/processes/renderer-process.md - Renderer process concepts
examples/processes/preload-scripts.md - Preload scripts usage
examples/processes/ipc-communication.md - IPC communication patterns

API Examples (API 示例) - examples/api/:

examples/api/browser-window.md - BrowserWindow usage
examples/api/menu.md - Menu and context menu
examples/api/tray.md - System tray
examples/api/dialog.md - File dialogs
examples/api/ipc-main.md - ipcMain usage
examples/api/ipc-renderer.md - ipcRenderer usage

Advanced (高级) - examples/advanced/:

examples/advanced/packaging.md - Application packaging
examples/advanced/security.md - Security best practices
examples/advanced/auto-updater.md - Auto updater
examples/advanced/native-modules.md - Native modules

Tools (工具) - examples/tools/:

examples/tools/electron-forge.md - Electron Forge usage
examples/tools/electron-fiddle.md - Electron Fiddle usage

Follow the specific instructions in that example file for syntax, structure, and best practices

Important Notes:

All examples follow Electron latest API
Examples use both CommonJS (require) and ES modules (import)
Each example file includes key concepts, code examples, and key points
Always check the example file for best practices and common patterns
Electron supports Windows, macOS, and Linux

Reference API documentation in the api/ directory when needed:

api/app.md - app module API
api/browser-window.md - BrowserWindow API
api/ipc-main.md - ipcMain API
api/ipc-renderer.md - ipcRenderer API
api/menu.md - Menu API
api/tray.md - Tray API

Use templates from the templates/ directory:

templates/main-process.md - Main process template
templates/preload-script.md - Preload script template
templates/renderer-process.md - Renderer process template
templates/package-json.md - package.json template
Doc mapping (one-to-one with official documentation)
examples/ → https://www.electronjs.org/zh/docs/latest/
api/ → https://www.electronjs.org/zh/docs/latest/api/app
Quick Start Example
// main.js
const { app, BrowserWindow, ipcMain } = require('electron')
const path = require('path')

function createWindow() {
  const win = new BrowserWindow({
    width: 800, height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,  // Security: always disable
      contextIsolation: true    // Security: always enable
    }
  })
  win.loadFile('index.html')
}

app.whenReady().then(createWindow)

// IPC handler example
ipcMain.handle('get-data', async () => {
  return { message: 'Hello from main process' }
})

// preload.js
const { contextBridge, ipcRenderer } = require('electron')
contextBridge.exposeInMainWorld('api', {
  getData: () => ipcRenderer.invoke('get-data')
})

API Reference (api/)
api/app.md - app module API
api/browser-window.md - BrowserWindow API
api/ipc-main.md / api/ipc-renderer.md - IPC APIs
api/menu.md / api/tray.md / api/dialog.md - UI APIs
Best Practices
Security: Never enable nodeIntegration in renderer process, use preload scripts
Process separation: Keep main and renderer processes separate
IPC communication: Use IPC for safe communication between processes
Resource management: Properly clean up resources (windows, listeners)
Error handling: Implement proper error handling and crash reporting
Performance: Optimize for performance, use webContents for debugging
Packaging: Use Electron Forge or electron-builder for packaging
Auto updates: Implement auto-updater for production apps
Native modules: Handle native module compatibility
Cross-platform: Test on all target platforms
Resources
Official Website: https://www.electronjs.org/zh/
Documentation: https://www.electronjs.org/zh/docs/latest/
API Reference: https://www.electronjs.org/zh/docs/latest/api/app
Electron Forge: https://www.electronforge.io
Electron Fiddle: https://www.electronjs.org/zh/fiddle
GitHub Repository: https://github.com/electron/electron
Keywords

Electron, desktop app, main process, renderer process, preload, IPC, BrowserWindow, Menu, Tray, Dialog, packaging, electron-builder, electron-forge, electron-fiddle, cross-platform, 桌面应用, 主进程, 渲染进程, IPC 通信, 窗口, 菜单, 托盘, 打包

Weekly Installs
1.7K
Repository
teachingai/full…k-skills
GitHub Stars
349
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass