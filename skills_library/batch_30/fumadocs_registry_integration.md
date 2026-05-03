---
title: fumadocs-registry-integration
url: https://skills.sh/theorcdev/8bitcn-ui/fumadocs-registry-integration
---

# fumadocs-registry-integration

skills/theorcdev/8bitcn-ui/fumadocs-registry-integration
fumadocs-registry-integration
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill fumadocs-registry-integration
SKILL.md
Registry Integration

Register 8-bit components in registry.json for discovery via shadcn add @8bitcn/[component-name].

Component Entry Pattern
{
  "name": "button",
  "type": "registry:component",
  "title": "8-bit Button",
  "description": "A simple 8-bit button component",
  "registryDependencies": ["button"],
  "files": [
    {
      "path": "components/ui/8bit/button.tsx",
      "type": "registry:component",
      "target": "components/ui/8bit/button.tsx"
    },
    {
      "path": "components/ui/8bit/styles/retro.css",
      "type": "registry:component",
      "target": "components/ui/8bit/styles/retro.css"
    }
  ]
}

Block Entry Pattern

For pre-built layouts like game UIs:

{
  "name": "quest-log",
  "type": "registry:block",
  "title": "8-bit Quest Log",
  "description": "An 8-bit quest and mission tracking system.",
  "registryDependencies": ["card", "accordion"],
  "categories": ["gaming"],
  "files": [
    {
      "path": "components/ui/8bit/quest-log.tsx",
      "type": "registry:block",
      "target": "components/ui/8bit/quest-log.tsx"
    },
    {
      "path": "components/ui/8bit/styles/retro.css",
      "type": "registry:component",
      "target": "components/ui/8bit/styles/retro.css"
    }
  ]
}

Required retro.css

Always include retro.css in files array:

"files": [
  {
    "path": "components/ui/8bit/new-component.tsx",
    "type": "registry:component",
    "target": "components/ui/8bit/new-component.tsx"
  },
  {
    "path": "components/ui/8bit/styles/retro.css",
    "type": "registry:component",
    "target": "components/ui/8bit/styles/retro.css"
  }
]

Categories

Use gaming-specific categories for game components:

"categories": ["gaming"]


Available categories: gaming, layout, form, data-display, feedback, navigation, overlay.

Registry Dependencies

List base shadcn dependencies (not 8-bit versions):

"registryDependencies": ["button", "dialog", "progress"]


For blocks with multiple components:

"registryDependencies": ["card", "button", "progress", "tabs"]

Type Selection

registry:component - Single reusable component:

{
  "type": "registry:component",
  "files": [...]
}


registry:block - Pre-built layout or feature:

{
  "type": "registry:block",
  "categories": ["gaming"],
  "files": [...]
}

Complete Example
{
  "name": "health-bar",
  "type": "registry:component",
  "title": "8-bit Health Bar",
  "description": "An 8-bit health bar component for game UI.",
  "registryDependencies": ["progress"],
  "files": [
    {
      "path": "components/ui/8bit/health-bar.tsx",
      "type": "registry:component",
      "target": "components/ui/8bit/health-bar.tsx"
    },
    {
      "path": "components/ui/8bit/progress.tsx",
      "type": "registry:component",
      "target": "components/ui/8bit/progress.tsx"
    },
    {
      "path": "components/ui/8bit/styles/retro.css",
      "type": "registry:component",
      "target": "components/ui/8bit/styles/retro.css"
    }
  ]
}

Key Principles
Type - Use registry:component for single, registry:block for layouts
retro.css required - Always include in files array
Target path - Same path for source and target
Categories - Use gaming for retro-themed blocks
Dependencies - List base shadcn/ui components (not 8-bit)
Description - Clear, concise for CLI output
Files order - Component first, retro.css last
Adding a New Component
Create component in components/ui/8bit/component.tsx
Create documentation in content/docs/components/component.mdx
Add entry to registry.json:
Copy existing component as template
Update name, title, description
Set correct registryDependencies
Include retro.css in files
Test: pnpm dlx shadcn@latest add @8bitcn/component
Reference
registry.json - Full component registry
content/docs/components/*.mdx - Component documentation
Weekly Installs
57
Repository
theorcdev/8bitcn-ui
GitHub Stars
1.8K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass