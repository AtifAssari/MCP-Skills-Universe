---
title: vite-shadcn-tailwind4
url: https://skills.sh/igorwarzocha/opencode-workflows/vite-shadcn-tailwind4
---

# vite-shadcn-tailwind4

skills/igorwarzocha/opencode-workflows/vite-shadcn-tailwind4
vite-shadcn-tailwind4
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill vite-shadcn-tailwind4
SKILL.md

For Next.js, Remix, or other frameworks, You MUST use their respective shadcn installation guides.

<question_tool>

Batching Rule: You MUST use only for 2+ related questions; single questions use plain text.
Syntax Constraints: header max 12 chars, labels 1-5 words, mark defaults with (Recommended).
Purpose: Clarify component selection, style preferences, and optional AI elements before running shadcn CLI. </question_tool>

If prerequisites are missing, You MUST help the user set up Tailwind v4 first.

Action: You MUST update tsconfig.json to include compilerOptions:

{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ],
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}

import tailwindcss from "@tailwindcss/vite";
import path from "path";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
});


You SHOULD recommend these settings:

Style: New York
Base Color: Neutral or Zinc
CSS Variables: Yes

You MUST wait for user confirmation before continuing.

You SHOULD instruct them to select all components (a then Enter).

You MUST wait for user confirmation before continuing.

You SHOULD instruct them to answer NO to all overwrite prompts.

You MUST wait for user confirmation before continuing.

Required packages:

tw-animate-css (devDep) - v4 replacement for tailwindcss-animate
tailwind-merge (dep) - used by cn() utility
clsx (dep) - used by cn() utility
class-variance-authority (dep) - used by shadcn components

You MUST run if any are missing:

npm install tailwind-merge clsx class-variance-authority
npm install -D tw-animate-css

@import "tailwindcss";
@import "tw-animate-css";

@custom-variant dark (&:is(.dark *));

@theme inline {
  /* Variable mappings: --color-X: var(--X); */
}

:root {
  /* Token definitions using oklch() */
}

.dark {
  /* Dark mode tokens using oklch() */
}

@layer base {
  * {
    @apply border-border outline-ring/50;
  }
  body {
    @apply bg-background text-foreground;
  }
}


You MUST remove these if present:

@media (prefers-color-scheme) blocks
Duplicate @theme blocks (keep only @theme inline)
@config directives

You MUST fix any TypeScript errors before marking setup complete.

Weekly Installs
51
Repository
igorwarzocha/op…orkflows
GitHub Stars
111
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass