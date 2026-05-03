---
rating: ⭐⭐⭐
title: tailwindcss-debugging
url: https://skills.sh/josiahsiegel/claude-plugin-marketplace/tailwindcss-debugging
---

# tailwindcss-debugging

skills/josiahsiegel/claude-plugin-marketplace/tailwindcss-debugging
tailwindcss-debugging
Installation
$ npx skills add https://github.com/josiahsiegel/claude-plugin-marketplace --skill tailwindcss-debugging
SKILL.md
Tailwind CSS Debugging & Troubleshooting
Common Issues & Solutions
1. Styles Not Applying
Check Content Detection

v4 automatically detects content, but if styles are missing:

/* Explicitly specify sources */
@import "tailwindcss";
@source "./src/**/*.{html,js,jsx,ts,tsx,vue,svelte}";

Verify Class Names
<!-- WRONG - Dynamic class won't be detected -->
<div class={`text-${color}-500`}>

<!-- CORRECT - Use complete class names -->
<div class={color === 'blue' ? 'text-blue-500' : 'text-red-500'}>

Check Build Process
# Restart dev server
npm run dev

# Clear cache and rebuild
rm -rf node_modules/.vite
npm run build

2. v4 Migration Issues
PostCSS Plugin Changed
// OLD (v3)
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {}
  }
}

// NEW (v4)
export default {
  plugins: {
    '@tailwindcss/postcss': {}
  }
}

Configuration Moved to CSS
/* v4 - Configure in CSS, not JS */
@import "tailwindcss";

@theme {
  --color-primary: oklch(0.6 0.2 250);
}

Dark Mode Variant
/* v4 - Add if using selector strategy */
@custom-variant dark (&:where(.dark, .dark *));

3. Classes Being Overridden
Check Specificity
/* Browser DevTools: Inspect element → Styles panel */
/* Look for crossed-out styles */

Solutions
<!-- Use !important (last resort) -->
<div class="!mt-0">

<!-- Or increase specificity with variants -->
<div class="[&]:mt-0">

Check Import Order
/* Your custom CSS should come after Tailwind */
@import "tailwindcss";
@import "./custom.css";  /* After Tailwind */

4. Typography Plugin Issues
Styles Not Applied
/* Ensure plugin is loaded */
@plugin "@tailwindcss/typography";

Utilities Overridden by Prose
<!-- Use element modifiers -->
<article class="prose prose-h1:text-4xl prose-a:text-blue-600">

<!-- Or escape prose entirely -->
<article class="prose">
  <div class="not-prose">
    <CustomComponent />
  </div>
</article>

5. Forms Plugin Issues
Styles Not Applied to Plain Inputs
<!-- Forms plugin only styles inputs with type attribute -->
<input type="text" />  <!-- ✓ Styled -->
<input />              <!-- ✗ Not styled -->

Using Class Strategy
@plugin "@tailwindcss/forms" {
  strategy: class;
}

<!-- Now explicitly opt-in -->
<input type="text" class="form-input" />

Debugging Tools
VS Code Extension
# Install Tailwind CSS IntelliSense
code --install-extension bradlc.vscode-tailwindcss


Features:

Autocomplete for class names
Hover previews showing CSS
Linting for errors
Color decorators
Debug Screens Plugin
npm install -D @tailwindcss/debug-screens

@plugin "@tailwindcss/debug-screens";

<!-- Shows current breakpoint in corner -->
<body class="debug-screens">

Browser DevTools
Inspect Element → See computed styles
Styles Panel → See which rules apply
Filter → Search for Tailwind classes
Computed Tab → See final computed values
Check Generated CSS
# Output CSS to file for inspection
npx tailwindcss -o output.css --content './src/**/*.{html,js}'

# With verbose logging
DEBUG=tailwindcss:* npm run build

v4 Specific Debugging
Check Plugin Loading
# Look for plugin-related errors
npm run build 2>&1 | grep -i plugin

Verify CSS Variable Output
/* In browser DevTools, check :root for variables */
:root {
  --color-blue-500: oklch(...);
  --spacing-4: 1rem;
}

Content Detection Issues
/* Add explicit sources if auto-detection fails */
@source "./src/**/*.tsx";
@source "./components/**/*.tsx";

/* Exclude paths */
@source not "./src/generated/**";

Common Error Messages
"Cannot find module '@tailwindcss/postcss'"
npm install -D @tailwindcss/postcss

"Unknown at-rule @theme"

Using v3 tooling with v4 syntax. Update your build setup:

npm install -D tailwindcss@latest @tailwindcss/postcss@latest

"Class 'X' doesn't exist"

Dynamic class generation issue:

// BAD
const classes = `bg-${dynamic}-500`

// GOOD
const colorMap = {
  primary: 'bg-blue-500',
  danger: 'bg-red-500'
}
const classes = colorMap[dynamic]

"Styles not updating in development"
# Restart dev server
npm run dev

# Clear Vite cache
rm -rf node_modules/.vite

# Clear Next.js cache
rm -rf .next

Performance Debugging
Large CSS Output
# Check CSS file size
ls -lh dist/assets/*.css

# If too large, check for:
# 1. Dynamic class generation
# 2. Unnecessary safelisting
# 3. Unused plugins

Slow Builds
# Time the build
time npm run build

# v4 should be very fast
# Full build: <1s
# Incremental: microseconds

Debugging Checklist
Initial Setup
 Correct import: @import "tailwindcss";
 PostCSS plugin: @tailwindcss/postcss (not tailwindcss)
 Vite plugin: @tailwindcss/vite (if using Vite)
 CSS file imported in entry point
 Development server restarted after changes
Styles Not Applying
 Class name is complete (no dynamic generation)
 File is in content path
 Browser cache cleared
 No CSS specificity conflicts
 Check DevTools for overridden styles
After Migration
 tailwind.config.js removed or converted
 @theme directive used for customization
 PostCSS config updated
 Dark mode variant added if using selector strategy
 Plugins updated to v4-compatible versions
Production Issues
 NODE_ENV=production
 Build output includes styles
 CSS file linked correctly
 No dynamic class generation issues
Getting Help
Create Minimal Reproduction
# Create fresh project
npm create vite@latest repro -- --template react-ts
cd repro
npm install -D tailwindcss @tailwindcss/vite

# Add minimal code that shows the issue
# Share on GitHub Issues or Discord

Resources
Official Docs
GitHub Issues
Tailwind CSS Discord
Stack Overflow
Weekly Installs
112
Repository
josiahsiegel/cl…ketplace
GitHub Stars
33
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass