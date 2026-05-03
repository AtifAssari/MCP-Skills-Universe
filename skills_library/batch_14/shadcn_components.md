---
title: shadcn-components
url: https://skills.sh/sgcarstrends/sgcarstrends/shadcn-components
---

# shadcn-components

skills/sgcarstrends/sgcarstrends/shadcn-components
shadcn-components
Installation
$ npx skills add https://github.com/sgcarstrends/sgcarstrends --skill shadcn-components
SKILL.md
shadcn/ui Components Skill

Components live in packages/ui/. shadcn/ui is copied into your codebase for full control.

packages/ui/
├── src/
│   ├── components/     # shadcn/ui components
│   ├── lib/utils.ts    # cn() utility
│   └── styles/globals.css
├── components.json     # shadcn/ui config
└── package.json

Discovery with MCP Tools
// Search for components
mcp__shadcn__search_items_in_registries({ registries: ["@shadcn"], query: "button" })

// View component details
mcp__shadcn__view_items_in_registries({ items: ["@shadcn/button", "@shadcn/card"] })

// Get add command
mcp__shadcn__get_add_command_for_items({ items: ["@shadcn/dropdown-menu"] })

Adding Components
cd packages/ui
npx shadcn@latest add dropdown-menu
npx shadcn@latest add dropdown-menu select tabs  # Multiple


Export in packages/ui/src/index.ts:

export {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
} from "./components/dropdown-menu";


Use in apps:

import { DropdownMenu, DropdownMenuTrigger, DropdownMenuContent, DropdownMenuItem } from "@sgcarstrends/ui";

Core Components
// Button variants: default, destructive, outline, secondary, ghost, link
// Button sizes: default, sm, lg, icon
<Button variant="destructive" size="sm">Delete</Button>

// Card composition
<Card>
  <CardHeader>
    <CardTitle>Title</CardTitle>
    <CardDescription>Description</CardDescription>
  </CardHeader>
  <CardContent>Content</CardContent>
  <CardFooter>Footer</CardFooter>
</Card>

// Dialog
<Dialog>
  <DialogTrigger asChild><Button>Open</Button></DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Confirm</DialogTitle>
      <DialogDescription>Are you sure?</DialogDescription>
    </DialogHeader>
  </DialogContent>
</Dialog>

// Form elements
<Label htmlFor="name">Name</Label>
<Input id="name" placeholder="Enter name" />
<Textarea id="message" />

// Badge variants: default, secondary, destructive, outline
<Badge variant="secondary">Status</Badge>

Customizing Variants

Edit component file directly in packages/ui/src/components/:

// button.tsx - Add custom variant
const buttonVariants = cva("inline-flex items-center...", {
  variants: {
    variant: {
      // existing variants...
      success: "bg-green-500 text-white hover:bg-green-600",
    },
    size: {
      // existing sizes...
      xl: "h-14 rounded-md px-10 text-lg",
    },
  },
});

Creating Compound Components
// packages/ui/src/components/stat-card.tsx
import { Card, CardHeader, CardTitle, CardContent } from "./card";
import { cn } from "../lib/utils";

interface StatCardProps {
  title: string;
  value: string | number;
  trend?: "up" | "down";
  className?: string;
}

export function StatCard({ title, value, trend, className }: StatCardProps) {
  return (
    <Card className={cn("", className)}>
      <CardHeader className="flex flex-row items-center justify-between pb-2">
        <CardTitle className="text-sm font-medium">{title}</CardTitle>
        {trend && <span className={trend === "up" ? "text-green-500" : "text-red-500"}>{trend === "up" ? "↑" : "↓"}</span>}
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{value}</div>
      </CardContent>
    </Card>
  );
}

cn() Utility
import { cn } from "@sgcarstrends/ui/lib/utils";

<div className={cn("base-classes", condition && "conditional", className)}>

Theming (CSS Variables)

Edit packages/ui/src/styles/globals.css:

@layer base {
  :root {
    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;
    /* ... */
  }
  .dark {
    --primary: 210 40% 98%;
    /* ... */
  }
}

Updating Components
cd packages/ui
npx shadcn@latest add button --overwrite

Troubleshooting
Component not found: Check export in packages/ui/src/index.ts
Styling not applied: Verify content paths in tailwind.config.ts
TypeScript errors: Run pnpm build in packages/ui
Best Practices
Use MCP Tools: Search before adding to avoid duplicates
Export Components: Always export in index.ts
Size Utility: Use size-* instead of h-* w-* for equal dimensions
Extend, don't modify: Add custom variants rather than changing core styles
References
shadcn/ui: https://ui.shadcn.com
packages/ui/CLAUDE.md for package details
Weekly Installs
80
Repository
sgcarstrends/sg…rstrends
GitHub Stars
20
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn