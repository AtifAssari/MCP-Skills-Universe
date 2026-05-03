---
title: example-skill
url: https://skills.sh/uwe-schwarz/skills/example-skill
---

# example-skill

skills/uwe-schwarz/skills/example-skill
example-skill
Installation
$ npx skills add https://github.com/uwe-schwarz/skills --skill example-skill
SKILL.md
Example Skill

This is an example skill that demonstrates how to structure skills for AI coding agents.

When to Apply

Reference these guidelines when:

Creating new skills
Understanding the skill format
Learning best practices for skill development
Core Guidelines
1. Frontmatter Requirements

Every SKILL.md file must include:

name: Unique identifier (lowercase, hyphens for spaces)
description: Clear description of what the skill does and when to use it

Optional fields:

license: License type (e.g., MIT)
metadata: Additional information (author, version, etc.)
2. Content Structure

Organize your skill content with:

Clear headings
Code examples
Use cases
Best practices
3. Script Integration

If your skill includes scripts:

Place them in the scripts/ directory
Make scripts executable
Document usage in this file
4. References

Include supporting documentation in:

The references/ directory
Links to external resources
Relevant documentation
Example Usage
# Using the skill in a conversation
"Use the example-skill to help me create a new skill"

Best Practices
Keep descriptions clear and concise
Use specific examples
Document edge cases
Include troubleshooting steps
Sub-rules

If your skill is complex, you can break it down into sub-rules in the rules/ directory:

Create separate markdown files for each rule
Reference them from this main SKILL.md
Use descriptive filenames (e.g., rule-name.md)
Weekly Installs
8
Repository
uwe-schwarz/skills
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass