---
rating: ⭐⭐⭐
title: open-pencil-design-editor
url: https://skills.sh/aradotso/trending-skills/open-pencil-design-editor
---

# open-pencil-design-editor

skills/aradotso/trending-skills/open-pencil-design-editor
open-pencil-design-editor
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill open-pencil-design-editor
SKILL.md
OpenPencil Design Editor

Skill by ara.so — Daily 2026 Skills collection.

OpenPencil is an open-source, AI-native design editor that reads and writes native Figma (.fig) files, provides a headless CLI, an MCP server for AI agents, and a Vue SDK for building custom editors. It is MIT-licensed and runs in the browser, as a desktop app (Tauri/macOS/Windows/Linux), or fully headlessly.

Installation
Web app (no install)

Visit app.openpencil.dev/demo.

Desktop (macOS)
brew install open-pencil/tap/open-pencil


Or download from releases.

CLI
bun add -g @open-pencil/cli

MCP server
bun add -g @open-pencil/mcp

Local development
git clone https://github.com/open-pencil/open-pencil
cd open-pencil
bun install
bun run dev          # Web app at localhost:1420
bun run tauri dev    # Desktop (requires Rust)

CLI Reference

The open-pencil CLI operates on .fig files headlessly. When the desktop app is running, omit the file argument to connect to the live canvas via RPC.

Inspect file structure
# Print the full node tree
open-pencil tree design.fig

# Find nodes by type
open-pencil find design.fig --type TEXT
open-pencil find design.fig --type FRAME

# Get a specific node by ID
open-pencil node design.fig --id 1:23

# File metadata
open-pencil info design.fig

XPath queries
# All frames
open-pencil query design.fig "//FRAME"

# Frames narrower than 300px
open-pencil query design.fig "//FRAME[@width < 300]"

# Text nodes whose name contains "Button"
open-pencil query design.fig "//TEXT[contains(@name, 'Button')]"

# Nodes with rounded corners
open-pencil query design.fig "//*[@cornerRadius > 0]"

# Text inside sections
open-pencil query design.fig "//SECTION//TEXT"

Export
# PNG (default)
open-pencil export design.fig

# JPG at 2x scale, quality 90
open-pencil export design.fig -f jpg -s 2 -q 90

# SVG
open-pencil export design.fig -f svg

# WEBP
open-pencil export design.fig -f webp

# JSX with Tailwind v4 utility classes
open-pencil export design.fig -f jsx --style tailwind


Example Tailwind output:

<div className="flex flex-col gap-4 p-6 bg-white rounded-xl">
  <p className="text-2xl font-bold text-[#1D1B20]">Card Title</p>
  <p className="text-sm text-[#49454F]">Description text</p>
</div>

Design token analysis
open-pencil analyze colors design.fig
open-pencil analyze typography design.fig
open-pencil analyze spacing design.fig
open-pencil analyze clusters design.fig   # Repeated structures / component candidates

Scripting with Figma Plugin API (eval)
# Read: count children on the current page
open-pencil eval design.fig -c "figma.currentPage.children.length"

# Read: get all text node contents
open-pencil eval design.fig -c "figma.currentPage.findAll(n => n.type === 'TEXT').map(n => n.characters)"

# Write: set opacity of all selected nodes (-w writes back to file)
open-pencil eval design.fig -c "figma.currentPage.selection.forEach(n => n.opacity = 0.5)" -w

# Write: rename all frames on the page
open-pencil eval design.fig -c "figma.currentPage.findAll(n => n.type === 'FRAME').forEach((f, i) => f.name = 'Frame ' + i)" -w

# Connect to the live running desktop app (no file arg)
open-pencil eval -c "figma.currentPage.name"
open-pencil tree
open-pencil export -f png


All commands support --json for machine-readable output:

open-pencil find design.fig --type TEXT --json
open-pencil analyze colors design.fig --json

MCP Server

The MCP server exposes 90 tools (87 core + 3 file management) for AI agents to read and write .fig files.

Stdio (Claude Code, Cursor, Windsurf)
bun add -g @open-pencil/mcp


Add to your MCP client config (e.g. ~/.claude/mcp.json or Cursor settings):

{
  "mcpServers": {
    "open-pencil": {
      "command": "openpencil-mcp"
    }
  }
}

HTTP server (scripts, CI)
openpencil-mcp-http
# Listens at http://localhost:3100/mcp

Claude Code desktop integration
Install the ACP adapter:
npm i -g @zed-industries/claude-agent-acp

Add MCP permission to ~/.claude/settings.json:
{
  "permissions": {
    "allow": ["mcp__open-pencil"]
  }
}

Open the desktop app → Ctrl+J → select Claude Code from the provider dropdown.
Agent skill (quick setup)
npx skills add open-pencil/skills@open-pencil

AI Chat (Built-in)
Open with ⌘J (macOS) or Ctrl+J (desktop/web).
87 tools: create shapes, set fills/strokes, manage auto-layout, work with components and variables, boolean operations, token analysis, asset export.
Bring your own API key — no backend or account required.
Supported providers

Configure via the provider dropdown in the chat panel:

Provider	Env var
Anthropic	ANTHROPIC_API_KEY
OpenAI	OPENAI_API_KEY
Google AI	GOOGLE_AI_API_KEY
OpenRouter	OPENROUTER_API_KEY
Any compatible endpoint	Custom base URL
Real-time Collaboration

No server, no account. Peer-to-peer via WebRTC.

Click the Share button (top-right).
Share the generated URL: app.openpencil.dev/share/<room-id>.
Peers see live cursors, selections, and edits.
Click a peer's avatar to follow their viewport.
Project Structure
packages/
  core/     @open-pencil/core  — engine: scene graph, renderer, layout, codec
  cli/      @open-pencil/cli   — headless CLI
  mcp/      @open-pencil/mcp   — MCP server (stdio + HTTP)
  docs/     Documentation site
src/        Vue 3 app — components, composables, stores
desktop/    Tauri v2 (Rust + config)
tests/      E2E (188 tests) + unit (764 tests)

Tech stack
Layer	Technology
Rendering	Skia (CanvasKit WASM)
Layout	Yoga WASM (flex + CSS Grid)
UI	Vue 3, Reka UI, Tailwind CSS 4
File format	Kiwi binary + Zstd + ZIP
Collaboration	Trystero (WebRTC P2P) + Yjs (CRDT)
Desktop	Tauri v2
AI/MCP	Anthropic, OpenAI, Google AI, OpenRouter; MCP SDK; Hono
Development Commands
bun run dev        # Start web dev server (localhost:1420)
bun run tauri dev  # Start desktop app (requires Rust)
bun run check      # Lint + typecheck
bun run test       # E2E visual regression tests
bun run test:unit  # Unit tests
bun run format     # Code formatting
bun run tauri build  # Production desktop build


Desktop prerequisites: Rust + Tauri v2 platform deps.

Common Patterns
Batch-rename all text nodes in a .fig file
open-pencil eval design.fig \
  -c "figma.currentPage.findAll(n => n.type === 'TEXT').forEach((t, i) => t.name = 'Text_' + i)" \
  -w

Extract all colors as JSON
open-pencil analyze colors design.fig --json > colors.json

Export every frame as PNG in CI
for id in $(open-pencil find design.fig --type FRAME --json | jq -r '.[].id'); do
  open-pencil export design.fig --id "$id" -f png -o "frames/$id.png"
done

Query nodes matching a naming convention
# Find all nodes named with a "btn-" prefix
open-pencil query design.fig "//*[starts-with(@name, 'btn-')]"

Connect an MCP client to a running desktop app

When the desktop app is open, the MCP stdio server can connect to the live canvas. No file path needed — all reads and writes go to the open document.

{
  "mcpServers": {
    "open-pencil": {
      "command": "openpencil-mcp"
    }
  }
}

Export a selection as Tailwind JSX programmatically
open-pencil export design.fig --id 1:23 -f jsx --style tailwind

Troubleshooting

openpencil-mcp not found after install

Ensure bun's global bin dir is on your PATH: export PATH="$HOME/.bun/bin:$PATH"
Or use npx openpencil-mcp as the MCP command value.

Desktop app CLI connection fails

The desktop app must be running before issuing commands without a file argument.
Check that no firewall rule blocks the local RPC socket.

Tauri dev build errors

Install platform prerequisites: v2.tauri.app/start/prerequisites
Ensure Rust is up to date: rustup update

.fig file won't open

Confirm the file was exported from Figma (not a .fig backup or plugin artifact).
Run open-pencil info design.fig to check if the codec can parse the header.

AI chat returns no response

Verify your API key is set correctly in the provider settings panel.
For OpenRouter, ensure your key has credits and the selected model is available.

Collaboration peers not connecting

Both peers must use the exact same share URL (room ID is case-sensitive).
WebRTC requires both peers to allow the browser/app through any firewall.
Links
Web app: app.openpencil.dev/demo
Documentation: openpencil.dev
MCP tools reference: openpencil.dev/reference/mcp-tools
Releases: github.com/open-pencil/open-pencil/releases
License: MIT
Weekly Installs
576
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass