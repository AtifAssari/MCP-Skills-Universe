---
rating: ⭐⭐
title: stylex-styling
url: https://skills.sh/qingqishi/shiqingqi.com/stylex-styling
---

# stylex-styling

skills/qingqishi/shiqingqi.com/stylex-styling
stylex-styling
Installation
$ npx skills add https://github.com/qingqishi/shiqingqi.com --skill stylex-styling
SKILL.md
StyleX Styling
Overview

This project uses StyleX for styling with design tokens, responsive breakpoints, and theme-aware colors.

Key Patterns
Design Tokens
Import tokens from: @/tokens.stylex.ts
Available token categories:
color - Theme-aware colors (textMain, backgroundRaised, controlActive, etc.)
controlSize - Spacing and sizing values (_1 through _9)
font - Typography values (weight_5, etc.)
Breakpoints
Import from: @/breakpoints
Defined via: Babel plugin in .babelrc.js with typing in src/babel.d.ts
Usage: { default: value, [breakpoints.md]: largeScreenValue }
Custom CSS Prop
Use css={styles.someStyle} prop instead of {...stylex.props(styles.someStyle)}
Transpiled by custom Babel plugin
Supports arrays: css={[styles.base, isActive && styles.active]}
Complete Example
import * as stylex from "@stylexjs/stylex";
import { breakpoints } from "@/breakpoints";
import { color, controlSize, font } from "@/tokens.stylex";

function Button({ children, isActive, hideLabelOnMobile, ...props }) {
  return (
    <button
      {...props}
      css={[
        styles.button,
        isActive && styles.active,
        hideLabelOnMobile && styles.hideLabelOnMobile,
      ]}
    >
      {children}
    </button>
  );
}

const styles = stylex.create({
  button: {
    // Use design tokens
    fontSize: controlSize._4,
    fontWeight: font.weight_5,
    minHeight: controlSize._9,
    paddingBlock: controlSize._1,
    paddingInline: controlSize._3,

    // Responsive design with breakpoints
    display: { default: "none", [breakpoints.md]: "inline-flex" },

    // Theme-aware colors
    color: color.textMain,
    backgroundColor: {
      default: color.backgroundRaised,
      ":hover": color.backgroundHover,
    },
  },
  active: {
    backgroundColor: color.controlActive,
    color: color.textOnActive,
  },
  hideLabelOnMobile: {
    paddingLeft: {
      default: controlSize._3,
      [breakpoints.md]: controlSize._2,
    },
  },
});

Best Practices
Always use design tokens - Never hardcode colors, spacing, or font values
Use the css prop - Don't use {...stylex.props()} directly
Conditional styles with arrays - css={[base, condition && conditional]}
Responsive by default - Consider mobile-first with breakpoint overrides
Theme-aware colors - Use color tokens that adapt to light/dark themes
Pseudo-selectors in objects - { default: value, ":hover": hoverValue }
Common Patterns
Responsive Display
display: { default: "none", [breakpoints.md]: "flex" }

Conditional Styles
css={[styles.base, isActive && styles.active, hasError && styles.error]}

Hover States
backgroundColor: {
  default: color.backgroundRaised,
  ":hover": color.backgroundHover,
}

Mobile-First Padding
padding: {
  default: controlSize._2,
  [breakpoints.md]: controlSize._4,
  [breakpoints.lg]: controlSize._6,
}

Weekly Installs
11
Repository
qingqishi/shiqingqi.com
GitHub Stars
4
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass