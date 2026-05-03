---
title: create-skill
url: https://skills.sh/jasonharmongit/jh-skills/create-skill
---

# create-skill

skills/jasonharmongit/jh-skills/create-skill
create-skill
Installation
$ npx skills add https://github.com/jasonharmongit/jh-skills --skill create-skill
SKILL.md
Creating Skills in Cursor

This skill guides you through creating effective Agent Skills for Cursor. Skills are markdown files that teach the agent how to perform specific tasks: reviewing PRs using team standards, generating commit messages in a preferred format, querying database schemas, or any specialized workflow.

Before You Begin: Gather Requirements

Before creating a skill, gather essential information from the user about:

Purpose and scope: What specific task or workflow should this skill help with?
Target location: Should this be a personal skill (~/.cursor/skills/) or project skill (.cursor/skills/)?
Trigger scenarios: When should the agent automatically apply this skill?
Key domain knowledge: What specialized information does the agent need that it wouldn't already know?
Output format preferences: Are there specific templates, formats, or styles required?
Existing patterns: Are there existing examples or conventions to follow?
Inferring from Context

If you have previous conversation context, infer the skill from what was discussed. You can create skills based on workflows, patterns, or domain knowledge that emerged in the conversation.

Gathering Additional Information

If you need clarification, use the AskQuestion tool when available:

Example AskQuestion usage:
- "Where should this skill be stored?" with options like ["Personal (~/.cursor/skills/)", "Project (.cursor/skills/)"]
- "Should this skill include executable scripts?" with options like ["Yes", "No"]


If the AskQuestion tool is not available, ask these questions conversationally.

Skill File Structure
Directory Layout

Skills are stored as directories containing a SKILL.md file:

skill-name/
├── SKILL.md              # Required - main instructions
├── reference.md          # Optional - detailed documentation
├── examples.md           # Optional - usage examples
└── scripts/              # Optional - utility scripts
    ├── validate.py
    └── helper.sh

Core Authoring Principles
1. Concise is Key

The context window is shared with conversation history, other skills, and requests. Every token competes for space.

Default assumption: The agent is already very smart. Only add context it doesn't already have.

Challenge each piece of information:

"Does the agent really need this explanation?"
"Can I assume the agent knows this?"
"Does this paragraph justify its token cost?"

Good (concise):

## Extract PDF text

Use pdfplumber for text extraction:

\`\`\`python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
\`\`\`


Bad (verbose):

## Extract PDF text

PDF (Portable Document Format) files are a common file format that contains
text, images, and other content. To extract text from a PDF, you'll need to
use a library. There are many libraries available for PDF processing, but we
recommend pdfplumber because it's easy to use and handles most cases well...

2. Keep SKILL.md Under 500 Lines

For optimal performance, the main SKILL.md file should be concise. Use progressive disclosure for detailed content.

3. Progressive Disclosure

Put essential information in SKILL.md; detailed reference material in separate files that the agent reads only when needed.

# PDF Processing

## Quick start
[Essential instructions here]

## Additional resources
- For complete API details, see [reference.md](reference.md)
- For usage examples, see [examples.md](examples.md)


Keep references one level deep - link directly from SKILL.md to reference files. Deeply nested references may result in partial reads.

4. Set Appropriate Degrees of Freedom

Match specificity to the task's fragility:

Freedom Level	When to Use	Example
High (text instructions)	Multiple valid approaches, context-dependent	Code review guidelines
Medium (pseudocode/templates)	Preferred pattern with acceptable variation	Report generation
Low (specific scripts)	Fragile operations, consistency critical	Database migrations
Utility Scripts

Pre-made scripts offer advantages over generated code:

More reliable than generated code
Save tokens (no code in context)
Save time (no code generation)
Ensure consistency across uses
## Utility scripts

**analyze_form.py**: Extract all form fields from PDF
\`\`\`bash
python scripts/analyze_form.py input.pdf > fields.json
\`\`\`

**validate.py**: Check for errors
\`\`\`bash
python scripts/validate.py fields.json
# Returns: "OK" or lists conflicts
\`\`\`


Make clear whether the agent should execute the script (most common) or read it as reference.

Anti-Patterns to Avoid
1. Windows-Style Paths
✅ Use: scripts/helper.py
❌ Avoid: scripts\helper.py
2. Too Many Options
# Bad - confusing
"You can use pypdf, or pdfplumber, or PyMuPDF, or..."

# Good - provide a default with escape hatch
"Use pdfplumber for text extraction.
For scanned PDFs requiring OCR, use pdf2image with pytesseract instead."

3. Time-Sensitive Information
# Bad - will become outdated
"If you're doing this before August 2025, use the old API."

# Good - use an "old patterns" section
## Current method
Use the v2 API endpoint.

## Old patterns (deprecated)
<details>
<summary>Legacy v1 API</summary>
...
</details>

4. Inconsistent Terminology

Choose one term and use it throughout:

✅ Always "API endpoint" (not mixing "URL", "route", "path")
✅ Always "field" (not mixing "box", "element", "control")
5. Vague Skill Names
✅ Good: processing-pdfs, analyzing-spreadsheets
❌ Avoid: helper, utils, tools
Skill Creation Workflow

When helping a user create a skill, follow this process:

Phase 1: Discovery

Gather information about:

The skill's purpose and primary use case
Storage location (personal vs project)
Trigger scenarios
Any specific requirements or constraints
Existing examples or patterns to follow

If you have access to the AskQuestion tool, use it for efficient structured gathering. Otherwise, ask conversationally.

Phase 2: Design
Draft the skill name (lowercase, hyphens, max 64 chars)
Write a specific, third-person description
Outline the main sections needed
Identify if supporting files or scripts are needed
Phase 3: Implementation
Create the directory structure
Write the SKILL.md file with frontmatter
Create any supporting reference files
Create any utility scripts if needed
Phase 4: Verification
Verify the SKILL.md is under 500 lines
Check that the description is specific and includes trigger terms
Ensure consistent terminology throughout
Verify all file references are one level deep
Test that the skill can be discovered and applied
Weekly Installs
14
Repository
jasonharmongit/jh-skills
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass