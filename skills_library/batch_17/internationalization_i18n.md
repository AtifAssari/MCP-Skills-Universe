---
title: internationalization-i18n
url: https://skills.sh/secondsky/claude-skills/internationalization-i18n
---

# internationalization-i18n

skills/secondsky/claude-skills/internationalization-i18n
internationalization-i18n
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill internationalization-i18n
SKILL.md
Internationalization (i18n)

Implement multi-language support with proper translation management and formatting.

i18next Setup (React)
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    fallbackLng: 'en',
    interpolation: { escapeValue: false },
    resources: {
      en: { translation: { welcome: 'Welcome, {{name}}!' } },
      es: { translation: { welcome: '¡Bienvenido, {{name}}!' } }
    }
  });

// Usage
const { t } = useTranslation();
<h1>{t('welcome', { name: 'John' })}</h1>

Pluralization
// Translation file
{
  "items": "{{count}} item",
  "items_plural": "{{count}} items",
  "items_zero": "No items"
}

// Usage
t('items', { count: 0 })  // "No items"
t('items', { count: 1 })  // "1 item"
t('items', { count: 5 })  // "5 items"

Date/Number Formatting
// Dates
new Intl.DateTimeFormat('de-DE', {
  dateStyle: 'long',
  timeStyle: 'short'
}).format(new Date());

// Numbers
new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD'
}).format(1234.56);  // "$1,234.56"

// Relative time
new Intl.RelativeTimeFormat('en', { numeric: 'auto' })
  .format(-1, 'day');  // "yesterday"

RTL Support
/* Use logical properties */
.container {
  margin-inline-start: 1rem;  /* margin-left in LTR, margin-right in RTL */
  padding-inline-end: 1rem;
}

/* Direction attribute */
html[dir="rtl"] .icon {
  transform: scaleX(-1);
}

Additional Frameworks

See references/frameworks.md for:

React-Intl (Format.js) complete implementation
Python gettext with Flask/Babel
RTL language support patterns
ICU Message Format examples
Best Practices
Extract all user-facing strings
Use ICU message format for complex translations
Test with pseudo-localization
Support RTL from the start
Never concatenate translated strings
Use professional translators for production
Weekly Installs
174
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass