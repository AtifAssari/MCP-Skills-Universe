---
rating: ⭐⭐
title: lovstudio:fill-form
url: https://skills.sh/lovstudio/skills/lovstudio:fill-form
---

# lovstudio:fill-form

skills/lovstudio/skills/lovstudio:fill-form
lovstudio:fill-form
Installation
$ npx skills add https://github.com/lovstudio/skills --skill lovstudio:fill-form
SKILL.md
fill-form — Fill Word Form Templates

This skill fills in Word document form templates (.docx) with user-provided data. It detects table-based form fields (label in one cell, value in the adjacent cell) and populates them automatically.

When to Use
User has a .docx form template with blank fields to fill
User wants to fill in an application form, registration form, etc.
Document uses Word tables for form layout (label | value cell pairs)
User mentions 填表, 申请表, 登记表, or wants to automate form filling
Workflow (MANDATORY)

You MUST follow these steps in order:

Step 1: Scan the template

Discover all fillable fields:

python lovstudio-fill-form/scripts/fill_form.py --template <path> --scan

Step 2: Pre-fill from known context

Before asking the user, try to fill as many fields as possible from:

User memory — name, title, organization, etc.
Context files — if the user provides reference documents (e.g. STARTER-PROMPT.md, project docs), extract relevant info to fill content-heavy fields
Conversation context — anything already mentioned

For content-heavy fields (e.g. "主要内容/简介/摘要"), actively compose the content by synthesizing from context files, user's known expertise, and the topic/title.

Step 3: Ask only what you don't know

Use AskUserQuestion to collect ONLY the fields you cannot fill from context.

Group fields into a single question
If ALL fields are unknown, list them all
If the user says some fields can be left blank (e.g. "其他朋友会帮我填"), respect that and leave those empty
Do NOT force the user to provide every field
Step 4: Fill and save

Write a JSON data file (avoids shell escaping issues with long text), then run:

python lovstudio-fill-form/scripts/fill_form.py \
  --template <path> \
  --data-file /tmp/form_data.json


Output path rules:

Default: <template_dir>/<name>_filled.docx (same directory as the template)
If the template is in a temp directory or system path, save to user's document directory or ask the user where to save
Use --output to override explicitly
CLI Reference
Argument	Default	Description
--template	(required)	Path to template .doc/.docx file
--output	<template_dir>/<name>_filled.docx	Output .docx path
--scan	false	List all detected form fields
--data	""	JSON string with field→value mapping
--data-file	""	Path to JSON file with field→value mapping
--font	Platform CJK serif	Font name for filled text
--font-size	11	Font size in points
How Field Detection Works
Table-based (primary): Scans all tables for rows with label→value cell pairs. A label cell contains short text (CJK or Latin); the adjacent cell is the value field.
Merged rows: Detects full-width merged cells with "Label：" pattern as large text areas.
Paragraph fallback: If no tables found, detects "Label：value" patterns in paragraphs.
Limitations
.doc files are auto-converted to .docx via macOS textutil, which loses table structure. For best results, use .docx templates directly. If you only have .doc, convert with LibreOffice first: libreoffice --headless --convert-to docx file.doc
Fields are matched by normalized label text (whitespace removed). If a label contains unusual formatting, the match may fail — use --scan to verify detection.
Dependencies
pip install python-docx --break-system-packages

Weekly Installs
59
Repository
lovstudio/skills
GitHub Stars
45
First Seen
10 days ago