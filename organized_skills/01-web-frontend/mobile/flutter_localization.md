---
rating: ⭐⭐
title: flutter-localization
url: https://skills.sh/flutter/skills/flutter-localization
---

# flutter-localization

skills/flutter/skills/flutter-localization
flutter-localization
Installation
$ npx skills add https://github.com/flutter/skills --skill flutter-localization
Summary

Configure Flutter apps to support multiple languages and locales with proper i18n setup.

Manages dependency injection (flutter_localizations, intl), code generation configuration (l10n.yaml), and .arb translation file creation with support for placeholders, plurals, and regional variants
Configures root widget delegates (MaterialApp, CupertinoApp, or WidgetsApp) and handles isolated widgets like TextField and CupertinoTabBar that require explicit Localizations wrapping
Supports complex locales using Locale.fromSubtags for multi-script languages (e.g., Chinese zh_Hans_CN) and includes iOS Xcode project configuration for App Store locale exposure
Prevents common assertion errors by ensuring proper localization delegate hierarchy and validates generated code with flutter gen-l10n
SKILL.md
Flutter Localization Setup
Goal

Configures and implements internationalization (i18n) and localization (l10n) in a Flutter application. This skill manages dependency injection (flutter_localizations, intl), code generation configuration (l10n.yaml), root widget setup (MaterialApp, CupertinoApp, or WidgetsApp), .arb translation file management, and platform-specific configurations (iOS Xcode project updates). It ensures proper locale resolution and prevents common assertion errors related to missing localization delegates in specific widgets like TextField and CupertinoTabBar.

Decision Logic
Determine App Root: Identify if the application uses MaterialApp, CupertinoApp, or WidgetsApp to inject the correct global delegates.
Identify Target Platforms: If iOS is a target platform, Xcode project files (Info.plist / project.pbxproj) must be updated to expose supported locales to the App Store.
Analyze Widget Tree: Check for isolated TextField or CupertinoTabBar widgets that might exist outside the root app's localization scope. If found, wrap them in explicit Localizations widgets.
Determine Locale Complexity: If supporting languages with multiple scripts/regions (e.g., Chinese zh_Hans_CN), use Locale.fromSubtags instead of the default Locale constructor.
Instructions

Configure Dependencies Update pubspec.yaml to include required packages and enable code generation.

dependencies:
  flutter:
    sdk: flutter
  flutter_localizations:
    sdk: flutter
  intl: any

flutter:
  generate: true


Configure Code Generation Create an l10n.yaml file in the project root to define the localization tool's behavior.

arb-dir: lib/l10n
template-arb-file: app_en.arb
output-localization-file: app_localizations.dart
synthetic-package: false


Define Supported Locales STOP AND ASK THE USER: "Which languages and regions do you want to support? Please provide a list of language codes (e.g., 'en', 'es', 'zh_Hans_CN')."

Create ARB Files Generate the template .arb file (e.g., lib/l10n/app_en.arb) and corresponding translation files. Implement placeholders, plurals, and selects as needed.

{
  "helloWorld": "Hello World!",
  "@helloWorld": {
    "description": "Standard greeting"
  },
  "greeting": "Hello {userName}",
  "@greeting": {
    "description": "Greeting with a parameter",
    "placeholders": {
      "userName": {
        "type": "String"
      }
    }
  },
  "nWombats": "{count, plural, =0{no wombats} =1{1 wombat} other{{count} wombats}}",
  "@nWombats": {
    "placeholders": {
      "count": {
        "type": "num",
        "format": "compact"
      }
    }
  }
}


Initialize Root App Import the generated localizations file and configure the root MaterialApp or CupertinoApp.

import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:your_app_name/l10n/app_localizations.dart'; // Adjust path based on synthetic-package setting

// Inside your root widget build method:
return MaterialApp(
  title: 'Localized App',
  localizationsDelegates: const [
    AppLocalizations.delegate,
    GlobalMaterialLocalizations.delegate,
    GlobalWidgetsLocalizations.delegate,
    GlobalCupertinoLocalizations.delegate,
  ],
  supportedLocales: const [
    Locale('en', ''), // English
    Locale('es', ''), // Spanish
    Locale.fromSubtags(languageCode: 'zh', scriptCode: 'Hans', countryCode: 'CN'),
  ],
  home: const MyHomePage(),
);


Handle Isolated Widgets (If Applicable) If a TextField or CupertinoTabBar throws a missing MaterialLocalizations or Localizations ancestor error, inject a Localizations widget directly above it.

Localizations(
  locale: const Locale('en', 'US'),
  delegates: const <LocalizationsDelegate<dynamic>>[
    DefaultWidgetsLocalizations.delegate,
    DefaultMaterialLocalizations.delegate,
    DefaultCupertinoLocalizations.delegate,
  ],
  child: CupertinoTabBar(
    items: const <BottomNavigationBarItem>[...],
  ),
)


Configure iOS Project STOP AND ASK THE USER: "Does this project target iOS? If yes, I will provide instructions for updating the Xcode project." If yes, instruct the user to:

Open ios/Runner.xcodeproj in Xcode.
Select the Runner project in the Project Navigator.
Go to the Info tab.
Under Localizations, click + to add all supported languages.

Validate and Fix Run flutter gen-l10n. Verify that app_localizations.dart is generated successfully. If compilation fails with "No MaterialLocalizations found" or "CupertinoTabBar requires a Localizations parent", traverse up the widget tree from the failing widget and ensure localizationsDelegates are properly provided.

Constraints
No Synthetic Packages: Ensure synthetic-package: false is considered if the user's environment requires direct source generation, or rely on standard generate: true behavior for modern Flutter versions. Do not use package:flutter_gen imports if synthetic-package: false is set.
Widget Requirements: TextField MUST have a MaterialLocalizations ancestor. CupertinoTabBar MUST have a Localizations ancestor.
Complex Locales: Always use Locale.fromSubtags for languages requiring script codes (e.g., Chinese zh_Hans, zh_Hant).
ARB Syntax: Ensure all placeholders used in .arb strings are explicitly defined in the corresponding @ metadata object.
Escaping: If literal curly braces {} or single quotes ' are needed in .arb files, enable use-escaping: true in l10n.yaml and use consecutive single quotes '' for escaping.
Weekly Installs
991
Repository
flutter/skills
GitHub Stars
1.3K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass