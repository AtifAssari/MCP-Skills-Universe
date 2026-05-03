---
title: localize
url: https://skills.sh/ryokun6/ryos/localize
---

# localize

skills/ryokun6/ryos/localize
localize
Installation
$ npx skills add https://github.com/ryokun6/ryos --skill localize
SKILL.md
Localize App or Component
Workflow Checklist
- [ ] 1. Extract hardcoded strings
- [ ] 2. Replace with t() calls in source files
- [ ] 3. Add English translations to en/translation.json
- [ ] 4. Sync translations across languages
- [ ] 5. Machine translate [TODO] keys
- [ ] 6. Validate coverage

Step 1: Extract Hardcoded Strings
bun run scripts/extract-strings.ts --pattern [PATTERN]

Step 2: Replace Strings with t() Calls

For each component:

Add import: import { useTranslation } from "react-i18next";
Add hook: const { t } = useTranslation();
Replace strings: t("apps.[appName].category.key")
Add t to dependency arrays for useMemo/useCallback
Key Structure
apps.[appName].menu.*        # Menu labels
apps.[appName].dialogs.*     # Dialog titles/descriptions
apps.[appName].status.*      # Status messages
apps.[appName].ariaLabels.*  # Accessibility labels
apps.[appName].help.*        # Help items (auto-translated)

Common Patterns
// Basic
t("apps.ipod.menu.file")

// With variables
t("apps.ipod.status.trackCount", { count: 5 })

// Conditional
isPlaying ? t("pause") : t("play")

// With symbol prefix
`✓ ${t("apps.ipod.menu.shuffle")}`

Step 3: Add English Translations

Add to src/lib/locales/en/translation.json:

{
  "apps": {
    "ipod": {
      "menu": { "file": "File", "addSong": "Add Song..." },
      "dialogs": { "clearLibraryTitle": "Clear Library" },
      "status": { "shuffleOn": "Shuffle ON" }
    }
  }
}

Step 4: Sync Across Languages
bun run scripts/sync-translations.ts --mark-untranslated


Adds missing keys to all language files, marked with [TODO].

Step 5: Machine Translate
bun run scripts/machine-translate.ts


Requires GOOGLE_GENERATIVE_AI_API_KEY env variable.

Step 6: Validate
bun run scripts/find-untranslated-strings.ts

Component Guidelines
Component	What to translate
Menu bars	All labels, items, submenus
Dialogs	Titles, descriptions, button labels
Status	showStatus() calls, toasts
Help items	Auto-translated via useTranslatedHelpItems
Notes
Emoji/symbols (♪, ✓) can stay hardcoded
Help items use pattern: apps.[appName].help.[key].title/description
Include t in dependency arrays when used in useMemo/useCallback
Weekly Installs
25
Repository
ryokun6/ryos
GitHub Stars
1.1K
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass