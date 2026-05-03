---
rating: ⭐⭐⭐
title: md-slides
url: https://skills.sh/claude-office-skills/skills/md-slides
---

# md-slides

skills/claude-office-skills/skills/md-slides
md-slides
Installation
$ npx skills add https://github.com/claude-office-skills/skills --skill md-slides
SKILL.md
Markdown Slides Skill
Overview

This skill enables creation of presentations from pure Markdown using Marp. Write slides in familiar Markdown syntax and export to PDF, PPTX, or HTML with professional themes.

How to Use
Write or provide Markdown content
I'll format it for Marp with proper directives
Export to your preferred format (PDF/PPTX/HTML)

Example prompts:

"Convert my notes to a presentation"
"Create slides from this markdown"
"Build a pitch deck using markdown"
"Generate PDF slides from this outline"
Domain Knowledge
Basic Syntax
---
marp: true
---

# First Slide

Content here

---

# Second Slide

- Bullet 1
- Bullet 2

Themes
---
marp: true
theme: default  # default, gaia, uncover
---

Directives
---
marp: true
theme: gaia
class: lead        # Centered title
paginate: true     # Page numbers
header: 'Header'   # Header text
footer: 'Footer'   # Footer text
backgroundColor: #fff
---

Images
![width:500px](image.png)
![bg](background.jpg)
![bg left:40%](sidebar.jpg)

Columns
<div class="columns">
<div>

## Left

Content

</div>
<div>

## Right

Content

</div>
</div>

Example
---
marp: true
theme: gaia
paginate: true
---

<!-- _class: lead -->

# Project Update

Q4 2024 Review

---

# Highlights

- Revenue: +25%
- Users: +50%
- NPS: 72

---

# Roadmap

| Q1 | Q2 | Q3 | Q4 |
|----|----|----|-----|
| MVP | Beta | Launch | Scale |

---

<!-- _class: lead -->

# Thank You!

questions@company.com

CLI Usage
# Install
npm install -g @marp-team/marp-cli

# Convert
marp slides.md -o presentation.pdf
marp slides.md -o presentation.pptx
marp slides.md -o presentation.html

Resources
Marp Documentation
GitHub
Weekly Installs
738
Repository
claude-office-s…s/skills
GitHub Stars
94
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass