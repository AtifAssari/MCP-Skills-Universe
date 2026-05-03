---
title: character-management
url: https://skills.sh/bs779517/story-skills/character-management
---

# character-management

skills/bs779517/story-skills/character-management
character-management
Installation
$ npx skills add https://github.com/bs779517/story-skills --skill character-management
SKILL.md
Character Management
Overview

Create and manage rich character profiles for a story project. Each character is a markdown file with YAML frontmatter in the characters/ directory. Characters are cross-referenced with other story elements through kebab-case identifiers.

Prerequisites

A story project must already exist (created via the story-init skill). Verify by checking for story.md in the project root.

Creating a Character
Read story.md for genre, themes, and tone context
Read characters/_index.md for existing characters
Ask for the character's name and role (protagonist, antagonist, supporting, minor)
Build the profile through conversation, exploring:
Appearance and distinguishing features
Personality, traits, and quirks
Backstory and formative events
Motivations (external wants vs internal needs)
Voice and speech patterns (ask for example dialogue)
Character arc (starting state, turning points, ending state)
Key life events for the timeline
Write the character file using the template in references/character-template.md
Save to characters/{name-kebab}.md
Update characters/_index.md registry table
If relationships reference existing characters, update those character files too
Updating a Character
Read the existing character file
Read characters/_index.md for context on other characters
Make the requested changes
If relationships changed, update the other character's file (bidirectional)
Update characters/_index.md if role or status changed
Managing Relationships

Reference references/relationship-types.md for the full list of relationship types and inverse pairs.

When adding a relationship:

Add the relationship entry to the character's frontmatter
Add the inverse relationship to the other character's frontmatter
Update the Relationship Map section in characters/_index.md
Family Trees

Family trees are maintained in the characters/_index.md under the "Family Trees" section. Format:

## Family Trees

### {Family Name}
- **{Character Name}** ({status}) - [{name-kebab}.md]
  - **{Child Name}** - [{name-kebab}.md]
  - **{Child Name}** - [{name-kebab}.md]


Indent children under parents. Note marriages/partnerships inline.

Cross-Referencing
When a character is referenced in worldbuilding (e.g., a location's notable-characters), ensure the link exists both ways
When a character appears in a plot arc, ensure they're listed in the arc's characters frontmatter
Character tags should be consistent across the project (e.g., if magic-user is used, always use that exact tag)
Reference Files
references/character-template.md - Full blank template for character profiles
references/relationship-types.md - Complete relationship type reference with inverse pairs
Weekly Installs
51
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