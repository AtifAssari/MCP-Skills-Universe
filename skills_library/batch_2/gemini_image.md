---
title: gemini-image
url: https://skills.sh/johnlindquist/claude/gemini-image
---

# gemini-image

skills/johnlindquist/claude/gemini-image
gemini-image
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill gemini-image
Summary

Analyze images using Gemini's vision capabilities for OCR, UI analysis, and visual understanding.

Supports PNG, JPEG, GIF, and WebP images including screenshots, diagrams, charts, and code snippets
Built-in analysis templates for common tasks: text extraction, code recovery, UI/UX feedback, error diagnosis, and data extraction from charts
Handles single and multiple image comparisons in a single request
Requires Google Generative AI library and valid GEMINI_API_KEY environment variable
SKILL.md
Gemini Image Analysis

Analyze images using Gemini Pro's vision capabilities.

Prerequisites
pip install google-generativeai
export GEMINI_API_KEY=your_api_key

CLI Reference
Basic Image Analysis
# Analyze an image
gemini -m pro -f /path/to/image.png "Describe this image in detail"

# With specific question
gemini -m pro -f screenshot.png "What error message is shown?"

# Multiple images
gemini -m pro -f image1.png -f image2.png "Compare these two images"

Analysis Operations
General Description
gemini -m pro -f image.png "Describe this image comprehensively:
1. Main subject/content
2. Colors and composition
3. Text visible (if any)
4. Context and purpose
5. Notable details"

Extract Text (OCR)
gemini -m pro -f screenshot.png "Extract all text from this image.
Format as plain text, preserving layout where possible.
Include any text in buttons, labels, or UI elements."

Code from Screenshot
gemini -m pro -f code-screenshot.png "Extract the code from this screenshot.
Provide as properly formatted code with correct indentation.
Note any parts that are unclear or partially visible."

UI Analysis
gemini -m pro -f ui-screenshot.png "Analyze this UI:
1. What application/website is this?
2. What page/screen is shown?
3. Main UI elements and their purpose
4. User flow/actions available
5. Any UX issues or suggestions"

Error Analysis
gemini -m pro -f error-screenshot.png "Analyze this error:
1. What error is shown?
2. What is the likely cause?
3. How to fix it?
4. Any related information visible?"

Diagram Understanding
gemini -m pro -f diagram.png "Explain this diagram:
1. What type of diagram is this?
2. Main components and their relationships
3. Data/process flow
4. Key takeaways"

Specific Use Cases
Debug Screenshot
gemini -m pro -f debug-screen.png "I'm debugging an issue. From this screenshot:
1. What is the current state?
2. What errors or warnings are visible?
3. What should I look at?
4. Suggested next steps"

Compare Before/After
gemini -m pro -f before.png -f after.png "Compare these before and after images:
1. What changed?
2. Is this an improvement?
3. Any issues in the 'after' version?
4. Anything missing?"

Design Feedback
gemini -m pro -f design.png "Provide design feedback:
1. Visual hierarchy
2. Color usage
3. Typography
4. Spacing and alignment
5. Accessibility concerns
6. Suggestions for improvement"

Data Extraction
gemini -m pro -f chart.png "Extract data from this chart:
1. Chart type
2. Data series and values
3. Axes labels and ranges
4. Key trends or insights
5. Output as structured data if possible"

Form Analysis
gemini -m pro -f form.png "Analyze this form:
1. Form purpose
2. Fields and their types
3. Required vs optional
4. Validation rules visible
5. UX suggestions"

Workflow Patterns
Screenshot to Issue
# Capture screenshot (macOS)
screencapture -i /tmp/bug.png

# Analyze and format as issue
gemini -m pro -f /tmp/bug.png "Create a bug report from this screenshot:

## Summary
[One-line description]

## Steps to Reproduce
[Inferred from screenshot]

## Expected Behavior
[What should happen]

## Actual Behavior
[What the screenshot shows]

## Environment
[Any visible system info]"

UI to Code
gemini -m pro -f ui-design.png "Generate React component code that recreates this UI:
- Use Tailwind CSS for styling
- Make it responsive
- Include proper TypeScript types
- Add appropriate accessibility attributes"

Documentation
gemini -m pro -f app-screen.png "Write user documentation for this screen:
- What this screen is for
- How to use each feature
- Common tasks
- Tips and notes"

Image Types Supported
PNG, JPEG, GIF, WebP
Screenshots
Photos
Diagrams and charts
UI mockups
Code snippets
Documents
Best Practices
Use clear images - Higher quality = better analysis
Crop to relevant area - Remove unnecessary context
Ask specific questions - Vague prompts get vague answers
Provide context - Tell Gemini what you're looking for
Verify extracted text - OCR isn't perfect
Multiple angles - Use multiple images for complex subjects
Weekly Installs
929
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass