---
rating: ⭐⭐
title: next-intl-add-language
url: https://skills.sh/github/awesome-copilot/next-intl-add-language
---

# next-intl-add-language

skills/github/awesome-copilot/next-intl-add-language
next-intl-add-language
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill next-intl-add-language
Summary

Add a new language to a Next.js application using next-intl internationalization.

Requires translating all entries from en.json in the ./messages directory to the new language
Update routing configuration in src/i18n/routing.ts and middleware in src/middleware.ts to recognize the new language
Register the language in the language toggle component at src/components/language-toggle.tsx
SKILL.md

This is a guide to add a new language to a Next.js project using next-intl for internationalization,

For i18n, the application uses next-intl.
All translations are in the directory ./messages.
The UI component is src/components/language-toggle.tsx.
Routing and middleware configuration are handled in:
src/i18n/routing.ts
src/middleware.ts

When adding a new language:

Translate all the content of en.json to the new language. The goal is to have all the JSON entries in the new language for a complete translation.
Add the path in routing.ts and middleware.ts.
Add the language to language-toggle.tsx.
Weekly Installs
8.6K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass