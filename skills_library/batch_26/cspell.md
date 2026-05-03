---
title: cspell
url: https://skills.sh/vdustr/vp-claude-code-marketplace/cspell
---

# cspell

skills/vdustr/vp-claude-code-marketplace/cspell
cspell
Installation
$ npx skills add https://github.com/vdustr/vp-claude-code-marketplace --skill cspell
SKILL.md
cspell

Prioritized strategy for handling cspell unknown word warnings. Classify each flagged word, pick the narrowest fix, and optionally bootstrap cspell config for projects that don't have it yet.

Core Principles
Config Check First — Verify repo has cspell config before any action; offer bootstrap if missing
Adjust Text Before Adding to Dictionary — Restructure words (hyphenate, camelCase) when safe
Narrowest Scope Wins — Inline directive for one-off words; project dictionary for recurring terms

Documentation: Fetch cspell syntax and config details via Context7 (/streetsidesoftware/cspell) at runtime; never rely on hardcoded syntax.

When to Use
cspell flags an unknown word (IDE diagnostic or CI output)
User asks to fix cspell warnings, add words to dictionary, or suppress cspell errors
User wants to set up cspell in a project that doesn't have it
User asks why a word is flagged or wants to understand cspell behavior
Linting pipeline or pre-commit hook fails due to unrecognized words

When NOT to use: For non-cspell spell checkers (typo, codespell, Vale, textlint). For other linting tools (ESLint, markdownlint), use their respective strategies.

Workflow
Check for cspell config — Search from the file's directory upward for cspell config files: package.json (cspell field), .cspell.json, cspell.json, cspell.config.{json,mjs,js,cjs,yaml,yml,toml}, cspell.{yaml,yml}, and their ./.config/ prefixed variants (e.g., .cspell.config.yaml, .config/cspell.json). Also check .vscode/cspell.json. If none found: notify user, do NOT auto-fix, offer to bootstrap (see below). Note: cspell.* settings in .vscode/settings.json are IDE-local and do not count as project config.
Apply fix priority — Stop at the first applicable level (see table below).
Select directive — When using inline directives, consult decision-tree.md for the selection guide.
Fix Priority
Priority	Strategy	When to Use
1	Adjust text	Compound word cspell doesn't recognize; restructuring is safe (hyphenate, camelCase). See decision-tree.md for the full exception list
2	Project dictionary	Word appears in 2+ files or is expected to recur project-wide
3	Inline directive	One-off word in a single file/location. See decision-tree.md for directive selection and placement
Config Bootstrapping

When a repo has no cspell config and the user wants to add one, guide through an interactive Q&A flow.

See config-bootstrapping.md for the full interactive setup flow.

Guidelines
DO
Check repo config before any action
Prefer text adjustment over dictionary pollution
Use narrowest scope directive that fits
Place cspell:words at file top for discoverability
Verify the flagged word is genuinely unknown (not a missing dictionary)
DON'T
Replace words with semantically different alternatives
Add one-off words to project dictionary (use inline directives)
Use cspell:disable to suppress large sections when individual words can be handled
Blindly accept all cspell suggestions — some flagged words are correct
Hyphenate or restructure runtime API identifiers, package names, or fixed external terms
Error Handling
Error	Action
No write permission to config	Notify user, suggest manual edit path
Excessive cspell . output	Scope to source directory, configure ignorePaths first
Context7 unavailable	Fall back to cspell.org or cspell init --help

For bootstrapping-specific errors (cspell CLI not installed, cspell init fails), see config-bootstrapping.md.

Reference Files
decision-tree.md — Full decision flowchart, text adjustment rules and exceptions, dictionary vs inline criteria, directive selection, edge cases
config-bootstrapping.md — Interactive setup flow, stack detection, CI integration, post-init adjustments
Weekly Installs
10
Repository
vdustr/vp-claud…ketplace
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn