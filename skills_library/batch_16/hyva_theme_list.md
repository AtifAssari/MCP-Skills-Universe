---
title: hyva-theme-list
url: https://skills.sh/hyva-themes/hyva-ai-tools/hyva-theme-list
---

# hyva-theme-list

skills/hyva-themes/hyva-ai-tools/hyva-theme-list
hyva-theme-list
Installation
$ npx skills add https://github.com/hyva-themes/hyva-ai-tools --skill hyva-theme-list
SKILL.md
Hyvä Theme Listing

Lists all Hyvä theme paths in a Magento 2 project. Themes are identified by the presence of web/tailwind/package.json.

Usage

Important: Execute this script from the Magento project root directory.

Run the discovery script to list all Hyvä themes:

bash <skill_path>/scripts/list_hyva_themes.sh


Where <skill_path> is the directory containing this SKILL.md file (e.g., .claude/skills/hyva-theme-list).

Output format: One theme path per line (relative to project root), or empty output if no themes found.

app/design/frontend/Example/customTheme
vendor/hyva-themes/magento2-default-theme-csp

Search Locations

The script searches two locations:

Location	Description
app/design/frontend/	Custom themes developed for the project
vendor/	Installed themes from any vendor (not limited to hyva-themes)
Theme Identification

A directory is identified as a Hyvä theme when it contains both:

web/tailwind/package.json (Hyvä/Tailwind structure)
theme.xml (valid Magento theme)
Integration with Other Skills

Other skills that need to locate Hyvä themes should invoke this skill by name:

Invoke the `hyva-theme-list` skill to discover available themes.


The output can be processed line-by-line or stored in a variable for selection prompts.

Weekly Installs
301
Repository
hyva-themes/hyv…ai-tools
GitHub Stars
65
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass