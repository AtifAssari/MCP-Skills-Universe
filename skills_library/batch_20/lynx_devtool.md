---
title: lynx-devtool
url: https://skills.sh/lynx-community/skills/lynx-devtool
---

# lynx-devtool

skills/lynx-community/skills/lynx-devtool
lynx-devtool
Installation
$ npx skills add https://github.com/lynx-community/skills --skill lynx-devtool
SKILL.md
DevTool Skill

This skill allows you to interact with Lynx applications running on connected devices (Android, iOS, Desktop) using the Lynx DevTool CLI.

Usage

The CLI is located at <path_to_the_skill>/scripts/index.mjs relative to this skill's directory. You can run it using node.

In the skill directory, use:

node <path_to_the_skill>/scripts/index.mjs <command>


Note: All command outputs are multi-line JSON. You can use jq or Node.js to process the data.

Global Options
-h, --help: Display help for command.

Note: Each subcommand supports the --help flag (e.g. node <path_to_the_skill>/scripts/index.mjs cdp --help). Use this to view the full list of available arguments and their descriptions.

Command List
Send CDP Command: Send a supported CDP method to a selected session.
Send App Command: Send an App-level method to the Lynx app.
Open URL: Open a target URL in the Lynx app.
Get Sources: List parsed scripts for later debugger operations.
Take Screenshot: Capture the current page as a screenshot.
Example List
Inspecting the DOM: Find a session, fetch the document tree, and inspect a specific node.
Evaluating JavaScript: Run a small JavaScript expression in the current Lynx session.
Redirect with Development URL: Reload a page with a local dev-server URL during development.
Getting Console Logs: Filter console output to focus on errors and warnings.
Troubleshooting

For connector and transport debug logging, see Troubleshooting Reference.

References
Supported CDP Methods: Detailed documentation of all supported CDP methods, their inputs, and outputs.
Supported App Methods: Detailed documentation of all supported App methods, their inputs, and outputs.
Get Console Reference: Detailed documentation of the get-console command.
Get Sources Reference: Detailed documentation of the get-sources command.
Take Screenshot Reference: Detailed documentation of the take-screenshot command.
Troubleshooting Reference: Debug namespaces, transport-level logs, and examples of healthy connector output.
Weekly Installs
516
Repository
lynx-community/skills
GitHub Stars
21
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn