---
rating: ⭐⭐
title: automating-keynote
url: https://skills.sh/spillwavesolutions/automating-mac-apps-plugin/automating-keynote
---

# automating-keynote

skills/spillwavesolutions/automating-mac-apps-plugin/automating-keynote
automating-keynote
Installation
$ npx skills add https://github.com/spillwavesolutions/automating-mac-apps-plugin --skill automating-keynote
SKILL.md
Automating Keynote (JXA-first, AppleScript discovery)
Contents
Relationship to the macOS automation skill
Core framing
Workflow (default)
Quick Examples
What to load
Relationship to the macOS automation skill
This skill focuses on Keynote-specific automation (documents, slides, charts).
Use automating-mac-apps for cross-app workflows or general macOS scripting foundations.
Assumes Apple Events knowledge from the related skill.
PyXA Installation: To use PyXA examples in this skill, see the installation instructions in automating-mac-apps skill (PyXA Installation section).
Core Framing
JXA (JavaScript for Automation) enables macOS app scripting with JavaScript syntax.
AppleScript dictionaries define Keynote's object model—discover via Script Editor.
JXA objects are specifiers: read with methods like .name(), write with assignments.
Production scripts use JXA for reliability; AppleScript for prototyping.
Important: The JXA Path() function is required when specifying file paths to Keynote (e.g., for images, exports, or opening documents). Use Path("/path/to/file") instead of plain strings.
Workflow (default)
Discover terms in Script Editor > File > Open Dictionary > Keynote.
Prototype minimal AppleScript: tell application "Keynote" to get name of document 1.
Port to JXA: Application("Keynote").documents[0].name() with try-catch blocks.
Validate with read-only probes: Application("Keynote").documents.length > 0.
Use UI scripting only when dictionary lacks features (e.g. Application("System Events")).
Quick Examples

Prototype (AppleScript):

tell application "Keynote"
    get name of document 1
end tell


Production (JXA):

const keynote = Application("Keynote");
if (keynote.documents.length > 0) {
    console.log(keynote.documents[0].name());
}


Create Slide:

const doc = keynote.documents[0];
const slide = doc.slides.push(keynote.Slide({baseSlide: doc.masterSlides['Title - Center']}));
slide.defaultTitleItem.objectText = "New Slide";


Add Image to Slide (note Path() usage):

const slide = doc.slides[0];
const img = keynote.Image({
  file: Path("/Users/you/Desktop/diagram.png"),  // Path() required!
  position: { x: 100, y: 100 },
  width: 800
});
slide.images.push(img);

Validation Checklist

After implementing Keynote automation:

 Verify Keynote is running and accessible
 Test slide creation with master slide assignment
 Confirm image paths use Path() function
 Check text rendering in default text items
 Validate export operations complete without errors
When Not to Use
For cross-platform presentation automation (use PowerPoint with Python libraries)
When AppleScript alone suffices (skip JXA complexity)
For web-based presentations (Google Slides, reveal.js)
For non-macOS platforms
What to load
Keynote JXA basics + runtime caveats: automating-keynote/references/keynote-basics.md
Keynote recipes (slides, text, images, export): automating-keynote/references/keynote-recipes.md
Deck generator example: automating-keynote/references/keynote-deck-generator.md
Chart-aware deck pattern: automating-keynote/references/keynote-chart-aware-deck.md
Advanced workflows (charts bridge, magic move, UI scripting): automating-keynote/references/keynote-advanced.md
PyXA (Python) practical examples: automating-keynote/references/keynote-pyxa.md
PyXA API Reference (complete class/method docs): automating-keynote/references/keynote-pyxa-api-reference.md
Weekly Installs
72
Repository
spillwavesoluti…s-plugin
GitHub Stars
29
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykPass