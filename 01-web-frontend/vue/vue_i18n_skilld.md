---
rating: ⭐⭐
title: vue-i18n-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/vue-i18n-skilld
---

# vue-i18n-skilld

skills/harlan-zw/vue-ecosystem-skills/vue-i18n-skilld
vue-i18n-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill vue-i18n-skilld
SKILL.md
intlify/vue-i18n vue-i18n@11.4.0

Tags: rc: 9.0.0-rc.9, alpha: 9.2.0-alpha.9, legacy: 8.28.2

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

DEPRECATED: Legacy API mode — deprecated in v11 for Composition API preference; scheduled for removal in v12 source

DEPRECATED: Custom Directive v-t — deprecated in v11 due to limited optimization benefits in Vue 3; scheduled for removal in v12 source

BREAKING: tc and $tc — dropped in v11 for Legacy API mode; use pluralization support in t and $t instead source

NEW: Vue 3 Vapor Mode — added compatibility for Vue 3 vapor mode in v11.2.0 source

BREAKING: JIT Compilation — enabled by default in v10 to solve CSP issues and support dynamic resources source

BREAKING: $t and t Signatures — Legacy API mode signatures changed in v10 to match Composition API mode; positional locale args now require options object source

NEW: Generated Locale Types — v10 adds support for extending locale types via GeneratedTypeConfig for better TypeScript inference source

BREAKING: Modulo % Syntax — named interpolation using modulo syntax dropped in v10; use standard {} interpolation source

BREAKING: vue-i18n-bridge — dropped in v10 following Vue 2 EOL source

BREAKING: allowComposition Option — dropped in v10; was previously used for Legacy to Composition API migration on v9 source

Also changed: petite-vue-i18n GA v10 · Configurable $i18n type new v11.1.0 · mode property deprecated v11 · tm accepts DefineLocaleMessage key type v11.0.0 · Part options support $n & $d new v11.1.4

Best Practices

Prefer Composition API mode (legacy: false) for all new projects — Legacy API mode is deprecated in v11 and will be removed in v12 source

Use t() function or <i18n-t> component over the v-t directive — the directive is deprecated in v11 and lacks IDE support for key completion source

Define global resource schemas using DefineLocaleMessage, DefineDateTimeFormat, and DefineNumberFormat interfaces — enables automatic type inference and key completion in useI18n without passing type parameters source

Use rt() (Resolve Translation) when processing locale messages retrieved via tm() — ensures proper resolution of nested structures and pluralization for programmatically accessed messages

Enable escapeParameter: true when using v-html with translations containing user input — prevents XSS by escaping interpolation parameters and neutralizing dangerous HTML attributes

Explicitly configure __VUE_I18N_FULL_INSTALL__ and __VUE_I18N_LEGACY_API__ feature flags — setting these to false in bundler configuration enables better tree-shaking and reduces bundle size source

Pre-compile locale messages using @intlify/unplugin-vue-i18n — improves performance by using AST/Functions and ensures CSP compliance by avoiding eval during runtime compilation source

Implement lazy loading for locale messages using dynamic import() and setLocaleMessage() — reduces initial bundle size by loading language resources only when needed (e.g., in router guards) source

Synchronize the html lang attribute and Accept-Language headers when switching locales — ensures accessibility (screen readers) and consistent language handling for server-side requests source

Weekly Installs
147
Repository
harlan-zw/vue-e…m-skills
GitHub Stars
158
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass