---
title: registry-component-patterns
url: https://skills.sh/theorcdev/8bitcn-ui/registry-component-patterns
---

# registry-component-patterns

skills/theorcdev/8bitcn-ui/registry-component-patterns
registry-component-patterns
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill registry-component-patterns
SKILL.md
Registry Component Patterns

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
  "name": "chapter-intro",
  "type": "registry:block",
  "title": "8-bit Chapter Intro",
  "description": "A cinematic chapter/level intro with pixel art background.",
  "registryDependencies": ["card"],
  "categories": ["gaming"],
  "files": [
    {
      "path": "components/ui/8bit/blocks/chapter-intro.tsx",
      "type": "registry:block",
      "target": "components/ui/8bit/blocks/chapter-intro.tsx"
    },
    {
      "path": "components/ui/8bit/styles/retro.css",
      "type": "registry:component",
      "target": "components/ui/8bit/styles/retro.css"
    },
    {
      "path": "components/ui/8bit/card.tsx",
      "type": "registry:component",
      "target": "components/ui/8bit/card.tsx"
    }
  ]
}

Required retro.css

Always include retro.css in registry entries:

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

Use gaming-specific categories:

"categories": ["gaming"]


Available categories: gaming, layout, form, data-display, feedback, navigation, overlay.

Registry Dependencies

List base shadcn dependencies:

"registryDependencies": ["button", "dialog"]


For blocks with multiple components:

"registryDependencies": ["card", "button", "progress"]

Key Principles
Type - Use registry:component for single components, registry:block for layouts
retro.css required - Always include in files array
Target path - Use same path for source and target
Categories - Use gaming for retro-themed components
Dependencies - List base shadcn/ui components (not 8-bit versions)
Description - Clear, concise description for CLI output
Adding a New Component
Create component in components/ui/8bit/component.tsx
Update registry.json with entry (copy existing component as template)
Include retro.css dependency
Test with: pnpm dlx shadcn@latest add @8bitcn/component
Weekly Installs
25
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