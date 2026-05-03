---
title: recipe-create-presentation
url: https://skills.sh/googleworkspace/cli/recipe-create-presentation
---

# recipe-create-presentation

skills/googleworkspace/cli/recipe-create-presentation
recipe-create-presentation
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-create-presentation
Summary

Create a new Google Slides presentation with initial slides and sharing.

Requires the gws-slides skill as a prerequisite dependency
Creates presentations with a specified title and retrieves the presentation ID for further operations
Supports sharing presentations with team members by setting permissions (writer, viewer, or other roles) via email address
SKILL.md
Create a Google Slides Presentation

PREREQUISITE: Load the following skills to execute this recipe: gws-slides

Create a new Google Slides presentation and add initial slides.

Steps
Create presentation: gws slides presentations create --json '{"title": "Quarterly Review Q2"}'
Get the presentation ID from the response
Share with team: gws drive permissions create --params '{"fileId": "PRESENTATION_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}'
Weekly Installs
12.1K
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