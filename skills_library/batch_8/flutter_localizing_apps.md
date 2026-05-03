---
title: flutter-localizing-apps
url: https://skills.sh/flutter/skills/flutter-localizing-apps
---

# flutter-localizing-apps

skills/flutter/skills/flutter-localizing-apps
flutter-localizing-apps
Installation
$ npx skills add https://github.com/flutter/skills --skill flutter-localizing-apps
Summary

Multi-language support for Flutter apps using ARB files and code generation.

Configure pubspec.yaml with flutter_localizations and intl, then define an l10n.yaml file to enable the gen-l10n code generator
Store localized strings in Application Resource Bundle (.arb) JSON files; the template file defines all keys, and locale-specific files provide translations
Integrate localizations into MaterialApp or CupertinoApp by adding AppLocalizations.delegate and platform-specific delegates to localizationsDelegates, then access strings via AppLocalizations.of(context)
Support dynamic content with placeholders, plurals, selects, and formatted dates/numbers using ICU message syntax in ARB metadata
iOS requires additional bundle configuration in Xcode to register supported languages with the App Store
SKILL.md
Localizing Flutter Applications
Contents
Core Configuration
Defining ARB Resources
App Integration
Advanced Formatting
Workflows
Troubleshooting & Gotchas
Core Configuration

Configure the project to support code generation for localizations.

Add required dependencies to pubspec.yaml:
dependencies:
  flutter:
    sdk: flutter
  flutter_localizations:
    sdk: flutter
  intl: any

flutter:
  generate: true # Required for l10n code generation

Create an l10n.yaml file in the project root to configure the gen-l10n tool:
arb-dir: lib/l10n
template-arb-file: app_en.arb
output-localization-file: app_localizations.dart
# Optional: Set to false to generate files into lib/ instead of the synthetic package
# synthetic-package: false 

Defining ARB Resources

Store localized strings in Application Resource Bundle (.arb) files within the configured arb-dir.

Create the template file (e.g., lib/l10n/app_en.arb):

{
  "helloWorld": "Hello World!",
  "@helloWorld": {
    "description": "The conventional newborn programmer greeting"
  }
}


Create translation files (e.g., lib/l10n/app_es.arb):

{
  "helloWorld": "¡Hola Mundo!"
}

App Integration

Initialize the Localizations widget by configuring the root MaterialApp or CupertinoApp.

import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart'; // Adjust import if synthetic-package is false

return MaterialApp(
  title: 'Localized App',
  localizationsDelegates: const [
    AppLocalizations.delegate,
    GlobalMaterialLocalizations.delegate,
    GlobalWidgetsLocalizations.delegate,
    GlobalCupertinoLocalizations.delegate,
  ],
  supportedLocales: const [
    Locale('en'), // English
    Locale('es'), // Spanish
  ],
  home: const MyHomePage(),
);


Access localized values in the widget tree using the generated AppLocalizations class:

Text(AppLocalizations.of(context)!.helloWorld)


Note: If using WidgetsApp instead of MaterialApp, omit GlobalMaterialLocalizations.delegate.

Advanced Formatting

Use placeholders, plurals, and selects for dynamic content. Define parameters in the @key metadata.

Placeholders
"hello": "Hello {userName}",
"@hello": {
  "description": "A message with a single parameter",
  "placeholders": {
    "userName": {
      "type": "String",
      "example": "Bob"
    }
  }
}

Plurals
"nWombats": "{count, plural, =0{no wombats} =1{1 wombat} other{{count} wombats}}",
"@nWombats": {
  "placeholders": {
    "count": {
      "type": "num",
      "format": "compact"
    }
  }
}

Selects (Gender/Enums)
"pronoun": "{gender, select, male{he} female{she} other{they}}",
"@pronoun": {
  "placeholders": {
    "gender": {
      "type": "String"
    }
  }
}

Dates and Numbers

Use format and optionalParameters to leverage intl formatting.

"dateMessage": "Date: {date}",
"@dateMessage": {
  "placeholders": {
    "date": {
      "type": "DateTime",
      "format": "yMd"
    }
  }
}

Workflows
Task Progress: Adding a New Language

Copy this checklist to track progress when introducing a new locale.

 Create a new .arb file in the arb-dir (e.g., app_fr.arb).
 Translate all keys present in the template .arb file.
 Add the new Locale to the supportedLocales list in MaterialApp.
 Run validator -> Execute flutter gen-l10n to verify ARB syntax and regenerate AppLocalizations.
 Review errors -> Fix any missing placeholders or malformed plural/select statements.
 If targeting iOS, complete the "Configuring iOS App Bundle" workflow.
Task Progress: Configuring iOS App Bundle

Flutter handles runtime localization, but iOS requires bundle-level configuration for the App Store and system settings.

 Open ios/Runner.xcodeproj in Xcode.
 Select the Runner project in the Project Navigator.
 Navigate to the Info tab.
 Under the Localizations section, click the + button.
 Add the newly supported languages/regions.
 Run validator -> Build the iOS app to ensure project.pbxproj is correctly updated.
Troubleshooting & Gotchas
Missing Localizations Ancestor

Widgets like TextField and CupertinoTabBar require a Localizations ancestor with specific delegates (MaterialLocalizations or CupertinoLocalizations).

Error: No MaterialLocalizations found. or CupertinoTabBar requires a Localizations parent... Fix: Ensure the widget is a descendant of MaterialApp/CupertinoApp. If building a standalone widget tree (e.g., in tests or a custom WidgetsApp), wrap the widget in a Localizations widget:

Localizations(
  locale: const Locale('en', 'US'),
  delegates: const [
    DefaultWidgetsLocalizations.delegate,
    DefaultMaterialLocalizations.delegate, // Required for TextField
    DefaultCupertinoLocalizations.delegate, // Required for CupertinoTabBar
  ],
  child: child,
)

Advanced Locale Definition

If supporting languages with multiple scripts (e.g., Chinese), use Locale.fromSubtags to explicitly define the scriptCode and countryCode to prevent Flutter from resolving to an unexpected variant.

supportedLocales: const [
  Locale.fromSubtags(languageCode: 'zh', scriptCode: 'Hans', countryCode: 'CN'),
  Locale.fromSubtags(languageCode: 'zh', scriptCode: 'Hant', countryCode: 'TW'),
]

Weekly Installs
8.5K
Repository
flutter/skills
GitHub Stars
1.3K
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass