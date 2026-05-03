---
title: character-profile-generator
url: https://skills.sh/bizshuk/llm_plugin/character-profile-generator
---

# character-profile-generator

skills/bizshuk/llm_plugin/character-profile-generator
character-profile-generator
Installation
$ npx skills add https://github.com/bizshuk/llm_plugin --skill character-profile-generator
SKILL.md
Character Profile Generator

This skill enables the creation of rich, consistent virtual character profiles by combining a structured template with an interactive discovery process.

Workflow

To generate a character profile, follow these steps:

1. Initial Consultation

Ask the user for basic information about the character (e.g., name, gender, role) and any initial ideas they have.

2. Clarifying Dialogue

Ask 3-5 targeted questions to delve deeper into the character's psyche. Focus on:

Personality & MBTI: How do they react to stress? Are they introverted or extroverted?
Behavior & Habits: Do they have any unique quirks or repetitive actions?
Background & Motivation: What drives them? What is a significant event from their past?
Communication Style: How do they speak? Any specific slang or verbal tics?
3. Profile Generation

Load the template from assets/profile_template.md and populate it using the information gathered.

Use the provided structure strictly.
Expand on the "核心人格特質" (Core Personality Traits) and "說話方式" (Speaking Style) to ensure they are distinctive.
For missing fields not covered in the dialogue, generate creative and consistent details that fit the character's established persona.
Resources
assets/
profile_template.md: The markdown template used as the base for all character profiles.
Weekly Installs
24
Repository
bizshuk/llm_plugin
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass