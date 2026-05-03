---
title: react-i18n
url: https://skills.sh/fusengine/agents/react-i18n
---

# react-i18n

skills/fusengine/agents/react-i18n
react-i18n
Installation
$ npx skills add https://github.com/fusengine/agents --skill react-i18n
SKILL.md
react-i18next for React 19
Agent Workflow (MANDATORY)

Before ANY implementation, use TeamCreate to spawn 3 agents:

fuse-ai-pilot:explore-codebase - Analyze existing i18n setup and translation patterns
fuse-ai-pilot:research-expert - Verify latest react-i18next/i18next docs via Context7/Exa
mcp__context7__query-docs - Check TypeScript Selector API and React 19 Suspense patterns

After implementation, run fuse-ai-pilot:sniper for validation.

MANDATORY: SOLID Principles

ALWAYS apply SOLID principles from solid-react skill.

→ See ../solid-react/SKILL.md for complete rules

Key Rules:

Files < 100 lines (split at 90)
Interfaces in modules/[feature]/src/interfaces/
JSDoc mandatory on all exports
No business logic in components
Core Hooks
Hook	Purpose	Guide
useTranslation()	Access translations and i18n instance	references/i18next-basics.md
useTranslation(ns)	Load specific namespace	references/namespaces.md
useTranslation([ns])	Load multiple namespaces	references/namespaces.md

→ See references/i18next-basics.md for detailed usage

Key Packages
Package	Purpose	Size
i18next	Core library	~40KB
react-i18next	React bindings	~12KB
i18next-http-backend	Lazy loading	~5KB
i18next-browser-languagedetector	Auto-detection	~8KB
Key Features
TypeScript Selector API (i18next ≥25.4)

Type-safe translations with autocompletion. → See references/typescript-types.md

Namespaces

Organize translations by feature for code splitting. → See references/namespaces.md

Pluralization

Count-based rules with ICU MessageFormat support. → See references/pluralization.md

Interpolation

Variables, dates, numbers, and currency formatting. → See references/interpolation.md

Lazy Loading

Load translations on-demand per route. → See references/lazy-loading.md

Language Detection

Auto-detect from browser, URL, cookie, localStorage. → See references/language-detection.md

React 19 Integration

Suspense, useTransition, Concurrent Rendering. → See references/react-19-integration.md

Trans Component

JSX elements inside translations. → See references/trans-component.md

Testing

Mock i18n for unit tests. → See references/testing.md

RTL Support

Right-to-left languages (Arabic, Hebrew). → See references/rtl-support.md

Fallback Strategies

Handle missing keys gracefully. → See references/fallback-strategies.md

Templates
Template	Use Case
templates/basic-setup.md	Configuration with React 19
templates/language-switcher.md	Dropdown component
templates/typed-translations.md	TypeScript Selector API
templates/form-validation-i18n.md	Translated form errors
templates/lazy-loading-routes.md	Per-route loading
templates/date-number-formatter.md	Intl formatting
templates/plural-interpolation.md	Count-based messages
templates/trans-component-examples.md	JSX in translations
templates/testing-i18n.md	Unit test setup
Modular Architecture (SOLID)
src/
├── modules/cores/i18n/
│   ├── src/
│   │   ├── interfaces/
│   │   │   └── i18n.interface.ts
│   │   ├── services/
│   │   │   └── i18n.service.ts
│   │   ├── hooks/
│   │   │   └── useLanguage.ts
│   │   └── config/
│   │       └── i18n.config.ts
│   ├── components/
│   │   └── LanguageSwitcher.tsx
│   └── locales/
│       ├── en/
│       │   └── translation.json
│       └── fr/
│           └── translation.json
└── main.tsx

Best Practices
Suspense: Wrap app with <Suspense> for loading states
Namespaces: One namespace per feature/module
TypeScript: Use Selector API for type-safe keys
Lazy Loading: Load namespaces on-demand
Detection: Configure language detection order
Fallback: Always set fallbackLng
Forbidden (Anti-Patterns)
❌ Hardcoded strings → use t('key')
❌ No Suspense → causes loading flicker
❌ All translations in one file → use namespaces
❌ No fallback language → broken UI
❌ String concatenation → use interpolation {{var}}
❌ Manual language state → use i18n.changeLanguage()
Weekly Installs
24
Repository
fusengine/agents
GitHub Stars
11
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass