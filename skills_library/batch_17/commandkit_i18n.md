---
title: commandkit-i18n
url: https://skills.sh/neplextech/commandkit/commandkit-i18n
---

# commandkit-i18n

skills/neplextech/commandkit/commandkit-i18n
commandkit-i18n
Installation
$ npx skills add https://github.com/neplextech/commandkit --skill commandkit-i18n
SKILL.md
CommandKit i18n Plugin
Activation guidance

Use for multilingual command metadata and translated runtime responses.

Required filesystem expectations
plugin registration in commandkit.config.ts
locale files under src/app/locales/<locale>/*.json
command/event handlers in src/app/commands/** and src/app/events/**
Execution workflow
Register i18n() plugin.
Build locale directory and translation files.
Add $command keys for metadata localization.
Use ctx.locale() in commands and locale() in events/utilities.
Validate missing-key and fallback behavior.
Guardrails
Keep translation keys stable across locales.
Ensure all required keys exist in baseline locale.
Reference index
Name	Description
references/00-filesystem-structure.md	Locale folder layout and naming expectations.
references/01-plugin-setup.md	Plugin setup baseline.
references/02-locales-structure.md	Locale file placement and organization details.
references/03-command-metadata-localization.md	$command and context menu metadata localization format.
references/04-locale-helpers.md	Runtime locale helper usage in commands/events.
Tool index
Name	Description
tools/generate-locale-file.mjs	Prints a locale JSON starter template for a command and locale code.
Weekly Installs
13
Repository
neplextech/commandkit
GitHub Stars
159
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass