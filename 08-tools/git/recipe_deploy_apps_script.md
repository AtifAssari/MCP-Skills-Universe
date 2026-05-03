---
rating: ⭐⭐
title: recipe-deploy-apps-script
url: https://skills.sh/googleworkspace/cli/recipe-deploy-apps-script
---

# recipe-deploy-apps-script

skills/googleworkspace/cli/recipe-deploy-apps-script
recipe-deploy-apps-script
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-deploy-apps-script
Summary

Deploy local files to Google Apps Script projects with version control.

Requires the gws-apps-script skill and gws command-line tool as prerequisites
Supports listing projects, retrieving project content, updating files, and creating versioned releases
Workflow covers four core operations: project discovery, content inspection, file updates, and version creation
SKILL.md
Deploy an Apps Script Project

PREREQUISITE: Load the following skills to execute this recipe: gws-apps-script

Push local files to a Google Apps Script project.

Steps
List existing projects: gws apps-script projects list --format table
Get project content: gws apps-script projects getContent --params '{"scriptId": "SCRIPT_ID"}'
Update content: gws apps-script projects updateContent --params '{"scriptId": "SCRIPT_ID"}' --json '{"files": [{"name": "Code", "type": "SERVER_JS", "source": "function main() { ... }"}]}'
Create a new version: gws apps-script projects versions create --params '{"scriptId": "SCRIPT_ID"}' --json '{"description": "v2 release"}'
Weekly Installs
604
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass