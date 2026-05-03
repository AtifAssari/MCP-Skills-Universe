---
rating: ⭐⭐
title: localization
url: https://skills.sh/johnrogers/claude-swift-engineering/localization
---

# localization

skills/johnrogers/claude-swift-engineering/localization
localization
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill localization
SKILL.md
Localization

Modern iOS localization using String Catalogs (.xcstrings) for managing translations, plural forms, and locale-aware content. Supports SwiftUI's LocalizedStringKey and String(localized:) APIs.

Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
String Catalogs	Setting up or using Xcode 15+ String Catalogs
Pluralization	Handling plural forms, stringsdict migration
Formatting	Date, number, currency locale-aware formatting
RTL Support	Right-to-left layouts, semantic directions
Core Workflow
Create String Catalog in Xcode (File > New > String Catalog)
Mark strings with String(localized:comment:) or use SwiftUI's automatic extraction
Add plural variants in String Catalog editor where needed
Test with pseudo-localization (Scheme > Run > Options > App Language)
Export for translation (File > Export Localizations)
Key Patterns
// SwiftUI - automatic localization
Text("Welcome")
Button("Continue") { }

// Explicit localization with context
let title = String(localized: "Settings", comment: "Navigation title")

// Deferred localization for custom views
struct CardView: View {
    let title: LocalizedStringResource
    var body: some View { Text(title) }
}

Build Settings
Use Compiler to Extract Swift Strings: Yes
Localization Prefers String Catalogs: Yes
Common Mistakes

Forgetting String Catalog in Build Phases — Adding String Catalog but forgetting to check "Localize" in File Inspector means it's not embedded. Always verify in Build Phases > Copy Bundle Resources.

Pseudo-localization not tested — Not running your app with pseudo-localization (German/Chinese pseudo-locale) means you miss text overflow and RTL issues. Always test with pseudo-localization before translation.

Hardcoded strings anywhere — Even one hardcoded string outside the String Catalog breaks extraction and automation. Use String(localized:) everywhere or use LocalizedStringResource for deferred localization.

Context loss in translations — Providing no comment for translators means they guess context and get it wrong. Add comments explaining where the string appears and what it means.

RTL layouts not tested — Assuming LTR layout works for RTL languages (Arabic, Hebrew) fails miserably. Test with system language set to Arabic and verify semantic directions are used.

Weekly Installs
100
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass