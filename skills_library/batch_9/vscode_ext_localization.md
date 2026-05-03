---
title: vscode-ext-localization
url: https://skills.sh/github/awesome-copilot/vscode-ext-localization
---

# vscode-ext-localization

skills/github/awesome-copilot/vscode-ext-localization
vscode-ext-localization
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill vscode-ext-localization
Summary

Localize VS Code extensions across configurations, walkthrough content, and source code messages.

Three localization approaches: package.nls.LANGID.json for settings, commands, menus, and views; markdown files for walkthrough content; bundle.l10n.LANGID.json for source code strings
Covers all user-facing resources including contributed configurations, commands, menus, views, ViewsWelcome, and walkthrough titles and descriptions
Requires creating or updating localization files for all supported languages whenever a localizable resource is added or modified
SKILL.md
VS Code extension localization

This skill helps you localize every aspect of VS Code extensions

When to use this skill

Use this skill when you need to:

Localize new or existing contributed configurations (settings), commands, menus, views or walkthroughs
Localize new or existing messages or other string resources contained in extension source code that are displayed to the end user
Instructions

VS Code localization is composed by three different approaches, depending on the resource that is being localized. When a new localizable resource is created or updated, the corresponding localization for all currently available languages must be created/updated.

Configurations like Settings, Commands, Menus, Views, ViewsWelcome, Walkthrough Titles and Descriptions, defined in package.json -> An exclusive package.nls.LANGID.json file, like package.nls.pt-br.json of Brazilian Portuguese (pt-br) localization
Walkthrough content (defined in its own Markdown files) -> An exclusive Markdown file like walkthrough/someStep.pt-br.md for Brazilian Portuguese localization
Messages and string located in extension source code (JavaScript or TypeScript files) -> An exclusive bundle.l10n.pt-br.json for Brazilian Portuguese localization
Weekly Installs
8.5K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass