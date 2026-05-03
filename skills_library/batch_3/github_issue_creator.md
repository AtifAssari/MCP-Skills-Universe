---
title: github-issue-creator
url: https://skills.sh/google-gemini/gemini-cli/github-issue-creator
---

# github-issue-creator

skills/google-gemini/gemini-cli/github-issue-creator
github-issue-creator
Installation
$ npx skills add https://github.com/google-gemini/gemini-cli --skill github-issue-creator
SKILL.md
GitHub Issue Creator

This skill guides the creation of high-quality GitHub issues that adhere to the repository's standards and use the appropriate templates.

Workflow

Follow these steps to create a GitHub issue:

Identify Issue Type: Determine if the request is a bug report, feature request, or other category.

Locate Template: Search for issue templates in .github/ISSUE_TEMPLATE/.

bug_report.yml
feature_request.yml
website_issue.yml
If no relevant YAML template is found, look for .md templates in the same directory.

Read Template: Read the content of the identified template file to understand the required fields.

Draft Content: Draft the issue title and body/fields.

If using a YAML template (form), prepare values for each id defined in the template.
If using a Markdown template, follow its structure exactly.
Default Label: Always include the 🔒 maintainer only label unless the user explicitly requests otherwise.

Create Issue: Use the gh CLI to create the issue.

CRITICAL: To avoid shell escaping and formatting issues with multi-line Markdown or complex text, ALWAYS write the description/body to a temporary file first.

For Markdown Templates or Simple Body:

# 1. Write the drafted content to a temporary file
# 2. Create the issue using the --body-file flag
gh issue create --title "Succinct title" --body-file <temp_file_path> --label "🔒 maintainer only"
# 3. Remove the temporary file
rm <temp_file_path>


For YAML Templates (Forms): While gh issue create supports --body-file, YAML forms usually expect key-value pairs via flags if you want to bypass the interactive prompt. However, the most reliable non-interactive way to ensure formatting is preserved for long text fields is to use the --body or --body-file if the form has been converted to a standard body, OR to use the --field flags for YAML forms.

Note: For the gemini-cli repository which uses YAML forms, you can often submit the content as a single body if a specific field-based submission is not required by the automation.

Verify: Confirm the issue was created successfully and provide the link to the user.

Principles
Clarity: Titles should be descriptive and follow project conventions.
Defensive Formatting: Always use temporary files with --body-file to prevent newline and special character issues.
Maintainer Priority: Default to internal/maintainer labels to keep the backlog organized.
Completeness: Provide all requested information (e.g., version info, reproduction steps).
Weekly Installs
504
Repository
google-gemini/gemini-cli
GitHub Stars
103.0K
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass