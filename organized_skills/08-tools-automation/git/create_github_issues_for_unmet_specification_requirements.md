---
rating: ⭐⭐
title: create-github-issues-for-unmet-specification-requirements
url: https://skills.sh/github/awesome-copilot/create-github-issues-for-unmet-specification-requirements
---

# create-github-issues-for-unmet-specification-requirements

skills/github/awesome-copilot/create-github-issues-for-unmet-specification-requirements
create-github-issues-for-unmet-specification-requirements
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill create-github-issues-for-unmet-specification-requirements
Summary

Automatically create GitHub issues for specification requirements not yet implemented in code.

Analyzes specification files to extract all requirements, then checks codebase implementation status for each one
Searches existing issues to prevent duplicates before creating new feature request issues
Generates issues with requirement IDs, detailed descriptions, implementation guidance, and acceptance criteria
Scans related specification files and code patterns to verify whether requirements are partially or fully implemented
SKILL.md
Create GitHub Issues for Unmet Specification Requirements

Create GitHub Issues for unimplemented requirements in the specification at ${file}.

Process
Analyze specification file to extract all requirements
Check codebase implementation status for each requirement
Search existing issues using search_issues to avoid duplicates
Create new issue per unimplemented requirement using create_issue
Use feature_request.yml template (fallback to default)
Requirements
One issue per unimplemented requirement from specification
Clear requirement ID and description mapping
Include implementation guidance and acceptance criteria
Verify against existing issues before creation
Issue Content
Title: Requirement ID and brief description
Description: Detailed requirement, implementation method, and context
Labels: feature, enhancement (as appropriate)
Implementation Check
Search codebase for related code patterns
Check related specification files in /spec/ directory
Verify requirement isn't partially implemented
Weekly Installs
8.4K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass