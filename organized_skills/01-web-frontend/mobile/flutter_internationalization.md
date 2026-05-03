---
rating: ⭐⭐
title: flutter-internationalization
url: https://skills.sh/madteacher/mad-agents-skills/flutter-internationalization
---

# flutter-internationalization

skills/madteacher/mad-agents-skills/flutter-internationalization
flutter-internationalization
Installation
$ npx skills add https://github.com/madteacher/mad-agents-skills --skill flutter-internationalization
Summary

Complete guide for internationalizing Flutter apps with gen-l10n, intl package, and custom approaches.

Covers three setup paths: gen-l10n (recommended, code-generated from ARB files), intl package (manual, code-based), and custom Map-based localizations for maximum flexibility
Supports message types including simple strings, placeholders with parameters, plurals based on count, and select messages based on string values
Includes automatic number and date formatting with locale-aware options like simpleCurrency, compact, and date patterns (yMMMd, Hm, etc.)
Provides advanced features: locale override for specific widgets, custom locale definitions for regional variants, locale resolution callbacks, and RTL language support
SKILL.md
Flutter Internationalization

You are a Flutter localization implementer. Make localized apps build, generate, and read naturally across target locales.

Principle 0

Generated localization code must match the current Flutter project and SDK. Do not copy stale package:flutter_gen imports or enable synthetic-package; use source-generated AppLocalizations imports unless the project proves it is on an older pinned Flutter workflow.

Decision Guide
Use gen-l10n for new work, most migrations, ARB management, plural/select messages, generated AppLocalizations, and Material/Cupertino apps.
Use legacy intl_translation only when the project already uses Intl.message() plus generated messages_all.dart, or the user explicitly asks to keep that workflow. Confirm intl_translation is a dependency before running its generators.
Use custom map-based localizations only for tiny prototypes or existing code that intentionally avoids code generation. Name this limitation in the final response.
If the project has an existing localization setup, follow its paths, class names, locale list, and generation style before introducing defaults.
Workflow
Inspect pubspec.yaml, l10n.yaml, existing *.arb files, generated imports, MaterialApp/CupertinoApp setup, and current translation usage.
Identify the requested change: bootstrap l10n, add a locale, replace hardcoded UI text, add placeholders/plurals/selects, format values, fix generation, or migrate stale imports/config.
Use the decision guide to choose gen-l10n, legacy intl_translation, or a custom fallback. Prefer the smallest change that fits the existing project.
Read only the routed references needed for the task.
Make the localization change:
add flutter_localizations and intl:any when missing;
set flutter: generate: true;
create or update l10n.yaml;
create or update ARB files with descriptions and placeholder metadata;
wire AppLocalizations into MaterialApp or CupertinoApp;
replace hardcoded UI strings with generated getters or methods.
Generate and validate with flutter gen-l10n. Then run the narrowest relevant project check, usually flutter analyze or affected tests.
Report changed files, generated behavior, validation run, and any locales or translation gaps that remain.
Resource Routing
Task	Read or use	Why
Configure or debug l10n.yaml, generated output paths, nullable getters, deferred loading, or untranslated tracking	references/l10n-config.md	Current gen-l10n options and safe defaults
Create or repair ARB messages, placeholders, plurals, selects, escaping, or metadata	references/arb-format.md	ARB schema patterns and translator context rules
Add number, currency, percent, or date/time formatting	references/number-date-formats.md	Supported NumberFormat and DateFormat values
Bootstrap a new gen-l10n setup or run a smoke fixture	assets/l10n.yaml, assets/app_en.arb	Reusable minimal templates
gen-l10n Contract

For new gen-l10n setup, the minimum current configuration is:

flutter:
  generate: true

arb-dir: lib/l10n
template-arb-file: app_en.arb
output-localization-file: app_localizations.dart


Use source imports that match the generated location, commonly:

import 'l10n/app_localizations.dart';


Prefer generated lists when possible:

localizationsDelegates: AppLocalizations.localizationsDelegates,
supportedLocales: AppLocalizations.supportedLocales,


If generated files are written to a custom output-dir, update imports to that directory. Do not import package:flutter_gen/gen_l10n/app_localizations.dart unless the local project is intentionally pinned to an older Flutter workflow.

Legacy Intl Fallback

When preserving Intl.message():

require intl_translation in dev dependencies before extraction/generation;
keep generated files and imports consistent with the existing project;
run extraction before generation;
on Windows or shells without wildcard expansion, list ARB files explicitly.

Typical commands:

dart run intl_translation:extract_to_arb --output-dir=lib/l10n lib/main.dart
dart run intl_translation:generate_from_arb --output-dir=lib/l10n --no-use-deferred-loading lib/main.dart lib/l10n/intl_*.arb


If this workflow is not already present, explain why gen-l10n is the safer default.

Constraints
Do not invent translations. If target-language text is not supplied, add clear placeholder translations only when the user approved that, or report the missing translations.
Do not concatenate localized strings. Use placeholders, plural, or select messages.
Do not manually format numbers, currency, percentages, dates, or times when gen-l10n placeholder formatting can do it.
Do not add synthetic-package: true; current Flutter marks synthetic package generation as deprecated and unavailable.
Set nullable-getter: false only when the project accepts non-null generated getter behavior. Otherwise keep the project default and use the required null handling in code.
Keep translator-facing descriptions and examples in the template ARB file.
For RTL locales, check text direction, layout assumptions, mirrored icons, and locale-specific widgets.
Validation

Always validate a completed localization change:

flutter gen-l10n succeeds with the project's l10n.yaml;
generated import paths compile;
every new ARB key exists in the template file and needed locale files;
placeholders in translated ARB values match template metadata;
plural/select messages include other;
number/date placeholders use supported formats from references/number-date-formats.md;
relevant flutter analyze or tests pass, or blockers are reported.

For skill maintenance, also check YAML frontmatter, local markdown links, JSON validity for ARB assets, YAML validity for l10n.yaml, resource routing, and layer coherence between SKILL.md, references, and assets.

Weekly Installs
384
Repository
madteacher/mad-…s-skills
GitHub Stars
92
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass