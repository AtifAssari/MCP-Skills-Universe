---
title: mantine-dev
url: https://skills.sh/itechmeat/llm-code/mantine-dev
---

# mantine-dev

skills/itechmeat/llm-code/mantine-dev
mantine-dev
Installation
$ npx skills add https://github.com/itechmeat/llm-code --skill mantine-dev
SKILL.md
Mantine UI Library

Mantine is a fully-featured React components library with TypeScript support. It provides 100+ hooks and components with native dark mode, CSS-in-JS via CSS modules, and excellent accessibility.

v9.0 Breaking Changes
React 19.2+ required for all @mantine/* packages
Tiptap 3+ required for @mantine/tiptap
Recharts 3+ required for @mantine/charts (no migration needed)
Follow the official 8.x → 9.x migration guide for full details
Focus

This skill focuses on:

Vite + TypeScript setup (not Next.js or CRA)
CSS modules with PostCSS preset
Vitest for testing
ESLint with eslint-config-mantine
Installation

See references/getting-started.md for Vite template setup, manual installation, and optional packages.

PostCSS Configuration

Create postcss.config.cjs:

module.exports = {
  plugins: {
    "postcss-preset-mantine": {},
    "postcss-simple-vars": {
      variables: {
        "mantine-breakpoint-xs": "36em",
        "mantine-breakpoint-sm": "48em",
        "mantine-breakpoint-md": "62em",
        "mantine-breakpoint-lg": "75em",
        "mantine-breakpoint-xl": "88em",
      },
    },
  },
};

App Setup
// src/App.tsx
import "@mantine/core/styles.css";
// Other style imports as needed:
// import '@mantine/dates/styles.css';
// import '@mantine/notifications/styles.css';

import { MantineProvider, createTheme } from "@mantine/core";

const theme = createTheme({
  // Theme customization here
});

function App() {
  return <MantineProvider theme={theme}>{/* Your app */}</MantineProvider>;
}

Critical Prohibitions
Do NOT skip MantineProvider wrapper — all components require it
Do NOT forget to import @mantine/core/styles.css — components won't style without it
Do NOT mix Mantine with other UI libraries (e.g., Chakra, MUI) in same project
Do NOT use inline styles for theme values — use CSS variables or theme object
Do NOT skip PostCSS setup — responsive mixins won't work
Do NOT forget key={form.key('path')} when using uncontrolled forms
Core Concepts
1. MantineProvider

Wraps your app, provides theme context and color scheme management.

2. Theme Object

Customize colors, typography, spacing, component default props.

3. Style Props

All components accept style props like mt, p, c, bg, etc.

4. CSS Variables

All theme values exposed as CSS variables (e.g., --mantine-color-blue-6).

5. Polymorphic Components

Many components support component prop to render as different elements.

Definition of Done
 MantineProvider wraps the app
 Styles imported (@mantine/core/styles.css)
 PostCSS configured with mantine-preset
 Theme customization in createTheme
 Color scheme (light/dark) handled
 TypeScript types working
 Tests pass with Vitest + custom render
References (Detailed Guides)
Setup & Configuration
getting-started.md — Installation, Vite setup, project structure
styling.md — MantineProvider, theme, CSS modules, style props, dark mode
Core Features
components.md — Core UI components patterns
hooks.md — @mantine/hooks utility hooks
forms.md — @mantine/form, useForm, validation
schedule.md — @mantine/schedule calendar scheduling
Development
testing.md — Vitest setup, custom render, mocking
eslint.md — eslint-config-mantine setup
Links
Documentation
Releases
GitHub
npm
Vite template
LLM docs
Weekly Installs
179
Repository
itechmeat/llm-code
GitHub Stars
15
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass