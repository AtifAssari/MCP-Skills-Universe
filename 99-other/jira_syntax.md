---
title: jira-syntax
url: https://skills.sh/netresearch/jira-skill/jira-syntax
---

# jira-syntax

skills/netresearch/jira-skill/jira-syntax
jira-syntax
Installation
$ npx skills add https://github.com/netresearch/jira-skill --skill jira-syntax
SKILL.md
Jira Syntax

Jira wiki markup syntax, templates, and validation. For API operations, use the jira-communication skill.

Quick Syntax Reference
Jira Syntax	Purpose	NOT this (Markdown)
h2. Title	Heading	## Title
*bold*	Bold	**bold**
_italic_	Italic	*italic*
{{code}}	Inline code	`code`
{code:java}...{code}	Code block	java ```
[text|url]	Link	[text](url)
[PROJ-123]	Issue link	-
[~username]	User mention	@username
* item	Bullet list	- item
# item	Numbered list	1. item
||Header||	Table header	|Header|

See references/jira-syntax-quick-reference.md for complete syntax documentation.

Available Templates
Bug Report

Path: templates/bug-report-template.md

Sections: Environment, Steps to Reproduce, Expected/Actual Behavior, Error Messages, Technical Notes

Feature Request

Path: templates/feature-request-template.md

Sections: Overview, User Stories, Acceptance Criteria, Technical Approach, Success Metrics

Syntax Validation

Run before submitting to Jira:

${CLAUDE_SKILL_DIR}/scripts/validate-jira-syntax.sh path/to/content.txt

Validation Checklist
 Headings: h2. Title (space after period)
 Bold: *text* (single asterisk)
 Code blocks: {code:language}...{code}
 Lists: * for bullets, # for numbers
 Links: [label|url] or [PROJ-123]
 Tables: ||Header|| and |Cell|
 Colors: {color:red}text{color}
 Panels: {panel:title=X}...{panel}
Common Mistakes
❌ Wrong	✅ Correct
## Heading	h2. Heading
**bold**	*bold*
`code`	{{code}}
[text](url)	[text|url]
- bullet	* bullet
h2.Title	h2. Title
Integration with jira-communication Skill

Workflow:

Get template from jira-syntax
Fill content using Jira wiki markup
Validate with ${CLAUDE_SKILL_DIR}/scripts/validate-jira-syntax.sh
Submit via jira-communication skill
References
references/jira-syntax-quick-reference.md - Complete syntax documentation
templates/bug-report-template.md - Bug report template
templates/feature-request-template.md - Feature request template
${CLAUDE_SKILL_DIR}/scripts/validate-jira-syntax.sh - Automated syntax checker
Official Jira Wiki Markup
Weekly Installs
158
Repository
netresearch/jira-skill
GitHub Stars
48
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass