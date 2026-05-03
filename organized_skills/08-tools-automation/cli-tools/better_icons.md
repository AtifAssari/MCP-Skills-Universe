---
rating: ⭐⭐⭐
title: better-icons
url: https://skills.sh/better-auth/better-icons/better-icons
---

# better-icons

skills/better-auth/better-icons/better-icons
better-icons
Installation
$ npx skills add https://github.com/better-auth/better-icons --skill better-icons
Summary

Search and retrieve SVGs from 200+ icon libraries with CLI and MCP server integration.

Supports searching across major collections (Lucide, Material Design Icons, Heroicons, Tabler, and 200+ more) with filtering by prefix and result limits
CLI commands for searching icons, downloading batches as SVG files, and retrieving individual icons with color and size customization
MCP server tools for AI agents including smart recommendations, similarity matching, project scanning, and batch icon retrieval (up to 20 at once)
Icon ID format uses prefix:name convention (e.g., lucide:home, mdi:arrow-right) for consistent referencing across all libraries
SKILL.md
Better Icons

Search and retrieve icons from 200+ libraries via Iconify.

Installation

Before using any better-icons commands, ensure the tool is available in the environment.

Option 1 — Install globally (recommended, matches all examples below):

# Using npm
npm install -g better-icons

# Using Bun (faster)
bun add -g better-icons


Option 2 — Run without installing (prefix every command with npx or bunx):

# Using npx (npm)
npx better-icons search arrow --limit 10
npx better-icons get lucide:home > icon.svg

# Using bunx (Bun — faster)
bunx better-icons search arrow --limit 10
bunx better-icons get lucide:home > icon.svg


For AI agents: Prefer the global install so that better-icons is on $PATH and the commands below work as-is. Run the install step once during environment setup, then use the commands without npx/bunx.

CLI
# Search icons
better-icons search <query> [--prefix <prefix>] [--limit <n>] [--json]

# Search and download all found icons as SVG files
better-icons search <query> -d [dir] [--color <color>] [--size <px>]

# Get icon SVG (outputs to stdout)
better-icons get <icon-id> [--color <color>] [--size <px>] [--json]

# Setup MCP server for AI agents
better-icons setup [-a cursor,claude-code] [-s global|project]

Examples
better-icons search arrow --limit 10
better-icons search home --json | jq '.icons[0]'
better-icons get lucide:home > icon.svg
better-icons get mdi:home --color '#333' --json

# Batch download all search results
better-icons search arrow -d              # saves to ./icons/
better-icons search check -d ./my-icons   # saves to ./my-icons/
better-icons search star -d -c '#000' -s 24 --limit 64

Icon ID Format

prefix:name - e.g., lucide:home, mdi:arrow-right, heroicons:check

Popular Collections

lucide, mdi, heroicons, tabler, ph, ri, solar, iconamoon

MCP Tools (for AI agents)
Tool	Description
search_icons	Search across all libraries
get_icon	Get single icon SVG
get_icons	Batch retrieve multiple icons
list_collections	Browse available icon sets
recommend_icons	Smart recommendations for use cases
find_similar_icons	Find variations across collections
sync_icon	Add icon to project file
scan_project_icons	List icons in project
TypeScript Interfaces
interface SearchIcons {
  query: string
  limit?: number        // 1-999, default 32
  prefix?: string       // e.g., 'mdi', 'lucide'
  category?: string     // e.g., 'General', 'Emoji'
}

interface GetIcon {
  icon_id: string       // 'prefix:name' format
  color?: string        // e.g., '#ff0000', 'currentColor'
  size?: number         // pixels
}

interface GetIcons {
  icon_ids: string[]    // max 20
  color?: string
  size?: number
}

interface RecommendIcons {
  use_case: string      // e.g., 'navigation menu'
  style?: 'solid' | 'outline' | 'any'
  limit?: number        // default 10
}

interface SyncIcon {
  icons_file: string    // absolute path
  framework: 'react' | 'vue' | 'svelte' | 'solid' | 'svg'
  icon_id: string
  component_name?: string
}

API

All icons from https://api.iconify.design

Weekly Installs
2.4K
Repository
better-auth/better-icons
GitHub Stars
975
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass