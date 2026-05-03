---
title: accelint-readme-writer
url: https://skills.sh/gohypergiant/agent-skills/accelint-readme-writer
---

# accelint-readme-writer

skills/gohypergiant/agent-skills/accelint-readme-writer
accelint-readme-writer
Installation
$ npx skills add https://github.com/gohypergiant/agent-skills --skill accelint-readme-writer
SKILL.md
README Writer

This skill guides the creation and maintenance of comprehensive, human-friendly README documentation by analyzing the codebase and ensuring documentation stays in sync with actual functionality.

When to Activate This Skill

Use this skill when:

Creating a new README.md for a project or package
Updating an existing README.md after code changes
Auditing documentation for completeness and accuracy
Converting sparse documentation into thorough guides
User asks to "document this package" or "write a README"
User mentions README in context of a monorepo subdirectory
When NOT to Use This Skill

Do not activate for:

API documentation generation (use JSDoc/TSDoc tools)
Changelog or release notes
Internal developer notes not meant for README
Documentation in formats other than Markdown
How to Use
Step 1: Locate the README Context

Identify where the README should live. In monorepos, this determines the scope of codebase analysis:

project-root/           # README here documents entire monorepo
├── packages/
│   └── my-lib/         # README here documents only my-lib
│       └── README.md
└── README.md

Step 2: Analyze the Codebase

Recursively parse code starting from the README's directory:

Identify entry points: Look for index.ts, main.ts, package.json main/exports
Map public API: Find all exported functions, classes, types, constants
Trace dependencies: Understand what the package depends on
Find examples: Look for examples/, test files, or inline usage comments
Check package.json: Extract scripts, dependencies, peer dependencies
Step 3: Compare Against Existing README

If a README exists, identify gaps:

Missing exports: Public API not documented
Stale examples: Code samples using deprecated patterns
Missing sections: No installation, no quick start, no API reference
Outdated commands: Wrong package manager, missing scripts
Step 4: Generate or Update README

Follow the README Structure and apply Writing Principles.

Use the README Template as a starting point for new READMEs.

README Workflow Decision Tree
Start
  ↓
Does README.md exist?
  ├─ No → Analyze codebase → Generate from template
  └─ Yes → Analyze codebase → Compare with existing
             ↓
         Identify gaps and staleness
             ↓
         Suggest specific changes
             ↓
         Apply updates (with user confirmation)

Key References

Load these as needed for detailed guidance:

references/readme-structure.md - Section ordering and content requirements
references/writing-principles.md - How to write human-sounding, thorough docs
references/codebase-analysis.md - How to parse and understand code for documentation
references/readme-template.md - Copy-pasteable template for new READMEs
Example Trigger Phrases
"Create a README for this package"
"Update the README to reflect recent changes"
"The README is out of date, can you fix it?"
"Document this library"
"Write docs for packages/my-lib"
"This package needs better documentation"
Required Skills

This skill requires the humanizer skill for reviewing generated content.

If humanizer is not available:

Check Settings > Capabilities to enable it
Or invoke it with /skill humanizer

The humanizer skill removes AI writing patterns and ensures documentation sounds natural. Without it, generated READMEs may contain robotic language, inflated significance claims, and other AI artifacts.

Important Notes
Package Manager Detection

Always use the correct package manager based on lockfiles:

Lockfile	Package Manager	Install Command
pnpm-lock.yaml	pnpm	pnpm install
package-lock.json	npm	npm install
yarn.lock	yarn	yarn
bun.lockb	bun	bun install
Table of Contents

Include a TOC for READMEs over ~200 lines. Place it after the heading area, before the Installation section.

Human-Sounding Writing

REQUIRED SUB-SKILL: Use humanizer to review and refine generated README content.

Documentation should sound like it was written by someone who genuinely wants to help. The humanizer skill identifies and removes AI writing patterns including:

Inflated significance language ("pivotal", "testament", "crucial")
Promotional/advertisement-like tone
Superficial -ing analyses
Vague attributions and weasel words
Em dash overuse and rule-of-three patterns

After generating README content, apply the humanizer skill to ensure the output sounds natural and human-written. See references/writing-principles.md for additional guidance specific to technical documentation.

Weekly Installs
143
Repository
gohypergiant/ag…t-skills
GitHub Stars
11
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass