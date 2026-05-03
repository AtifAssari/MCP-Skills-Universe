---
title: pptx-skill
url: https://skills.sh/404kidwiz/claude-supercode-skills/pptx-skill
---

# pptx-skill

skills/404kidwiz/claude-supercode-skills/pptx-skill
pptx-skill
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill pptx-skill
SKILL.md
PPTX Skill
Purpose

Provides expertise in programmatic PowerPoint presentation creation, editing, and automation. Specializes in using python-pptx (Python) and PptxGenJS (JavaScript) for generating dynamic slide decks and automating presentation workflows.

When to Use
Generating presentations programmatically
Creating slides from data sources
Modifying existing PowerPoint files
Building automated report generators
Adding charts and tables to slides
Applying templates and branding
Extracting content from presentations
Batch processing multiple presentations
Quick Start

Invoke this skill when:

Creating PowerPoint files from code
Automating slide generation
Modifying existing PPTX files
Building presentation templates
Extracting data from slides

Do NOT invoke when:

PDF generation → use /pdf-skill
Word documents → use /docx-skill
Excel files → use /xlsx-skill
Manual presentation design → use appropriate design tools
Decision Framework
PPTX Operation?
├── Generate from Scratch
│   ├── Python → python-pptx
│   └── JavaScript → PptxGenJS
├── Modify Existing
│   └── python-pptx (read + modify)
├── Template-Based
│   └── Load template, fill placeholders
└── Extract Content
    └── python-pptx for reading

Core Workflows
1. Presentation Generation (python-pptx)
Install python-pptx
Create Presentation object
Add slides from layouts
Add content (text, images, tables)
Apply formatting
Save presentation
2. Chart Creation
Prepare data for chart
Create chart data object
Add chart to slide
Configure chart type and options
Style chart elements
Position and size appropriately
3. Template-Based Generation
Create master template with placeholders
Load template in code
Identify placeholder shapes
Replace placeholder content
Add dynamic slides as needed
Save as new file
Best Practices
Use slide layouts from the template
Keep text within placeholder boundaries
Use appropriate chart types for data
Maintain consistent styling
Test output in PowerPoint
Handle missing fonts gracefully
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
Ignoring layouts	Inconsistent formatting	Use slide layouts
Hardcoded positions	Layout breaks	Use placeholders
Too much text per slide	Unreadable	Limit content, use bullets
Missing templates	Reinventing styling	Create reusable templates
No error handling	Corrupted files	Validate and handle errors
Weekly Installs
122
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass