---
rating: ⭐⭐⭐
title: tuzi-article-illustrator
url: https://skills.sh/tuziapi/tuzi-skills/tuzi-article-illustrator
---

# tuzi-article-illustrator

skills/tuziapi/tuzi-skills/tuzi-article-illustrator
tuzi-article-illustrator
Installation
$ npx skills add https://github.com/tuziapi/tuzi-skills --skill tuzi-article-illustrator
SKILL.md
Article Illustrator

Analyze articles, identify illustration positions, generate images with Type × Style consistency.

Two Dimensions
Dimension	Controls	Examples
Type	Information structure	infographic, scene, flowchart, comparison, framework, timeline
Style	Visual aesthetics	notion, warm, minimal, blueprint, watercolor, elegant

Combine freely: --type infographic --style blueprint

Types
Type	Best For
infographic	Data, metrics, technical
scene	Narratives, emotional
flowchart	Processes, workflows
comparison	Side-by-side, options
framework	Models, architecture
timeline	History, evolution
Styles

See references/styles.md for Core Styles, full gallery, and Type × Style compatibility.

Workflow
- [ ] Step 1: Pre-check (EXTEND.md, references, config)
- [ ] Step 2: Analyze content
- [ ] Step 3: Confirm settings (AskUserQuestion)
- [ ] Step 4: Generate outline
- [ ] Step 5: Generate images
- [ ] Step 6: Finalize

Step 1: Pre-check

1.5 Load Preferences (EXTEND.md) ⛔ BLOCKING

test -f .tuzi-skills/tuzi-article-illustrator/EXTEND.md && echo "project"
test -f "$HOME/.tuzi-skills/tuzi-article-illustrator/EXTEND.md" && echo "user"

Result	Action
Found	Read, parse, display summary
Not found	⛔ Run first-time-setup

Full procedures: references/workflow.md

Step 2: Analyze
Analysis	Output
Content type	Technical / Tutorial / Methodology / Narrative
Purpose	information / visualization / imagination
Core arguments	2-5 main points
Positions	Where illustrations add value

CRITICAL: Metaphors → visualize underlying concept, NOT literal image.

Full procedures: references/workflow.md

Step 3: Confirm Settings ⚠️

ONE AskUserQuestion, max 4 Qs. Q1-Q3 REQUIRED.

Q	Options
Q1: Type	[Recommended], infographic, scene, flowchart, comparison, framework, timeline, mixed
Q2: Density	minimal (1-2), balanced (3-5), per-section (Recommended), rich (6+)
Q3: Style	[Recommended], minimal-flat, sci-fi, hand-drawn, editorial, scene, Other
Q4: Language	When article language ≠ EXTEND.md setting

Full procedures: references/workflow.md

Step 4: Generate Outline

Save outline.md with frontmatter (type, density, style, image_count) and entries:

## Illustration 1
**Position**: [section/paragraph]
**Purpose**: [why]
**Visual Content**: [what]
**Filename**: 01-infographic-concept-name.png


Full template: references/workflow.md

Step 5: Generate Images

⛔ BLOCKING: Prompt files MUST be saved before ANY image generation.

For each illustration, create a prompt file per references/prompt-construction.md
Save to prompts/NN-{type}-{slug}.md with YAML frontmatter
Prompts MUST use type-specific templates with structured sections (ZONES / LABELS / COLORS / STYLE / ASPECT)
LABELS MUST include article-specific data: actual numbers, terms, metrics, quotes
DO NOT pass ad-hoc inline prompts to --prompt without saving prompt files first
Select generation skill, process references (direct/style/palette)
Apply watermark if EXTEND.md enabled
Generate from saved prompt files; retry once on failure

Full procedures: references/workflow.md

Step 6: Finalize

Insert ![description](path/NN-{type}-{slug}.png) after paragraphs.

Article Illustration Complete!
Article: [path] | Type: [type] | Density: [level] | Style: [style]
Images: X/N generated

Output Directory
illustrations/{topic-slug}/
├── source-{slug}.{ext}
├── references/           # if provided
├── outline.md
├── prompts/
└── NN-{type}-{slug}.png


Slug: 2-4 words, kebab-case. Conflict: append -YYYYMMDD-HHMMSS.

Modification
Action	Steps
Edit	Update prompt → Regenerate → Update reference
Add	Position → Prompt → Generate → Update outline → Insert
Delete	Delete files → Remove reference → Update outline
References
File	Content
references/workflow.md	Detailed procedures
references/usage.md	Command syntax
references/styles.md	Style gallery
references/prompt-construction.md	Prompt templates
references/config/first-time-setup.md	First-time setup
Weekly Installs
121
Repository
tuziapi/tuzi-skills
GitHub Stars
33
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass