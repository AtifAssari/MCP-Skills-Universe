---
title: markdown-slides
url: https://skills.sh/jykim/claude-obsidian-skills/markdown-slides
---

# markdown-slides

skills/jykim/claude-obsidian-skills/markdown-slides
markdown-slides
Installation
$ npx skills add https://github.com/jykim/claude-obsidian-skills --skill markdown-slides
SKILL.md
Markdown Slides Skill

Convert content to presentation slides in Markdown format compatible with Deckset and Marp presentation tools.

When to Use This Skill

Activate this skill when the user:

Asks to create slides or a presentation
Requests to convert a document to slide format
Mentions Deckset or Marp
Wants to generate speaker notes
Needs to format images for presentations
Input Requirements
Source content: Markdown file, outline, or structured content
Images: Files in _files_/ directory or paths to be resolved
Target platform: Deckset (default) or Marp
Options:
Speaker notes (enabled by default)
Slide numbering (optional frontmatter)
Emoji enhancement (enabled by default)
Output Specifications
File location: Same folder as source
File naming: Original name with - slides suffix
Example: document.md → document - slides.md
Format: Deckset-compatible markdown
Structure: Proper slide dividers, image tags, speaker notes
Enhancement: Emojis added for visual appeal
Main Process
Step 1: Slide Structure Setup

Objective: Create logical slide divisions with proper hierarchy

Actions:

Read and analyze source content structure
Insert slide dividers (---) at logical breaks:
Between major sections
Between distinct topics
After section intro slides
Before/after major diagrams
Maintain content hierarchy:
H1 (#) for section titles
H2 (##) for main slide titles
H3 (###) for sub-topics
Preserve original organization and flow
Add optional frontmatter: slidenumbers: true

Example:

slidenumbers: true
# 1. Section Title 🎯

![](section-background.png)

^ Introduction to this section.

---

## Main Topic 📊

Content here...

---

### Detailed Subtopic

More details...

Step 2: Image Format Conversion

Objective: Convert images to Deckset format with proper positioning

Critical Requirements: ⚠️ MUST resolve relative paths per-image basis ⚠️ MUST URL-encode spaces and escape special characters ⚠️ MUST verify image files exist

Image Position Formats:

Format	Usage	Example
![]()	Section intro backgrounds	![](background.png)
![inline]()	Diagrams within text flow	![inline](diagram.svg)
![right fit]()	PRIMARY: Content slides	![right fit](chart.png)
![right 80%]()	Specific sizing needed	![right 80%](image.png)
![inline fill]()	Full-width inline	![inline fill](wide.png)

Actions:

Identify all image references in source
For each image:
a. Determine appropriate position format
b. Resolve relative path from slide file location
c. URL-encode spaces: " " → "%20"
d. Escape parentheses: "(" → "%28", ")" → "%29"
e. Verify file exists at resolved path
f. Use original images when available
g. Copy missing images to _files_/ directory

Apply positioning based on context:
Section intros: Use ![]() for full background
Diagrams in text: Use ![inline]()
Default for content slides: Use ![right fit]() ⭐
Custom sizing: Use ![right XX%]() when needed
Full-width inline: Use ![inline fill]() for wide images

Examples:

# Section Title
![](background-image.png)

---

## Content Slide
Key points here:
- Point 1
- Point 2

![right fit](diagram.png)

---

## Inline Diagram
Text before diagram.

![inline](process-flow.svg)

Text after diagram.

Step 3: Speaker Notes Conversion

Objective: Convert appropriate content to speaker notes

Format: Lines starting with ^ (caret + space)

Placement: At the end of each slide

Convert to speaker notes: ✅ Multi-sentence paragraphs ✅ Explanatory text ✅ Additional context ✅ Talking points

DO NOT convert: ❌ Single-sentence paragraphs ❌ Lists (bullet or numbered) ❌ Block quotes ❌ Sentences ending with colon (:) ❌ Headers (H1, H2, H3) ❌ Table content

For Marp platform: Use HTML comments instead

<!-- This is a speaker note for Marp -->


Examples:

## Slide Title

Main content visible to audience.

^ This paragraph becomes a speaker note because it's multi-sentence explanatory text. It provides context that the speaker needs but the audience doesn't need to read on the slide.

---

## Another Slide

- Bullet points stay visible
- Not converted to notes

^ Additional speaking points go here.

Step 4: Content Enhancement

Objective: Polish the presentation for maximum impact

Actions:

Add emojis to section and slide titles:

Use relevant emojis that enhance meaning
Don't overuse - keep it professional
Examples: 🎯📊🤖💡🚀📚🔧⚡

Clean up comments:

Remove markdown comments not meant for slides
Remove TODO items
Remove internal notes

Ensure clean format:

Consistent spacing
Proper header hierarchy
Clear slide breaks

Add frontmatter (if requested):

slidenumbers: true


Final review:

Each slide has clear focus
Images positioned correctly
Speaker notes placed at end
No orphaned content
Critical Guidelines
Image Handling

⚠️ CRITICAL RULES:

NEVER invent images - Only reference images that exist in the source document or _files_/ folder. Do NOT create placeholder references like background-xxx.png for images that don't exist.
Use original images from source when available
Copy missing images to _files_/ directory rather than substituting
Resolve paths per-image - don't assume same directory
URL-encode spaces: my file.png → my%20file.png
Escape special characters:
Parentheses: ( → %28, ) → %29
Other special chars as needed
Verify existence before referencing - run ls or glob to confirm file exists
Maintain semantic relevance - image should match slide content
Section intros without images are OK - If no background image exists for a section intro slide, just use the title and speaker notes without an image reference
Image Position Standards

Decision tree for image positioning:

Is it a section intro slide with just title?
  → Does a background image exist?
    → YES: Use ![]() for full background
    → NO: Skip image, use title + speaker notes only

Is it a diagram embedded in flowing text?
  → YES: Use ![inline]() or ![inline fill]()

Is it the main visual for the slide with bullet points?
  → YES: Use ![right fit]() ⭐ PRIMARY FORMAT

Does it need specific sizing?
  → YES: Use ![right 80%]() or other percentage

Speaker Notes Rules

When to convert to speaker notes:

Multi-sentence explanatory paragraphs
Contextual information not needed on slide
Talking points for the speaker
Additional details for verbal explanation

When NOT to convert:

Single-sentence paragraphs (might be slide content)
Bullet or numbered lists (usually slide content)
Block quotes (usually featured content)
Sentences ending with : (usually introducing lists)
Any header level
Table content

Format:

Slide content here.

^ Speaker note paragraph one. Can be multiple sentences providing context.

^ Speaker note paragraph two. Each note paragraph gets its own ^ prefix.

Content Standards

File Naming:

Always use - slides suffix
Preserve original filename otherwise
Example: AI for PKM.md → AI for PKM - slides.md

Emoji Usage:

Add to H1 and H2 headers
Choose relevant, professional emojis
Don't overuse - quality over quantity
Examples:
🎯 Goals/Objectives
📊 Data/Charts
🤖 AI/Technology
💡 Ideas/Insights
🚀 Future/Launch
📚 Learning/Knowledge

Hierarchy:

H1 for major sections (usually numbered)
H2 for main slide titles
H3 for subtopics within slides
Consistent numbering scheme

Slide Breaks:

Use --- (three dashes) on its own line
Blank line before and after recommended
Logical breaks between topics
Platform-Specific Notes
Deckset (Default)

Format:

Speaker notes: ^ prefix on each line
Image positioning: All formats fully supported
Frontmatter: Simple key-value pairs

Features:

Automatic slide numbering with slidenumbers: true
Full control over image positioning
Rich presenter notes support

Example Frontmatter:

slidenumbers: true
autoscale: true
theme: Plain Jane, 3

Marp (Optional)

Format:

Speaker notes: HTML comments <!-- speaker note -->
Image positioning: May use different syntax
Frontmatter: YAML with marp: true

Conversion for Marp:

---
marp: true
paginate: true
---

<!-- This is a speaker note in Marp -->


Differences:

HTML comments instead of ^ prefix
Different frontmatter structure
May need ![bg]() for backgrounds instead of ![]()
Quality Checklist

Before marking task complete, verify:

 No invented images - every image reference points to a real file
 All images have valid, URL-encoded paths
 Image files exist at specified locations (run ls to confirm)
 Spaces in paths converted to %20
 Special characters properly escaped
 Speaker notes use ^ prefix (or HTML for Marp)
 Speaker notes placed at END of each slide
 Slide dividers (---) at logical breaks
 Consistent header hierarchy (H1 → H2 → H3)
 Emojis added appropriately to titles
 File saved with '- slides' suffix
 Content hierarchy maintained from source
 No orphaned content or broken sections
 Internal comments removed
 Frontmatter added if requested
Error Handling
Missing Images

Problem: Source references image that doesn't exist

Solution:

Check source _files_/ directory
Check parent directory _files_/
Search for image by name in project
If found: Copy to presentation _files_/ directory
If not found: Note in speaker notes and skip image
Broken Relative Paths

Problem: Path doesn't resolve correctly

Solution:

Determine slide file location
Calculate relative path from slide to image
Test path resolution
URL-encode the working path
Invalid Characters in Paths

Problem: Special characters break image links

Solution:

Spaces: Convert to %20
Parentheses: ( → %28, ) → %29
Brackets: [ → %5B, ] → %5D
Other special chars: Use URL encoding
Tips for Best Results
Start with outline: Create clear section and slide structure first
One idea per slide: Each slide should have single clear message
Visual hierarchy: Use H1 for sections, H2 for slides, H3 for sub-points
Image positioning: Default to ![right fit]() for content slides
Speaker notes: Add context that helps speaker but clutters slide
Emoji consistency: Use similar emojis for similar concepts
Test in Deckset: Preview the slides to verify formatting
Iterate: First pass for structure, second for polish
Weekly Installs
39
Repository
jykim/claude-ob…n-skills
GitHub Stars
43
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass