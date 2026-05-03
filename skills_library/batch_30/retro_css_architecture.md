---
title: retro-css-architecture
url: https://skills.sh/theorcdev/8bitcn-ui/retro-css-architecture
---

# retro-css-architecture

skills/theorcdev/8bitcn-ui/retro-css-architecture
retro-css-architecture
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill retro-css-architecture
SKILL.md
Retro CSS Architecture

Organize CSS for 8-bit components using custom properties, pixel fonts, and responsive patterns.

Required Import

All 8-bit components must import the retro stylesheet:

import "@/components/ui/8bit/styles/retro.css";

Pixel Font

Use "Press Start 2P" for authentic 8-bit typography:

.retro {
  font-family: "Press Start 2P", system-ui, -apple-system, sans-serif;
  line-height: 1.5;
  letter-spacing: 0.5px;
}


Apply via class or font variant:

<Button className="retro">START GAME</Button>

// or via font prop
<Button font="retro">START GAME</Button>

Pixelated Images

For sharp pixel art images:

.pixelated {
  image-rendering: pixelated;
  image-rendering: crisp-edges;
}

<Image src="/pixel-art.png" className="pixelated" />

Dark Mode Colors

Use semantic color names with dark mode variants:

<div className="border-foreground dark:border-ring" />
<div className="bg-foreground dark:bg-ring" />

Responsive Pixel Sizes

Use consistent pixel values for retro feel:

{/* Standard pixel sizes */}
<div className="size-1.5" />      {/* Corner pixels */}
<div className="h-1.5 w-3" />     {/* Shadow segments */}
<div className="border-y-6" />     {/* Card borders */}

{/* Mobile considerations */}
<div className="h-[5px] md:h-1.5" />

CSS Organization

Keep retro-specific styles in components/ui/8bit/styles/retro.css:

/* Import pixel font */
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");

/* Font class */
.retro {
  font-family: "Press Start 2P", system-ui, -apple-system, sans-serif;
  line-height: 1.5;
  letter-spacing: 0.5px;
}

/* Image handling */
.pixelated {
  image-rendering: pixelated;
  image-rendering: crisp-edges;
}

Component-Level CSS

Use Tailwind utilities for component-specific styling:

<div
  className={cn(
    "relative border-y-6 border-foreground dark:border-ring",
    "rounded-none active:translate-y-1 transition-transform",
    className
  )}
/>

Key Principles
Import retro.css - Required for all 8-bit components
Pixel font - Use "Press Start 2P" for authentic look
Pixelated images - Apply image-rendering: pixelated to sprites
Consistent sizing - Use fixed pixel values (1.5, 3, 6px)
Dark mode - Use semantic colors with dark: prefix
rounded-none - Remove all border radius for retro feel
Tailwind first - Use utilities before custom CSS
Reference Files
components/ui/8bit/styles/retro.css - Global retro styles
components/ui/8bit/button.tsx - CSS class usage example
Weekly Installs
48
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