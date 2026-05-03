---
title: internationalization-i18n
url: https://skills.sh/aj-geddes/useful-ai-prompts/internationalization-i18n
---

# internationalization-i18n

skills/aj-geddes/useful-ai-prompts/internationalization-i18n
internationalization-i18n
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill internationalization-i18n
SKILL.md
Internationalization (i18n) & Localization
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Comprehensive guide to implementing internationalization and localization in applications. Covers message translation, pluralization, date/time/number formatting, RTL languages, and integration with popular i18n libraries.

When to Use
Building multi-language applications
Supporting international users
Implementing language switching
Formatting dates, times, and numbers for different locales
Supporting RTL (right-to-left) languages
Extracting and managing translation strings
Implementing pluralization rules
Setting up translation workflows
Quick Start

Minimal working example:

// i18n.ts
import i18next from "i18next";
import Backend from "i18next-http-backend";
import LanguageDetector from "i18next-browser-languagedetector";

await i18next
  .use(Backend)
  .use(LanguageDetector)
  .init({
    fallbackLng: "en",
    debug: process.env.NODE_ENV === "development",

    interpolation: {
      escapeValue: false, // React already escapes
    },

    backend: {
      loadPath: "/locales/{{lng}}/{{ns}}.json",
    },

    detection: {
      order: ["querystring", "cookie", "localStorage", "navigator"],
      caches: ["localStorage", "cookie"],
    },
  });
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
i18next (JavaScript/TypeScript)	i18next (JavaScript/TypeScript)
React-Intl (Format.js)	React-Intl (Format.js)
Python i18n (gettext)	Python i18n (gettext)
Date and Time Formatting	Date and Time Formatting
Number and Currency Formatting	Number and Currency Formatting
Pluralization Rules	Pluralization Rules
RTL (Right-to-Left) Language Support	RTL (Right-to-Left) Language Support
Translation Management	Translation Management
Locale Detection	Locale Detection
Server-Side i18n	Server-Side i18n
Best Practices
✅ DO
Extract all user-facing strings to translation files
Use ICU message format for complex messages
Support pluralization correctly for each language
Use locale-aware date/time/number formatting
Implement RTL support for Arabic, Hebrew, etc.
Provide fallback language (usually English)
Use namespaces to organize translations
Test with pseudo-localization (ääçćëńţś)
Store locale preference (cookie, localStorage)
Use professional translators for production
Implement translation management workflow
Support dynamic locale switching
Use translation memory tools
❌ DON'T
Hardcode user-facing strings in code
Concatenate translated strings
Assume English grammar rules apply to all languages
Use generic plural forms (one/many) for all languages
Forget about text expansion (German is ~30% longer)
Store dates/times in locale-specific formats
Use flags to represent languages (flag ≠ language)
Translate technical terms without context
Mix translation keys with UI strings
Forget to translate alt text, titles, placeholders
Assume left-to-right layout
Weekly Installs
361
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass