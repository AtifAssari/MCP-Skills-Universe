---
rating: ⭐⭐
title: create-github-pull-request-from-specification
url: https://skills.sh/github/awesome-copilot/create-github-pull-request-from-specification
---

# create-github-pull-request-from-specification

skills/github/awesome-copilot/create-github-pull-request-from-specification
create-github-pull-request-from-specification
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill create-github-pull-request-from-specification
Summary

Automated GitHub pull request creation from specification templates with draft-to-review workflow.

Reads pull request template from .github/pull_request_template.md and extracts requirements to populate PR body and title
Checks for existing pull requests on the target branch before creation to prevent duplicates
Progresses pull requests from draft status to ready for review, then auto-assigns to the creator
Analyzes PR diffs to ensure specification changes are properly documented in the pull request description
SKILL.md
Create GitHub Pull Request from Specification

Create GitHub Pull Request for the specification at ${workspaceFolder}/.github/pull_request_template.md .

Process
Analyze specification file template from '${workspaceFolder}/.github/pull_request_template.md' to extract requirements by 'search' tool.
Create pull request draft template by using 'create_pull_request' tool on to ${input:targetBranch}. and make sure don't have any pull request of current branch was exist get_pull_request. If has continue to step 4, and skip step 3.
Get changes in pull request by using 'get_pull_request_diff' tool to analyze information that was changed in pull Request.
Update the pull request body and title created in the previous step using the 'update_pull_request' tool. Incorporate the information from the template obtained in the first step to update the body and title as needed.
Switch from draft to ready for review by using 'update_pull_request' tool. To update state of pull request.
Using 'get_me' to get username of person was created pull request and assign to update_issue tool. To assign pull request
Response URL Pull request was create to user.
Requirements
Single pull request for the complete specification
Clear title/pull_request_template.md identifying the specification
Fill enough information into pull_request_template.md
Verify against existing pull requests before creation
Weekly Installs
8.8K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass