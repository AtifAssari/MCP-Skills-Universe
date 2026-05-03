---
title: suggest-awesome-github-copilot-prompts
url: https://skills.sh/github/awesome-copilot/suggest-awesome-github-copilot-prompts
---

# suggest-awesome-github-copilot-prompts

skills/github/awesome-copilot/suggest-awesome-github-copilot-prompts
suggest-awesome-github-copilot-prompts
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill suggest-awesome-github-copilot-prompts
SKILL.md
Suggest Awesome GitHub Copilot Prompts

Analyze current repository context and suggest relevant prompt files from the GitHub awesome-copilot repository that are not already available in this repository.

Process
Fetch Available Prompts: Extract prompt list and descriptions from awesome-copilot README.prompts.md. Must use #fetch tool.
Scan Local Prompts: Discover existing prompt files in .github/prompts/ folder
Extract Descriptions: Read front matter from local prompt files to get descriptions
Fetch Remote Versions: For each local prompt, fetch the corresponding version from awesome-copilot repository using raw GitHub URLs (e.g., https://raw.githubusercontent.com/github/awesome-copilot/main/prompts/<filename>)
Compare Versions: Compare local prompt content with remote versions to identify:
Prompts that are up-to-date (exact match)
Prompts that are outdated (content differs)
Key differences in outdated prompts (tools, description, content)
Analyze Context: Review chat history, repository files, and current project needs
Compare Existing: Check against prompts already available in this repository
Match Relevance: Compare available prompts against identified patterns and requirements
Present Options: Display relevant prompts with descriptions, rationale, and availability status including outdated prompts
Validate: Ensure suggested prompts would add value not already covered by existing prompts
Output: Provide structured table with suggestions, descriptions, and links to both awesome-copilot prompts and similar local prompts AWAIT user request to proceed with installation or updates of specific prompts. DO NOT INSTALL OR UPDATE UNLESS DIRECTED TO DO SO.
Download/Update Assets: For requested prompts, automatically:
Download new prompts to .github/prompts/ folder
Update outdated prompts by replacing with latest version from awesome-copilot
Do NOT adjust content of the files
Use #fetch tool to download assets, but may use curl using #runInTerminal tool to ensure all content is retrieved
Use #todos tool to track progress
Context Analysis Criteria

🔍 Repository Patterns:

Programming languages used (.cs, .js, .py, etc.)
Framework indicators (ASP.NET, React, Azure, etc.)
Project types (web apps, APIs, libraries, tools)
Documentation needs (README, specs, ADRs)

🗨️ Chat History Context:

Recent discussions and pain points
Feature requests or implementation needs
Code review patterns
Development workflow requirements
Output Format

Display analysis results in structured table comparing awesome-copilot prompts with existing repository prompts:

Awesome-Copilot Prompt	Description	Already Installed	Similar Local Prompt	Suggestion Rationale
code-review.prompt.md	Automated code review prompts	❌ No	None	Would enhance development workflow with standardized code review processes
documentation.prompt.md	Generate project documentation	✅ Yes	create_oo_component_documentation.prompt.md	Already covered by existing documentation prompts
debugging.prompt.md	Debug assistance prompts	⚠️ Outdated	debugging.prompt.md	Tools configuration differs: remote uses 'codebase' vs local missing - Update recommended
Local Prompts Discovery Process
List all *.prompt.md files in .github/prompts/ directory
For each discovered file, read front matter to extract description
Build comprehensive inventory of existing prompts
Use this inventory to avoid suggesting duplicates
Version Comparison Process
For each local prompt file, construct the raw GitHub URL to fetch the remote version:
Pattern: https://raw.githubusercontent.com/github/awesome-copilot/main/prompts/<filename>
Fetch the remote version using the #fetch tool
Compare entire file content (including front matter and body)
Identify specific differences:
Front matter changes (description, tools, mode)
Tools array modifications (added, removed, or renamed tools)
Content updates (instructions, examples, guidelines)
Document key differences for outdated prompts
Calculate similarity to determine if update is needed
Requirements
Use githubRepo tool to get content from awesome-copilot repository prompts folder
Scan local file system for existing prompts in .github/prompts/ directory
Read YAML front matter from local prompt files to extract descriptions
Compare local prompts with remote versions to detect outdated prompts
Compare against existing prompts in this repository to avoid duplicates
Focus on gaps in current prompt library coverage
Validate that suggested prompts align with repository's purpose and standards
Provide clear rationale for each suggestion
Include links to both awesome-copilot prompts and similar local prompts
Clearly identify outdated prompts with specific differences noted
Don't provide any additional information or context beyond the table and the analysis
Icons Reference
✅ Already installed and up-to-date
⚠️ Installed but outdated (update available)
❌ Not installed in repo
Update Handling

When outdated prompts are identified:

Include them in the output table with ⚠️ status
Document specific differences in the "Suggestion Rationale" column
Provide recommendation to update with key changes noted
When user requests update, replace entire local file with remote version
Preserve file location in .github/prompts/ directory
Weekly Installs
6.8K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn