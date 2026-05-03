---
title: vscode-ext-commands
url: https://skills.sh/github/awesome-copilot/vscode-ext-commands
---

# vscode-ext-commands

skills/github/awesome-copilot/vscode-ext-commands
vscode-ext-commands
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill vscode-ext-commands
Summary

VS Code extension command contribution patterns and naming conventions.

Defines two command types: regular commands (accessible in Command Palette with required category and title) and Side Bar commands (prefixed with underscore and suffixed with #sideBar, requiring an icon)
Side Bar commands support visibility rules via enablement and when conditions, with positioning controlled through group and order attributes
All commands must define a title; icons are optional for regular commands but required for Side Bar commands
Emphasizes best practices including Command Palette visibility control, localization support, and conditional rendering based on extension state
SKILL.md
VS Code extension command contribution

This skill helps you to contribute commands in VS Code extensions

When to use this skill

Use this skill when you need to:

Add or update commands to your VS Code extension
Instructions

VS Code commands must always define a title, independent of its category, visibility or location. We use a few patterns for each "kind" of command, with some characteristics, described below:

Regular commands: By default, all commands should be accessible in the Command Palette, must define a category, and don't need an icon, unless the command will be used in the Side Bar.

Side Bar commands: Its name follows a special pattern, starting with underscore (_) and suffixed with #sideBar, like _extensionId.someCommand#sideBar for instance. Must define an icon, and may or may not have some rule for enablement. Side Bar exclusive commands should not be visible in the Command Palette. Contributing it to the view/title or view/item/context, we must inform order/position that it will be displayed, and we can use terms "relative to other command/button" in order to you identify the correct group to be used. Also, it's a good practice to define the condition (when) for the new command is visible.

Weekly Installs
8.6K
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