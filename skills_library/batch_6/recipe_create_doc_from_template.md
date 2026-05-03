---
title: recipe-create-doc-from-template
url: https://skills.sh/googleworkspace/cli/recipe-create-doc-from-template
---

# recipe-create-doc-from-template

skills/googleworkspace/cli/recipe-create-doc-from-template
recipe-create-doc-from-template
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-create-doc-from-template
Summary

Template-based Google Doc creation with automated content population and team sharing.

Requires gws-drive and gws-docs skills; uses Google Workspace APIs for file operations and document editing
Workflow: copy a template doc, populate it with structured content via the docs API, then grant collaborator access through drive permissions
Supports markdown-style content insertion and granular permission assignment (writer, editor roles, user/group targeting)
SKILL.md
Create a Google Doc from a Template

PREREQUISITE: Load the following skills to execute this recipe: gws-drive, gws-docs

Copy a Google Docs template, fill in content, and share with collaborators.

Steps
Copy the template: gws drive files copy --params '{"fileId": "TEMPLATE_DOC_ID"}' --json '{"name": "Project Brief - Q2 Launch"}'
Get the new doc ID from the response
Add content: `gws docs +write --document-id NEW_DOC_ID --text '## Project: Q2 Launch
Objective

Launch the new feature by end of Q2.'4. Share with team:gws drive permissions create --params '{"fileId": "NEW_DOC_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}'`

Weekly Installs
11.6K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass