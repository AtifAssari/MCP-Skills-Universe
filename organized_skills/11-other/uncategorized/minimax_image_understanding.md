---
rating: ⭐⭐
title: minimax-image-understanding
url: https://skills.sh/imsus/pi-extension-minimax-coding-plan-mcp/minimax-image-understanding
---

# minimax-image-understanding

skills/imsus/pi-extension-minimax-coding-plan-mcp/minimax-image-understanding
minimax-image-understanding
Installation
$ npx skills add https://github.com/imsus/pi-extension-minimax-coding-plan-mcp --skill minimax-image-understanding
SKILL.md
MiniMax Image Understanding Skill

Use this skill when you need to analyze, describe, or extract information from images.

How to Use

Call the understand_image tool directly with a prompt and image URL:

understand_image({
  prompt: "Your question about the image",
  image_url: "https://example.com/image.png"
})

When to Use

Use understand_image when:

Screenshots: Error messages, UI issues, code in screenshots
Visual content: Photos, diagrams, charts, graphs
Documents: Extracting text from images (OCR), understanding layouts
UI/UX analysis: Evaluating designs, identifying components
Visual debugging: Understanding visual bugs or layout issues
When NOT to Use

Do NOT use understand_image when:

Image is already described in the conversation
The image is a simple icon or emoji you recognize
No image is provided or the image URL is inaccessible
Redundant with existing context (e.g., file contents already visible)
Usage
understand_image({
  prompt: "What do you see in this image?",
  image_url: "https://example.com/screenshot.png"
})

API Details

Endpoint: POST {api_host}/v1/coding_plan/vlm

Request Body:

{
  "prompt": "Your question about the image",
  "image_url": "data:image/jpeg;base64,/9j/4AAQ..."
}


Response Format:

{
  "content": "AI analysis of the image...",
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  }
}

Image Processing

The tool automatically handles three types of image inputs:

HTTP/HTTPS URLs: Downloads the image and converts to base64

Example: https://example.com/image.jpg

Local file paths: Reads local files and converts to base64

Absolute: /Users/username/Documents/image.png
Relative: images/photo.png
Removes @ prefix if present

Base64 data URLs: Passes through existing base64 data

Example: data:image/png;base64,iVBORw0KGgo...
Image Formats

Supported:

JPEG (.jpg, .jpeg)
PNG (.png)
WebP (.webp)

Not supported:

PDF, GIF, PSD, SVG, and other formats
Crafting Effective Prompts
For Descriptions
"Describe what's in this image in detail"
"What is the main subject of this image?"
"Describe the visual style and composition"
For Code/Technical
"What code is shown in this screenshot?"
"Extract all text from this image"
"Identify the UI framework/components used"
For Analysis
"Analyze this UI design. What is working well and what could be improved?"
"What emotions or mood does this image convey?"
"Compare this design to Material Design principles"
For OCR/Text Extraction
"Extract all text from this image"
"Read the error message in this screenshot"
"What does the label say in this image?"
Examples
Error Analysis
understand_image({
  prompt: "What is the error message and where is it located in this screenshot?",
  image_url: "./error-screenshot.png"
})

Code Screenshot
understand_image({
  prompt: "What code is shown in this screenshot? Please transcribe it exactly.",
  image_url: "https://example.com/code.png"
})

Design Review
understand_image({
  prompt: "Analyze this UI design. What is working well and what could be improved?",
  image_url: "https://example.com/mockup.png"
})

OCR
understand_image({
  prompt: "Extract all text from this image",
  image_url: "/Users/username/Documents/scan.png"
})

Tips
Be specific in your prompt about what you want to know
Mention format if you need structured output (e.g., "list all elements")
Include context if the image is part of a larger task
For screenshots, specify if you need full-page or just a specific area
Complex analysis may trigger a confirmation prompt (analyze, extract, describe, recognize, transcribe, read)
Error Handling
Status code 1004: Authentication error - check API key and region
Status code 2038: Real-name verification required
Invalid image: File doesn't exist or URL is inaccessible
Unsupported format: Image format not in JPEG, PNG, WebP
Weekly Installs
469
Repository
imsus/pi-extens…plan-mcp
GitHub Stars
12
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail