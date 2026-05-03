---
rating: ⭐⭐
title: i18n-frontend-implementer
url: https://skills.sh/patricio0312rev/skills/i18n-frontend-implementer
---

# i18n-frontend-implementer

skills/patricio0312rev/skills/i18n-frontend-implementer
i18n-frontend-implementer
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill i18n-frontend-implementer
SKILL.md
i18n Frontend Implementer

Implement internationalization with next-intl, react-i18next, or similar libraries.

Core Setup

1. Install: npm install next-intl or react-i18next 2. Create dictionaries: locales/en.json, locales/es.json 3. Provider setup: Wrap app with IntlProvider 4. Translation keys: Hierarchical namespace structure 5. Formatters: Date, number, currency formatting 6. Language switcher: Dropdown or flags UI

Translation Structure
{
  "common": { "nav": { "home": "Home", "about": "About" } },
  "auth": { "login": "Sign In", "logout": "Sign Out" },
  "errors": { "required": "{field} is required" }
}

Usage Examples
const t = useTranslations('common');
<h1>{t('nav.home')}</h1>

// With plurals
t('items', { count: 5 }) // "5 items"

// With formatting
<p>{formatDate(date, { dateStyle: 'long' })}</p>

Best Practices

Use namespaces for organization, extract all text to translations, handle plurals properly, format dates/numbers per locale, provide language switcher, support RTL languages, lazy-load translations.

Weekly Installs
176
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass