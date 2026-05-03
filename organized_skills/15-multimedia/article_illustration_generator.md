---
rating: ⭐⭐
title: article-illustration-generator
url: https://skills.sh/2898117012/agent-skills/article-illustration-generator
---

# article-illustration-generator

skills/2898117012/agent-skills/article-illustration-generator
article-illustration-generator
Installation
$ npx skills add https://github.com/2898117012/agent-skills --skill article-illustration-generator
SKILL.md
Article Illustration Generator

This skill automatically generates relevant illustrations for a text article using the Gemini Image API and converts it into a visually appealing HTML file.

Workflow

API Key Check:

First, check if the GOOGLE_API_KEY environment variable is set.
If not set, use the AskUserQuestion tool to ask the user if they have configured their API key.
If the user hasn't configured it, ask them to provide their Google API key.
Store the API key for use in the script execution.

Input Analysis:

Read the user's article text.
Split the text into logical sections (paragraphs).
Identify key scenes for illustration (aim for 1 image every 2-3 paragraphs).

Image Generation:

For each identified scene, generate a descriptive prompt based on the text context.
Use the google.genai SDK to generate images.
Model: gemini-2.5-flash-image (default, or user specified).
Config: Use aspect_ratio="16:9" or 4:3 for article images.

HTML Construction:

Use the HTML template provided in assets/template.html ("故都的秋" style).
Insert the text and generated images (saved locally) into the HTML structure.
Resources

This skill includes reference files in the references/ directory:

references/template.html: The HTML/CSS template with serif fonts and clean layout. Use this as the base for the output file.
references/api_guide.md: Detailed documentation for the Nano Banana Pro (Gemini 3 Pro Image) API, which can be used for advanced image generation needs.
references/script_template.py: A Python script template containing the API calling logic.
Usage Guide

When invoked, the agent should:

Check API Key Configuration:

Use Bash to check if GOOGLE_API_KEY environment variable is set: echo $GOOGLE_API_KEY (Linux/Mac) or echo %GOOGLE_API_KEY% (Windows).
If empty or not set, use AskUserQuestion to ask: "您是否已经配置了 Google API Key？"
Option 1: "是，已配置为环境变量" - Proceed with the script.
Option 2: "否，我需要提供 API Key" - Ask for the API key and pass it as a command-line argument to the script.
If the user provides an API key, store it temporarily for this execution.

Read the target article provided by the user.

Plan the image insertion points.

Execute the Python script (scripts/article_to_html.py) with appropriate parameters:

If API key was provided by user: python scripts/article_to_html.py <article_file> <api_key>
If using environment variable: python scripts/article_to_html.py <article_file>
Optional parameters: --images N, --model MODEL, --ratio RATIO, --size SIZE

Verify the result and inform the user of the output location.

Weekly Installs
35
Repository
2898117012/agent-skills
First Seen
Feb 10, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail