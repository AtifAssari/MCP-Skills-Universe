---
title: i18n-completeness
url: https://skills.sh/sakataka/tetris-game2/i18n-completeness
---

# i18n-completeness

skills/sakataka/tetris-game2/i18n-completeness
i18n-completeness
Installation
$ npx skills add https://github.com/sakataka/tetris-game2 --skill i18n-completeness
SKILL.md
i18n Consistency Check & Cleanup

Comprehensive i18n analysis tool for the Tetris project supporting 2 languages (Japanese, English).

Quick Check
bun run check:i18n

Detection Capabilities
🔴 Missing Keys (Critical)
Keys used in code but not present in translation files
Priority: Critical (causes runtime errors)
Impact: Displays raw translation keys to users
Action: Add missing keys to all translation files immediately
📝 Hardcoded Strings (i18n Compliance)
User-facing strings not using t() function
Examples: "AI Replay", "Start AI", "Loading..."
Scope: Production code only (test files excluded)
Action: Convert to translation keys for proper localization
🔄 Dynamic Key Patterns (Analysis Required)
Template literal patterns like t(\game.${type}`)`
Analysis: Validates all possible key combinations exist
Action: Verify all generated keys are defined
⚠️ Unused Keys (Optimization)
Keys present in translation files but not used in code
Priority: Medium (cleanup opportunity)
Action: Remove unnecessary keys to optimize file size
Workflow
Execute Check: Run bun run check:i18n
Identify Issues: List Missing/Unused keys
Propose Fixes: Present specific correction methods
Confirm Execution: Ask user to approve modifications
Apply Fixes: Update translation files after approval
Verify: Re-run check after modifications
Translation Files
src/assets/locales/ja.json - Japanese translations (default)
src/assets/locales/en.json - English translations
Safety Measures
Re-verify usage before key deletion
Execute consistent operations across all language files
Validate JSON syntax after modifications
Confirm no issues with tests and build
When This Skill Activates
"Check translations"
"i18n consistency check"
"Are all translation keys defined?"
"Find hardcoded strings"
"Translation cleanup"
"Localization issues"
"Missing translation keys"
Weekly Installs
8
Repository
sakataka/tetris-game2
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass