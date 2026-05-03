---
rating: ⭐⭐⭐
title: heroui-migration
url: https://skills.sh/heroui-inc/heroui/heroui-migration
---

# heroui-migration

skills/heroui-inc/heroui/heroui-migration
heroui-migration
Installation
$ npx skills add https://github.com/heroui-inc/heroui --skill heroui-migration
SKILL.md
HeroUI v2 to v3 Migration Guide

This skill helps agents migrate HeroUI v2 applications to v3. HeroUI v3 introduces breaking changes: compound components, no Provider, Tailwind v4, and removed hooks.

Installation
curl -fsSL https://heroui.com/install | bash -s heroui-migration

CRITICAL: Always Fetch Migration Docs Before Applying

Do NOT assume v2 patterns work in v3. Always fetch migration guides before implementing changes.

Key v2 → v3 Changes
Feature	v2 (Migrate From)	v3 (Migrate To)
Provider	<HeroUIProvider> required	No Provider needed
Component API	Flat props: <Card title="x">	Compound: <Card><Card.Header>
Event handlers	onClick	onPress
Styling	classNames prop	className prop
Hooks	useSwitch, useDisclosure, etc.	Compound components, useOverlayState
Packages	@heroui/system, @heroui/theme	@heroui/react, @heroui/styles
Accessing Migration Documentation

For migration details, examples, and step-by-step guides, always fetch documentation:

Using Scripts
# List all available component migration guides
node scripts/list_migration_guides.mjs

# Get main migration workflow (full or incremental)
node scripts/get_migration_guide.mjs full
node scripts/get_migration_guide.mjs incremental

# Get component-specific migration guides
node scripts/get_component_migration_guides.mjs button
node scripts/get_component_migration_guides.mjs button card modal

# Get styling migration guide
node scripts/get_styling_migration_guide.mjs

# Get hooks migration guide
node scripts/get_hooks_migration_guide.mjs

Direct URLs

Migration docs (preview): https://heroui-git-docs-migration-heroui.vercel.app/docs/react/migration/{filename}

Examples:

Full migration: .../agent-guide-full.mdx
Incremental: .../agent-guide-incremental.mdx
Button: .../button.mdx
Styling: .../styling.mdx
Hooks: .../hooks.mdx

Override base URL with HEROUI_MIGRATION_DOCS_BASE when docs are merged to production.

MCP Alternative

When using Cursor or other MCP clients, configure the Migration MCP server for tool-based access:

{
  "mcpServers": {
    "heroui-migration": {
      "url": "https://migration-mcp.heroui.com"
    }
  }
}

Migration Strategies
Full Migration
Best for: Projects that can dedicate focused time; teams comfortable with temporarily broken code
Migrate all component code first (project broken during migration)
Switch dependencies to v3
Complete styling migration
Incremental Migration
Best for: Projects that must stay functional; large codebases migrating gradually
Set up coexistence (pnpm aliases or component packages)
Migrate components one-by-one
Both v2 and v3 coexist during migration

Always fetch the agent guide before starting: node scripts/get_migration_guide.mjs full or incremental

Core Principles
Fetch first: Use scripts to get migration guides before applying changes
Compound components: v3 uses Card.Header, Card.Title, Button with children—not flat props
No Provider: Remove HeroUIProvider when migrating
onPress not onClick: All interactive components use onPress
Workflow: Analyze → Migrate components → Switch deps → Styling migration
Migration Workflow Summary
Create migration branch
Analyze project (HeroUI imports, component usage)
Fetch main guide: node scripts/get_migration_guide.mjs full
Migrate components in batches (fetch component guides per batch)
Switch dependencies to v3
Fetch styling guide: node scripts/get_styling_migration_guide.mjs
Apply styling updates
Preview Mode

This skill targets the staging deployment of the docs/migration branch. Once docs are merged to main and live on heroui.com, set HEROUI_MIGRATION_DOCS_BASE=https://heroui.com/docs/react/migration or update the default in scripts.

Weekly Installs
1.1K
Repository
heroui-inc/heroui
GitHub Stars
29.1K
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn