---
title: tailwind-config
url: https://skills.sh/sgcarstrends/sgcarstrends/tailwind-config
---

# tailwind-config

skills/sgcarstrends/sgcarstrends/tailwind-config
tailwind-config
Installation
$ npx skills add https://github.com/sgcarstrends/sgcarstrends --skill tailwind-config
SKILL.md
Tailwind CSS Configuration Skill
Configuration Structure
packages/ui/
├── tailwind.config.ts       # Base config with shadcn/ui theming
└── src/styles/globals.css   # CSS variables

apps/web/
├── tailwind.config.ts       # Extends UI package config
└── src/app/globals.css      # App-specific styles

CSS Variables

Defined in packages/ui/src/styles/globals.css:

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96.1%;
    --muted: 210 40% 96.1%;
    --accent: 210 40% 96.1%;
    --destructive: 0 84.2% 60.2%;
    --border: 214.3 31.8% 91.4%;
    --radius: 0.5rem;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    /* ... dark mode values */
  }
}

Adding Custom Colors
// tailwind.config.ts
export default {
  theme: {
    extend: {
      colors: {
        brand: {
          primary: "#0070F3",
          secondary: "#7928CA",
        },
      },
    },
  },
};

Adding Animations
theme: {
  extend: {
    keyframes: {
      shimmer: {
        "0%": { backgroundPosition: "-200% 0" },
        "100%": { backgroundPosition: "200% 0" },
      },
    },
    animation: {
      shimmer: "shimmer 2s linear infinite",
    },
  },
}

Custom Utilities
/* globals.css */
@layer utilities {
  .text-balance {
    text-wrap: balance;
  }
  .scrollbar-hide {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
}

Plugins
plugins: [
  require("@tailwindcss/typography"),  // prose classes
  require("@tailwindcss/forms"),        // form resets
  require("tailwindcss-animate"),       // animations
]

Size Utility Convention

Use size-* instead of h-* w-* for equal dimensions:

// ✅ Good
<div className="size-4">Icon</div>
<div className="size-8">Avatar</div>

// ❌ Avoid
<div className="h-4 w-4">Icon</div>

Dark Mode

Tailwind v4 uses a CSS custom variant instead of config-based darkMode:

/* globals.css */
@custom-variant dark (&:is(.dark *));


This is already configured in both apps/web/src/app/globals.css and packages/ui/src/styles/globals.css. Dark CSS variables are fully defined in .dark blocks in both files.

Theme switching uses next-themes with attribute="class" to toggle .dark on <html>:

import { useTheme } from "next-themes";
const { resolvedTheme, setTheme } = useTheme();


Status: Dark mode activation is deferred until after HeroUI v3 migration (#714, blocked by #587). The CSS infrastructure is ready.

Debugging
# Check resolved config
npx tailwindcss config

# Watch for generated classes
TAILWIND_MODE=watch npx tailwindcss -i ./src/styles/globals.css -o ./dist/output.css --watch


Common issues:

Classes not applying → Check content paths
Dark mode not working → Verify darkMode: ["class"] and ThemeProvider
Classes purged → Add to safelist or use complete class names
Best Practices
Mobile-first - Default styles for mobile, add breakpoints up
CSS Variables - Use for theming (enables dark mode)
Content paths - Include all component paths
Semantic names - Use brand, accent not blue-500
Size utility - Use size-* for equal dimensions
References
Tailwind CSS: https://tailwindcss.com
Design tokens: See design-language-system skill
Weekly Installs
61
Repository
sgcarstrends/sg…rstrends
GitHub Stars
20
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass