---
title: astro-i18n
url: https://skills.sh/soborbo/claudeskills/astro-i18n
---

# astro-i18n

skills/soborbo/claudeskills/astro-i18n
astro-i18n
Installation
$ npx skills add https://github.com/soborbo/claudeskills --skill astro-i18n
SKILL.md
Astro i18n Skill
Purpose

Provides internationalization patterns for lead generation sites targeting multiple markets/languages. Implements URL-based routing (/en/, /de/, /fr/), translation management, SEO optimization with hreflang tags, and RTL support.

Core Rules
URL structure first — /en/, /de/, /fr/ prefixes for SEO and user clarity
Fallback gracefully — Missing translations default to primary language with console warning
hreflang tags — Required on every page for proper language alternates
RTL support — Use logical CSS properties (margin-inline-start) for Arabic/Hebrew
Persist preference — Store user's language choice in localStorage/cookie
Type-safe translations — Use TypeScript for language codes and translation keys
No hardcoded text — All user-facing strings must come from translation files
SEO metadata — Translate title, description, og:locale for each language
Content parity — Each language should have equivalent content structure
Intl API formatting — Use native Intl for dates, numbers, currency per locale
Implementation Overview
Component	Purpose	Location
languages config	Define supported locales + metadata	src/i18n/config.ts
Translation files	JSON with nested keys	src/i18n/translations/{lang}.json
t() function	Translation with fallback + params	src/i18n/utils.ts
[lang]/ routes	Dynamic URL segments	src/pages/[lang]/
Language switcher	Dropdown component	Component in layout
hreflang tags	SEO language alternates	<head> in BaseLayout
Middleware	Optional browser detection	src/middleware.ts
Quick Start
Minimal Config
// src/i18n/config.ts
export const languages = {
  en: { name: 'English', code: 'en-GB', dir: 'ltr' },
  de: { name: 'Deutsch', code: 'de-DE', dir: 'ltr' },
} as const;
export const defaultLang = 'en';
export type Lang = keyof typeof languages;

Translation Usage
---
import { t } from '@/i18n/utils';
const lang = getLangFromUrl(Astro.url);
---
<h1>{t(lang, 'hero.title')}</h1>
<p>{t(lang, 'hero.subtitle')}</p>
<button>{t(lang, 'hero.cta')}</button>

Dynamic Route
---
// src/pages/[lang]/index.astro
export function getStaticPaths() {
  return Object.keys(languages).map(lang => ({ params: { lang } }));
}
---

References

Configuration & Setup:

config.md - Language config, translation files, utilities

Routing & URLs:

routing.md - Dynamic routes, redirects, middleware

Components:

components.md - Base layout, language switcher

Content & Collections:

content-collections.md - Multi-language blog posts

Formatting:

formatters.md - Numbers, dates, currency per locale

RTL Support:

rtl-support.md - Arabic/Hebrew layout support

SEO:

seo.md - hreflang, Open Graph, sitemaps
Forbidden
❌ Hardcoded text in components (use t() function)
❌ Missing hreflang tags on pages
❌ Auto-translating without human review
❌ Different URLs for same content without hreflang links
❌ Ignoring RTL requirements for Arabic/Hebrew
❌ Locale in query params (?lang=de) instead of path (/de/)
❌ Using left/right CSS instead of logical properties
❌ Forgetting to translate meta descriptions and titles
Definition of Done
 Language config with all supported locales defined
 Translation JSON files for each language with complete key coverage
 t() utility function with fallback to default language
 URL-based language routing using [lang]/ dynamic segments
 hreflang tags on all pages pointing to language alternates
 Language switcher component in navigation
 Root / redirects to default language
 Browser language detection (optional, via middleware)
 RTL support implemented if targeting Arabic/Hebrew
 Date/number/currency formatting per locale using Intl API
 Content collections with language-specific entries
 All user-facing text extracted to translation files
 SEO meta tags translated (title, description, og:locale)
Weekly Installs
11
Repository
soborbo/claudeskills
GitHub Stars
2
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass