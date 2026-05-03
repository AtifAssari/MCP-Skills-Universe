---
title: i18n-localization
url: https://skills.sh/sickn33/antigravity-awesome-skills/i18n-localization
---

# i18n-localization

skills/sickn33/antigravity-awesome-skills/i18n-localization
i18n-localization
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill i18n-localization
Summary

Internationalization and localization patterns for multi-language app support.

Covers core i18n concepts, implementation patterns for React, Next.js, and Python, and file structure organization for managing translations across locales
Includes best practices for using translation keys, namespacing, pluralization, date/number formatting, and ICU message format to avoid common pitfalls
Provides RTL (right-to-left) layout guidance using CSS logical properties for languages like Arabic and Hebrew
Includes a hardcoded string detection script to identify missing translations and ensure all user-facing text uses translation keys
SKILL.md
i18n & Localization

Internationalization (i18n) and Localization (L10n) best practices.

1. Core Concepts
Term	Meaning
i18n	Internationalization - making app translatable
L10n	Localization - actual translations
Locale	Language + Region (en-US, tr-TR)
RTL	Right-to-left languages (Arabic, Hebrew)
2. When to Use i18n
Project Type	i18n Needed?
Public web app	✅ Yes
SaaS product	✅ Yes
Internal tool	⚠️ Maybe
Single-region app	⚠️ Consider future
Personal project	❌ Optional
3. Implementation Patterns
React (react-i18next)
import { useTranslation } from 'react-i18next';

function Welcome() {
  const { t } = useTranslation();
  return <h1>{t('welcome.title')}</h1>;
}

Next.js (next-intl)
import { useTranslations } from 'next-intl';

export default function Page() {
  const t = useTranslations('Home');
  return <h1>{t('title')}</h1>;
}

Python (gettext)
from gettext import gettext as _

print(_("Welcome to our app"))

4. File Structure
locales/
├── en/
│   ├── common.json
│   ├── auth.json
│   └── errors.json
├── tr/
│   ├── common.json
│   ├── auth.json
│   └── errors.json
└── ar/          # RTL
    └── ...

5. Best Practices
DO ✅
Use translation keys, not raw text
Namespace translations by feature
Support pluralization
Handle date/number formats per locale
Plan for RTL from the start
Use ICU message format for complex strings
DON'T ❌
Hardcode strings in components
Concatenate translated strings
Assume text length (German is 30% longer)
Forget about RTL layout
Mix languages in same file
6. Common Issues
Issue	Solution
Missing translation	Fallback to default language
Hardcoded strings	Use linter/checker script
Date format	Use Intl.DateTimeFormat
Number format	Use Intl.NumberFormat
Pluralization	Use ICU message format
7. RTL Support
/* CSS Logical Properties */
.container {
  margin-inline-start: 1rem;  /* Not margin-left */
  padding-inline-end: 1rem;   /* Not padding-right */
}

[dir="rtl"] .icon {
  transform: scaleX(-1);
}

8. Checklist

Before shipping:

 All user-facing strings use translation keys
 Locale files exist for all supported languages
 Date/number formatting uses Intl API
 RTL layout tested (if applicable)
 Fallback language configured
 No hardcoded strings in components
Script
Script	Purpose	Command
scripts/i18n_checker.py	Detect hardcoded strings & missing translations	python scripts/i18n_checker.py <project_path>
When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
1.7K
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass