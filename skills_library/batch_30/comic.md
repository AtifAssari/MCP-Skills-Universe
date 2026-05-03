---
title: comic
url: https://skills.sh/zlh-428/naruto-skills/comic
---

# comic

skills/zlh-428/naruto-skills/comic
comic
Installation
$ npx skills add https://github.com/zlh-428/naruto-skills --skill comic
SKILL.md
Knowledge Comic Creator

Create original knowledge comics with multiple visual styles.

Usage
/comic posts/turing-story/source.md
/comic  # then paste content

Options
Option	Values
--style	classic (default), dramatic, warm, sepia, vibrant, ohmsha, realistic, wuxia, shoujo, or custom description
--layout	standard (default), cinematic, dense, splash, mixed, webtoon
--aspect	3:4 (default, portrait), 4:3 (landscape), 16:9 (widescreen)
--lang	auto (default), zh, en, ja, etc.

Style × Layout × Aspect can be freely combined. Custom styles can be described in natural language.

Aspect ratio is consistent across all pages in a comic.

Auto Selection
Content Signals	Style	Layout
Tutorial, how-to, beginner	ohmsha	webtoon
Computing, AI, programming	ohmsha	dense
Pre-1950, classical, ancient	sepia	cinematic
Personal story, mentor	warm	standard
Conflict, breakthrough	dramatic	splash
Wine, food, business, lifestyle, professional	realistic	cinematic
Martial arts, wuxia, xianxia, Chinese historical	wuxia	splash
Romance, love, school life, friendship, emotional	shoujo	standard
Biography, balanced	classic	mixed
Script Directory

Important: All scripts are located in scripts/ subdirectory of this skill.

Agent Execution Instructions:

Determine this SKILL.md file's directory path as SKILL_DIR
Script path = ${SKILL_DIR}/scripts/<script-name>.ts
Replace all ${SKILL_DIR} in this document with actual path

Script Reference:

Script	Purpose
scripts/merge-to-pdf.ts	Merge comic pages into PDF
File Structure

Each session creates an independent directory named by content slug:

comic/{topic-slug}/
├── source-{slug}.{ext}            # Source files (text, images, etc.)
├── analysis.md                    # Deep analysis results (YAML+MD)
├── storyboard-chronological.md    # Variant A (preserved)
├── storyboard-thematic.md         # Variant B (preserved)
├── storyboard-character.md        # Variant C (preserved)
├── characters-chronological/      # Variant A chars (preserved)
│   ├── characters.md
│   └── characters.png
├── characters-thematic/           # Variant B chars (preserved)
│   ├── characters.md
│   └── characters.png
├── characters-character/          # Variant C chars (preserved)
│   ├── characters.md
│   └── characters.png
├── storyboard.md                  # Final selected
├── characters/                    # Final selected
│   ├── characters.md
│   └── characters.png
├── prompts/
│   ├── 00-cover-[slug].md
│   └── NN-page-[slug].md
├── 00-cover-[slug].png
├── NN-page-[slug].png
└── {topic-slug}.pdf


Slug Generation:

Extract main topic from content (2-4 words, kebab-case)
Example: "Alan Turing Biography" → alan-turing-bio

Conflict Resolution: If comic/{topic-slug}/ already exists:

Append timestamp: {topic-slug}-YYYYMMDD-HHMMSS
Example: turing-story exists → turing-story-20260118-143052

Source Files: Copy all sources with naming source-{slug}.{ext}:

source-biography.md, source-portrait.jpg, source-timeline.png, etc.
Multiple sources supported: text, images, files from conversation
Workflow
Step 1: Analyze Content → analysis.md

Read source content, save it if needed, and perform deep analysis.

Actions:

Save source content (if not already a file):
If user provides a file path: use as-is
If user pastes content: save to source.md in target directory
Read source content
Deep analysis following references/analysis-framework.md:
Target audience identification
Value proposition for readers
Core themes and narrative potential
Key figures and their story arcs
Detect source language
Determine recommended page count:
Short story: 5-8 pages
Medium complexity: 9-15 pages
Full biography: 16-25 pages
Analyze content signals for style/layout recommendations
Save to analysis.md

analysis.md Format:

---
title: "Alan Turing: Father of Computing"
topic: Biography
time_span: 1912-1954
source_language: en
user_language: zh
aspect_ratio: "3:4"
recommended_page_count: 12
---

## Target Audience

- **Primary**: Tech enthusiasts curious about computing history
- **Secondary**: Students learning about scientific breakthroughs
- **Tertiary**: General readers interested in biographical stories

## Value Proposition

What readers will gain:
1. Understanding of how modern computing was born
2. Emotional connection to a brilliant but tragic figure
3. Appreciation for human cost of innovation

## Core Themes

| Theme | Narrative Potential | Visual Opportunity |
|-------|--------------------|--------------------|
| Genius vs. Society | High conflict, dramatic arcs | Contrast scenes |
| Code-breaking | Mystery, tension | Technical diagrams as art |
| Personal tragedy | Emotional depth | Intimate, somber panels |

## Key Figures & Story Arcs

### Alan Turing (Protagonist)
- **Arc**: Misunderstood genius → War hero → Tragic end
- **Visual identity**: Disheveled academic, intense eyes
- **Key moments**: Enigma breakthrough, arrest, final days

### Christopher Morcom (Catalyst)
- **Role**: Early friend whose death shaped Turing
- **Visual identity**: Youthful, bright
- **Key moments**: School friendship, sudden death

## Content Signals

- "biography" → classic + mixed
- "computing history" → ohmsha + dense
- "personal tragedy" → dramatic + splash

## Recommended Approaches

1. **Chronological** - follow life timeline (recommended for biography)
2. **Thematic** - organize by contributions (good for educational focus)
3. **Character-focused** - relationships drive narrative (good for emotional impact)

Step 2: Generate 3 Storyboard Variants

Create three distinct variants, each combining a narrative approach with a recommended style.

Variant	Narrative Approach	Recommended Style	Layout
A	Chronological	sepia	cinematic
B	Thematic	ohmsha	dense
C	Character-focused	warm	standard

For each variant:

Generate storyboard (storyboard-{approach}.md):

YAML front matter with narrative_approach, recommended_style, recommended_layout, aspect_ratio
Cover design
Each page: layout, panel breakdown, visual prompts
Written in user's preferred language
Reference: references/storyboard-template.md

Generate matching characters (characters-{approach}/):

characters.md - visual specs matching recommended style (in user's preferred language)
characters.png - character reference sheet
Reference: references/character-template.md

All variants are preserved after selection for reference.

Step 3: User Confirms All Options

IMPORTANT: Present ALL options in a single confirmation step using AskUserQuestion. Do NOT interrupt workflow with multiple separate confirmations.

Determine which questions to ask:

Question	When to Ask
Storyboard variant	Always (required)
Visual style	Always (required)
Language	Only if source_language ≠ user_language
Aspect ratio	Only if user might prefer non-default (e.g., landscape content)

Language handling:

If source language = user language: Just inform user (e.g., "Comic will be in Chinese")
If different: Ask which language to use

All storyboards and prompts are generated in user's selected/preferred language.

Aspect ratio handling:

Default: 3:4 (portrait) - standard comic format
Offer 4:3 (landscape) if content suits it (e.g., panoramic scenes, technical diagrams)
Offer 16:9 (widescreen) for cinematic content

AskUserQuestion format (example with all questions):

Question 1 (Storyboard): Which storyboard variant?
- A: Chronological + sepia (Recommended)
- B: Thematic + ohmsha
- C: Character-focused + warm
- Custom

Question 2 (Style): Which visual style?
- sepia (Recommended from variant)
- classic / dramatic / warm / sepia / vibrant / ohmsha / realistic / wuxia
- Custom description

Question 3 (Language) - only if mismatch:
- Chinese (source material language)
- English (your preference)

Question 4 (Aspect) - only if relevant:
- 3:4 Portrait (Recommended)
- 4:3 Landscape
- 16:9 Widescreen


After confirmation:

Copy selected storyboard → storyboard.md
Copy selected characters → characters/
Update YAML front matter with confirmed style, language, aspect_ratio
If style differs from variant's recommended: regenerate characters/characters.png
User may edit files directly for fine-tuning
Step 4: Generate Images

With confirmed storyboard + style + aspect ratio:

For each page (cover + pages):

Save prompt to prompts/NN-{cover|page}-[slug].md (in user's preferred language)
Generate image using confirmed style and aspect ratio
Report progress after each generation

Image Generation Skill Selection:

Check available image generation skills
If multiple skills available, ask user preference

Character Reference Handling:

If skill supports reference image: pass characters/characters.png
If skill does NOT support reference image: include characters/characters.md content in prompt

Session Management: If image generation skill supports --sessionId:

Generate unique session ID: comic-{topic-slug}-{timestamp}
Use same session ID for all pages
Ensures visual consistency across generated images
Step 5: Merge to PDF

After all images generated:

npx -y bun ${SKILL_DIR}/scripts/merge-to-pdf.ts <comic-dir>


Creates {topic-slug}.pdf with all pages as full-page images.

Step 6: Completion Report
Comic Complete!
Title: [title] | Style: [style] | Pages: [count] | Aspect: [ratio] | Language: [lang]
Location: [path]
✓ analysis.md
✓ characters.png
✓ 00-cover-[slug].png ... NN-page-[slug].png
✓ {topic-slug}.pdf

Page Modification

Support for modifying individual pages after initial generation.

Edit Single Page

Regenerate a specific page with modified prompt:

Identify page to edit (e.g., 03-page-enigma-machine.png)
Update prompt in prompts/03-page-enigma-machine.md if needed
If content changes significantly, update slug in filename
Regenerate image using same session ID and aspect ratio
Regenerate PDF
Add New Page

Insert a new page at specified position:

Specify insertion position (e.g., after page 3)
Create new prompt with appropriate slug (e.g., 04-page-bletchley-park.md)
Generate new page image (same aspect ratio)
Renumber files: All subsequent pages increment NN by 1
04-page-tragedy.png → 05-page-tragedy.png
Slugs remain unchanged
Update storyboard.md with new page entry
Regenerate PDF
Delete Page

Remove a page and renumber:

Identify page to delete (e.g., 03-page-enigma-machine.png)
Remove image file and prompt file
Renumber files: All subsequent pages decrement NN by 1
04-page-tragedy.png → 03-page-tragedy.png
Slugs remain unchanged
Update storyboard.md to remove page entry
Regenerate PDF
File Naming Convention

Files use meaningful slugs for better readability:

NN-cover-[slug].png / NN-page-[slug].png
NN-cover-[slug].md / NN-page-[slug].md (in prompts/)


Examples:

00-cover-turing-story.png
01-page-early-life.png
02-page-cambridge-years.png
03-page-enigma-machine.png

Slug rules:

Derived from page title/content (kebab-case)
Must be unique within comic
When page content changes significantly, update slug accordingly

Renumbering:

After add/delete, update NN prefix for affected pages
Slug remains unchanged unless content changes
Maintain sequential numbering with no gaps
Style-Specific Guidelines
Ohmsha Style (--style ohmsha)

Additional requirements for educational manga:

Default: Use Doraemon characters directly - No need to create new characters
大雄 (Nobita): Student role, curious learner
哆啦A梦 (Doraemon): Mentor role, explains concepts with gadgets
胖虎 (Gian): Antagonist/challenge role, represents obstacles or misconceptions
静香 (Shizuka): Supporting role, asks clarifying questions
Custom characters only if explicitly requested: --characters "Student:小明,Mentor:教授"
Must use visual metaphors (gadgets, action scenes) - NO talking heads
Page titles: narrative style, not "Page X: Topic"

Reference: references/ohmsha-guide.md for detailed guidelines.

References

Detailed templates and guidelines in references/ directory:

analysis-framework.md - Deep content analysis for comic adaptation
character-template.md - Character definition format and examples
storyboard-template.md - Storyboard structure and panel breakdown
ohmsha-guide.md - Ohmsha manga style specifics
styles/ - Detailed style definitions
layouts/ - Detailed layout definitions
Extension Support

Custom styles and configurations via EXTEND.md.

Check paths (priority order):

.content-gen-skills/comic/EXTEND.md (project)
~/.content-gen-skills/comic/EXTEND.md (user)

If found, load before Step 1. Extension content overrides defaults.

Weekly Installs
21
Repository
zlh-428/naruto-skills
GitHub Stars
3
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass