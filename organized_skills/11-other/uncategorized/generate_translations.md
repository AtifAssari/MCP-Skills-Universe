---
rating: ⭐⭐
title: generate-translations
url: https://skills.sh/payloadcms/payload/generate-translations
---

# generate-translations

skills/payloadcms/payload/generate-translations
generate-translations
Installation
$ npx skills add https://github.com/payloadcms/payload --skill generate-translations
SKILL.md
Translation Generation Guide

Payload has two separate translation systems:

Core Translations - for core Payload packages (packages/ui, packages/payload, packages/next)
Plugin Translations - for plugins (packages/plugin-*)
Table of Contents
1. Core Translations
2. Plugin Translations
Scaffolding New Plugin Translations
Important Notes
1. Core Translations

When to use: Adding translations to core Payload packages (packages/ui, packages/payload, packages/next)

Steps:

Add the English translation to packages/translations/src/languages/en.ts

Add your new key/value to the appropriate section (e.g., authentication, general, fields, etc.)
Use nested objects for organization
Example:
export const enTranslations = {
  authentication: {
    // ... existing keys
    newFeature: 'New Feature Text',
  },
}


Add client key (if needed for client-side usage) to packages/translations/src/clientKeys.ts

Add the translation key path using colon notation
Example: 'authentication:newFeature'
Client keys are used for translations that need to be available in the browser

Generate translations for all languages

Change directory: cd tools/scripts
Run: pnpm generateTranslations:core
This auto-translates your new English keys to all other supported languages
2. Plugin Translations

When to use: Adding translations to any plugin package (packages/plugin-*)

Steps:

Verify plugin has translations folder

Check if packages/plugin-{name}/src/translations exists
If it doesn't exist, see "Scaffolding New Plugin Translations" below

Add the English translation to the plugin's packages/plugin-{name}/src/translations/languages/en.ts

Plugin translations are namespaced under the plugin name
Example for plugin-multi-tenant:
export const enTranslations = {
  'plugin-multi-tenant': {
    'new-feature-label': 'New Feature',
  },
}


Generate translations for all languages

Change directory: cd tools/scripts
Run the plugin-specific script: pnpm generateTranslations:plugin-{name}
Examples:
pnpm generateTranslations:plugin-multi-tenant
pnpm generateTranslations:plugin-ecommerce
pnpm generateTranslations:plugin-import-export
Scaffolding New Plugin Translations

If a plugin doesn't have a translations folder yet, ask the user if they want to scaffold one.

Structure to create:
packages/plugin-{name}/src/translations/
├── index.ts
├── types.ts
└── languages/
    ├── en.ts
    ├── es.ts
    └── ... (all other language files)

Files to create:
types.ts - Define the plugin's translation types
index.ts - Export all translations and re-export types
languages/en.ts - English translations (the source for generation)
languages/*.ts - Other language files (initially empty, will be generated)
Generation script to create:

Create tools/scripts/src/generateTranslations/plugin-{name}.ts

Use plugin-multi-tenant.ts as a template
Update the import paths to point to the new plugin
Update the targetFolder path

Add script to tools/scripts/package.json:

"generateTranslations:plugin-{name}": "node --no-deprecation --import @swc-node/register/esm-register src/generateTranslations/plugin-{name}.ts"

Important Notes
All translation generation requires OPENAI_KEY environment variable to be set
The generation scripts use OpenAI to translate from English to other languages
Always add translations to English first - it's the source of truth
Core translations: Client keys are only needed for translations used in the browser/admin UI
Plugin translations: Automatically namespaced under the plugin name to avoid conflicts
Weekly Installs
282
Repository
payloadcms/payload
GitHub Stars
42.1K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass