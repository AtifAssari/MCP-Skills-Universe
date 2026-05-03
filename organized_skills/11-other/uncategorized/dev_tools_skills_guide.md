---
rating: ⭐⭐⭐
title: dev-tools-skills-guide
url: https://skills.sh/gmh5225/awesome-skills/dev-tools-skills-guide
---

# dev-tools-skills-guide

skills/gmh5225/awesome-skills/dev-tools-skills-guide
dev-tools-skills-guide
Installation
$ npx skills add https://github.com/gmh5225/awesome-skills --skill dev-tools-skills-guide
SKILL.md
Development & Code Tools Skills
Scope

Use this skill when:

Finding or adding development tool skills
Understanding document processing capabilities
Working with browser automation and testing
Organizing IDE and editor integrations
Document Processing Skills
Office Documents
Format	Skill	Capabilities
DOCX	anthropics/docx	Create, edit, track changes, comments
XLSX	anthropics/xlsx	Formulas, charts, data transformations
PPTX	anthropics/pptx	Slides, layouts, templates
PDF	anthropics/pdf	Extract, merge, annotate, forms
Other Formats
Format	Skill	Capabilities
EPUB	claude-epub-skill	Markdown to ebook conversion
Reveal.js	revealjs-skill	HTML presentations
Translation
Format	Skill	Capabilities
EPUB	epub-translator	Multi-language EPUB translation with parallel processing
PDF	pdf-translator	PDF translation with layout preservation, Markdown/PDF output
Browser Automation
Tool	Skill	Use Case
Playwright	playwright-skill	E2E testing, web scraping
Puppeteer	browser-automation	Chrome automation
iOS Simulator	ios-simulator-skill	iOS app testing
Testing Frameworks
Category	Skills
TDD	test-driven-development, test-fixing
Property Testing	pypict-claude-skill (PICT)
Web Testing	webapp-testing (Playwright)
Fuzzing	ffuf_claude_skill (web fuzzing)
Code Quality
Category	Skills
Move Language	move-code-quality-skill
Solana	solana-dev-skill
Git Workflows	git-pushing, using-git-worktrees
Visualization
Tool	Skill
D3.js	claude-d3js-skill
Three.js	3d-web-experience
Where to Add in README
Document tools: Document Processing
Browser automation: Development & Code Tools
Testing tools: Development & Code Tools or Collaboration & Project Management
Visualization: Development & Code Tools
Key Skill Repositories
Official (Anthropic)
anthropics/skills/
├── docx/
├── xlsx/
├── pptx/
├── pdf/
├── webapp-testing/
└── web-artifacts-builder/

Community
obra/superpowers/skills/
├── test-driven-development/
├── test-fixing/
├── using-git-worktrees/
├── finishing-a-development-branch/
└── systematic-debugging/

Translation (Nebu1eto/skills)
Nebu1eto/skills/
├── epub-translator/    # EPUB multi-language translation
└── pdf-translator/     # PDF translation with layout preservation

Integration Patterns
IDE Integration
IDE	Skill Path
VS Code	.github/skills/ or .vscode/skills/
Cursor	.cursor/skills/
CI/CD Integration
Use skills with GitHub Actions
Automate testing workflows
Generate changelogs from commits
Best Practices
Atomic operations: One skill per focused task
Error handling: Include recovery strategies
Logging: Provide debug output options
Dependencies: Document required tools/packages
Examples: Include real-world usage examples
Full Resource List

For more detailed dev tools skill resources, complete link lists, or the latest information, use WebFetch to retrieve the full README.md:

https://raw.githubusercontent.com/gmh5225/awesome-skills/refs/heads/main/README.md


The README.md contains the complete categorized resource list with all links.

Weekly Installs
21
Repository
gmh5225/awesome-skills
GitHub Stars
31
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn