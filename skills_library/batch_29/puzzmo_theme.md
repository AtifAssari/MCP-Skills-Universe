---
title: puzzmo-theme
url: https://skills.sh/puzzmo-com/oss/puzzmo-theme
---

# puzzmo-theme

skills/puzzmo-com/oss/puzzmo-theme
puzzmo-theme
Installation
$ npx skills add https://github.com/puzzmo-com/oss --skill puzzmo-theme
SKILL.md
Puzzmo Theme

Convert the game's colors to use Puzzmo theme tokens, enabling automatic light/dark mode.

Steps

Review the theme object received from sdk.gameReady(). Key color tokens:

theme.g_bg - Game background
theme.g_bgAlt - Alternate background (checkerboard patterns)
theme.fg - Foreground text
theme.g_textDark - Dark text (on light backgrounds)
theme.g_textLight - Light text (on dark backgrounds)
theme.key - Primary accent (pink/brand)
theme.player - Player color (blue)
theme.alt1, alt2, alt3 - Additional accent colors
theme.g_key - A variant of key that always has good contrast for dark text
theme.error - Error/wrong state color
theme.g_unsolved - Unsolved/empty tile color
theme.alwaysDark / theme.alwaysLight - Colors that don't change with theme

Create a applyTheme(theme) function that maps theme tokens to CSS custom properties:

function applyTheme(theme: Theme) {
  const root = document.documentElement
  root.style.setProperty("--game-bg", theme.g_bg)
  root.style.setProperty("--game-fg", theme.fg)
  root.style.setProperty("--game-accent", theme.key)
  root.style.setProperty("--game-player", theme.player)
  // ... map all colors the game uses
}


Replace all hardcoded color values in CSS with var(--game-*) custom properties.

Wire up theme updates for live changes:

sdk.on("settingsUpdate", (settings) => {
  if (settings.theme) applyTheme(settings.theme)
})


The game's fonts should use Puzzmo's available fonts where appropriate:

Poppins - UI text (various weights)
Zodiak - Display/heading text
Red Hat Mono - Monospace
Success Criteria
npm run build completes without errors
No hardcoded color values remain in CSS (except for shadows, gradients with opacity, etc.)
Game renders correctly with both light and dark themes
Theme changes are applied without page reload
Weekly Installs
10
Repository
puzzmo-com/oss
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass