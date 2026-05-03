---
rating: ⭐⭐⭐
title: typo3-typoscript-ref
url: https://skills.sh/netresearch/typo3-typoscript-ref-skill/typo3-typoscript-ref
---

# typo3-typoscript-ref

skills/netresearch/typo3-typoscript-ref-skill/typo3-typoscript-ref
typo3-typoscript-ref
Installation
$ npx skills add https://github.com/netresearch/typo3-typoscript-ref-skill --skill typo3-typoscript-ref
SKILL.md
TYPO3 TypoScript, TSconfig and Fluid Reference

Version-aware local lookup with always-on best practices.

Usage
scripts/lookup.sh "stdWrap wrap"              # Reference lookup
scripts/lookup.sh "PAGEVIEW" --with-fluid     # With Fluid context
scripts/lookup.sh --recipe page-setup         # Recipe for common tasks
scripts/lookup.sh "FLUIDTEMPLATE" --review    # Adds deprecation warnings
scripts/lookup.sh --deprecations              # Deprecation list
scripts/lookup.sh --checklist typoscript      # Review checklist (typoscript|tsconfig|fluid)
scripts/lookup.sh --lint-rules                # Project lint rules
scripts/lookup.sh --debug "The page is not configured"  # Debug error
scripts/lookup.sh --update                    # Update cache
scripts/lookup.sh "TEXT" --version 12         # Override version

Rules
ALWAYS run lookup.sh before writing or reviewing TypoScript/TSconfig/Fluid code
ALWAYS follow best practice annotations (required/deprecated/recommended/tip)
ALWAYS check project lint rules (--lint-rules) before writing TypoScript
When writing NEW code: use the most modern approach for the detected version
When reviewing EXISTING code: flag deprecated patterns, check --deprecations for the project's version
For combined TypoScript+Fluid tasks: use --with-fluid flag
Never generate config.no_cache = 1 in production setups
Prefer DataProcessors over CONTENT cObject in Fluid-based templates
Version-Specific Guidance
v12: Use FLUIDTEMPLATE, sys_template static includes, constants.typoscript
v13: Prefer PAGEVIEW for new page templates, introduce Site Sets, use settings.definitions.yaml
v14: Site Sets mandatory, FLUIDTEMPLATE deprecated, @import replaces INCLUDE_TYPOSCRIPT

When answering version-specific questions, always consult references/review/deprecations.md and the relevant migration guide (migration-v12-to-v13.md or migration-v13-to-v14.md).

Review Workflow

When reviewing TypoScript/TSconfig/Fluid code:

Run --checklist for the file type (typoscript, tsconfig, or fluid)
Run --deprecations filtered to project version
Cross-reference references/review/common-mistakes.md for known pitfalls
Check references/review/security.md for Fluid XSS patterns (f:format.raw, f:sanitize.html)
Check references/review/performance.md for COA_INT/USER_INT overuse
Use --review flag on keyword lookups to append deprecation context
Reference Index
Need	Reference
TypoScript patterns, Fluid best practices	references/patterns.md
Debugging errors	references/debugging.md
Deprecation lists	references/review/deprecations.md
Security (XSS, escaping)	references/review/security.md
Performance (caching, INT objects)	references/review/performance.md
Common mistakes	references/review/common-mistakes.md
Migration v12-v13	references/review/migration-v12-to-v13.md
Migration v13-v14	references/review/migration-v13-to-v14.md
First Run
scripts/lookup.sh --update

Weekly Installs
19
Repository
netresearch/typ…ef-skill
GitHub Stars
1
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass