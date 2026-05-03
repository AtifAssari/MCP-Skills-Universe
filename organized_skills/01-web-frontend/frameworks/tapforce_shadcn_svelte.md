---
rating: ⭐⭐
title: tapforce-shadcn-svelte
url: https://skills.sh/tapforce/agents-skills/tapforce-shadcn-svelte
---

# tapforce-shadcn-svelte

skills/tapforce/agents-skills/tapforce-shadcn-svelte
tapforce-shadcn-svelte
Installation
$ npx skills add https://github.com/tapforce/agents-skills --skill tapforce-shadcn-svelte
SKILL.md
tapforce-shadcn-svelte

This skill provides comprehensive guidance for setting up and using the shadcn-svelte library in Svelte projects. It covers installation, configuration, component usage, theming, and best practices.

Requirements
Project must be based on SvelteKit framework version 2.0 or higher
Project must use Svelte 5.0 or higher
Project should use TailwindCSS (recommended)
Resources
Available Components
Accordion
Alert
Alert Dialog
Aspect Ratio
Avatar
Badge
Breadcrumb
Button
Button Group
Calendar
Card
Carousel
Chart
Checkbox
Collapsible
Combobox
Command
Context Menu
Data Table
Date Picker
Dialog
Drawer
Dropdown Menu
Empty
Field
Form
Hover Card
Input
Input Group
Input OTP
Item
Kbd
Label
Menubar
Native Select
Navigation Menu
Pagination
Popover
Progress
Radio Group
Range Calendar
Resizable
Scroll Area
Select
Separator
Sheet
Sidebar
Skeleton
Slider
Sonner
Spinner
Switch
Table
Tabs
Textarea
Toggle
Toggle Group
Tooltip
Typography
Check Project Installation

You must check if shadcn-svelte is already installed in the project. To check, look for the components.json file in the project root directory.

# Check if components.json exists
ls -la components.json


If the file exists, shadcn-svelte is already configured in the project.

Installation
Prerequisites

Project requires SvelteKit ^2 and TailwindCSS ^4 ready before initializing shadcn-svelte.

Initialize shadcn-svelte
pnpm dlx shadcn-svelte@latest init


The @latest tag indicates installing the latest version. For adding components by command, you need to get the real version from package.json and use it in the command.

Configure components.json

You will be asked a few questions to configure components.json:

Which base color would you like to use? › Slate
Where is your global CSS file? (this file will be overwritten) › src/routes/layout.css
Configure the import alias for lib: › $lib
Configure the import alias for components: › $lib/components
Configure the import alias for utils: › $lib/utils
Configure the import alias for hooks: › $lib/hooks
Configure the import alias for ui: › $lib/components/ui
Setup Path Aliases (if needed)

If you are not using the default alias $lib, you'll need to update your svelte.config.js file to include those aliases:

const config = {
  // ... other config
  kit: {
    // ... other config
    alias: {
      "@/*": "./path/to/lib/*",
    },
  },
};

CLI Usage
Initialize Project
pnpm dlx shadcn-svelte@latest init


Options:

-c, --cwd <path>: the working directory (default: the current directory)
-o, --overwrite: overwrite existing files (default: false)
--no-deps: disable adding & installing dependencies
--skip-preflight: ignore preflight checks and continue (default: false)
--base-color <name>: the base color for the components (choices: "slate", "gray", "zinc", "neutral", "stone")
--css <path>: path to the global CSS file
--components-alias <path>: import alias for components
--lib-alias <path>: import alias for lib
--utils-alias <path>: import alias for utils
--hooks-alias <path>: import alias for hooks
--ui-alias <path>: import alias for ui
--proxy <proxy>: fetch items from registry using a proxy
Add Components
pnpm dlx shadcn-svelte@latest add [component]


Example:

pnpm dlx shadcn-svelte@latest add button


Options:

-c, --cwd <path>: the working directory (default: the current directory)
--no-deps: skips adding & installing package dependencies
--skip-preflight: ignore preflight checks and continue (default: false)
-a, --all: install all components to your project (default: false)
-y, --yes: skip confirmation prompt (default: false)
-o, --overwrite: overwrite existing files (default: false)
--proxy <proxy>: fetch components from registry using a proxy
Import and Use Components

After adding a component, you can import it like this:

<script lang="ts">
  import { Button } from "$lib/components/ui/button";
</script>

<Button>Click me</Button>


Import Guidelines:

Always use destructuring imports from the component's own folder: import { Button } from "$lib/components/ui/button"
Import sub-components together from their parent: import { Card, CardHeader, CardTitle } from "$lib/components/ui/card"
Never use namespace imports for simple components: import * as Button from "$lib/components/ui/button"
Use direct component paths without /index.js suffix
Theming
CSS Variables Convention

shadcn-svelte uses a simple background and foreground convention for colors. The background variable is used for the background color of the component and the foreground variable is used for the text color.

For example, given these CSS variables:

--primary: oklch(0.208 0.042 265.755);
--primary-foreground: oklch(0.984 0.003 247.858);


The background color will be var(--primary) and the foreground color will be var(--primary-foreground):

<div class="bg-primary text-primary-foreground">Hello</div>

Generated CSS Structure

The init command generates the full CSS structure in your global CSS file. The exact oklch values depend on the chosen base color (slate, gray, zinc, neutral, stone). The generated file includes:

TailwindCSS import and tw-animate-css animation library
Dark mode custom variant: @custom-variant dark (&:is(.dark *))
:root CSS variables for light mode colors
.dark CSS variables for dark mode colors
@theme inline block mapping CSS variables to TailwindCSS v4 utilities
@layer base block for default border and background styles
Available CSS Variables

The following variables are available (values shown are for the slate base color):

Variable	Purpose
--background / --foreground	Page background and text
--card / --card-foreground	Card component colors
--popover / --popover-foreground	Popover/dropdown colors
--primary / --primary-foreground	Primary action colors
--secondary / --secondary-foreground	Secondary action colors
--muted / --muted-foreground	Muted/subtle content
--accent / --accent-foreground	Accent/highlight colors
--destructive	Destructive action color
--border	Border color
--input	Input border color
--ring	Focus ring color
--chart-1 through --chart-5	Chart colors
--sidebar-*	Sidebar-specific variants
--radius	Base border radius
TailwindCSS v4 Theme Mapping

The init command also generates a @theme inline block required by TailwindCSS v4 to map CSS variables to Tailwind utility classes (e.g., bg-primary, text-foreground, border-border):

@theme inline {
  --radius-sm: calc(var(--radius) - 4px);
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 4px);
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  /* ... maps all CSS variables to Tailwind color utilities */
}

@layer base {
  * {
    @apply border-border outline-ring/50;
  }
  body {
    @apply bg-background text-foreground;
  }
}

Dark Mode
Install mode-watcher
pnpm i mode-watcher

Add the ModeWatcher Component

Import the ModeWatcher component and use it in your root layout:

<script lang="ts">
  import { ModeWatcher } from "mode-watcher";
  let { children } = $props();
</script>

<ModeWatcher />
{@render children?.()}

Add a Mode Toggle
Simple Toggle Button
<script lang="ts">
  import SunIcon from "@lucide/svelte/icons/sun";
  import MoonIcon from "@lucide/svelte/icons/moon";
  import { toggleMode } from "mode-watcher";
  import { Button } from "$lib/components/ui/button";
</script>

<Button onclick={toggleMode} variant="outline" size="icon">
  <SunIcon class="h-[1.2rem] w-[1.2rem] scale-100 rotate-0 !transition-all dark:scale-0 dark:-rotate-90" />
  <MoonIcon class="absolute h-[1.2rem] w-[1.2rem] scale-0 rotate-90 !transition-all dark:scale-100 dark:rotate-0" />
  <span class="sr-only">Toggle theme</span>
</Button>

Dropdown Menu Toggle
<script lang="ts">
  import SunIcon from "@lucide/svelte/icons/sun";
  import MoonIcon from "@lucide/svelte/icons/moon";
  import { resetMode, setMode } from "mode-watcher";
  import { 
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger
  } from "$lib/components/ui/dropdown-menu";
  import { buttonVariants } from "$lib/components/ui/button";
</script>

<DropdownMenu>
  <DropdownMenuTrigger class={buttonVariants({ variant: "outline", size: "icon" })}>
    <SunIcon class="h-[1.2rem] w-[1.2rem] scale-100 rotate-0 !transition-all dark:scale-0 dark:-rotate-90" />
    <MoonIcon class="absolute h-[1.2rem] w-[1.2rem] scale-0 rotate-90 !transition-all dark:scale-100 dark:rotate-0" />
    <span class="sr-only">Toggle theme</span>
  </DropdownMenuTrigger>
  <DropdownMenuContent align="end">
    <DropdownMenuItem onclick={() => setMode("light")}>Light</DropdownMenuItem>
    <DropdownMenuItem onclick={() => setMode("dark")}>Dark</DropdownMenuItem>
    <DropdownMenuItem onclick={() => resetMode()}>System</DropdownMenuItem>
  </DropdownMenuContent>
</DropdownMenu>

Rules

This skill includes the following rules:

[Component Maintenance]
Rule: component-maintenance
Description: Guidelines for maintaining shadcn components to ensure future update compatibility
[Component Usage Best Practices]
Rule: component-usage
Description: Best practices for using shadcn components effectively with their options
[Component Imports]
Rule: component-imports
Description: Best practices for importing shadcn-svelte components using folder paths for maximum compatibility
[CLI Usage]
Rule: cli-usage
Description: Always use CLI commands for installation, initialization, and adding components - never manually create config files
Weekly Installs
32
Repository
tapforce/agents-skills
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass