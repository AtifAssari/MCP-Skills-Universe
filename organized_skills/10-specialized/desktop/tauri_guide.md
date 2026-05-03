---
rating: ⭐⭐⭐
title: tauri-guide
url: https://skills.sh/0xraduan/raduan-plugins/tauri-guide
---

# tauri-guide

skills/0xraduan/raduan-plugins/tauri-guide
tauri-guide
Installation
$ npx skills add https://github.com/0xraduan/raduan-plugins --skill tauri-guide
SKILL.md
Tauri + React Architecture Guide

This guide explains how to build well-structured Tauri + React desktop applications.

References

For detailed documentation on specific topics:

Distribution & Updates
Auto-Updates - Implementing automatic updates with signing, hosting, and best practices
Code Signing - Code signing, notarization, and entitlements for macOS distribution
macOS Native Features
Window Chrome - Title bars, traffic lights, draggable regions, and vibrancy effects
Menu System - Native app menus, keyboard shortcuts, and context menus
Permissions - Handling screen recording, camera, microphone, and other permissions
Deep Linking - URL schemes, OAuth callbacks, and opening content from URLs
App Architecture
Multi-Window - Managing multiple windows, spotlight panels, and inter-window communication
Data Storage - Where to store databases, files, caches, and preferences
First-Run Experience - Onboarding, permission priming, and app location verification
Rust vs TypeScript: Where Does Code Live?

The most important architectural decision in a Tauri app is knowing what belongs in Rust vs what belongs in TypeScript. Here's a clear framework:

Use Rust (src-tauri/) For:
Capability	Why Rust?	Example
Global shortcuts	OS-level keyboard hooks	Alt+Space to open from anywhere
System tray	Native menu bar integration	Tray icon with menu
Window management	Native window APIs	Spotlight-style panels, vibrancy effects
Screenshot capture	OS screen capture APIs	screencapture on macOS
Deep links	URL scheme registration	myapp://open/123
File system watching	Efficient OS notifications	Watch for file changes
Native dialogs	OS file pickers	Open/save dialogs
Clipboard	System clipboard access	Copy/paste integration
Notifications	System notification center	Push notifications
Auto-updates	Binary replacement	App update flow
Process spawning	Running external processes	MCP servers, CLI tools
Permission requests	OS permission dialogs	Screen recording access
Use TypeScript (src/) For:
Capability	Why TypeScript?	Example
All UI	React ecosystem	Components, layouts
Business logic	Faster iteration	Validation, transformations
Database queries	SQL via plugin	CRUD operations
API calls	Fetch/streaming	AI provider integrations
State management	React/TanStack Query	App state, cache
Routing	React Router	Navigation
Forms	React patterns	User input
Decision Framework

Ask these questions:

Does it need OS-level access? → Rust
Does it need to work when app isn't focused? → Rust
Does it interact with native UI chrome? → Rust
Is it purely data/UI logic? → TypeScript
Does it need fast iteration? → TypeScript (hot reload)
Real-World Examples

Spotlight-style quick launcher (like Raycast, Alfred):

Rust:
- Global shortcut registration (Cmd+Space)
- Panel window type (non-activating, floating)
- Vibrancy/blur effects
- Show/hide without focus stealing

TypeScript:
- Search UI
- Result rendering
- Keyboard navigation within the panel
- Search logic


Screenshot annotation tool:

Rust:
- Screen capture (needs permissions)
- Window enumeration
- Save to disk
- Clipboard integration

TypeScript:
- Annotation canvas
- Tool palette
- Undo/redo
- Export options UI


AI chat app (like the app that inspired this guide):

Rust:
- Global shortcut for quick chat
- System tray
- Deep links (chorus://chat/123)
- Screenshot capture for context
- Image resizing for LLM limits

TypeScript:
- Chat UI
- Message streaming
- Model provider integrations
- Database queries
- Settings UI

Anti-Patterns to Avoid

Don't use Rust for:

Business logic that could be in TypeScript
UI rendering (use React)
API calls (use fetch in TypeScript)
Complex state management

Don't use TypeScript for:

Anything requiring sudo or elevated permissions
System-wide keyboard shortcuts
Native window decorations
Accessing restricted OS APIs
Communication Pattern

When Rust and TypeScript need to talk:

TypeScript → Rust: invoke("command_name", { args })
Rust → TypeScript: events (emit/listen)


Keep the boundary thin. Pass simple data (strings, numbers, JSON), not complex objects.

Core Architecture
┌─────────────────────────────────────────────────────────────┐
│                    React Components                          │
│                    (src/ui/components/)                      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    TanStack Query                            │
│              (caching, state management)                     │
│                    (src/core/api/)                           │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   Database Layer                             │
│                 (direct SQL queries)                         │
│                    (src/core/db/)                            │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      SQLite                                  │
│              (via tauri-plugin-sql)                          │
└─────────────────────────────────────────────────────────────┘

Project Structure
my-app/
├── src/                          # Frontend (React/TypeScript)
│   ├── ui/                       # Presentation layer
│   │   ├── components/           # React components
│   │   ├── hooks/                # Custom React hooks
│   │   ├── providers/            # Context providers
│   │   └── App.tsx               # Root component
│   ├── core/                     # Business logic
│   │   ├── api/                  # TanStack Query queries/mutations
│   │   ├── db/                   # Database access functions
│   │   └── types/                # TypeScript types
│   └── main.tsx                  # Entry point
├── src-tauri/                    # Backend (Rust)
│   └── src/
│       ├── lib.rs                # Tauri initialization
│       ├── commands.rs           # Tauri commands (IPC)
│       └── migrations.rs         # SQLite schema migrations
└── index.html                    # Vite entry

Data Flow Pattern
1. Define Types
// src/core/types/Note.ts
export interface Note {
    id: string;
    title: string;
    content: string;
    createdAt: Date;
    updatedAt: Date;
}

2. Create Database Functions
// src/core/db/notes.ts
import { db } from "./connection";
import type { Note } from "../types/Note";

export async function fetchNotes(): Promise<Note[]> {
    const rows = await db.select<NoteRow[]>("SELECT * FROM notes ORDER BY updated_at DESC");
    return rows.map(rowToNote);
}

export async function createNote(note: Omit<Note, "id" | "createdAt" | "updatedAt">): Promise<Note> {
    const id = crypto.randomUUID();
    const now = new Date().toISOString();

    await db.execute(
        "INSERT INTO notes (id, title, content, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
        [id, note.title, note.content, now, now]
    );

    return { id, ...note, createdAt: new Date(now), updatedAt: new Date(now) };
}

// Helper to convert DB row to domain object
function rowToNote(row: NoteRow): Note {
    return {
        id: row.id,
        title: row.title,
        content: row.content,
        createdAt: new Date(row.created_at),
        updatedAt: new Date(row.updated_at),
    };
}

3. Create TanStack Query Layer
// src/core/api/notes.ts
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { fetchNotes, createNote } from "../db/notes";
import type { Note } from "../types/Note";

// Query keys - hierarchical for easy invalidation
export const noteKeys = {
    all: ["notes"] as const,
    lists: () => [...noteKeys.all, "list"] as const,
    detail: (id: string) => [...noteKeys.all, "detail", id] as const,
};

// Queries
export const noteQueries = {
    list: () => ({
        queryKey: noteKeys.lists(),
        queryFn: fetchNotes,
        staleTime: Infinity,  // Data is local, no need to refetch
    }),
};

// Hooks
export function useNotes() {
    return useQuery(noteQueries.list());
}

export function useCreateNote() {
    const queryClient = useQueryClient();

    return useMutation({
        mutationFn: createNote,
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: noteKeys.lists() });
        },
    });
}

4. Use in Components
// src/ui/components/NoteList.tsx
import { useNotes, useCreateNote } from "@core/api/notes";

export function NoteList() {
    const { data: notes, isLoading } = useNotes();
    const createNote = useCreateNote();

    if (isLoading) return <div>Loading...</div>;

    return (
        <div>
            <button
                onClick={() => createNote.mutate({ title: "New Note", content: "" })}
            >
                Add Note
            </button>

            {notes?.map(note => (
                <div key={note.id}>{note.title}</div>
            ))}
        </div>
    );
}

Database Patterns
Migrations
// src-tauri/src/migrations.rs
pub fn get_migrations() -> Vec<Migration> {
    vec![
        Migration {
            version: 1,
            description: "create_notes_table",
            sql: r#"
                CREATE TABLE IF NOT EXISTS notes (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL DEFAULT '',
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );
            "#,
            kind: MigrationKind::Up,
        },
        // Add more migrations as your schema evolves
    ]
}

Database Connection
// src/core/db/connection.ts
import Database from "@tauri-apps/plugin-sql";

let database: Database | null = null;

export async function initDatabase(): Promise<Database> {
    if (!database) {
        database = await Database.load("sqlite:app.db");
    }
    return database;
}

export { database as db };

Best Practices
No foreign keys - They're hard to remove and cause migration headaches
Use TEXT for dates - Store as ISO 8601 strings, convert in TypeScript
Prefer undefined over null - Convert DB nulls: value ?? undefined
Use UUIDs for IDs - crypto.randomUUID() works everywhere
Tauri Commands (IPC)

For operations that need native capabilities:

Define in Rust
// src-tauri/src/commands.rs
use tauri::command;

#[command]
pub fn get_app_version() -> String {
    env!("CARGO_PKG_VERSION").to_string()
}

#[command]
pub async fn read_file(path: String) -> Result<String, String> {
    std::fs::read_to_string(&path)
        .map_err(|e| e.to_string())
}

Register in lib.rs
// src-tauri/src/lib.rs
mod commands;

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            commands::get_app_version,
            commands::read_file,
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}

Call from React
import { invoke } from "@tauri-apps/api/core";

// Simple call
const version = await invoke<string>("get_app_version");

// With arguments
const content = await invoke<string>("read_file", { path: "/path/to/file" });

State Management
When to Use What
State Type	Solution
Server/DB state	TanStack Query
App-wide UI state	React Context
Component state	useState/useReducer
Form state	React Hook Form or local state
Context Pattern
// src/ui/providers/AppProvider.tsx
import { createContext, useContext, useState, type ReactNode } from "react";

interface AppState {
    sidebarOpen: boolean;
    toggleSidebar: () => void;
}

const AppContext = createContext<AppState | null>(null);

export function AppProvider({ children }: { children: ReactNode }) {
    const [sidebarOpen, setSidebarOpen] = useState(true);

    return (
        <AppContext.Provider value={{
            sidebarOpen,
            toggleSidebar: () => setSidebarOpen(prev => !prev),
        }}>
            {children}
        </AppContext.Provider>
    );
}

export function useApp() {
    const context = useContext(AppContext);
    if (!context) throw new Error("useApp must be used within AppProvider");
    return context;
}

Styling
Tailwind + Radix UI
import * as Dialog from "@radix-ui/react-dialog";

export function Modal({ children, open, onOpenChange }) {
    return (
        <Dialog.Root open={open} onOpenChange={onOpenChange}>
            <Dialog.Portal>
                <Dialog.Overlay className="fixed inset-0 bg-black/50" />
                <Dialog.Content className="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white rounded-lg p-6 shadow-xl">
                    {children}
                </Dialog.Content>
            </Dialog.Portal>
        </Dialog.Root>
    );
}

Theme Support
// src/ui/providers/ThemeProvider.tsx
export function ThemeProvider({ children }) {
    const [theme, setTheme] = useState<"light" | "dark">("light");

    useEffect(() => {
        document.documentElement.classList.toggle("dark", theme === "dark");
    }, [theme]);

    return (
        <ThemeContext.Provider value={{ theme, setTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

Path Aliases

Configure in tsconfig.json:

{
  "compilerOptions": {
    "paths": {
      "@ui/*": ["./src/ui/*"],
      "@core/*": ["./src/core/*"],
      "@/*": ["./src/*"]
    }
  }
}


Use throughout:

import { Button } from "@ui/components/Button";
import { useNotes } from "@core/api/notes";

Common Tauri Plugins
Plugin	Purpose
tauri-plugin-sql	SQLite database
tauri-plugin-store	Key-value storage
tauri-plugin-fs	File system access
tauri-plugin-dialog	Native dialogs
tauri-plugin-clipboard	Clipboard access
tauri-plugin-notification	System notifications
tauri-plugin-updater	Auto-updates
tauri-plugin-global-shortcut	Global keyboard shortcuts
macOS-Specific Native Features

Tauri can access powerful macOS-specific APIs through Rust. Here are patterns for common features:

Spotlight-Style Panels

Convert a window into a floating panel that behaves like Spotlight:

// Cargo.toml
[target.'cfg(target_os = "macos")'.dependencies]
tauri-nspanel = "0.1"

// src-tauri/src/lib.rs
#[cfg(target_os = "macos")]
use tauri_nspanel::{panel_delegate, WebviewWindowExt};

// Convert window to panel
#[cfg(target_os = "macos")]
fn setup_panel(window: &tauri::WebviewWindow) {
    let panel = window.to_panel().unwrap();

    // Floating above other windows
    panel.set_level(NSMainMenuWindowLevel + 1);

    // Non-activating (doesn't steal focus)
    panel.set_style_mask(NSWindowStyleMaskNonActivatingPanel);

    // Works on all spaces/desktops
    panel.set_collection_behavior(
        NSWindowCollectionBehaviorCanJoinAllSpaces |
        NSWindowCollectionBehaviorFullScreenAuxiliary
    );
}

Vibrancy/Glassmorphism

Add macOS blur effects:

use tauri::window::Effect;

window.set_effects(
    EffectsBuilder::default()
        .effect(Effect::Popover)  // or HudWindow, Sidebar, etc.
        .state(EffectState::Active)
        .build()
);

Global Shortcuts
// src-tauri/src/lib.rs
use tauri_plugin_global_shortcut::{GlobalShortcutExt, Shortcut};

app.handle().plugin(
    tauri_plugin_global_shortcut::Builder::new()
        .with_handler(move |_app, shortcut, event| {
            if shortcut == &Shortcut::new(Some(Modifiers::ALT), Code::Space) {
                if event.state == ShortcutState::Pressed {
                    // Toggle your quick panel
                    toggle_panel();
                }
            }
        })
        .build(),
)?;

Screenshot Capture
#[tauri::command]
async fn capture_screen() -> Result<String, String> {
    let temp_path = std::env::temp_dir().join("screenshot.png");

    // Use native screencapture on macOS
    let output = std::process::Command::new("screencapture")
        .args(["-i", "-x", temp_path.to_str().unwrap()])  // -i: interactive, -x: no sound
        .output()
        .map_err(|e| e.to_string())?;

    if output.status.success() {
        let bytes = std::fs::read(&temp_path).map_err(|e| e.to_string())?;
        Ok(base64::encode(&bytes))
    } else {
        Err("Screenshot cancelled".to_string())
    }
}

Permission Handling

Check and request permissions:

#[tauri::command]
fn check_screen_recording_permission() -> bool {
    #[cfg(target_os = "macos")]
    {
        // CGPreflightScreenCaptureAccess returns true if permission granted
        unsafe {
            core_graphics::display::CGPreflightScreenCaptureAccess()
        }
    }
    #[cfg(not(target_os = "macos"))]
    true
}

#[tauri::command]
fn open_privacy_settings() {
    #[cfg(target_os = "macos")]
    {
        std::process::Command::new("open")
            .arg("x-apple.systempreferences:com.apple.preference.security?Privacy_ScreenCapture")
            .spawn()
            .ok();
    }
}

Menu Bar Integration
use tauri::menu::{Menu, MenuItem, PredefinedMenuItem};

let menu = Menu::with_items(&app, &[
    &Submenu::with_items(&app, "File", true, &[
        &MenuItem::with_id(&app, "new", "New", true, Some("CmdOrCtrl+N"))?,
        &PredefinedMenuItem::separator(&app)?,
        &MenuItem::with_id(&app, "quit", "Quit", true, Some("CmdOrCtrl+Q"))?,
    ])?,
])?;

app.set_menu(menu)?;

// Handle menu events
app.on_menu_event(|app, event| {
    match event.id().as_ref() {
        "new" => { /* handle new */ }
        "quit" => app.exit(0),
        _ => {}
    }
});

Auto-Updates

Auto-updates are essential for desktop apps. Tauri provides a built-in updater plugin.

Quick Setup
Generate signing keys:
pnpm tauri signer generate -w ~/.tauri/myapp.key

Configure tauri.conf.json:
{
  "bundle": {
    "createUpdaterArtifacts": true
  },
  "plugins": {
    "updater": {
      "pubkey": "YOUR_PUBLIC_KEY",
      "endpoints": [
        "https://your-update-server.com/{{target}}-{{arch}}/{{current_version}}"
      ]
    }
  }
}

Check for updates in React:
import { check } from "@tauri-apps/plugin-updater";
import { relaunch } from "@tauri-apps/plugin-process";

const update = await check();
if (update) {
    await update.downloadAndInstall();
    await relaunch();
}

Best Practices
Do	Don't
Download silently in background	Block UI during download
Let user choose when to restart	Auto-restart without warning
Poll every 5 minutes	Only check on startup
Handle errors gracefully	Crash on update failure
Skip update checks in dev mode	Annoy developers with prompts
Hosting Options
CrabNebula - Purpose-built for Tauri, zero config
GitHub Releases - Free, integrates with CI
Self-hosted - Full control, more work

For complete implementation details including production-ready code, CI/CD setup, and security considerations, see references/auto-updates.md.

Building for Production
# Development
pnpm tauri dev

# Production build
pnpm tauri build

# Output: src-tauri/target/release/bundle/

Further Reading
Tauri Documentation
TanStack Query
Radix UI
Weekly Installs
12
Repository
0xraduan/raduan-plugins
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn