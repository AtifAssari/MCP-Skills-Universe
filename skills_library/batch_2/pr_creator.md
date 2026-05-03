---
title: pr-creator
url: https://skills.sh/google-gemini/gemini-cli/pr-creator
---

# pr-creator

skills/google-gemini/gemini-cli/pr-creator
pr-creator
Installation
$ npx skills add https://github.com/google-gemini/gemini-cli --skill pr-creator
Summary

Guided pull request creation that enforces repository templates and safety standards.

Enforces branch safety with critical checks to prevent commits and pushes to main
Locates and applies repository-specific PR templates from .github/ directories, supporting multiple template variants
Guides description drafting with template structure preservation, checklist completion, and issue linking
Includes preflight validation via npm run preflight to catch build, lint, and test failures before PR creation
Uses gh CLI with temporary files to safely handle multi-line Markdown descriptions and enforce Conventional Commits formatting
SKILL.md
Pull Request Creator

This skill guides the creation of high-quality Pull Requests that adhere to the repository's standards.

Workflow

Follow these steps to create a Pull Request:

Branch Management: CRITICAL: Ensure you are NOT working on the main branch.

Run git branch --show-current.
If the current branch is main, you MUST create and switch to a new descriptive branch:
git checkout -b <new-branch-name>


Commit Changes: Verify that all intended changes are committed.

Run git status to check for unstaged or uncommitted changes.
If there are uncommitted changes, stage and commit them with a descriptive message before proceeding. NEVER commit directly to main.
git add .
git commit -m "type(scope): description"


Locate Template: Search for a pull request template in the repository.

Check .github/pull_request_template.md
Check .github/PULL_REQUEST_TEMPLATE.md
If multiple templates exist (e.g., in .github/PULL_REQUEST_TEMPLATE/), ask the user which one to use or select the most appropriate one based on the context (e.g., bug_fix.md vs feature.md).

Read Template: Read the content of the identified template file.

Draft Description: Create a PR description that strictly follows the template's structure.

Headings: Keep all headings from the template.
Checklists: Review each item. Mark with [x] if completed. If an item is not applicable, leave it unchecked or mark as [ ] (depending on the template's instructions) or remove it if the template allows flexibility (but prefer keeping it unchecked for transparency).
Content: Fill in the sections with clear, concise summaries of your changes.
Related Issues: Link any issues fixed or related to this PR (e.g., "Fixes #123").

Preflight Check: Before creating the PR, run the workspace preflight script to ensure all build, lint, and test checks pass.

npm run preflight


If any checks fail, address the issues before proceeding to create the PR.

Push Branch: Push the current branch to the remote repository. CRITICAL SAFETY RAIL: Double-check your branch name before pushing. NEVER push if the current branch is main.

# Verify current branch is NOT main
git branch --show-current
# Push non-interactively
git push -u origin HEAD


Create PR: Use the gh CLI to create the PR. To avoid shell escaping issues with multi-line Markdown, write the description to a temporary file first.

# 1. Write the drafted description to a temporary file
# 2. Create the PR using the --body-file flag
gh pr create --title "type(scope): succinct description" --body-file <temp_file_path>
# 3. Remove the temporary file
rm <temp_file_path>

Title: Ensure the title follows the Conventional Commits format if the repository uses it (e.g., feat(ui): add new button, fix(core): resolve crash).
Principles
Safety First: NEVER push to main. This is your highest priority.
Compliance: Never ignore the PR template. It exists for a reason.
Completeness: Fill out all relevant sections.
Accuracy: Don't check boxes for tasks you haven't done.
Weekly Installs
1.6K
Repository
google-gemini/gemini-cli
GitHub Stars
103.0K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass