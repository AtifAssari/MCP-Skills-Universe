---
title: worldbuilding
url: https://skills.sh/bs779517/story-skills/worldbuilding
---

# worldbuilding

skills/bs779517/story-skills/worldbuilding
worldbuilding
Installation
$ npx skills add https://github.com/bs779517/story-skills --skill worldbuilding
SKILL.md
Worldbuilding
Overview

Create and manage world elements for a story project. Locations and systems (magic, politics, technology, etc.) are stored as markdown files in the worldbuilding/ directory with YAML frontmatter. All elements cross-reference characters and other story elements.

Prerequisites

A story project must already exist (created via the story-init skill). Verify by checking for story.md in the project root.

Creating a Location
Read story.md for genre, era, and tone context
Read worldbuilding/_index.md for existing locations and systems
Ask for the location's name and type (city, fortress, wilderness, etc.)
Build the location through conversation, covering:
Physical description and atmosphere
History relevant to the story
Culture and customs of inhabitants
Notable features characters will interact with
Current state at story's timeline
Write the file using references/location-template.md
Save to worldbuilding/locations/{name-kebab}.md
Update worldbuilding/_index.md locations table
If notable characters are listed, verify those character files exist and add location references to them
Creating a System
Read story.md for genre and themes context
Read worldbuilding/_index.md for existing systems
Identify the system type and consult references/world-element-types.md for the relevant prompts
Build the system through conversation, addressing the key questions for that type
Write the file using references/system-template.md
Save to worldbuilding/systems/{name-kebab}.md
Update worldbuilding/_index.md systems table
Cross-reference with characters who interact with the system (e.g., magic-users for a magic system)
Updating World Elements
Read the existing file
Make the requested changes
If cross-references changed, update the linked files
Update worldbuilding/_index.md if name, type, or status changed
Cross-Referencing
Locations reference characters via notable-characters in frontmatter
Systems reference practitioners via character tags
When a location is used in a chapter, the chapter's frontmatter locations field links back
Keep the worldbuilding/_index.md world overview section current as elements are added
Reference Files
references/location-template.md - Template for location files
references/system-template.md - Template for system files
references/world-element-types.md - Detailed prompts for each system type (magic, political, technology, religion, economic, military, social)
Weekly Installs
52
Repository
bs779517/story-skills
GitHub Stars
4
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass