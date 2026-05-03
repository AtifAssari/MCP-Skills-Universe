---
rating: ⭐⭐
title: create-skill
url: https://skills.sh/siviter-xyz/dot-agent/create-skill
---

# create-skill

skills/siviter-xyz/dot-agent/create-skill
create-skill
Installation
$ npx skills add https://github.com/siviter-xyz/dot-agent --skill create-skill
Summary

Comprehensive guide for building modular skills that extend agent capabilities with specialized knowledge and workflows.

Skills are self-contained packages providing specialized workflows, tool integrations, domain expertise, and bundled resources for agents
SKILL.md must stay under 200 lines; use progressive disclosure by splitting detailed content into references/ files to reduce context load and activation time
Structure includes required YAML frontmatter (name, description) and markdown instructions, plus optional bundled resources (scripts, references, assets)
Follow core principles: be concise with every token, set appropriate degrees of freedom in instructions, and test across all target models
SKILL.md
Create Skill

Guide for creating effective skills that extend agent capabilities with specialized knowledge, workflows, and tool integrations.

About Skills

Skills are modular, self-contained packages that extend agent capabilities by providing specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific domains or tasks.

What Skills Provide
Specialized workflows - Multi-step procedures for specific domains
Tool integrations - Instructions for working with specific file formats or APIs
Domain expertise - Company-specific knowledge, schemas, business logic
Bundled resources - Scripts, references, and assets for complex and repetitive tasks
Progressive Disclosure Principle

The 200-line rule is critical. SKILL.md must be under 200 lines. If you need more, split content into references/ files.

Three-Level Loading System
Metadata (name + description) - Always in context (~100 words)
SKILL.md body - When skill triggers (<200 lines, ideally <500 lines for optimal performance)
Bundled resources - As needed by agent (unlimited)
Why Progressive Disclosure Matters
85% reduction in initial context load
Activation times drop from 500ms+ to under 100ms
Agent loads only what's needed, when it's needed
Skills remain maintainable and focused
Skill Structure
skill-name/
├── SKILL.md (required, <200 lines)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code
    ├── references/       - Documentation loaded as needed
    └── assets/           - Files used in output

Core Principles
Concise is Key

The context window is a shared resource. Your skill shares it with everything else the agent needs. Be concise and challenge each piece of information:

Does the agent really need this explanation?
Can I assume the agent knows this?
Does this paragraph justify its token cost?
Set Appropriate Degrees of Freedom
High freedom: Text-based instructions for multiple valid approaches
Medium freedom: Pseudocode or scripts with parameters
Low freedom: Specific scripts with few/no parameters for fragile operations
Test with All Models

Skills act as additions to models, so effectiveness depends on the underlying model. Test your skill with all models you plan to use it with.

References

For detailed guidance, see:

references/progressive-disclosure.md - 200-line rule and references pattern
references/skill-structure.md - SKILL.md format and frontmatter details
references/examples.md - Good skill examples
references/best-practices.md - Comprehensive best practices guide
Weekly Installs
1.8K
Repository
siviter-xyz/dot-agent
GitHub Stars
11
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass