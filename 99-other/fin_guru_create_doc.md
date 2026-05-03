---
title: fin-guru-create-doc
url: https://skills.sh/aojdevstudio/finance-guru/fin-guru-create-doc
---

# fin-guru-create-doc

skills/aojdevstudio/finance-guru/fin-guru-create-doc
fin-guru-create-doc
Installation
$ npx skills add https://github.com/aojdevstudio/finance-guru --skill fin-guru-create-doc
SKILL.md
Document Creation Skill

Create professional financial documents using Finance Guru templates.

Available Templates
Template	Path	Purpose
Analysis Report	{project-root}/fin-guru/templates/analysis-report.md	Research and analysis reports
Buy Ticket	{project-root}/fin-guru/templates/buy-ticket-template.md	Capital deployment authorization
Compliance Memo	{project-root}/fin-guru/templates/compliance-memo.md	Regulatory compliance documentation
Excel Model Spec	{project-root}/fin-guru/templates/excel-model-spec.md	Financial model specifications
Presentation	{project-root}/fin-guru/templates/presentation-format.md	Stakeholder presentations
Onboarding Report	{project-root}/fin-guru/templates/onboarding-report.md	Client onboarding summaries
Workflow
Identify the appropriate template for the document type
Load the template from {project-root}/fin-guru/templates/
Gather required inputs (analysis data, recommendations, metrics)
Generate document with proper YAML frontmatter (date stamp, disclaimer, citations)
Save to fin-guru-private/fin-guru/analysis/ using naming conventions:
Analysis reports: {topic}-{YYYY-MM-DD}.md
Buy tickets: buy-ticket-{YYYY-MM-DD}-{short-descriptor}.md
Strategy docs: {strategy-name}-master-strategy.md
Requirements
All documents MUST include educational-only disclaimer
All sources MUST be cited with timestamps
All documents MUST include YAML frontmatter with date stamp
Follow institutional-grade formatting standards
Weekly Installs
9
Repository
aojdevstudio/fi…nce-guru
GitHub Stars
303
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass