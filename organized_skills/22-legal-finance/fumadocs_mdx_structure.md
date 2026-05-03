---
rating: ⭐⭐⭐⭐⭐
title: fumadocs-mdx-structure
url: https://skills.sh/theorcdev/8bitcn-ui/fumadocs-mdx-structure
---

# fumadocs-mdx-structure

skills/theorcdev/8bitcn-ui/fumadocs-mdx-structure
fumadocs-mdx-structure
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill fumadocs-mdx-structure
SKILL.md
Fumadocs MDX Structure

Create well-structured MDX documentation files for 8-bit components following the established patterns.

Frontmatter Pattern
---
title: Component Name
description: Brief description of the 8-bit component.
---

Import Pattern

All documentation files require these imports:

import { ComponentName } from "@/components/ui/8bit/component-name";
import CopyCommandButton from "@/components/copy-command-button";
import InstallationCommands from "@/components/installation-commands";
import ComponentPreview from "@/components/component-preview";

Copy Command Button

Place immediately after frontmatter:

<div className="flex flex-col md:flex-row items-center justify-end gap-2 mb-2">
  <CopyCommandButton
    copyCommand="pnpm dlx shadcn@latest add @8bitcn/component-name"
    command="pnpm dlx shadcn@latest add @8bitcn/component-name"
  />
</div>

Component Preview

Wrap component examples:

<ComponentPreview title="8-bit ComponentName component" name="component-name">
  <ComponentName>Example</ComponentName>
</ComponentPreview>

Installation Section
## Installation

---

<InstallationCommands packageName="component-name" />

Usage Section
## Usage

---

```tsx
import { ComponentName } from "@/components/ui/8bit/component-name"

<ComponentName variant="outline">Example</ComponentName>


### Complete Example

```mdx
---
title: Button
description: Displays an 8-bit button component.
---

import { Button } from "@/components/ui/8bit/button";
import CopyCommandButton from "@/components/copy-command-button";
import InstallationCommands from "@/components/installation-commands";
import ComponentPreview from "@/components/component-preview";

<div className="flex flex-col md:flex-row items-center justify-end gap-2 mb-2">
  <CopyCommandButton
    copyCommand="pnpm dlx shadcn@latest add @8bitcn/button"
    command="pnpm dlx shadcn@latest add @8bitcn/button"
  />
</div>

<ComponentPreview title="8-bit button component" name="button">
  <Button>Button</Button>
</ComponentPreview>

## Installation

---

<InstallationCommands packageName="button" />

## Usage

---

```tsx
import { Button } from "@/components/ui/8bit/button"

<Button variant="outline">Button</Button>


### Key Principles

1. **Frontmatter required** - title and description are mandatory
2. **Import order** - Component → utilities → UI components
3. **Copy button** - Place before ComponentPreview
4. **ComponentPreview** - Use for all component examples
5. **Code blocks** - Use ```tsx for TypeScript examples
6. **Section separators** - Use `---` after headings
7. **8-bit imports** - Use `@/components/ui/8bit/` path

### File Location

Place documentation files in:
- `content/docs/components/component-name.mdx` for components
- `content/docs/blocks/category/block-name.mdx` for blocks

Weekly Installs
155
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